#!/usr/bin/env python3
r"""Checks the theme gallery's published tree: public/themes/v1/ against themes/ (#77, #144).

Usage:
    python3 scripts/check_theme_index.py                  # this tree only
    python3 scripts/check_theme_index.py --base <ref>     # plus the rules that compare to a base
    python3 scripts/check_theme_index.py --ci             # in GitHub Actions: base + PR authorship
    python3 scripts/check_theme_index.py --self-test

Design of record: the app repo's docs/theme-ecosystem-design.md §5.1-§5.3 (release/1.0.2 2c03440);
plan-website-104 revision 4, W3. `scripts/build_themes.py` (macOS, runs the kit CLI) writes what
this checks; this runs on Ubuntu CI with the standard library only, so it can't run the kit's
validator: the kit's verdict is taken at build time, and this holds the committed result to it
(sha256 of the exact source bytes) and to every rule that doesn't need the kit.

What lives where:

- `themes/<id>/theme.json` -- the build input, one folder per listed theme, and `themes/revoked.json`
  (a list of {id, reason, revokedAt}; mandatory, `[]` when nothing is revoked).
- `public/themes/v1/index.json` -- the index the app fetches (§5.1).
- `public/themes/v1/<id>/<version>/{theme.json,preview-light.png,preview-dark.png}` -- versioned,
  immutable files.
- `public/themes/v1/published.json` -- the append-only record, {path: sha256}, of every file ever
  published under public/themes/v1/ (paths relative to it, like the index's).

Rules on this tree alone (each has a --self-test plant that must produce exactly one problem, with
that rule's own words):

- index.json exists and has §5.1's shape field for field: schemaVersion an integer (not a bool),
  generatedAt an ISO-8601 UTC time (`YYYY-MM-DDTHH:MM:SSZ`), themes a list of entries with id,
  version, minAppVersion, name{en}, summary{en}, author{name}, **scenarios** (1-2 distinct ids from
  §4.5's closed list), files with a `theme.json` entry {path, sha256} and **no `theme.css`**
  (parameters-only themes, 2026-09-27), previews{light, dark}; revoked a list of {id, reason,
  revokedAt}. Every path matches the allowlist PATH_RE (see path_is_safe).
- themes/ holds only revoked.json and <id>/ folders; each folder holds only theme.json, a regular
  file (not a symlink) of at most 16 KB, parsing as a JSON object without duplicate keys, whose id
  equals its folder name, matches the id grammar and isn't a built-in's, whose version is
  MAJOR.MINOR.PATCH (1-4 ASCII digits each), with name{en}, summary{en}, author{name} and scenarios
  as above. The grammars are the kit's (ThemeGrammar.swift at the pinned commit), re-checked here
  rather than trusted.
- public/themes/v1/ holds only regular files: index.json, published.json, and files published.json
  lists; every listed file exists and its sha256 matches.
- index <-> themes/ is a bijection by id; each entry's version/name/summary/scenarios/author equal
  its theme.json's; its paths are the canonical `<id>/<version>/...`; its theme.json sha256 equals
  both themes/<id>/theme.json's and published.json's; both previews are listed, start with the PNG
  signature, are PREVIEW_WIDTH pixels wide, 1-8000 tall, at most 500 KB.
- index.revoked equals themes/revoked.json (sorted by id), and no revoked id is still in themes/ or
  the index.

Rules against the base branch (`--ci` fetches it explicitly, by SHA, and **fails closed** if it
can't be read):

- published.json only gains entries: every base entry is still there with the same sha256 (and, by
  the rule above, the file itself is unchanged).
- Ids are never reused: an id that has files in the base published.json but isn't in the base
  index was delisted or revoked; seeing it in themes/ again fails.
- A theme already in the base index keeps its author.github (case-insensitively) unless the PR has
  the label `theme-author-change`.

PR authorship classes (`--ci` on a pull_request event; by `pull_request.user.id`, read from the
event payload file, never from text spliced into `run:`):

- **bot** (github-actions[bot], id 41898282): at most one themes/<id>/ folder, no
  themes/revoked.json, and under public/themes/v1/ only that id's folder, index.json and
  published.json.
- **maintainer** (id in $THEME_MAINTAINER_IDS, a repo variable; comma-separated; default 16503101):
  any number of themes, delisting, revocation and the emergency index edit (§5.3) -- all still
  subject to every rule above.
- **anyone else**: may not change public/themes/v1/**, themes/revoked.json, or more than one
  themes/<id>/ folder. A single-theme data PR from anyone else still fails (the index doesn't list
  it); it goes through W2's theme-from-pr instead.

The emergency path (§5.3), by hand without a Mac: remove themes/<id>/, drop its index entry and,
to revoke, add the same {id, reason, revokedAt} to themes/revoked.json and index.revoked. Published
files and their published.json entries stay. That tree passes; the self-test's revocation plant is
exactly this edit.

Limits (for review, not hidden): a pull_request check runs the PR's own copy of this script and
workflow, so a PR can weaken the check it is judged by -- the diff review is the gate for changes
to scripts/ and .github/. The kit's validity verdict can't be recomputed here (no kit on Linux).

--self-test also covers the base reader: a real temporary git repository read back through the
same `git ls-tree`/`git cat-file` path CI uses, and an unknown revision failing closed.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

THEMES_REL = "themes"
V1_REL = "public/themes/v1"
REVOKED_REL = "themes/revoked.json"
INDEX_REL = V1_REL + "/index.json"
PUBLISHED_REL = V1_REL + "/published.json"

# Allowlist for every path the index and published.json carry. A denylist (reject `..`, a scheme,
# `//`) had real gaps in #141's review rounds -- single-colon schemes (`c:`, `javascript:`) and
# percent-encoded dots (`%2e%2e`). Only lowercase letters, digits, `.`, `_`, `-` within a segment,
# single `/` between segments, every segment starting with a letter or digit: no `%`, `?`, `#`,
# `:`, `\`, uppercase, empty segment, or `.`/`..` segment can pass, so nothing needs decoding.
PATH_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$")
# The kit's ThemeGrammar at the pinned commit, as ASCII-only patterns used with fullmatch (so no
# `$`-before-newline, and `[0-9]` rather than `\d`, which would accept other scripts' digits).
ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MAX_ID_LENGTH = 32
VERSION_RE = re.compile(r"[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}")
TIME_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
SHA_RE = re.compile(r"[0-9a-f]{64}")
REASON_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

SCENARIOS = ("agent-review", "technical-docs", "formal-output", "notes-sharing")  # design §4.5
RESERVED_IDS = ("dawn", "classic", "modern", "vivid")  # design §4.2: built-in ids are reserved
MAX_THEME_BYTES = 16 * 1024
MAX_PREVIEW_BYTES = 500 * 1024
PREVIEW_WIDTH = 1200
PREVIEW_MAX_HEIGHT = 8000
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
FILE_NAMES = ("theme.json", "preview-light.png", "preview-dark.png")
# The first app version with the gallery (app #293, milestone "1.1.1 theme gallery").
MIN_APP_VERSION = "1.1.1"

BOT_ID = 41898282  # github-actions[bot]
DEFAULT_MAINTAINER_IDS = (16503101,)  # redtear1115; plan-website-104 Needs-you
AUTHOR_CHANGE_LABEL = "theme-author-change"


# --- small predicates -----------------------------------------------------------------------------

def is_int_not_bool(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_nonempty_str(value) -> bool:
    return isinstance(value, str) and bool(value)


def path_is_safe(value) -> bool:
    return isinstance(value, str) and bool(PATH_RE.fullmatch(value))


def is_theme_id(value) -> bool:
    return isinstance(value, str) and len(value) <= MAX_ID_LENGTH and bool(ID_RE.fullmatch(value))


def is_version(value) -> bool:
    return isinstance(value, str) and bool(VERSION_RE.fullmatch(value))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_id(data: bytes) -> str:
    """The id git gives these bytes as a blob, so a tree read from disk and one read from git can
    be compared path by path without reading every base blob."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def strict_json(data: bytes):
    """json.loads that refuses duplicate keys (the kit refuses them too) and non-UTF-8 bytes."""
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError(f"duplicate key {key!r}")
            out[key] = value
        return out
    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs)


