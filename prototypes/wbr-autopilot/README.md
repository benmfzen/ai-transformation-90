# WBR Autopilot — the repo runs a weekly routine

**Every Monday at 06:00 UTC, a GitHub Action drafts the Weekly Business Review for the fictional NATURA Foods SE and opens a pull request** — the working prototype behind [business case 3](../../cases/natura-foods/business-cases/weekly-business-review.md), running as an actual routine instead of a demo. Check the [open PRs](https://github.com/benmfzen/ai-transformation-90/pulls?q=is%3Apr+wbr) to see it live.

```
Monday 06:00 ─► generate week data ─► detect anomalies ─► draft memo ─► VERIFY ─► pull request
   (cron)        (deterministic,       (thresholds,        (ranked by     every number      (analyst
                  seeded CSVs)          not vibes)          EUR at stake)  recomputed        reviews &
                                                                           or no PR)         merges)
```

## What it proves

1. **Routines, not demos** — the artifact renews itself weekly without anyone touching it; the PR history is the audit trail.
2. **No unsourced numbers survive** — `verify.py` independently recomputes every figure in the memo from the source CSVs and counts the anomaly sections; a tampered total or an invented finding blocks the PR (tested).
3. **The analyst stays in the loop** — the PR *is* the human review step from the business case: check hypotheses, add judgment, merge to accept. The autopilot drafts, it never decides.
4. **Deterministic core** (same ISO week → same data → same memo), so the whole loop is testable in CI with zero secrets and zero API cost — same philosophy as [ADR-002](../../decisions/adr-002-prototype-offline-first.md).

## What it detects

| Signal | Threshold | Proposed action pattern |
|---|---|---|
| Channel revenue week-over-week | ±15% | diagnose funnel/tracking before believing demand shifts |
| Campaign ROAS | < 1.5 | pause or cut 50% today — below breakeven daily |
| Stock cover | < 1.5 weeks demand | expedite reorder, check supplier lead time |

Findings are ranked by EUR at stake, each with hypothesis, action and owner — the memo format from the business case.

## Run it locally

```bash
python3 -m wbr.run_week            # current ISO week: data/ + outputs/wbr-YYYY-wWW.md + verify
python3 -m wbr.run_week 2026 29    # any specific week (deterministic)
python3 -m pytest tests/ -q        # 8 tests incl. tamper detection
```

## Honest limits

The data is synthetic and the anomalies are injected — the point is the **operating pattern** (scheduled generation → gated verification → human-review PR), which transfers 1:1 to real extracts: swap `gen_week.py` for a warehouse query and everything downstream stays. An optional LLM narrative layer (hypothesis prose from a model, numbers still gated) is deliberately not wired into CI — see ADR-002.
