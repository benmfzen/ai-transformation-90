"""Orchestrator: generate data -> draft memo -> verify -> write outputs.

Usage: python -m wbr.run_week [YYYY WW]   (defaults to the current ISO week)
Prints WEEK_ID=... for the CI workflow. Exit 1 if verification fails.
"""

import datetime
import sys
from pathlib import Path

from . import analyze, gen_week, verify

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) == 3:
        year, week = int(sys.argv[1]), int(sys.argv[2])
    else:
        iso = datetime.date.today().isocalendar()
        year, week = iso[0], iso[1]

    data = gen_week.generate(year, week)
    data_dir = gen_week.write_csvs(data)
    f = analyze.facts(year, week)
    memo = analyze.render_memo(f)
    out = ROOT / "outputs" / f"wbr-{f['week']}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(memo, encoding="utf-8")

    problems = verify.verify(memo, year, week)
    print(f"WEEK_ID={f['week']}")
    print(f"data: {data_dir.relative_to(ROOT)} | memo: {out.relative_to(ROOT)} | anomalies: {len(analyze.anomalies(f))}")
    if problems:
        print("VERIFY FAIL:", *problems, sep="\n  ")
        return 1
    print("VERIFY PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
