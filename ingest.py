"""Ingest the corpus into Chroma.

Reads every Markdown file in data/corpus/, splits each into overlapping
chunks, embeds them with Chroma's built-in local model (no API key needed),
and upserts them into a persistent collection.

Chunk IDs are deterministic (doc_id#chunk_index), so re-running ingest
upserts the same chunks instead of duplicating them.

Run:  uv run python ingest.py [--reset]
"""

import argparse
from pathlib import Path

import chromadb

CHUNK_SIZE = 1000
OVERLAP = 200
COLLECTION = "rag-eval-lab"


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    """Sliding-window character chunks. The overlap keeps sentences that
    straddle a boundary searchable from both sides."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = end - overlap
    return chunks


def chunk_text_words(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    """Word-boundary chunks: same sliding window, but a chunk never ends
    mid-word. Words are accumulated up to chunk_size chars, then the
    window steps forward by (chunk_size - overlap) chars worth of words.
    Whitespace is normalized (words joined by single spaces)."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start
        length = 0
        while end < len(words):
            add = len(words[end]) + (1 if end > start else 0)
            if length + add > chunk_size and end > start:
                break
            length += add
            end += 1
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        # Advance by (chunk_size - overlap) chars worth of words.
        step = chunk_size - overlap
        advanced = 0
        nxt = start
        while nxt < end and advanced < step:
            advanced += len(words[nxt]) + 1
            nxt += 1
        start = max(nxt, start + 1)
    return chunks


def load_doc(path):
    """Return (title, body) for a corpus file, dropping the source footer."""
    text = path.read_text(encoding="utf-8")
    body = text.split("\n---\n", 1)[0]
    title = path.stem
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body = "\n".join(lines[1:]).strip()
    return title, body


def main():
    parser = argparse.ArgumentParser(description="Ingest data/corpus into Chroma.")
    parser.add_argument("--corpus", default="data/corpus")
    parser.add_argument("--db", default="chroma_db")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE)
    parser.add_argument("--overlap", type=int, default=OVERLAP)
    parser.add_argument("--reset", action="store_true",
                        help="Delete the existing collection before ingesting.")
    parser.add_argument("--word-boundary", action="store_true",
                        help="Split chunks at word boundaries instead of mid-word.")
    args = parser.parse_args()

    client = chromadb.PersistentClient(path=args.db)
    if args.reset:
        try:
            client.delete_collection(COLLECTION)
        except Exception:
            pass
    collection = client.get_or_create_collection(COLLECTION)

    corpus_dir = Path(args.corpus)
    files = sorted(corpus_dir.glob("*.md"))
    if not files:
        raise SystemExit(
            f"No .md files found in {corpus_dir}. Run scripts/fetch_corpus.py first."
        )

    ids, documents, metadatas = [], [], []
    for path in files:
        title, body = load_doc(path)
        doc_id = path.stem
        chunker = chunk_text_words if args.word_boundary else chunk_text
        for i, chunk in enumerate(chunker(body, args.chunk_size, args.overlap)):
            ids.append(f"{doc_id}#{i}")
            documents.append(chunk)
            metadatas.append({"doc_id": doc_id, "title": title, "chunk_index": i})

    collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
    print(f"Ingested {len(files)} docs -> {len(ids)} chunks into '{COLLECTION}'")
    print(f"Collection now holds {collection.count()} chunks.")


if __name__ == "__main__":
    main()
