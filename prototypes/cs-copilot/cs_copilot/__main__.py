"""CLI: python -m cs_copilot "message" [--order N-1042] [--llm]"""

import argparse
import json

from .pipeline import run


def main():
    parser = argparse.ArgumentParser(prog="cs_copilot", description="Draft a grounded customer-service reply.")
    parser.add_argument("message", help="The customer inquiry text")
    parser.add_argument("--order", default=None, help="Order ID, e.g. N-1042")
    parser.add_argument("--llm", action="store_true", help="Polish the draft via the Anthropic API (needs ANTHROPIC_API_KEY)")
    args = parser.parse_args()

    result = run(args.message, order_id=args.order, use_llm=args.llm)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
