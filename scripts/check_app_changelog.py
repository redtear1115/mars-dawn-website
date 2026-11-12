#!/usr/bin/env python3
"""Checks /changelog/'s app sections (website #273, #368) against their vendored sources.

Usage:
    python3 scripts/check_app_changelog.py [--root public] [--self-test] [--release] [--no-pending-in-public]

The expected page is computed from vendor/app-release-notes/whats-new.json (each app version's What's
New on the App Store, vendored from the app repo's approved release notes by scripts/tmde130/ingest.py:
the Mac's under "versions", the iPhone and iPad app's under "ios") and scripts/tmde130/data.py (the page
copy, from the pinned comments on #273 and #368), never from the build's own code. The page has three
sections in this order: the Mac app (h2 #marsdawn-app), the iPhone and iPad app (h2 #marsdawn-ios), the
CLI (h2 #marsdawn-command-line-tool). A version marked "pending" in whats-new.json is not on the App
Store yet and is not published: the page lists only the other versions, and while every iOS version is
pending it has no iOS section at all (the sections A8-A12 then expect none). In every locale's
/changelog/index.html and its index.md twin:

  A1  whats-new.json's sha256 is the one in manifest.json.
  A2  A Mac version the App Store has in the locale's language with a What's New: every bullet, verbatim
      (escaped in the HTML), under that version's heading in the Mac section.
  A3  A version whose What's New is empty there (1.0.0, the first release): the "first release" line
      under its heading.
  A4  A Mac version the App Store doesn't have in that language: no heading for it in the Mac section.
  A5  The "earlier versions are in English only" line is there if and only if the locale misses a Mac
      version, as the Mac section's last paragraph.
  A6  The page copy: meta description, intro, the three section headings' text, the CLI line.
  A7  The CLI entries are h3 under the CLI heading, each with its old anchor (#marsdawn-0-6-3, ...),
      the same versions in every locale.
  A8  The Mac, iOS and CLI headings are all there, in that order (HTML and Markdown twin).
  A9  An iOS version's bullets: every one verbatim (escaped in the HTML) in the HTML and in the .md
      twin, and as many <li> as bullets. (Mac 1.0.2 and iOS 1.0.2 have the same title: the two are
      kept apart by section, the .md twin's Mac and iOS parts are cut at their ## headings first.)
  A10 An iOS version has its h3 with anchor ios-<version> (#ios-1-0-2) and the title MarsDawn <version>,
      and a "### MarsDawn <version>" in the .md twin's iOS part.
  A11 That h3 is inside the iOS section, and the iOS section has no other h3.
  A12 The iOS line ("versions before 1.0.2 are not listed") is the iOS section's last paragraph, in the
      HTML and in the .md twin.
  A13 A pending version is not on the page: no heading or anchor for it in the HTML or the twin, and no iOS
      section while no iOS version is published.
  A14 A listed version's date line is its `released` date, as the page writes dates in that locale, in the
      HTML and in the .md twin.
  A15 The Mac and iOS sections list exactly the versions of whats-new.json that are published (not
      pending) and that the locale has: no version more (HTML and twin).

--self-test plants one break per rule in a copy of the built pages and of the vendored file, and
fails unless each plant is reported by its own rule's message and nothing else, and the clean copy
passes. A2 and A9 also get plants that change the last character of a bullet in the HTML and one in the
.md twin, each of which must be reported as a missing bullet: a dropped bullet alone would still be
caught by the bullet count if the text comparison stopped comparing text (#292). Then it checks the
real tree (or --root's).

--release (not run in CI) fails while whats-new.json has a version marked "pending", Mac or iOS: a
version the App Store doesn't have yet is vendored from the app repo's release notes with a placeholder
date, and the site must not merge with that date. --self-test covers it too.

--no-pending-in-public scans every text file in public/ (html, md, txt, xml, json, atom, rss, vtt, js, css,
svg, _headers, _redirects) for each version that whats-new.json marks pending (read from the file, never
from a constant) and fails if one is published there. A pending version is found by its context, not by
its digits, because "1.0.2" is also the Mac's shipped 1.0.2 and "1.2.2" can sit inside "11.2.2", "1.2.20"
or a URL:
  P1  the anchor of its entry (app-1-2-2 / ios-1-0-2), as an id or a #link, with no word character or
      hyphen on either side;
  P2  a "MarsDawn <version>" heading inside that platform's section (the Mac or the iPhone and iPad
      heading of any locale, in HTML or Markdown), the version bounded by a non-word character and not
      followed by ".<digit>" or "-<digit>";
  P3  for a version no platform has shipped (so not 1.0.2, which the Mac has): "MarsDawn <version>" anywhere,
      and the quoted JSON string "<version>" (JSON-LD, JSON and feeds);
  P4  for a Mac version: "softwareVersion": "<version>" even when the version is shared;
  P5  its date: the ISO date and the date as each locale's changelog writes it.
The roadmap's "Mac 1.2.2" under "Next" is a plan, not a release, and is not one of these contexts. --self-test
covers it too.
"""
import copy as copylib
import datetime
import hashlib
import html
import importlib.util
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "vendor" / "app-release-notes"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
# The three sections, in page order: key, the id of its h2.
HEADS = (("app", "marsdawn-app"), ("ios", "marsdawn-ios"), ("cli", "marsdawn-command-line-tool"))
# How a locale's changelog writes a date. Its own copy of the rule, so a wrong date in the build is caught.
MONTHS_LOCALES = ("en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko")
MONTHS = {
    "en": "January February March April May June July August September October November December".split(),
    "de": "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split(),
    "fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(),
    "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(),
}


def fmt_date(locale: str, iso: str) -> str:
    y, m, d = (int(n) for n in iso.split("-"))
    if locale in ("zh-hant", "zh-hans"):
        return f"{y} 年 {m} 月 {d} 日"
    if locale == "ja":
        return f"{y}年{m}月{d}日"
    if locale == "ko":
        return f"{y}년 {m}월 {d}일"
    month = MONTHS[locale][m - 1]
    if locale == "de":
        return f"{d}. {month} {y}"
    if locale == "es":
        return f"{d} de {month} de {y}"
    if locale == "fr" and d == 1:
        return f"1er {month} {y}"
    return f"{d} {month} {y}"


