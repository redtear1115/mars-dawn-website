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

Structured data on inner pages (every locale): each page except a home page carries a
BreadcrumbList whose first item is that locale's home, whose last is the page itself, with
consecutive positions and named items; each essay and reading note (`ARTICLE_DATES` in
build_pages.py) carries a TechArticle with ISO datePublished and dateModified, in order and not in
the future; and nothing else claims to be a TechArticle.

Answer-engine copy (every locale): the home page, /pay-once/ and /quicklook/ each carry a visible FAQ
(`<section class="faq">`) and a FAQPage block whose questions and answers are, word for word, the
visible ones, in the same order, and no other page has either; /quicklook/ carries a HowTo whose
steps are its visible numbered steps; the home page and /native/ open with a definition sentence
(`<p class="definition">`), and `llms-full.txt` repeats each of them.

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
import datetime
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_PAGES = ROOT / "scripts" / "build_pages.py"

PREFIX = {"zh-hant/": "zh-hant", "zh-hans/": "zh-hans", "ja/": "ja", "de/": "de", "fr/": "fr", "es/": "es", "ko/": "ko"}
NEW_LOCALES = ("de", "fr", "es", "ko")  # served only once their copy is complete (scripts/locales.py)

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
# de, fr, es and ko are switched on with app 1.1.0, after launch, so their footers have no
# pre-launch line to compare: after launch the footer must link the listing, in any wording.
# Before launch such a locale must not be served at all (see below). The line sits in the footer, or
# in the home page's closing section, so the pattern is the link itself.
LAUNCHED_FOOTER_ANY = r"<a href=\"https://apps\.apple\.com/app/id\d+\">Mac App Store</a>"

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


LD_BLOCK = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
HOME_SLUGS = {"index.html"} | {f"{l}/index.html" for l in ("zh-hant", "zh-hans", "ja", *NEW_LOCALES)}


def article_slugs():
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_pages
    return set(build_pages.ARTICLE_DATES)


def check_structured_data(relative, text, articles, llms_full, problems):
    """Breadcrumbs on every inner page; TechArticle with dates exactly on the essays and notes."""
    locale = locale_of(relative)
    slug = relative[:-len("index.html")].strip("/")
    if locale != "en":
        slug = slug[len(locale) + 1:] if slug != locale else ""
    blocks = []
    for raw in LD_BLOCK.findall(text):
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            problems.append(f"{relative}: JSON-LD doesn't parse: {exc}")
    check_answer_copy(relative, slug, text, blocks, problems)
    check_definition(relative, slug, text, llms_full, problems)
    if relative in HOME_SLUGS:
        return
    crumbs = [b for b in blocks if b.get("@type") == "BreadcrumbList"]
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', text)
    home = f"https://marsdawn.southern-light.dev/{'' if locale == 'en' else locale + '/'}"
    if len(crumbs) != 1:
        problems.append(f"{relative}: {len(crumbs)} BreadcrumbList blocks, want 1")
    else:
        items = crumbs[0].get("itemListElement")
        if not isinstance(items, list) or len(items) < 2:
            problems.append(f"{relative}: BreadcrumbList has fewer than two items")
        else:
            if [i.get("position") for i in items] != list(range(1, len(items) + 1)):
                problems.append(f"{relative}: BreadcrumbList positions aren't 1..{len(items)}")
            if not all(i.get("name") and i.get("item") for i in items):
                problems.append(f"{relative}: a BreadcrumbList item has no name or no URL")
            if items[0].get("item") != home:
                problems.append(f"{relative}: breadcrumb starts at {items[0].get('item')!r}, want {home!r}")
            if canonical and items[-1].get("item") != canonical.group(1):
                problems.append(f"{relative}: breadcrumb ends at {items[-1].get('item')!r}, not the page's canonical URL")
    tech = [b for b in blocks if b.get("@type") == "TechArticle"]
    if slug in articles:
        if len(tech) != 1:
            problems.append(f"{relative}: {len(tech)} TechArticle blocks, want 1")
        else:
            try:
                published = datetime.date.fromisoformat(tech[0].get("datePublished", ""))
                modified = datetime.date.fromisoformat(tech[0].get("dateModified", ""))
            except ValueError:
                problems.append(f"{relative}: TechArticle dates aren't ISO dates")
            else:
                if modified < published or modified > datetime.date.today():
                    problems.append(f"{relative}: TechArticle dates {published}..{modified} are out of order or in the future")
            if tech[0].get("publisher") != {"@type": "Person", "name": "Nan-Kuang Lee"}:
                problems.append(f"{relative}: TechArticle publisher isn't the App Store seller")
            if not tech[0].get("headline"):
                problems.append(f"{relative}: TechArticle has no headline")
    elif tech:
        problems.append(f"{relative}: a TechArticle on a page that isn't an essay or note")


