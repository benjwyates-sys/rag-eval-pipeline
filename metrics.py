"""Pure retrieval metrics. No I/O, no models — easy to unit-test.

Inputs are per-question lists of retrieved doc_ids (in rank order) and
sets of gold doc_ids. Unanswerable questions are excluded upstream.
"""


def hit_rate_at_k(retrieved_docs_list, gold_sets, k):
    """Fraction of questions with at least one gold doc in the top-k."""
    if not retrieved_docs_list:
        return 0.0
    hits = sum(
        1
        for docs, gold in zip(retrieved_docs_list, gold_sets)
        if gold & set(docs[:k])
    )
    return hits / len(retrieved_docs_list)


def mean_reciprocal_rank(retrieved_docs_list, gold_sets):
    """Mean of 1/rank of the first gold doc hit (0 when there is none)."""
    if not retrieved_docs_list:
        return 0.0
    total = 0.0
    for docs, gold in zip(retrieved_docs_list, gold_sets):
        for rank, doc_id in enumerate(docs, start=1):
            if doc_id in gold:
                total += 1.0 / rank
                break
    return total / len(retrieved_docs_list)
