#!/usr/bin/env python3
r"""Checks public/themes/v1/index.json, the theme gallery's published index.

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
    string and a `sha256` string of exactly 64 lowercase hex characters (a sha256 digest's fixed
    encoded length, not an extra rule).
  - `previews`: an object with `light` and `dark` string paths (the app reads
    `preview-light.png`/`preview-dark.png`; §5.1's URL list).
  - Every `path` (in `files.*` and `previews.*`) must resolve under `/themes/v1/` and nowhere else
    (§5.1: "Paths from the index are resolved against [the base URL], and anything outside that
    prefix is rejected"). This used to be a denylist (reject `..`, reject a scheme, reject `//`,
    ...), and round 2 of review found real gaps in it: the `://` scheme test missed single-colon
    schemes (`c:`, `javascript:`), and the `..` test missed the percent-encoded form (`%2e%2e`).
    `path_is_safe` below is an **allowlist** instead: every path must fully match
    `^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$` — lowercase letters, digits, `.`, `_`, `-`
    within a segment, segments separated by a single `/`, every segment starting with a letter or
    digit. Nothing needs decoding, because nothing outside that character class can pass: no `%`
    (so no percent-encoding of anything, decoded or not), no `?`, `#`, `:` (so no scheme and no
    query/fragment for a resolver to reinterpret), no `\`, no uppercase, no empty segment (`//` or a
    leading/trailing `/`), and no segment starting with `.` (which rules out `.` and `..` segments
    the same way, since their first character isn't `[a-z0-9]`). Checked against every path shape
    §5.1 actually fixes (`olympus-dusk/1.0.0/theme.json`, `.../theme.css`, `.../preview-light.png`,
    `.../preview-dark.png`, and `id` from §4.2's own `^[a-z0-9]+(-[a-z0-9]+)*$`): all lowercase,
    hyphen- and dot-separated, nothing this pattern would reject, so no character class widening was
    needed.
- `revoked`, when present: a list; each entry an object with `id`, `reason`, `revokedAt` as
  non-empty strings (§5.1's example; §5.3 never adds more fields).

This is what issue #77 asks for: the check used to run only `if -f index.json`, so it validated
nothing before the gallery shipped and could keep validating nothing even after, if the file were
ever accidentally dropped, or its shape drifted, without the change being flagged.

`--self-test` plants one break per condition in `RULES` below, in a copy of a valid fixture, and
requires the check's own report of that break to be **exactly one problem**, carrying that
condition's own words — not just any problem, and not that problem plus others, so a plant can't be
credited to the wrong rule or hide a second broken rule behind it. It also checks that an unbroken
index, and an absent `public/themes/v1/`, both pass first, so a check that can't pass can't pass as
catching everything. One condition has no dedicated plant, documented at its `RULES` entry instead:
an unreadable (as opposed to merely malformed or absent) `index.json` isn't something a plant can
portably arrange (permissions differ by OS and by whether CI runs as root).

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

# Allowlist: see the module docstring for why this replaced a denylist, and for the check against
# every path shape §5.1 and §4.2 actually fix.
PATH_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$")

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
    return isinstance(value, str) and bool(PATH_RE.fullmatch(value))


def check_path(problems, where, value):
    if not isinstance(value, str):
        problems.append(f"{where}: must be a string")
    elif not PATH_RE.fullmatch(value):
        problems.append(f"{where}: must match {PATH_RE.pattern}")


def check_file_entry(problems, where, entry, kind):
    if not isinstance(entry, dict):
        problems.append(f"{where}: files[{kind!r}] must be an object")
        return
    check_path(problems, f"{where}: files[{kind!r}].path", entry.get("path"))
    sha = entry.get("sha256")
    if not isinstance(sha, str):
        problems.append(f"{where}: files[{kind!r}].sha256 must be a string")
    elif len(sha) != 64:
        problems.append(f"{where}: files[{kind!r}].sha256 must be exactly 64 characters")
    elif not re.fullmatch(r"[0-9a-f]{64}", sha):
        problems.append(f"{where}: files[{kind!r}].sha256 must be lowercase hex only")


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
        check_path(problems, f"{where}: previews.light", previews.get("light"))
        check_path(problems, f"{where}: previews.dark", previews.get("dark"))


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
        # Not covered by --self-test: see the module docstring.
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


# Each rule: a short name, a mutator that damages exactly one condition in an otherwise-valid
# fixture, and the word(s) that must appear in the check's single resulting problem. `self_test`
# requires len(problems) == 1 for every one of these: a plant that also breaks a second condition,
# or that a second, unrelated bug also breaks, both fail loudly instead of passing quietly.
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


def rule_theme_files_missing_theme_json(root):
    data = read_index(root)
    del data["themes"][0]["files"]["theme.json"]
    write_index(root, data)


def rule_theme_files_missing_theme_css(root):
    data = read_index(root)
    del data["themes"][0]["files"]["theme.css"]
    write_index(root, data)


def rule_theme_file_entry_not_object(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"] = "nope"
    write_index(root, data)


def rule_theme_file_sha256_not_string(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["sha256"] = 12345
    write_index(root, data)


def rule_theme_file_sha256_wrong_length(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["sha256"] = "a" * 63
    write_index(root, data)


def rule_theme_file_sha256_uppercase(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["sha256"] = "A" * 64
    write_index(root, data)


def rule_theme_previews_missing(root):
    data = read_index(root)
    del data["themes"][0]["previews"]
    write_index(root, data)


def rule_theme_previews_missing_light(root):
    data = read_index(root)
    del data["themes"][0]["previews"]["light"]
    write_index(root, data)


def rule_theme_previews_missing_dark(root):
    data = read_index(root)
    del data["themes"][0]["previews"]["dark"]
    write_index(root, data)


def rule_theme_preview_dark_unsafe(root):
    data = read_index(root)
    data["themes"][0]["previews"]["dark"] = "a//b.png"
    write_index(root, data)


def rule_revoked_not_list(root):
    data = read_index(root)
    data["revoked"] = "nope"
    write_index(root, data)


def rule_revoked_entry_not_object(root):
    data = read_index(root)
    data["revoked"][0] = "nope"
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


# path_is_safe's own conditions. With an allowlist there are really only two: "not a string" and
# "doesn't match the pattern" — but the pattern is exercised with one plant per way of failing it
# (upper case, each disallowed character, an empty segment, a leading-dot segment, and verify2's own
# round-2/round-3 escape attempts), on the file-entry path (theme.json AND theme.css, since round 3
# only ever exercised theme.json) and on both preview paths (light AND dark, since round 3 only ever
# exercised dark).
def rule_path_not_string(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = 12345
    write_index(root, data)


def rule_path_uppercase(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "Olympus-Dusk/theme.json"
    write_index(root, data)


def rule_path_percent(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a%2ejson"
    write_index(root, data)


def rule_path_question_mark(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a?x=1"
    write_index(root, data)


def rule_path_hash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a#frag"
    write_index(root, data)


def rule_path_colon(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a:b.json"
    write_index(root, data)


def rule_path_backslash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a\\b.json"
    write_index(root, data)


def rule_path_leading_slash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "/a.json"
    write_index(root, data)


def rule_path_double_slash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a//b.json"
    write_index(root, data)


def rule_path_single_dot_segment(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a/./b.json"
    write_index(root, data)


def rule_path_double_dot_segment(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a/../b.json"
    write_index(root, data)


def rule_path_del_char(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "a\x7fb.json"
    write_index(root, data)


def rule_path_theme_css_unsafe(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.css"]["path"] = "/a.css"
    write_index(root, data)


def rule_path_preview_light_unsafe(root):
    data = read_index(root)
    data["themes"][0]["previews"]["light"] = "/a.png"
    write_index(root, data)


def rule_path_preview_dark_unsafe(root):
    data = read_index(root)
    data["themes"][0]["previews"]["dark"] = "/a.png"
    write_index(root, data)


# verify2's own escape attempts (round 2 and round 3), replayed as plants directly.
def rule_path_escape_encoded_dot_hash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "%2e%2e#"
    write_index(root, data)


def rule_path_escape_dotdot_query(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "..?x"
    write_index(root, data)


def rule_path_escape_mixed_encoded_dot_hash(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "%2e.#"
    write_index(root, data)


def rule_path_escape_drive_letter(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "c:/x"
    write_index(root, data)


def rule_path_escape_javascript(root):
    data = read_index(root)
    data["themes"][0]["files"]["theme.json"]["path"] = "javascript:alert(1)"
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
    ("theme.files missing 'theme.json' key", rule_theme_files_missing_theme_json, ["files must be an object with 'theme.json' and 'theme.css'"]),
    ("theme.files missing 'theme.css' key", rule_theme_files_missing_theme_css, ["files must be an object with 'theme.json' and 'theme.css'"]),
    ("theme.files entry not an object", rule_theme_file_entry_not_object, ["files['theme.json'] must be an object"]),
    ("theme.files.sha256 not a string", rule_theme_file_sha256_not_string, ["sha256 must be a string"]),
    ("theme.files.sha256 wrong length", rule_theme_file_sha256_wrong_length, ["sha256 must be exactly 64 characters"]),
    ("theme.files.sha256 uppercase", rule_theme_file_sha256_uppercase, ["sha256 must be lowercase hex only"]),
    ("theme.previews missing", rule_theme_previews_missing, ["previews must be an object"]),
    ("theme.previews missing 'light' key", rule_theme_previews_missing_light, ["previews must be an object with 'light' and 'dark'"]),
    ("theme.previews missing 'dark' key", rule_theme_previews_missing_dark, ["previews must be an object with 'light' and 'dark'"]),
    ("theme.previews.dark unsafe path", rule_theme_preview_dark_unsafe, ["previews.dark", "must match"]),
    ("revoked not a list", rule_revoked_not_list, ["revoked must be a list"]),
    ("revoked entry not an object", rule_revoked_entry_not_object, ["revoked[0]", "is not an object"]),
    ("revoked[].id missing", rule_revoked_entry_id, ["revoked[0]", "id must be a non-empty string"]),
    ("revoked[].reason missing", rule_revoked_entry_reason, ["revoked[0]", "reason must be a non-empty string"]),
    ("revoked[].revokedAt missing", rule_revoked_entry_revoked_at, ["revoked[0]", "revokedAt must be a non-empty string"]),
    ("path: not a string", rule_path_not_string, ["path", "must be a string"]),
    ("path: uppercase", rule_path_uppercase, ["path", "must match"]),
    ("path: percent sign", rule_path_percent, ["path", "must match"]),
    ("path: question mark", rule_path_question_mark, ["path", "must match"]),
    ("path: hash", rule_path_hash, ["path", "must match"]),
    ("path: colon", rule_path_colon, ["path", "must match"]),
    ("path: backslash", rule_path_backslash, ["path", "must match"]),
    ("path: leading slash (empty segment)", rule_path_leading_slash, ["path", "must match"]),
    ("path: double slash (empty segment)", rule_path_double_slash, ["path", "must match"]),
    ("path: single '.' segment", rule_path_single_dot_segment, ["path", "must match"]),
    ("path: '..' segment", rule_path_double_dot_segment, ["path", "must match"]),
    ("path: DEL (0x7F) character", rule_path_del_char, ["path", "must match"]),
    ("path: theme.css file entry", rule_path_theme_css_unsafe, ["files['theme.css'].path", "must match"]),
    ("path: previews.light", rule_path_preview_light_unsafe, ["previews.light", "must match"]),
    ("path: previews.dark (direct)", rule_path_preview_dark_unsafe, ["previews.dark", "must match"]),
    ("path: verify2 escape '%2e%2e#'", rule_path_escape_encoded_dot_hash, ["path", "must match"]),
    ("path: verify2 escape '..?x'", rule_path_escape_dotdot_query, ["path", "must match"]),
    ("path: verify2 escape '%2e.#'", rule_path_escape_mixed_encoded_dot_hash, ["path", "must match"]),
    ("path: verify2 escape 'c:/x'", rule_path_escape_drive_letter, ["path", "must match"]),
    ("path: verify2 escape 'javascript:alert(1)'", rule_path_escape_javascript, ["path", "must match"]),
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
            if len(problems) != 1:
                print(f"self-test: planted {name!r}; wanted exactly 1 problem, got {problems}")
                failures += 1
                continue
            if not all(word in problems[0] for word in words):
                print(f"self-test: planted {name!r}; wanted {words!r} in the single problem, got {problems[0]!r}")
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
