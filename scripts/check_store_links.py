#!/usr/bin/env python3
"""Checks the form of every Mac App Store listing URL in the built site.

Usage:
    python3 scripts/check_store_links.py [--root public] [--self-test]

Since 2026-10-12 (website #36) the site's on-page App Store links are App Store Connect campaign
links, so the App Store can say which page sent a download. Everything a machine reads stays plain.
Every listing URL gets exactly one verdict; the rules are:

  R5  A listing URL carrying any query parameter other than pt, ct and mt (utm_*, ...), anywhere.
      Judged first, so a stray parameter is always reported as this.
  R1  In public/**/*.html, every <a href> to apps.apple.com is exactly
      https://apps.apple.com/app/apple-store/id6812925073?pt=128976951&amp;ct=<ct>&amp;mt=8
      (the `&` is written `&amp;` in HTML), and no listing URL appears outside an <a href>.
  R2  Its <ct> is `web-` + the first path segment of the page's slug, `web-home` for a home page,
      `web-404` for the 404 pages, `web-themes` for themes/third-party-notices.html. No locale in it.
      Page-specific positions also allow home: web-home-iphone/web-close; features: web-mac-iphone;
      pay-once: web-pricing.
  R6  Every HTML page except redirect stubs includes the Smart App Banner in its head.
  R3  A listing URL inside <script type="application/ld+json"> is exactly the plain
      https://apps.apple.com/app/id6812925073 (downloadUrl, sameAs).
  R4  A listing URL in public/**/*.md and public/**/*.txt (the twins, llms.txt, llms-full.txt,
      product-facts.md) is exactly the plain form.

check_links.py holds the shape of the URL on every file type; this script does the strict per-file
work. /go/app-store stays plain, and check_redirects.py keeps that.

--self-test builds a small tree, plants one break per rule in a copy, and fails unless each plant is
reported by its own rule's message and the clean tree passes. Then it checks the real tree.
"""
import re
import shutil
import sys
import tempfile
from pathlib import Path

PLAIN = "https://apps.apple.com/app/id6812925073"
CAMPAIGN_BASE = "https://apps.apple.com/app/apple-store/id6812925073"
PROVIDER = "128976951"
LOCALE_PREFIXES = ("zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko")

LISTING = re.compile(r"https?://apps\.apple\.com/[^\s\"'<>)\]`]*")
LD_BLOCK = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
CAMPAIGN_HTML = re.compile(
    re.escape(CAMPAIGN_BASE) + r"\?pt=(?P<pt>[^&]*)&amp;ct=(?P<ct>[^&]*)&amp;mt=8$")
ALLOWED_PARAMS = {"pt", "ct", "mt"}


def url_of(match) -> str:
    return match.group(0).rstrip(".,;:!?")


def expected_ct(relative: str) -> str:
    """The campaign token an HTML file's links must carry, from its path under public/."""
    parts = relative.split("/")
    if parts[0] in LOCALE_PREFIXES:
        parts = parts[1:]
    if parts == ["404.html"]:
        return "web-404"
    if parts == ["themes", "third-party-notices.html"]:
        return "web-themes"
    folder = parts[:-1]
    return "web-" + folder[0] if folder else "web-home"


def stray_params(url: str) -> list:
    query = url.partition("?")[2]
    names = [pair.partition("=")[0] for pair in re.split(r"&(?:amp;)?", query) if pair]
    return [name for name in names if name not in ALLOWED_PARAMS]