def is_pending(entry: dict) -> bool:
    return bool(entry.get("pending"))


def anchor_of(prefix: str, version: str) -> str:
    return prefix + "-" + version.replace(".", "-")


def load_copy() -> dict:
    spec = importlib.util.spec_from_file_location("tmde130_data", ROOT / "scripts" / "tmde130" / "data.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DATA


def page_dir(public: Path, locale: str) -> Path:
    return public / "changelog" if locale == "en" else public / locale / "changelog"


def plain(fragment: str) -> str:
    """Text of an HTML fragment as the .md twin writes it: links as [text](href), entities decoded."""
    text = re.sub(r'<a href="([^"]*)">(.*?)</a>', r"[\2](\1)", fragment)
    return twin(html.unescape(re.sub(r"<[^>]+>", "", text)))


def twin(text: str) -> str:
    """The site's HTML-to-Markdown converter writes a no-break space as a plain space (every twin does)."""
    return text.replace("\u00a0", " ")


def no_shy(text: str) -> str:
    return text.replace("&shy;", "").replace("­", "")


def section(page: str, anchor: str) -> str:
    """The HTML from the heading with this id to the next h2 or h3."""
    m = re.search(rf'<h3 id="{anchor}">.*?(?=<h[23][\s>]|$)', page, re.S)
    return m.group(0) if m else ""


def md_section(md: str, title: str) -> str:
    m = re.search(rf"^### {re.escape(title)}\n(.*?)(?=^##)", md + "\n##", re.S | re.M)
    return m.group(1) if m else ""


def html_heads(main: str, spec: tuple = HEADS) -> dict:
    """{key: (start, text)} of the h2 of each section that is there, found by its id."""
    out = {}
    for key, anchor in spec:
        m = re.search(rf'<h2 id="{anchor}">(.*?)</h2>', main, re.S)
        if m:
            out[key] = (m.start(), m.group(1))
    return out


def html_part(main: str, heads: dict, key: str) -> str:
    """The section's HTML: from its h2 to the next h2 of whichever section comes next (to the end for the
    last), so a section out of order still owns its own text."""
    if key not in heads:
        return ""
    start = heads[key][0]
    return main[start:min([s for s, _ in heads.values() if s > start] + [len(main)])]


def md_start(md: str, title: str) -> int:
    m = re.search(rf"^## {re.escape(title)}$", md, re.M)
    return m.start() if m else -1


def md_part(md: str, title: str) -> str:
    """The twin's text under the `## title` line, up to the next `## ` heading."""
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1) if m else ""


def last_paragraph(md_text: str) -> str:
    return md_text.rstrip().split("\n\n")[-1]


def release_problems(notes: dict) -> list:
    """--release: a version still marked pending (Mac or iOS) is not ready to merge."""
    pending = [f"{name} {e['version']}" for name, entries in (("Mac", notes["versions"]), ("iOS", notes["ios"]["versions"]))
               for e in entries if e.get("pending")]
    if not pending:
        return []
    return ["pending versions: " + ", ".join(pending) + " - set their dates from the App Store and run the ingester "
            "without `pending` before merging"]


def date_problems(where: str, label: str, locale: str, entry: dict, anchor: str, body: str, md_body: str) -> list:
    """A14: the line after the version's heading is its `released` date, in the HTML and in the twin."""
    date = fmt_date(locale, entry["released"])
    out = []
    if not re.match(rf'<h3 id="{re.escape(anchor)}">[^<]*</h3>\n<p>{re.escape(date)}</p>\n', body):
        out.append(f"A14 {where}: {label}: the date line in the HTML is not {date!r} ({entry['released']})")
    lines = [l for l in md_body.split("\n") if l.strip()]
    if not lines or lines[0] != date:
        out.append(f"A14 {where}: {label}: the date line in the .md twin is not {date!r} ({entry['released']})")
    return out


def extra_problems(where: str, label: str, prefix: str, html_part_text: str, md_text: str, listed: list,
                   pending: list) -> list:
    """A15: the section lists no version that whats-new.json does not publish. (A pending one is A13's; a
    published one a locale doesn't have is A4's; an iOS anchor that is not ios-* is A11's.)"""
    known = {e["version"] for e in listed} | {e["version"] for e in pending}
    extra = [v for v in re.findall(r'<h3 id="[^"]*">MarsDawn ([^<\s]+)</h3>', html_part_text) if v not in known]
    out = []
    if extra:
        out.append(f"A15 {where}: the {label} section lists versions that are not in whats-new.json: {extra}")
    extra_md = [v for v in re.findall(r"^### MarsDawn (\S+)\s*$", md_text, re.M) if v not in known]
    if extra_md:
        out.append(f"A15 {where}: the {label} section of the .md twin lists versions that are not in whats-new.json: {extra_md}")
    return out


TEXT_SUFFIXES = {".html", ".md", ".txt", ".xml", ".json", ".atom", ".rss", ".vtt", ".js", ".css", ".svg"}
TEXT_NAMES = {"_headers", "_redirects"}


def _version_re(version: str) -> str:
    """The version as a whole number: not inside 11.2.2 or 1.2.20, not 1.2.2.1 or 1.2.2-beta (a following
    full stop that ends a sentence is fine)."""
    return rf"(?<![\w.]){re.escape(version)}(?!\w|\.\d|-\d)"


def pending_list(notes: dict) -> list:
    """[(platform key "app" or "ios", label, entry)] for every version marked pending, read from the data."""
    return ([("app", "Mac", e) for e in notes["versions"] if is_pending(e)]
            + [("ios", "iOS", e) for e in notes["ios"]["versions"] if is_pending(e)])


def text_files(public: Path) -> list:
    return sorted(f for f in public.rglob("*") if f.is_file() and (f.suffix in TEXT_SUFFIXES or f.name in TEXT_NAMES))