def dumps(obj) -> str:
    """The one serialization every generated JSON file here uses (build_themes.py too)."""
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def png_size(data: bytes):
    """(width, height) from a PNG's IHDR, or None if the bytes don't start like a PNG."""
    if len(data) < 24 or not data.startswith(PNG_SIGNATURE) or data[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", data[16:24])


# --- the index entry, shared with build_themes.py -------------------------------------------------

def localized(value: dict) -> dict:
    return {key: value[key] for key in sorted(value)}


def author_of(doc: dict) -> dict:
    author = doc["author"]
    out = {"name": author["name"]}
    if "github" in author:
        out["github"] = author["github"]
    return out


def index_entry(doc: dict, theme_sha: str) -> dict:
    """The index entry build_themes.py writes for a validated theme.json, and the one this check
    requires each entry to equal (§5.1, minus theme.css, plus scenarios)."""
    tid, version = doc["id"], doc["version"]
    base = f"{tid}/{version}/"
    return {
        "id": tid,
        "version": version,
        "name": localized(doc["name"]),
        "summary": localized(doc["summary"]),
        "scenarios": list(doc["scenarios"]),
        "author": author_of(doc),
        "minAppVersion": MIN_APP_VERSION,
        "files": {"theme.json": {"path": base + "theme.json", "sha256": theme_sha}},
        "previews": {"light": base + "preview-light.png", "dark": base + "preview-dark.png"},
    }


def github_of(entry) -> str:
    author = entry.get("author") if isinstance(entry, dict) else None
    github = author.get("github") if isinstance(author, dict) else None
    return github.lower() if isinstance(github, str) else ""


# --- snapshots: the two trees the rules compare ----------------------------------------------------

class BaseUnavailable(RuntimeError):
    pass


class Snapshot:
    """{repo-relative path: (kind, git blob id)} for everything under themes/ and
    public/themes/v1/, plus a reader. kind is "file", "symlink" or "other"."""

    def __init__(self, entries: dict, reader):
        self.entries = entries
        self._reader = reader
        self._cache = {}

    def read(self, path: str):
        if self.entries.get(path, (None,))[0] != "file":
            return None
        if path not in self._cache:
            self._cache[path] = self._reader(path)
        return self._cache[path]

    def paths_under(self, prefix: str):
        prefix = prefix.rstrip("/") + "/"
        return sorted(p for p in self.entries if p.startswith(prefix))

    @classmethod
    def from_dir(cls, repo: Path):
        entries = {}
        for prefix in (THEMES_REL, V1_REL):
            top = repo / prefix
            if top.is_symlink():
                entries[prefix] = ("symlink", git_blob_id(os.readlink(top).encode()))
                continue
            if not top.is_dir():
                continue
            for dirpath, dirnames, filenames in os.walk(top, followlinks=False):
                for name in sorted(dirnames):
                    full = Path(dirpath) / name
                    if full.is_symlink():
                        rel = full.relative_to(repo).as_posix()
                        entries[rel] = ("symlink", git_blob_id(os.readlink(full).encode()))
                for name in filenames:
                    full = Path(dirpath) / name
                    rel = full.relative_to(repo).as_posix()
                    if name == ".DS_Store":  # Finder's, gitignored; never committed
                        continue
                    if full.is_symlink():
                        entries[rel] = ("symlink", git_blob_id(os.readlink(full).encode()))
                    elif full.is_file():
                        entries[rel] = ("file", git_blob_id(full.read_bytes()))
                    else:
                        entries[rel] = ("other", "")
        return cls(entries, lambda p: (repo / p).read_bytes())

    @classmethod
    def from_git(cls, repo: Path, rev: str):
        def git(*args) -> bytes:
            try:
                result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
            except OSError as error:
                raise BaseUnavailable(f"git couldn't run ({error})") from error
            if result.returncode != 0:
                raise BaseUnavailable(f"git {' '.join(args)}: {result.stderr.decode(errors='replace').strip()}")
            return result.stdout

        commit = git("rev-parse", "--verify", "--end-of-options", f"{rev}^{{commit}}").decode().strip()
        entries = {}
        for record in git("ls-tree", "-r", "-z", commit, "--", THEMES_REL, V1_REL).split(b"\0"):
            if not record:
                continue
            meta, _, path = record.partition(b"\t")
            mode, kind, blob = meta.decode().split()
            path = path.decode("utf-8", errors="surrogateescape")
            if kind == "blob" and mode in ("100644", "100755"):
                entries[path] = ("file", blob)
            elif kind == "blob" and mode == "120000":
                entries[path] = ("symlink", blob)
            else:
                entries[path] = ("other", blob)
        return cls(entries, lambda p: git("cat-file", "blob", entries[p][1]))


def fetch_base(repo: Path, rev: str) -> str:
    """Fetches `rev` (a SHA or branch) from origin and returns the fetched commit. Raises
    BaseUnavailable on any failure: the caller fails closed."""
    if not re.fullmatch(r"[0-9a-f]{40}|[A-Za-z0-9._/-]{1,200}", rev) or rev.startswith("-"):
        raise BaseUnavailable(f"refusing to fetch {rev!r}")
    result = subprocess.run(["git", "-C", str(repo), "fetch", "--no-tags", "--depth=1", "origin", rev],
                            capture_output=True)
    if result.returncode != 0:
        raise BaseUnavailable(f"git fetch origin {rev}: {result.stderr.decode(errors='replace').strip()}")
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "FETCH_HEAD^{commit}"],
                          capture_output=True)
    if head.returncode != 0:
        raise BaseUnavailable("FETCH_HEAD isn't a commit after fetching the base")
    return head.stdout.decode().strip()


class PR:
    """What a pull_request event says about who opened it and how it's labelled."""

    def __init__(self, author_id: int, labels=(), maintainers=DEFAULT_MAINTAINER_IDS):
        self.author_id = author_id
        self.labels = set(labels)
        self.maintainers = set(maintainers)

    @property
    def kind(self) -> str:
        if self.author_id == BOT_ID:
            return "bot"
        if self.author_id in self.maintainers:
            return "maintainer"
        return "other"


def parse_maintainers(text) -> tuple:
    text = (text or "").strip()
    if not text:
        return DEFAULT_MAINTAINER_IDS
    ids = []
    for part in text.replace(" ", ",").split(","):
        if not part:
            continue
        if not re.fullmatch(r"[1-9][0-9]{0,11}", part):
            raise ValueError(f"THEME_MAINTAINER_IDS: {part!r} isn't a GitHub numeric user id")
        ids.append(int(part))
    return tuple(ids) or DEFAULT_MAINTAINER_IDS


# --- rules on the index's own shape (#141's, updated for #144) -------------------------------------

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
    elif not SHA_RE.fullmatch(sha):
        problems.append(f"{where}: files[{kind!r}].sha256 must be lowercase hex only")


def scenarios_problem(value):
    if (not isinstance(value, list) or not 1 <= len(value) <= 2
            or not all(isinstance(s, str) and s in SCENARIOS for s in value) or len(set(value)) != len(value)):
        return f"scenarios must be 1-2 distinct ids from the closed list {', '.join(SCENARIOS)}"
    return None


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

    bad = scenarios_problem(theme.get("scenarios"))
    if bad:
        problems.append(f"{where}: {bad}")

    files = theme.get("files")
    if isinstance(files, dict) and "theme.css" in files:
        problems.append(f"{where}: files must not have a 'theme.css' entry (themes are parameters only)")
    elif not isinstance(files, dict) or "theme.json" not in files:
        problems.append(f"{where}: files must be an object with a 'theme.json' entry")
    else:
        check_file_entry(problems, where, files.get("theme.json"), "theme.json")

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


def check_index_shape(data, where: str) -> list:
    problems = []
    if not is_int_not_bool(data.get("schemaVersion")):
        problems.append(f"{where}: schemaVersion must be an integer (not a boolean)")

    generated = data.get("generatedAt")
    if not is_nonempty_str(generated):
        problems.append(f"{where}: generatedAt must be a non-empty string")
    elif not TIME_RE.fullmatch(generated):
        problems.append(f"{where}: generatedAt must be a UTC time like 2026-10-01T00:00:00Z")

    themes = data.get("themes")
    if not isinstance(themes, list):
        problems.append(f"{where}: themes must be a list")
    else:
        for i, theme in enumerate(themes):
            theme_id = theme.get("id") if isinstance(theme, dict) else None
            label = f"{where}: themes[{i}]" + (f" ({theme_id!r})" if theme_id else "")
            check_theme(problems, label, theme)

    if "revoked" in data:
        revoked = data["revoked"]
        if not isinstance(revoked, list):
            problems.append(f"{where}: revoked must be a list when present")
        else:
            for i, entry in enumerate(revoked):
                check_revoked_entry(problems, f"{where}: revoked[{i}]", entry)
    return problems


