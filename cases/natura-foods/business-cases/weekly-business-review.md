# Business Case — Pilot 3: AI-Drafted Weekly Business Review

**Type:** Opportunity · **Owner:** Nils Berger (Finance), with E-Commerce and Supply Chain as data partners

## Problem

The Monday business review is assembled by hand: two analysts spend ~2.5 days/week each pulling revenue, margin, campaign and stock data into slides. The result is descriptive ("what happened"), rarely diagnostic ("why, and what should we do"), and anomalies — a stockout building up, a campaign quietly burning budget — surface days later than the data would allow.

## Solution shape

A pipeline that ingests the fictional company's weekly extracts (sales, margin, ad spend, inventory) and drafts the review: top anomalies with magnitude, candidate explanations cross-referencing the data, and a short list of proposed actions with owners. Analysts verify, correct and add judgment — their role moves from assembling to investigating. C-level gets the same document every Monday, now including a "decisions needed" section.

## Baseline (frozen)

| Metric | Value |
|---|---|
| Analyst time on WBR assembly | 2 × 2.5 days/week |
| Median lag: anomaly in data → discussed in review | 9 days |
| Stockout incidents on top-50 SKUs | ~8/year, avg. ≈ €25k contribution margin each |
| WBR actions with named owner + deadline | ~30% |

## Target

This is an **Opportunity pilot: the value claim is better and faster decisions.** Time saved is real but secondary.

| Metric | Target |
|---|---|
| Anomaly-to-discussion lag | 9 days → ≤ 3 days |
| WBR actions with owner + deadline | 30% → 80% |
| Assembly time | 5 → ≤ 1.5 analyst-days/week |

## Value logic — deliberately honest

```
Countable (capacity)
  3.5 analyst-days/week freed × €45/h × 46 wks     ≈ €58k/year
  → redeployed to deep-dives and forecast quality, not cut

Decision value (scenario, counted at 30% confidence)
  1–2 top-SKU stockouts caught early per year       €25–50k margin
  Underperforming campaigns paused ~1 week earlier  ~0.5% of €12m spend ≈ €60k
  Expected value @30%                               ≈ €30–35k/year

Cost (year 1)
  Build (12 person-days) + data extracts            ≈ €10k one-off
  LLM usage                                         ≈ €2k/year
```

**Why only 30% confidence:** decision value depends on the organization acting on the signal, which the pilot itself must prove. Overclaiming here is how AI programs lose CFOs.

## Measurement design — a decision log, not a stopwatch

- **Design:** 8 weeks. The pipeline drafts every Monday; analysts log per item: *caught by AI first / caught by human first / AI wrong.* Every WBR decision is logged with trigger, owner, deadline and — 4 weeks later — outcome.
- **Evidence of value** = decisions demonstrably taken earlier or better because of the draft (e.g., reorder triggered on day 2 instead of day 9), reviewed with the C-level at week 8.
- **Quality bar:** false-alarm rate < 20% of flagged anomalies; every claim in the draft must cite the underlying figures (no unsourced numbers survive review).
- **Stop criteria:** analysts spend more time correcting than the old assembly took · two consecutive weeks where the draft contains a material numeric error that passed its own citations check.

## Risks

| Risk | Mitigation |
|---|---|
| Hallucinated numbers in an executive document | Every figure cited from the extract; automated recomputation check; analyst sign-off |
| "Interesting" replaces "actionable" | Fixed format: anomaly → size → hypothesis → proposed action → owner |
| C-level treats the draft as truth | Labelled as draft until analyst sign-off; error log reviewed monthly |
| Data extracts are the real bottleneck | Week-1 spike to validate extract quality before promising anything |