def platform_spans(text: str, copy: dict) -> list:
    """[(platform key, start, end)] of the Mac and iPhone and iPad sections in a file: an HTML h2 with the
    section's id, or a Markdown `## ` heading with a locale's title for it (llms-full.txt has all eight), up
    to the next h2 or `# ` / `## ` heading."""
    starts = [(m.start(), key) for key, anchor in HEADS[:2] for m in re.finditer(rf'<h2 id="{anchor}">', text)]
    for key in ("app", "ios"):
        for title in {twin(plain(copy[l][f"{key}_h"])) for l in copy}:
            starts += [(m.start(), key) for m in re.finditer(rf"^## {re.escape(title)}$", text, re.M)]
    ends = sorted(m.start() for m in re.finditer(r"<h2[\s>]|^#{1,2} ", text, re.M))
    return [(key, s, next((e for e in ends if e > s), len(text))) for s, key in sorted(starts)]


def scan_public(public: Path, notes: dict, copy: dict) -> list:
    """--no-pending-in-public: P1-P5 (see the module docstring) for every pending version, in every text file."""
    pending = pending_list(notes)
    if not pending:
        return []
    shipped = {e["version"] for e in notes["versions"] + notes["ios"]["versions"] if not is_pending(e)}
    contexts = []   # (rule, platform key, label, version, compiled regex, restricted to the platform's sections)
    dates = []      # (label, version, compiled regex)
    for key, label, entry in pending:
        v = entry["version"]
        contexts.append(("P1", key, label, v, re.compile(rf"(?<![\w-]){re.escape(anchor_of(key, v))}(?![\w-])"), False))
        contexts.append(("P2", key, label, v, re.compile(rf"MarsDawn {_version_re(v)}"), True))
        if v not in shipped:
            contexts.append(("P3", key, label, v, re.compile(rf"MarsDawn {_version_re(v)}"), False))
            contexts.append(("P3", key, label, v, re.compile(rf'"{re.escape(v)}"'), False))
        if key == "app":
            contexts.append(("P4", key, label, v, re.compile(rf'softwareVersion"\s*:\s*"{re.escape(v)}"'), False))
        forms = {entry["released"]} | {fmt_date(l, entry["released"]) for l in MONTHS_LOCALES}
        dates.append((label, v, re.compile("|".join(rf"(?<!\d){re.escape(f)}(?!\d)" for f in sorted(forms)))))
    problems = []
    for path in text_files(public):
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(public).as_posix()
        spans = platform_spans(text, copy)
        for rule, key, label, v, rx, in_section in contexts:
            hits = [m.start() for m in rx.finditer(text)
                    if not in_section or any(k == key and s <= m.start() < e for k, s, e in spans)]
            if hits:
                line = text.count("\n", 0, hits[0]) + 1
                problems.append(f"{rule} {rel}:{line}: pending {label} {v} is published here ({len(hits)}x, "
                                f"{rx.pattern if rule != 'P2' else 'a heading in its section'})")
        for label, v, rx in dates:
            hits = [m.start() for m in rx.finditer(text)]
            if hits:
                line = text.count("\n", 0, hits[0]) + 1
                problems.append(f"P5 {rel}:{line}: the date of pending {label} {v} is published here ({len(hits)}x, "
                                f"{text[hits[0]:hits[0] + 24].splitlines()[0]!r})")
    return problems


