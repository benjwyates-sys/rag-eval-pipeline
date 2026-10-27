"""Ask a question over the corpus.

Retrieves the top-k chunks with retrieve.py, then:
- with OPENAI_API_KEY set (and the openai package installed): synthesizes
  a short answer grounded in the retrieved chunks, with citations.
- without it: prints the retrieved evidence with citations, which is
  still a complete retrieval demo.

Run from the project root:  uv run python ask.py "what is lidar?" --k 5
"""

import argparse
import os

from retrieve import retrieve


def generate_with_openai(question, results):
    import openai  # ImportError -> caller handles

    client = openai.OpenAI()
    context = "\n\n".join(
        f"[{i + 1}] {r['title']}: {r['text']}" for i, r in enumerate(results)
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer using ONLY the provided sources. "
                    "Cite each claim as [n] matching the source numbers."
                ),
            },
            {"role": "user", "content": f"Question: {question}\n\nSources:\n{context}"},
        ],
    )
    return resp.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(description="Ask a question over the corpus.")
    parser.add_argument("question")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--db", default="chroma_db")
    args = parser.parse_args()

    results = retrieve(args.question, k=args.k, db=args.db)
    if not results:
        print("No matches found.")
        return

    if os.environ.get("OPENAI_API_KEY"):
        try:
            print(generate_with_openai(args.question, results))
            print()
        except ImportError:
            print(
                "(openai package not installed — showing retrieved evidence "
                "instead. Run: uv add openai)\n"
            )
        except Exception as e:
            print(f"(generation failed: {e} — showing retrieved evidence instead)\n")
    else:
        print(
            "(No OPENAI_API_KEY set — showing retrieved evidence. "
            "Set the key for a synthesized answer.)\n"
        )

    print("Sources:")
    for i, r in enumerate(results, start=1):
        print(f"[{i}] {r['title']} (chunk {r['chunk_index']}, score {r['score']})")
        print("   " + r["text"][:300].replace("\n", " "))


if __name__ == "__main__":
    main()
