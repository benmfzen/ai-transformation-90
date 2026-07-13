"""Transformation OS — MCP server.

Exposes the 90-day method as tools: any MCP client (Claude Desktop, Claude
Code, …) can debrief interviews into evidence-backed scores, inspect the
portfolio, draft decision memos and run governance red-line checks.

Run: uv run --with "mcp[cli]" --with pyyaml mcp run server.py
"""

import subprocess
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core

mcp = FastMCP(
    "transformation-os",
    instructions=(
        "Tools for running a 90-day AI transformation program: score departments "
        "(evidence required per score), inspect the impact/readiness portfolio, "
        "draft day-30/60/90 decision memos, and check use cases against governance "
        "red lines. Scores persist to the case's org.yaml; sync_outputs regenerates "
        "the dashboard and score tables from it."
    ),
)


@mcp.tool()
def get_scoring_rubric() -> dict:
    """The 6-dimension scoring rubric (anchors per dimension) and the scoring rules.
    Read this before scoring a department."""
    return core.RUBRIC


@mcp.tool()
def get_interview_guide() -> str:
    """The 45-minute lead-interview guide (German): 12 questions in 4 blocks,
    with a debrief checklist. Use it to conduct or debrief an interview."""
    return core.interview_guide()


@mcp.tool()
def list_portfolio() -> dict:
    """Current portfolio: every department with impact, readiness, quadrant and
    role, plus recommended pilots and the deliberately-postponed list."""
    return core.portfolio_summary()


@mcp.tool()
def submit_department_scores(department_id: str, name: str, lead: str, staff: int,
                             scores: dict, evidence: dict, role: str = "") -> dict:
    """Submit scores for a department (all 6 dimensions, integers 1-5).

    EVERY score requires evidence: a verbatim quote from the interview, a metric,
    or a system inspection (>= 20 chars per dimension). Submissions without
    evidence are rejected — that is the method's core rule, enforced.
    Persists to org.yaml; call sync_outputs afterwards to regenerate outputs.
    """
    return core.upsert_department(department_id, name, lead, staff, scores, evidence, role)


@mcp.tool()
def draft_decision_memo(day: int) -> str:
    """Markdown skeleton for the day-30/60/90 executive decision memo
    (result / plan / budget+resolutions), prefilled with the live portfolio."""
    return core.draft_decision_memo(day)


@mcp.tool()
def check_use_case(description: str, data_classes: list | None = None,
                   evaluates_people: bool = False,
                   automated_decision_without_human_review: bool = False,
                   customer_facing: bool = False) -> dict:
    """Deterministic governance red-line check for an AI use-case idea.
    data_classes: any of public, internal, confidential, personal, employee.
    Returns blocked / review_required / fast_track with reasons and required approvals."""
    return core.check_use_case(description, data_classes, evaluates_people,
                               automated_decision_without_human_review, customer_facing)


@mcp.tool()
def sync_outputs() -> str:
    """Regenerate dashboard data and score tables from org.yaml (runs tools/generate.py)."""
    result = subprocess.run(
        [sys.executable, str(core.ROOT / "tools" / "generate.py")],
        capture_output=True, text=True, timeout=30,
    )
    return (result.stdout + result.stderr).strip() or "outputs in sync"


@mcp.prompt()
def interview_debrief(transcript: str) -> str:
    """Debrief a lead interview into evidence-backed scores."""
    return f"""You are debriefing a department-lead interview for a 90-day AI transformation program.

1. Call get_scoring_rubric and read the rules and dimension anchors.
2. Read the transcript below. For each of the 6 dimensions, find the strongest
   piece of EVIDENCE (verbatim quote or concrete fact). If a dimension has no
   evidence in the transcript, say so and score conservatively — never invent.
3. Watch for champion signals: does the lead name a concrete, quantified process
   problem? Have they experimented already? Do they carry weight in the org?
4. Call submit_department_scores with your scores and the evidence per dimension.
5. Call list_portfolio and report where the department lands (quadrant, vs. others)
   and whether your champion assessment changes the pilot recommendation.

Transcript:
{transcript}"""


if __name__ == "__main__":
    mcp.run()
