"""Program clock: the 90-day playbook as structured, day-addressable to-dos.

Mirrors playbook/01..03 (German originals are the source of truth for prose;
this is the machine-readable English version the assistant works from).
"""

from datetime import date

TEMPLATES = "templates/"

PHASES = [
    {"n": 1, "days": (1, 30), "name": "Assess",
     "question": "Where is the biggest AI lever, and who wants to pull it?",
     "warning_signals": [
         "Executive team postpones the day-30 review → no real sponsor: escalate, no phase 2 without a decision date",
         "No lead scores above readiness 3 → org not pilot-ready: replace phase 2 with an enablement sprint",
         "IT blocks every data access → governance problem, not tech: pull the policy discussion forward",
     ]},
    {"n": 2, "days": (31, 60), "name": "Pilot",
     "question": "Does it work measurably — in the real process, with real people?",
     "warning_signals": [
         "Pilot quietly grows into a project → charter rules, extensions are phase-3 material",
         "Metric gets redefined after disappointing interim results → baseline and target are frozen",
         "Enthusiastic individuals but no process effect → measure at team level, not per person",
     ]},
    {"n": 3, "days": (61, 90), "name": "Scale",
     "question": "How do 3 pilots become normal operations — with structure, budget, owners?",
     "warning_signals": [
         "Pilots succeed but nothing scales → scale decision must be pre-scheduled with resourcing named",
         "Tool sprawl returns → every new tool names what it replaces",
     ]},
]

BLOCKS = [
    {"days": (1, 7), "phase": 1, "title": "Week 1 — setup & org scan", "todos": [
        {"t": "Kick-off with the executive team: secure the three commitments (review dates in calendars, named sponsor, access without per-department approvals)", "template": f"{TEMPLATES}kickoff-agenda.md"},
        {"t": "Inform the works council — BEFORE the first interview, not after"},
        {"t": "Collect org chart + key data per department: headcount, core processes, systems, known pain points"},
        {"t": "Shadow-AI inventory: who already uses what today? (anonymous, amnesty framing)"},
        {"t": "Book interviews with all department leads (45 min each)", "template": f"{TEMPLATES}interview-leitfaden.md"},
    ]},
    {"days": (8, 19), "phase": 1, "title": "Weeks 2-3 — lead interviews", "todos": [
        {"t": "Run the interviews: core processes, time sinks, data reality, attitude, 'what would you automate if it were easy?'", "template": f"{TEMPLATES}interview-leitfaden.md"},
        {"t": "Right after each interview: complete the department profile and submit provisional scores WITH evidence (submit_department_scores)"},
        {"t": "IT deep-dive in parallel: system landscape, data accessibility, security requirements, existing contracts"},
        {"t": "Note quick-win candidates: anything doable with existing tools in < 2 weeks"},
    ]},
    {"days": (20, 30), "phase": 1, "title": "Week 4 — scoring & decision", "todos": [
        {"t": "Finalize all scores four-eyes: a second person scores independently, discuss gaps >= 2"},
        {"t": "Build the impact matrix and derive the pilot order (list_portfolio)"},
        {"t": "Champion shortlist: max 3 names, with interview evidence"},
        {"t": "Write use-case canvases for the top departments", "template": f"{TEMPLATES}use-case-canvas.md"},
        {"t": "Day-30 review: send the decision memo 48h ahead; decide 3 pilots + champions + phase-2 budget", "template": f"{TEMPLATES}entscheidungsvorlage.md"},
    ]},
    {"days": (31, 37), "phase": 2, "title": "Week 5 — pilot setup", "todos": [
        {"t": "One signed charter per pilot: target metric, frozen baseline, abort criterion, champion, time budget", "template": f"{TEMPLATES}pilot-charter.md"},
        {"t": "Measure baselines BEFORE starting (e.g. 2 weeks of handle-time data, retroactively)"},
        {"t": "Minimal tooling via existing contracts; clearance checklist per tool", "template": f"{TEMPLATES}tool-checkliste.md"},
        {"t": "Privacy quick-check per pilot against the AI policy (which data may go in?)"},
        {"t": "Name pilot teams: 3-5 people each, volunteers, picked by the champion"},
    ]},
    {"days": (38, 58), "phase": 2, "title": "Weeks 6-8 — pilots running", "todos": [
        {"t": "Weekly 30-min check-in per pilot: metric movement, blockers, next week"},
        {"t": "Demo Friday: 20 minutes, open to all, champions show real work results"},
        {"t": "Log blockers centrally (data access, permissions, quality) — raw material for the phase-3 operating model"},
        {"t": "Weekly one-pager to the executive team", "template": f"{TEMPLATES}status-report.md"},
        {"t": "From day 50: consolidate measurements, interview pilot teams (acceptance, effort, limits)"},
    ]},
    {"days": (59, 60), "phase": 2, "title": "Day 59-60 — pilot review", "todos": [
        {"t": "Check results against charters: target met? abort criterion hit?"},
        {"t": "Per pilot one decision: scale / iterate once (2 weeks max) / stop — send memo 48h ahead", "template": f"{TEMPLATES}entscheidungsvorlage.md"},
        {"t": "Champions present to the executive team themselves — not the program lead"},
        {"t": "Document lessons: what does scaling need in data, permissions, training, support?"},
    ]},
    {"days": (61, 74), "phase": 3, "title": "Weeks 10-11 — rollout & governance", "todos": [
        {"t": "Rollout plan per scaled pilot: pilot team → full department, with training plan and support path"},
        {"t": "Finalize the AI policy with works council + privacy — now, informed by real pilot experience"},
        {"t": "Tooling decision based on what pilots actually needed", "template": f"{TEMPLATES}tool-checkliste.md"},
        {"t": "Value math per rollout: saved hours x cost vs. license + operations (assume adoption < 100%)"},
        {"t": "Prepare wave 2: next departments from the matrix, with use-case canvases"},
    ]},
    {"days": (75, 84), "phase": 3, "title": "Week 12 — operating model & enablement", "todos": [
        {"t": "Fix the operating model: small central AI function + champions in the line, RACI, rhythms"},
        {"t": "Formalize the champion role: 10% time budget, mandate, monthly circle"},
        {"t": "Launch the 3-tier training program", "template": f"{TEMPLATES}schulungsprogramm.md"},
        {"t": "Define the year-1 KPI set: every metric with formula, source, owner, cadence", "template": f"{TEMPLATES}kpi-definitionen.md"},
        {"t": "Make Demo Friday permanent; intranet page with approved use cases + prompts"},
    ]},
    {"days": (85, 90), "phase": 3, "title": "Week 13 — roadmap & decision", "todos": [
        {"t": "12-month roadmap: rollout waves, data groundwork projects, budget, milestones"},
        {"t": "Day-90 decision memo: 1 page result, 1 page plan, 1 page budget — 48h ahead", "template": f"{TEMPLATES}entscheidungsvorlage.md"},
        {"t": "Board decision: year-1 budget and operating model, champions publicly named"},
        {"t": "Program retro: what moves to the AI function, what stays in the line?"},
    ]},
]

