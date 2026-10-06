#!/usr/bin/env python3
"""Checks the whole-site invariants that a launch-day merge has to preserve.

Usage:
    python3 scripts/check_invariants.py [--root public]

Two of these hold whatever day it is:

- every locale has exactly the pages en has, so one locale can't quietly fall behind;
- every page carries the footer's Mac App Store line, in its own language.

The rest depend on which side of launch the build is on, and the build says which side that is:
`AVAILABILITY` in scripts/build_pages.py is `PreOrder` before the app is downloadable and `InStock`
after. Before launch, every page has to say the app is coming soon, nothing may link to the
listing, and no home page may carry a `downloadUrl`. After launch, exactly the reverse: no
coming-soon wording anywhere, the footer's line links to the listing on every page, and all four
home pages carry `downloadUrl`.

Deriving the phase from `AVAILABILITY` is the point. On launch morning the availability, the copy
and the listing link are flipped in one commit (the go-live checklist, B4), and the failure this
guards against is flipping some of them: a site that says it's on the Mac App Store while its
structured data still says pre-order, or one locale left saying "coming soon" after the others
moved on. Either half-flip fails here.

The home page's calls to action follow the same phase. Before launch the hero's one primary
button installs the free CLI (it jumps to the `#install` block) and nothing store-shaped is a
button; after launch the primary goes to the Mac App Store listing and the CLI is second. In
neither phase is the hero's call to action an image, so it can't pass for a store badge.

Two things this deliberately does not catch, so nobody reads a green run as more than it is:

- **A placeholder listing URL passes.** `https://apps.apple.com/app/idPLACEHOLDER` is a link to
  apps.apple.com as far as this check is concerned. `check_links.py` is what fails on a placeholder,
  so it has to stay wired into CI beside this one.
- **"Coming soon on every page" is really "the footer's coming-soon line".** A page whose *body*
  was flipped to launch wording early, without linking to the listing, still has its footer and so
  still passes. The link check above catches the common case, since launch copy normally links.

To see it catch one:

    cp -R public /tmp/site
    sed -i '' 's/coming soon to the Mac App Store/on the Mac App Store/' /tmp/site/pdf/index.html
    python3 scripts/check_invariants.py --root /tmp/site
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_PAGES = ROOT / "scripts" / "build_pages.py"

PREFIX = {"zh-hant/": "zh-hant", "zh-hans/": "zh-hans", "ja/": "ja"}

# The footer's Mac App Store line, per locale, in either phase: (before launch, after launch).
# The launch form wraps "Mac App Store" in a link, so it's matched as a pattern.
FOOTER = {
    "en": (
        "MarsDawn is coming soon to the Mac App Store.",
        r"MarsDawn is on the <a href=\"[^\"]+\">Mac App Store</a>\.",
    ),
    "zh-hant": (
        "MarsDawn 即將在 Mac App Store 上架。",
        r"MarsDawn 已在 <a href=\"[^\"]+\">Mac App Store</a> 上架。",
    ),
    "zh-hans": (
        "MarsDawn 即将在 Mac App Store 上架。",
        r"MarsDawn 已在 <a href=\"[^\"]+\">Mac App Store</a> 上架。",
    ),
    "ja": (
        "MarsDawn は Mac App Store で近日公開予定です。",
        r"MarsDawn は <a href=\"[^\"]+\">Mac App Store</a> で配信中です。",
    ),
}

# Wording that may not survive launch day, per locale.
PRE_LAUNCH_WORDING = {
    "en": ["coming soon to the Mac App Store", "not on sale yet"],
    "zh-hant": ["即將在 Mac App Store 上架", "還沒開賣"],
    "zh-hans": ["即将在 Mac App Store 上架", "还没开卖"],
    "ja": ["Mac App Store で近日公開", "近日公開：", "まだ販売されていません", "近日 Mac App Store に登場予定"],
}

LISTING_HOST = "apps.apple.com"

# The hero's calls to action, as (class, href) pairs in order, per phase.
CTA = re.compile(r'<a class="cta ([\w-]+)" href="([^"]*)"')
HERO_CTA = re.compile(r'<p class="hero-cta">(.*?)</p>', re.S)

# What the offer's availability has to say in each phase.
AVAILABILITY_FOR = {
    "pre-launch": "https://schema.org/PreOrder",
    "launched": "https://schema.org/InStock",
}
OFFER = re.compile(r'"@type":\s*"Offer"')
AVAILABILITY_IN_PAGE = re.compile(r'"availability":\s*"([^"]*)"')


def phase():
    """"launched" once the build says the offer is in stock, else "pre-launch"."""
    source = BUILD_PAGES.read_text()
    match = re.search(r'^AVAILABILITY = "([^"]+)"', source, re.MULTILINE)
    if not match:
        sys.exit("check_invariants: no AVAILABILITY in scripts/build_pages.py")
    value = match.group(1)
    if value.endswith("/InStock"):
        return "launched"
    if value.endswith("/PreOrder"):
        return "pre-launch"
    sys.exit(f"check_invariants: AVAILABILITY is {value!r}, which is neither PreOrder nor InStock")


def locale_of(relative):
    for prefix, locale in PREFIX.items():
        if relative.startswith(prefix):
            return locale
    return "en"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT / "public"))
    args = parser.parse_args()
    site = Path(args.root)

    where = phase()
    pages = {}
    for page in sorted(site.rglob("index.html")):
        pages[str(page.relative_to(site))] = page
    if not pages:
        sys.exit(f"check_invariants: no pages under {site}")

    problems = []

    # Same page set in every locale.
    by_locale = {"en": set(), "zh-hant": set(), "zh-hans": set(), "ja": set()}
    for relative in pages:
        locale = locale_of(relative)
        slug = relative if locale == "en" else relative[len(locale) + 1 :]
        by_locale[locale].add(slug)
    for locale, slugs in by_locale.items():
        if locale == "en":
            continue
        for missing in sorted(by_locale["en"] - slugs):
            problems.append(f"{locale} is missing {missing}, which en has")
        for extra in sorted(slugs - by_locale["en"]):
            problems.append(f"{locale} has {extra}, which en doesn't")

    for relative, page in pages.items():
        locale = locale_of(relative)
        text = page.read_text()
        before, after = FOOTER[locale]
        wanted = after if where == "launched" else re.escape(before)
        if not re.search(wanted, text):
            problems.append(
                f"{relative}: no {locale} footer Mac App Store line for the {where} phase"
            )
        if where == "launched":
            for wording in PRE_LAUNCH_WORDING[locale]:
                if wording in text:
                    problems.append(f"{relative}: still says {wording!r} after launch")
        offers = len(OFFER.findall(text))
        stated = AVAILABILITY_IN_PAGE.findall(text)
        if offers and len(stated) < offers:
            problems.append(f"{relative}: {offers - len(stated)} of {offers} offers state no availability")
        for value in stated:
            if value != AVAILABILITY_FOR[where]:
                problems.append(
                    f"{relative}: offer availability is {value!r}, but the copy is {where} "
                    f"({AVAILABILITY_FOR[where]})"
                )
        links_out = LISTING_HOST in text
        if where == "pre-launch" and links_out:
            problems.append(f"{relative}: links to {LISTING_HOST} before launch")
        if where == "launched" and not links_out:
            problems.append(f"{relative}: doesn't link to {LISTING_HOST} after launch")

    for home in ("index.html", "zh-hant/index.html", "zh-hans/index.html", "ja/index.html"):
        if home not in pages:
            problems.append(f"{home} is missing")
            continue
        text = pages[home].read_text()
        ctas = CTA.findall(text)
        if where == "pre-launch" and ctas != [("cta-primary", "#install")]:
            problems.append(f"{home}: before launch the hero's calls to action should be just the CLI install, got {ctas}")
        if where == "launched" and not (
            len(ctas) == 2 and ctas[0][0] == "cta-primary" and ctas[0][1].startswith(f"https://{LISTING_HOST}/")
            and ctas[1] == ("cta-secondary", "#install")
        ):
            problems.append(f"{home}: after launch the hero's calls to action should be the listing, then the CLI, got {ctas}")
        hero_cta = HERO_CTA.search(text)
        if not hero_cta or "<img" in hero_cta.group(1):
            problems.append(f"{home}: the hero's call to action is missing, or is an image")
        if 'id="install"' not in text or "brew install" not in text.split('id="install"', 1)[-1].split("</section>", 1)[0]:
            problems.append(f"{home}: no #install block with the Homebrew command for the CTA to land on")
        has = '"downloadUrl"' in text
        if where == "launched" and not has:
            problems.append(f"{home}: no downloadUrl in the JSON-LD after launch")
        if where == "pre-launch" and has:
            problems.append(f"{home}: a downloadUrl in the JSON-LD before launch")

    for problem in problems:
        print(f"check_invariants: {problem}")
    print(f"{len(pages)} pages checked in the {where} phase: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
