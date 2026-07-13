# Transformation OS — the method as an MCP server

**The 90-day playbook, installable.** This MCP server exposes the program's method as tools — any MCP client (Claude Code, Claude Desktop, …) can debrief interviews into evidence-backed scores, inspect the live portfolio, draft executive decision memos and run governance red-line checks. The intelligence stays in the client model; the server enforces the method.

## The demo (60 seconds)

Connect the server, then paste an interview transcript and say *"debrief this for the Quality department"*. The model will:

1. pull the scoring rubric (`get_scoring_rubric`) and the interview guide,
2. extract evidence per dimension from the transcript,
3. submit scores via `submit_department_scores` — **which rejects any score without evidence** (the method's core rule, enforced in code, not in the prompt),
4. show where the department lands in the portfolio (`list_portfolio`),
5. optionally regenerate the dashboard from the new scores (`sync_outputs`).

The scores persist to [`cases/nordwerk/org.yaml`](../cases/nordwerk/org.yaml) — the same single source of truth the [dashboard](https://benmfzen.github.io/ai-transformation-90/) and the score tables are generated from.

## Install

With [uv](https://docs.astral.sh/uv/) (no local Python setup needed):

```bash
# Claude Code
claude mcp add transformation-os -- uv run --with "mcp[cli]" --with pyyaml \
  mcp run /path/to/ai-transformation-90/mcp-server/server.py
```

```json
// Claude Desktop (claude_desktop_config.json)
{
  "mcpServers": {
    "transformation-os": {
      "command": "uv",
      "args": ["run", "--with", "mcp[cli]", "--with", "pyyaml",
               "mcp", "run", "/path/to/ai-transformation-90/mcp-server/server.py"]
    }
  }
}
```

## Tools

| Tool | What it does |
|---|---|
| `get_scoring_rubric` | The 6 dimensions with 1/5 anchors + the scoring rules |
| `get_interview_guide` | The 45-min lead-interview guide (12 questions, debrief checklist) |
| `submit_department_scores` | Persist scores — **rejected without ≥20 chars of evidence per dimension** |
| `list_portfolio` | Live matrix: impact, readiness, quadrant, recommended pilots, deliberately-postponed list |
| `draft_decision_memo` | Day-30/60/90 executive memo skeleton, prefilled with the live portfolio |
| `check_use_case` | Deterministic governance red-line check (AI Act Annex III, Art. 22 GDPR, data classes) → blocked / review_required / fast_track |
| `sync_outputs` | Regenerate dashboard + score tables from org.yaml |

Plus the `interview_debrief` prompt, which wires steps 1–5 above together.

## Design decisions

- **Client reasons, server enforces.** The LLM reads transcripts and argues about scores; the server holds the rubric, validates evidence, computes quadrants and blocks red-line use cases. Policy is code — a persuasive model cannot talk its way past `evaluates_people=true`.
- **Core logic has zero MCP dependency** ([`core.py`](core.py)) — CI tests it on every push without installing the MCP stack ([`tests/`](tests/)).
- **Same SSOT as everything else:** scores written here show up in the dashboard after `sync_outputs`. One `org.yaml`, three consumers (dashboard, docs, MCP).
