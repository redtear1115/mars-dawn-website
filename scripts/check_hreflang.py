#!/usr/bin/env python3
"""Checks that every page's hreflang set is complete and reciprocal, in the HTML and the sitemap.

Usage:
    python3 scripts/check_hreflang.py [--root public]

For every public/**/index.html page it checks that:
- <html lang> matches the locale its path is under;
- the page lists exactly one alternate per locale plus x-default, and x-default is the en page;
- the alternate for its own language is its canonical URL;
- every alternate is a page that exists, and that page lists the same set back (reciprocity);
- the language switch links to the same four pages.
And for sitemap.xml, that every page is listed once with the same set of alternates as its HTML.

Exits 1 and lists every problem if anything is off. To see it catch one, check a copy of public/
with one alternate removed (the control in website #41):

    cp -R public /tmp/site && sed -i '' '/hreflang="ja" href=.*\\/ja\\/pdf\\//d' /tmp/site/pdf/index.html
    python3 scripts/check_hreflang.py --root /tmp/site
"""
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

BASE_URL = "https://marsdawn.southern-light.dev"
# hreflang value -> path prefix. Mirrors LOCALES in build_pages.py, written out again on purpose:
# a check that imports the thing it checks can't catch a mistake in it.
LOCALES = {"en": "/", "zh-Hant": "/zh-hant/", "zh-Hans": "/zh-hans/", "ja": "/ja/"}
EXPECTED = set(LOCALES) | {"x-default"}


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.canonical = None
        self.alternates = []  # (hreflang, href)
        self.switch = []  # (hreflang, href)
        self._in_switch = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "link" and a.get("rel") == "alternate" and "hreflang" in a:
            self.alternates.append((a["hreflang"], a.get("href")))
        elif tag == "nav" and "lang" in (a.get("class") or "").split():
            self._in_switch = True
        elif tag == "a" and self._in_switch:
            self.switch.append((a.get("hreflang"), a.get("href")))

    def handle_endtag(self, tag):
        if tag == "nav":
            self._in_switch = False


def locale_of(url_path: str) -> str:
    for lang, prefix in LOCALES.items():
        if prefix != "/" and url_path.startswith(prefix):
            return lang
    return "en"


def url_to_file(root: Path, url: str):
    if not url.startswith(BASE_URL + "/"):
        return None
    return root / url[len(BASE_URL) + 1:] / "index.html"


def main(argv) -> int:
    root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else Path(__file__).resolve().parent.parent / "public"
    problems = []
    pages = {}  # url -> {hreflang: href}
    for path in sorted(root.rglob("index.html")):
        rel = "/" + str(path.parent.relative_to(root)).replace("\\", "/") + "/"
        rel = "/" if rel == "/./" else rel
        url = BASE_URL + rel
        head = Head()
        head.feed(path.read_text(encoding="utf-8"))
        where = rel
        if head.lang != locale_of(rel):
            problems.append(f"{where}: <html lang={head.lang!r}>, expected {locale_of(rel)!r}")
        langs = [lang for lang, _ in head.alternates]
        if set(langs) != EXPECTED or len(langs) != len(EXPECTED):
            missing, extra = EXPECTED - set(langs), sorted({x for x in langs if langs.count(x) > 1 or x not in EXPECTED})
            problems.append(f"{where}: hreflang set is off (missing {sorted(missing)}, extra or repeated {extra})")
        alts = dict(head.alternates)
        if head.canonical != url:
            problems.append(f"{where}: canonical is {head.canonical}, expected {url}")
        if alts.get(locale_of(rel)) != url:
            problems.append(f"{where}: its own-language alternate is {alts.get(locale_of(rel))}, expected {url}")
        if "x-default" in alts and alts["x-default"] != alts.get("en"):
            problems.append(f"{where}: x-default {alts['x-default']} isn't the en page {alts.get('en')}")
        switch = {lang: BASE_URL + href for lang, href in head.switch}
        if switch != {lang: href for lang, href in alts.items() if lang != "x-default"}:
            problems.append(f"{where}: language switch {sorted(switch.items())} doesn't match the alternates")
        pages[url] = alts

    for url, alts in pages.items():
        for lang, href in alts.items():
            target = url_to_file(root, href) if href else None
            if target is None or not target.exists():
                problems.append(f"{url}: alternate {lang} -> {href} is not a page")
            elif pages.get(href) != alts:
                problems.append(f"{url}: not reciprocal with {href} ({lang}): the two pages list different alternates")

    sitemap = root / "sitemap.xml"
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
    listed = {}
    for entry in ET.parse(sitemap).getroot().findall("s:url", ns):
        loc = entry.findtext("s:loc", namespaces=ns)
        links = {link.get("hreflang"): link.get("href") for link in entry.findall("x:link", ns)}
        if loc in listed:
            problems.append(f"sitemap: {loc} is listed twice")
        listed[loc] = links
    for url, alts in pages.items():
        if url not in listed:
            problems.append(f"sitemap: {url} is missing")
        elif listed[url] != alts:
            problems.append(f"sitemap: {url} lists different alternates from its HTML")

    print(f"{len(pages)} pages, {len(listed)} sitemap entries checked: {len(problems)} problems")
    for problem in problems:
        print(" -", problem)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
