# The Method — executive summary (EN)

One-page English summaries of the German core artifacts. Each section links its full original — the German documents remain the working versions ([why](decisions/adr-001-two-case-tracks.md)).

## The 90-day playbook — [full version (DE)](playbook/00-programmueberblick.md)

Three phases, three decision points. The executive team decides on data at days 30, 60 and 90 — the fixed dates are the anchor that keeps the program from being sat out.

| Phase | Days | Leading question | Deliverable | Decision at the end |
|---|---|---|---|---|
| **1 — Assess** | 1–30 | Where is the lever, who wants to pull it? | Impact matrix + champion shortlist | Which 3 pilots? |
| **2 — Pilot** | 31–60 | Does it work measurably? | 3 pilot results vs. frozen baselines | Scale / iterate once / stop — per pilot |
| **3 — Scale** | 61–90 | How does it become normal operations? | 12-month roadmap + operating model | Year-1 budget and structure |

Program principles: champions before use cases (momentum is the scarcest resource) · measure or stop (every pilot has a frozen baseline, target metric and abort criterion **before** it starts — a stopped pilot is the system working) · guardrails over bans (shadow AI gets legalized and channeled) · visibility is part of the work (weekly one-pager, Demo Friday) · no platform decision before day 60.

Each phase has week-level to-do checklists with warning signals (e.g. *"executive team postpones the day-30 review → the program has no real sponsor: escalate"*), and every to-do links a fill-in template — kick-off agenda, decision memos, pilot charter, weekly report, training curriculum, tool clearance checklist, KPI sheet.

## Champion scoring — [full version (DE)](methodik/champion-scoring.md)

Every department is scored 1–5 on six dimensions, giving two axes:

- **Impact — is it worth it?** = repetitiveness · pain · leverage
- **Readiness — can it work now?** = data · lead's willingness · freedom to execute

Rules that keep it objective: **every score needs evidence** (interview quote, metric, or system inspection — "feels like a 4" doesn't count; the [MCP server](mcp-server/) enforces this in code, verifying quotes verbatim against the transcript); four-eyes scoring with mandatory discussion of gaps ≥ 2; the **lead** is scored, not just the department; scores are snapshots, re-scored each phase.

Champions are **recognized, not appointed** — the signals: a concrete quantified process problem of their own, prior experimentation, reach in the organization. The result is a 2×2 matrix ([live](https://benmfzen.github.io/ai-transformation-90/)) that derives the pilot order instead of negotiating it politically — including the discipline to *postpone* the highest-leverage department when its readiness isn't there.

## The pilot charter — [full template (DE)](templates/pilot-charter.md)

Signed by champion, program lead and sponsor before any pilot starts, then **frozen**: one target metric with a measured (not estimated) baseline, team-level measurement only (no individual performance monitoring — a works-council commitment), an explicit abort criterion, a €5k tooling cap, and a fixed decision logic at pilot end (scale / iterate once for 2 weeks / stop). Scope growth and metric redefinition are ruled out by construction — the two ways pilots usually go zombie.

## Governance — [full policy (DE)](governance/ai-richtlinie.md)

Guardrails over bans: AI use is *wanted*, inside clear lanes. A 4-class data classification (public / internal / confidential / personal) maps to which tools may see what. Four non-negotiable red lines: no AI performance monitoring of individuals; no AI screening or ranking of applicants or employees (EU AI Act Annex III high-risk); no automated decisions with legal effect without human review (Art. 22 GDPR); no trade secrets in unapproved tools. New use cases get an answer within 5 working days — slower approvals are how shadow AI wins. Incidents are reported without sanction; the policy is finalized in phase 3 *with* pilot experience, not abstractly at the start. The red lines are executable: [`check_use_case`](mcp-server/) returns blocked / review_required / fast_track deterministically.
