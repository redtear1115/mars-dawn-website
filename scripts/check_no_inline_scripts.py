#!/usr/bin/env python3
"""Checks that no generated page has an inline `<script>` other than the two the site's CSP
allows by hash (public/_headers: Consent Mode default, then the GTM loader -- see
build_pages.py's `consent_head_html()`).

Every other script on the site must be external (`<script src="...">`), which `script-src 'self'`
already allows without a hash: adding one is how mars-dawn-website#147 shipped an inline
`<script type="module">` that Safari/Chrome/Firefox silently block under this CSP, so the theme
simulator never mounted -- caught only by hand, in a real browser, because nothing here checked
for it. This is that check.

A `<script type="application/ld+json">` (the home page's schema.org block) is data, never executed
as a script, and CSP's script-src doesn't gate it; this check leaves it alone.

Usage:
    python3 scripts/check_no_inline_scripts.py [--root public]
    python3 scripts/check_no_inline_scripts.py --self-test
"""
import argparse
import base64
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCRIPT_TAG = re.compile(r"<script\b([^>]*)>(.*?)</script>", re.S | re.I)
ATTR = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')
NON_EXECUTABLE_TYPES = {"application/ld+json", "application/json"}


def allowed_hashes(headers_text: str) -> set:
    m = re.search(r"Content-Security-Policy:.*", headers_text)
    assert m, "no Content-Security-Policy line found in _headers"
    return set(re.findall(r"'sha256-([A-Za-z0-9+/=]+)'", m.group(0)))


def sha256_b64(text: str) -> str:
    return base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode()


def inline_script_problems(html: str, path: Path, allowed: set) -> list:
    problems = []
    for m in SCRIPT_TAG.finditer(html):
        attrs = dict(ATTR.findall(m.group(1)))
        if "src" in attrs:
            continue  # external: script-src 'self' already allows it, no hash needed
        if attrs.get("type", "").lower() in NON_EXECUTABLE_TYPES:
            continue  # inert data, not gated by script-src
        digest = sha256_b64(m.group(2))
        if digest not in allowed:
            snippet = " ".join(m.group(2).split())[:80]
            problems.append(f"{path}: inline <script> not covered by the CSP hash allowlist ('sha256-{digest}'): {snippet!r}")
    return problems


def check(root: Path) -> list:
    headers_path = root / "_headers"
    if not headers_path.is_file():
        return [f"{headers_path}: missing, can't read the CSP's allowed hashes"]
    allowed = allowed_hashes(headers_path.read_text(encoding="utf-8"))
    problems = []
    for html_path in sorted(root.rglob("*.html")):
        problems += inline_script_problems(html_path.read_text(encoding="utf-8"), html_path.relative_to(root), allowed)
    return problems


def self_test() -> int:
    import shutil
    import tempfile

    baseline = check(ROOT / "public")
    if baseline:
        print("self-test: the real tree already fails:", baseline, file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "public"
        shutil.copytree(ROOT / "public", work)
        target = work / "themes" / "new" / "index.html"
        text = target.read_text(encoding="utf-8")
        assert "</head>" in text
        planted = text.replace("</head>", '<script type="module">alert(1)</script>\n</head>', 1)
        target.write_text(planted, encoding="utf-8")
        result = check(work)
        if any("alert(1)" in p for p in result):
            print("  caught: a planted inline <script> (its own message)")
        else:
            print("  MISSED: a planted inline <script>", file=sys.stderr)
            return 1

    # Prove the restore worked: the real tree (never touched) is still clean.
    restored = check(ROOT / "public")
    if restored:
        print(f"  MISSED: the real tree is no longer clean: {restored}", file=sys.stderr)
        return 1
    print("self-test: 1 plant, 0 missed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=str(ROOT / "public"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    problems = check(Path(args.root))
    for p in problems:
        print(f"::error::{p}")
    if problems:
        print(f"{len(problems)} problem(s). Move the script to an external file (script-src 'self' already allows it).")
        return 1
    n = len(list(Path(args.root).rglob("*.html")))
    print(f"{n} page(s) checked: every inline <script> is one of the CSP's hashed pair, 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