def check_html(relative: str, text: str, problems: list) -> int:
    count = 0
    head = re.search(r"<head\b[^>]*>(.*?)</head>", text, re.S | re.I)
    redirect = head and re.search(r'<meta\s+http-equiv=["\']refresh["\']', head.group(1), re.I)
    if not redirect and (not head or '<meta name="apple-itunes-app" content="app-id=6812925073">' not in head.group(1)):
        problems.append(f"R6 {relative}: missing Smart App Banner meta in head")
    for block in LD_BLOCK.findall(text):
        for match in LISTING.finditer(block):
            count += 1
            url = url_of(match)
            if stray_params(url):
                problems.append(f"R5 {relative}: listing URL with a parameter other than pt/ct/mt: {url}")
            elif url != PLAIN:
                problems.append(f"R3 {relative}: JSON-LD listing URL must be exactly {PLAIN}, found {url}")
    rest = LD_BLOCK.sub("", text)
    want = expected_ct(relative)
    path = relative.split("/")
    if path[0] in LOCALE_PREFIXES:
        path = path[1:]
    positions = {
        "index.html": {"web-home-iphone", "web-close"},
        "features/index.html": {"web-mac-iphone"},
        "pay-once/index.html": {"web-pricing"},
    }
    allowed = {want} | positions.get("/".join(path), set())
    for match in LISTING.finditer(rest):
        count += 1
        url = url_of(match)
        if stray_params(url):
            problems.append(f"R5 {relative}: listing URL with a parameter other than pt/ct/mt: {url}")
            continue
        in_href = rest[:match.start()].endswith('href="') and rest[match.end():match.end() + 1] == '"'
        if not in_href:
            problems.append(f"R1 {relative}: listing URL outside an <a href>: {url}")
            continue
        form = CAMPAIGN_HTML.match(url)
        if not form:
            problems.append(f"R1 {relative}: <a href> to the listing isn't the campaign form {CAMPAIGN_BASE}?pt={PROVIDER}&amp;ct={want}&amp;mt=8: {url}")
        elif form.group("pt") != PROVIDER:
            problems.append(f"R1 {relative}: wrong provider token pt={form.group('pt')}, want pt={PROVIDER}: {url}")
        elif form.group("ct") not in allowed:
            problems.append(f"R2 {relative}: wrong campaign token ct={form.group('ct')}, want ct={want}: {url}")
    return count


def check_plain(relative: str, text: str, problems: list) -> int:
    count = 0
    for match in LISTING.finditer(text):
        count += 1
        url = url_of(match)
        if stray_params(url):
            problems.append(f"R5 {relative}: listing URL with a parameter other than pt/ct/mt: {url}")
        elif url != PLAIN:
            problems.append(f"R4 {relative}: listing URL in a Markdown/text file must be exactly {PLAIN}, found {url}")
    return count


def check_tree(root: Path):
    problems, counts = [], {".html": 0, ".md": 0, ".txt": 0}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in counts:
            continue
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix == ".html":
            counts[".html"] += check_html(relative, text, problems)
        else:
            counts[path.suffix] += check_plain(relative, text, problems)
    return problems, counts


# --- self-test -----------------------------------------------------------------------------------

def campaign_href(ct: str) -> str:
    return f"{CAMPAIGN_BASE}?pt={PROVIDER}&amp;ct={ct}&amp;mt=8"


def fixture(root: Path) -> None:
    """A tree with every kind of file the rules look at, all conforming."""
    def write(relative, text):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def page(ct):
        return ('<head><meta name="apple-itunes-app" content="app-id=6812925073"></head>\n'
                f'<footer><a href="{campaign_href(ct)}">Mac App Store</a></footer>\n'
                f'<script type="application/ld+json">{{"downloadUrl": "{PLAIN}", "sameAs": ["{PLAIN}"]}}</script>\n')
    write("index.html", page("web-home"))
    write("zh-hant/index.html", page("web-home"))
    write("view-markdown-on-mac/index.html", page("web-view-markdown-on-mac"))
    write("zh-hant/vs/macmd-viewer/index.html", page("web-vs"))
    write("404.html", page("web-404"))
    write("themes/third-party-notices.html", page("web-themes"))
    write("view-markdown-on-mac/index.md", f"Get it on the [Mac App Store]({PLAIN}).\n")
    for prefix in ("", *(locale + "/" for locale in LOCALE_PREFIXES)):
        for path, tokens in {"index.html": ("web-home-iphone", "web-close"),
                             "features/index.html": ("web-mac-iphone",),
                             "pay-once/index.html": ("web-pricing",)}.items():
            write(prefix + path, page(expected_ct(prefix + path)) +
                  "".join(f'<a href="{campaign_href(token)}">Download</a>' for token in tokens))
    write("llms.txt", f"- App: {PLAIN}\n")