# --- rules on themes/ (the build input) -------------------------------------------------------------

def check_source_doc(problems, where, folder, doc):
    if not isinstance(doc, dict):
        problems.append(f"{where}: must be a JSON object")
        return False
    before = len(problems)
    tid = doc.get("id")
    if tid != folder:
        problems.append(f"{where}: id {tid!r} doesn't match its folder name {folder!r}")
    if not is_version(doc.get("version")):
        problems.append(f"{where}: version must be MAJOR.MINOR.PATCH with 1-4 ASCII digits each")
    for field in ("name", "summary"):
        value = doc.get(field)
        if not isinstance(value, dict) or not is_nonempty_str(value.get("en")):
            problems.append(f"{where}: {field} must be an object with a non-empty 'en' string")
    author = doc.get("author")
    if not isinstance(author, dict) or not is_nonempty_str(author.get("name")):
        problems.append(f"{where}: author must be an object with a non-empty 'name' string (the index shows it)")
    bad = scenarios_problem(doc.get("scenarios"))
    if bad:
        problems.append(f"{where}: {bad}")
    return len(problems) == before


def check_revoked_source(problems, snap):
    """themes/revoked.json -> sorted list, or None when it's unusable."""
    kind = snap.entries.get(REVOKED_REL, (None,))[0]
    if kind is None:
        problems.append(f"{REVOKED_REL}: missing; it is mandatory ([] when nothing is revoked)")
        return None
    if kind != "file":
        problems.append(f"{REVOKED_REL}: is a symlink or not a regular file")
        return None
    try:
        data = strict_json(snap.read(REVOKED_REL))
    except ValueError as error:
        problems.append(f"{REVOKED_REL}: not valid JSON ({error})")
        return None
    if not isinstance(data, list):
        problems.append(f"{REVOKED_REL}: must be a list of {{id, reason, revokedAt}}")
        return None
    before = len(problems)
    seen = set()
    for i, entry in enumerate(data):
        where = f"{REVOKED_REL}[{i}]"
        if not isinstance(entry, dict) or set(entry) != {"id", "reason", "revokedAt"}:
            problems.append(f"{where}: must be an object with exactly id, reason, revokedAt")
            continue
        if not is_theme_id(entry["id"]):
            problems.append(f"{where}: id must be a theme id")
        elif entry["id"] in seen:
            problems.append(f"{where}: id {entry['id']!r} is revoked twice")
        seen.add(entry["id"])
        if not (isinstance(entry["reason"], str) and len(entry["reason"]) <= 64 and REASON_RE.fullmatch(entry["reason"])):
            problems.append(f"{where}: reason must be a lowercase-hyphenated code like validator-bypass")
        if not (isinstance(entry["revokedAt"], str) and TIME_RE.fullmatch(entry["revokedAt"])):
            problems.append(f"{where}: revokedAt must be a UTC time like 2026-10-02T08:00:00Z")
    if len(problems) != before:
        return None
    return sorted(data, key=lambda e: e["id"])


def check_sources(problems, snap):
    """{id: (bytes, doc)} for every usable themes/<id>/theme.json."""
    sources = {}
    folders = {}
    for path in snap.paths_under(THEMES_REL):
        kind = snap.entries[path][0]
        parts = path.split("/")[1:]
        if kind == "symlink":
            problems.append(f"{path}: is a symlink; themes/ holds regular files only")
            continue
        if kind != "file":
            problems.append(f"{path}: isn't a regular file")
            continue
        if parts == ["revoked.json"]:
            continue
        if len(parts) == 1:
            problems.append(f"{path}: unexpected; themes/ holds only revoked.json and <id>/ folders")
            continue
        folder = parts[0]
        if not is_theme_id(folder):
            problems.append(f"themes/{folder}/: folder name isn't a theme id (^[a-z0-9]+(-[a-z0-9]+)*$, at most 32)")
            continue
        if parts[1:] != ["theme.json"]:
            problems.append(f"{path}: unexpected; a theme folder holds only theme.json")
            continue
        folders[folder] = path
    if snap.entries.get(THEMES_REL, (None,))[0] == "symlink":
        problems.append(f"{THEMES_REL}: is a symlink; themes/ holds regular files only")

    for folder, path in sorted(folders.items()):
        if folder in RESERVED_IDS:
            problems.append(f"{path}: id {folder!r} is a built-in theme's and reserved")
            continue
        data = snap.read(path)
        if len(data) > MAX_THEME_BYTES:
            problems.append(f"{path}: larger than {MAX_THEME_BYTES} bytes")
            continue
        try:
            doc = strict_json(data)
        except ValueError as error:
            problems.append(f"{path}: not valid JSON ({error})")
            continue
        if check_source_doc(problems, path, folder, doc):
            sources[folder] = (data, doc)
    return sources


# --- rules on public/themes/v1/ -------------------------------------------------------------------

def published_key_problem(key):
    if not path_is_safe(key):
        return f"must match {PATH_RE.pattern}"
    parts = key.split("/")
    if len(parts) != 3 or not is_theme_id(parts[0]) or not is_version(parts[1]) or parts[2] not in FILE_NAMES:
        return "must be <id>/<version>/<" + "|".join(FILE_NAMES) + ">"
    return None


def check_published_source(problems, snap):
    kind = snap.entries.get(PUBLISHED_REL, (None,))[0]
    if kind is None:
        problems.append(f"{PUBLISHED_REL}: missing; it is the append-only record of every published file")
        return None
    if kind != "file":
        problems.append(f"{PUBLISHED_REL}: is a symlink or not a regular file")
        return None
    try:
        data = strict_json(snap.read(PUBLISHED_REL))
    except ValueError as error:
        problems.append(f"{PUBLISHED_REL}: not valid JSON ({error})")
        return None
    if not isinstance(data, dict):
        problems.append(f"{PUBLISHED_REL}: must be an object mapping path to sha256")
        return None
    before = len(problems)
    for key, value in data.items():
        bad = published_key_problem(key)
        if bad:
            problems.append(f"{PUBLISHED_REL}: key {key!r} {bad}")
        if not (isinstance(value, str) and SHA_RE.fullmatch(value)):
            problems.append(f"{PUBLISHED_REL}: {key!r} must map to a lowercase sha256")
    return data if len(problems) == before else None


def check_v1_files(problems, snap, published):
    """Every file under public/themes/v1/ is index.json, published.json or listed; every listed
    file exists, unchanged."""
    for path in snap.paths_under(V1_REL):
        kind = snap.entries[path][0]
        rel = path[len(V1_REL) + 1:]
        if kind == "symlink":
            problems.append(f"{path}: is a symlink; public/themes/v1 holds regular files only")
        elif kind != "file":
            problems.append(f"{path}: isn't a regular file")
        elif rel in ("index.json", "published.json"):
            continue
        elif rel not in published:
            problems.append(f"{path}: not listed in published.json; build_themes.py writes both together")
    for rel, digest in sorted(published.items()):
        path = f"{V1_REL}/{rel}"
        data = snap.read(path)
        if data is None:
            if path not in snap.entries:
                problems.append(f"{PUBLISHED_REL} lists {rel}, which doesn't exist")
        elif sha256(data) != digest:
            problems.append(f"{path}: sha256 doesn't match published.json; a published file never changes")


def check_preview(problems, where, snap, rel, published):
    if rel not in published:
        problems.append(f"{where}: preview {rel} isn't listed in published.json")
        return
    data = snap.read(f"{V1_REL}/{rel}")
    if data is None:
        return  # reported by check_v1_files
    size = png_size(data)
    if size is None:
        problems.append(f"{where}: preview {rel} doesn't start with a PNG signature and IHDR")
    elif size[0] != PREVIEW_WIDTH or not 1 <= size[1] <= PREVIEW_MAX_HEIGHT:
        problems.append(f"{where}: preview {rel} is {size[0]}x{size[1]}; it must be {PREVIEW_WIDTH} wide and 1-{PREVIEW_MAX_HEIGHT} tall")
    if len(data) > MAX_PREVIEW_BYTES:
        problems.append(f"{where}: preview {rel} is {len(data)} bytes; at most {MAX_PREVIEW_BYTES}")


