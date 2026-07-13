"""Optional LLM polish step (Anthropic API).

Only rewrites tone and flow — the system prompt forbids adding facts, and the
deterministic pipeline has already decided WHAT may be said (sources, order
data) and whether the case escalates. If no API key is configured or the call
fails, the unpolished draft is returned unchanged: the LLM is an enhancement,
never a dependency.
"""

import os

MODEL = os.environ.get("CS_COPILOT_MODEL", "claude-opus-4-8")

SYSTEM = (
    "You polish customer-service reply drafts for NATURA Foods, a friendly "
    "online food retailer. Rewrite the draft so it flows naturally and warmly. "
    "STRICT RULES: Keep every fact, number, date, tracking number and policy "
    "statement exactly as given. Do not add information, offers, apologies for "
    "things not mentioned, or promises. Keep it under 120 words. Reply with "
    "the rewritten draft only."
)


def polish(draft: str, customer_message: str) -> str:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return draft
    try:
        import anthropic

        client = anthropic.Anthropic()
        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            system=SYSTEM,
            messages=[{
                "role": "user",
                "content": f"Customer wrote:\n{customer_message}\n\nDraft to polish:\n{draft}",
            }],
        )
        text = next((b.text for b in response.content if b.type == "text"), "")
        return text.strip() or draft
    except Exception:
        return draft
