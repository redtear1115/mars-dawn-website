#!/usr/bin/env python3
"""Checks public/themes/v1/index.json, the theme gallery's published index.

Usage:
    python3 scripts/check_theme_index.py [--root public]
    python3 scripts/check_theme_index.py --self-test

`/themes/v1/` is reserved (see README.md) until the theme gallery ships (app repo's
docs/theme-ecosystem-design.md, read at origin/main c0d4addb9349298a305725f4d5ae97e7d0e48c0b).
Nothing under it is committed yet, and that is a valid state: if `public/themes/v1/` doesn't exist
at all, this check passes without looking further — there is nothing to validate.

Once anything is committed under `public/themes/v1/`, the directory is no longer just reserved:
`index.json` must exist there, must parse as JSON, and must match the shape §5.1 fixes, field for
field, with nothing invented beyond it:

- `schemaVersion`: an integer (a JSON `true`/`false` is not one, even though Python's `bool` is an
  `int` subclass).
- `generatedAt`: a non-empty string.
- `themes`: a list; each entry an object with:
  - `id`, `version`, `minAppVersion`: strings.
  - `name`, `summary`: objects with an `en` string (§4.2: "`en` is required, other languages are
    optional" — written for `theme.json` but the index carries the same localized-map fields).
  - `author`: an object with a `name` string (`github` is shown in the example but §5.1 never says
    it's required, so it isn't checked).
  - `files`: an object with `theme.json` and `theme.css` entries, each an object with a `path`
    string and a `sha256` string of 64 lowercase hex characters (a sha256 digest's fixed encoded
    length, not an extra rule).
  - `previews`: an object with `light` and `dark` string paths (the app reads
    `preview-light.png`/`preview-dark.png`; §5.1's URL list).
  - Every `path` (in `files.*` and `previews.*`) must be a safe relative path: no leading `/`, no
    `://` scheme, no `\`, no `//`, and no `..` segment. §5.1: "The base URL .../themes/v1/ is fixed
    in the app. Paths from the index are resolved against it, and anything outside that prefix is
    rejected" — this is what makes a resolved path stay under that prefix; the check doesn't chase a
    fuller path-safety spec than that sentence states.
- `revoked`, when present: a list; each entry an object with `id`, `reason`, `revokedAt` as
  non-empty strings (§5.1's example; §5.3 never adds more fields).

This is what issue #77 asks for: the check used to run only `if -f index.json`, so it validated
nothing before the gallery shipped and could keep validating nothing even after, if the file were
ever accidentally dropped, or its shape drifted, without the change being flagged.

`--self-test` plants one break per rule above (`RULES` below) in a copy of a valid fixture, and
requires the check's own message for that break to name that rule and no other rule's break to also
report; it also checks that an unbroken index, and an absent `public/themes/v1/`, both pass first,
so a check that can't pass can't pass as catching everything.

**Ship signal (not covered): absence still passes.** If `public/themes/v1/` is deleted outright
after the gallery has shipped, this check still passes (nothing to validate, by the same rule that
lets it pass today). Turning that into a failure needs a ship signal — something in this repo that
says "the gallery has shipped, so index.json is now mandatory" — and nothing here decides gallery
launch the way `AVAILABILITY` (scripts/build_pages.py) decides Mac App Store launch: they are
different, unrelated launches, so reusing `AVAILABILITY` would be wrong, not just unwired. Until a
ship signal exists, treat this line, and the TODO beside the CI step and in README.md, as the
reminder that this must become mandatory once one does.
"""
import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

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
                "theme.json": {
                    "path": "olympus-dusk/1.0.0/theme.json",
                    "sha256": "a" * 64,
                },
                "theme.css": {
                    "path": "olympus-dusk/1.0.0/theme.css",
                    "sha256": "b" * 64,
                },
            },
            "previews": {
                "light": "olympus-dusk/1.0.0/preview-light.png",
                "dark": "olympus-dusk/1.0.0/preview-dark.png",
            },
        }
    ],
    "revoked": [
        {"id": "some-theme", "reason": "malicious-css", "revokedAt": "2026-10-02T08:00:00Z"}
    ],
}


