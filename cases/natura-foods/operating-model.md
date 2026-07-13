# Operating Model — AI at 350 People

**Design principle: outcomes stay in the line, standards stay central.** A two-person central AI function cannot — and should not — own the results of ten teams. It owns the portfolio, the platform and the coaching; team leads own their business outcomes. This is the only model that scales past the pilot phase without the central function becoming the bottleneck.

## Central roles

**Principal AI Transformation (this role)**
- AI portfolio: intake, [scoring](portfolio.md), pilot slots, kill/scale decisions (proposal — final call per decision rights below)
- Target system: every team's Efficiency/Opportunity goal, negotiated with the lead
- Coaching the ten team leads ([how](team-lead-coaching.md))
- [Buy/build/deprecate](buy-build-deprecate.md) proposals and vendor strategy
- Executive reporting and escalations
- Hands-on prototyping where it de-risks a decision ([example](../../prototypes/cs-copilot/))

**AI Senior Manager (platform)**
- Shared platform: model access, retrieval infrastructure, integration patterns
- Security controls, access management, logging, cost monitoring
- Tool enablement and technical standards (prompt/versioning conventions, eval harnesses)
- Second pair of hands on pilots

## Decentralized roles

| Role | Owns |
|---|---|
| **Team leads (10)** | The business outcome, the process change, adoption in their team, staffing their side of the pilot. If a lead won't own it, the initiative doesn't run. |
| **AI champions** (1–2/team, grown not appointed) | Local application, feedback into the portfolio, peer enablement, documented recipes |
| **Data/Legal/Security** | Data access approvals, DPAs, risk assessment, red-line enforcement (fast-track SLA: 5 working days) |

## Decision rights (RACI)

| Decision | Principal AI | Team Lead | AI Sr. Mgr | C-level | Legal/Sec |
|---|---|---|---|---|---|
| Team AI goal (Efficiency/Opportunity) | A | R | C | I | — |
| Pilot slot allocation | R | C | C | **A** | — |
| Pilot design, metrics, stop criteria | A | R | C | I | C |
| Stop / iterate / scale a pilot | R (on evidence) | R | C | **A** (scale only) | — |
| Tool buy/build/deprecate | R | C | R | **A** (> €25k) | C |
| Data access for a use case | C | R | C | — | **A** |
| Production standard exceptions | R | C | R | A | C |

A = accountable, R = responsible, C = consulted, I = informed. The deliberate asymmetry: the Principal is **accountable for the quality of the portfolio and proposals**, the line is accountable for outcomes, the C-level for money and scaling.

## Rhythms

| Cadence | Format | Content |
|---|---|---|
| Weekly | Pilot review (30 min/pilot) | Metric movement, blockers, next week |
| Bi-weekly | AI office hours (open) | Any team, any question, demo-friendly |
| Monthly | Portfolio Council (Principal, leads with active initiatives, AI Sr. Mgr) | Re-score, slot decisions, kill/promote |
| Monthly | Champions circle | Recipes, cross-team reuse, friction list |
| Quarterly | C-level review | Validated value, adoption, decisions needed, next quarter's slots |

## What the central function refuses to do

Written down because scope creep kills two-person teams:

1. **No ticket queue.** The AI function is not first-level support for every tool question — office hours and champions absorb that.
2. **No proxy ownership.** If a pilot's team lead skips two weekly reviews, the pilot pauses — it does not migrate to the AI team.
3. **No shadow IT.** Everything runs through the platform standards, including the Principal's own prototypes.
4. **No strategy theater.** Any document without a decision, an owner or a metric attached doesn't get written.

## Failure modes this model is designed against

| Failure mode | Countermeasure |
|---|---|
| Central team becomes the bottleneck | Outcomes in the line; platform not projects; champions absorb long-tail |
| Leads outsource thinking to the AI team | Goal-setting is negotiated, coaching replaces doing ([canvas](team-lead-coaching.md)) |
| Pilots succeed, nothing scales | Scale decision pre-scheduled with the C-level at pilot end; rollout resourcing named in the charter |
| Tool sprawl returns | Quarterly [deprecation review](buy-build-deprecate.md); every new tool names what it replaces |
