"""Transformation OS — core logic (no MCP dependency, fully testable).

The method as functions: scoring rubric, evidence-gated score submission,
portfolio math, decision-memo drafting, governance red-line checks.
The MCP layer in server.py is a thin wrapper around this module.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ORG_PATH = ROOT / "cases" / "nordwerk" / "org.yaml"
INTERVIEW_GUIDE = ROOT / "templates" / "interview-leitfaden.md"

MIN_EVIDENCE_CHARS = 20

RUBRIC = {
    "rules": [
        "Every score needs evidence: a quote from the interview, a metric, or a system inspection. 'Feels like a 4' does not count.",
        "Score the lead, not just the department: willingness measures whether the lead pulls.",
        "A concrete, quantified process problem named by the lead is a strong signal; 'AI is the future' is a weak one.",
        "Scores are snapshots — re-score after every program phase.",
    ],
    "dimensions": {
        "repetitiveness": {"axis": "impact", "question": "How much of the work follows recurring patterns?",
                           "anchor_1": "every case is unique", "anchor_5": ">40% clearly typable standard cases"},
        "pain": {"axis": "impact", "question": "How much does the department suffer today?",
                 "anchor_1": "runs relaxed", "anchor_5": "backlog, overload, measurable follow-up costs"},
        "leverage": {"axis": "impact", "question": "How directly does an improvement hit the business?",
                     "anchor_1": "internal edge process", "anchor_5": "directly revenue- or core-process-relevant"},
        "data": {"axis": "readiness", "question": "Is the needed data digital, accessible, usable?",
                 "anchor_1": "paper / people's heads", "anchor_5": "clean and structured in a system"},
        "willingness": {"axis": "readiness", "question": "Does the lead pull — and can the team follow?",
                        "anchor_1": "active resistance", "anchor_5": "lead drives it, asks proactively"},
        "freedom": {"axis": "readiness", "question": "How many legal/political hurdles are in the way?",
                    "anchor_1": "AI-Act high-risk, works-council conflict", "anchor_5": "hardly any sensitive data, clear path"},
    },
}

DIMS = list(RUBRIC["dimensions"].keys())


# ---------- org / portfolio ----------

def load_org(path: Path = ORG_PATH) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def save_org(org: dict, path: Path = ORG_PATH) -> None:
    Path(path).write_text(yaml.dump(org, allow_unicode=True, sort_keys=False), encoding="utf-8")


def averages(scores: dict) -> tuple:
    imp = sum(scores[d] for d in DIMS if RUBRIC["dimensions"][d]["axis"] == "impact") / 3
    rea = sum(scores[d] for d in DIMS if RUBRIC["dimensions"][d]["axis"] == "readiness") / 3
    return round(imp, 2), round(rea, 2)


def quadrant(impact: float, readiness: float, thresholds: dict | None = None) -> str:
    t = thresholds or {"readiness": 3.0, "impact": 3.5}
    if impact >= t["impact"]:
        return "pilot-now" if readiness >= t["readiness"] else "build-first"
    return "quick-win-or-enabler" if readiness >= t["readiness"] else "later"


def portfolio_summary(org: dict | None = None) -> dict:
    org = org or load_org()
    rows = []
    for d in org["departments"]:
        imp, rea = averages(d["scores"])
        rows.append({
            "id": d["id"], "name": d["name"], "lead": d["lead"], "staff": d["staff"],
            "impact": imp, "readiness": rea,
            "quadrant": quadrant(imp, rea, org.get("thresholds")),
            "role": d.get("role", ""),
        })
    rows.sort(key=lambda r: (r["impact"], r["readiness"]), reverse=True)
    pilots = [r for r in rows if r["quadrant"] == "pilot-now"][:3]
    build = [r for r in rows if r["quadrant"] == "build-first"]
    return {
        "departments": rows,
        "recommended_pilots": [r["name"] for r in pilots],
        "build_readiness_first": [
            f"{r['name']} (impact {r['impact']}, readiness {r['readiness']}) — highest leverage without readiness: data groundwork before piloting"
            for r in build
        ],
        "principles": [
            "Champions before use cases — pilot where the lead pulls.",
            "Time to evidence beats theoretical value — early proof buys trust for everything later.",
            "A low score is a statement about timing, not about the department.",
        ],
    }


# ---------- evidence-gated score submission ----------

import re

QUOTE_RE = re.compile(r'["“„»«\'‘‚]([^"“”„»«\'‘’‚]{12,})["”“«»\'’‘]')
NON_SOURCE_PREFIXES = ("metric:", "system:")
MIN_QUOTE_CHARS = 12


def _normalize(text: str) -> str:
    """Whitespace/case/typography-insensitive form for verbatim matching."""
    text = text.lower()
    for src, dst in (("’", "'"), ("‘", "'"), ("‚", "'"), ("`", "'"),
                     ("“", '"'), ("”", '"'), ("„", '"'), ("«", '"'), ("»", '"'),
                     ("­", ""), ("–", "-"), ("—", "-")):
        text = text.replace(src, dst)
    return " ".join(text.split())


def verify_against_source(evidence_text: str, source_norm: str) -> str | None:
    """Check one evidence entry against the source. Returns an error or None.

    Contract: evidence quoting the source must contain the quote in quotation
    marks — every quoted span is checked VERBATIM (whitespace/case-insensitive).
    Evidence from outside the source (a metric, a system inspection) must be
    prefixed 'metric:' or 'system:' to be exempt from verification.
    """
    stripped = evidence_text.strip().lower()
    if stripped.startswith(NON_SOURCE_PREFIXES):
        return None
    spans = [s.strip() for s in QUOTE_RE.findall(evidence_text) if len(_normalize(s)) >= MIN_QUOTE_CHARS]
    if not spans:
        return ("no verifiable quote: wrap the verbatim source quote in quotation marks, "
                "or prefix evidence from outside the source with 'metric:' or 'system:'")
    for span in spans:
        if _normalize(span) not in source_norm:
            return f"quote not found verbatim in source: “{span[:80]}”"
    return None


def validate_submission(scores: dict, evidence: dict, source_text: str | None = None) -> list:
    """The core rule of the method, enforced: no score without evidence."""
    errors = []
    for dim in DIMS:
        if dim not in scores:
            errors.append(f"missing score: {dim}")
            continue
        v = scores[dim]
        if not isinstance(v, int) or not 1 <= v <= 5:
            errors.append(f"{dim}: score must be an integer 1-5, got {v!r}")
        ev = (evidence or {}).get(dim, "")
        if not isinstance(ev, str) or len(ev.strip()) < MIN_EVIDENCE_CHARS:
            errors.append(
                f"{dim}: evidence required (>= {MIN_EVIDENCE_CHARS} chars) — quote the interview, "
                f"a metric, or a system inspection. 'Feels like a {scores.get(dim)}' does not count."
            )
        elif source_text:
            err = verify_against_source(ev, _normalize(source_text))
            if err:
                errors.append(f"{dim}: {err}")
    unknown = set(scores) - set(DIMS)
    if unknown:
        errors.append(f"unknown dimensions: {sorted(unknown)}")
    return errors


def upsert_department(dept_id: str, name: str, lead: str, staff: int,
                      scores: dict, evidence: dict, role: str = "",
                      source_text: str | None = None,
                      org_path: Path = ORG_PATH, write: bool = True) -> dict:
    errors = validate_submission(scores, evidence, source_text)
    if errors:
        return {"accepted": False, "errors": errors}
    org = load_org(org_path)
    entry = {
        "id": dept_id, "name": name, "name_de": name, "lead": lead, "staff": staff,
        "scores": {d: scores[d] for d in DIMS},
        "evidence": {d: evidence[d].strip() for d in DIMS},
        "role": role or "unassigned",
        "role_de": role or "unassigned",
    }
    existing = next((i for i, d in enumerate(org["departments"]) if d["id"] == dept_id), None)
    if existing is not None:
        old = org["departments"][existing]
        entry["profile"] = old.get("profile", "")
        # keep curated German name always; keep curated German role unless a new role was given
        if old.get("name_de"):
            entry["name_de"] = old["name_de"]
        if not role and old.get("role_de"):
            entry["role_de"] = old["role_de"]
            entry["role"] = old.get("role", entry["role"])
        org["departments"][existing] = {**old, **entry}
    else:
        org["departments"].append(entry)
    if write:
        save_org(org, org_path)
    imp, rea = averages(entry["scores"])
    return {
        "accepted": True,
        "department": name,
        "impact": imp,
        "readiness": rea,
        "quadrant": quadrant(imp, rea, org.get("thresholds")),
        "evidence_verification": "quotes verified verbatim against source" if source_text
                                 else "no source provided — quotes NOT verified",
        "written_to": str(org_path) if write else None,
        "next_step": "run sync_outputs to regenerate dashboard and score tables",
    }


# ---------- decision memos ----------

MEMO_FOCUS = {
    30: ("Pilot selection", "Present the impact matrix, decide the 3 pilots + champions, release phase-2 budget."),
    60: ("Pilot review", "Per pilot: target metric vs. baseline vs. result — decide scale / iterate once / stop."),
    90: ("Year-1 decision", "Validated value, adoption, operating model — decide budget and structure for year 1."),
}


def draft_decision_memo(day: int, org: dict | None = None) -> str:
    if day not in MEMO_FOCUS:
        raise ValueError("day must be 30, 60 or 90")
    title, focus = MEMO_FOCUS[day]
    p = portfolio_summary(org)
    lines = [
        f"# Decision memo — day {day}: {title}",
        "",
        f"_Rule: sent 48h before the meeting; 'acknowledged' is not an outcome. Focus: {focus}_",
        "",
        "## Page 1 — Result",
        "- **Core statement (one sentence):** …",
        "- **Evidence (3-5 numbers vs. baseline):** …",
        "- **What did not work (before the successes, if it changes the decision):** …",
        "",
        "### Current portfolio",
        "| Department | Impact | Readiness | Quadrant | Role |",
        "|---|---|---|---|---|",
    ]
    for r in p["departments"]:
        lines.append(f"| {r['name']} | {r['impact']} | {r['readiness']} | {r['quadrant']} | {r['role']} |")
    lines += [
        "",
        "## Page 2 — Plan",
        "- **Proposal (3 sentences):** …",
        "- **Alternatives considered and rejected (1-2, one sentence each):** …",
        "- **Milestones (next 3-5 with deliverable):** …",
        "- **Top-3 risks with countermeasure:** …",
        "- **Dependencies only the executive team can resolve:** …",
        "",
        "## Page 3 — Budget & resolutions",
        "| Item | One-off | Recurring p.a. | Note |",
        "|---|---|---|---|",
        "| Tooling/licenses | | | |",
        "| External support | | | |",
        "| Internal capacity (FTE) | | | assume adoption < 100% |",
        "",
        "**Resolutions (checkbox — decide in the room):**",
        "- [ ] Resolution 1: …",
        "- [ ] Resolution 2: …",
    ]
    if day == 30:
        lines.insert(6, f"- **Recommended pilots from current scores:** {', '.join(p['recommended_pilots'])}")
        if p["build_readiness_first"]:
            lines.insert(7, f"- **Deliberately postponed:** {p['build_readiness_first'][0]}")
    return "\n".join(lines)


# ---------- governance red-line check ----------

BLOCKED_PATTERNS = [
    ("applicant screening/ranking", ["screen applicant", "rank applicant", "rank candidate", "score candidate",
                                     "cv screening", "bewerber-screening", "bewerber ranking", "bewerberauswahl"]),
    ("employee performance evaluation", ["performance monitoring", "employee scoring", "leistungskontrolle",
                                         "mitarbeiterbewertung", "productivity tracking per employee"]),
    ("emotion recognition at work", ["emotion recognition", "emotionserkennung"]),
]


def check_use_case(description: str,
                   data_classes: list | None = None,
                   evaluates_people: bool = False,
                   automated_decision_without_human_review: bool = False,
                   customer_facing: bool = False) -> dict:
    """Deterministic red-line check mirroring governance/ai-richtlinie.md.

    Returns verdict: blocked | review_required | fast_track, with reasons and
    required approvals. Policy is code: the model cannot talk its way past it.
    """
    desc = (description or "").lower()
    data_classes = [c.lower() for c in (data_classes or [])]
    blocked, reviews, approvals = [], [], set()

    if evaluates_people:
        blocked.append("AI-based evaluation/ranking of applicants or employees — EU AI Act Annex III high-risk (red line, not approvable in this program)")
    for label, patterns in BLOCKED_PATTERNS:
        if any(pat in desc for pat in patterns):
            blocked.append(f"{label} — EU AI Act Annex III / works-council red line")
    if automated_decision_without_human_review:
        blocked.append("automated decision with legal/significant effect and no human review — Art. 22 GDPR (add a human-in-the-loop step, then resubmit)")

    if "personal" in data_classes:
        reviews.append("personal data → GDPR quick check, DPA with provider required")
        approvals.update(["data_protection"])
    if "employee" in data_classes:
        reviews.append("employee data → works council must be involved before the pilot")
        approvals.update(["works_council", "data_protection"])
    if "confidential" in data_classes:
        reviews.append("confidential data → per-use-case release, tool must be on the approved list")
        approvals.update(["ai_office", "it_security"])
    if customer_facing:
        reviews.append("customer-facing AI interaction → transparency/labeling duty (EU AI Act), quality gate before go-live")
        approvals.update(["ai_office"])

    if blocked:
        verdict = "blocked"
    elif reviews:
        verdict = "review_required"
    else:
        verdict = "fast_track"
        reviews.append("no sensitive data classes, not people-evaluating, internal → fast track (5 working days SLA)")
    return {"verdict": verdict, "blocked_reasons": blocked, "review_notes": reviews,
            "required_approvals": sorted(approvals)}


def interview_guide() -> str:
    return INTERVIEW_GUIDE.read_text(encoding="utf-8")
