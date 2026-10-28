"""Selective routing: ground only where entities are the answer.

Session 5 showed grounding hurts general questions (eval-025: entity
checks crowded out the general doc) while session 4 showed single-pass
guessing works well overall. So route by question form: questions that
ask which/who/what-company (entity-seeking) go down the grounded path
(two_stage); everything else uses single-pass decomposition (decompose).
The router is rule-based and deterministic — no LLM call, no new
nondeterminism — so the routing decision itself is reproducible.
"""

import re

from decompose import decompose
from two_stage import two_stage_sub_questions

_GROUNDED_PATTERNS = [
    re.compile(r"\bwhich\b"),
    re.compile(r"\bwho\b"),
    re.compile(r"\bwhat company\b"),
    re.compile(r"\bwhat organization\b"),
    re.compile(r"\bwhat organisation\b"),
]


def needs_grounding(question):
    """True when the question seeks an entity (which/who/what-company)."""
    q = question.lower()
    return any(p.search(q) for p in _GROUNDED_PATTERNS)


def selective_sub_questions(question, db="chroma_db", mode="vector", max_per_doc=1, keyword_filter=False):
    """Dispatch: grounded path for entity-seeking questions, else single-pass.

    Returns the two_stage info dict plus a "routed" field ("grounded" or
    "auto"). Auto questions carry empty stage-1/filter fields.
    """
    if needs_grounding(question):
        info = two_stage_sub_questions(question, db=db, mode=mode, max_per_doc=max_per_doc, keyword_filter=keyword_filter)
        info["routed"] = "grounded"
        return info
    return {
        "sub_questions": decompose(question),
        "stage1_doc_ids": [],
        "dropped_entities": [],
        "fallback": False,
        "routed": "auto",
    }
