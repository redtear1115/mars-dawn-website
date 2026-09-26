#!/usr/bin/env python3
"""Checks public/themes/v1/index.json, the theme gallery's published index.

Usage:
    python3 scripts/check_theme_index.py [--root public]
    python3 scripts/check_theme_index.py --self-test

`/themes/v1/` is reserved (see README.md) until the theme gallery ships (app repo's
docs/theme-ecosystem-design.md). Nothing under it is committed yet, and that is a valid state:
if `public/themes/v1/` doesn't exist at all, this check passes without looking further — there is
nothing to validate.

Once anything is committed under `public/themes/v1/`, the directory is no longer just reserved:
`index.json` must exist there, must parse as JSON, and must have the shape the design doc fixes
(§5.1): a `schemaVersion` integer, a `generatedAt` timestamp, and a `themes` list whose entries each
carry `id`, `version`, `name`, `summary`, `author`, `minAppVersion` and `files`. This is what issue
#77 asks for: the check used to run only `if -f index.json`, so it validated nothing before the
gallery shipped and could keep validating nothing even after, if the file were ever accidentally
dropped from a commit that otherwise touched the directory. Requiring the directory's presence to
imply the file's presence closes that gap without inventing a requirement the design doc doesn't
already state.

`--self-test` plants one break of each kind in a copy of `public/themes/v1/` (missing directory,
directory present but index.json missing, malformed JSON, and each required field missing) and
fails unless the check's own message reports that specific problem; it also checks that an unbroken
index passes first, so a check that can't pass can't pass as catching everything.
"""
import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_THEME_FIELDS = ("id", "version", "name", "summary", "author", "minAppVersion", "files")

VALID_INDEX = {
    "schemaVersion": 1,
    "generatedAt": "2026-10-01T00:00:00Z",
    "themes": [
        {
            "id": "olympus-dusk",
            "version": "1.0.0",
            "name": {"en": "Olympus Dusk"},
            "summary": {"en": "Cool violet dusk over the volcano"},
            "author": {"name": "Jane Doe", "github": "janedoe"},
            "minAppVersion": "1.1.0",
            "files": {
                "theme.json": {"path": "olympus-dusk/1.0.0/theme.json", "sha256": "…"},
                "theme.css": {"path": "olympus-dusk/1.0.0/theme.css", "sha256": "…"},
            },
            "previews": {
                "light": "olympus-dusk/1.0.0/preview-light.png",
                "dark": "olympus-dusk/1.0.0/preview-dark.png",
            },
        }
    ],
    "revoked": [],
}


def check(root: Path) -> list:
    """Returns a list of problem strings; empty means the check passes."""
    themes_dir = root / "themes" / "v1"
    if not themes_dir.exists():
        # Reserved and not shipped yet (README.md). Nothing to validate.
        return []

    index_path = themes_dir / "index.json"
    if not index_path.is_file():
        return [f"{index_path.relative_to(root.parent)}: missing, but {themes_dir.name}/ exists"]

    try:
        text = index_path.read_text()
    except OSError as error:
        return [f"{index_path}: unreadable ({error})"]

    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        return [f"{index_path}: not valid JSON ({error})"]

    problems = []
    if not isinstance(data, dict):
        return [f"{index_path}: top level must be a JSON object"]

    if not isinstance(data.get("schemaVersion"), int):
        problems.append(f"{index_path}: missing or non-integer schemaVersion")
    if not isinstance(data.get("generatedAt"), str) or not data.get("generatedAt"):
        problems.append(f"{index_path}: missing or empty generatedAt")

    themes = data.get("themes")
    if not isinstance(themes, list):
        problems.append(f"{index_path}: missing or non-list themes")
    else:
        for i, theme in enumerate(themes):
            if not isinstance(theme, dict):
                problems.append(f"{index_path}: themes[{i}] is not an object")
                continue
            for field in REQUIRED_THEME_FIELDS:
                if field not in theme:
                    theme_id = theme.get("id", f"index {i}")
                    problems.append(f"{index_path}: theme {theme_id!r} missing {field!r}")

    if "revoked" in data and not isinstance(data["revoked"], list):
        problems.append(f"{index_path}: revoked must be a list when present")

    return problems


# Each plant: a function that damages a valid fixture tree, and the words that must appear in the
# check's own report of it. Damaging a different rule, or a different file, doesn't count.
def plant_missing_index(themes_dir: Path):
    (themes_dir / "index.json").unlink()


def plant_malformed_json(themes_dir: Path):
    (themes_dir / "index.json").write_text("{not json")


def plant_missing_schema_version(themes_dir: Path):
    data = json.loads((themes_dir / "index.json").read_text())
    del data["schemaVersion"]
    (themes_dir / "index.json").write_text(json.dumps(data))


def plant_missing_theme_field(themes_dir: Path):
    data = json.loads((themes_dir / "index.json").read_text())
    del data["themes"][0]["minAppVersion"]
    (themes_dir / "index.json").write_text(json.dumps(data))


PLANTS = [
    ("missing index.json", plant_missing_index, ["missing"]),
    ("malformed JSON", plant_malformed_json, ["not valid JSON"]),
    ("missing schemaVersion", plant_missing_schema_version, ["schemaVersion"]),
    ("missing theme field", plant_missing_theme_field, ["minAppVersion"]),
]


def self_test() -> int:
    failures = 0

    # No public/themes/v1/ at all: passes, nothing to check.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "public"
        root.mkdir()
        problems = check(root)
        if problems:
            print(f"self-test: an absent themes/v1/ should pass, got {problems}")
            failures += 1

    # A directory present with an extra file but no index.json: must fail, and say so.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "public"
        themes_dir = root / "themes" / "v1"
        themes_dir.mkdir(parents=True)
        (themes_dir / "some-theme").mkdir()
        problems = check(root)
        if not problems or not any("missing" in p for p in problems):
            print(f"self-test: themes/v1/ present without index.json should fail with 'missing', got {problems}")
            failures += 1

    # Unbroken fixture must pass first.
    def make_fixture(tmp: str) -> Path:
        root = Path(tmp) / "public"
        themes_dir = root / "themes" / "v1"
        themes_dir.mkdir(parents=True)
        (themes_dir / "index.json").write_text(json.dumps(VALID_INDEX))
        return root

    with tempfile.TemporaryDirectory() as tmp:
        root = make_fixture(tmp)
        problems = check(root)
        if problems:
            print(f"self-test: the unbroken fixture doesn't pass: {problems}")
            failures += 1

    for what, plant, words in PLANTS:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_fixture(tmp)
            plant(root / "themes" / "v1")
            problems = check(root)
            joined = " ".join(problems)
            if not problems or not all(word in joined for word in words):
                print(f"self-test: planted {what}; wanted {words!r}, got {problems}")
                failures += 1

    print(f"self-test: {1 + 1 + len(PLANTS)} fixtures, {len(PLANTS)} plants, {failures} failures")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="public")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    problems = check(Path(args.root).resolve())
    for problem in problems:
        print(f"::error::{problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
