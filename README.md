# rag-eval-lab

A clean-room RAG pipeline + eval harness in Python, built to learn retrieval
fundamentals by hand — no frameworks hiding the machinery.

## What's here

- `scripts/fetch_corpus.py` — downloads a Wikipedia corpus (AV, robotics,
  perception topics; CC BY-SA, source noted in each file)
- `ingest.py` — chunk + embed + upsert into Chroma (local embeddings, no API key)
- `retrieve.py` — hybrid (vector + keyword, RRF) and pure-vector retrieval, with a per-doc diversity cap (`--mode`, `--max-per-doc`)
- `ask.py` — Q&A with citations (grounded mode without an API key; LLM synthesis with OPENAI_API_KEY)
- `evals/eval_set.json` — eval questions with verified gold answers + gold docs
- `evals/decompositions.json` — oracle sub-questions for the multi-hop items (ceiling test)
- `evals/SCORECARD.md` — session 3 ablation results and findings
- `metrics.py` — hit-rate@k, MRR (pure functions, no I/O)
- `run.py` — runs the eval set and prints scores
- `decompose.py` — automatic query decomposition (LLM guess-first prompt, rule-based fallback; `--auto-decompose`)
- `two_stage.py` — two-stage grounded decomposition (retrieve first, LLM proposes entities from candidates; `--two-stage`, optional `--keyword-filter`)
- `selective.py` — selective routing (entity-seeking questions grounded, rest single-pass; `--selective`)
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
```

## Results

Champion config from session 3 (27 answerable questions, k=5):
pure-vector retrieval with max 1 chunk per doc — hit@1 0.889, hit@3 0.963,
hit@5 0.963, MRR 0.926. Automatic LLM decomposition (session 4,
guess-first prompt, round-robin merge) lifts that to hit@3/hit@5 1.000,
MRR 0.938 with zero misses. Two-stage grounded decomposition (session 5,
retrieve first, then guess from candidates) scores lower: MRR 0.880,
keyword-filter variant 0.887 — grounding hurts general questions (see
scorecard). Selective routing (session 6, grounded only for entity-seeking questions) ties session 4 at MRR 0.935 with zero misses, and the faithfulness judge rates champion evidence SUPPORTED 23, PARTIAL 4, UNSUPPORTED 0. Oracle query decomposition lifts that to hit@3/hit@5
1.000, MRR 0.963. Full ablation table and findings: `evals/SCORECARD.md`.

```
uv run python run.py
uv run python run.py --decompose
uv run python run.py --auto-decompose  # needs OPENAI_API_KEY
uv run python run.py --two-stage  # needs OPENAI_API_KEY
uv run python run.py --selective  # needs OPENAI_API_KEY
uv run python run.py --judge  # needs OPENAI_API_KEY
```
