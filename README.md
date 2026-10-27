# rag-eval-lab

A clean-room RAG pipeline + eval harness in Python, built to learn retrieval
fundamentals by hand — no frameworks hiding the machinery.

## What's here

- `scripts/fetch_corpus.py` — downloads a Wikipedia corpus (AV, robotics,
  perception topics; CC BY-SA, source noted in each file)
- `ingest.py` — chunk + embed + upsert into Chroma (local embeddings, no API key)
- `retrieve.py` — (coming) hybrid retrieval
- `ask.py` — (coming) Q&A with citations
- `evals/eval_set.json` — eval questions with verified gold answers + gold docs
- `metrics.py` — hit-rate@k, MRR (pure functions, no I/O)
- `run.py` — runs the eval set and prints scores
- `judge.py` — LLM evidence-support judge (needs OPENAI_API_KEY)

## Run it

```
uv sync
uv run python scripts/fetch_corpus.py
uv run python ingest.py
uv run python run.py
```

Score the eval set with a different k, save per-question results, or add
the LLM evidence judge:

```
uv run python run.py --k 3 --output evals/results.json
uv run python run.py --judge
