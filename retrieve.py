"""Hybrid retrieval over the ingested corpus.

Two rankers, one fused result:
1. Vector search (Chroma, semantic similarity)
2. Keyword search (query-term overlap — catches exact names and terms
   that embeddings sometimes blur)

Fusion uses Reciprocal Rank Fusion (RRF): each ranker votes
1 / (60 + rank) for its picks, and chunks are ordered by total votes.
RRF needs no score normalization, which is why it works when the two
rankers' raw scores live on totally different scales.

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


def retrieve(query, k=5, db="chroma_db"):
    """Return the top-k chunks for a query as dicts with id, score,
    title, doc_id, chunk_index, and text."""
    client = chromadb.PersistentClient(path=db)
    collection = client.get_or_create_collection(COLLECTION)

    # Ranker 1: vector search.
    vec = collection.query(query_texts=[query], n_results=2 * k)
    vector_ranking = vec["ids"][0] if vec["ids"] else []

    # Ranker 2: keyword overlap over all chunks.
    all_docs = collection.get()
    docs = list(zip(all_docs["ids"], all_docs["documents"]))
    keyword_ranking = keyword_rank(docs, query_terms(query))

    fused = rrf_fuse([vector_ranking, keyword_ranking])[:k]

    wanted = [doc_id for doc_id, _ in fused]
    got = collection.get(ids=wanted) if wanted else {"ids": [], "documents": [], "metadatas": []}
    by_id = {i: (d, m) for i, d, m in zip(got["ids"], got["documents"], got["metadatas"])}
    results = []
    for doc_id, score in fused:
        if doc_id not in by_id:
            continue
        text, meta = by_id[doc_id]
        results.append({"id": doc_id, "score": round(score, 4), **meta, "text": text})
    return results


def main():
    parser = argparse.ArgumentParser(description="Hybrid retrieval over the corpus.")
    parser.add_argument("query")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--db", default="chroma_db")
    args = parser.parse_args()

    results = retrieve(args.query, k=args.k, db=args.db)
    if not results:
        print("No matches.")
        return
    for rank, r in enumerate(results, start=1):
        print(f"\n[{rank}] {r['title']} (chunk {r['chunk_index']}, score {r['score']})")
        print(r["text"][:400].replace("\n", " "))


if __name__ == "__main__":
    main()
