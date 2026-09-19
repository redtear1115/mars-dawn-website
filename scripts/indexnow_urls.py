#!/usr/bin/env python3
"""Maps files changed under public/ to the URLs they are served at, for IndexNow.

Usage:
    python3 scripts/indexnow_urls.py <before-sha> <after-sha>
    python3 scripts/indexnow_urls.py --sitemap

The first form lists the URLs for files that changed (added, copied, modified
or renamed) between two commits. The second form, used as a fallback when
`before` is unusable (the all-zeros SHA GitHub sends on a branch's first push,
or a commit this checkout can't reach), prints every URL in the sitemap
instead.

Mapping:
    public/x/index.html -> https://marsdawn.southern-light.dev/x/
    public/index.html   -> https://marsdawn.southern-light.dev/
    public/x/index.md   -> https://marsdawn.southern-light.dev/x/index.md
    public/robots.txt   -> https://marsdawn.southern-light.dev/robots.txt
    (any other changed file, e.g. .css/.json/.png, is not pinged)

Prints one URL per line, sorted and de-duplicated.
"""
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
BASE_URL = "https://marsdawn.southern-light.dev"


def changed_files(before: str, after: str) -> list[str]:
    """Repo-relative paths changed under public/ between two commits."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", before, after, "--", "public"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def file_to_url(path: str) -> Optional[str]:
    if not path.startswith("public/"):
        return None
    rel = path[len("public/"):]
    if rel.endswith("index.html"):
        prefix = rel[: -len("index.html")]
        return f"{BASE_URL}/{prefix}" if prefix else f"{BASE_URL}/"
    if rel.endswith(".md") or rel.endswith(".txt"):
        return f"{BASE_URL}/{rel}"
    return None


def sitemap_urls() -> list[str]:
    tree = ET.parse(PUBLIC / "sitemap.xml")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text for loc in tree.getroot().findall("s:url/s:loc", ns) if loc.text]


def main(argv: list[str]) -> int:
    if argv[1:2] == ["--sitemap"]:
        urls = sitemap_urls()
    elif len(argv) == 3:
        before, after = argv[1], argv[2]
        files = changed_files(before, after)
        mapped = (file_to_url(f) for f in files)
        urls = sorted({u for u in mapped if u})
    else:
        print("usage: indexnow_urls.py <before-sha> <after-sha> | --sitemap", file=sys.stderr)
        return 2
    for url in urls:
        print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
