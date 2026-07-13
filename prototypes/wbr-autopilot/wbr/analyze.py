"""Analyze a week vs. the previous one and draft the Weekly Business Review.

Anomaly detection is deterministic (thresholds, not vibes); the memo cites
every number, and verify.py recomputes them all — a draft with an unverifiable
number never ships (the pilot-3 rule: no unsourced numbers survive review).
"""

from . import gen_week

WOW_FLAG = 0.15          # |week-over-week| >= 15% on channel revenue
ROAS_FLAG = 1.5          # campaigns below this burn money
COVER_FLAG_WEEKS = 1.5   # stock below 1.5 weeks of demand


def eur(x: float) -> str:
    return f"{round(x):,} EUR"


def facts(year: int, week: int) -> dict:
    cur = gen_week.generate(year, week)
    prev = gen_week.generate(*gen_week.prev_week(year, week))
    f = {"week": cur["week"], "prev_week": prev["week"], "channels": {}, "campaigns": {}, "stock": {}}

    for ch in cur["sales"]:
        c, p = cur["sales"][ch]["revenue"], prev["sales"][ch]["revenue"]
        wow = (c - p) / p
        f["channels"][ch] = {"revenue": c, "prev": p, "wow_pct": round(wow * 100, 1),
                             "delta_eur": c - p, "flag": abs(wow) >= WOW_FLAG}
    f["total_revenue"] = sum(v["revenue"] for v in f["channels"].values())

    for camp, v in cur["ads"].items():
        roas = v["revenue_attributed"] / v["spend"]
        f["campaigns"][camp] = {"spend": v["spend"], "attributed": v["revenue_attributed"],
                                "roas": round(roas, 2), "flag": roas < ROAS_FLAG}

    for sku, v in cur["inventory"].items():
        weeks = v["stock_units"] / v["weekly_demand"]
        f["stock"][sku] = {"name": v["name"], "stock": v["stock_units"],
                           "weekly_demand": v["weekly_demand"], "weeks_cover": round(weeks, 1),
                           "flag": weeks < COVER_FLAG_WEEKS}
    return f


def anomalies(f: dict) -> list:
    """Flagged findings, ranked by EUR size, each with hypothesis + action + owner."""
    found = []
    for ch, v in f["channels"].items():
        if v["flag"]:
            direction = "dropped" if v["delta_eur"] < 0 else "jumped"
            found.append({
                "size_eur": abs(v["delta_eur"]),
                "headline": f"{ch} revenue {direction} {abs(v['wow_pct'])}% week-over-week ({eur(v['prev'])} -> {eur(v['revenue'])})",
                "hypothesis": "check shop conversion funnel, promo calendar and tracking before assuming demand shift" if v["delta_eur"] < 0 else "verify it is real demand (not double-tracking) before scaling spend",
                "action": f"E-Commerce lead to diagnose by Wednesday; if funnel-related, hotfix; source: sales.csv {f['week']} vs {f['prev_week']}",
                "owner": "E-Commerce",
            })
    for camp, v in f["campaigns"].items():
        if v["flag"]:
            waste = v["spend"] - v["attributed"]
            found.append({
                "size_eur": abs(waste),
                "headline": f"Campaign '{camp}' ROAS at {v['roas']} ({eur(v['spend'])} spend, {eur(v['attributed'])} attributed)",
                "hypothesis": "creative fatigue or audience overlap; below breakeven every day it keeps running",
                "action": f"pause or cut budget 50% today, relaunch after creative refresh; source: adspend.csv {f['week']}",
                "owner": "Performance Marketing",
            })
    for sku, v in f["stock"].items():
        if v["flag"]:
            found.append({
                "size_eur": v["weekly_demand"] * 4,  # rough margin-at-risk proxy, stated as such in memo
                "headline": f"{v['name']} ({sku}) at {v['weeks_cover']} weeks of cover ({v['stock']:,} units vs {v['weekly_demand']:,}/week demand)",
                "hypothesis": "reorder point missed or supplier delay; stockout would hit the top-selling category",
                "action": f"expedite reorder today, check supplier lead time; source: inventory.csv {f['week']}",
                "owner": "Supply Chain",
            })
    return sorted(found, key=lambda a: -a["size_eur"])


def render_memo(f: dict) -> str:
    found = anomalies(f)
    lines = [
        f"# Weekly Business Review — {f['week']} (draft)",
        "",
        f"_Auto-drafted by the WBR autopilot from {f['week']} extracts; every number recomputed and gated by verify.py. Analyst review pending — this is a draft, not a decision._",
        "",
        f"**Total revenue:** {eur(f['total_revenue'])}",
        "",
        "## Top anomalies (ranked by EUR at stake)",
        "",
    ]
    if not found:
        lines.append("No thresholds tripped this week (channel WoW < 15%, all ROAS >= 1.5, all stock >= 1.5 weeks cover).")
    for i, a in enumerate(found, 1):
        lines += [f"### {i}. {a['headline']}",
                  f"- **Hypothesis:** {a['hypothesis']}",
                  f"- **Proposed action:** {a['action']}",
                  f"- **Owner:** {a['owner']}",
                  ""]
    lines += ["## Channel view", "", "| Channel | Revenue | WoW | Flag |", "|---|---|---|---|"]
    for ch, v in f["channels"].items():
        lines.append(f"| {ch} | {eur(v['revenue'])} | {v['wow_pct']:+}% | {'⚠️' if v['flag'] else ''} |")
    lines += ["", "## Campaign view", "", "| Campaign | Spend | Attributed | ROAS | Flag |", "|---|---|---|---|---|"]
    for camp, v in f["campaigns"].items():
        lines.append(f"| {camp} | {eur(v['spend'])} | {eur(v['attributed'])} | {v['roas']} | {'⚠️' if v['flag'] else ''} |")
    lines += ["", "## Decisions needed", ""]
    lines += [f"- [ ] {a['owner']}: {a['action'].split(';')[0]}" for a in found] or ["- none this week"]
    return "\n".join(lines)
