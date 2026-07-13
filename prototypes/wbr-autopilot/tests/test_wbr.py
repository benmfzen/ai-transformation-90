import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wbr import analyze, gen_week, verify


def find_week_with(anomaly: str) -> tuple:
    for week in range(1, 53):
        if anomaly in gen_week.generate(2026, week)["anomalies_injected"]:
            return 2026, week
    raise AssertionError(f"no 2026 week with {anomaly}")


def test_determinism():
    assert gen_week.generate(2026, 29) == gen_week.generate(2026, 29)


def test_prev_week_year_rollover():
    y, w = gen_week.prev_week(2026, 1)
    assert y == 2025 and w in (52, 53)


def test_injected_stockout_is_flagged():
    y, w = find_week_with("stockout_risk")
    f = analyze.facts(y, w)
    assert f["stock"]["N-203"]["flag"] and f["stock"]["N-203"]["weeks_cover"] < 1.5


def test_injected_campaign_burn_is_flagged():
    y, w = find_week_with("campaign_burn")
    f = analyze.facts(y, w)
    assert f["campaigns"]["Social Prospecting"]["flag"]
    assert f["campaigns"]["Social Prospecting"]["roas"] < 1.0


def test_channel_dip_flagged_unless_prev_week_also_dipped():
    y, w = find_week_with("channel_dip")
    prev_dipped = "channel_dip" in gen_week.generate(*gen_week.prev_week(y, w))["anomalies_injected"]
    f = analyze.facts(y, w)
    if not prev_dipped:
        assert f["channels"]["D2C Web"]["flag"] and f["channels"]["D2C Web"]["delta_eur"] < 0


def test_memo_verifies_and_tampering_fails():
    f = analyze.facts(2026, 29)
    memo = analyze.render_memo(f)
    assert verify.verify(memo, 2026, 29) == []
    total = analyze.eur(f["total_revenue"])
    tampered = memo.replace(total, "999,999 EUR")
    assert verify.verify(tampered, 2026, 29)


def test_anomaly_count_gate():
    memo = analyze.render_memo(analyze.facts(2026, 29))
    padded = memo + "\n### 9. invented finding nobody computed\n"
    problems = verify.verify(padded, 2026, 29)
    assert any("anomaly count mismatch" in p for p in problems)
