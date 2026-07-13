"""CS Copilot — grounded customer-service answer drafts with hard escalation rules.

Prototype for the NATURA Foods case (fictional). Offline-deterministic by
default; optional LLM polish via the Anthropic API when a key is configured.
"""

from .pipeline import run

__all__ = ["run"]