def check(public: Path, vendor: Path, copy: dict) -> list:
    problems = []
    raw = (vendor / "whats-new.json").read_bytes()
    manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))
    if hashlib.sha256(raw).hexdigest() != manifest["whats-new.json"]:
        problems.append("A1 vendor/app-release-notes/whats-new.json does not match manifest.json's sha256")
    notes = json.loads(raw)
    to_store = {site: store for store, site in notes["locale_map"].items()}
    # A pending version is not published: the page lists the others (A13 says it must not list this one).
    published = [e for e in notes["versions"] if not is_pending(e)]
    pending_mac = [e for e in notes["versions"] if is_pending(e)]
    ios_published = [e for e in notes["ios"]["versions"] if not is_pending(e)]
    ios_pending = [e for e in notes["ios"]["versions"] if is_pending(e)]
    spec = tuple(h for h in HEADS if h[0] != "ios" or ios_published)
    cli_sets = {}
    for locale in LOCALES:
        folder = page_dir(public, locale)
        page = no_shy((folder / "index.html").read_text(encoding="utf-8"))
        md = no_shy((folder / "index.md").read_text(encoding="utf-8"))
        c = copy[locale]
        where = f"{locale}/changelog"
        main = page[page.index('<main id="main">'):page.index("</main>")]
        heads = html_heads(main)
        titles = {key: twin(plain(c[f"{key}_h"])) for key, _ in HEADS}
        # A8: the headings are there, Mac then iOS then CLI, in the HTML and in the twin (no iOS one while
        # no iOS version is published: A13 says if there is).
        starts = [heads[key][0] if key in heads else -1 for key, _ in spec]
        md_starts = [md_start(md, titles[key]) for key, _ in spec]
        in_order = lambda xs: all(x >= 0 for x in xs) and xs == sorted(xs)  # noqa: E731
        if not in_order(starts) or not in_order(md_starts):
            problems.append(f"A8 {where}: the {', '.join(k for k, _ in spec)} headings are not all there, in that order")
        sound = all(x >= 0 for x in starts) and all(x >= 0 for x in md_starts)
        for key, _ in spec:
            if key in heads and heads[key][1] != c[f"{key}_h"]:
                problems.append(f"A6 {where}: the {key} heading is not the pinned one")
        if not ios_published and ("ios" in heads or md_start(md, titles["ios"]) >= 0):
            problems.append(f"A13 {where}: has the iPhone and iPad section, but no iOS version is published")
        app_part, ios_part = html_part(main, heads, "app"), html_part(main, heads, "ios")
        md_app, md_ios = md_part(md, titles["app"]), md_part(md, titles["ios"])
        omitted = False
        for entry in pending_mac:
            v, anchor = entry["version"], anchor_of("app", entry["version"])
            if f'id="{anchor}"' in main or md_section(md_app, f"MarsDawn {v}"):
                problems.append(f"A13 {where}: Mac {v} is pending (not on the App Store) but the page lists it")
        for entry in ios_pending:
            v, anchor = entry["version"], anchor_of("ios", entry["version"])
            if f'id="{anchor}"' in main or md_section(md_ios, f"MarsDawn {v}"):
                problems.append(f"A13 {where}: iOS {v} is pending (not on the App Store) but the page lists it")
        for entry in published:
            v, anchor = entry["version"], anchor_of("app", entry["version"])
            text = entry["whatsNew"].get(to_store[locale])
            body, md_body = section(app_part, anchor), md_section(md_app, f"MarsDawn {v}")
            if text is None:
                omitted = True
                if f'id="{anchor}"' in main or f"### MarsDawn {v}\n" in md_app:
                    problems.append(f"A4 {where}: has a heading for {v}, which the App Store doesn't have in this language")
                continue
            if not body.startswith(f'<h3 id="{anchor}">MarsDawn {v}</h3>') or not md_body:
                problems.append(f"A2 {where}: no heading for {v}")
                continue
            problems += date_problems(where, f"Mac {v}", locale, entry, anchor, body, md_body)
            if text:
                lacking = [line[2:] for line in text.split("\n")
                           if f"<li>{html.escape(line[2:], quote=False)}</li>" not in body
                           or f"\n- {twin(line[2:])}\n" not in "\n" + md_body + "\n"]
                for bullet in lacking:
                    problems.append(f"A2 {where}: {v} lacks the bullet {bullet[:40]!r}…")
                if not lacking and len(re.findall("<li>", body)) != len(text.split("\n")):
                    problems.append(f"A2 {where}: {v} has a different number of bullets from its What's New")
            elif f'<p>{c["first_release"]}</p>' not in body or plain(c["first_release"]) not in md_body:
                problems.append(f"A3 {where}: {v} lacks the first-release line")
        line = c.get("earlier")
        shown = [line is not None and app_part.rstrip().endswith(f"<p>{line}</p>"), line is not None and plain(line) in md_app]
        if omitted and not all(shown):
            problems.append(f"A5 {where}: the English-only line is missing")
        elif not omitted and any(shown):
            problems.append(f"A5 {where}: the English-only line is there, but no version is missing")
        problems += extra_problems(where, "Mac", "app", app_part, md_app, published, pending_mac)
        # The iOS section (A9-A12). Skipped when a heading is missing or out of order: A8 has said so.
        ios_anchors = []
        if sound and ios_published:
            for entry in ios_published:
                v, anchor = entry["version"], anchor_of("ios", entry["version"])
                ios_anchors.append(anchor)
                text = entry["whatsNew"].get(to_store[locale])
                if not text:
                    problems.append(f"A9 {where}: iOS {v} has no What's New in this language in whats-new.json")
                    continue
                body, md_body = section(main, anchor), md_section(md_ios, f"MarsDawn {v}")
                if not body.startswith(f'<h3 id="{anchor}">MarsDawn {v}</h3>') or not md_body:
                    problems.append(f"A10 {where}: iOS {v} has no h3 with the anchor {anchor} and the title MarsDawn {v}, "
                                    f"or no ### heading in the .md twin's iOS part")
                    continue
                if f'<h3 id="{anchor}">' not in ios_part:
                    problems.append(f"A11 {where}: iOS {v} is not inside the iOS section")
                problems += date_problems(where, f"iOS {v}", locale, entry, anchor, body, md_body)
                lacking = [line[2:] for line in text.split("\n")
                           if f"<li>{html.escape(line[2:], quote=False)}</li>" not in body
                           or f"\n- {twin(line[2:])}\n" not in "\n" + md_body + "\n"]
                for bullet in lacking:
                    problems.append(f"A9 {where}: iOS {v} lacks the bullet {bullet[:40]!r}…")
                if not lacking and len(re.findall("<li>", body)) != len(text.split("\n")):
                    problems.append(f"A9 {where}: iOS {v} has a different number of bullets from its What's New")
            # (An iOS h3 with a wrong anchor is A10's, not this one's.)
            foreign = [a for a in re.findall(r'<h3 id="([^"]*)"', ios_part) if not a.startswith("ios-")]
            if foreign:
                problems.append(f"A11 {where}: the iOS section has h3 that are not iOS versions: {foreign}")
            problems += extra_problems(where, "iOS", "ios", ios_part, md_ios, ios_published, ios_pending)
            ios_line = c["ios_line"]
            if not ios_part.rstrip().endswith(f"<p>{ios_line}</p>") or last_paragraph(md_ios) != plain(ios_line):
                problems.append(f"A12 {where}: the iOS line is not the iOS section's last paragraph")
        if f'<meta name="description" content="{html.escape(c["description"])}">' not in page:
            problems.append(f"A6 {where}: the meta description is not the pinned one")
        intro = re.search(r'<section class="intro">\s*<h1>[^<]*</h1>\s*<p>(.*?)</p>', main, re.S)
        if not intro or intro.group(1) != c["intro"] or plain(c["intro"]) not in md:
            problems.append(f"A6 {where}: the intro is not the pinned one")
        cli_at = heads["cli"][0] if "cli" in heads else -1
        if cli_at < 0 or not main[cli_at:].split("</h2>", 1)[1].lstrip().startswith(f'<p>{c["cli_line"]}</p>'):
            problems.append(f"A6 {where}: the CLI line is not under the CLI heading")
        cli_part = main[cli_at:] if cli_at >= 0 else ""
        cli_heads = re.findall(r'<h3 id="([^"]*)">marsdawn ([0-9.]+)</h3>', cli_part)
        if not cli_heads or any(anchor != "marsdawn-" + v.replace(".", "-") for anchor, v in cli_heads) \
                or re.search(r"<h2[^>]*>marsdawn [0-9]", main):
            problems.append(f"A7 {where}: a CLI entry is not an h3 with its old anchor")
        cli_sets[locale] = [v for _, v in cli_heads]
    if len({tuple(s) for s in cli_sets.values()}) > 1:
        problems.append(f"A7 the CLI versions differ between locales: {cli_sets}")
    return problems


