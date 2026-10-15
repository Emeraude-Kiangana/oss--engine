"""Command-line entry point."""

import argparse
import json
from .classifier import classify_issue


def main() -> None:
    parser = argparse.ArgumentParser(description="OSS² Engine offline prototype")
    sub = parser.add_subparsers(dest="command", required=True)
    classify = sub.add_parser("classify", help="Classify an issue locally")
    classify.add_argument("--title", required=True)
    classify.add_argument("--labels", nargs="*", default=[])
    args = parser.parse_args()
    if args.command == "classify":
        result = classify_issue(args.title, args.labels)
        print(json.dumps({"category": result.category, "beginner_friendly": result.beginner_friendly}))


if __name__ == "__main__":
    main()
