#!/usr/bin/env python3
"""Checks that every legal page's cached rendering (content/legal/*.rendered.html) still
matches its Markdown source and the kit tag the site pins, without running the kit itself.

Rendering the legal pages needs macOS (the kit is a Swift package) — see
scripts/render_legal.py, which is what actually renders them and records every input's
sha256 in content/legal/manifest.json. This script is the other half, safe to run on Ubuntu
CI: it recomputes those hashes from what's actually committed and compares them to the
manifest, so a .md source edited without a re-render, or a generated file edited by hand,
fails the build instead of quietly shipping stale or hand-tweaked HTML. It also checks the
manifest's kit tag against the one tools/hero-render/Package.swift pins, so a kit bump that
forgot to re-render is caught too.

This is a consistency check (the committed files agree with each other and the manifest),
not a correctness one (that the kit really renders privacy.en.md to that HTML) — that would
need Swift. --self-test plants one break of each kind in memory and fails unless every one
is caught, so a check that can't fail doesn't pass for one that works.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "legal"
PACKAGE_SWIFT = ROOT / "tools" / "hero-render" / "Package.swift"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def pinned_kit_tag() -> str:
    text = PACKAGE_SWIFT.read_text(encoding="utf-8")
    m = re.search(r'exact:\s*"([^"]+)"', text)
    assert m, f"{PACKAGE_SWIFT}: couldn't find the kit's pinned exact version"
    return m[1]


def check(manifest: dict, read_text) -> list:
    """Returns every problem found; read_text(path relative to content/legal, or an
    assets path) lets --self-test substitute a broken fixture without touching disk."""
    problems = []
    pinned = pinned_kit_tag()
    if manifest.get("kit_tag") != pinned:
        problems.append(f"manifest kit_tag is {manifest.get('kit_tag')!r}, "
                         f"tools/hero-render/Package.swift pins {pinned!r}")
    for source_name, entry in manifest.get("pages", {}).items():
        source = read_text(source_name)
        if source is None:
            problems.append(f"{source_name}: missing")
            continue
        if sha256(source) != entry["source_sha256"]:
            problems.append(f"{source_name}: edited since the last render "
                             f"(rerun scripts/render_legal.py)")
        rendered = read_text(entry["rendered"])
        if rendered is None:
            problems.append(f"{entry['rendered']}: missing")
            continue
        if sha256(rendered) != entry["rendered_sha256"]:
            problems.append(f"{entry['rendered']}: doesn't match the manifest "
                             f"(hand-edited, or the manifest is stale)")
    for key, path in (("preview_css_sha256", "../../public/assets/preview.css"),
                       ("themes_css_sha256", "../../public/assets/themes.css")):
        text = read_text(path)
        if text is None:
            problems.append(f"{path}: missing")
        elif sha256(text) != manifest.get(key):
            problems.append(f"{path}: doesn't match the manifest's {key} "
                             f"(hand-edited, or the manifest is stale)")
    return problems


def _real_read_text(name: str):
    path = (CONTENT / name).resolve()
    return path.read_text(encoding="utf-8") if path.is_file() else None


def self_test() -> int:
    manifest = json.loads((CONTENT / "manifest.json").read_text(encoding="utf-8"))
    files = {name: _real_read_text(name) for name in
             list(manifest["pages"]) + [e["rendered"] for e in manifest["pages"].values()] +
             ["../../public/assets/preview.css", "../../public/assets/themes.css"]}
    baseline = check(manifest, files.get)
    if baseline:
        print("self-test: the real tree already fails:", baseline, file=sys.stderr)
        return 1
    plants = [
        ("a stale source", {**files, next(iter(manifest["pages"])): "tampered"}, dict(manifest)),
        ("a hand-edited render", {**files, next(iter(manifest["pages"].values()))["rendered"]: "tampered"}, dict(manifest)),
        ("a hand-edited preview.css", {**files, "../../public/assets/preview.css": "tampered"}, dict(manifest)),
        ("a hand-edited themes.css", {**files, "../../public/assets/themes.css": "tampered"}, dict(manifest)),
        ("a kit tag the pin no longer matches", files, {**manifest, "kit_tag": "0.0.0"}),
        ("a missing rendered file", {**files, next(iter(manifest["pages"].values()))["rendered"]: None}, dict(manifest)),
    ]
    failures = 0
    for label, fake_files, fake_manifest in plants:
        problems = check(fake_manifest, fake_files.get)
        if problems:
            print(f"  caught: {label}")
        else:
            print(f"  MISSED: {label}", file=sys.stderr)
            failures += 1
    print(f"self-test: {len(plants)} plants, {failures} missed")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--self-test", action="store_true",
                         help="plant one break of each kind and confirm every one is caught")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    manifest = json.loads((CONTENT / "manifest.json").read_text(encoding="utf-8"))
    problems = check(manifest, _real_read_text)
    if problems:
        for p in problems:
            print(f"::error::{p}")
        print(f"{len(problems)} problem(s). Rerun scripts/render_legal.py and commit the result.")
        return 1
    n = len(manifest.get("pages", {}))
    print(f"{n} legal page(s) checked against content/legal/manifest.json: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
