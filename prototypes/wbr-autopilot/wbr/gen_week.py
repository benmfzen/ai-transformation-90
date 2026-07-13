"""Deterministic weekly business data for the fictional NATURA Foods SE.

Same ISO week → same data, always (seeded RNG). Each week the seed injects
1-2 anomalies (a channel revenue dip, a campaign burning spend, a looming
stockout) so the analyzer has something real to find — and the verifier can
recompute every number from these CSVs.
"""

import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

CHANNELS = {"D2C Web": 210_000, "Retail/B2B": 260_000, "Marketplaces": 90_000}
CAMPAIGNS = {"Search Brand": (18_000, 4.2), "Search Generic": (32_000, 2.1),
             "Social Prospecting": (28_000, 1.9), "Social Retargeting": (14_000, 3.4),
             "Display": (9_000, 1.6)}
SKUS = [("N-201", "Organic Almond Butter 500g", 5200), ("N-202", "Trail Mix Classic 1kg", 4100),
        ("N-203", "Peanut Butter Crunchy 1kg", 6800), ("N-204", "Dried Mango 1kg", 3900),
        ("N-205", "Dates Medjool 1kg", 4600), ("N-206", "Cashews Roasted 1kg", 3100),
        ("N-207", "Granola Chocolate 750g", 5700), ("N-208", "Protein Bar Box 24x", 2400)]

ANOMALY_TYPES = ["channel_dip", "campaign_burn", "stockout_risk"]


def week_id(year: int, week: int) -> str:
    return f"{year}-w{week:02d}"


def prev_week(year: int, week: int) -> tuple:
    if week > 1:
        return year, week - 1
    import datetime
    last = datetime.date(year - 1, 12, 28).isocalendar()  # 28 Dec is always in the last ISO week
    return last[0], last[1]


def generate(year: int, week: int) -> dict:
    """Generate one week's data in memory. Deterministic per (year, week)."""
    rng = random.Random(year * 100 + week)
    anomalies = rng.sample(ANOMALY_TYPES, k=rng.choice([1, 1, 2]))

    sales = {}
    for channel, base in CHANNELS.items():
        revenue = base * rng.uniform(0.95, 1.05)
        if "channel_dip" in anomalies and channel == "D2C Web":
            revenue *= 0.72
        sales[channel] = {"revenue": round(revenue), "margin_pct": round(rng.uniform(24, 31), 1)}

    ads = {}
    for campaign, (base_spend, base_roas) in CAMPAIGNS.items():
        spend = base_spend * rng.uniform(0.9, 1.1)
        roas = base_roas * rng.uniform(0.85, 1.15)
        if "campaign_burn" in anomalies and campaign == "Social Prospecting":
            spend, roas = base_spend * 1.3, 0.8
        ads[campaign] = {"spend": round(spend), "revenue_attributed": round(spend * roas)}

    inventory = {}
    for sku, name, weekly_demand in SKUS:
        weeks_cover = rng.uniform(2.5, 6.0)
        if "stockout_risk" in anomalies and sku == "N-203":
            weeks_cover = 0.9
        inventory[sku] = {"name": name, "weekly_demand": weekly_demand,
                          "stock_units": round(weekly_demand * weeks_cover)}

    return {"week": week_id(year, week), "anomalies_injected": sorted(anomalies),
            "sales": sales, "ads": ads, "inventory": inventory}


def write_csvs(data: dict) -> Path:
    out = DATA_DIR / data["week"]
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "sales.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["channel", "revenue_eur", "margin_pct"])
        for ch, v in data["sales"].items():
            w.writerow([ch, v["revenue"], v["margin_pct"]])
    with open(out / "adspend.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["campaign", "spend_eur", "revenue_attributed_eur"])
        for c, v in data["ads"].items():
            w.writerow([c, v["spend"], v["revenue_attributed"]])
    with open(out / "inventory.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sku", "name", "stock_units", "weekly_demand_units"])
        for sku, v in data["inventory"].items():
            w.writerow([sku, v["name"], v["stock_units"], v["weekly_demand"]])
    return out
