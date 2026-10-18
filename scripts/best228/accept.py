#!/usr/bin/env python3
"""Acceptance checks for /best-markdown-viewer-mac/ (website #228) that read the built tree. Not part of
CI; the PR body quotes their output.

    python3 -I -B scripts/best228/accept.py a2 [PUBLIC]   # every slot string is in its locale's built page
    python3 -I -B scripts/best228/accept.py a3 [PUBLIC]   # anchors: 8 + 8 + 8 ids, once each, same set in all locales
    python3 -I -B scripts/best228/accept.py a7 [BASE]     # git diff scope against BASE (default origin/main)

Exit 0 green, 1 red (every problem is printed).
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SLUG = "best-markdown-viewer-mac"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]


def page(public: Path, locale: str) -> Path:
    return public / (SLUG if locale == "en" else f"{locale}/{SLUG}") / "index.html"


def a2(public: Path) -> list:
    slots = json.loads((HERE / "slots.json").read_text(encoding="utf-8"))["slots"]
    problems, cache = [], {}
    for s in slots:
        text = cache.setdefault(s["locale"], page(public, s["locale"]).read_text(encoding="utf-8"))
        if s["html"]:
            ok = s["text"] in text
        else:
            ok = html.escape(s["text"], quote=True) in text or html.escape(s["text"], quote=False) in text
        if not ok:
            problems.append(f'{s["locale"]} {s["field"]} ({s["source"]}): {s["text"][:70]!r} is not in the built page')
    print(f"a2: {len(slots)} slots over {len(cache)} locales")
    return problems


def a3(public: Path) -> list:
    data = json.loads((HERE / "slots.json").read_text(encoding="utf-8"))
    problems, sets = [], {}
    for locale in LOCALES:
        text = page(public, locale).read_text(encoding="utf-8")
        ids = re.findall(r'\bid="([^"]+)"', text)
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup:
            problems.append(f"{locale}: duplicate ids {dup}")
        apps = [i for i in ids if not i.startswith(("cmp-", "col-")) and i in APPS]
        cmp_ = [i for i in ids if i.startswith("cmp-")]
        col = [i for i in ids if i.startswith("col-")]
        if len(apps) != 8 or len(cmp_) != 8 or len(col) != 8:
            problems.append(f"{locale}: {len(apps)} app ids, {len(cmp_)} cmp- ids, {len(col)} col- ids (want 8 each)")
        sets[locale] = set(ids)
        print(f"a3: {locale}: {len(apps)} app, {len(cmp_)} cmp-, {len(col)} col-, {len(ids)} ids in all")
    for locale in LOCALES[1:]:
        if sets[locale] != sets["en"]:
            problems.append(f"{locale}: id set differs from en: {sorted(sets[locale] ^ sets['en'])}")
    return problems


APPS = ["macdown-3000", "marked", "markedit", "marsdawn", "obsidian", "qlmarkdown", "typora", "vs-code"]


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def a7(base: str) -> list:
    problems = []
    names = {}
    for line in git("diff", "--numstat", base, "--", ".").splitlines():
        add, dele, path = line.split("\t")
        names[path] = (add, dele)
    status = git("status", "--porcelain", "-uall").splitlines()
    for line in status:
        if line.startswith("??"):
            names.setdefault(line[3:].rstrip("/"), ("new", "0"))
    fixed = {"scripts/build_pages.py", "scripts/check_invariants.py", "scripts/selftest_locales.py", "public/assets/site.css",
             "public/sitemap.xml", "public/llms.txt", "public/llms-full.txt"}
    counts = {"best": 0, "vs": 0, "twin": 0, "src": 0, "fixed": 0}
    for path, (add, dele) in sorted(names.items()):
        if path.startswith("scripts/best228"):
            counts["src"] += 1
        elif path in fixed:
            counts["fixed"] += 1
        elif re.fullmatch(rf"public/(?:[a-z-]+/)?{SLUG}/index\.(?:html|md)", path):
            counts["best"] += 1
        elif re.fullmatch(r"public/(?:[a-z-]+/)?vs/index\.html", path):
            counts["vs"] += 1
        elif re.fullmatch(r"public/(?:[a-z-]+/)?vs/index\.md", path):
            counts["vs"] += 1
            if (add, dele) != ("2", "0"):
                problems.append(f"{path}: +{add} -{dele}, want +2 -0 (hub link and More entry)")
        elif path.endswith(".md") and path.startswith("public/"):
            counts["twin"] += 1
            if (add, dele) != ("1", "0"):
                problems.append(f"{path}: +{add} -{dele}, want +1 -0 (its More entry)")
        else:
            problems.append(f"out of scope: {path} (+{add} -{dele})")
    print(f"a7: {len(names)} files: {counts}")
    return problems


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    arg = sys.argv[2] if len(sys.argv) > 2 else None
    if mode == "a2":
        problems = a2(Path(arg) if arg else ROOT / "public")
    elif mode == "a3":
        problems = a3(Path(arg) if arg else ROOT / "public")
    elif mode == "a7":
        problems = a7(arg or "origin/main")
    else:
        print(__doc__)
        return 1
    for p in problems:
        print("RED:", p)
    print(f"{mode}: {'GREEN' if not problems else 'RED, ' + str(len(problems)) + ' problems'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
