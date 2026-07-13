# Buy / Build / Deprecate — Owning the Tool Landscape

**Principle: the landscape is a portfolio too.** Every tool decision is made against criteria, revisited quarterly, and every new tool must name what it replaces or why it's additive. Default posture: **buy for standard processes, build thin layers on proprietary data, deprecate ruthlessly.**

## Decision table

| Decision | When |
|---|---|
| **Buy** | Standard process, mature product category, value now > differentiation later |
| **Build** | The process differentiates us, or the value sits in proprietary data/integrations no vendor has |
| **Configure** | Standard platform covers 80%, our workflow is the last 20% (most common outcome) |
| **Deprecate** | Duplication, adoption < 20% after enablement, security finding, or ROI below cost of ownership |
| **Do nothing** | Value unproven and risk or TCO disproportionate — a legitimate decision, recorded like the others |

## Assessment dimensions (scored per candidate)

Business fit · total cost of ownership (licenses + integration + enablement + maintenance) · integration with existing systems · **data residency & processing terms (DPA)** · access control & auditability · evaluation/monitoring hooks · vendor lock-in & **exit path** (export? switching cost?) · expected adoption · overlap with tools we already pay for.

## Worked example 1 — CS Copilot: buy, build or configure?

**Candidates:** (a) helpdesk vendor's native AI add-on, (b) standalone AI-support suite, (c) thin in-house layer on the LLM API over our own FAQ/order data.

| Criterion | (a) Native add-on | (b) AI suite | (c) Thin build |
|---|---|---|---|
| Business fit | Good for generic replies; weak on our order data | Strong, but replaces the helpdesk workflow | Exactly our data, our escalation rules |
| TCO (3yr) | ~€86k (per-seat) | ~€150k + migration | ~€45k (build + run + maintain) |
| Eval/guardrail control | Black box | Partial | Full (own [eval harness](../../prototypes/cs-copilot/)) |
| Lock-in / exit | Low (stays if helpdesk stays) | High | Low — model-agnostic API layer |
| Time to evidence | 2 weeks | 2–3 months | 2 weeks (prototype exists) |

**Decision: (c) build thin, revisit at scale.** The differentiator is our product/order data and our escalation policy, not chat UI. Explicit exit clause: if the native add-on (a) reaches feature parity on grounded order-data answers within 12 months, we switch and deprecate the layer — the build is priced as a 12-month bridge, not a forever system. *(This is the kind of reversible, evidence-priced bet a two-person AI team can afford.)*

## Worked example 2 — deprecation

**Finding (day-20 tool inventory):** three overlapping transcription/meeting-notes tools across teams (€14k/yr combined), one of them storing recordings outside the EU; plus 11 personal ChatGPT accounts on private emails.

**Decision:** consolidate on one meeting tool with EU processing and workspace SSO (€6k/yr); 60-day sunset for the other two with migration support; personal accounts replaced by workspace accounts with the [red lines](../../governance/ai-richtlinie.md) attached — amnesty framing, no blame. **Net: −€8k/yr, one data-residency risk closed, and the shadow usage is now visible and governable.**

## The register

One table, maintained by the AI Senior Manager, reviewed at the quarterly landscape review:

| Tool | Teams | Decision | Cost/yr | Adoption | DPA | Next review | Exit path |
|---|---|---|---|---|---|---|---|
| *(example)* Meeting notes tool X | all | Buy (consolidated) | €6k | 74% | ✅ EU | Q3 | export API, 30-day switch |
| *(example)* CS copilot layer | CS | Build (bridge, 12mo) | €15k | pilot | ✅ | Q3 | prompt+data portable, model-agnostic |

Rules: every row has a next-review date and an exit path — a tool without an exit path doesn't get bought; a row without adoption data doesn't survive review.