def check_cross(problems, snap, index, sources, published, revoked):
    entries = index["themes"]
    listed = {}
    for i, entry in enumerate(entries):
        tid = entry["id"]
        where = f"{INDEX_REL}: themes[{i}] ({tid!r})"
        if tid in listed:
            problems.append(f"{where}: id appears more than once")
            continue
        listed[tid] = entry
        if not is_theme_id(tid) or not is_version(entry["version"]):
            problems.append(f"{where}: id or version doesn't match the kit's grammar")
            continue
        source = sources.get(tid)
        if source is None:
            problems.append(f"{where}: listed, but themes/{tid}/theme.json doesn't exist (delist by removing both)")
            continue
        data, doc = source
        expected = index_entry(doc, sha256(data))
        expected["minAppVersion"] = entry["minAppVersion"]
        differing = [key for key in expected if entry.get(key) != expected[key] and key not in ("files", "previews")]
        extra = sorted(set(entry) - set(expected))
        if differing or extra:
            problems.append(f"{where}: doesn't match themes/{tid}/theme.json in {', '.join(differing + extra)}")
            continue
        if entry["files"] != expected["files"]:
            problems.append(f"{where}: files['theme.json'] must be {expected['files']['theme.json']['path']} "
                            f"with the sha256 of themes/{tid}/theme.json")
            continue
        if entry["previews"] != expected["previews"]:
            problems.append(f"{where}: previews must be {expected['previews']['light']} and {expected['previews']['dark']}")
            continue
        rel = expected["files"]["theme.json"]["path"]
        if published.get(rel) != sha256(data):
            problems.append(f"{where}: {rel} isn't in published.json with themes/{tid}/theme.json's sha256")
        check_preview(problems, where, snap, expected["previews"]["light"], published)
        check_preview(problems, where, snap, expected["previews"]["dark"], published)

    for tid in sorted(set(sources) - set(listed)):
        problems.append(f"themes/{tid}/: not in {INDEX_REL}; run scripts/build_themes.py")

    if index.get("revoked", []) != revoked:
        problems.append(f"{INDEX_REL}: revoked doesn't equal {REVOKED_REL} sorted by id")
    for entry in revoked:
        tid = entry["id"]
        if tid in sources or tid in listed:
            problems.append(f"revoked id {tid!r} is still published: remove themes/{tid}/ and its index entry")


def load_index(snap):
    """(data, problems): the parsed index, or a single problem that stops everything after it."""
    if snap.entries.get(V1_REL, (None,))[0] == "symlink":
        return None, [f"{V1_REL}: is a symlink; public/themes/v1 holds regular files only"]
    if not snap.paths_under(V1_REL):
        return None, [f"{V1_REL}: missing; public/themes/v1/index.json is mandatory"]
    if snap.entries.get(INDEX_REL, (None,))[0] != "file":
        return None, [f"{INDEX_REL}: missing, but v1/ exists"]
    try:
        data = json.loads(snap.read(INDEX_REL).decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as error:
        return None, [f"{INDEX_REL}: not valid JSON ({error})"]
    if not isinstance(data, dict):
        return None, [f"{INDEX_REL}: top level must be a JSON object"]
    return data, []


# --- rules against the base branch and the PR's author ----------------------------------------------

def base_published(base):
    """The base's published.json, {} when the base has never published anything (the bootstrap
    before #144), or BaseUnavailable -- fail closed -- when it should have one and doesn't."""
    kind = base.entries.get(PUBLISHED_REL, (None,))[0]
    if kind is None:
        others = [p for p in base.paths_under(V1_REL) if p != INDEX_REL]
        try:
            index = json.loads(base.read(INDEX_REL) or b"{}")
            themes = index.get("themes", []) if isinstance(index, dict) else ["?"]
        except ValueError:
            themes = ["?"]
        if not others and not themes:
            return {}
        raise BaseUnavailable(f"the base has published themes but no readable {PUBLISHED_REL}")
    try:
        data = strict_json(base.read(PUBLISHED_REL))
    except ValueError as error:
        raise BaseUnavailable(f"the base's {PUBLISHED_REL} isn't valid JSON ({error})") from error
    if not isinstance(data, dict):
        raise BaseUnavailable(f"the base's {PUBLISHED_REL} isn't an object")
    return data


def base_index_themes(base) -> dict:
    try:
        index = json.loads(base.read(INDEX_REL) or b"{}")
    except ValueError as error:
        raise BaseUnavailable(f"the base's {INDEX_REL} isn't valid JSON ({error})") from error
    themes = index.get("themes", []) if isinstance(index, dict) else []
    return {t["id"]: t for t in themes if isinstance(t, dict) and isinstance(t.get("id"), str)}


def check_against_base(problems, base, published, sources, index, labels):
    try:
        old_published = base_published(base)
        old_index = base_index_themes(base)
    except BaseUnavailable as error:
        problems.append(f"base branch: {error}; failing closed")
        return
    if published is not None:
        lost = sorted(k for k, v in old_published.items() if published.get(k) != v)
        if lost:
            problems.append(f"{PUBLISHED_REL}: only gains entries, but these base entries are gone or changed: {', '.join(lost)}")
    ever_published = {k.split("/", 1)[0] for k in old_published}
    for tid in sorted(sources):
        if tid in ever_published and tid not in old_index:
            problems.append(f"themes/{tid}/: id {tid!r} was published before and delisted or revoked; ids are never reused")
    if index is not None and AUTHOR_CHANGE_LABEL not in labels:
        for entry in index.get("themes", []):
            old = old_index.get(entry.get("id"))
            if old is not None and github_of(old) != github_of(entry):
                problems.append(f"{entry['id']!r}: author.github changed from {github_of(old)!r} to {github_of(entry)!r} "
                                f"versus the base branch; that needs the {AUTHOR_CHANGE_LABEL} label")


def changed_paths(head, base) -> list:
    keys = set(head.entries) | set(base.entries)
    return sorted(k for k in keys if head.entries.get(k) != base.entries.get(k))


def check_authorship(problems, pr, changed):
    if pr.kind == "maintainer":
        return
    theme_dirs = sorted({p.split("/")[1] for p in changed
                         if p.startswith(THEMES_REL + "/") and p != REVOKED_REL and p.count("/") >= 2})
    revoked = REVOKED_REL in changed
    v1 = [p for p in changed if p == V1_REL or p.startswith(V1_REL + "/")]
    who = f"PR author (id {pr.author_id})"
    if pr.kind == "bot":
        if len(theme_dirs) > 1:
            problems.append(f"bot PR may change at most one themes/<id>/ folder; this one changes {', '.join(theme_dirs)}")
        if revoked:
            problems.append(f"bot PR may not change {REVOKED_REL}")
        allowed = {INDEX_REL, PUBLISHED_REL}
        own = [f"{V1_REL}/{d}/" for d in theme_dirs[:1]]
        outside = [p for p in v1 if p not in allowed and not any(p.startswith(o) for o in own)]
        if outside:
            problems.append(f"bot PR changes {V1_REL} files outside its theme's folder, index.json and published.json: {', '.join(outside)}")
        return
    if v1:
        problems.append(f"{who} isn't a maintainer and may not change {V1_REL}/: {', '.join(v1)}")
    if revoked:
        problems.append(f"{who} isn't a maintainer and may not change {REVOKED_REL}")
    if len(theme_dirs) > 1:
        problems.append(f"{who} isn't a maintainer and may change at most one themes/<id>/ folder; this PR changes {', '.join(theme_dirs)}")


# --- the check --------------------------------------------------------------------------------------

def check_snapshot(head, base=None, pr=None) -> list:
    """Returns a list of problem strings; empty means the check passes."""
    index, problems = load_index(head)
    if index is None:
        return problems
    index_problems = check_index_shape(index, INDEX_REL)
    problems += index_problems

    source_problems = []
    sources = check_sources(source_problems, head)
    revoked = check_revoked_source(source_problems, head)
    problems += source_problems

    published_problems = []
    published = check_published_source(published_problems, head)
    if published is not None:
        check_v1_files(published_problems, head, published)
    problems += published_problems

    if not index_problems and not source_problems and not published_problems:
        check_cross(problems, head, index, sources, published, revoked)

    if base is not None:
        check_against_base(problems, base, published, sources, None if index_problems else index,
                           pr.labels if pr else set())
        if pr is not None:
            check_authorship(problems, pr, changed_paths(head, base))
    return problems


def check(repo: Path, base=None, pr=None) -> list:
    return check_snapshot(Snapshot.from_dir(repo), base, pr)


# --- self-test fixtures -----------------------------------------------------------------------------

def make_png(width=PREVIEW_WIDTH, height=2, pad=0) -> bytes:
    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)
    raw = b"".join(b"\0" + b"\x80" * width for _ in range(height))
    png = (PNG_SIGNATURE + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))
    return png + b"\0" * pad


