# ADR-002: Prototype is offline-first, LLM is an optional layer

**Status:** accepted · 2026-07-13

## Context

The CS Copilot prototype must be runnable by anyone cloning the repo (recruiters, reviewers, CI) — most of whom have no API key — while still demonstrating real LLM integration.

## Decision

The pipeline core (classify → retrieve → escalate-or-draft) is deterministic, stdlib-only Python. The LLM (Anthropic API, `claude-opus-4-8`) is an optional `--llm` polish step that may rewrite tone but never facts; on missing key or API error it falls back to the unpolished draft.

## Consequences

- Tests and the eval harness run in CI with zero secrets and zero flakiness — quality gates (escalation recall = 1.0) are enforceable on every commit.
- The escalation policy is code, not prompt: it cannot be jailbroken or drift with model versions. This mirrors the governance stance of the program (red lines enforced outside the model).
- Trade-off: draft fluency without `--llm` is template-like. Acceptable — the pilot's value claim is handle-time and grounding, not prose beauty, and the demo with a key shows the polished path.
