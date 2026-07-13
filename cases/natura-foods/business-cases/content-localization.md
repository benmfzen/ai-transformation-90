# Business Case — Pilot 2: Product Content Localization Engine

**Type:** Efficiency (with a growth tail) · **Owner:** Jonas Petersen (Brand & Content)

## Problem

~120 product launches and relaunches per year, each needing product page, SEO metadata and shop copy in **8 locales**. Today: external agency per locale (€140/SKU/locale average), 10 working days lead time, inconsistent terminology, and food-claim risks handled by ad-hoc review. Localization is the bottleneck for both launch speed and market expansion.

## Solution shape

Generation pipeline on top of structured PIM data: product facts, ingredients, nutrition, tone-of-voice guide and a **market-specific claims rulebook** go in; localized product description, SEO metadata and social copy come out — with warnings where source data is missing and hard blocks where copy would touch regulated claims. Native-speaker review and sign-off is mandatory per locale; the pipeline produces drafts, never publishes.

## Baseline (frozen)

| Metric | Value |
|---|---|
| Launches needing localization | 120/year × 8 locales = 960 localization jobs |
| External cost | €140/job avg → **€134k/year** |
| Lead time (brief → all locales live) | 10 working days |
| Internal coordination | ~1.5 h/job (briefing, chasing, QA) |
| Claim-related corrections post-publish | ~2/quarter |

## Target

**Localization cost −60%** and **lead time 10 → 3 working days**, at equal review quality and zero unreviewed regulated claims.

## Value logic

```
External cost
  6 of 8 locales move to draft-generation + native review   (2 premium locales stay agency)
  960 jobs: 720 × (€140 − €45 review cost)                  ≈ €68k/year saved
Internal coordination
  −0.75 h/job × 960 × €42/h                                 ≈ €30k/year capacity

Cost (year 1)
  Build (10 person-days) + claims rulebook with legal        ≈ €10k one-off
  LLM usage                                                  ≈ €3k/year
  Terminology/glossary upkeep (Brand team, 0.05 FTE)         ≈ €4k/year

Net year-1 value                                             ≈ €81k   ·   Payback ≈ 6 weeks
Confidence: 65% (draft quality per locale is the open question — hence the pilot)
```

**Growth tail (tracked, not counted in the case):** 7 days faster per launch ≈ one extra week of shelf life per new SKU per market; and market expansion stops being gated by localization capacity — the strategic reason this is Pilot 2 even though pure savings would rank others close.

## Measurement design

- **Design:** 20 launches through the pipeline vs. the last 20 agency-only launches (matched by category). Per locale: reviewer effort (minutes), edit distance, quality rubric.
- **Quality rubric:** native reviewers score fluency, brand tone, factual accuracy against PIM data; pipeline drafts must reach "publishable with light edits" in ≥ 80% of jobs.
- **Compliance gate:** 100% of regulated-claim triggers (health/nutrition claims, allergen wording) must be flagged or blocked — tested against a seeded adversarial set before any real launch, then continuously.
- **Stop criteria:** any unflagged regulated claim reaching review stage twice · reviewer effort > 60% of writing from scratch (then the drafts aren't drafts).

## Risks

| Risk | Mitigation |
|---|---|
| EU food claims (Reg. 1924/2006) in generated copy | Rulebook as hard filter, legal-approved blocklist, human sign-off per locale |
| Terminology drift across 8 markets | Locked glossary per market, part of the prompt and the eval |
| Brand voice flattening | Tone guide in context + Brand team owns the rubric, not the AI team |
| PIM data gaps produce confident nonsense | Pipeline warns on missing source fields instead of filling gaps |
