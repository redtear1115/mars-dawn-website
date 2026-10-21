#!/usr/bin/env python3
"""Every schema.org Offer in the built site states its availability.

A priced offer with no `availability` reads to a crawler as obtainable today, which is a
claim about being on sale — the same claim the prose is careful about. Before launch that
has to be PreOrder; on launch day it becomes InStock, and after that this check keeps a
new page from quietly shipping an offer with no availability at all.

It also holds each home page's SoftwareApplication to the price the product actually has: an
AggregateOffer from 0 to the unlock price in scripts/price.py (4.99 USD, or the sale price in the
sale phase; a free download with a 14-day trial, then a one-time unlock), two Offers inside it with
exactly those prices, a priceValidUntil on the unlock Offer in the sale phase and none otherwise, and the rest of the block that makes it citable:
a version number (the newest app version in vendor/app-release-notes), operating system, category, screenshot, publisher (the App Store seller, a Person) and sameAs list. A JSON-LD
block that doesn't parse fails on any page.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import price  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "public"
# The newest Mac app version on the App Store, as vendored for /changelog/ (website #273, #289).
NOTES = Path(__file__).resolve().parent.parent / "vendor" / "app-release-notes" / "whats-new.json"
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


# The App Store's sellerName and artistName for MarsDawn.
PUBLISHER = {"@type": "Person", "name": "Nan-Kuang Lee"}
HOMES = ["index.html", "zh-hant/index.html", "zh-hans/index.html", "ja/index.html",
         "de/index.html", "fr/index.html", "es/index.html", "ko/index.html"]
REQUIRED = ("name", "description", "applicationCategory", "operatingSystem", "softwareVersion",
            "screenshot", "publisher", "sameAs", "downloadUrl", "url")


def newest_app_version():
    versions = [v["version"] for v in json.loads(NOTES.read_text(encoding="utf-8"))["versions"]]
    return max(versions, key=lambda v: tuple(map(int, v.split("."))))


def check_home(where, data, problems, unlock=None, phase=None):
    """The home page's blocks must hold exactly one SoftwareApplication with the real price."""
    unlock = price.current() if unlock is None else unlock
    phase = price.PHASE if phase is None else phase
    apps = [d for d in data if isinstance(d, dict) and d.get("@type") == "SoftwareApplication"]
    if len(apps) != 1:
        problems.append(f"{where}: {len(apps)} SoftwareApplication blocks, want 1")
        return
    app = apps[0]
    for key in REQUIRED:
        if not app.get(key):
            problems.append(f"{where}: SoftwareApplication has no {key}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(app.get("softwareVersion", ""))):
        problems.append(f"{where}: softwareVersion {app.get('softwareVersion')!r} isn't major.minor.patch")
    elif app["softwareVersion"] != newest_app_version():
        problems.append(f"{where}: softwareVersion {app['softwareVersion']!r} isn't the newest app version, "
                        f"{newest_app_version()!r} ({NOTES.relative_to(NOTES.parents[2])})")
    if str(app.get("screenshot", "")).startswith("https://") is False:
        problems.append(f"{where}: screenshot isn't an absolute https URL")
    if app.get("publisher") != PUBLISHER:
        problems.append(f"{where}: publisher is {app.get('publisher')!r}, want {PUBLISHER!r}")
    if not isinstance(app.get("sameAs"), list) or not all(str(u).startswith("https://") for u in app["sameAs"]):
        problems.append(f"{where}: sameAs isn't a list of https URLs")
    agg = app.get("offers")
    if not isinstance(agg, dict) or agg.get("@type") != "AggregateOffer":
        problems.append(f"{where}: offers isn't an AggregateOffer")
        return
    want = {"lowPrice": "0", "highPrice": unlock, "priceCurrency": "USD", "offerCount": 2}
    for key, value in want.items():
        if agg.get(key) != value:
            problems.append(f"{where}: AggregateOffer {key} is {agg.get(key)!r}, want {value!r}")
    inner = agg.get("offers")
    prices = sorted(str(o.get("price")) for o in inner if isinstance(o, dict)) if isinstance(inner, list) else None
    if prices != ["0", unlock]:
        problems.append(f"{where}: the AggregateOffer's Offers have prices {prices}, want ['0', {unlock!r}]")
    paid = [o for o in inner if isinstance(o, dict) and str(o.get("price")) != "0"] if isinstance(inner, list) else []
    until = [o.get("priceValidUntil") for o in paid]
    want_until = [price.SALE_LAST_DAY] if phase == "sale" else [None]
    if until != want_until:
        problems.append(f"{where}: the unlock Offer's priceValidUntil is {until}, want {want_until} in the {phase} phase")


def self_test():
    """Each rule in check_home that price.py feeds goes red on a plant, with its own message."""
    def home(unlock, until=None):
        paid = {"@type": "Offer", "price": unlock, "priceCurrency": "USD"}
        if until:
            paid["priceValidUntil"] = until
        return [{"@type": "SoftwareApplication", "name": "MarsDawn", "description": "d",
                 "applicationCategory": "DeveloperApplication", "operatingSystem": "macOS 26 or later",
                 "softwareVersion": newest_app_version(), "screenshot": "https://x/s.png", "publisher": PUBLISHER,
                 "sameAs": ["https://x"], "downloadUrl": "https://x", "url": "https://x",
                 "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "0",
                            "highPrice": unlock, "offerCount": 2,
                            "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "USD"}, paid]}}]
    cases = [
        ("regular, regular price", home(price.REGULAR), price.REGULAR, "regular", None),
        ("sale, sale price until the last day", home(price.SALE, price.SALE_LAST_DAY), price.SALE, "sale", None),
        ("regular phase stating the sale price", home(price.SALE), price.REGULAR, "regular", "AggregateOffer highPrice is"),
        ("sale phase stating the regular price", home(price.REGULAR, price.SALE_LAST_DAY), price.SALE, "sale", "AggregateOffer highPrice is"),
        ("sale phase with no priceValidUntil", home(price.SALE), price.SALE, "sale", "priceValidUntil is [None]"),
        ("regular phase keeping a priceValidUntil", home(price.REGULAR, price.SALE_LAST_DAY), price.REGULAR, "regular", "priceValidUntil is ['2026-11-30']"),
    ]
    failed = 0
    for name, data, unlock, phase, expect in cases:
        problems = []
        check_home("plant", data, problems, unlock, phase)
        ok = (not problems) if expect is None else any(expect in p for p in problems)
        print(f"check_offers self-test: {'ok' if ok else 'FAIL'}: {name}: {problems}")
        failed += not ok
    return 1 if failed else 0


def main():
    problems = []
    checked = 0
    for page in sorted(SITE.rglob("*.html")):
        where = page.relative_to(SITE)
        blocks = []
        for block in SCRIPT.findall(page.read_text()):
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                problems.append(f"{where}: JSON-LD doesn't parse: {exc}")
                continue
            blocks.append(data)
        if str(where) in HOMES:
            check_home(where, blocks, problems)
        for data in blocks:
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
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else main())
