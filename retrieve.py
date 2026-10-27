"""Retrieval over the ingested corpus.

Default: pure vector search (Chroma, semantic similarity) with max 1
chunk per doc — the session 3 champion. Hybrid mode is also available:
vector + keyword search fused with Reciprocal Rank Fusion (RRF), where
each ranker votes 1 / (60 + rank) for its picks. RRF needs no score
normalization, which is why it works when the two rankers' raw scores
live on totally different scales.

Run:  uv run python retrieve.py "what is lidar" --k 5
"""

import argparse
import re

import chromadb

COLLECTION = "rag-eval-lab"
RRF_K = 60

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "with",
    "is", "are", "was", "were", "what", "how", "why", "when", "which",
    "does", "do", "did", "by", "at", "from", "as", "it", "its",
}


def query_terms(query):
    terms = re.findall(r"[a-z0-9]+", query.lower())
    return [t for t in terms if t not in STOPWORDS]


def keyword_rank(documents, terms):
    """Rank chunks by how many distinct query terms each contains.
    At this scale (hundreds of chunks) scanning all of them is fine;
    at larger scale this is where an inverted index would go."""
    scored = []
    for doc_id, text in documents:
        hay = set(re.findall(r"[a-z0-9]+", text.lower()))
        score = sum(1 for t in terms if t in hay)
        scored.append((score, doc_id))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [doc_id for score, doc_id in scored if score > 0]


def rrf_fuse(rankings, k=RRF_K):
    fused = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            fused[doc_id] = fused.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(fused.items(), key=lambda x: -x[1])


def retrieve(query, k=5, db="chroma_db", mode="vector", max_per_doc=1):
    """Return the top-k chunks for a query as dicts with id, score,
    title, doc_id, chunk_index, and text.

    mode="vector" (default) is pure vector search — the session 3
    champion. mode="hybrid" fuses vector + keyword rankings with RRF.
    max_per_doc caps how many chunks a single doc may contribute to
    the top-k (doc-diversity ablation; default 1).
    """
    client = chromadb.PersistentClient(path=db)
    collection = client.get_or_create_collection(COLLECTION)

    # Ranker 1: vector search (over-retrieve so a diversity cap still
    # leaves enough candidates to fill k).
    vec = collection.query(query_texts=[query], n_results=2 * k)
    vector_ids = vec["ids"][0] if vec["ids"] else []
    vector_dists = vec["distances"][0] if vec.get("distances") and vec["distances"] else [None] * len(vector_ids)

    if mode == "vector":
        ranked = list(zip(vector_ids, vector_dists))
    else:
        # Ranker 2: keyword overlap over all chunks.
        all_docs = collection.get()
        docs = list(zip(all_docs["ids"], all_docs["documents"]))
        keyword_ranking = keyword_rank(docs, query_terms(query))
        ranked = rrf_fuse([vector_ids, keyword_ranking])

    # Diversity cap: walk the ranking in order, keeping at most
    # max_per_doc chunks per doc. Chunk ids are "doc_id#chunk_index".
    if max_per_doc is not None:
        counts = {}
        capped = []
        for chunk_id, score in ranked:
            doc = chunk_id.rsplit("#", 1)[0]
            if counts.get(doc, 0) >= max_per_doc:
                continue
            counts[doc] = counts.get(doc, 0) + 1
            capped.append((chunk_id, score))
        ranked = capped

    wanted = [chunk_id for chunk_id, _ in ranked[:k]]
    got = collection.get(ids=wanted) if wanted else {"ids": [], "documents": [], "metadatas": []}
    by_id = {i: (d, m) for i, d, m in zip(got["ids"], got["documents"], got["metadatas"])}
    results = []
    for chunk_id, score in ranked[:k]:
        if chunk_id not in by_id:
            continue
        text, meta = by_id[chunk_id]
        results.append({"id": chunk_id, "score": round(score, 4) if score is not None else None, **meta, "text": text})
    return results


def main():
    parser = argparse.ArgumentParser(description="Hybrid retrieval over the corpus.")
    parser.add_argument("query")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--db", default="chroma_db")
    parser.add_argument("--mode", choices=["hybrid", "vector"], default="vector")
    parser.add_argument("--max-per-doc", type=int, default=1)
    args = parser.parse_args()

    results = retrieve(args.query, k=args.k, db=args.db, mode=args.mode, max_per_doc=args.max_per_doc)
    if not results:
        print("No matches.")
        return
    for rank, r in enumerate(results, start=1):
        print(f"\n[{rank}] {r['title']} (chunk {r['chunk_index']}, score {r['score']})")
        print(r["text"][:400].replace("\n", " "))


if __name__ == "__main__":
    main()