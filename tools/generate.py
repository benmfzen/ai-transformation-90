#!/usr/bin/env python3
"""Generate all score-derived outputs from the single source of truth (org.yaml).

Outputs:
  docs/data.js                       — dashboard data (English)
  cases/nordwerk/impact-matrix.md    — score table between generation markers (German)

Usage:
  python3 tools/generate.py           # write outputs
  python3 tools/generate.py --check   # exit 1 if outputs are out of sync (CI)
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ORG = ROOT / "cases" / "nordwerk" / "org.yaml"
DATA_JS = ROOT / "docs" / "data.js"
MATRIX_MD = ROOT / "cases" / "nordwerk" / "impact-matrix.md"

MARK_START = "<!-- generated:scores:start (edit cases/nordwerk/org.yaml, then run tools/generate.py) -->"
MARK_END = "<!-- generated:scores:end -->"

DIM_LABELS_EN = {"repetitiveness": "Repetitiveness", "pain": "Pain", "leverage": "Leverage",
                 "data": "Data", "willingness": "Willingness", "freedom": "Freedom"}
DIM_LABELS_DE = {"repetitiveness": "Repetitivität", "pain": "Schmerz", "leverage": "Hebel",
                 "data": "Datenlage", "willingness": "Bereitschaft", "freedom": "Freiheit"}


def load():
    return yaml.safe_load(ORG.read_text(encoding="utf-8"))


def averages(dept, dims):
    imp = sum(dept["scores"][d] for d in dims["impact"]) / len(dims["impact"])
    rea = sum(dept["scores"][d] for d in dims["readiness"]) / len(dims["readiness"])
    return imp, rea


def sorted_departments(org):
    dims = org["dimensions"]
    return sorted(org["departments"], key=lambda d: averages(d, dims), reverse=True)


def render_data_js(org):
    dims = org["dimensions"]
    order = dims["impact"] + dims["readiness"]
    rows = [[d["name"], d["lead"], d["staff"], *[d["scores"][k] for k in order], d["role"]]
            for d in org["departments"]]
    c = org["company"]
    meta = {"employees": c["employees"], "departments": c["departments_scored"],
            "pilots": c["pilots"], "champions": c["champions"], "days": c["program_days"]}
    return (
        "// GENERATED from cases/nordwerk/org.yaml — do not edit. Run: python3 tools/generate.py\n"
        f"const META = {json.dumps(meta)};\n"
        f"const DIMS = {json.dumps([DIM_LABELS_EN[k] for k in order])};\n"
        "const DEPTS = [\n" + ",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in rows) + "\n];\n"
    )


def render_matrix_table(org):
    dims = org["dimensions"]
    de = lambda n: f"{n:.1f}".replace(".", ",")
    head = ("| Abteilung | " + " | ".join(DIM_LABELS_DE[k] for k in dims["impact"])
            + " | **Impact** | " + " | ".join(DIM_LABELS_DE[k] for k in dims["readiness"])
            + " | **Readiness** |")
    sep = "|" + "---|" * (len(dims["impact"]) + len(dims["readiness"]) + 3)
    lines = [MARK_START, head, sep]
    for d in sorted_departments(org):
        imp, rea = averages(d, dims)
        cells = [str(d["scores"][k]) for k in dims["impact"]] + [f"**{de(imp)}**"] \
              + [str(d["scores"][k]) for k in dims["readiness"]] + [f"**{de(rea)}**"]
        lines.append(f"| {d['name_de']} | " + " | ".join(cells) + " |")
    lines.append(MARK_END)
    return "\n".join(lines)


def patch_matrix_md(org, current: str) -> str:
    block = render_matrix_table(org)
    pattern = re.compile(re.escape(MARK_START) + r".*?" + re.escape(MARK_END), re.DOTALL)
    if not pattern.search(current):
        sys.exit(f"generation markers not found in {MATRIX_MD}")
    return pattern.sub(block, current)


def main():
    check = "--check" in sys.argv
    org = load()
    outputs = {
        DATA_JS: render_data_js(org),
        MATRIX_MD: patch_matrix_md(org, MATRIX_MD.read_text(encoding="utf-8")),
    }
    stale = []
    for path, content in outputs.items():
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            if check:
                stale.append(path.relative_to(ROOT))
            else:
                path.write_text(content, encoding="utf-8")
                print(f"wrote {path.relative_to(ROOT)}")
    if check and stale:
        print("OUT OF SYNC with org.yaml (run: python3 tools/generate.py):")
        for p in stale:
            print(f"  {p}")
        sys.exit(1)
    if check:
        print("generated outputs in sync")


if __name__ == "__main__":
    main()
