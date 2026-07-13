import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import core

GOOD_EVIDENCE = {d: f"Lead said: 'we spend 30% of our time on {d}-related rework, see ticket report Q2'" for d in core.DIMS}
GOOD_SCORES = {"repetitiveness": 4, "pain": 3, "leverage": 4, "data": 3, "willingness": 5, "freedom": 4}


def test_portfolio_matches_case_numbers():
    p = core.portfolio_summary()
    cs = next(r for r in p["departments"] if r["id"] == "customer-service")
    assert cs["impact"] == 4.67 and cs["readiness"] == 4.33
    assert cs["quadrant"] == "pilot-now"
    prod = next(r for r in p["departments"] if r["id"] == "production")
    assert prod["quadrant"] == "build-first"
    assert p["recommended_pilots"][0] == "Customer Service"


def test_quadrants():
    assert core.quadrant(4.0, 4.0) == "pilot-now"
    assert core.quadrant(4.0, 2.0) == "build-first"
    assert core.quadrant(2.0, 4.0) == "quick-win-or-enabler"
    assert core.quadrant(2.0, 2.0) == "later"


def test_scores_without_evidence_are_rejected():
    errors = core.validate_submission(GOOD_SCORES, {})
    assert len(errors) == 6 and all("evidence required" in e for e in errors)


def test_short_evidence_is_rejected():
    errors = core.validate_submission(GOOD_SCORES, {d: "feels right" for d in core.DIMS})
    assert errors


def test_score_range_and_completeness():
    assert any("must be an integer 1-5" in e for e in core.validate_submission({**GOOD_SCORES, "pain": 7}, GOOD_EVIDENCE))
    bad = dict(GOOD_SCORES)
    del bad["data"]
    assert any("missing score: data" in e for e in core.validate_submission(bad, GOOD_EVIDENCE))


def test_upsert_roundtrip(tmp_path):
    org_copy = tmp_path / "org.yaml"
    shutil.copy(core.ORG_PATH, org_copy)
    result = core.upsert_department("quality", "Quality Assurance", "T. Test", 15,
                                    GOOD_SCORES, GOOD_EVIDENCE, role="candidate",
                                    org_path=org_copy)
    assert result["accepted"] and result["quadrant"] in {"pilot-now", "build-first", "quick-win-or-enabler", "later"}
    org = core.load_org(org_copy)
    added = next(d for d in org["departments"] if d["id"] == "quality")
    assert added["evidence"]["pain"].startswith("Lead said")
    # rejection path leaves file untouched
    result2 = core.upsert_department("quality2", "X", "Y", 1, GOOD_SCORES, {}, org_path=org_copy)
    assert not result2["accepted"]
    assert all(d["id"] != "quality2" for d in core.load_org(org_copy)["departments"])


def test_memo_contains_portfolio_and_structure():
    memo = core.draft_decision_memo(30)
    assert "Customer Service" in memo and "Page 3 — Budget" in memo
    assert "Recommended pilots" in memo
    try:
        core.draft_decision_memo(45)
        assert False, "should raise"
    except ValueError:
        pass


def test_red_lines_block():
    r = core.check_use_case("AI to rank applicant CVs for hiring", evaluates_people=True)
    assert r["verdict"] == "blocked"
    r2 = core.check_use_case("automatic cv screening of candidates")
    assert r2["verdict"] == "blocked"


def test_review_and_fast_track():
    r = core.check_use_case("draft replies to customer emails", data_classes=["personal"], customer_facing=True)
    assert r["verdict"] == "review_required"
    assert "data_protection" in r["required_approvals"]
    r2 = core.check_use_case("summarize public product reviews", data_classes=["public"])
    assert r2["verdict"] == "fast_track"


# ---------- program clock ----------

import program  # noqa: E402


def test_every_program_day_has_exactly_one_block():
    for day in range(1, 91):
        blocks = [b for b in program.BLOCKS if b["days"][0] <= day <= b["days"][1]]
        assert len(blocks) == 1, f"day {day}: {len(blocks)} blocks"


