# Scorecard — sessions 3–6

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
| Vector, div1, oracle decomposition + round-robin | 0.926 | 1.000 | 1.000 | 0.957 | none |
| Vector, div1, rule-based auto-decomposition + round-robin | 0.852 | 0.963 | 0.963 | 0.901 | 028 |
| Vector, div1, LLM auto-decomposition + round-robin (guess-first) | 0.889 | 1.000 | 1.000 | 0.938 | none |
| Vector, div1, two-stage grounded decomposition + round-robin | 0.815 | 0.926 | 0.963 | 0.880 | 025 |
| Vector, div1, two-stage grounded decomposition + keyword filter + round-robin | 0.815 | 0.926 | 1.000 | 0.887 | none |
| Vector, div1, selective routing (grounded for entity questions, auto otherwise) + round-robin | 0.889 | 0.963 | 1.000 | 0.935 | none |

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

## Session 4: automatic decomposition

`decompose.py` generates sub-questions itself: an LLM path (gpt-4o-mini,
temperature 0) with a guess-first prompt — for which/who/what-company
questions it guesses candidate entities from its own knowledge and phrases
one verification sub-question per candidate — plus a rule-based fallback
(split on `;` or `, and`). `run.py --auto-decompose` applies it to every
question uniformly and merges sub-question rankings round-robin, so one bad
sub-question can't starve the others.

### The debugging story (read this before trusting the numbers)

The first three 'LLM' runs were not LLM runs at all. Every sub-question they
produced matched the rule-based splitter exactly, and a direct call to
`decompose_llm()` raised `openai.AuthenticationError: 401 — Incorrect API
key`. `decompose()` had caught all exceptions and fallen back silently, so
the runs wore an '(LLM)' label while running rules. Those numbers are kept
in the table, relabeled as rule-based auto-decomposition (MRR 0.901). The
fix was a valid key plus a loud warning: `decompose()` now warns to stderr
on LLM failure instead of silently degrading. Lesson: a fallback that
fails silently is a measurement bug, not robustness.

### Results

The first real LLM run (guess-first prompt, round-robin merge): hit@1 0.889,
hit@3/hit@5 1.000, MRR 0.938, zero misses — between the champion (0.926) and
the oracle ceiling (0.957). Decomposition fully closes the coverage gap and
about 39% of the ranking gap ((0.938-0.926)/(0.957-0.926)). Only 003 (rank 2),
011 (rank 2), and 028 (rank 3) sit below rank 1.

### What the LLM actually did

- eval-022 fixed properly at rank 1: one sub-question per P/I/D term, each
  naming the whole. The current prompt contains no PID example, so this is
  generalization, not example contamination.
- eval-006/008 decompose into clean entity-named triples (founder, when,
  acquirer) — anaphora gone, rank 1. eval-003 improves rank 3 → 2 the same way.
- eval-028 passes at rank 3 with an asterisk. The run guessed Sony (wrong)
  and Amazon (right, Zoox at rank 3); Cruise reaches rank 4 because
  acquisition-flavored AV docs cluster in embedding space, and the metric
  counts any gold doc as a hit. A separate direct call with the same prompt
  guessed McAfee and NortonLifeLock — the model read 'AV' as antivirus, not
  autonomous vehicles. Two findings: temperature 0 is not deterministic
  across calls on this API, and single-pass guessing can land in the wrong
  domain because the decomposer never sees the corpus. This run dodged that
  failure mode; it did not solve it.