def show_pending(public: Path, vendor: Path, copy: dict) -> None:
    """Test fixture. The built pages leave a pending version out, but the plants below need every version
    on the page, so this writes each pending version into the copy of the pages as a published one (the
    markup and the Markdown the build writes) and clears `pending` in the vendored copy to match. A no-op
    when nothing is pending: the pages are then complete. check() is clean on the result."""
    raw = (vendor / "whats-new.json").read_bytes()
    notes = json.loads(raw)
    if not pending_list(notes):
        return
    to_store = {site: store for store, site in notes["locale_map"].items()}
    for locale in LOCALES:
        folder, c = page_dir(public, locale), copy[locale]
        page, md = (folder / "index.html").read_text(encoding="utf-8"), (folder / "index.md").read_text(encoding="utf-8")
        for key, entries in (("app", notes["versions"]), ("ios", notes["ios"]["versions"])):
            shown = [e for e in entries if is_pending(e) and e["whatsNew"].get(to_store[locale])]
            if not shown:
                continue
            blocks_html, blocks_md = [], []
            for e in shown:
                v, bullets = e["version"], e["whatsNew"][to_store[locale]].split("\n")
                date = fmt_date(locale, e["released"])
                lis = "\n".join(f"  <li>{html.escape(b[2:], quote=False)}</li>" for b in bullets)
                blocks_html.append(f'<h3 id="{anchor_of(key, v)}">MarsDawn {v}</h3>\n<p>{date}</p>\n<ul>\n{lis}\n</ul>')
                blocks_md.append(f"### MarsDawn {v}\n\n{date}\n\n" + "\n".join(f"- {twin(b[2:])}" for b in bullets) + "\n\n")
            h2 = f'<h2 id="{dict(HEADS)[key]}">{c[key + "_h"]}</h2>\n\n'
            md_h2 = f"## {twin(plain(c[key + '_h']))}\n\n"
            cli_h2, md_cli = f'<h2 id="{dict(HEADS)["cli"]}">', f"## {twin(plain(c['cli_h']))}\n"
            if h2 in page:   # the section is there: the pending versions come first in it
                page = page.replace(h2, h2 + "\n\n".join(blocks_html) + "\n\n", 1)
                md = md.replace(md_h2, md_h2 + "".join(blocks_md), 1)
            else:            # the iOS section is not there at all: it goes before the CLI's
                page = page.replace(cli_h2, h2 + "\n\n".join(blocks_html) + f'\n\n<p>{c["ios_line"]}</p>\n\n' + cli_h2, 1)
                md = md.replace(md_cli, md_h2 + "".join(blocks_md) + plain(c["ios_line"]) + "\n\n" + md_cli, 1)
        (folder / "index.html").write_text(page, encoding="utf-8")
        (folder / "index.md").write_text(md, encoding="utf-8")
    for entry in notes["versions"] + notes["ios"]["versions"]:
        entry.pop("pending", None)
    out = (json.dumps(notes, indent=1, ensure_ascii=False) + "\n").encode("utf-8")
    (vendor / "whats-new.json").write_bytes(out)
    manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))
    manifest["whats-new.json"] = hashlib.sha256(out).hexdigest()
    (vendor / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")


def self_test(source: Path) -> bool:
    copy = load_copy()
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        def fresh():
            for name in ("public", "vendor"):
                shutil.rmtree(base / name, ignore_errors=True)
            for locale in LOCALES:
                dst = page_dir(base / "public", locale)
                shutil.copytree(page_dir(source, locale), dst)
            shutil.copytree(VENDOR, base / "vendor")
            show_pending(base / "public", base / "vendor", copy)
            return base / "public", base / "vendor"

        def edit(path: Path, old: str, new: str, count: int = 1):
            text = path.read_text(encoding="utf-8")
            assert old in text, f"self-test plant has nothing to replace in {path}: {old[:60]!r}"
            path.write_text(text.replace(old, new, count), encoding="utf-8")

        def swap(path: Path, first: str, second: str, third: str):
            """Put the section that starts at `second` before the one that starts at `first`."""
            text = path.read_text(encoding="utf-8")
            a, b, z = text.index(first), text.index(second), text.index(third)
            assert a < b < z, f"self-test swap: the markers are not in order in {path}"
            path.write_text(text[:a] + text[b:z] + text[a:b] + text[z:], encoding="utf-8")

        def move_ios_entry(path: Path, anchor: str):
            """Cut an iOS version's h3 block out of the iOS section and put it first in the Mac section."""
            text = path.read_text(encoding="utf-8")
            start = text.index(f'<h3 id="{anchor}">')
            end = text.index("</ul>", start) + len("</ul>")
            block = text[start:end]
            text = text[:start] + text[end:]
            first_mac = text.index('<h3 id="app-')
            path.write_text(text[:first_mac] + block + "\n\n" + text[first_mac:], encoding="utf-8")

        public, vendor = fresh()
        clean = check(public, vendor, copy)
        if clean:
            print("self-test: the clean copy fails:\n  " + "\n  ".join(clean))
            return False
        notes = json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8"))
        first_bullet = notes["versions"][0]["whatsNew"]["en-US"].split("\n")[0][2:]
        first_v = notes["versions"][-1]["version"]
        first_html = html.escape(first_bullet, quote=False)
        lacks = f"A2 en/changelog: {notes['versions'][0]['version']} lacks the bullet "
        ios_v = notes["ios"]["versions"][0]["version"]
        ios_anchor = "ios-" + ios_v.replace(".", "-")
        ios_bullet = notes["ios"]["versions"][0]["whatsNew"]["en-US"].split("\n")[0][2:]
        ios_html = html.escape(ios_bullet, quote=False)
        ios_lacks = f"A9 en/changelog: iOS {ios_v} lacks the bullet "
        ios_iso, mac_iso = notes["ios"]["versions"][0]["released"], notes["versions"][0]["released"]
        mac_h = '<h2 id="marsdawn-app">'
        ios_h = '<h2 id="marsdawn-ios">'
        cli_h = '<h2 id="marsdawn-command-line-tool">'
        wrong = lambda s: s[:-1] + ("#" if s[-1] != "#" else "%")  # noqa: E731
        plants = [
            ("A1", lambda p, v: edit(v / "whats-new.json", '"dates_read": "2026', '"dates_read": "2025')),
            ("A2", lambda p, v: edit(p / "changelog" / "index.html", f"  <li>{first_html}</li>\n", "")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.html", f"<li>{first_html}</li>", f"<li>{wrong(first_html)}</li>")),
            (lacks, lambda p, v: edit(p / "changelog" / "index.md", f"\n- {twin(first_bullet)}\n", f"\n- {wrong(twin(first_bullet))}\n")),
            ("A3", lambda p, v: edit(p / "zh-hant" / "changelog" / "index.html", f'<p>{copy["zh-hant"]["first_release"]}</p>', "")),
            ("A4", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'{mac_h}{copy["de"]["app_h"]}</h2>\n',
                                     f'{mac_h}{copy["de"]["app_h"]}</h2>\n'
                                     f'<h3 id="app-{first_v.replace(".", "-")}">MarsDawn {first_v}</h3>\n')),
            ("A5", lambda p, v: edit(p / "ko" / "changelog" / "index.html", f'<p>{copy["ko"]["earlier"]}</p>', "")),
            ("A5", lambda p, v: edit(p / "changelog" / "index.html", f'\n\n{ios_h}',
                                     f'\n<p>{copy["en"]["earlier"]}</p>\n\n{ios_h}')),
            ("A6", lambda p, v: edit(p / "ja" / "changelog" / "index.html", copy["ja"]["intro"], copy["ja"]["intro"][:-1])),
            ("A6", lambda p, v: edit(p / "fr" / "changelog" / "index.html", f'{mac_h}{copy["fr"]["app_h"]}</h2>',
                                     f'{mac_h}{copy["fr"]["app_h"][:-1]}</h2>')),
            ("A6", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'{ios_h}{copy["de"]["ios_h"]}</h2>',
                                     f'{ios_h}{copy["de"]["ios_h"][:-1]}</h2>')),
            ("A7", lambda p, v: edit(p / "fr" / "changelog" / "index.html", '<h3 id="marsdawn-0-5-4">', '<h3 id="marsdawn-054">')),
            # A8: the Mac and iOS sections swapped, in the HTML and in the twin.
            ("A8", lambda p, v: swap(p / "ko" / "changelog" / "index.html", mac_h, ios_h, cli_h)),
            ("A8", lambda p, v: swap(p / "zh-hans" / "changelog" / "index.md",
                                     f"## {twin(plain(copy['zh-hans']['app_h']))}\n", f"## {twin(plain(copy['zh-hans']['ios_h']))}\n",
                                     f"## {twin(plain(copy['zh-hans']['cli_h']))}\n")),
            # A9: an iOS bullet gone, and one whose last character differs, in the HTML and in the twin.
            ("A9", lambda p, v: edit(p / "changelog" / "index.html", f"  <li>{ios_html}</li>\n", "")),
            (ios_lacks, lambda p, v: edit(p / "changelog" / "index.html", f"<li>{ios_html}</li>", f"<li>{wrong(ios_html)}</li>")),
            (ios_lacks, lambda p, v: edit(p / "changelog" / "index.md", f"\n- {twin(ios_bullet)}\n", f"\n- {wrong(twin(ios_bullet))}\n")),
            # A10: the iOS anchor is wrong.
            ("A10", lambda p, v: edit(p / "ja" / "changelog" / "index.html", f'<h3 id="{ios_anchor}">', '<h3 id="ios-102">')),
            # A11: the iOS entry sits in the Mac section.
            ("A11", lambda p, v: move_ios_entry(p / "fr" / "changelog" / "index.html", ios_anchor)),
            # A12: the iOS line is gone, from the HTML and from the twin.
            ("A12", lambda p, v: edit(p / "changelog" / "index.html", f'<p>{copy["en"]["ios_line"]}</p>', "")),
            ("A12", lambda p, v: edit(p / "es" / "changelog" / "index.md", plain(copy["es"]["ios_line"]), "")),
            # A14: a wrong date, in an iOS entry (HTML, then twin) and in a Mac entry of another locale.
            ("A14", lambda p, v: edit(p / "ja" / "changelog" / "index.html",
                                      f'<h3 id="{ios_anchor}">MarsDawn {ios_v}</h3>\n<p>{fmt_date("ja", ios_iso)}</p>',
                                      f'<h3 id="{ios_anchor}">MarsDawn {ios_v}</h3>\n<p>2099年1月1日</p>')),
            ("A14", lambda p, v: edit(p / "changelog" / "index.md", f"### MarsDawn {ios_v}\n\n{fmt_date('en', ios_iso)}\n",
                                      f"### MarsDawn {ios_v}\n\n1 January 2099\n")),
            ("A14", lambda p, v: edit(p / "de" / "changelog" / "index.html", f'<p>{fmt_date("de", mac_iso)}</p>', "<p>1. Januar 2099</p>")),
            # A15: one version too many in the iOS section (HTML, then twin) and in the Mac section.
            ("A15", lambda p, v: edit(p / "ja" / "changelog" / "index.html", f'<p>{copy["ja"]["ios_line"]}</p>',
                                      '<h3 id="ios-1-0-1">MarsDawn 1.0.1</h3>\n<p>2026年10月29日</p>\n<ul>\n  <li>x</li>\n</ul>\n\n'
                                      f'<p>{copy["ja"]["ios_line"]}</p>')),
            ("A15", lambda p, v: edit(p / "ko" / "changelog" / "index.md", plain(copy["ko"]["ios_line"]),
                                      "### MarsDawn 1.0.1\n\n2026년 10월 29일\n\n- x\n\n" + plain(copy["ko"]["ios_line"]))),
            ("A15", lambda p, v: edit(p / "fr" / "changelog" / "index.html", f'{mac_h}{copy["fr"]["app_h"]}</h2>\n\n',
                                      f'{mac_h}{copy["fr"]["app_h"]}</h2>\n\n<h3 id="app-9-9-9">MarsDawn 9.9.9</h3>\n'
                                      '<p>1er janvier 2030</p>\n<ul>\n  <li>x</li>\n</ul>\n\n')),
        ]
        for rule, plant in plants:
            public, vendor = fresh()
            plant(public, vendor)
            found = check(public, vendor, copy)
            if len(found) != 1 or not found[0].startswith(rule if rule.endswith(" ") else rule + " "):
                print(f"self-test: plant for {rule} reported {found}")
                ok = False
            else:
                print(f"self-test: {rule.split()[0]} caught: {found[0][:100]}")
        # --release: pending versions fail it, shipped ones pass.
        shipped = copylib.deepcopy(notes)
        for entry in shipped["versions"] + shipped["ios"]["versions"]:
            entry.pop("pending", None)
        both = copylib.deepcopy(shipped)
        both["versions"][0]["pending"] = both["ios"]["versions"][0]["pending"] = True
        mac_only = copylib.deepcopy(shipped)
        mac_only["versions"][0]["pending"] = True
        ios_only = copylib.deepcopy(shipped)
        ios_only["ios"]["versions"][0]["pending"] = True
        for label, data, want in (("none pending", shipped, 0), ("a Mac version pending", mac_only, 1),
                                  ("an iOS version pending", ios_only, 1), ("both pending", both, 1)):
            found = release_problems(data)
            if len(found) != want or (want and not found[0].startswith("pending versions: ")):
                print(f"self-test: --release with {label} reported {found}")
                ok = False
            else:
                print(f"self-test: --release with {label}: {found[0][:100] if found else 'passes'}")
        if "pending versions: Mac %s, iOS %s" % (both["versions"][0]["version"], both["ios"]["versions"][0]["version"]) \
                not in release_problems(both)[0]:
            print("self-test: --release does not name both versions")
            ok = False
        ok = pending_self_test(base, source, copy, notes, fresh) and ok
    return ok