def fixture_theme(tid, version="1.0.0", github="janedoe", scenarios=("agent-review",)) -> dict:
    return {
        "schemaVersion": 1, "id": tid, "version": version,
        "name": {"en": "Olympus Dusk", "zh-Hant": "奧林帕斯暮色"},
        "summary": {"en": "Cool violet dusk over the volcano"},
        "fontDesign": "sans", "scenarios": list(scenarios),
        "author": {"name": "Jane Doe", "github": github}, "license": "Apache-2.0",
        "light": {"background": "#FFFDFB"}, "dark": {"background": "#1C1A1F"},
    }


def write_file(repo: Path, rel: str, data) -> None:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))


def write_tree(repo: Path, listed=("olympus-dusk",), delisted=(), revoked=()) -> None:
    """A consistent tree, as build_themes.py would leave it: `listed` themes in themes/ and the
    index, `delisted` ones published earlier (files + published.json) but in neither, `revoked`
    ids in both revoked lists."""
    published, entries = {}, []
    for tid in list(listed) + list(delisted):
        doc = fixture_theme(tid)
        data = dumps(doc).encode()
        base = f"{doc['id']}/{doc['version']}/"
        for name, body in (("theme.json", data), ("preview-light.png", make_png()), ("preview-dark.png", make_png(height=3))):
            write_file(repo, f"{V1_REL}/{base}{name}", body)
            published[base + name] = sha256(body)
        if tid in listed:
            write_file(repo, f"{THEMES_REL}/{tid}/theme.json", data)
            entries.append(index_entry(doc, sha256(data)))
    revoked_list = [{"id": r, "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"} for r in sorted(revoked)]
    write_file(repo, REVOKED_REL, dumps(revoked_list))
    write_file(repo, PUBLISHED_REL, dumps(dict(sorted(published.items()))))
    write_file(repo, INDEX_REL, dumps({"schemaVersion": 1, "generatedAt": "2026-10-01T00:00:00Z",
                                       "themes": entries, "revoked": revoked_list}))


def read_json(repo, rel):
    return json.loads((repo / rel).read_text(encoding="utf-8"))


def write_json(repo, rel, data):
    write_file(repo, rel, dumps(data))


def edit_index(fn):
    def plant(head, base):
        data = read_json(head, INDEX_REL)
        fn(data)
        write_json(head, INDEX_REL, data)
    return plant


def edit_entry(fn):
    return edit_index(lambda data: fn(data["themes"][0]))


def set_path(value):
    return edit_entry(lambda t: t["files"]["theme.json"].__setitem__("path", value))


def plant_missing_index(head, base):
    (head / INDEX_REL).unlink()


def plant_malformed_json(head, base):
    write_file(head, INDEX_REL, "{not json")


def plant_top_level_not_object(head, base):
    write_file(head, INDEX_REL, "[1, 2, 3]")


def plant_themes_folder_symlink(head, base):
    real = head / "elsewhere.json"
    (head / THEMES_REL / "olympus-dusk" / "theme.json").rename(real)
    os.symlink(real, head / THEMES_REL / "olympus-dusk" / "theme.json")


def plant_folder_not_id(head, base):
    # The folder keeps its name; the file inside says another id. Moving the file under a new
    # folder would also break the index bijection, so this is the plant that isolates the rule.
    data = read_json(head, f"{THEMES_REL}/olympus-dusk/theme.json")
    data["id"] = "olympus-dawn"
    write_json(head, f"{THEMES_REL}/olympus-dusk/theme.json", data)


def plant_theme_too_large(head, base):
    data = read_json(head, f"{THEMES_REL}/olympus-dusk/theme.json")
    data["summary"]["en"] = "x" * MAX_THEME_BYTES
    write_json(head, f"{THEMES_REL}/olympus-dusk/theme.json", data)


def plant_theme_duplicate_key(head, base):
    text = (head / THEMES_REL / "olympus-dusk" / "theme.json").read_text(encoding="utf-8")
    write_file(head, f"{THEMES_REL}/olympus-dusk/theme.json", text.replace('"schemaVersion": 1,', '"schemaVersion": 1, "schemaVersion": 1,', 1))


def plant_theme_bad_version(head, base):
    data = read_json(head, f"{THEMES_REL}/olympus-dusk/theme.json")
    data["version"] = "1.0.٣"  # Arabic-Indic digit: \d would accept it
    write_json(head, f"{THEMES_REL}/olympus-dusk/theme.json", data)


def plant_theme_bad_scenario(head, base):
    data = read_json(head, f"{THEMES_REL}/olympus-dusk/theme.json")
    data["scenarios"] = ["agent-review", "agent-review"]
    write_json(head, f"{THEMES_REL}/olympus-dusk/theme.json", data)


def plant_reserved_id(head, base):
    write_file(head, f"{THEMES_REL}/dawn/theme.json", dumps(fixture_theme("dawn")))


def plant_bad_folder_name(head, base):
    write_file(head, f"{THEMES_REL}/Olympus/theme.json", dumps(fixture_theme("Olympus")))


def plant_extra_file_in_theme(head, base):
    write_file(head, f"{THEMES_REL}/olympus-dusk/theme.css", "body{}")


def plant_stray_file_in_themes(head, base):
    write_file(head, f"{THEMES_REL}/notes.txt", "hi")


def plant_revoked_missing(head, base):
    (head / REVOKED_REL).unlink()


def plant_revoked_bad_entry(head, base):
    write_json(head, REVOKED_REL, [{"id": "x", "reason": "Because <b>", "revokedAt": "2026-10-02T08:00:00Z"}])


def plant_revoked_mismatch(head, base):
    write_json(head, REVOKED_REL, [{"id": "some-theme", "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"}])


def plant_revoked_id_present(head, base):
    entry = {"id": "olympus-dusk", "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"}
    write_json(head, REVOKED_REL, [entry])
    edit_index(lambda d: d.__setitem__("revoked", [entry]))(head, base)


def plant_published_missing(head, base):
    (head / PUBLISHED_REL).unlink()


def plant_published_bad_key(head, base):
    data = read_json(head, PUBLISHED_REL)
    data["../x.png"] = "a" * 64
    write_json(head, PUBLISHED_REL, data)


def plant_unlisted_file(head, base):
    write_file(head, f"{V1_REL}/olympus-dusk/1.0.0/notes.txt", "hi")


def plant_listed_file_gone(head, base):
    (head / V1_REL / "olympus-dusk" / "1.0.0" / "preview-dark.png").unlink()


def plant_published_byte_edited(head, base):
    path = head / V1_REL / "olympus-dusk" / "1.0.0" / "preview-light.png"
    data = bytearray(path.read_bytes())
    data[-1] ^= 1
    path.write_bytes(bytes(data))


def plant_published_byte_edited_and_rehashed(head, base):
    path = head / V1_REL / "olympus-dusk" / "1.0.0" / "preview-light.png"
    data = bytearray(path.read_bytes())
    data[-1] ^= 1
    path.write_bytes(bytes(data))
    published = read_json(head, PUBLISHED_REL)
    published["olympus-dusk/1.0.0/preview-light.png"] = sha256(bytes(data))
    write_json(head, PUBLISHED_REL, published)


def plant_published_entry_dropped(head, base):
    # A delisted theme's published file and its entry both removed: this tree is consistent on
    # its own; only the base shows that a published file went away.
    (head / V1_REL / "second-theme" / "1.0.0" / "preview-dark.png").unlink()
    published = read_json(head, PUBLISHED_REL)
    del published["second-theme/1.0.0/preview-dark.png"]
    write_json(head, PUBLISHED_REL, published)


