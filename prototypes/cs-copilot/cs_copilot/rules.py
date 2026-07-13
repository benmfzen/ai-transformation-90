"""Classification and hard escalation rules.

Escalation is policy, not model output: these rules run deterministically and
cannot be overridden by anything the LLM produces. That is the core
human-in-the-loop guarantee of this prototype.
"""

CATEGORIES = ["order_status", "return_refund", "shipping_info", "product_info", "complaint", "other"]

CATEGORY_KEYWORDS = {
    # complaint first: on a score tie a complaint reading wins (safer default)
    "complaint": [
        "damaged", "broken", "wrong item", "wrong product", "missing", "spoiled",
        "terrible", "unacceptable", "disappointed", "complaint", "bad quality",
        "opened package", "leaking",
    ],
    "order_status": [
        "where is", "order status", "status of", "tracking", "track", "shipped",
        "arrive", "eta", "package", "parcel", "delivery date", "my order",
        "cancel", "address",
    ],
    "return_refund": [
        "return", "refund", "money back", "send back", "send it back", "exchange",
        "give back", "reimburse",
    ],
    "shipping_info": [
        "shipping cost", "shipping fee", "delivery cost", "how long does delivery",
        "delivery take", "ship to", "do you ship", "free shipping", "shipping",
    ],
    "product_info": [
        "ingredient", "contain", "vegan", "vegetarian", "gluten", "organic",
        "storage", "store", "shelf life", "nutrition", "sugar", "protein",
        "allergen", "traces", "best before", "subscription", "payment", "invoice",
        "discount", "loyalty", "points",
    ],
}

HEALTH_KEYWORDS = [
    "allergic", "allergy", "anaphyla", "sick", "ill after", "hospital",
    "food poisoning", "poisoning", "mold", "moldy", "rash", "reaction",
]

LEGAL_KEYWORDS = [
    "lawyer", "attorney", "sue", "suing", "legal action", "lawsuit",
    "consumer protection", "press", "court",
]

HOSTILE_KEYWORDS = [
    "scam", "fraud", "thieves", "worst company", "never order again",
    "reported you", "criminal",
]


def classify(message: str) -> tuple[str, float]:
    """Keyword-based category with a crude margin as confidence signal.

    Returns (category, margin) where margin is the score lead over the runner-up
    (1.0 when only one category matched at all).
    """
    text = message.lower()
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        scores[cat] = sum(1 for kw in keywords if kw in text)
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    best_cat, best = ranked[0]
    second = ranked[1][1]
    if best == 0:
        return "other", 0.0
    margin = (best - second) / best
    return best_cat, margin


def escalation(message: str, order_id: str | None, order_found: bool, top_score: float) -> str | None:
    """Return an escalation reason, or None if a draft may be produced.

    Checked in priority order. Health/allergy and legal are absolute — they
    escalate even when the KB could answer (policy from the pilot charter).
    """
    text = message.lower()
    if any(kw in text for kw in HEALTH_KEYWORDS):
        return "health_allergy"
    if any(kw in text for kw in LEGAL_KEYWORDS):
        return "legal"
    if order_id and not order_found:
        return "order_not_found"
    if any(kw in text for kw in HOSTILE_KEYWORDS):
        return "hostile_tone"
    if top_score < 0.2:
        return "low_confidence"
    return None
