# ADR-001: Two case tracks instead of one generic framework

**Status:** accepted · 2026-07-13

## Context

The repo started with one fictional case (NORDWERK GmbH, German industrial SME) to make the 90-day method concrete. The method also needs to hold in consumer/e-commerce organizations, where the org shape (D2C + retail channels, marketing-heavy, product data everywhere) and the AI goal types (efficiency *and* growth/opportunity) differ substantially from an industrial SME.

## Decision

Keep the method generic (`playbook/`, `methodik/`) and instantiate it in **two self-contained cases** under `cases/`: NORDWERK (German, industrial, efficiency-heavy) and NATURA Foods (English, omnichannel food, efficiency + opportunity portfolio with business cases, operating model and a working prototype). No real company is named or implied in either case.

## Consequences

- The method's transferability is *demonstrated* rather than claimed — same scoring philosophy, two very different organizations.
- The NATURA track carries the commercial artifacts (costed business cases, buy/build/deprecate, operating model) a consumer business needs; NORDWERK keeps the change-management depth (works council, shop-floor skepticism).
- Cost: two link roots to maintain; mitigated by the CI link check.
