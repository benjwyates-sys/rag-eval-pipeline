"""Two-stage retrieval: retrieve first, then guess from what exists.

Session 4's single-pass guesser had one specific failure mode: it guessed
entities from its own knowledge without ever seeing the corpus, so it
could land in the wrong domain ('AV' read as antivirus → McAfee and
NortonLifeLock, neither in the corpus). This module grounds guessing in
retrieved evidence:

Stage 1: broad vector retrieval on the original question (k=10, max 1
chunk per doc) — candidate docs from the corpus itself, not the model.
Stage 2: the LLM reads those candidates (title + first 500 chars of each
chunk) and proposes entities that appear in them, one verification
sub-question per entity. It may only propose entities it sees in the
candidates; if none is relevant, it returns the original question.
Stage 2.5 (optional, --keyword-filter): drop any proposed entity that
appears in none of the stage-1 candidate chunks. Vector search always
returns something; a candidate-scope existence check returns nothing
when the entity isn't there, which is the clean rejection signal for
wrong-domain guesses. The check is scoped to the candidates, not the
whole corpus: its job is catching inventions, not re-judging relevance.

Any LLM failure warns loudly (once) and falls back to the original
question as a single retrieval — never silently, never crashing the run
(the session 4 lesson).
"""

import json
import re
import sys

from decompose import MODEL, llm_available
from retrieve import retrieve

STAGE1_K = 10
SNIPPET_CHARS = 500

_GROUNDED_SYSTEM = (
    "You turn a research question into retrieval sub-questions, using "
    "ONLY the candidate documents provided below the question. Reply with "
    "a JSON list of objects only, no other text, no markdown code fences. Each object has two "
    "fields: \"entity\" — the main subject of the sub-question (a company, "
    "person, vehicle, technology, or standard named in the candidate "
    "documents), or null if the sub-question has no such subject — and "
    "\"sub_question\" — one verification sub-question naming that entity "
    "explicitly (e.g. {\"entity\": \"Pixar\", \"sub_question\": \"Which company "
    "acquired Pixar?\"}). Rules: propose ONLY entities that appear in the "
    "candidate documents — never guess entities from your own knowledge. "
    "If the question asks which, who, or what company or organization is "
    "involved, propose the relevant entities from the documents, one object "
    "per entity. Otherwise, split the question into self-contained "
    "sub-questions, each naming its subject explicitly. If the question "
    "needs no splitting, return one object with the original question as "
    "the sub_question and entity null. Do not answer the questions, only "
    "split or ground them."
)


def _parse_json_list(text):
    """Parse the LLM's JSON list, tolerating markdown fences and prose.

    The model often wraps JSON in ```json fences despite being told not
    to; a bare json.loads then fails at char 0 with no clue what the
    model actually returned. Strip fences, and if that fails, extract the
    first [...] block. The error message carries the raw head so the next
    failure is diagnosable instead of mysterious.
    """
    raw = text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
    raise ValueError(f"LLM output was not parseable JSON; raw head: {text[:200]!r}")


def grounded_sub_questions(question, candidates):
    """LLM sub-questions grounded in stage-1 candidates; raises on failure."""
    import openai

    context = "\n".join(
        f"- {c['title']}: {c['text'][:SNIPPET_CHARS]}" for c in candidates
    )
    client = openai.OpenAI()
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": _GROUNDED_SYSTEM},
            {"role": "user", "content": f"Question: {question}\n\nCandidate documents:\n{context}"},
        ],
    )
    parsed = _parse_json_list(resp.choices[0].message.content)
    if not isinstance(parsed, list) or not parsed:
        raise ValueError("LLM did not return a usable list")
    sub_qs, entities = [], []
    for item in parsed:
        if isinstance(item, str) and item.strip():
            sub_qs.append(item.strip())
            entities.append(None)
        elif (
            isinstance(item, dict)
            and isinstance(item.get("sub_question"), str)
            and item["sub_question"].strip()
            and (item.get("entity") is None or isinstance(item.get("entity"), str))
        ):
            sub_qs.append(item["sub_question"].strip())
            entities.append(item.get("entity"))
        else:
            raise ValueError("LLM did not return usable sub-questions")
    return sub_qs, entities


def _appears_in_candidates(entity, candidates):
    needle = entity.lower()
    return any(
        needle in c["title"].lower() or needle in c["text"].lower()
        for c in candidates
    )


def apply_keyword_filter(sub_qs, entities, candidates):
    """Drop sub-questions whose entity appears in no candidate doc.

    Returns (kept_sub_qs, dropped_entities). Items with entity null pass
    through unfiltered — there is nothing to check.
    """
    kept, dropped = [], []
    for sq, ent in zip(sub_qs, entities):
        if ent is not None and not _appears_in_candidates(ent, candidates):
            dropped.append(ent)
        else:
            kept.append(sq)
    return kept, dropped


_warned = False


def two_stage_sub_questions(question, db="chroma_db", mode="vector", max_per_doc=1, keyword_filter=False):
    """Stage 1 retrieve → stage 2 grounded LLM → optional keyword filter.

    Returns a dict with sub_questions, stage1_doc_ids, dropped_entities.
    On any LLM failure, warns loudly (once) and returns the original
    question as the sole sub-question (single-step retrieval).
    """
    global _warned
    candidates = retrieve(question, k=STAGE1_K, db=db, mode=mode, max_per_doc=max_per_doc)
    stage1_docs = [c["doc_id"] for c in candidates]
    if not candidates or not llm_available():
        return {"sub_questions": [question], "stage1_doc_ids": stage1_docs, "dropped_entities": [], "fallback": True}
    try:
        sub_qs, entities = grounded_sub_questions(question, candidates)
    except Exception as e:
        if not _warned:
            print(f"Warning: two-stage LLM grounding failed ({e}); falling back to single-step retrieval.", file=sys.stderr)
            _warned = True
        return {"sub_questions": [question], "stage1_doc_ids": stage1_docs, "dropped_entities": [], "fallback": True}
    dropped = []
    if keyword_filter:
        sub_qs, dropped = apply_keyword_filter(sub_qs, entities, candidates)
        if not sub_qs:
            sub_qs = [question]
    return {"sub_questions": sub_qs, "stage1_doc_ids": stage1_docs, "dropped_entities": dropped, "fallback": False}
