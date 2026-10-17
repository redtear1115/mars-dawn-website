#!/usr/bin/env python3
"""Checks that every page's hreflang set is complete and reciprocal, in the HTML and the sitemap.

Usage:
    python3 scripts/check_hreflang.py [--root public]

For every public/**/index.html page it checks that:
- <html lang> matches the locale its path is under;
- the page lists exactly one alternate for every locale that has this page (read from the files on
  disk, since a locale may have only some pages) plus x-default, and x-default is the en page;
- the alternate for its own language is its canonical URL;
- every alternate is a page that exists, and that page lists the same set back (reciprocity);
- the "More" group follows the locales this page has: with none of de, fr, es and ko the header has no
  `details.lang-more` and the narrow switch no separator; with any, exactly one of each; and the More
  button names the page's own language when that is one of them (#247);
- the page has exactly one language switch (`nav.lang`), and each of its two copies (the wide one and the
  narrow one: CSS shows one) links to the same pages as the alternates, on its own and not as one merged
  list, with exactly one link marked aria-current, the page's own language (#247).
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import chrome_parse  # noqa: E402  (reads the header's markup; does not import build_pages)

BASE_URL = "https://marsdawn.southern-light.dev"
# hreflang value -> path prefix. Mirrors LOCALES in build_pages.py, written out again on purpose:
# a check that imports the thing it checks can't catch a mistake in it.
# de, fr, es and ko are listed here though the site may not serve them: a locale counts only when it has
# pages on disk, and check_locales.py is what fails a half-built or unfinished one.
LOCALES = {"en": "/", "zh-Hant": "/zh-hant/", "zh-Hans": "/zh-hans/", "ja": "/ja/",
           "de": "/de/", "fr": "/fr/", "es": "/es/", "ko": "/ko/"}
MORE = ("de", "fr", "es", "ko")   # the languages the switch keeps under "More"
LABEL = {"en": "English", "zh-Hant": "繁體中文", "zh-Hans": "简体中文", "ja": "日本語",
         "de": "Deutsch", "fr": "Français", "es": "Español", "ko": "한국어"}   # each language's own name


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.canonical = None
        self.alternates = []  # (hreflang, href)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "link" and a.get("rel") == "alternate" and "hreflang" in a:
            self.alternates.append((a["hreflang"], a.get("href")))


def locale_of(url_path: str) -> str:
    for lang, prefix in LOCALES.items():
        if prefix != "/" and url_path.startswith(prefix):
            return lang
    return "en"


def slug_of(url_path: str) -> str:
    prefix = LOCALES[locale_of(url_path)]
    return url_path[len(prefix):] if prefix != "/" else url_path[1:]


def expected_langs(root: Path, url_path: str) -> set:
    slug = slug_of(url_path)
    have = {lang for lang, prefix in LOCALES.items() if (root / (prefix.lstrip("/") + slug) / "index.html").exists()}
    return have | {"x-default"}


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
        text = path.read_text(encoding="utf-8")
        head.feed(text)
        where = rel
        if head.lang != locale_of(rel):
            problems.append(f"{where}: <html lang={head.lang!r}>, expected {locale_of(rel)!r}")
        langs = [lang for lang, _ in head.alternates]
        expected = expected_langs(root, rel)
        if "en" not in expected:
            problems.append(f"{where}: no en version of this page")
        if set(langs) != expected or len(langs) != len(expected):
            missing, extra = expected - set(langs), sorted({x for x in langs if langs.count(x) > 1 or x not in expected})
            problems.append(f"{where}: hreflang set is off (missing {sorted(missing)}, extra or repeated {extra})")
        alts = dict(head.alternates)
        if head.canonical != url:
            problems.append(f"{where}: canonical is {head.canonical}, expected {url}")
        if alts.get(locale_of(rel)) != url:
            problems.append(f"{where}: its own-language alternate is {alts.get(locale_of(rel))}, expected {url}")
        if "x-default" in alts and alts["x-default"] != alts.get("en"):
            problems.append(f"{where}: x-default {alts['x-default']} isn't the en page {alts.get('en')}")
        chrome = chrome_parse.parse(text)
        if chrome.nav_lang_count != 1:
            problems.append(f"{where}: {chrome.nav_lang_count} language switches (nav.lang), want exactly 1")
        want = {lang: href for lang, href in alts.items() if lang != "x-default"}
        for copy in ("wide", "narrow"):
            links = chrome.lang[copy]
            switch = {lang: BASE_URL + href for lang, href, _, _ in links}
            if switch != want or len(links) != len(want):
                problems.append(f"{where}: {copy} language switch {sorted(switch.items())} doesn't match the alternates")
            marked = [lang for lang, _, _, current in links if current == "true"]
            if marked != [head.lang]:
                problems.append(f"{where}: {copy} language switch marks {marked} aria-current, want just the page's own language {head.lang!r}")
        live_more = [lang for lang in want if lang in MORE]
        if not live_more and (chrome.lang_more_details or chrome.lang_seps):
            problems.append(f"{where}: the More group is empty (no de, fr, es or ko version) but the header has "
                            f"{chrome.lang_more_details} details.lang-more and {chrome.lang_seps} narrow separator(s)")
        elif live_more and (chrome.lang_more_details, chrome.lang_seps) != (1, 1):
            problems.append(f"{where}: the More group has {live_more} but the header has {chrome.lang_more_details} "
                            f"details.lang-more and {chrome.lang_seps} narrow separator(s), want 1 and 1")
        elif live_more:
            shown = chrome.lang_more_summary
            if head.lang in MORE and (shown is None or shown != (LABEL[head.lang], head.lang)):
                problems.append(f"{where}: the More button shows {shown}, want the page's own language {(LABEL[head.lang], head.lang)}")
            elif head.lang not in MORE and (shown is None or shown[0] in LABEL.values() or shown[1] is not None):
                problems.append(f"{where}: the More button shows {shown}, but the page isn't in the More group, so it should say More")
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
