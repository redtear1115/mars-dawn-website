#!/usr/bin/env python3
"""Checks two things the site's CSP depends on, both learned the hard way on mars-dawn-website#147:

1. No generated page has an inline `<script>` other than the two the CSP allows by hash
   (public/_headers: Consent Mode default, then the GTM loader -- see build_pages.py's
   `consent_head_html()`). Every other script must be external (`<script src="...">`), which
   `script-src 'self'` already allows without a hash: shipping one inline instead is how #147's
   theme simulator got a bootstrap that Safari/Chrome/Firefox silently blocked, so it never
   mounted -- caught only by hand, in a real browser, because nothing here checked for it.

   A `<script type="application/ld+json">` (the home page's schema.org block) is data, never
   executed as a script, and CSP's script-src doesn't gate it; this check leaves it alone.

2. No generated page, and no source file under public/assets/theme-sim/, has a `style="..."`
   attribute. The CSP's `style-src` is `'self'` with no `'unsafe-inline'` and no hash allowance for
   attributes (`style-src-attr` falls back to `style-src`), so an inline `style=` is blocked the
   same way an inline script is -- and when the blocked style was the only thing hiding an element
   (`style="display:none"`), the element doesn't just fail to darken; it becomes visible instead
   (round 2 of #147: two decorative, meant-to-be-hidden SVG paths in the sample diagram, rendered
   because their `display:none` never took effect). Scanning the *source* under
   public/assets/theme-sim/, not just the built pages, catches this where it's actually written --
   a page-only scan would only catch it after the next `build_pages.py` run happened to touch that
   page, and theme-sim/*.js pages are otherwise static (build_pages.py copies them, unchanged).

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
STYLE_ATTR = re.compile(r'\bstyle\s*=\s*"')


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


def style_attribute_problems(text: str, path: Path) -> list:
    problems = []
    for m in STYLE_ATTR.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        snippet = " ".join(text[m.start(): m.start() + 60].split())
        problems.append(f"{path}:{line}: style= attribute (blocked by style-src, no 'unsafe-inline' or hash for attributes): {snippet!r}...")
    return problems


def check(root: Path) -> list:
    headers_path = root / "_headers"
    if not headers_path.is_file():
        return [f"{headers_path}: missing, can't read the CSP's allowed hashes"]
    allowed = allowed_hashes(headers_path.read_text(encoding="utf-8"))
    problems = []
    for html_path in sorted(root.rglob("*.html")):
        text = html_path.read_text(encoding="utf-8")
        rel = html_path.relative_to(root)
        problems += inline_script_problems(text, rel, allowed)
        problems += style_attribute_problems(text, rel)
    theme_sim_src = root / "assets" / "theme-sim"
    if theme_sim_src.is_dir():
        for js_path in sorted(theme_sim_src.rglob("*.js")):
            problems += style_attribute_problems(js_path.read_text(encoding="utf-8"), js_path.relative_to(root))
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

        # Plant 1: an inline <script>.
        target = work / "themes" / "new" / "index.html"
        text = target.read_text(encoding="utf-8")
        assert "</head>" in text
        target.write_text(text.replace("</head>", '<script type="module">alert(1)</script>\n</head>', 1), encoding="utf-8")
        result = check(work)
        if any("alert(1)" in p for p in result) and not any("style=" in p for p in result):
            print("  caught: a planted inline <script> (its own message, style= rule stayed quiet)")
        else:
            print(f"  MISSED: a planted inline <script>: {result}", file=sys.stderr)
            return 1
        target.write_text(text, encoding="utf-8")  # restore before the next plant

        # Plant 2: a style= attribute in a page.
        text2 = target.read_text(encoding="utf-8")
        assert "<body>" in text2
        target.write_text(text2.replace("<body>", '<body>\n<div style="display:none">x</div>', 1), encoding="utf-8")
        result = check(work)
        if any("style=" in p and "themes/new" in p for p in result) and not any("<script>" in p for p in result):
            print("  caught: a planted style= attribute in a page (its own message, script rule stayed quiet)")
        else:
            print(f"  MISSED: a planted style= attribute in a page: {result}", file=sys.stderr)
            return 1
        target.write_text(text2, encoding="utf-8")

        # Plant 3: a style= attribute in theme-sim source (not a built page).
        js_target = work / "assets" / "theme-sim" / "sample-document.js"
        js_text = js_target.read_text(encoding="utf-8")
        js_target.write_text(js_text.replace("<svg", '<svg style="display:none"', 1), encoding="utf-8")
        result = check(work)
        if any("theme-sim/sample-document.js" in p for p in result):
            print("  caught: a planted style= attribute in theme-sim source")
        else:
            print(f"  MISSED: a planted style= attribute in theme-sim source: {result}", file=sys.stderr)
            return 1
        js_target.write_text(js_text, encoding="utf-8")

    # Prove the restore worked: the real tree (never touched) is still clean.
    restored = check(ROOT / "public")
    if restored:
        print(f"  MISSED: the real tree is no longer clean: {restored}", file=sys.stderr)
        return 1
    print("self-test: 3 plants, 0 missed")
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
        print(f"{len(problems)} problem(s). Move the script to an external file, or the style to a stylesheet -- the CSP allows neither inline.")
        return 1
    n = len(list(Path(args.root).rglob("*.html")))
    print(f"{n} page(s) (plus public/assets/theme-sim/**/*.js) checked: no inline <script> outside the CSP's hashed pair, no style= attribute, 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