def self_test() -> int:
    failures = 0
    base = Path(tempfile.mkdtemp(prefix="check_store_links_"))
    try:
        clean = base / "clean"
        fixture(clean)
        problems, _ = check_tree(clean)
        print(f"self-test: clean fixture, {len(problems)} problems")
        if problems:
            failures += 1
            for line in problems:
                print(f"  UNEXPECTED {line}")

        def edit(relative, old, new):
            def apply(root):
                target = root / relative
                text = target.read_text(encoding="utf-8")
                assert old in text, (relative, old)
                target.write_text(text.replace(old, new, 1), encoding="utf-8")
            return apply

        view = "view-markdown-on-mac/index.html"
        plants = [
            ("position token on the wrong page", "R2 view-markdown-on-mac/index.html: wrong campaign token ct=web-close",
             edit(view, "ct=web-view-markdown-on-mac", "ct=web-close")),
            ("localized position token on the wrong page", "R2 zh-hant/vs/macmd-viewer/index.html: wrong campaign token ct=web-mac-iphone",
             edit("zh-hant/vs/macmd-viewer/index.html", "ct=web-vs", "ct=web-mac-iphone")),
            ("missing Smart App Banner", "R6 index.html: missing Smart App Banner meta in head",
             edit("index.html", '<meta name="apple-itunes-app" content="app-id=6812925073">', "")),
            ("a plain <a href> in a page", "R1 view-markdown-on-mac/index.html: <a href> to the listing isn't the campaign form",
             edit(view, campaign_href("web-view-markdown-on-mac"), PLAIN)),
            ("a listing URL in prose, outside an <a href>", "R1 view-markdown-on-mac/index.html: listing URL outside an <a href>",
             edit(view, "</footer>", f"<p>{PLAIN}</p></footer>")),
            ("a wrong provider token", "R1 view-markdown-on-mac/index.html: wrong provider token pt=1",
             edit(view, f"pt={PROVIDER}", "pt=1")),
            ("a wrong ct", "R2 view-markdown-on-mac/index.html: wrong campaign token ct=web-home",
             edit(view, "ct=web-view-markdown-on-mac", "ct=web-home")),
            ("a locale in the ct", "R2 zh-hant/vs/macmd-viewer/index.html: wrong campaign token ct=web-vs-zh-hant",
             edit("zh-hant/vs/macmd-viewer/index.html", "ct=web-vs", "ct=web-vs-zh-hant")),
            ("a campaign URL inside JSON-LD", "R3 view-markdown-on-mac/index.html: JSON-LD listing URL must be exactly",
             edit(view, f'"downloadUrl": "{PLAIN}"', f'"downloadUrl": "{campaign_href("web-view-markdown-on-mac").replace("&amp;", "&")}"')),
            ("a campaign URL in one .md", "R4 view-markdown-on-mac/index.md: listing URL in a Markdown/text file must be exactly",
             edit("view-markdown-on-mac/index.md", PLAIN, campaign_href("web-view-markdown-on-mac").replace("&amp;", "&"))),
            ("a campaign URL in llms.txt", "R4 llms.txt: listing URL in a Markdown/text file must be exactly",
             edit("llms.txt", PLAIN, campaign_href("web-home").replace("&amp;", "&"))),
            ("a utm_source appended to a page link", "R5 index.html: listing URL with a parameter other than pt/ct/mt",
             edit("index.html", "&amp;mt=8", "&amp;mt=8&amp;utm_source=x")),
            ("a utm_source appended in one .md", "R5 view-markdown-on-mac/index.md: listing URL with a parameter other than pt/ct/mt",
             edit("view-markdown-on-mac/index.md", PLAIN, PLAIN + "?utm_source=x")),
        ]
        for number, (what, message, apply) in enumerate(plants):
            copy = base / f"plant{number}"
            shutil.copytree(clean, copy)
            apply(copy)
            problems, _ = check_tree(copy)
            caught = [line for line in problems if line.startswith(message)]
            others = [line for line in problems if not line.startswith(message)]
            if caught and not others:
                print(f"  caught: {what} -> {caught[0]}")
            else:
                failures += 1
                print(f"  MISSED: {what}: wanted a line starting {message!r}, got {problems or 'nothing'}")
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print(f"self-test: {len(plants)} plants, {failures} failures")
    return 1 if failures else 0


def main(argv) -> int:
    root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else Path(__file__).resolve().parent.parent / "public"
    if "--self-test" in argv and self_test():
        return 1
    problems, counts = check_tree(root)
    print(f"Mac App Store links checked: {counts['.html']} in .html, {counts['.md']} in .md, "
          f"{counts['.txt']} in .txt: {len(problems)} not in the form for their file")
    for line in problems:
        print(" -", line)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
