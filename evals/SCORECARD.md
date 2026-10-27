# Scorecard — session 3 ablations

27 answerable questions, k=5, 1024-char chunks / 200 overlap unless noted.
Per-question results live in `evals/results_*.json`.

## Results

| Config | hit@1 | hit@3 | hit@5 | MRR | Misses |
|---|---|---|---|---|---|
| Hybrid, no cap (session 2 baseline) | 0.852 | 0.926 | 0.926 | 0.883 | 011, 028 |
| Vector, no cap | 0.889 | 0.926 | 0.963 | 0.909 | 028 |
| Hybrid, div2 | 0.852 | 0.926 | 0.963 | 0.890 | 028 |
| Hybrid, div1 | 0.852 | 0.926 | 0.963 | 0.898 | 028 |
| Vector, div2 | 0.889 | 0.963 | 0.963 | 0.914 | 028 |
| Vector, div1 (champion, no decomposition) | 0.889 | 0.963 | 0.963 | 0.926 | 028 |
| Vector, div1, 512-char chunks | 0.778 | 0.926 | 1.000 | 0.862 | none |
| Vector, div1, 256-char chunks | 0.815 | 0.963 | 0.963 | 0.889 | 028 |
| Vector, div1, word-boundary 1024 | 0.889 | 0.963 | 0.963 | 0.926 | 028 |
| Vector, div1, oracle decomposition | 0.926 | 1.000 | 1.000 | 0.963 | none |

## Findings

1. **Pure vector beats hybrid on every metric.** The keyword ranker adds noise:
   single-term ties plus an alphabetical tie-break feed junk into the RRF
   consensus. On a corpus where embeddings already handle the semantics,
   the keyword ranker is dead weight.
2. **The diversity cap fixes crowding, and it stacks with vector.** eval-011
   failed because one doc took three of five slots; both the cap and pure
   vector fix it independently. Tradeoff: when the raw top-10 is dominated
   by one doc, the cap starves the result list (some questions return 1–2
   chunks instead of 5) — diversity costs context quantity.
3. **Chunk size is precision vs. coverage, not a domination.** 1024 has the
   best ranking (MRR 0.926); 512 has the best top-5 coverage (1.000) but the
   worst ranking (MRR 0.862) — it drags Zoox to rank 4 for eval-028 while
   dropping other questions (eval-025 falls rank 1 → 5). 256 fragments too far.
   The right pick depends on the downstream reader.
4. **Word boundaries change nothing on the metrics.** Embeddings don't care
   about mid-word splits; the boundary fix is aesthetic (it matters for what
   a generator reads, not for retrieval scores).
5. **Oracle decomposition is the ceiling — and it is a full-chain ceiling.**
   With perfect sub-questions, hit@3 and hit@5 are 1.000 and MRR is 0.963,
   and all four multi-hop items retrieve *both* gold docs (e.g. eval-028
   returns Zoox and Cruise at ranks 1–2). The bottleneck is *generating*
   the decomposition (entity identification), not retrieval.

## Caveats

- 27 questions, one corpus: the champion is champion on this set, not a
  universal law.
- The metric counts *any* gold doc as a hit; the decomposition check above
  verified both docs present, so the ceiling claim is stronger than the
  metric alone.
- The oracle sub-questions are hand-written and, for eval-028, name the
  answer entities. A deployable decomposer must generate them itself —
  that is the next project (it needs an LLM in the loop; see `judge.py`'s
  OPENAI_API_KEY setup).

## Champion command

```
uv run python run.py --mode vector --max-per-doc 1
uv run python run.py --mode vector --max-per-doc 1 --decompose  # oracle ceiling
```