def is_int_not_bool(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_nonempty_str(value) -> bool:
    return isinstance(value, str) and bool(value)


def path_is_safe(value) -> bool:
    """A relative path that, resolved against .../themes/v1/, can't land outside it."""
    if not is_nonempty_str(value):
        return False
    if value.startswith("/"):
        return False
    if "://" in value:
        return False
    if "\\" in value:
        return False
    if "//" in value:
        return False
    if ".." in value.split("/"):
        return False
    return True


def check_file_entry(problems, where, entry, kind):
    if not isinstance(entry, dict):
        problems.append(f"{where}: files[{kind!r}] must be an object")
        return
    if not path_is_safe(entry.get("path")):
        problems.append(f"{where}: files[{kind!r}].path must be a safe relative path under themes/v1/")
    sha = entry.get("sha256")
    if not isinstance(sha, str) or not SHA256_RE.match(sha):
        problems.append(f"{where}: files[{kind!r}].sha256 must be 64 lowercase hex characters")


def check_theme(problems, where, theme):
    if not isinstance(theme, dict):
        problems.append(f"{where}: is not an object")
        return

    if not is_nonempty_str(theme.get("id")):
        problems.append(f"{where}: id must be a non-empty string")
    if not is_nonempty_str(theme.get("version")):
        problems.append(f"{where}: version must be a non-empty string")
    if not is_nonempty_str(theme.get("minAppVersion")):
        problems.append(f"{where}: minAppVersion must be a non-empty string")

    name = theme.get("name")
    if not isinstance(name, dict) or not is_nonempty_str(name.get("en")):
        problems.append(f"{where}: name must be an object with a non-empty 'en' string")

    summary = theme.get("summary")
    if not isinstance(summary, dict) or not is_nonempty_str(summary.get("en")):
        problems.append(f"{where}: summary must be an object with a non-empty 'en' string")

    author = theme.get("author")
    if not isinstance(author, dict) or not is_nonempty_str(author.get("name")):
        problems.append(f"{where}: author must be an object with a non-empty 'name' string")

    files = theme.get("files")
    if not isinstance(files, dict) or "theme.json" not in files or "theme.css" not in files:
        problems.append(f"{where}: files must be an object with 'theme.json' and 'theme.css' entries")
    else:
        check_file_entry(problems, where, files.get("theme.json"), "theme.json")
        check_file_entry(problems, where, files.get("theme.css"), "theme.css")

    previews = theme.get("previews")
    if not isinstance(previews, dict) or "light" not in previews or "dark" not in previews:
        problems.append(f"{where}: previews must be an object with 'light' and 'dark' entries")
    else:
        if not path_is_safe(previews.get("light")):
            problems.append(f"{where}: previews.light must be a safe relative path under themes/v1/")
        if not path_is_safe(previews.get("dark")):
            problems.append(f"{where}: previews.dark must be a safe relative path under themes/v1/")


def check_revoked_entry(problems, where, entry):
    if not isinstance(entry, dict):
        problems.append(f"{where}: is not an object")
        return
    if not is_nonempty_str(entry.get("id")):
        problems.append(f"{where}: id must be a non-empty string")
    if not is_nonempty_str(entry.get("reason")):
        problems.append(f"{where}: reason must be a non-empty string")
    if not is_nonempty_str(entry.get("revokedAt")):
        problems.append(f"{where}: revokedAt must be a non-empty string")


def check(root: Path) -> list:
    """Returns a list of problem strings; empty means the check passes."""
    themes_dir = root / "themes" / "v1"
    if not themes_dir.exists():
        # Reserved and not shipped yet (README.md). Nothing to validate. See the module
        # docstring's "Ship signal" note: this is also why deleting v1/ after ship still passes.
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

    if not isinstance(data, dict):
        return [f"{index_path}: top level must be a JSON object"]

    problems = []

    if not is_int_not_bool(data.get("schemaVersion")):
        problems.append(f"{index_path}: schemaVersion must be an integer (not a boolean)")

    if not is_nonempty_str(data.get("generatedAt")):
        problems.append(f"{index_path}: generatedAt must be a non-empty string")

    themes = data.get("themes")
    if not isinstance(themes, list):
        problems.append(f"{index_path}: themes must be a list")
    else:
        for i, theme in enumerate(themes):
            theme_id = theme.get("id") if isinstance(theme, dict) else None
            where = f"{index_path}: themes[{i}]" + (f" ({theme_id!r})" if theme_id else "")
            check_theme(problems, where, theme)

    if "revoked" in data:
        revoked = data["revoked"]
        if not isinstance(revoked, list):
            problems.append(f"{index_path}: revoked must be a list when present")
        else:
            for i, entry in enumerate(revoked):
                check_revoked_entry(problems, f"{index_path}: revoked[{i}]", entry)

    return problems


def make_fixture(tmp: str) -> Path:
    root = Path(tmp) / "public"
    themes_dir = root / "themes" / "v1"
    themes_dir.mkdir(parents=True)
    (themes_dir / "index.json").write_text(json.dumps(VALID_INDEX))
    return root


def write_index(root: Path, data) -> None:
    (root / "themes" / "v1" / "index.json").write_text(json.dumps(data))


def read_index(root: Path):
    return json.loads((root / "themes" / "v1" / "index.json").read_text())


# Each rule: a short name, a mutator that damages one fixture field, and the word(s) that must
# appear in the check's own report of that break. `run` gets a fresh copy of VALID_INDEX and the
# fixture root; it plants the break itself (rather than editing files) so the same mutator also
# backs the "sabotage the rule itself" table in the PR, run by hand outside this file.
def rule_missing_index(root):
    (root / "themes" / "v1" / "index.json").unlink()


def rule_malformed_json(root):
    (root / "themes" / "v1" / "index.json").write_text("{not json")


def rule_top_level_not_object(root):
    write_index(root, [1, 2, 3])


def rule_schema_version_bool(root):
    data = read_index(root)
    data["schemaVersion"] = True
    write_index(root, data)


def rule_generated_at_empty(root):
    data = read_index(root)
    data["generatedAt"] = ""
    write_index(root, data)


def rule_themes_not_list(root):
    data = read_index(root)
    data["themes"] = "nope"
    write_index(root, data)


def rule_theme_not_object(root):
    data = read_index(root)
    data["themes"][0] = "nope"
    write_index(root, data)


def rule_theme_id(root):
    data = read_index(root)
    del data["themes"][0]["id"]
    write_index(root, data)


def rule_theme_version(root):
    data = read_index(root)
    data["themes"][0]["version"] = 1
    write_index(root, data)


def rule_theme_min_app_version(root):
    data = read_index(root)
    del data["themes"][0]["minAppVersion"]
    write_index(root, data)


def rule_theme_name(root):
    data = read_index(root)
    data["themes"][0]["name"] = "Olympus Dusk"
    write_index(root, data)


def rule_theme_summary(root):
    data = read_index(root)
    data["themes"][0]["summary"] = {}
    write_index(root, data)


def rule_theme_author(root):
    data = read_index(root)
    data["themes"][0]["author"] = "Jane Doe"
    write_index(root, data)


def rule_theme_files_missing(root):
    data = read_index(root)
    del data["themes"][0]["files"]["theme.css"]
    write_index(root, data)


def rule_theme_file_path_unsafe(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "../../etc/passwd"
    write_index(root, data)


def rule_theme_file_sha256(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["sha256"] = "not-hex"
    write_index(root, data)


def rule_theme_previews_missing(root):
    data = read_index(root)
    del data["themes"][0]["previews"]
    write_index(root, data)


def rule_theme_preview_path_unsafe(root):
    data = read_index(root)
    data["themes"][0]["previews"]["light"] = "/themes/v1/../escaped.png"
    write_index(root, data)


def rule_revoked_not_list(root):
    data = read_index(root)
    data["revoked"] = "nope"
    write_index(root, data)


def rule_revoked_entry_id(root):
    data = read_index(root)
    del data["revoked"][0]["id"]
    write_index(root, data)


def rule_revoked_entry_reason(root):
    data = read_index(root)
    del data["revoked"][0]["reason"]
    write_index(root, data)


def rule_revoked_entry_revoked_at(root):
    data = read_index(root)
    del data["revoked"][0]["revokedAt"]
    write_index(root, data)


RULES = [
    ("missing index.json", rule_missing_index, ["missing"]),
    ("malformed JSON", rule_malformed_json, ["not valid JSON"]),
    ("top level not an object", rule_top_level_not_object, ["top level must be a JSON object"]),
    ("schemaVersion is a boolean", rule_schema_version_bool, ["schemaVersion must be an integer"]),
    ("generatedAt empty", rule_generated_at_empty, ["generatedAt must be a non-empty string"]),
    ("themes not a list", rule_themes_not_list, ["themes must be a list"]),
    ("theme entry not an object", rule_theme_not_object, ["is not an object"]),
    ("theme.id missing", rule_theme_id, ["id must be a non-empty string"]),
    ("theme.version wrong type", rule_theme_version, ["version must be a non-empty string"]),
    ("theme.minAppVersion missing", rule_theme_min_app_version, ["minAppVersion must be a non-empty string"]),
    ("theme.name wrong type", rule_theme_name, ["name must be an object"]),
    ("theme.summary missing 'en'", rule_theme_summary, ["summary must be an object"]),
    ("theme.author wrong type", rule_theme_author, ["author must be an object"]),
    ("theme.files missing theme.css", rule_theme_files_missing, ["files must be an object with 'theme.json' and 'theme.css'"]),
    ("theme.files path traversal", rule_theme_file_path_unsafe, ["path must be a safe relative path"]),
    ("theme.files sha256 not hex", rule_theme_file_sha256, ["sha256 must be 64 lowercase hex characters"]),
    ("theme.previews missing", rule_theme_previews_missing, ["previews must be an object"]),
    ("theme.previews.light escapes v1/", rule_theme_preview_path_unsafe, ["previews.light must be a safe relative path"]),
    ("revoked not a list", rule_revoked_not_list, ["revoked must be a list"]),
    ("revoked[].id missing", rule_revoked_entry_id, ["revoked[0]", "id must be a non-empty string"]),
    ("revoked[].reason missing", rule_revoked_entry_reason, ["revoked[0]", "reason must be a non-empty string"]),
    ("revoked[].revokedAt missing", rule_revoked_entry_revoked_at, ["revoked[0]", "revokedAt must be a non-empty string"]),
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
    with tempfile.TemporaryDirectory() as tmp:
        root = make_fixture(tmp)
        problems = check(root)
        if problems:
            print(f"self-test: the unbroken fixture doesn't pass: {problems}")
            failures += 1

    for name, rule, words in RULES:
        with tempfile.TemporaryDirectory() as tmp:
            root = make_fixture(tmp)
            rule(root)
            problems = check(root)
            joined = " ".join(problems)
            if not problems or not all(word in joined for word in words):
                print(f"self-test: planted {name!r}; wanted {words!r}, got {problems}")
                failures += 1

    total = 3 + len(RULES)
    print(f"self-test: {total} fixtures, {len(RULES)} plants, {failures} failures")
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
