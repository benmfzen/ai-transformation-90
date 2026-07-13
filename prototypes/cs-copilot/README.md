# CS Copilot — working prototype

**Grounded customer-service reply drafts with hard escalation rules and an eval harness.** This is the working prototype behind [Pilot 1 of the NATURA case](../../cases/natura-foods/business-cases/cs-copilot.md) — built to be demonstrably safe, measurable and cheap, not to be a product.

![Demo: grounded draft with sources, then a hard health escalation](demo.gif)

```
customer message ──► classify ──► retrieve (FAQ + order data) ──► escalation rules
                                                                       │
                                          escalate ◄── policy hit ─────┤
                                                                       ▼
                                          grounded draft (+ optional LLM polish)
```

## What it proves

1. **Grounding** — the draft is assembled *only* from retrieved FAQ passages and order records; every claim carries a `sources` citation. No retrieval hit → no draft.
2. **Human-in-the-loop by design** — the agent reviews and sends; the pipeline only produces drafts. Health/allergy and legal topics **always** escalate, even when the knowledge base could answer (deterministic policy, not model judgment).
3. **Evaluation as a gate, not a demo** — 20 labeled cases with hard thresholds (escalation recall must be 1.0). Runs in CI on every change: a keyword tweak that would let an allergy question slip through fails the build.
4. **LLM as enhancement, not dependency** — the pipeline is deterministic and runs offline. The optional Claude polish step (`--llm`) rewrites tone only; facts, escalation and sources are decided before the model is called, and any API failure falls back to the unpolished draft.

## Run it

No dependencies for the core pipeline (Python ≥ 3.10, stdlib only):

```bash
# a normal order inquiry → grounded draft with sources
python3 -m cs_copilot "Where is my order N-1045?"

# a health-related question → hard escalation, no draft
python3 -m cs_copilot "Does the granola contain nuts? I have a nut allergy."

# tests + eval harness (what CI runs)
python3 -m pytest tests/ -q
python3 eval/run_eval.py
```

Optional LLM polish (needs `pip install anthropic` and `ANTHROPIC_API_KEY`):

```bash
python3 -m cs_copilot "Where is my order N-1045?" --llm
```

## Eval results (current)

| Metric | Result | Gate |
|---|---|---|
| Category accuracy | 1.00 | ≥ 0.85 |
| Escalation recall | 1.00 | = 1.00 |
| Escalation precision | 1.00 | ≥ 0.90 |
| Grounding errors | 0 | = 0 |

## Structure

```
cs_copilot/
  knowledge.py   FAQ parsing + deterministic keyword retrieval
  orders.py      order store lookup + status sentences
  rules.py       classification + hard escalation policy
  pipeline.py    orchestration: classify → retrieve → escalate-or-draft
  llm.py         optional Claude polish (tone only, fact-preserving)
data/            fictional FAQ (16 entries) + order records (8)
eval/            20 labeled cases + gating harness (CI)
tests/           unit tests for retrieval, rules, pipeline
```

## Deliberate limitations

- Keyword retrieval instead of embeddings — good enough to prove the shape; a production version would use the helpdesk's search or an embedding index. The **interface** (retrieve → cite → gate) wouldn't change.
- Fictional data — real deployment plugs into the ticket system and order API behind the same functions.
- English only — the NATURA case is an 8-market business; locale routing is a rollout concern, not a pilot concern.
- The confidence score is a heuristic. In the pilot it is calibrated against the weekly blind quality sample (see the [measurement design](../../cases/natura-foods/business-cases/cs-copilot.md)).
