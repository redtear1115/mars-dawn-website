#!/usr/bin/env python3
"""Holds the theme simulator's hand-off link intake to its place in <head> (plan
PLAN-web-theme-tuning W2b).

/themes/new/#theme=<payload> carries a whole theme in the URL fragment. theme-link-head.js takes it
out of the address bar before Google Tag Manager loads, so GTM (and the GA4 tag inside it) never
sees it. That only holds while the script is synchronous and runs first, so on every served
locale's /themes/new/index.html this checks:

  head.missing   the page has exactly one theme-link-head.js tag, and it is the plain, synchronous
                 `<script src="/assets/theme-sim/theme-link-head.js"></script>`
                 (no async, defer or type=module, any of which would let GTM run first);
  head.order     it comes after <meta charset> and before both consent scripts (the Consent Mode
                 default and the GTM loader, consent_head_html() in build_pages.py);

and on every other generated page:

  head.elsewhere no other page loads it (it is for /themes/new/ only).

Usage:
    python3 scripts/check_theme_link_head.py [--root public]
    python3 scripts/check_theme_link_head.py --self-test

--self-test plants one break of each rule in an in-memory copy of the real pages and fails unless
each is reported by its own rule (and the unplanted copy is clean).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import locales  # noqa: E402

TAG = '<script src="/assets/theme-sim/theme-link-head.js"></script>'
ANY_TAG = re.compile(r"<script\b[^>]*theme-link-head\.js[^>]*>", re.I)
META_CHARSET = '<meta charset="utf-8">'
# The first characters of consent_head_html()'s two inline scripts, as build_pages.py renders them.
CONSENT_DEFAULT = "<script>window.dataLayer = window.dataLayer || [];"
GTM_LOADER = "<script>(function(w,d,s,l,i){"


def sim_pages(root: Path) -> list:
    """The /themes/new/index.html of every served locale (en at the root), relative to root."""
    out = []
    for locale in locales.enabled():
        prefix = "" if locale == "en" else f"{locale}/"
        out.append(f"{prefix}themes/new/index.html")
    return out


def problems(pages: dict, sim: list) -> list:
    """`pages` maps a path relative to the site root to its HTML. Returns (rule, path, detail)."""
    found = []
    for rel in sim:
        html = pages.get(rel)
        if html is None:
            found.append(("head.missing", rel, "page not generated"))
            continue
        tags = ANY_TAG.findall(html)
        if len(tags) != 1 or html.count(TAG) != 1:
            found.append(("head.missing", rel, f"expected exactly one plain {TAG}, found {tags}"))
            continue
        at = html.index(TAG)
        meta = html.find(META_CHARSET)
        consent = html.find(CONSENT_DEFAULT)
        gtm = html.find(GTM_LOADER)
        if meta < 0 or consent < 0 or gtm < 0:
            found.append(("head.order", rel, f"can't find <meta charset> ({meta}), the Consent Mode default ({consent}) or the GTM loader ({gtm})"))
        elif not (meta < at < consent and at < gtm):
            found.append(("head.order", rel, f"theme-link-head.js at {at}; <meta charset> at {meta}, Consent Mode default at {consent}, GTM loader at {gtm}"))
    for rel, html in pages.items():
        if rel not in sim and ANY_TAG.search(html):
            found.append(("head.elsewhere", rel, "loads theme-link-head.js but isn't /themes/new/"))
    return found


def load_pages(root: Path) -> dict:
    return {str(p.relative_to(root)): p.read_text(encoding="utf-8") for p in root.rglob("*.html")}


def self_test(root: Path) -> int:
    pages = load_pages(root)
    sim = sim_pages(root)
    failures = 0
    base = problems(pages, sim)
    if base:
        print(f"FAIL  self-test: the unplanted pages already have problems: {base}")
        return 1
    print(f"  ok  self-test: the unplanted pages are clean ({len(sim)} simulator pages, {len(pages)} pages)")
    en = sim[0]
    other = next(rel for rel in sim if rel != en)
    html = pages[en]
    consent_block = html[html.index(CONSENT_DEFAULT):html.index("</script>", html.index(GTM_LOADER)) + len("</script>")]
    plants = [
        ("moved after the consent scripts", en, "head.order",
         html.replace(TAG + "\n", "", 1).replace(consent_block, consent_block + "\n" + TAG, 1)),
        ("moved between the two consent scripts", en, "head.order",
         html.replace(TAG + "\n", "", 1).replace(GTM_LOADER, TAG + "\n" + GTM_LOADER, 1)),
        ("moved before <meta charset>", en, "head.order",
         html.replace(TAG + "\n", "", 1).replace(META_CHARSET, TAG + "\n" + META_CHARSET, 1)),
        ("removed", other, "head.missing", pages[other].replace(TAG + "\n", "", 1)),
        ("made defer", en, "head.missing", html.replace(TAG, TAG.replace("></script>", " defer></script>"), 1)),
        ("made async", en, "head.missing", html.replace(TAG, TAG.replace("<script ", "<script async "), 1)),
        ("made a module", en, "head.missing", html.replace(TAG, TAG.replace("<script ", '<script type="module" '), 1)),
        ("loaded twice", en, "head.missing", html.replace(TAG, TAG + "\n" + TAG, 1)),
        ("added to the gallery page", "themes/gallery/index.html", "head.elsewhere",
         pages["themes/gallery/index.html"].replace(META_CHARSET, META_CHARSET + "\n" + TAG, 1)),
    ]
    for label, rel, rule, planted in plants:
        if planted == pages[rel]:
            print(f"FAIL  self-test plant '{label}': the plant changed nothing")
            failures += 1
            continue
        got = problems({**pages, rel: planted}, sim)
        rules = sorted({g[0] for g in got})
        if rules == [rule] and all(g[1] == rel for g in got):
            print(f"  ok  self-test plant '{label}' ({rel}): caught by {rule}")
        else:
            print(f"FAIL  self-test plant '{label}' ({rel}): expected only {rule}, got {got}")
            failures += 1
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT / "public"))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    if args.self_test:
        failures = self_test(root)
        print("Self-test passed." if failures == 0 else f"Self-test: {failures} failure(s).")
        return 0 if failures == 0 else 1
    sim = sim_pages(root)
    found = problems(load_pages(root), sim)
    for rule, rel, detail in found:
        print(f"::error file=public/{rel}::{rule}: {detail}")
    if found:
        return 1
    print(f"theme-link-head.js is first in <head> on all {len(sim)} /themes/new/ pages, and on no other page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