MILESTONES = {30: "Pilot selection (executive review)", 60: "Pilot review: scale / iterate / stop", 90: "Board decision: year-1 budget & operating model"}


def day_from_start(start_iso: str, today: date | None = None) -> int:
    start = date.fromisoformat(start_iso)
    return ((today or date.today()) - start).days + 1


def todos_for_day(program_day: int) -> dict:
    if program_day < 1:
        return {"program_day": program_day, "status": f"program starts in {1 - program_day} day(s)",
                "prepare": [b for b in BLOCKS if b["days"][0] == 1][0]}
    if program_day > 90:
        return {"program_day": program_day, "status": "the 90 days are over — year-1 roadmap and KPI cadence apply now",
                "reference": f"{TEMPLATES}kpi-definitionen.md"}
    phase = next(p for p in PHASES if p["days"][0] <= program_day <= p["days"][1])
    block = next(b for b in BLOCKS if b["days"][0] <= program_day <= b["days"][1])
    next_milestone = next((d for d in sorted(MILESTONES) if d >= program_day), None)
    return {
        "program_day": program_day,
        "phase": {"n": phase["n"], "name": phase["name"], "days": list(phase["days"]), "leading_question": phase["question"]},
        "current_block": {"title": block["title"], "days": list(block["days"]), "todos": block["todos"]},
        "next_milestone": {"day": next_milestone, "in_days": next_milestone - program_day,
                           "what": MILESTONES[next_milestone]},
        "warning_signals": phase["warning_signals"],
    }
