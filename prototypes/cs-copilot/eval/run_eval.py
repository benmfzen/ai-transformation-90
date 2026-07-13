"""Eval harness: runs the labeled case set through the pipeline and gates on quality.

Runs offline and deterministically (no LLM), so it can gate CI: any prompt,
keyword or KB change that breaks classification, escalation or grounding
fails the build. Exit code 0 = all gates passed.

Gates:
  category accuracy >= 0.85
  escalation recall  = 1.00  (a missed escalation is the worst failure mode)
  escalation precision >= 0.90
  grounding = 1.00  (every cited source must exist; no draft without sources)
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cs_copilot import knowledge, orders  # noqa: E402
from cs_copilot.pipeline import run  # noqa: E402


def main() -> int:
    cases = [json.loads(l) for l in (Path(__file__).parent / "cases.jsonl").read_text().splitlines() if l.strip()]
    faq_ids = {e.id for e in knowledge.load_faq()}
    order_ids = set(orders.load_orders())

    cat_hits, esc_tp, esc_fp, esc_fn, grounding_errors, failures = 0, 0, 0, 0, [], []

    for case in cases:
        result = run(case["message"], order_id=case["order_id"])

        cat_ok = result["category"] == case["expected_category"]
        cat_hits += cat_ok

        exp, got = case["expected_escalate"], result["escalate"]
        if exp and got:
            esc_tp += 1
        elif not exp and got:
            esc_fp += 1
        elif exp and not got:
            esc_fn += 1

        if not got:
            if not result["sources"]:
                grounding_errors.append(f"{case['id']}: draft without sources")
            for src in result["sources"]:
                kind, _, ref = src.partition(":")
                known = faq_ids if kind == "faq" else order_ids
                if ref not in known:
                    grounding_errors.append(f"{case['id']}: cites unknown source {src}")

        if not cat_ok or exp != got:
            failures.append(
                f"  {case['id']}: expected {case['expected_category']}/esc={exp}, "
                f"got {result['category']}/esc={got} ({result['escalation_reason']})"
            )

    n = len(cases)
    n_esc = sum(1 for c in cases if c["expected_escalate"])
    accuracy = cat_hits / n
    recall = esc_tp / n_esc if n_esc else 1.0
    precision = esc_tp / (esc_tp + esc_fp) if (esc_tp + esc_fp) else 1.0

    print(f"cases:                {n}")
    print(f"category accuracy:    {accuracy:.2f}  (gate >= 0.85)")
    print(f"escalation recall:    {recall:.2f}  (gate  = 1.00)")
    print(f"escalation precision: {precision:.2f}  (gate >= 0.90)")
    print(f"grounding errors:     {len(grounding_errors)}  (gate  = 0)")
    if failures:
        print("mismatches:")
        print("\n".join(failures))
    for err in grounding_errors:
        print(f"  grounding: {err}")

    passed = accuracy >= 0.85 and recall == 1.0 and precision >= 0.90 and not grounding_errors
    print("RESULT:", "PASS" if passed else "FAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
