# Case: NATURA Foods SE (fictional)

**An omnichannel food company, ~350 people — the environment this 90-day operating system is calibrated for.**

> Entirely fictional. NATURA, its people and its numbers are invented to make the method concrete. No resemblance to any real company is intended, and nothing here claims knowledge of any real company's internal processes.

## Company snapshot

| | |
|---|---|
| Business | Own-brand food products (snacks, pantry staples, ~600 SKUs) |
| Channels | D2C webshop (8 European markets) · retail & B2B partners · marketplaces |
| People | ~350 across 10 teams |
| Revenue | €120m, growing ~20% YoY |
| Systems | Shop platform, ERP, PIM (partially maintained), helpdesk, BI stack, ad platforms |
| AI status quo | Individual tool usage in marketing and engineering, no portfolio, no shared standards, no measurement |

## Company goals the AI portfolio must serve

AI targets are derived from these goals — never from tool capabilities:

1. **Profitable international growth** — scale into new markets without proportional headcount growth
2. **Marketing efficiency** — more output and better performance per euro of ad and content spend
3. **Lower operating complexity** — fewer manual handoffs in service, supply chain and finance
4. **Better availability** — fewer stockouts and less overstock
5. **Faster launches** — shorter time from product idea to live product page in every market
6. **Scalable localization** — 8 languages today, more tomorrow, without linear cost growth

## The 10 teams

Each team gets **one AI goal per cycle, classified as either Efficiency or Opportunity** — owned by the team lead, not by the AI function (see [operating model](operating-model.md)).

| Team | Lead (fictional) | Size | Primary AI goal type |
|---|---|---|---|
| Customer Service | Mara Willems | 38 | Efficiency — handle time & first-contact resolution |
| Brand & Content | Jonas Petersen | 22 | Efficiency — localization cost & speed |
| Performance Marketing | Aylin Kaya | 26 | Opportunity — creative testing velocity, CRM revenue |
| E-Commerce & Shop | David Osei | 24 | Opportunity — conversion, search, merchandising |
| Retail / B2B Sales | Sofia Lindqvist | 18 | Efficiency — sell-in materials, account prep |
| Purchasing & Supply Chain | Tomasz Brand | 30 | Opportunity — forecasting & availability |
| Product Development | Lena Fischer | 20 | Opportunity — concept screening, spec drafting |
| Finance | Nils Berger | 16 | Efficiency — document processing, reporting |
| People & Culture | Ana Duarte | 10 | Efficiency — drafts & internal FAQ (high-risk uses excluded) |
| Data & Tech | Priya Nair | 28 | Enabler — platform, integrations, standards |

## What's in this case

| Artifact | What it proves |
|---|---|
| [AI Opportunity Portfolio](portfolio.md) | Commercial prioritization: 12 initiatives scored on business value and execution, 3 pilots selected |
| [Business case: CS Copilot](business-cases/cs-copilot.md) | Full value logic — baseline, target, economics, measurement design |
| [Business case: Content Localization](business-cases/content-localization.md) | Efficiency + growth case with food-claims guardrails |
| [Business case: Weekly Business Review](business-cases/weekly-business-review.md) | Opportunity case where value = better decisions, with an honest evidence design |
| [Operating model](operating-model.md) | How 2 central AI people and 10 team leads split ownership at 350 headcount — RACI, rhythms, decision rights |
| [Team lead coaching](team-lead-coaching.md) | From "we want more AI" to a shipped, measured outcome — canvas, example, decision tree |
| [Buy / Build / Deprecate](buy-build-deprecate.md) | Tool landscape decisions with criteria and two worked examples |
| [Working prototype: CS Copilot](../../prototypes/cs-copilot/) | Runnable code with retrieval, structured output, escalation rules and an eval harness |

The generic method behind all of this (90-day phasing, champion scoring) lives in [`playbook/`](../../playbook/) and [`methodik/`](../../methodik/) — developed on the German [NORDWERK case](../nordwerk/nordwerk.md) and adapted here for an omnichannel consumer business.
