"""Order lookup against the (fictional) order store."""

import json
import re
from pathlib import Path

from .knowledge import DATA_DIR


def load_orders(path: Path = DATA_DIR / "orders.json") -> dict:
    return {o["order_id"]: o for o in json.loads(path.read_text(encoding="utf-8"))}


def extract_order_id(text: str) -> str | None:
    """Find an order reference like 'N-1042' in free text."""
    m = re.search(r"\bN-\d{3,6}\b", text.upper())
    return m.group(0) if m else None


def status_sentence(order: dict) -> str:
    """Human-readable one-liner about an order's state, grounded in order data."""
    s = order["status"]
    if s == "processing":
        return f"Your order {order['order_id']} is being prepared and has not shipped yet."
    if s == "shipped":
        return (
            f"Your order {order['order_id']} shipped with {order['carrier']} "
            f"(tracking {order['tracking']}) and is expected on {order['eta']}."
        )
    if s == "delayed":
        return (
            f"Your order {order['order_id']} is unfortunately delayed. The carrier "
            f"{order['carrier']} currently expects delivery on {order['eta']} "
            f"(tracking {order['tracking']})."
        )
    if s == "delivered":
        return f"Our records show order {order['order_id']} as delivered on {order['eta']}."
    return f"Order {order['order_id']} has status: {s}."