def test_todos_for_key_days():
    d5 = program.todos_for_day(5)
    assert d5["phase"]["n"] == 1 and "setup" in d5["current_block"]["title"]
    assert d5["next_milestone"]["day"] == 30
    d45 = program.todos_for_day(45)
    assert d45["phase"]["name"] == "Pilot" and "pilots running" in d45["current_block"]["title"]
    d90 = program.todos_for_day(90)
    assert d90["next_milestone"]["in_days"] == 0 and "Board decision" in d90["next_milestone"]["what"]


def test_out_of_range_days():
    assert "starts in" in program.todos_for_day(-2)["status"]
    assert "over" in program.todos_for_day(120)["status"]


def test_day_from_start():
    from datetime import date
    assert program.day_from_start("2026-09-01", today=date(2026, 9, 1)) == 1
    assert program.day_from_start("2026-09-01", today=date(2026, 9, 30)) == 30


# ---------- source verification ----------

TRANSCRIPT = """Interview with logistics lead, day 14.
She said: "Two of my people do almost nothing but match order confirmations
against purchase orders." On digitization: "We had three digitization projects
already — two of them created more work than they saved." Ticket volume is
tracked in the ERP. She sees potential in customs paperwork, quote: "if it
really works and not just almost".
"""

VERIFIED_EVIDENCE = {
    "repetitiveness": 'She said: "Two of my people do almost nothing but match order confirmations against purchase orders."',
    "pain": '"Two of my people do almost nothing but match order confirmations" — daily, per the lead',
    "leverage": "metric: 4,100 shipments/month, 15% export share with customs paperwork (ERP report)",
    "data": "system: ERP and scanners in place, documents heterogeneous (inspection of the ERP module)",
    "willingness": '"We had three digitization projects already — two of them created more work than they saved."',
    "freedom": 'Customs has compliance stakes but she is open: "if it really works and not just almost"',
}


def test_verified_quotes_accepted():
    errors = core.validate_submission(GOOD_SCORES, VERIFIED_EVIDENCE, source_text=TRANSCRIPT)
    assert errors == []


def test_fabricated_quote_rejected():
    ev = dict(VERIFIED_EVIDENCE)
    ev["pain"] = '"We are drowning in tickets and everyone is desperate" (interview)'
    errors = core.validate_submission(GOOD_SCORES, ev, source_text=TRANSCRIPT)
    assert len(errors) == 1 and "not found verbatim" in errors[0]


def test_unquoted_unprefixed_evidence_rejected_with_source():
    ev = dict(VERIFIED_EVIDENCE)
    ev["data"] = "the ERP situation seemed pretty solid overall to me"
    errors = core.validate_submission(GOOD_SCORES, ev, source_text=TRANSCRIPT)
    assert len(errors) == 1 and "no verifiable quote" in errors[0]


def test_typography_and_case_insensitive_matching():
    ev = dict(VERIFIED_EVIDENCE)
    ev["willingness"] = "‚we had three digitization   projects already — two of them created MORE work than they saved.'"
    assert core.validate_submission(GOOD_SCORES, ev, source_text=TRANSCRIPT) == []


def test_without_source_quotes_are_not_checked():
    ev = dict(VERIFIED_EVIDENCE)
    ev["pain"] = '"totally invented but long enough quote here"'
    assert core.validate_submission(GOOD_SCORES, ev, source_text=None) == []


# ---------- four-eyes calibration ----------

def test_compare_flags_gaps_and_quadrant_flip():
    a = {"repetitiveness": 5, "pain": 5, "leverage": 4, "data": 4, "willingness": 5, "freedom": 4}
    b = {"repetitiveness": 5, "pain": 3, "leverage": 4, "data": 2, "willingness": 5, "freedom": 4}
    r = core.compare_submissions(a, b, "operator", "skeptic")
    assert sorted(r["must_discuss"]) == ["data", "pain"]
    assert not r["calibrated"]
    assert r["per_dimension"]["pain"]["consensus_default"] == 3
    assert r["portfolio_effect"]["quadrant_disagreement"] is False


def test_compare_calibrated_when_close():
    a = {"repetitiveness": 4, "pain": 3, "leverage": 4, "data": 3, "willingness": 4, "freedom": 3}
    b = {d: v - (1 if d == "pain" else 0) for d, v in a.items()}
    r = core.compare_submissions(a, b)
    assert r["calibrated"] and r["must_discuss"] == []


def test_compare_rejects_incomplete():
    assert "error" in core.compare_submissions({"pain": 3}, {"pain": 4})
