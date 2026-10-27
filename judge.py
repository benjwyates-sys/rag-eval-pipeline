"""LLM judge: does the retrieved evidence support the gold answer?

This judges retrieval quality, not generation: given the question, the
known-good answer, and the retrieved passages, does the evidence contain
what's needed to answer correctly? Requires OPENAI_API_KEY and the openai
package; callers should skip judging cleanly when either is absent.
"""


def judge_evidence(question, gold_answer, retrieved_texts):
    """Return (verdict, rationale) with verdict in SUPPORTED / PARTIAL /
    UNSUPPORTED."""
    import openai

    client = openai.OpenAI()
    passages = "\n\n".join(f"[{i + 1}] {t[:1500]}" for i, t in enumerate(retrieved_texts))
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You grade a retrieval system. Reply with exactly one word "
                    "on the first line — SUPPORTED, PARTIAL, or UNSUPPORTED — "
                    "then one sentence of rationale. SUPPORTED means the "
                    "passages contain the gold answer; PARTIAL means they "
                    "contain part of it; UNSUPPORTED means they do not."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Question: {question}\nGold answer: {gold_answer}\n\n"
                    f"Retrieved passages:\n{passages}"
                ),
            },
        ],
    )
    content = resp.choices[0].message.content.strip()
    first_line = content.splitlines()[0].strip().upper()
    verdict = next((v for v in ("SUPPORTED", "PARTIAL", "UNSUPPORTED") if v in first_line), "UNSUPPORTED")
    rationale = " ".join(content.splitlines()[1:]).strip()
    return verdict, rationale