def plant_v1_symlink(head, base):
    os.symlink(head / V1_REL / "published.json", head / V1_REL / "olympus-dusk" / "1.0.0" / "link.json")


def plant_bijection_unlisted(head, base):
    write_file(head, f"{THEMES_REL}/new-theme/theme.json", dumps(fixture_theme("new-theme")))


def plant_bijection_listed_only(head, base):
    shutil.rmtree(head / THEMES_REL / "olympus-dusk")


def plant_index_field_mismatch(head, base):
    edit_entry(lambda t: t["name"].__setitem__("en", "Something Else"))(head, base)


def plant_index_sha_mismatch(head, base):
    edit_entry(lambda t: t["files"]["theme.json"].__setitem__("sha256", "0" * 64))(head, base)


def plant_index_path_not_canonical(head, base):
    edit_entry(lambda t: t["previews"].__setitem__("dark", "olympus-dusk/1.0.0/preview-light.png"))(head, base)


def plant_index_duplicate_id(head, base):
    edit_index(lambda d: d["themes"].append(json.loads(json.dumps(d["themes"][0]))))(head, base)


def rewrite_preview(head, png):
    rel = "olympus-dusk/1.0.0/preview-light.png"
    write_file(head, f"{V1_REL}/{rel}", png)
    published = read_json(head, PUBLISHED_REL)
    published[rel] = sha256(png)
    write_json(head, PUBLISHED_REL, published)


# The preview plants put the same bad file in the base too, so the base rule (published.json only
# gains entries) stays quiet and the single problem is the PNG rule's own.
def plant_preview_not_png(head, base):
    for repo in (head, base):
        rewrite_preview(repo, b"GIF89a" + b"\0" * 40)


def plant_preview_wrong_width(head, base):
    for repo in (head, base):
        rewrite_preview(repo, make_png(width=800))


def plant_preview_too_large(head, base):
    for repo in (head, base):
        rewrite_preview(repo, make_png(pad=MAX_PREVIEW_BYTES))


def plant_reused_id(head, base):
    # The base published olympus-dusk and then delisted it (files stay, index entry gone);
    # this tree lists it again.
    edit_index(lambda d: d.__setitem__("themes", []))(base, None)
    shutil.rmtree(base / THEMES_REL / "olympus-dusk")


def plant_author_change(head, base):
    edit_entry(lambda t: t["author"].__setitem__("github", "someone-else"))(base, None)


def base_bytes_differ(rel):
    def plant(head, base):
        write_file(base, rel, (base / rel).read_text(encoding="utf-8") + "\n")
    return plant


def base_without_themes(*tids):
    """The base lacks these themes/<id>/ folders (an inconsistent base is fine: only the change
    matters), so the PR's only change is adding them."""
    def plant(head, base):
        for tid in tids:
            shutil.rmtree(base / THEMES_REL / tid)
    return plant


def plant_bot_outside(head, base):
    shutil.rmtree(base / THEMES_REL / "olympus-dusk")
    shutil.rmtree(base / V1_REL / "second-theme")


def two_themes(repo):
    write_tree(repo, listed=("olympus-dusk", "second-theme"))


def empty_tree(repo):
    write_tree(repo, listed=())


def delisted_tree(repo):
    write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",))


def revoked_tree(repo):
    write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",), revoked=("second-theme",))


MAINTAINER = PR(DEFAULT_MAINTAINER_IDS[0])
BOT = PR(BOT_ID)
OTHER = PR(12345)

