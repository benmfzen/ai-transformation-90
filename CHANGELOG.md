# Changelog

## v0.2.1 — 2026-07-13

Closes the "instruction without artifact" gaps: every playbook to-do now has a fill-in template behind it.

- **Kick-off agenda** (day 1, 60 min) — agenda, 8-slide deck outline, the three commitments that must be secured in the room, warning signs
- **Decision memo template** (day 30/60/90) — the 3-page result/plan/budget structure with per-milestone fill guidance and checkbox resolutions ("acknowledged" is not an outcome)
- **Training curriculum** — the 3-tier program (2h all-hands / 1-day rollout teams / champions) with block-level content; covers the EU AI Act Art. 4 literacy duty
- **Tool clearance checklist** — 30–60 min sign-off across need, privacy/legal (DPA, training-use, data classes), security (SSO, audit log), and operations (TCO, exit path, eval hook)
- **KPI definition sheet** — value / adoption / quality KPIs, each with formula, source, owner, cadence; "time saved counts only when its destination is documented"
- All five linked from the matching playbook to-dos

## v0.2.0 — 2026-07-13

The repo grows from a methodology showcase into a work sample for a Principal AI Transformation role in a consumer/e-commerce company.

- **New case track: NATURA Foods SE** (English) — fictional ~350-person omnichannel food company: company profile, 10 teams with leads
- **AI Opportunity Portfolio** — 12 initiatives scored on Business Value (efficiency / growth / risk-quality) and Execution (incl. *time to evidence*), with the efficiency-vs-opportunity goal split and an explicit "highest value ≠ first pilot" trade-off
- **Three costed business cases** — CS Copilot, Content Localization, AI-drafted Weekly Business Review: baselines, value math, payback, confidence, measurement design with stop criteria, and value-*realization* logic (what happens with freed time)
- **Working prototype: CS Copilot** — grounded drafts from FAQ + order data, hard escalation rules, 20-case eval harness with CI gates, optional fact-preserving LLM polish (`claude-opus-4-8`)
- **Operating model for 350 people** — central AI function (2 FTE) vs. team-lead ownership, RACI, rhythms, and what the central function refuses to do
- **Team lead coaching artifacts** — AI Goal Canvas (filled example), vague-goal-to-outcome conversation, stop/iterate/scale decision tree, difficult-conversation example, lead scorecard
- **Buy / Build / Deprecate framework** — decision table, assessment dimensions, two worked examples (CS copilot build-vs-buy with exit clause; tool consolidation), tool register
- **Repo as product** — restructured into `cases/`, CI (tests + eval gates + link check), ADRs, this changelog
- README rewritten as an English executive landing page

## v0.1.0 — 2026-07-13

Initial release: the 90-day operating system on the NORDWERK case (German).

- 90-day playbook in three phases with to-dos, deliverables and abort criteria
- NORDWERK GmbH case: 9 department profiles with leads, key data and score rationale
- Champion scoring model (6 dimensions) + evaluated impact matrix
- 4 reusable templates (interview guide, use-case canvas, pilot charter, status report)
- AI governance policy (guardrails over bans, EU AI Act red lines)
- Interactive dashboard (impact matrix, scoring heatmap, timeline) on GitHub Pages