def pending_self_test(base: Path, source: Path, copy: dict, notes: dict, fresh) -> bool:
    """A13 (the pages list a pending version) and --no-pending-in-public (P1-P5)."""
    ok = True

    def expect(label: str, found: list, rules: set, minimum: int = 1):
        nonlocal ok
        got = {f.split()[0] for f in found}
        if got != rules or len(found) < minimum:
            print(f"self-test: {label}: expected {sorted(rules) or 'nothing'}, got {len(found)}: {found[:3]}")
            ok = False
        else:
            print(f"self-test: {label}: {'caught ' + ','.join(sorted(rules)) + ' (' + str(len(found)) + ')' if rules else 'passes'}")

    # A13: the pages (complete: fresh() shows every version) while the data says the newest Mac and iOS version are pending.
    for label, mac, ios in (("a Mac version pending but listed", True, False), ("an iOS version pending but listed", False, True)):
        public, vendor = fresh()
        data = json.loads((vendor / "whats-new.json").read_text(encoding="utf-8"))
        if mac:
            data["versions"][0]["pending"] = True
        if ios:
            data["ios"]["versions"][0]["pending"] = True
        raw = (json.dumps(data, indent=1, ensure_ascii=False) + "\n").encode("utf-8")
        (vendor / "whats-new.json").write_bytes(raw)
        (vendor / "manifest.json").write_text(json.dumps({"whats-new.json": hashlib.sha256(raw).hexdigest()}), encoding="utf-8")
        expect("A13 " + label, check(public, vendor, copy), {"A13"}, minimum=len(LOCALES))
        # The same complete pages, the same data, through --no-pending-in-public: the pending version is found.
        found = scan_public(public, data, copy)
        expect("P1-P5 on the same pages (" + label + ")", found, {"P1", "P2", "P3", "P5"} if mac and not ios
               else {"P1", "P2", "P5"}, minimum=len(LOCALES))

    # --no-pending-in-public on small trees with made-up versions (so the cases hold whatever is pending in the
    # real data). Mac 9.8.7 and iOS 9.8.6 are pending, Mac 9.8.0 is published.
    def entry(v, d, pending=False):
        return {"version": v, "released": d, "whatsNew": {}, **({"pending": True} if pending else {})}

    syn = {"versions": [entry("9.8.7", "2030-01-02", True), entry("9.8.0", "2030-01-01")],
           "ios": {"versions": [entry("9.8.6", "2030-01-03", True)]}}
    shared = {"versions": [entry("9.8.0", "2030-01-01")], "ios": {"versions": [entry("9.8.0", "2030-01-04", True)]}}
    en = copy["en"]
    mac_head, ios_head = f'<h2 id="marsdawn-app">{en["app_h"]}</h2>', f'<h2 id="marsdawn-ios">{en["ios_h"]}</h2>'
    clean = {
        "changelog/index.html": mac_head + '<h3 id="app-9-8-0">MarsDawn 9.8.0</h3><p>1 January 2030</p>',
        "changelog/index.md": f"## {en['app_h']}\n\n### MarsDawn 9.8.0\n\n1 January 2030\n\n- a\n",
        "index.html": '<script type="application/ld+json">{"softwareVersion": "9.8.0"}</script>',
        "llms-full.txt": "with MarsDawn 9.8.0 or later\n\nMarsDawn 9.8.70 and 9.8.7.1 and 19.8.7 and /v9.8.7/x and app-9-8-70\n",
        "roadmap/index.md": "## Next\n\n### Mac 9.8.7\n\n- a plan, not a release\n",
        "sitemap.xml": "<urlset><loc>https://example.test/12030-01-02</loc><lastmod>2030-01-12</lastmod></urlset>",
    }

    def tree(extra: dict, name: str) -> Path:
        root = base / name
        shutil.rmtree(root, ignore_errors=True)
        for rel, text in {**clean, **extra}.items():
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            (root / rel).write_text(text, encoding="utf-8")
        return root

    expect("scan: a clean tree (a published version, a plan on the roadmap, look-alike numbers)",
           scan_public(tree({}, "s0"), syn, copy), set(), minimum=0)
    cases = [
        ("a pending version injected into an html file", {"changelog/index.html": clean["changelog/index.html"] + ios_head + '<h3 id="ios-9-8-6">MarsDawn 9.8.6</h3>'}, syn, {"P1", "P2", "P3"}),
        ("a pending Mac heading without its anchor", {"changelog/index.html": clean["changelog/index.html"] + "<h3>MarsDawn 9.8.7</h3>"}, syn, {"P2", "P3"}),
        ("a pending version in llms-full.txt", {"llms-full.txt": clean["llms-full.txt"] + f"\n## {en['ios_h']}\n\n### MarsDawn 9.8.6\n"}, syn, {"P2", "P3"}),
        ("a pending version in JSON-LD", {"index.html": '<script type="application/ld+json">{"softwareVersion": "9.8.7"}</script>'}, syn, {"P3", "P4"}),
        ("a pending version in an Atom feed", {"feed.atom": "<entry><title>MarsDawn 9.8.7</title></entry>"}, syn, {"P3"}),
        ("a pending version in a JSON feed", {"feed.json": '{"items": [{"version": "9.8.7"}]}'}, syn, {"P3"}),
        ("a pending version's ISO date", {"sitemap.xml": "<lastmod>2030-01-02</lastmod>"}, syn, {"P5"}),
        ("a pending version's date as a locale writes it", {"changelog/index.md": clean["changelog/index.md"] + "\n2 January 2030\n"}, syn, {"P5"}),
        ("an iOS version that shares its number with a shipped Mac one, under the iOS heading",
         {"llms-full.txt": f"## {en['ios_h']}\n\n### MarsDawn 9.8.0\n"}, shared, {"P2"}),
        ("... and its anchor", {"changelog/index.html": '<h3 id="ios-9-8-0">MarsDawn 9.8.0</h3>'}, shared, {"P1"}),
    ]
    for label, extra, data, rules in cases:
        expect("scan: " + label, scan_public(tree(extra, "s1"), data, copy), rules)
    # Not found: a shipped version, and the shared number outside the iOS section.
    expect("scan: a version that is not pending does not trigger it",
           scan_public(tree({"llms-full.txt": '"9.8.0" MarsDawn 9.8.0 app-9-8-0 "softwareVersion": "9.8.0"'}, "s2"), syn, copy), set(), minimum=0)
    expect("scan: a shared number in the Mac section, in JSON-LD and in prose does not trigger it",
           scan_public(tree({"llms-full.txt": f"## {en['app_h']}\n\n### MarsDawn 9.8.0\n\nMarsDawn 9.8.0 or later",
                             "index.html": '{"softwareVersion": "9.8.0", "x": "9.8.0"}'}, "s3"), shared, copy), set(), minimum=0)
    # A pending entry flipped to published: nothing is flagged for it.
    flipped = copylib.deepcopy(syn)
    for e in flipped["versions"] + flipped["ios"]["versions"]:
        e.pop("pending", None)
    every = {"changelog/index.html": '<h3 id="ios-9-8-6">MarsDawn 9.8.6</h3><h3 id="app-9-8-7">MarsDawn 9.8.7</h3>',
             "llms-full.txt": f"## {en['ios_h']}\n\n### MarsDawn 9.8.6\n", "index.html": '{"softwareVersion": "9.8.7"}',
             "sitemap.xml": "<lastmod>2030-01-02</lastmod>"}
    expect("scan: the same tree with the pending entries flipped to published flags nothing",
           scan_public(tree(every, "s4"), flipped, copy), set(), minimum=0)
    expect("scan: ... and with them pending flags them", scan_public(tree(every, "s4"), syn, copy), {"P1", "P2", "P3", "P4", "P5"})
    # The pending versions come from the data, not from a constant: other data, other findings.
    other = {"versions": [entry("9.8.0", "2030-01-01")], "ios": {"versions": [entry("9.8.5", "2030-02-02", True)]}}
    text = {"llms-full.txt": f"## {en['ios_h']}\n\n### MarsDawn 9.8.5\n\nMarsDawn 9.8.5\n9.8.7 on 2030-02-02"}
    expect("scan: data with 9.8.5 pending finds 9.8.5 and its date", scan_public(tree(text, "s5"), other, copy), {"P2", "P3", "P5"})
    expect("scan: data with 9.8.7 pending does not find 9.8.5", scan_public(tree({"llms-full.txt": text["llms-full.txt"].replace("2030-02-02", "")}, "s5"), syn, copy), set(), minimum=0)
    nothing = {"versions": [entry("9.8.0", "2030-01-01")], "ios": {"versions": []}}
    expect("scan: nothing pending, nothing to find", scan_public(tree(every, "s6"), nothing, copy), set(), minimum=0)
    # The real tree and the real data.
    expect("scan: the real public/", scan_public(source, json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8")), copy), set(), minimum=0)
    return ok


def main() -> int:
    args = sys.argv[1:]
    public = ROOT / "public"
    if "--root" in args:
        public = Path(args[args.index("--root") + 1])
    if "--self-test" in args and not self_test(public):
        print("check_app_changelog: self-test FAILED")
        return 1
    if "--no-pending-in-public" in args:
        notes = json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8"))
        pending = pending_list(notes)
        problems = scan_public(public, notes, load_copy())
        for p in problems:
            print(p)
        names = ", ".join(f"{label} {e['version']}" for _, label, e in pending) or "none"
        if problems:
            print(f"check_app_changelog: {len(problems)} places in {public} publish a pending version ({names})")
            return 1
        print(f"check_app_changelog: no pending version in {public} (pending: {names}; "
              f"{len(text_files(public))} text files scanned)")
        return 0
    problems = check(public, VENDOR, load_copy())
    if "--release" in args:
        problems += release_problems(json.loads((VENDOR / "whats-new.json").read_text(encoding="utf-8")))
    for p in problems:
        print(p)
    if problems:
        return 1
    print(f"check_app_changelog: ok ({len(LOCALES)} locales)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
