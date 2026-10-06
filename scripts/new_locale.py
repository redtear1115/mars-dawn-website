#!/usr/bin/env python3
"""Writes, or checks, the skeleton of a planned locale's copy module (website #162).

Usage:
    python3 scripts/new_locale.py de            write scripts/copy_de.py: every key, every value empty
    python3 scripts/new_locale.py --check       every scripts/copy_<l>.py (de, fr, es, ko) that exists
                                                has exactly en's structure (values may be empty)

The skeleton is the shape build_pages.py holds a complete locale to (en's: same keys, same list
lengths, no empty string where en has words), with `COMPLETE = False`. Fill the values, translated
from en, then set `COMPLETE = True`: that, and nothing else, makes the build serve the locale.
It refuses to overwrite a module that exists, so a filled-in one is never lost.

--check runs in CI. It fails when en gains a page, table or label that a copy module doesn't have
yet (for instance when the theme gallery pages arrive from release-1.0.4), so a locale can't be
switched on, or fall behind, without its module saying so.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import build_pages  # noqa: E402
import locales  # noqa: E402

HEADER = '''"""{name} copy for the MarsDawn site: a skeleton, every value empty (website #162).

build(k) returns what copy_ja.py's does, plus "tables": the tables zh-Hans and ja keep in
build_pages.py (see build_pages.locale_tables). Translate every value from the en copy in
build_pages.py, keep every key and every list's length, and keep what is code, a command, a URL or
a placeholder ({{langs}}, {{root}}, {{mcp}}, {{a}}, {{u}}, {{b}}, {{file}}) as it is in en.
Structure is checked by `python3 scripts/new_locale.py --check`; the build also refuses a locale
that says COMPLETE = True with a key missing or a string empty, and says which.

The privacy and support pages are rendered from content/legal/<slug>.{locale}.md
(scripts/render_legal.py, on a Mac): their "body" here is k.render_legal_body(slug, "{locale}"), their
title and description are written here. Also needed before COMPLETE: the hero window snapshot
(scripts/sync_hero_sources.py), and public/assets/templates/<case>-{locale}.png and
public/assets/cli/plan-{locale}.png.
"""

# Set to True only when everything below is translated. Until then {locale} is not built, linked,
# in a sitemap, or anywhere else on the site.
COMPLETE = False


def build(k) -> dict:
    return '''


def blank(value):
    if isinstance(value, dict):
        return {key: blank(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [blank(item) for item in value]
    if isinstance(value, str):
        return ""
    return value


def literal(value, indent: int) -> str:
    """Python source for value: a table or a long list one item per line, a short list on one line."""
    pad = "    " * (indent + 1)
    if isinstance(value, dict):
        if not value:
            return "{}"
        return "{\n" + "".join(f"{pad}{key!r}: {literal(item, indent + 1)},\n" for key, item in value.items()) + "    " * indent + "}"
    if isinstance(value, list):
        one_line = "[" + ", ".join(literal(item, indent) for item in value) + "]"
        if all(isinstance(item, str) for item in value) and len(one_line) < 90:
            return one_line
        return "[\n" + "".join(f"{pad}{literal(item, indent + 1)},\n" for item in value) + "    " * indent + "]"
    return repr(value)


def skeleton(locale: str) -> str:
    name = {"de": "German", "fr": "French", "es": "Spanish", "ko": "Korean"}[locale]
    return HEADER.format(name=name, locale=locale) + literal(blank(build_pages.en_reference()), 1) + "\n"


def check() -> int:
    ref = build_pages.en_reference()
    failed = 0
    for locale in locales.PLANNED:
        path = Path(__file__).resolve().parent / (locales.module_name(locale) + ".py")
        if not path.is_file():
            print(f"{path.name}: not started (fine: {locale} is not built)")
            continue
        module = __import__(locales.module_name(locale))
        problems = build_pages.shape_problems(ref, module.build(build_pages._make_k(locale)), allow_empty=True)
        for problem in problems:
            print(f"{path.name}: {problem}")
        print(f"{path.name}: {len(problems)} structure problems")
        failed += bool(problems)
    return 1 if failed else 0


def main(argv) -> int:
    if argv[1:] == ["--check"]:
        return check()
    if len(argv) != 2 or argv[1] not in locales.PLANNED:
        print(__doc__, file=sys.stderr)
        return 2
    path = Path(__file__).resolve().parent / (locales.module_name(argv[1]) + ".py")
    if path.exists():
        print(f"{path} exists; not overwriting it", file=sys.stderr)
        return 1
    path.write_text(skeleton(argv[1]), encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