# (name, plant(head, base), words that must all be in the single problem, PR context, head/base
# builders). The default tree is one listed theme; the default base is an identical copy, and the
# default PR is the maintainer's, so a plant sees only the rule it breaks.
RULES = [
    # #141's index shape (updated: no theme.css, scenarios, generatedAt format).
    ("missing index.json", plant_missing_index, ["missing", "exists"]),
    ("malformed JSON", plant_malformed_json, ["not valid JSON"]),
    ("top level not an object", plant_top_level_not_object, ["top level must be a JSON object"]),
    ("schemaVersion is a boolean", edit_index(lambda d: d.__setitem__("schemaVersion", True)), ["schemaVersion must be an integer"]),
    ("generatedAt empty", edit_index(lambda d: d.__setitem__("generatedAt", "")), ["generatedAt must be a non-empty string"]),
    ("generatedAt not UTC ISO", edit_index(lambda d: d.__setitem__("generatedAt", "2026-10-01 00:00")), ["generatedAt must be a UTC time"]),
    ("themes not a list", edit_index(lambda d: d.__setitem__("themes", "nope")), ["themes must be a list"]),
    ("theme entry not an object", edit_index(lambda d: d["themes"].__setitem__(0, "nope")), ["is not an object"]),
    ("theme.id missing", edit_entry(lambda t: t.pop("id")), ["id must be a non-empty string"]),
    ("theme.version wrong type", edit_entry(lambda t: t.__setitem__("version", 1)), ["version must be a non-empty string"]),
    ("theme.minAppVersion missing", edit_entry(lambda t: t.pop("minAppVersion")), ["minAppVersion must be a non-empty string"]),
    ("theme.name wrong type", edit_entry(lambda t: t.__setitem__("name", "Olympus Dusk")), ["name must be an object"]),
    ("theme.summary missing 'en'", edit_entry(lambda t: t.__setitem__("summary", {})), ["summary must be an object"]),
    ("theme.author wrong type", edit_entry(lambda t: t.__setitem__("author", "Jane Doe")), ["author must be an object"]),
    ("theme.scenarios missing", edit_entry(lambda t: t.pop("scenarios")), ["scenarios must be 1-2 distinct ids"]),
    ("theme.scenarios outside the closed list", edit_entry(lambda t: t.__setitem__("scenarios", ["fun"])), ["scenarios must be 1-2 distinct ids"]),
    ("theme.scenarios three", edit_entry(lambda t: t.__setitem__("scenarios", list(SCENARIOS[:3]))), ["scenarios must be 1-2 distinct ids"]),
    ("theme.files has theme.css", edit_entry(lambda t: t["files"].__setitem__("theme.css", {"path": "a/1.0.0/theme.css", "sha256": "b" * 64})), ["must not have a 'theme.css'"]),
    ("theme.files missing 'theme.json' key", edit_entry(lambda t: t["files"].pop("theme.json")), ["files must be an object with a 'theme.json' entry"]),
    ("theme.files entry not an object", edit_entry(lambda t: t["files"].__setitem__("theme.json", "nope")), ["files['theme.json'] must be an object"]),
    ("theme.files.sha256 not a string", edit_entry(lambda t: t["files"]["theme.json"].__setitem__("sha256", 12345)), ["sha256 must be a string"]),
    ("theme.files.sha256 wrong length", edit_entry(lambda t: t["files"]["theme.json"].__setitem__("sha256", "a" * 63)), ["sha256 must be exactly 64 characters"]),
    ("theme.files.sha256 uppercase", edit_entry(lambda t: t["files"]["theme.json"].__setitem__("sha256", "A" * 64)), ["sha256 must be lowercase hex only"]),
    ("theme.previews missing", edit_entry(lambda t: t.pop("previews")), ["previews must be an object"]),
    ("theme.previews missing 'light' key", edit_entry(lambda t: t["previews"].pop("light")), ["previews must be an object with 'light' and 'dark'"]),
    ("theme.previews missing 'dark' key", edit_entry(lambda t: t["previews"].pop("dark")), ["previews must be an object with 'light' and 'dark'"]),
    ("theme.previews.dark unsafe path", edit_entry(lambda t: t["previews"].__setitem__("dark", "a//b.png")), ["previews.dark", "must match"]),
    ("revoked not a list", edit_index(lambda d: d.__setitem__("revoked", "nope")), ["revoked must be a list"]),
    ("revoked entry not an object", edit_index(lambda d: d.__setitem__("revoked", ["nope"])), ["revoked[0]", "is not an object"]),
    ("revoked[].id missing", edit_index(lambda d: d.__setitem__("revoked", [{"reason": "r", "revokedAt": "t"}])), ["revoked[0]", "id must be a non-empty string"]),
    ("revoked[].reason missing", edit_index(lambda d: d.__setitem__("revoked", [{"id": "i", "revokedAt": "t"}])), ["revoked[0]", "reason must be a non-empty string"]),
    ("revoked[].revokedAt missing", edit_index(lambda d: d.__setitem__("revoked", [{"id": "i", "reason": "r"}])), ["revoked[0]", "revokedAt must be a non-empty string"]),
    # The path allowlist, one plant per way of failing it (#141 rounds 2-3).
    ("path: not a string", set_path(12345), ["path", "must be a string"]),
    ("path: uppercase", set_path("Olympus-Dusk/theme.json"), ["path", "must match"]),
    ("path: percent sign", set_path("a%2ejson"), ["path", "must match"]),
    ("path: question mark", set_path("a?x=1"), ["path", "must match"]),
    ("path: hash", set_path("a#frag"), ["path", "must match"]),
    ("path: colon", set_path("a:b.json"), ["path", "must match"]),
    ("path: backslash", set_path("a\\b.json"), ["path", "must match"]),
    ("path: leading slash (empty segment)", set_path("/a.json"), ["path", "must match"]),
    ("path: double slash (empty segment)", set_path("a//b.json"), ["path", "must match"]),
    ("path: single '.' segment", set_path("a/./b.json"), ["path", "must match"]),
    ("path: '..' segment", set_path("a/../b.json"), ["path", "must match"]),
    ("path: DEL (0x7F) character", set_path("a\x7fb.json"), ["path", "must match"]),
    ("path: previews.light", edit_entry(lambda t: t["previews"].__setitem__("light", "/a.png")), ["previews.light", "must match"]),
    ("path: previews.dark (direct)", edit_entry(lambda t: t["previews"].__setitem__("dark", "/a.png")), ["previews.dark", "must match"]),
    ("path: verify2 escape '%2e%2e#'", set_path("%2e%2e#"), ["path", "must match"]),
    ("path: verify2 escape '..?x'", set_path("..?x"), ["path", "must match"]),
    ("path: verify2 escape '%2e.#'", set_path("%2e.#"), ["path", "must match"]),
    ("path: verify2 escape 'c:/x'", set_path("c:/x"), ["path", "must match"]),
    ("path: verify2 escape 'javascript:alert(1)'", set_path("javascript:alert(1)"), ["path", "must match"]),
    # themes/ (#144 W3 file rules).
    ("themes: symlinked theme.json", plant_themes_folder_symlink, ["is a symlink", "themes/"]),
    ("themes: folder != id", plant_folder_not_id, ["doesn't match its folder name"]),
    ("themes: theme.json over 16 KB", plant_theme_too_large, ["larger than 16384 bytes"]),
    ("themes: duplicate JSON key", plant_theme_duplicate_key, ["not valid JSON", "duplicate key"]),
    ("themes: version not ASCII MAJOR.MINOR.PATCH", plant_theme_bad_version, ["version must be MAJOR.MINOR.PATCH"]),
    ("themes: scenario listed twice", plant_theme_bad_scenario, ["themes/olympus-dusk/theme.json", "scenarios must be"]),
    ("themes: built-in id", plant_reserved_id, ["built-in theme's and reserved"]),
    ("themes: folder name not an id", plant_bad_folder_name, ["folder name isn't a theme id"]),
    ("themes: extra file in a theme folder", plant_extra_file_in_theme, ["holds only theme.json"]),
    ("themes: stray file in themes/", plant_stray_file_in_themes, ["holds only revoked.json"]),
    ("themes: revoked.json missing", plant_revoked_missing, ["revoked.json: missing"]),
    ("themes: revoked.json entry reason not a code", plant_revoked_bad_entry, ["reason must be a lowercase-hyphenated code"]),
    # public/themes/v1/ and published.json.
    ("v1: published.json missing", plant_published_missing, ["published.json: missing"]),
    ("v1: published.json key outside <id>/<version>/<file>", plant_published_bad_key, ["published.json: key", "must match"]),
    ("v1: file not listed in published.json", plant_unlisted_file, ["not listed in published.json"]),
    ("v1: listed file gone", plant_listed_file_gone, ["lists olympus-dusk/1.0.0/preview-dark.png, which doesn't exist"]),
    ("v1: edited published byte", plant_published_byte_edited, ["sha256 doesn't match published.json"]),
    ("v1: symlink", plant_v1_symlink, ["is a symlink", "public/themes/v1"]),
    # index <-> themes/ <-> files.
    ("cross: themes/<id>/ not in the index", plant_bijection_unlisted, ["themes/new-theme/", "not in public/themes/v1/index.json"]),
    ("cross: index entry without themes/<id>/", plant_bijection_listed_only, ["listed, but themes/olympus-dusk/theme.json doesn't exist"]),
    ("cross: index field differs from theme.json", plant_index_field_mismatch, ["doesn't match themes/olympus-dusk/theme.json in name"]),
    ("cross: index sha256 differs", plant_index_sha_mismatch, ["with the sha256 of themes/olympus-dusk/theme.json"]),
    ("cross: preview path not canonical", plant_index_path_not_canonical, ["previews must be olympus-dusk/1.0.0/preview-light.png and"]),
    ("cross: id listed twice", plant_index_duplicate_id, ["id appears more than once"]),
    ("cross: preview not a PNG", plant_preview_not_png, ["doesn't start with a PNG signature"]),
    ("cross: preview wrong width", plant_preview_wrong_width, ["800x2", "must be 1200 wide"]),
    ("cross: preview over 500 KB", plant_preview_too_large, ["at most 512000"]),
    ("cross: index.revoked != revoked.json", plant_revoked_mismatch, ["revoked doesn't equal themes/revoked.json"]),
    ("cross: revoked id present", plant_revoked_id_present, ["revoked id 'olympus-dusk' is still published"]),
    # Against the base branch.
    ("base: edited published byte, published.json rehashed", plant_published_byte_edited_and_rehashed, ["only gains entries", "preview-light.png"]),
    ("base: published entry dropped", plant_published_entry_dropped, ["only gains entries", "second-theme/1.0.0/preview-dark.png"], MAINTAINER, delisted_tree),
    ("base: reused id", plant_reused_id, ["delisted or revoked; ids are never reused"]),
    ("base: author change without the label", plant_author_change, ["author.github changed from 'someone-else' to 'janedoe'"]),
    # PR authorship classes.
    ("authorship: non-maintainer edits public/themes/v1", base_bytes_differ(INDEX_REL), ["isn't a maintainer and may not change public/themes/v1/"], OTHER),
    ("authorship: non-maintainer edits revoked.json", base_bytes_differ(REVOKED_REL), ["isn't a maintainer and may not change themes/revoked.json"], OTHER),
    ("authorship: non-maintainer changes two themes", base_without_themes("olympus-dusk", "second-theme"), ["isn't a maintainer and may change at most one themes/<id>/"], OTHER, two_themes),
    ("authorship: bot changes two themes", base_without_themes("olympus-dusk", "second-theme"), ["bot PR may change at most one themes/<id>/"], BOT, two_themes),
    ("authorship: bot edits revoked.json", base_bytes_differ(REVOKED_REL), ["bot PR may not change themes/revoked.json"], BOT),
    ("authorship: bot edits another theme's files", plant_bot_outside, ["bot PR changes public/themes/v1 files outside", "second-theme"], BOT, two_themes),
]


def no_plant(head, base):
    pass


# Changes that must pass: (name, plant(head, base), PR, head builder, base builder).
def passes():
    return [
        ("unbroken tree", no_plant, MAINTAINER, None, None),
        ("empty tree (as published after #144)", no_plant, OTHER, empty_tree, empty_tree),
        ("maintainer multi-theme PR", no_plant, MAINTAINER, two_themes, empty_tree),
        ("bot single-theme PR", no_plant, BOT, two_themes, write_tree),
        ("delisting PR (maintainer)", no_plant, MAINTAINER, delisted_tree, two_themes),
        ("revocation PR (maintainer)", no_plant, MAINTAINER, revoked_tree, two_themes),
        ("author change with the label", plant_author_change, PR(DEFAULT_MAINTAINER_IDS[0], [AUTHOR_CHANGE_LABEL]), None, None),
        ("new version of an existing theme (maintainer)", no_plant, MAINTAINER, new_version_head, write_tree),
    ]