FAQ_SLUGS = {"", "pay-once", "quicklook"}  # the home page's slug is empty
FAQ_SECTION = re.compile(r'<section class="faq">\n.*?\n</section>', re.S)
HOWTO_SECTION = re.compile(r'<section class="howto">\n.*?\n</section>', re.S)
DEFINITION = re.compile(r'<p class="definition">(.*?)</p>', re.S)


def plain(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment))


def check_answer_copy(relative, slug, text, blocks, problems):
    """Visible FAQ == FAQPage markup, HowTo == its visible steps, and where each may appear."""
    section = FAQ_SECTION.search(text)
    faq_blocks = [b for b in blocks if b.get("@type") == "FAQPage"]
    if slug in FAQ_SLUGS and not section:
        problems.append(f"{relative}: no visible FAQ")
    if slug not in FAQ_SLUGS and (section or faq_blocks):
        problems.append(f"{relative}: a FAQ on a page that shouldn't have one")
    if section:
        visible = [(plain(q), plain(a)) for q, a in re.findall(r"<h3>(.*?)</h3>\n<p>(.*?)</p>", section.group(0), re.S)]
        if len(faq_blocks) != 1:
            problems.append(f"{relative}: {len(faq_blocks)} FAQPage blocks, want 1")
        else:
            marked = [(e.get("name"), e.get("acceptedAnswer", {}).get("text")) for e in faq_blocks[0].get("mainEntity", [])]
            if not visible:
                problems.append(f"{relative}: the visible FAQ has no questions")
            elif marked != visible:
                problems.append(f"{relative}: the FAQPage markup differs from the visible FAQ")
    howto_blocks = [b for b in blocks if b.get("@type") == "HowTo"]
    howto = HOWTO_SECTION.search(text)
    if (slug == "quicklook") != bool(howto and howto_blocks):
        problems.append(f"{relative}: HowTo markup and steps should be on /quicklook/ and nowhere else")
    elif howto:
        visible = [(plain(n), plain(t)) for n, t in re.findall(r"<li><strong>(.*?)</strong> (.*?)</li>", howto.group(0), re.S)]
        marked = [(s.get("name"), s.get("text")) for s in howto_blocks[0].get("step", [])]
        if not visible or marked != visible:
            problems.append(f"{relative}: the HowTo markup differs from the visible steps")


def check_definition(relative, slug, text, llms_full, problems):
    if slug not in ("", "native"):
        return
    found = DEFINITION.search(text)
    if not found or not plain(found.group(1)).strip():
        problems.append(f"{relative}: no definition sentence under the h1")
    elif plain(found.group(1)) not in llms_full:
        problems.append(f"{relative}: the definition sentence isn't in llms-full.txt")


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
    articles = article_slugs()
    llms_full = (site / "llms-full.txt").read_text() if (site / "llms-full.txt").is_file() else ""

    # Same page set in every locale.
    by_locale = {"en": set(), "zh-hant": set(), "zh-hans": set(), "ja": set(), **{l: set() for l in NEW_LOCALES}}
    for relative in pages:
        locale = locale_of(relative)
        slug = relative if locale == "en" else relative[len(locale) + 1 :]
        by_locale[locale].add(slug)
    for locale, slugs in by_locale.items():
        if locale == "en" or (locale in NEW_LOCALES and not slugs):
            continue  # de, fr, es and ko are either all there or not built; check_locales.py says which
        for missing in sorted(by_locale["en"] - slugs):
            problems.append(f"{locale} is missing {missing}, which en has")
        for extra in sorted(slugs - by_locale["en"]):
            problems.append(f"{locale} has {extra}, which en doesn't")

    for relative, page in pages.items():
        locale = locale_of(relative)
        text = page.read_text()
        check_structured_data(relative, text, articles, llms_full, problems)
        if locale in NEW_LOCALES:
            if where != "launched":
                problems.append(f"{relative}: {locale} is served before launch; it ships with 1.1.0, after launch")
            elif not re.search(LAUNCHED_FOOTER_ANY, text):
                problems.append(f"{relative}: no {locale} footer Mac App Store line for the {where} phase")
        else:
            before, after = FOOTER[locale]
            wanted = after if where == "launched" else re.escape(before)
            if not re.search(wanted, text):
                problems.append(
                    f"{relative}: no {locale} footer Mac App Store line for the {where} phase"
                )
        if where == "launched":
            for wording in PRE_LAUNCH_WORDING.get(locale, []):
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

    homes = ["index.html", "zh-hant/index.html", "zh-hans/index.html", "ja/index.html"]
    homes += [f"{l}/index.html" for l in NEW_LOCALES if by_locale[l]]
    for home in homes:
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
