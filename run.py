"""Run the eval set against retrieve() and score retrieval quality.

Metrics (answerable questions only):
- hit@k: fraction of questions with a gold doc in the top-k chunks
- MRR: mean reciprocal rank of the first gold-doc chunk

Unanswerable questions are reported separately: retrieval metrics can't
score them, and a good system should abstain rather than hallucinate.

Usage: uv run python run.py [--k 5] [--output evals/results.json] [--judge]
--judge also scores evidence support with an LLM (needs OPENAI_API_KEY).
"""

import argparse
import json
import os
from pathlib import Path

from metrics import hit_rate_at_k, mean_reciprocal_rank
from retrieve import retrieve

EVAL_SET = Path(__file__).resolve().parent / "evals" / "eval_set.json"


def main():
    parser = argparse.ArgumentParser(description="Run the eval set.")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--db", default="chroma_db")
    parser.add_argument("--output", default=None, help="Write per-question results as JSON.")
    parser.add_argument("--judge", action="store_true", help="Score evidence support with an LLM.")
    parser.add_argument("--mode", choices=["hybrid", "vector"], default="vector")
    parser.add_argument("--max-per-doc", type=int, default=1)
    parser.add_argument("--decompose", action="store_true", help="Use oracle sub-questions from evals/decompositions.json for multi-hop items.")
    parser.add_argument("--auto-decompose", action="store_true", help="Generate sub-questions automatically with decompose.py (LLM when available, else rules).")
    parser.add_argument("--two-stage", action="store_true", help="Two-stage decomposition: broad retrieval first, then LLM proposes entities grounded in the retrieved candidates (two_stage.py).")
    parser.add_argument("--keyword-filter", action="store_true", help="With --two-stage: drop proposed entities that appear in none of the stage-1 candidate docs.")
    args = parser.parse_args()

    eval_set = json.loads(EVAL_SET.read_text(encoding="utf-8"))
    decomp_path = Path(__file__).resolve().parent / "evals" / "decompositions.json"
    decomps = {}
    if args.decompose and decomp_path.exists():
        decomps = {k: v for k, v in json.loads(decomp_path.read_text(encoding="utf-8")).items() if not k.startswith("_")}
        print(f"Decomposition on: {len(decomps)} questions use oracle sub-questions.")
    answerable = [q for q in eval_set if q["type"] != "unanswerable"]
    unanswerable = [q for q in eval_set if q["type"] == "unanswerable"]

    per_question = []
    retrieved_docs_list, gold_sets = [], []
    two_stage_fn = None
    if args.two_stage:
        from decompose import llm_available

        if llm_available():
            from two_stage import two_stage_sub_questions

            two_stage_fn = two_stage_sub_questions
            print("Two-stage decomposition on (LLM).")
        else:
            print("Two-stage requested but no LLM available; falling back to single-step retrieval.")
    if args.auto_decompose and not args.two_stage:
        from decompose import decompose, llm_available

        print(f"Auto-decomposition on ({'LLM' if llm_available() else 'rule-based fallback'}).")
    for item in answerable:
        stage1_docs, dropped, two_stage, fallback = [], [], False, False
        if two_stage_fn is not None:
            info = two_stage_fn(item["question"], db=args.db, mode=args.mode, max_per_doc=args.max_per_doc, keyword_filter=args.keyword_filter)
            sub_qs = info["sub_questions"]
            stage1_docs = info["stage1_doc_ids"]
            dropped = info["dropped_entities"]
            fallback = info["fallback"]
            two_stage = True
        elif args.auto_decompose and not args.two_stage:
            sub_qs = decompose(item["question"])
        elif item["id"] in decomps:
            sub_qs = decomps[item["id"]]
        else:
            sub_qs = None
        if sub_qs is not None:
            # Multi-step: retrieve per sub-question, merge round-robin
            # so one bad sub-question can't fill every slot and starve
            # the others (the eval-022 failure: sub-Q1's junk filled all
            # 5 slots while sub-Q2 alone retrieved the gold doc at rank 1).
            per_sq = []
            for sq in sub_qs:
                per_sq.append([r["doc_id"] for r in retrieve(sq, k=args.k, db=args.db, mode=args.mode, max_per_doc=args.max_per_doc)])
            docs = []
            for i in range(args.k):
                for lst in per_sq:
                    if i < len(lst) and lst[i] not in docs:
                        docs.append(lst[i])
                    if len(docs) >= args.k:
                        break
                if len(docs) >= args.k:
                    break
        else:
            results = retrieve(item["question"], k=args.k, db=args.db, mode=args.mode, max_per_doc=args.max_per_doc)
            docs = [r["doc_id"] for r in results]
        gold = set(item["gold_doc_ids"])
        retrieved_docs_list.append(docs)
        gold_sets.append(gold)
        first_hit = next((i + 1 for i, d in enumerate(docs) if d in gold), None)
        per_question.append({
            "id": item["id"],
            "question": item["question"],
            "gold_doc_ids": sorted(gold),
            "retrieved_doc_ids": docs,
            "hit_at_k": bool(gold & set(docs)),
            "first_hit_rank": first_hit,
            "decomposed": sub_qs is not None,
            "sub_questions": sub_qs,
            "two_stage": two_stage,
            "two_stage_fallback": fallback,
            "stage1_doc_ids": stage1_docs,
            "dropped_entities": dropped,
        })

    print(f"\n{len(answerable)} answerable questions, k={args.k}")
    print(f"hit@1: {hit_rate_at_k(retrieved_docs_list, gold_sets, 1):.3f}")
    print(f"hit@3: {hit_rate_at_k(retrieved_docs_list, gold_sets, 3):.3f}")
    print(f"hit@{args.k}: {hit_rate_at_k(retrieved_docs_list, gold_sets, args.k):.3f}")
    print(f"MRR:   {mean_reciprocal_rank(retrieved_docs_list, gold_sets):.3f}")
    print(f"\n{len(unanswerable)} unanswerable questions (excluded from retrieval metrics):")
    for item in unanswerable:
        print(f"  - {item['id']}: {item['question']}")

    misses = [q for q in per_question if not q["hit_at_k"]]
    if misses:
        print("\nMisses (no gold doc in top-k):")
        for q in misses:
            print(f"  - {q['id']}: {q['question']}")
            print(f"    gold: {q['gold_doc_ids']}, got: {q['retrieved_doc_ids']}")

    if args.judge:
        if not os.environ.get("OPENAI_API_KEY"):
            print("\n--judge skipped: OPENAI_API_KEY not set.")
        else:
            from judge import judge_evidence

            verdicts = {}
            for item, q in zip(answerable, per_question):
                texts = [r["text"] for r in retrieve(item["question"], k=args.k, db=args.db, mode=args.mode, max_per_doc=args.max_per_doc)]
                verdict, _ = judge_evidence(item["question"], item["gold_answer"], texts)
                verdicts[verdict] = verdicts.get(verdict, 0) + 1
                q["evidence_support"] = verdict
            print(f"\nEvidence support (LLM judge): {verdicts}")

    if args.output:
        Path(args.output).write_text(json.dumps(per_question, indent=2), encoding="utf-8")
        print(f"\nWrote per-question results to {args.output}")


if __name__ == "__main__":
    main()
