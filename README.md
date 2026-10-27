# rag-eval-lab

A clean-room RAG pipeline + eval harness in Python, built to learn retrieval
fundamentals by hand — no frameworks hiding the machinery.

## What's here

- `scripts/fetch_corpus.py` — downloads a Wikipedia corpus (AV, robotics,
  perception topics; CC BY-SA, source noted in each file)
- `ingest.py` — chunk + embed + upsert into Chroma (local embeddings, no API key)
- `retrieve.py` — (coming) hybrid retrieval
- `ask.py` — (coming) Q&A with citations
- `evals/` — (coming) eval set + scorecard

## Run it

```
uv sync
uv run python scripts/fetch_corpus.py
uv run python ingest.py
```
