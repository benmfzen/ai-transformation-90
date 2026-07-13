# AI Opportunity Portfolio — NATURA Foods SE

**Purpose:** turn "we should do something with AI" into a ranked, defensible portfolio. Every initiative is classified as **Efficiency** (same work, less cost/time) or **Opportunity** (new capability, growth, better decisions) and scored on two axes.

## Scoring model

All dimensions 1–5, where 5 is best. Evidence required per score — no gut-feel numbers.

**Business Value** = 0.4 × Efficiency Value + 0.4 × Revenue/Growth Value + 0.2 × Risk/Quality Value

| Dimension | 5 means |
|---|---|
| Efficiency Value | > €100k/yr in capacity or external cost at full rollout |
| Revenue/Growth Value | credible path to measurable revenue, conversion or speed-to-market impact |
| Risk/Quality Value | materially fewer errors, compliance incidents or quality escapes |

**Execution** = average of:

| Dimension | 5 means |
|---|---|
| Data Readiness | data exists, structured, accessible today |
| Process Readiness | process is stable and documented enough to augment |
| Owner Readiness | team lead wants it and can staff it |
| Technical Simplicity | prompt + retrieval over existing systems; no new infrastructure |
| **Time to Evidence** | a believable yes/no signal in **days, not months** |

*Time to Evidence is weighted equal to the rest but is the tie-breaker between close candidates: early evidence compounds — it buys trust, budget and adoption for everything after.*

## The portfolio (assessment as of day 25)

| # | Initiative | Team | Type | Value | Execution | Decision |
|---|---|---|---|---|---|---|
| 1 | Customer service response copilot | Customer Service | Efficiency | 3.8 | **4.4** | 🚀 **Pilot 1** |
| 2 | Product content localization engine | Brand & Content | Efficiency | 3.8 | **3.6** | 🚀 **Pilot 2** |
| 3 | AI-drafted Weekly Business Review | Finance / C-level | Opportunity | 3.4 | **3.4** | 🚀 **Pilot 3** |
| 4 | Ad creative variation & testing | Performance Mktg | Efficiency | 3.0 | 4.0 | Wave 2 (Q1) |
| 5 | Invoice & PO document extraction | Finance | Efficiency | 2.8 | 3.8 | Wave 2 (Q1) |
| 6 | Retail sell-in deck automation | B2B Sales | Efficiency | 2.6 | 3.6 | Wave 2 (Q1) |
| 7 | Supplier negotiation prep packs | Purchasing | Efficiency | 2.8 | 3.2 | Wave 2 (Q2) |
| 8 | Label & claims compliance checker | Quality / Legal | Opportunity | 3.2 | 2.8 | Q2 — with legal co-owner |
| 9 | CRM lifecycle personalization | Performance Mktg | Opportunity | 3.6 | 2.6 | Q2 — needs event data cleanup |
| 10 | On-site search & merchandising | E-Commerce | Opportunity | 3.6 | 2.4 | Q2/Q3 — platform dependency |
| 11 | Demand forecasting & replenishment | Supply Chain | Opportunity | **4.2** | 1.8 | ⚠️ **Data project first**, pilot Q3 |
| 12 | New product concept screening | Product Dev | Opportunity | 3.0 | 2.2 | Q3 — after PIM cleanup |

*HR drafting/FAQ use cases run as enablement inside the People team (small value, near-zero risk when screening/ranking of people is excluded — see the [red lines](../../governance/ai-richtlinie.md)); they don't compete for pilot slots.*

## Why these three pilots

- **Pilot 1 — CS Copilot** is the best value × execution combination in the portfolio and produces evidence within two weeks. It is also the trust-builder: every team watches customer service. → [Business case](business-cases/cs-copilot.md), [working prototype](../../prototypes/cs-copilot/)
- **Pilot 2 — Content Localization** attacks the scaling constraint of an 8-market business and carries a real guardrail problem (EU food claims) — solving it visibly proves governance can enable rather than block. → [Business case](business-cases/content-localization.md)
- **Pilot 3 — Weekly Business Review** is deliberately an **Opportunity** pilot: it tests whether AI can improve *decisions*, not just tasks, and gives the C-level a weekly touchpoint with the program's output. → [Business case](business-cases/weekly-business-review.md)

**The one that hurts to postpone:** demand forecasting (#11) has the highest value score in the portfolio and the worst execution score. Piloting it now would burn six months and the program's credibility on a data problem. Instead: a scoped data-readiness project in Q1–Q2 (forecast-relevant history, promotions calendar, partner sell-out feeds), pilot in Q3. The portfolio makes this trade-off explicit instead of letting the loudest stakeholder decide.

## Portfolio rules

1. **Every initiative has one accountable team lead** — no lead, no slot (see [operating model](operating-model.md)).
2. **Efficiency and Opportunity are reported separately.** Efficiency value is validated against baselines; opportunity value against pre-registered decision or revenue metrics. Mixing them inflates both.
3. **Re-score monthly** at the Portfolio Council. Execution scores move (that's the point of data projects and enablement); value scores move only with new evidence.
4. **Killed ≠ failed.** An initiative stopped on evidence returns its slot to the next candidate — the portfolio is a queue, not a graveyard.
