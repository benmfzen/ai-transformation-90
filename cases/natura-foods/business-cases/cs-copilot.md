# Business Case — Pilot 1: Customer Service Response Copilot

**Type:** Efficiency · **Owner:** Mara Willems (Customer Service) · **Working prototype:** [`prototypes/cs-copilot/`](../../../prototypes/cs-copilot/)

## Problem

38 agents handle ~6,500 inquiries/month across 8 markets. ~55% are recurring standard cases (order status, returns, shipping, product questions). Answer quality varies by agent tenure; response SLA (24h) is missed in peak weeks.

## Solution shape

Copilot inside the existing helpdesk: classifies the inquiry, retrieves the relevant FAQ/policy passages and order data, drafts a grounded response with cited sources. **The agent reviews and sends — nothing goes out without a human.** Uncertain or sensitive cases (allergy/health, legal threats, missing order data) are escalated, not answered.

## Baseline (measured over 4 weeks before start — frozen)

| Metric | Value |
|---|---|
| Inquiries | 6,500 / month |
| Avg. handle time (AHT), standard cases | 9.0 min |
| First-contact resolution | 64% |
| Response time, p90 | 22h |
| Rework rate (reopened tickets) | 6% |

## Target

**AHT on standard cases −25%** at equal or better quality (rework ≤ 6%, FCR ≥ 64%), measured at team level — never per person.

## Value logic

```
Capacity value
  6,500 inquiries × 55% standard × 9.0 min      = 536 h/month on standard cases
  −25% AHT                                       = 134 h/month freed
  × €38/h fully loaded                           = €5,100/month  ≈ €61k/year

Cost (year 1)
  Build & integration (15 person-days internal)  ≈ €12k one-off
  LLM usage (~6,500 × ~8k tokens/month)          ≈ €4k/year
  Maintenance & eval upkeep (0.05 FTE)           ≈ €5k/year

Net year-1 value                                 ≈ €40k   ·   Payback ≈ 4 months
Confidence: 70% (prototype evidence + stable baseline; adoption is the main risk)
```

**Where the freed time actually goes (this is the value realization, not the time saving):**

1. Absorb ~15% YoY inquiry growth **without the backfill hire** planned for Q3 (≈ €52k/yr avoided — counted from the moment the hire is formally cancelled, not before)
2. p90 response time from 22h toward 8h (retention-relevant, tracked but not monetized)
3. Freed senior-agent time moves to the complex cases that drive FCR

## Measurement design

- **Design:** two comparable agent pods (12 vs. 12), copilot enabled for one, 4 weeks; then crossover. Team-level metrics only.
- **Quality rubric:** weekly sample of 40 sent answers scored blind (correctness, tone, completeness) by 2 senior agents; copilot answers must score ≥ control.
- **Minimum sample:** ≥ 1,500 standard cases per arm before reading results.
- **Stop criteria:** rework > 8% in any week · any incident where an escalation-class case (health/allergy/legal) went out unescalated · adoption < 50% of pod in week 2 (then fix workflow, not agents).
- **Groundedness gate:** the [prototype's eval harness](../../../prototypes/cs-copilot/) runs on every prompt/model change — category accuracy, escalation recall and source-grounding must not regress.

## Risks

| Risk | Mitigation |
|---|---|
| Personal data in prompts | Only order fields needed for the case; PII redaction; DPA with provider |
| Wrong answers on health/allergy questions | Hard escalation rule (never answered by draft), tested in eval set |
| Works-in-demo, fails-in-queue | Pilot runs inside the real helpdesk queue from day 1 |
| Agents feel monitored | Team-level metrics only, works council briefed before start |
