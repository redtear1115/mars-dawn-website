#!/usr/bin/env python3
"""Every schema.org Offer in the built site states its availability.

A priced offer with no `availability` reads to a crawler as obtainable today, which is a
claim about being on sale — the same claim the prose is careful about. Before launch that
has to be PreOrder; on launch day it becomes InStock, and after that this check keeps a
new page from quietly shipping an offer with no availability at all.
"""
import json
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "public"
ALLOWED = {"https://schema.org/PreOrder", "https://schema.org/InStock"}
SCRIPT = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
)


def offers(node):
    """Every dict under `node` that is an Offer."""
    if isinstance(node, dict):
        if node.get("@type") == "Offer":
            yield node
        for value in node.values():
            yield from offers(value)
    elif isinstance(node, list):
        for value in node:
            yield from offers(value)


def main():
    problems = []
    checked = 0
    for page in sorted(SITE.rglob("*.html")):
        where = page.relative_to(SITE)
        for block in SCRIPT.findall(page.read_text()):
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                problems.append(f"{where}: JSON-LD doesn't parse: {exc}")
                continue
            for offer in offers(data):
                checked += 1
                availability = offer.get("availability")
                if availability is None:
                    problems.append(
                        f"{where}: an Offer with price {offer.get('price')!r} "
                        f"has no availability"
                    )
                elif availability not in ALLOWED:
                    problems.append(
                        f"{where}: availability {availability!r} isn't one of "
                        f"{sorted(ALLOWED)}"
                    )
    for problem in problems:
        print(f"check_offers: {problem}")
    print(f"{checked} offers checked: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
