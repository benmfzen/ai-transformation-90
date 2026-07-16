# Changelog

## v0.4.2 — 2026-07-16

Repositioning: from work sample to **transformation copilot**.

- README leads with the copilot framing ("the method plus the software to run it — swap the fictional org for yours and the copilot runs your program"); proof-piece table reworded from candidate questions to program questions
- Repo description, dashboard subtitle/footer and ADR wording generalized accordingly; application-specific phrasing removed


## v0.4.1 — 2026-07-13

Curation release — presentation over features (per external review: "weniger weiterbauen, mehr präsentieren").

- **Guided tour** in the README: 5 / 15 / 45-minute paths through the repo
- **Outcome sentence** under the title: what is different after 90 days
- **[METHOD.md](METHOD.md)** — English executive summaries of the German core artifacts (playbook, champion scoring, pilot charter, governance)
- **Demo GIF** for the CS Copilot: grounded draft with cited sources, then the deterministic health escalation (closes #6)
- MCP proof piece reframed benefit-first ("paste a transcript …"), technology second
- Issue hygiene: #3 closed with shipped-in-v0.4.0 note, #5 rescoped


## v0.4.0 — 2026-07-13

Agentic operations complete: the repo now runs a routine, and scoring gets a second pair of eyes.

- **WBR autopilot** (`prototypes/wbr-autopilot/` + `.github/workflows/wbr.yml`) — every Monday 06:00 UTC a GitHub Action generates the week's fictional extracts (deterministic, seeded), detects anomalies by threshold (channel WoW ±15%, ROAS < 1.5, stock cover < 1.5 weeks), drafts the Weekly Business Review ranked by EUR at stake (hypothesis + action + owner per finding) and opens a pull request — the analyst review from business case 3 as a merge decision. `verify.py` recomputes every figure and the anomaly count before the PR opens; tampered or invented numbers block it (tested)
- **Four-eyes calibration** — `compare_submissions` tool flags dimensions where two independent scorings diverge ≥ 2 (must be resolved with evidence, never averaged), warns when the disagreement flips the portfolio quadrant; `four_eyes_debrief` prompt orchestrates operator-eye + skeptic-eye passes
- 37 tests across prototypes and MCP core


## v0.3.2 — 2026-07-13

Anti-hallucination gate: evidence quotes are now verified against the source.

- `submit_department_scores` accepts `source_text` (the transcript/notes): every quotation-marked span in the evidence is checked **verbatim** against the source (whitespace-, case- and typography-normalized) — fabricated quotes are rejected with "quote not found verbatim in source"
- Evidence not from the source must declare itself with a `metric:` or `system:` prefix; unquoted, undeclared evidence is rejected when a source is provided
- `interview_debrief` prompt updated to always pass the transcript; submission result reports the verification status

## v0.3.1 — 2026-07-13

The MCP server becomes a 90-day assistant: a program clock joins the method tools.

- **`get_todos`** — day-addressable playbook: current phase with leading question, this block's to-dos (with template paths), next milestone countdown, phase warning signals — cross-checked against the live program state (departments scored, recommended pilots), so gaps surface in conversation ("2 interviews still missing before day 30")
- **`set_program_start`** — persists day 1 to org.yaml; `get_todos` then computes the current program day automatically
- Machine-readable playbook (`mcp-server/program.py`): 9 blocks covering all 90 days exactly once (property-tested), 3 milestones, per-phase warning signals

## v0.3.0 — 2026-07-13

The method becomes operational: one source of truth for all scores, and the playbook as an installable MCP server.

- **Single source of truth** — all NORDWERK scores live in `cases/nordwerk/org.yaml`; `tools/generate.py` generates the dashboard data (`docs/data.js`) and the score table in the impact matrix from it. CI fails when outputs drift (`--check`)
- **Transformation OS MCP server** (`mcp-server/`) — the method as tools for any MCP client: `get_scoring_rubric`, `get_interview_guide`, `submit_department_scores` (**rejects scores without ≥20 chars of evidence per dimension** — the method's core rule enforced in code), `list_portfolio` (live quadrants + pilot recommendation), `draft_decision_memo` (day 30/60/90, prefilled with the live portfolio), `check_use_case` (deterministic AI-Act/GDPR red-line check → blocked/review/fast-track), `sync_outputs`, plus an `interview_debrief` prompt wiring the full flow
- Core logic is MCP-free and CI-tested (9 tests); dashboard now reads generated `data.js` and fills stat tiles from the same source

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
