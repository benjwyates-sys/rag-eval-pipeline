"""Automatic query decomposition for multi-hop questions.

The session 3 oracle (evals/decompositions.json) showed that perfect
sub-questions lift retrieval to hit@3 1.000. This module generates those
sub-questions automatically, two ways:

1. LLM (when OPENAI_API_KEY is set and the openai package is installed):
   gpt-4o-mini splits the question into 2-3 self-contained sub-questions.
   It returns sub-questions only, never answers, so retrieval stays
   grounded in the corpus. Sub-questions name the entities/facts the
   question hinges on — the LLM proposes from its own knowledge,
   retrieval verifies against the corpus.
2. Rule-based fallback: split on ';' or ', and' into clauses. This
   handles conjunction splits (eval-012, eval-029) but cannot do entity
   identification (eval-011, eval-028) — that gap is exactly what the
   LLM path is for.

Any LLM failure falls back to the rule-based splitter; decomposition
never crashes a run.
"""

import json
import os
import re
import sys

MODEL = "gpt-4o-mini"

_SYSTEM = (
    "You turn a research question into retrieval sub-questions. "
    "Reply with a JSON list of strings only, no other text. "
    "Rules: if the question asks which, who, or what company or "
    "organization is involved, FIRST guess the most likely candidates "
    "from your own knowledge, then phrase one verification sub-question "
    "per candidate, each naming the candidate explicitly (e.g. 'Which "
    "company acquired Pixar?', 'Which company acquired Marvel?'). "
    "Retrieval will check each guess against the corpus — a wrong guess "
    "is harmless, a missing candidate is fatal. Otherwise, split the "
    "question into 2-3 self-contained sub-questions, each naming its "
    "subject explicitly — never a pronoun referring to another "
    "sub-question, never a fragment. If the question asks about parts of "
    "a single thing, ask one sub-question per part, each naming the whole. "
    "Do not answer the questions, only split or guess them. If the question "
    "needs no splitting, return a list containing just the original question."
)


def llm_available():
    """True when the LLM path can run (key set + package importable)."""
    if not os.environ.get("OPENAI_API_KEY"):
        return False
    try:
        import openai  # noqa: F401
    except ImportError:
        return False
    return True


def decompose_llm(question):
    """Split via LLM; raises on any failure (caller falls back)."""
    import openai

    client = openai.OpenAI()
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": question},
        ],
    )
    sub_qs = json.loads(resp.choices[0].message.content.strip())
    if not isinstance(sub_qs, list) or not sub_qs or not all(isinstance(s, str) and s.strip() for s in sub_qs):
        raise ValueError("LLM did not return a usable list of sub-questions")
    return [s.strip() for s in sub_qs]


def decompose_rule_based(question):
    """Split on ';' or ', and' into clauses; else return [question]."""
    parts = [p.strip() for p in re.split(r"\s*;\s*|\s*,\s+and\s+", question) if p.strip()]
    if len(parts) <= 1:
        return [question]
    cleaned = []
    for p in parts:
        p = p[0].upper() + p[1:] if p else p
        if not p.endswith("?"):
            p += "?"
        cleaned.append(p)
    return cleaned


_warned = False


def decompose(question):
    """Sub-questions for a question: LLM when available, else rules.
    An LLM failure warns loudly (once) instead of silently degrading:
    silent fallback once made three runs look like LLM runs that may
    never have called the model."""
    global _warned
    if llm_available():
        try:
            return decompose_llm(question)
        except Exception as e:
            if not _warned:
                print(f"Warning: LLM decomposition failed ({e}); falling back to rules.", file=sys.stderr)
                _warned = True
    return decompose_rule_based(question)
