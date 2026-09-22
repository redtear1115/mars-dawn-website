#!/usr/bin/env python3
"""Checks that every same-site link in the built site points at a file that exists.

Usage:
    python3 scripts/check_links.py [--root public]

Reads every .html, .md, .txt, .xml and .css file under the root and collects same-site targets:
href, src and srcset in HTML; Markdown links and bare site URLs in .md and .txt; <loc> and
alternate hrefs in the sitemap; url() in CSS. Relative paths ("/x/"), and absolute URLs on
marsdawn.southern-light.dev, both count. A path ending in "/" needs its index.html. Query strings
and fragments are ignored. mailto:, other hosts and data: URLs are not checked.

A same-site link may also point at a redirect: a source listed in public/_redirects, which Cloudflare
answers with a redirect and no file (`/go/app-store`, the link published for the Mac App Store
listing). Those sources count as existing; scripts/check_redirects.py checks where they go. A link
to a `/go/` path that isn't listed there is broken like any other:

    cp -R public /tmp/site && sed -i '' 's#href="/zh-hant/support/"#href="/go/nope"#' /tmp/site/support/index.html
    python3 scripts/check_links.py --root /tmp/site

Exits 1 and lists every broken link. To see it catch one, check a copy of public/ with a link
pointed at a page that doesn't exist:

    cp -R public /tmp/site && sed -i '' 's#href="/zh-hant/support/"#href="/zh-hans/nope/"#' /tmp/site/support/index.html
    python3 scripts/check_links.py --root /tmp/site
"""
import re
import sys
from pathlib import Path

BASE_URL = "https://marsdawn.southern-light.dev"

PATTERNS = [
    re.compile(r'(?:href|src)="([^"]+)"'),
    re.compile(r'srcset="([^"]+)"'),
    re.compile(r"\]\(([^)\s]+)\)"),
    re.compile(r"<loc>([^<]+)</loc>"),
    re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)"),
    re.compile(r"(?<![\w(\"'=])(" + re.escape(BASE_URL) + r"/[^\s)\"'<>`]*)"),
]


def targets(text: str):
    for pattern in PATTERNS:
        for match in pattern.finditer(text):
            value = match.group(1)
            if pattern.pattern.startswith("srcset"):
                for candidate in value.split(","):
                    yield candidate.strip().split(" ")[0]
            else:
                yield value


def site_path(link: str):
    """The site path a link points at, or None if it isn't a same-site link."""
    if link.startswith(BASE_URL):
        link = link[len(BASE_URL):] or "/"
    if not link.startswith("/") or link.startswith("//"):
        return None
    return re.split(r"[?#]", link, maxsplit=1)[0]


def redirect_sources(root: Path) -> set:
    """The paths public/_redirects answers with a redirect, so a link to one isn't broken."""
    file = root / "_redirects"
    if not file.is_file():
        return set()
    sources = set()
    for line in file.read_text(encoding="utf-8").splitlines():
        fields = line.split()
        if fields and not fields[0].startswith("#") and len(fields) in (2, 3):
            sources.add(fields[0])
    return sources


def main(argv) -> int:
    root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else Path(__file__).resolve().parent.parent / "public"
    broken, checked = [], 0
    redirected = redirect_sources(root)
    for path in sorted(root.rglob("*")):
        if path.suffix not in {".html", ".md", ".txt", ".xml", ".css"} or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for link in targets(text):
            target = site_path(link)
            if target is None:
                continue
            checked += 1
            file = root / target.lstrip("/")
            if target.endswith("/"):
                file = file / "index.html"
            if not file.is_file() and target not in redirected:
                broken.append(f"{path.relative_to(root)}: {link}")
    print(f"{checked} same-site links checked: {len(broken)} broken")
    for line in broken:
        print(" -", line)
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
