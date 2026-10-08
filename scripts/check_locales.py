#!/usr/bin/env python3
"""Checks that each of de, fr, es and ko is either completely served or not at all (website #162).

Usage:
    python3 scripts/check_locales.py [--root public]
    python3 scripts/check_locales.py --self-test

A planned locale is complete when scripts/copy_<l>.py says `COMPLETE = True` (see scripts/locales.py).
Then, and only then, the built site must have all of this, and each rule fails with its own tag:

- parity:   every en page, its Markdown twin and the 404 page exist under /<l>/ with the same slug;
            and the other way round, a complete locale has been built;
- unlisted: a locale that is NOT complete leaves no trace: no /<l>/ folder, no hreflang for it, no
            link into it, nothing in the sitemap or llms.txt. This is what keeps English (or half a
            translation) from going live under a German URL;
- legal:    content/legal/privacy.<l>.md and support.<l>.md, their rendered HTML and their
            manifest entries exist;
- copy:     no page's <main> is word for word en's (a placeholder), and none has an empty title or h1;
- assets:   the images the locale's pages show exist (the rendered templates, the CLI plan);
- sitemap:  every page's URL is in the sitemap, which is also the list IndexNow falls back to
            (scripts/indexnow_urls.py --sitemap).

hreflang (all enabled locales, reciprocal, x-default = en), <html lang> and the language switch are
check_hreflang.py's; the same-pages-in-every-locale and footer invariants are check_invariants.py's.
--self-test builds a throwaway locale in a scratch copy of the site and plants a break of each rule
(and of those two scripts' rules) in it, and fails if one is missed or caught by the wrong rule.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True

BASE_URL = "https://marsdawn.southern-light.dev"
# Written out again on purpose (see check_hreflang.py): a check that imports the thing it checks can't
# catch a mistake in it.
BASE_PREFIXES = ("zh-hant", "zh-hans", "ja")
PLANNED = ("de", "fr", "es", "ko")
CASES = ("spec", "flowchart", "meeting-notes")


def is_complete(root: Path, locale: str) -> bool:
    path = root / "scripts" / f"copy_{locale}.py"
    return path.is_file() and re.search(r"^COMPLETE\s*=\s*True\b", path.read_text(encoding="utf-8"), re.M) is not None


def en_slugs(public: Path) -> list:
    """The folders (relative, '' for the home page) of every en page."""
    other = set(BASE_PREFIXES) | set(PLANNED)
    return sorted(str(p.parent.relative_to(public)).replace("\\", "/") if p.parent != public else ""
                  for p in public.rglob("index.html") if p.relative_to(public).parts[0] not in other
                  and p.relative_to(public).parts[0] != "assets")


def main_text(html: str) -> str:
    m = re.search(r"<main\b.*?</main>", html, re.S)
    text = re.sub(r"<[^>]+>", " ", m.group(0) if m else html)
    return re.sub(r"\s+", " ", text).strip()


def check(root: Path, public: Path) -> list:
    import indexnow_urls
    problems = []
    slugs = en_slugs(public)
    sitemap = set(indexnow_urls.sitemap_urls(public))
    legal = root / "content" / "legal"
    manifest = (legal / "manifest.json").read_text(encoding="utf-8") if (legal / "manifest.json").is_file() else ""
    for locale in PLANNED:
        folder = public / locale
        built = folder.is_dir()
        if not is_complete(root, locale):
            if built:
                problems.append(f"unlisted: {locale} is not complete (scripts/copy_{locale}.py has no COMPLETE = True) but public/{locale}/ exists")
            for path in sorted(public.rglob("*.html")) + [public / "sitemap.xml", public / "llms.txt", public / "llms-full.txt"]:
                if not path.is_file() or path.relative_to(public).parts[0] == locale:
                    continue
                text = path.read_text(encoding="utf-8")
                if f'hreflang="{locale}"' in text or f'href="/{locale}/' in text or f"{BASE_URL}/{locale}/" in text:
                    problems.append(f"unlisted: {path.relative_to(public)} mentions {locale}, which is not complete")
            continue
        if not built or not any(folder.rglob("index.html")):
            problems.append(f"parity: {locale} is complete (COMPLETE = True in scripts/copy_{locale}.py) but public/{locale}/ has no pages: run scripts/build_pages.py")
            continue
        for slug in slugs:
            url = f"/{slug}/" if slug else "/"
            for name in ("index.html", "index.md"):
                if not (folder / slug / name).is_file():
                    problems.append(f"parity: {locale} is missing {url}{name if name != 'index.html' else ''}, which en has")
            if f"{BASE_URL}/{locale}/{slug}{'/' if slug else ''}" not in sitemap:
                problems.append(f"sitemap: {BASE_URL}/{locale}/{slug}{'/' if slug else ''} is not in the sitemap, so not in IndexNow's list either")
            page, en_page = folder / slug / "index.html", public / slug / "index.html"
            if page.is_file():
                html = page.read_text(encoding="utf-8")
                if main_text(html) == main_text(en_page.read_text(encoding="utf-8")):
                    problems.append(f"copy: /{locale}{url} is English: its <main> is word for word en's")
                for tag in ("title", "h1"):
                    m = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", html, re.S)
                    if m is None or not re.sub(r"<[^>]+>", "", m.group(1)).strip():
                        problems.append(f"copy: /{locale}{url} has no {tag} text")
        for extra in sorted(str(p.parent.relative_to(folder)).replace("\\", "/") for p in folder.rglob("index.html")):
            if extra != "." and extra not in slugs:
                problems.append(f"parity: {locale} has /{extra}/, which en doesn't")
        if not (folder / "404.html").is_file():
            problems.append(f"parity: {locale} is missing 404.html, which en has")
        for slug in ("privacy", "support"):
            for name in (f"{slug}.{locale}.md", f"{slug}.{locale}.rendered.html"):
                if not (legal / name).is_file():
                    problems.append(f"legal: content/legal/{name} is missing")
            if f'"{slug}.{locale}.md"' not in manifest:
                problems.append(f"legal: content/legal/manifest.json has no {slug}.{locale}.md")
        for image in [f"assets/templates/{case}-{locale}.png" for case in CASES] + [f"assets/cli/plan-{locale}.png"]:
            if not (public / image).is_file():
                problems.append(f"assets: public/{image} is missing")
    return problems


def main(argv) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=str(ROOT / "public"))
    parser.add_argument("--repo", default=str(ROOT), help="the checkout whose scripts/ and content/ go with --root")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv[1:])
    if args.self_test:
        import selftest_locales
        return selftest_locales.run()
    problems = check(Path(args.repo), Path(args.root))
    enabled = [l for l in PLANNED if is_complete(Path(args.repo), l)]
    for problem in problems:
        print(f"check_locales: {problem}")
    print(f"locales served: en, zh-hant, zh-hans, ja{''.join(', ' + l for l in enabled)}; {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
