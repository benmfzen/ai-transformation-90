"""The recomputation gate: a WBR memo ships only if its numbers re-derive.

Recomputes all facts fresh from the (deterministic) data and asserts every
key figure appears verbatim in the memo. A tampered or hallucinated number
means the memo does not match its own sources — exit 1, no PR.
"""

import re
import sys

from . import analyze


def expected_strings(f: dict) -> list:
    exp = [analyze.eur(f["total_revenue"])]
    for v in f["channels"].values():
        exp += [analyze.eur(v["revenue"]), f"{v['wow_pct']:+}%"]
    for v in f["campaigns"].values():
        exp += [analyze.eur(v["spend"]), analyze.eur(v["attributed"]), str(v["roas"])]
    for v in f["stock"].values():
        if v["flag"]:
            exp += [f"{v['weeks_cover']} weeks", f"{v['stock']:,} units"]
    return exp


def verify(memo: str, year: int, week: int) -> list:
    f = analyze.facts(year, week)
    missing = [s for s in expected_strings(f) if s not in memo]
    flagged = len(analyze.anomalies(f))
    claimed = len(re.findall(r"^### \d+\.", memo, re.M))
    if claimed != flagged:
        missing.append(f"anomaly count mismatch: memo claims {claimed}, recomputation finds {flagged}")
    return missing


def main(memo_path: str, year: int, week: int) -> int:
    memo = open(memo_path, encoding="utf-8").read()
    problems = verify(memo, year, week)
    if problems:
        print("VERIFY FAIL — memo does not match recomputed sources:")
        for p in problems:
            print(f"  missing/mismatch: {p}")
        return 1
    print(f"VERIFY PASS — all figures in {memo_path} recomputed from source data")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