def run_case(plant, pr, head_builder=None, base_builder=None, use_base=True):
    with tempfile.TemporaryDirectory() as tmp:
        head, base = Path(tmp) / "head", Path(tmp) / "base"
        (head_builder or write_tree)(head)
        base.mkdir()
        (base_builder or head_builder or write_tree)(base)
        plant(head, base)
        return check(head, Snapshot.from_dir(base) if use_base else None, pr if use_base else None)


def new_version_head(repo):
    """olympus-dusk moved to 1.0.1: 1.0.0's files stay published, the index points at 1.0.1."""
    write_tree(repo)
    doc = fixture_theme("olympus-dusk", version="1.0.1")
    data = dumps(doc).encode()
    write_file(repo, f"{THEMES_REL}/olympus-dusk/theme.json", data)
    published = read_json(repo, PUBLISHED_REL)
    for name, body in (("theme.json", data), ("preview-light.png", make_png()), ("preview-dark.png", make_png())):
        write_file(repo, f"{V1_REL}/olympus-dusk/1.0.1/{name}", body)
        published[f"olympus-dusk/1.0.1/{name}"] = sha256(body)
    write_json(repo, PUBLISHED_REL, dict(sorted(published.items())))
    edit_index(lambda d: d.__setitem__("themes", [index_entry(doc, sha256(data))]))(repo, None)


def git_env():
    env = dict(os.environ)
    env.update(GIT_AUTHOR_NAME="self-test", GIT_AUTHOR_EMAIL="self-test@example.invalid",
               GIT_COMMITTER_NAME="self-test", GIT_COMMITTER_EMAIL="self-test@example.invalid",
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
    return env


def self_test() -> int:
    failures = 0

    def fail(message):
        nonlocal failures
        print(f"self-test: {message}")
        failures += 1

    # No public/themes/v1/ at all: mandatory, with its own words ("mandatory", which the
    # index-missing message below doesn't contain).
    with tempfile.TemporaryDirectory() as tmp:
        problems = check(Path(tmp))
        if len(problems) != 1 or "mandatory" not in problems[0]:
            fail(f"an absent themes/v1/ should fail with 'mandatory', got {problems}")

    # v1/ present with a file but no index.json: its own words ("exists").
    with tempfile.TemporaryDirectory() as tmp:
        write_file(Path(tmp), f"{V1_REL}/some-theme/x", "x")
        problems = check(Path(tmp))
        if not any("missing" in p and "exists" in p for p in problems):
            fail(f"themes/v1/ without index.json should fail with 'missing' and 'exists', got {problems}")

    for name, plant, pr, head_builder, base_builder in passes():
        problems = run_case(plant, pr, head_builder, base_builder)
        if problems:
            fail(f"{name!r} should pass, got {problems}")

    for rule in RULES:
        name, plant, words = rule[:3]
        pr = rule[3] if len(rule) > 3 else MAINTAINER
        head_builder = rule[4] if len(rule) > 4 else None
        problems = run_case(plant, pr, head_builder)
        if len(problems) != 1:
            fail(f"planted {name!r}; wanted exactly 1 problem, got {problems}")
        elif not all(word in problems[0] for word in words):
            fail(f"planted {name!r}; wanted {words!r} in the single problem, got {problems[0]!r}")
        else:
            print(f"  ok  {name}: {problems[0]}")

    # The non-maintainer PR that edits public/themes/v1 fails even as a whole-tree change the
    # maintainer could make (the rev-3 plant, stated as the real PR shape: adding a theme).
    problems = run_case(no_plant, OTHER, two_themes, empty_tree)
    if not any("isn't a maintainer and may not change public/themes/v1/" in p for p in problems):
        fail(f"a non-maintainer adding two published themes should fail on public/themes/v1, got {problems}")

    # The base reader CI uses: a real git repository, read back through ls-tree/cat-file, must
    # equal the same tree read from disk; an unknown revision must fail closed.
    if shutil.which("git"):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",))
            env = git_env()
            for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "fixture"]):
                subprocess.run(["git", "-C", str(repo), *args], check=True, env=env, capture_output=True)
            from_git = Snapshot.from_git(repo, "HEAD")
            from_dir = Snapshot.from_dir(repo)
            if from_git.entries != from_dir.entries:
                fail("Snapshot.from_git and Snapshot.from_dir disagree on the same tree")
            elif from_git.read(PUBLISHED_REL) != (repo / PUBLISHED_REL).read_bytes():
                fail("Snapshot.from_git reads different bytes than the file on disk")
            elif check(repo, from_git, MAINTAINER):
                fail(f"a tree checked against itself from git should pass, got {check(repo, from_git, MAINTAINER)}")
            try:
                Snapshot.from_git(repo, "0" * 40)
                fail("an unknown base revision was read instead of failing closed")
            except BaseUnavailable:
                pass
    else:
        fail("git isn't available; the base reader can't be tested")

    # Bootstrap: a base that never published anything has no published.json and that's fine; a
    # base that did publish and lacks it fails closed.
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        write_file(base, INDEX_REL, dumps({"schemaVersion": 1, "generatedAt": "2026-09-27T00:00:00Z", "themes": [], "revoked": []}))
        if base_published(Snapshot.from_dir(base)) != {}:
            fail("a base with an empty index and no published.json should read as {}")
        write_file(base, f"{V1_REL}/olympus-dusk/1.0.0/theme.json", "{}")
        try:
            base_published(Snapshot.from_dir(base))
            fail("a base with published files but no published.json didn't fail closed")
        except BaseUnavailable:
            pass

    # The maintainer allowlist parser fails closed on anything but numeric ids.
    try:
        parse_maintainers("redtear1115")
        fail("a login in THEME_MAINTAINER_IDS was accepted")
    except ValueError:
        pass
    if parse_maintainers("") != DEFAULT_MAINTAINER_IDS or parse_maintainers("1, 2") != (1, 2):
        fail("THEME_MAINTAINER_IDS parsing is wrong")

    print(f"self-test: {len(RULES)} plants, {len(passes())} passing changes, {failures} failures")
    return 1 if failures else 0


# --- entry point --------------------------------------------------------------------------------------

def ci_context(repo: Path):
    """(base Snapshot, PR or None) from the GitHub Actions event payload file. Raises
    BaseUnavailable (fail closed) when anything needed is missing."""
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = os.environ.get("GITHUB_EVENT_PATH", "")
    try:
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise BaseUnavailable(f"can't read the event payload ({error})") from error
    if event_name == "pull_request":
        pr = event.get("pull_request") or {}
        base_sha = (pr.get("base") or {}).get("sha")
        author_id = (pr.get("user") or {}).get("id")
        if not isinstance(base_sha, str) or not is_int_not_bool(author_id):
            raise BaseUnavailable("the pull_request payload lacks base.sha or user.id")
        labels = [label.get("name") for label in pr.get("labels") or [] if isinstance(label, dict)]
        try:
            maintainers = parse_maintainers(os.environ.get("THEME_MAINTAINER_IDS"))
        except ValueError as error:
            raise BaseUnavailable(str(error)) from error
        commit = fetch_base(repo, base_sha)
        return Snapshot.from_git(repo, commit), PR(author_id, labels, maintainers)
    if event_name == "push":
        before = event.get("before")
        rev = before if isinstance(before, str) and re.fullmatch(r"[0-9a-f]{40}", before) and before != "0" * 40 else "main"
        commit = fetch_base(repo, rev)
        return Snapshot.from_git(repo, commit), None
    raise BaseUnavailable(f"--ci doesn't know the event {event_name!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=str(ROOT), help="repository root (default: this script's)")
    parser.add_argument("--base", help="compare against this local revision (no PR authorship rules)")
    parser.add_argument("--ci", action="store_true", help="GitHub Actions: fetch the base, apply PR rules")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    repo = Path(args.repo).resolve()
    base = pr = None
    try:
        if args.ci:
            base, pr = ci_context(repo)
        elif args.base:
            base = Snapshot.from_git(repo, args.base)
    except BaseUnavailable as error:
        print(f"::error::base branch: {error}; failing closed")
        return 1

    problems = check(repo, base, pr)
    for problem in problems:
        print(f"::error::{problem}")
    if not problems:
        scope = "against the base" + (f", PR author class {pr.kind}" if pr else "") if base else "this tree only"
        print(f"check_theme_index: ok ({scope})")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
