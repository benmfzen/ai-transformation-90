"""End-to-end pipeline: classify → retrieve → escalate-or-draft → (optional) polish."""

from . import knowledge, orders, rules

_FAQ = None
_ORDERS = None


def _kb():
    global _FAQ, _ORDERS
    if _FAQ is None:
        _FAQ = knowledge.load_faq()
        _ORDERS = orders.load_orders()
    return _FAQ, _ORDERS


def run(message: str, order_id: str | None = None, use_llm: bool = False) -> dict:
    """Process one customer inquiry into a structured, grounded result.

    Returns a dict with: category, confidence, escalate, escalation_reason,
    order, answer_draft, sources. The draft is built ONLY from retrieved FAQ
    text and order data — the optional LLM step rewrites tone, never facts.
    """
    faq, order_store = _kb()

    oid = order_id or orders.extract_order_id(message)
    order = order_store.get(oid) if oid else None

    category, margin = rules.classify(message)
    hits = knowledge.retrieve(message, faq)
    top_score = hits[0][1] if hits else 0.0

    # An answerable order question doesn't need FAQ coverage — order data is the source.
    effective_score = max(top_score, 0.9 if (order and category == "order_status") else 0.0)

    reason = rules.escalation(message, oid, order is not None, effective_score)
    if reason:
        return {
            "category": category,
            "confidence": 0.0,
            "escalate": True,
            "escalation_reason": reason,
            "order": oid,
            "answer_draft": None,
            "sources": [],
        }

    parts = ["Hi, thanks for reaching out!"]
    sources = []
    if order:
        parts.append(orders.status_sentence(order))
        sources.append(f"order:{order['order_id']}")
    for entry, score in hits[:2]:
        if score >= 0.2:
            parts.append(entry.answer)
            sources.append(f"faq:{entry.id}")
    parts.append("Is there anything else we can help you with?")

    confidence = round(min(1.0, 0.5 * effective_score + 0.5 * (margin if margin > 0 else effective_score)), 2)
    draft = " ".join(parts)

    if use_llm:
        from . import llm
        draft = llm.polish(draft, message)

    return {
        "category": category,
        "confidence": confidence,
        "escalate": False,
        "escalation_reason": None,
        "order": oid,
        "answer_draft": draft,
        "sources": sources,
    }