- eval-011 rephrased, not guessed ('Which self-driving company was founded
  by the team...'): Waymo is still missing from the top 5; it passes via
  stanley alone. Guessing fires inconsistently.
- Over-decomposition is benign here: simple questions (020, 025) get three
  sub-questions each and still rank 1 — but that is 2-3x the retrieval calls
  per question, a real latency/cost tradeoff.

### Next

Session 5: retrieve first, then guess. A two-stage loop — broad retrieval
grounds the domain, the LLM reads candidate docs, then proposes entities
for targeted verification — directly addresses the wrong-domain failure
above. Ranking (003/011/028 below rank 1) is the remaining gap.

## Session 5: two-stage grounded decomposition

`two_stage.py` retrieves first, then guesses: stage 1 broad vector retrieval (k=10, max 1 chunk per doc), stage 2 LLM proposes entities from those candidates only (title + first 500 chars each), one verification sub-question per entity, merged round-robin. An optional `--keyword-filter` drops proposed entities appearing in none of the stage-1 candidates. `run.py --two-stage` runs it; per-question output records `stage1_doc_ids`, `dropped_entities`, and `two_stage_fallback`.

### Results (negative result)

Two-stage scores BELOW both the single-step champion and session-4 single-pass decomposition: plain 0.815/0.926/0.963, MRR 0.880, sole miss 025; with keyword filter 0.815/0.926/1.000, MRR 0.887, zero misses. Only three questions moved against session 4 (0.938); the other 24 are identical. Grounding as implemented does not work.

### Why it lost

- eval-025 (rank 1 → miss) is the mechanism. Session 4's abstract split retrieved the self-driving-car doc at rank 1. Two-stage entity-instantiated a general question ('has ANY system...') into Nuro, Pony.ai, Waymo, and Tesla checks, each retrieving its company doc and crowding the general doc out entirely. Entity-grounding is actively harmful for questions whose answer is a general claim: the answer ('no') lives in the general doc, not the company docs. eval-001 shows the same mechanism benignly: six sub-questions enumerating candidate entities, harmless at rank 1.
- eval-028 (rank 3 → 4) and eval-011 (rank 2, unchanged) show grounding did not fix entity selection. For 028 the grounded model again guessed Argo AI and Mobileye (Cruise at rank 4 via clustering; Zoox absent from stage-1 candidates, a recall cap). For 011, Waymo WAS in the stage-1 candidates and still was not proposed — the model rephrased instead. Grounding fixed the session-4 domain error (no more antivirus guesses) but not entity selection, twice over.

### The keyword filter was a no-op

`dropped_entities` is empty on all 27 questions in the filter run: the grounded prompt already constrains proposals to candidates, so there was nothing to catch. The filter run's 025 pass is NOT the filter — its stage-2 output nondeterministically included the original question as a fifth sub-question, whose retrieval supplied self-driving-car at rank 5. Plain-vs-filter is therefore confounded by temperature-0 nondeterminism, not a clean ablation; a real filter ablation would freeze stage-2 outputs and toggle only the filter.

### Engineering notes

- The first two-stage runs failed on JSON parsing (the object-format prompt returned markdown-fenced JSON); the fix is a tolerant parser (`_parse_json_list`: strip fences, extract the first [...] block) plus the raw output head in the error, and a per-question `two_stage_fallback` flag. The shipped runs have zero fallbacks.
- Temperature 0 is not deterministic across calls (also seen in session 4): treat single-run LLM numbers as one sample.

### Next

Session 6 candidate: SELECTIVE grounding — route which/who questions (where entities are the answer) to grounded entity-proposal, and keep general and definitional questions on single-pass splits or single-step retrieval. 025 is the poster child for why the routing matters.

## Session 6: selective routing + faithfulness judge

`selective.py` routes by question form: questions asking which/who/what-company (entity-seeking) go down the grounded path (`two_stage.py`); everything else uses single-pass decomposition (`decompose.py`). The router is rule-based and deterministic — no LLM call, so routing itself is reproducible. `run.py --selective` runs it; per-question output records `routed` (grounded/auto/oracle/none).

### Results (statistical tie with session 4)

Selective routing: hit@1 0.889, hit@3 0.963, hit@5 1.000, MRR 0.935, zero misses — versus session-4 auto at 0.938. Against the pre-stated criteria: 025 back at rank 1 (routed auto) ✓; 011 at rank 2 (= auto) ✓; 028 at rank 4 (vs auto's 3) ✗; MRR ≥ 0.938 ✗, short by exactly the 028 slip (1/3 → 1/4 = 0.003). Routing recovered everything two-stage broke (025/026 back to rank 1; 0.880 → 0.935) but grounded beat auto nowhere. Verdict: routing neutralizes grounding's downside without adding upside on this set — complexity for no measured gain.

### Routing audit

The router's decisions match the design exactly: grounded = 003, 006, 008, 011, 028, 029; auto = the other 21. Both risk cases held: 003 grounded at rank 2 (= auto), 029 grounded at rank 1 (= auto). One quirk: for 011 the grounded model returned the SAME rephrased sub-question four times; round-robin merge dedups identical rankings, so it was harmless (rank 2 unchanged).

### Faithfulness judge (closes the session-2 exit criteria)

`run.py --judge` on champion single-step evidence, first run since the judge was built (it needed an API key): SUPPORTED 23, PARTIAL 4, UNSUPPORTED 0. The four partials are all two-part questions (003, 007, 009, 010) where retrieved chunks cover part of the gold answer — a sensible pattern. Anomaly: 028 judged SUPPORTED despite a retrieval miss (neither gold doc retrieved). Either some non-gold chunk genuinely supports the answer or the judge was lenient — and it can't be audited from the output, because `run.py` computes the rationale and discards it (`verdict, _ = ...`). Saving rationales is a follow-up fix for judge auditability.

### Next

This closes the rag-eval arc: pipeline, eval harness, ablations, auto-decomposition, grounded decomposition, selective routing, and faithfulness scores. The recommended next project is a perception-eval study on public data (the Zoox V&V direction from Oct 26), not a seventh session on this harness: at 27 questions, further deltas are within temperature-0 noise.

## Caveats

- 27 questions, one corpus: the champion is champion on this set, not a
  universal law.
- The metric counts *any* gold doc as a hit; the decomposition check above
  verified both docs present, so the ceiling claim is stronger than the
  metric alone.
- The oracle sub-questions are hand-written and, for eval-028, name the
  answer entities. Session 4 built a decomposer that generates them
  itself (see above).
- Temperature 0 did not reproduce identical outputs across calls: the
  same prompt and question produced different entity guesses on different
  calls. Treat single-run LLM numbers as one sample, not a fixed score.

## Champion command

```
uv run python run.py --mode vector --max-per-doc 1
uv run python run.py --mode vector --max-per-doc 1 --decompose  # oracle ceiling
uv run python run.py --mode vector --max-per-doc 1 --auto-decompose  # LLM decomposer, needs OPENAI_API_KEY
uv run python run.py --mode vector --max-per-doc 1 --two-stage  # grounded decomposer, needs OPENAI_API_KEY
uv run python run.py --mode vector --max-per-doc 1 --two-stage --keyword-filter
uv run python run.py --mode vector --max-per-doc 1 --selective  # selective routing, needs OPENAI_API_KEY
uv run python run.py --judge  # faithfulness judge, needs OPENAI_API_KEY
```
