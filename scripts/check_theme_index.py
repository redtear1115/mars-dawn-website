#!/usr/bin/env python3
r"""Checks the theme gallery's published tree: public/themes/v1/ against themes/ (#77, #144).

Usage:
    python3 scripts/check_theme_index.py                  # this tree only
    python3 scripts/check_theme_index.py --base <ref>     # plus the rules that compare to a base
    python3 scripts/check_theme_index.py --ci             # in GitHub Actions: base + PR authorship
    python3 scripts/check_theme_index.py --self-test

Design of record: the app repo's docs/theme-ecosystem-design.md §5.1-§5.3 (release/1.0.2 2c03440);
plan-website-104 revision 4, W3, and the implementation security review of PR #149 (M1-M3, L1-L7).
`scripts/build_themes.py` (macOS, runs the kit CLI) writes what this checks; this runs on Ubuntu CI
with the standard library only, so it can't run the kit's validator: the kit's verdict is taken at
build time, and this holds the committed result to it (sha256 of the exact source bytes) and to
every rule that doesn't need the kit.

**This check is advisory for any PR that touches scripts/** or .github/**.** A pull_request check
runs the PR's own copy of this script and of the workflow, so such a PR can weaken the very check it
is judged by. The rule below that fails a non-maintainer/bot PR touching those paths can itself be
edited away -- but that edit then sits in the diff, which reviewers must read. For those PRs the
review is the gate, not a green `check`. No pull_request_target is used, by design (it would run
with a write token and secrets next to PR data).

What lives where:

- `themes/<id>/theme.json` -- the build input, one folder per listed theme, and `themes/revoked.json`
  (a list of {id, reason, revokedAt}; mandatory, `[]` when nothing is revoked).
- `public/themes/v1/index.json` -- the index the app fetches (§5.1).
- `public/themes/v1/<id>/<version>/{theme.json,preview-light.png,preview-dark.png}` -- versioned,
  immutable files.
- `public/themes/v1/published.json` -- the append-only record, {path: sha256}, of every file ever
  published under public/themes/v1/ (paths relative to it, like the index's).

public/, public/themes/, public/themes/v1/ and themes/ must be real directories (no symlink on the
way), and nothing under themes/ or public/themes/v1/ may be a symlink or a committed .DS_Store.

Rules on this tree alone (each has a --self-test plant that must produce exactly one problem, with
that rule's own words):

- index.json exists, parses without duplicate keys, has no top-level key beyond schemaVersion,
  generatedAt, themes, revoked, and has §5.1's shape field for field: schemaVersion an integer (not
  a bool), generatedAt an ISO-8601 UTC time, themes a list of entries with id, version,
  minAppVersion, name{en}, summary{en}, author{name}, **scenarios** (1-2 distinct ids from §4.5's
  closed list), files with a `theme.json` entry {path, sha256} and **no `theme.css`**,
  previews{light, dark}; revoked a list of {id, reason, revokedAt}. Every path matches the allowlist
  PATH_RE.
- themes/ holds only revoked.json and <id>/ folders; each folder holds only theme.json, a regular
  file of at most 16 KB, parsing as a JSON object without duplicate keys, whose id equals its folder
  name, matches the id grammar and isn't a built-in's, whose version is MAJOR.MINOR.PATCH (ASCII,
  0-9999, no leading zeros), with name{en}, summary{en}, author{name} (author.github, when present,
  an ASCII GitHub login) and scenarios as above.
- public/themes/v1/ holds only index.json, published.json and files published.json lists; every
  listed file exists and its sha256 matches.
- index <-> themes/ is a bijection by id; each entry's version/name/summary/scenarios/author equal
  its theme.json's; its paths are the canonical `<id>/<version>/...`; its theme.json sha256 equals
  both themes/<id>/theme.json's and published.json's; both previews are listed and are whole,
  well-formed PNGs (every chunk's CRC, a 13-byte IHDR first, an allowed bit depth/colour type, an
  allowlisted chunk set, IEND last with nothing after it), PREVIEW_WIDTH wide, 1-8000 tall, at most
  500 KB.
- index.revoked equals themes/revoked.json (sorted by id), and no revoked id is still in themes/ or
  the index.

Rules against the base branch (`--ci` takes the first parent of the merge commit it checked out,
fetches it by SHA, and **fails closed** if it can't be read):

- published.json only gains entries. A base without published.json is read as "nothing published"
  only for the first publication: when the base has neither themes/ nor public/themes/v1/, or its
  v1/ holds nothing but the exact empty index #141 published (blob BOOTSTRAP_INDEX_BLOB). Any
  other base lacking published.json, index.json or revoked.json fails closed.
- Ids are never reused: an id with files in the base published.json that the base index doesn't
  list was delisted or revoked; seeing it in themes/ again fails.
- On pull_request events only (a push runs after the PR's gate, without its labels):
  - a bot or non-maintainer PR keeps a listed theme's author.github (ASCII case-insensitively)
    unless the PR has the label `theme-author-change`; a maintainer PR may change it;
  - a new version of a listed theme is strictly greater than the base's, unless a maintainer PR has
    the label `theme-version-rollback`;
  - only a maintainer PR may remove an id from themes/revoked.json (un-revoke).
  Any user with triage access can apply labels (plan F3): a label is a reviewer's statement, not
  an authorization, which is why the rollback label only counts on a maintainer's PR.

PR authorship classes (`--ci` on a pull_request event; by `pull_request.user.id`, read from the
event payload file, never from text spliced into `run:`):

- **bot** (github-actions[bot], id 41898282): at most one themes/<id>/ folder, no
  themes/revoked.json, under public/themes/v1/ only that id's folder, index.json and
  published.json, nothing under scripts/ or .github/, and elsewhere only generated pages
  (GENERATED_PAGE_*: index.html/index.md under public/, sitemap, llms*.txt, product-facts.md).
- **maintainer** (id in $THEME_MAINTAINER_IDS, a repo variable; comma-separated numeric ids; unset
  means 16503101): anything, still subject to every rule on the tree and the base.
- **anyone else**: nothing under scripts/ or .github/; no public/themes/v1/**, themes/revoked.json
  or more than one themes/<id>/ folder; and a PR touching theme data changes nothing else but
  generated pages. (A PR that doesn't touch theme data may change the rest of the site.) A
  single-theme data PR still fails -- the index doesn't list it -- and goes through W2's
  theme-from-pr instead.

The emergency path (§5.3), by hand without a Mac: remove themes/<id>/, drop its index entry and,
to revoke, add the same {id, reason, revokedAt} to themes/revoked.json and index.revoked. Published
files and their published.json entries stay. The self-test's revocation case is exactly this edit.

In --ci the checked-out tree is read both from disk and from git (HEAD) and the two must agree, so
an untracked or ignored file can't make the disk view differ from what was committed.
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
import traceback
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

THEMES_REL = "themes"
V1_REL = "public/themes/v1"
REVOKED_REL = "themes/revoked.json"
INDEX_REL = V1_REL + "/index.json"
PUBLISHED_REL = V1_REL + "/published.json"
# Every directory on the way to the checked trees; each must be a real directory.
DIRS = ("public", "public/themes", V1_REL, THEMES_REL)
CODE_PREFIXES = ("scripts/", ".github/")
GENERATED_PAGE_NAMES = ("index.html", "index.md")
GENERATED_PAGE_FILES = ("public/sitemap.xml", "public/llms.txt", "public/llms-full.txt", "public/product-facts.md")

# Allowlist for every path the index and published.json carry. A denylist (reject `..`, a scheme,
# `//`) had real gaps in #141's review rounds -- single-colon schemes (`c:`, `javascript:`) and
# percent-encoded dots (`%2e%2e`). Only lowercase letters, digits, `.`, `_`, `-` within a segment,
# single `/` between segments, every segment starting with a letter or digit: no `%`, `?`, `#`,
# `:`, `\`, uppercase, empty segment, or `.`/`..` segment can pass, so nothing needs decoding.
PATH_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$")
# The kit's ThemeGrammar at the pinned commit, as ASCII-only patterns used with fullmatch (so no
# `$`-before-newline, and `[0-9]` rather than `\d`, which would accept other scripts' digits).
# Versions are stricter than the kit's (no leading zeros), so "01.0.0" and "1.0.0" can't coexist.
ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MAX_ID_LENGTH = 32
_NUM = r"(?:0|[1-9][0-9]{0,3})"
VERSION_RE = re.compile(rf"{_NUM}\.{_NUM}\.{_NUM}")
LOGIN_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}")
TIME_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
SHA_RE = re.compile(r"[0-9a-f]{64}")
COMMIT_RE = re.compile(r"[0-9a-f]{40}")
REASON_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
INDEX_KEYS = ("schemaVersion", "generatedAt", "themes", "revoked")

SCENARIOS = ("agent-review", "technical-docs", "formal-output", "notes-sharing")  # design §4.5
RESERVED_IDS = ("dawn", "classic", "modern", "vivid")  # design §4.2: built-in ids are reserved
MAX_THEME_BYTES = 16 * 1024
MAX_PREVIEW_BYTES = 500 * 1024
PREVIEW_WIDTH = 1200
PREVIEW_MAX_HEIGHT = 8000
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
# What the kit's renderer writes (IHDR, sRGB, eXIf, IDAT..., IEND) plus the other colour and
# physical chunks a PNG encoder may add. No text chunks: nothing in a preview needs one.
PNG_CHUNKS = {b"IHDR", b"PLTE", b"IDAT", b"IEND", b"tRNS", b"sRGB", b"gAMA", b"cHRM", b"iCCP",
              b"sBIT", b"pHYs", b"bKGD", b"eXIf"}
PNG_DEPTHS = {0: {1, 2, 4, 8, 16}, 2: {8, 16}, 3: {1, 2, 4, 8}, 4: {8, 16}, 6: {8, 16}}
FILE_NAMES = ("theme.json", "preview-light.png", "preview-dark.png")
# The first app version with the gallery (app #293, milestone "1.1.1 theme gallery").
MIN_APP_VERSION = "1.1.1"
# The exact empty index #141 committed (public/themes/v1/index.json at release-1.0.4 81be4f85):
# the one v1/ a base may have without a published.json.
BOOTSTRAP_INDEX_BLOB = "e6d8e0fcf3db23e34edeea6b780d59a590ba43d0"

BOT_ID = 41898282  # github-actions[bot]
DEFAULT_MAINTAINER_IDS = (16503101,)  # redtear1115; plan-website-104 Needs-you
AUTHOR_CHANGE_LABEL = "theme-author-change"
ROLLBACK_LABEL = "theme-version-rollback"


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


def version_key(value: str) -> tuple:
    return tuple(int(part) for part in value.split("."))


_ASCII_FOLD = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")


def ascii_lower(text: str) -> str:
    """Case-folds A-Z only: str.lower() would also fold e.g. the Kelvin sign (U+212A) to 'k'."""
    return text.translate(_ASCII_FOLD)


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


def png_info(data: bytes):
    """(problem, (width, height)): walks every chunk. problem is None for a whole, well-formed PNG
    this site accepts as a preview (dimensions are the caller's rule)."""
    if not data.startswith(PNG_SIGNATURE) or data[12:16] != b"IHDR":
        return "doesn't start with a PNG signature and IHDR", None
    pos, index, size, seen_idat, idat_done = len(PNG_SIGNATURE), 0, None, False, False
    while True:
        if pos + 12 > len(data):
            return "is truncated (a chunk runs past the end, or IEND is missing)", size
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        end = pos + 12 + length
        if end > len(data):
            return f"is truncated inside chunk {index} ({kind!r})", size
        body = data[pos + 8:pos + 8 + length]
        crc = struct.unpack(">I", data[end - 4:end])[0]
        if zlib.crc32(kind + body) & 0xFFFFFFFF != crc:
            return f"chunk {index} ({kind.decode('latin-1')}) has a bad CRC", size
        if kind not in PNG_CHUNKS:
            return f"chunk {index} has type {kind!r}, which isn't allowed in a preview", size
        if index == 0:
            if length != 13:
                return f"IHDR is {length} bytes; it must be 13", None
            width, height, depth, colour, compression, filtering, interlace = struct.unpack(">IIBBBBB", body)
            size = (width, height)
            if depth not in PNG_DEPTHS.get(colour, ()) or compression or filtering or interlace not in (0, 1):
                return (f"IHDR has bit depth {depth} / colour type {colour} / methods "
                        f"{compression},{filtering},{interlace}, which PNG doesn't allow"), size
        elif kind == b"IHDR":
            return "has a second IHDR", size
        if kind == b"IDAT":
            if idat_done:
                return "has IDAT chunks that aren't consecutive", size
            seen_idat = True
        elif seen_idat:
            idat_done = True
        if kind == b"IEND":
            if not seen_idat:
                return "has no IDAT before IEND", size
            if end != len(data):
                return f"has {len(data) - end} bytes after IEND", size
            return None, size
        pos, index = end, index + 1


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
    return ascii_lower(github) if isinstance(github, str) else ""


# --- snapshots: the trees the rules compare --------------------------------------------------------

class BaseUnavailable(RuntimeError):
    pass


class Snapshot:
    """{repo-relative path: (kind, git blob id)} for everything under themes/ and
    public/themes/v1/, plus an entry for any of DIRS that isn't a real directory; and a reader.
    kind is "file", "symlink" or "other"."""

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

    def bad_dir(self, prefix: str):
        """The first of DIRS on the way to `prefix` (inclusive) that isn't a real directory."""
        for d in DIRS:
            if (prefix == d or prefix.startswith(d + "/")) and d in self.entries:
                return d
        return None

    @classmethod
    def from_dir(cls, repo: Path):
        entries = {}
        for d in DIRS:
            path = repo / d
            if path.is_symlink():
                entries[d] = ("symlink", git_blob_id(os.readlink(path).encode()))
            elif path.exists() and not path.is_dir():
                entries[d] = ("other", "")
        snap = cls(entries, lambda p: (repo / p).read_bytes())
        for prefix in (THEMES_REL, V1_REL):
            top = repo / prefix
            if snap.bad_dir(prefix) or not top.is_dir():
                continue
            for dirpath, dirnames, filenames in os.walk(top, followlinks=False):
                for name in dirnames:
                    full = Path(dirpath) / name
                    if full.is_symlink():
                        entries[full.relative_to(repo).as_posix()] = ("symlink", git_blob_id(os.readlink(full).encode()))
                for name in filenames:
                    full = Path(dirpath) / name
                    rel = full.relative_to(repo).as_posix()
                    if full.is_symlink():
                        entries[rel] = ("symlink", git_blob_id(os.readlink(full).encode()))
                    elif full.is_file():
                        entries[rel] = ("file", git_blob_id(full.read_bytes()))
                    else:
                        entries[rel] = ("other", "")
        return snap

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

        def records(*args):
            for record in git(*args).split(b"\0"):
                if record:
                    meta, _, path = record.partition(b"\t")
                    mode, kind, blob = meta.decode().split()
                    yield mode, kind, blob, path.decode("utf-8", errors="surrogateescape")

        commit = git("rev-parse", "--verify", "--end-of-options", f"{rev}^{{commit}}").decode().strip()
        entries = {}
        for mode, kind, blob, path in records("ls-tree", "-z", commit, "--", *DIRS):
            if path in DIRS and kind != "tree":
                entries[path] = ("symlink" if mode == "120000" else "other", blob)
        snap = cls(entries, lambda p: git("cat-file", "blob", entries[p][1]))
        prefixes = [p for p in (THEMES_REL, V1_REL) if not snap.bad_dir(p)]
        if prefixes:
            for mode, kind, blob, path in records("ls-tree", "-r", "-z", commit, "--", *prefixes):
                if kind == "blob" and mode in ("100644", "100755"):
                    entries[path] = ("file", blob)
                elif kind == "blob" and mode == "120000":
                    entries[path] = ("symlink", blob)
                else:
                    entries[path] = ("other", blob)
        return snap


def git_out(repo: Path, *args) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if result.returncode != 0:
        raise BaseUnavailable(f"git {' '.join(args)}: {result.stderr.decode(errors='replace').strip()}")
    return result.stdout.decode("utf-8", errors="surrogateescape")


def fetch_base(repo: Path, rev: str) -> str:
    """Fetches `rev` (a SHA or branch) from origin and returns the fetched commit. Raises
    BaseUnavailable on any failure: the caller fails closed."""
    if not (COMMIT_RE.fullmatch(rev) or re.fullmatch(r"[A-Za-z0-9._/-]{1,200}", rev)) or rev.startswith("-"):
        raise BaseUnavailable(f"refusing to fetch {rev!r}")
    git_out(repo, "fetch", "--no-tags", "--depth=1", "origin", rev)
    commit = git_out(repo, "rev-parse", "--verify", "FETCH_HEAD^{commit}").strip()
    if COMMIT_RE.fullmatch(rev) and commit != rev:
        raise BaseUnavailable(f"fetched {commit}, not the requested {rev}")
    return commit


def changed_all(repo: Path, base_commit: str) -> list:
    """Every path (repo-wide) that differs between the base commit and HEAD."""
    out = git_out(repo, "diff", "--name-only", "-z", "--no-renames", base_commit, "HEAD")
    return sorted(p for p in out.split("\0") if p)


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
    unknown = sorted(set(data) - set(INDEX_KEYS))
    if unknown:
        problems.append(f"{where}: unknown top-level key(s) {', '.join(map(repr, unknown))}; only {', '.join(INDEX_KEYS)}")

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
        problems.append(f"{where}: version must be MAJOR.MINOR.PATCH, each an ASCII number 0-9999 without leading zeros")
    for field in ("name", "summary"):
        value = doc.get(field)
        if not isinstance(value, dict) or not is_nonempty_str(value.get("en")):
            problems.append(f"{where}: {field} must be an object with a non-empty 'en' string")
    author = doc.get("author")
    if not isinstance(author, dict) or not is_nonempty_str(author.get("name")):
        problems.append(f"{where}: author must be an object with a non-empty 'name' string (the index shows it)")
    elif "github" in author and not (isinstance(author["github"], str) and LOGIN_RE.fullmatch(author["github"])):
        problems.append(f"{where}: author.github must be a GitHub login (ASCII letters, digits, single inner hyphens, 1-39)")
    bad = scenarios_problem(doc.get("scenarios"))
    if bad:
        problems.append(f"{where}: {bad}")
    return len(problems) == before


def parse_revoked(data):
    """(sorted list, []) or (None, problem list) for a revoked.json's bytes."""
    try:
        parsed = strict_json(data)
    except ValueError as error:
        return None, [f"{REVOKED_REL}: not valid JSON ({error})"]
    if not isinstance(parsed, list):
        return None, [f"{REVOKED_REL}: must be a list of {{id, reason, revokedAt}}"]
    problems, seen = [], set()
    for i, entry in enumerate(parsed):
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
    if problems:
        return None, problems
    return sorted(parsed, key=lambda e: e["id"]), []


def check_revoked_source(problems, snap):
    """themes/revoked.json -> sorted list, or None when it's unusable."""
    kind = snap.entries.get(REVOKED_REL, (None,))[0]
    if kind is None:
        problems.append(f"{REVOKED_REL}: missing; it is mandatory ([] when nothing is revoked)")
        return None
    if kind != "file":
        problems.append(f"{REVOKED_REL}: is a symlink or not a regular file")
        return None
    revoked, found = parse_revoked(snap.read(REVOKED_REL))
    problems += found
    return revoked


def ds_store_problem(path):
    return f"{path}: a .DS_Store is committed; remove it (it's Finder's, never part of the gallery)"


def check_sources(problems, snap):
    """{id: (bytes, doc)} for every usable themes/<id>/theme.json."""
    sources = {}
    folders = {}
    for path in snap.paths_under(THEMES_REL):
        kind = snap.entries[path][0]
        parts = path.split("/")[1:]
        if parts[-1] == ".DS_Store":
            problems.append(ds_store_problem(path))
            continue
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


def parse_published(data):
    """(dict, []) or (None, problem list) for a published.json's bytes."""
    try:
        parsed = strict_json(data)
    except ValueError as error:
        return None, [f"{PUBLISHED_REL}: not valid JSON ({error})"]
    if not isinstance(parsed, dict):
        return None, [f"{PUBLISHED_REL}: must be an object mapping path to sha256"]
    problems = []
    for key, value in parsed.items():
        bad = published_key_problem(key)
        if bad:
            problems.append(f"{PUBLISHED_REL}: key {key!r} {bad}")
        if not (isinstance(value, str) and SHA_RE.fullmatch(value)):
            problems.append(f"{PUBLISHED_REL}: {key!r} must map to a lowercase sha256")
    return (None, problems) if problems else (parsed, [])


def check_published_source(problems, snap):
    kind = snap.entries.get(PUBLISHED_REL, (None,))[0]
    if kind is None:
        problems.append(f"{PUBLISHED_REL}: missing; it is the append-only record of every published file")
        return None
    if kind != "file":
        problems.append(f"{PUBLISHED_REL}: is a symlink or not a regular file")
        return None
    published, found = parse_published(snap.read(PUBLISHED_REL))
    problems += found
    return published


def check_v1_files(problems, snap, published):
    """Every file under public/themes/v1/ is index.json, published.json or listed; every listed
    file exists, unchanged."""
    for path in snap.paths_under(V1_REL):
        kind = snap.entries[path][0]
        rel = path[len(V1_REL) + 1:]
        if rel.split("/")[-1] == ".DS_Store":
            problems.append(ds_store_problem(path))
        elif kind == "symlink":
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
    problem, size = png_info(data)
    if problem:
        problems.append(f"{where}: preview {rel} {problem}")
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
            problems.append(f"{where}: id or version doesn't match the grammar")
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
    for d in DIRS:
        if d in snap.entries:
            return None, [f"{d}: is a symlink or not a directory; public/, public/themes/, "
                          f"public/themes/v1/ and themes/ must be real directories"]
    if not snap.paths_under(V1_REL):
        return None, [f"{V1_REL}: missing; public/themes/v1/index.json is mandatory"]
    if snap.entries.get(INDEX_REL, (None,))[0] != "file":
        return None, [f"{INDEX_REL}: missing, but v1/ exists"]
    try:
        data = strict_json(snap.read(INDEX_REL))
    except (ValueError, UnicodeDecodeError) as error:
        return None, [f"{INDEX_REL}: not valid JSON ({error})"]
    if not isinstance(data, dict):
        return None, [f"{INDEX_REL}: top level must be a JSON object"]
    return data, []


# --- rules against the base branch and the PR's author ----------------------------------------------

class BaseState:
    def __init__(self, published, themes, revoked_ids):
        self.published = published  # {path: sha256}
        self.themes = themes        # {id: index entry}
        self.revoked_ids = revoked_ids


def base_state(base) -> BaseState:
    """What the base had published, listed and revoked. The first publication (a base with
    neither themes/ nor public/themes/v1/, or with only #141's exact empty index) reads as nothing
    published; any other base missing or garbling one of the three files raises BaseUnavailable."""
    for d in DIRS:
        if d in base.entries:
            raise BaseUnavailable(f"the base's {d} is a symlink or not a directory")
    v1_paths = base.paths_under(V1_REL)
    themes_paths = base.paths_under(THEMES_REL)
    if PUBLISHED_REL not in base.entries:
        first = not themes_paths and (
            not v1_paths or (v1_paths == [INDEX_REL] and base.entries[INDEX_REL] == ("file", BOOTSTRAP_INDEX_BLOB)))
        if first:
            return BaseState({}, {}, set())
        raise BaseUnavailable(f"the base has themes/ or public/themes/v1/ but no {PUBLISHED_REL}")
    if base.entries[PUBLISHED_REL][0] == "file":
        published, found = parse_published(base.read(PUBLISHED_REL))
    else:
        published, found = None, ["not a regular file"]
    if published is None:
        raise BaseUnavailable(f"the base's {PUBLISHED_REL} is unusable ({'; '.join(found)})")
    if base.entries.get(INDEX_REL, (None,))[0] != "file":
        raise BaseUnavailable(f"the base has {PUBLISHED_REL} but no readable {INDEX_REL}")
    try:
        index = strict_json(base.read(INDEX_REL))
    except ValueError as error:
        raise BaseUnavailable(f"the base's {INDEX_REL} isn't valid JSON ({error})") from error
    themes = index.get("themes") if isinstance(index, dict) else None
    if not isinstance(themes, list):
        raise BaseUnavailable(f"the base's {INDEX_REL} has no themes list")
    if base.entries.get(REVOKED_REL, (None,))[0] != "file":
        raise BaseUnavailable(f"the base has {PUBLISHED_REL} but no readable {REVOKED_REL}")
    revoked, found = parse_revoked(base.read(REVOKED_REL))
    if revoked is None:
        raise BaseUnavailable(f"the base's {REVOKED_REL} is unusable ({'; '.join(found)})")
    by_id = {t["id"]: t for t in themes if isinstance(t, dict) and isinstance(t.get("id"), str)}
    return BaseState(published, by_id, {r["id"] for r in revoked})


def check_against_base(problems, old, published, sources, index, pr):
    if published is not None:
        lost = sorted(k for k, v in old.published.items() if published.get(k) != v)
        if lost:
            problems.append(f"{PUBLISHED_REL}: only gains entries, but these base entries are gone or changed: {', '.join(lost)}")
    ever_published = {k.split("/", 1)[0] for k in old.published}
    for tid in sorted(sources):
        if tid in ever_published and tid not in old.themes:
            problems.append(f"themes/{tid}/: id {tid!r} was published before and delisted or revoked; ids are never reused")
    if index is None or pr is None:
        return  # the rules below judge a PR; a push runs after that PR's gate, without its labels
    for entry in index.get("themes", []):
        old_entry = old.themes.get(entry.get("id"))
        if old_entry is None:
            continue
        if (pr.kind != "maintainer" and AUTHOR_CHANGE_LABEL not in pr.labels
                and github_of(old_entry) != github_of(entry)):
            problems.append(f"{entry['id']!r}: author.github changed from {github_of(old_entry)!r} to {github_of(entry)!r} "
                            f"versus the base branch; a {pr.kind} PR needs the {AUTHOR_CHANGE_LABEL} label for that")
        new_v, old_v = entry.get("version"), old_entry.get("version")
        rollback_ok = pr.kind == "maintainer" and ROLLBACK_LABEL in pr.labels
        if (is_version(new_v) and is_version(old_v) and version_key(new_v) < version_key(old_v)
                and not rollback_ok):
            problems.append(f"{entry['id']!r}: version {new_v} is lower than the base's {old_v}; a new version must be "
                            f"greater (a rollback needs a maintainer PR with the {ROLLBACK_LABEL} label)")


def changed_paths(head, base) -> list:
    keys = set(head.entries) | set(base.entries)
    return sorted(k for k in keys if head.entries.get(k) != base.entries.get(k))


def is_generated_page(path: str) -> bool:
    if path in GENERATED_PAGE_FILES:
        return True
    return (path.startswith("public/") and not path.startswith(V1_REL + "/")
            and path.rsplit("/", 1)[-1] in GENERATED_PAGE_NAMES)


def check_authorship(problems, pr, changed, old_revoked_ids, new_revoked):
    if pr.kind == "maintainer":
        return
    who = "bot PR" if pr.kind == "bot" else f"PR author (id {pr.author_id})"
    not_maintainer = "" if pr.kind == "bot" else " isn't a maintainer and"
    code = [p for p in changed if p.startswith(CODE_PREFIXES)]
    if code:
        problems.append(f"{who}{not_maintainer} may not change scripts/ or .github/ ({', '.join(code)}); "
                        f"`check` runs the PR's own copy of both, so it can't vouch for such a PR -- only a maintainer's")
    theme_dirs = sorted({p.split("/")[1] for p in changed
                         if p.startswith(THEMES_REL + "/") and p != REVOKED_REL and p.count("/") >= 2})
    v1 = [p for p in changed if p == V1_REL or p.startswith(V1_REL + "/")]
    theme_data = [p for p in changed if p == THEMES_REL or p.startswith(THEMES_REL + "/")] + v1
    if pr.kind == "bot" or theme_data:
        outside = [p for p in changed if p not in theme_data and not p.startswith(CODE_PREFIXES)
                   and not is_generated_page(p)]
        if outside:
            problems.append(f"{who} may change only themes/, public/themes/v1/ and generated pages in a theme PR: {', '.join(outside)}")
    if REVOKED_REL in changed:
        new_ids = {r["id"] for r in new_revoked} if new_revoked is not None else set()
        unrevoked = sorted(old_revoked_ids - new_ids) if new_revoked is not None else []
        if unrevoked:
            problems.append(f"{who} may not un-revoke {', '.join(unrevoked)}; only a maintainer PR may remove a revocation")
        else:
            problems.append(f"{who}{not_maintainer} may not change {REVOKED_REL}")
    if pr.kind == "bot":
        if len(theme_dirs) > 1:
            problems.append(f"bot PR may change at most one themes/<id>/ folder; this one changes {', '.join(theme_dirs)}")
        allowed = {INDEX_REL, PUBLISHED_REL}
        own = [f"{V1_REL}/{d}/" for d in theme_dirs[:1]]
        outside = [p for p in v1 if p not in allowed and not any(p.startswith(o) for o in own)]
        if outside:
            problems.append(f"bot PR changes {V1_REL} files outside its theme's folder, index.json and published.json: {', '.join(outside)}")
        return
    if v1:
        problems.append(f"{who} isn't a maintainer and may not change {V1_REL}/: {', '.join(v1)}")
    if len(theme_dirs) > 1:
        problems.append(f"{who} isn't a maintainer and may change at most one themes/<id>/ folder; this PR changes {', '.join(theme_dirs)}")


# --- the check --------------------------------------------------------------------------------------

def check_snapshot(head, base=None, pr=None, changed=None) -> list:
    """Returns a list of problem strings; empty means the check passes. `changed` is every path
    (repo-wide) the PR changes; without it, only themes/ and public/themes/v1/ are compared."""
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
        try:
            old = base_state(base)
        except BaseUnavailable as error:
            problems.append(f"base branch: {error}; failing closed")
            return problems
        check_against_base(problems, old, published, sources, None if index_problems else index, pr)
        if pr is not None:
            check_authorship(problems, pr, changed if changed is not None else changed_paths(head, base),
                             old.revoked_ids, revoked)
    return problems


def check(repo: Path, base=None, pr=None, changed=None) -> list:
    return check_snapshot(Snapshot.from_dir(repo), base, pr, changed)


# --- CI context -------------------------------------------------------------------------------------

def ci_context(repo: Path, event_name: str, event: dict, maintainers_text, fetch=fetch_base):
    """(base Snapshot, PR or None, changed paths) for a GitHub Actions event. Raises
    BaseUnavailable (fail closed) when anything needed is missing or inconsistent."""
    if event_name == "pull_request":
        pr = event.get("pull_request") or {}
        author_id = (pr.get("user") or {}).get("id")
        head_sha = (pr.get("head") or {}).get("sha")
        if not is_int_not_bool(author_id):
            raise BaseUnavailable("the pull_request payload lacks user.id")
        labels = [label.get("name") for label in pr.get("labels") or [] if isinstance(label, dict)]
        try:
            maintainers = parse_maintainers(maintainers_text)
        except ValueError as error:
            raise BaseUnavailable(str(error)) from error
        # The checkout is GitHub's merge commit: its first parent is the base the PR merges into
        # (the tip the merge was computed against, not the payload's possibly older base.sha),
        # its second the PR head. `cat-file -p` reads the parents even in a shallow clone.
        raw = git_out(repo, "cat-file", "-p", "HEAD")
        parents = [line.split()[1] for line in raw.split("\n\n", 1)[0].splitlines() if line.startswith("parent ")]
        if len(parents) != 2:
            raise BaseUnavailable(f"HEAD has {len(parents)} parent(s); a pull_request check must run on GitHub's two-parent merge commit")
        if isinstance(head_sha, str) and parents[1] != head_sha:
            raise BaseUnavailable(f"HEAD's second parent {parents[1]} isn't the PR head {head_sha}")
        commit = fetch(repo, parents[0])
        return Snapshot.from_git(repo, commit), PR(author_id, labels, maintainers), changed_all(repo, commit)
    if event_name == "push":
        before = event.get("before")
        rev = before if isinstance(before, str) and COMMIT_RE.fullmatch(before) and before != "0" * 40 else "main"
        commit = fetch(repo, rev)
        return Snapshot.from_git(repo, commit), None, changed_all(repo, commit)
    raise BaseUnavailable(f"--ci doesn't know the event {event_name!r}")


def head_matches_git(repo: Path) -> list:
    """The disk view must be exactly what HEAD commits (no untracked, ignored or modified file)."""
    disk, committed = Snapshot.from_dir(repo), Snapshot.from_git(repo, "HEAD")
    differ = changed_paths(disk, committed)
    if differ:
        return [f"the checkout differs from HEAD under themes/ or public/themes/v1/: {', '.join(differ)}"]
    return []


# --- self-test fixtures -----------------------------------------------------------------------------

def png_chunk(kind: bytes, body: bytes) -> bytes:
    return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)


def make_png(width=PREVIEW_WIDTH, height=2, level=6, ihdr_extra=b"") -> bytes:
    raw = b"".join(b"\0" + bytes((x * 7 + y * 13) % 251 for x in range(width)) for y in range(height))
    return (PNG_SIGNATURE + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0) + ihdr_extra)
            + png_chunk(b"IDAT", zlib.compress(raw, level)) + png_chunk(b"IEND", b""))


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
    ids in both revoked lists. Plus a hand-written public/_headers, like the real site."""
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
    write_file(repo, "public/_headers", "/*\n  X-Frame-Options: DENY\n")


def read_json(repo, rel):
    return json.loads((repo / rel).read_text(encoding="utf-8"))


def write_json(repo, rel, data):
    write_file(repo, rel, dumps(data))


def no_plant(head, base):
    pass


def edit_index(fn):
    def plant(head, base):
        data = read_json(head, INDEX_REL)
        fn(data)
        write_json(head, INDEX_REL, data)
    return plant


def edit_entry(fn):
    return edit_index(lambda data: fn(data["themes"][0]))


def edit_base_entry(fn):
    return lambda head, base: edit_entry(fn)(base, None)


def set_path(value):
    return edit_entry(lambda t: t["files"]["theme.json"].__setitem__("path", value))


def edit_source(fn):
    def plant(head, base):
        rel = f"{THEMES_REL}/olympus-dusk/theme.json"
        data = read_json(head, rel)
        fn(data)
        write_json(head, rel, data)
    return plant


def add_file(rel, data="x"):
    return lambda head, base: write_file(head, rel, data)


def plant_missing_index(head, base):
    (head / INDEX_REL).unlink()


def plant_malformed_json(head, base):
    write_file(head, INDEX_REL, "{not json")


def plant_top_level_not_object(head, base):
    write_file(head, INDEX_REL, "[1, 2, 3]")


def plant_index_second_themes_key(head, base):
    text = (head / INDEX_REL).read_text(encoding="utf-8")
    write_file(head, INDEX_REL, text.replace('"themes": [', '"themes": [], "themes": [', 1))


def plant_themes_folder_symlink(head, base):
    real = head / "elsewhere.json"
    (head / THEMES_REL / "olympus-dusk" / "theme.json").rename(real)
    os.symlink(real, head / THEMES_REL / "olympus-dusk" / "theme.json")


def symlink_dir(rel):
    def plant(head, base):
        real = head / "elsewhere"
        (head / rel).rename(real)
        os.symlink(real, head / rel)
    return plant


def plant_theme_duplicate_key(head, base):
    text = (head / THEMES_REL / "olympus-dusk" / "theme.json").read_text(encoding="utf-8")
    write_file(head, f"{THEMES_REL}/olympus-dusk/theme.json", text.replace('"schemaVersion": 1,', '"schemaVersion": 1, "schemaVersion": 1,', 1))


def plant_revoked_id_present(head, base):
    entry = {"id": "olympus-dusk", "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"}
    write_json(head, REVOKED_REL, [entry])
    edit_index(lambda d: d.__setitem__("revoked", [entry]))(head, base)


def plant_published_bad_key(head, base):
    data = read_json(head, PUBLISHED_REL)
    data["../x.png"] = "a" * 64
    write_json(head, PUBLISHED_REL, data)


def flip_last_byte(path):
    data = bytearray(path.read_bytes())
    data[-1] ^= 1
    path.write_bytes(bytes(data))
    return bytes(data)


def plant_published_byte_edited(head, base):
    flip_last_byte(head / V1_REL / "olympus-dusk" / "1.0.0" / "preview-light.png")


def plant_published_byte_edited_and_rehashed(head, base):
    # A different, still well-formed preview under a published path, with published.json updated
    # to match: consistent on its own, so only the base comparison can see it.
    rewrite_preview(head, make_png(height=4))


def plant_published_entry_dropped(head, base):
    # A delisted theme's published file and its entry both removed: this tree is consistent on
    # its own; only the base shows that a published file went away.
    (head / V1_REL / "second-theme" / "1.0.0" / "preview-dark.png").unlink()
    published = read_json(head, PUBLISHED_REL)
    del published["second-theme/1.0.0/preview-dark.png"]
    write_json(head, PUBLISHED_REL, published)


def plant_v1_symlink(head, base):
    os.symlink(head / V1_REL / "published.json", head / V1_REL / "olympus-dusk" / "1.0.0" / "link.json")


def plant_index_duplicate_id(head, base):
    edit_index(lambda d: d["themes"].append(json.loads(json.dumps(d["themes"][0]))))(head, base)


def rewrite_preview(repo, png):
    rel = "olympus-dusk/1.0.0/preview-light.png"
    write_file(repo, f"{V1_REL}/{rel}", png)
    published = read_json(repo, PUBLISHED_REL)
    published[rel] = sha256(png)
    write_json(repo, PUBLISHED_REL, published)


def bad_preview(png):
    # The same bad file goes in the base too, so the base rule (published.json only gains
    # entries) stays quiet and the single problem is the PNG rule's own.
    def plant(head, base):
        for repo in (head, base):
            rewrite_preview(repo, png)
    return plant


def png_bad_crc():
    png = bytearray(make_png())
    iend = png.rfind(b"IEND")
    png[iend - 8] ^= 0xFF  # a byte of IDAT's CRC, just before IEND's length field
    return bytes(png)


def png_extra_chunk():
    png = make_png()
    at = png.find(b"IDAT") - 4
    return png[:at] + png_chunk(b"tEXt", b"Comment\0hi") + png[at:]


def png_bad_depth():
    return (PNG_SIGNATURE + png_chunk(b"IHDR", struct.pack(">IIBBBBB", PREVIEW_WIDTH, 2, 3, 0, 0, 0, 0))
            + png_chunk(b"IDAT", zlib.compress(b"\0" * 10)) + png_chunk(b"IEND", b""))


def plant_reused_id(head, base):
    # The base published olympus-dusk and then delisted it (files stay, index entry gone);
    # this tree lists it again.
    edit_index(lambda d: d.__setitem__("themes", []))(base, None)
    shutil.rmtree(base / THEMES_REL / "olympus-dusk")


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


def plant_other_theme_pr_edits_headers(head, base):
    shutil.rmtree(base / THEMES_REL / "olympus-dusk")
    write_file(head, "public/_headers", "/*\n  X-Frame-Options: SAMEORIGIN\n")


def plant_unrevoke(head, base):
    # Only the base's revoked.json has the entry (its index doesn't: an inconsistent base keeps the
    # change to revoked.json alone).
    write_json(base, REVOKED_REL, [{"id": "old-theme", "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"}])


def plant_base_no_index(head, base):
    (base / INDEX_REL).unlink()


def plant_base_no_published(head, base):
    (base / PUBLISHED_REL).unlink()


def plant_base_v1_other_index(head, base):
    """A base whose v1/ holds only an empty index that isn't #141's exact bytes."""
    shutil.rmtree(base / V1_REL)
    shutil.rmtree(base / THEMES_REL)
    write_json(base, INDEX_REL, {"schemaVersion": 1, "generatedAt": "2026-09-01T00:00:00Z", "themes": [], "revoked": []})


def two_themes(repo):
    write_tree(repo, listed=("olympus-dusk", "second-theme"))


def empty_tree(repo):
    write_tree(repo, listed=())


def delisted_tree(repo):
    write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",))


def revoked_tree(repo):
    write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",), revoked=("second-theme",))


def nothing_published_base(repo):
    """A base before any theme work: no themes/, no public/themes/v1/."""
    write_file(repo, "public/_headers", "/*\n  X-Frame-Options: DENY\n")


def pre_144_base(repo):
    """release-1.0.4 before #144: public/themes/v1/ holds only #141's empty index."""
    nothing_published_base(repo)
    write_json(repo, INDEX_REL, {"schemaVersion": 1, "generatedAt": "2026-09-27T00:00:00Z", "themes": [], "revoked": []})


def new_version_head(repo, version="1.0.1"):
    """olympus-dusk moved to `version`: 1.0.0's files stay published, the index points at it."""
    write_tree(repo)
    doc = fixture_theme("olympus-dusk", version=version)
    data = dumps(doc).encode()
    write_file(repo, f"{THEMES_REL}/olympus-dusk/theme.json", data)
    published = read_json(repo, PUBLISHED_REL)
    for name, body in (("theme.json", data), ("preview-light.png", make_png()), ("preview-dark.png", make_png())):
        write_file(repo, f"{V1_REL}/olympus-dusk/{version}/{name}", body)
        published[f"olympus-dusk/{version}/{name}"] = sha256(body)
    write_json(repo, PUBLISHED_REL, dict(sorted(published.items())))
    edit_index(lambda d: d.__setitem__("themes", [index_entry(doc, sha256(data))]))(repo, None)


def rolled_back_head(repo):
    """olympus-dusk back to 1.0.0 from a base at 1.0.1 (1.0.1's files stay published)."""
    new_version_head(repo)
    doc = fixture_theme("olympus-dusk")
    data = dumps(doc).encode()
    write_file(repo, f"{THEMES_REL}/olympus-dusk/theme.json", data)
    edit_index(lambda d: d.__setitem__("themes", [index_entry(doc, sha256(data))]))(repo, None)


MAINTAINER = PR(DEFAULT_MAINTAINER_IDS[0])
BOT = PR(BOT_ID)
OTHER = PR(12345)
PUSH = "push"  # run_case: a base, no PR (a push event)


def pr_with(kind_pr, *labels):
    return PR(kind_pr.author_id, labels)


# (name, plant(head, base), words that must all be in the single problem, [PR context, head
# builder, base builder]). The default tree is one listed theme; the default base is an identical
# copy, and the default PR is the maintainer's, so a plant sees only the rule it breaks.
RULES = [
    # #141's index shape (updated: no theme.css, scenarios, generatedAt format, strict JSON).
    ("missing index.json", plant_missing_index, ["missing", "exists"]),
    ("malformed JSON", plant_malformed_json, ["not valid JSON"]),
    ("index: second 'themes' key", plant_index_second_themes_key, ["not valid JSON", "duplicate key 'themes'"]),
    ("index: unknown top-level key", edit_index(lambda d: d.__setitem__("gallery", 1)), ["unknown top-level key(s) 'gallery'"]),
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
    # Real directories (M3).
    ("dirs: public/themes is a symlink", symlink_dir("public/themes"), ["public/themes: is a symlink or not a directory"]),
    ("dirs: themes/ is a symlink", symlink_dir(THEMES_REL), ["themes: is a symlink or not a directory"]),
    # themes/ (#144 W3 file rules).
    ("themes: symlinked theme.json", plant_themes_folder_symlink, ["is a symlink", "themes/"]),
    ("themes: folder != id", edit_source(lambda d: d.__setitem__("id", "olympus-dawn")), ["doesn't match its folder name"]),
    ("themes: theme.json over 16 KB", edit_source(lambda d: d["summary"].__setitem__("en", "x" * MAX_THEME_BYTES)), ["larger than 16384 bytes"]),
    ("themes: duplicate JSON key", plant_theme_duplicate_key, ["not valid JSON", "duplicate key"]),
    ("themes: version with a non-ASCII digit", edit_source(lambda d: d.__setitem__("version", "1.0.٣")), ["version must be MAJOR.MINOR.PATCH"]),
    ("themes: version with a leading zero (01.0.0)", edit_source(lambda d: d.__setitem__("version", "01.0.0")), ["version must be MAJOR.MINOR.PATCH", "without leading zeros"]),
    ("themes: author.github with a Kelvin sign", edit_source(lambda d: d["author"].__setitem__("github", "\u212aate")), ["author.github must be a GitHub login"]),
    ("themes: scenario listed twice", edit_source(lambda d: d.__setitem__("scenarios", ["agent-review", "agent-review"])), ["themes/olympus-dusk/theme.json", "scenarios must be"]),
    ("themes: built-in id", add_file(f"{THEMES_REL}/dawn/theme.json", dumps(fixture_theme("dawn"))), ["built-in theme's and reserved"]),
    ("themes: folder name not an id", add_file(f"{THEMES_REL}/Olympus/theme.json", dumps(fixture_theme("Olympus"))), ["folder name isn't a theme id"]),
    ("themes: extra file in a theme folder", add_file(f"{THEMES_REL}/olympus-dusk/theme.css", "body{}"), ["holds only theme.json"]),
    ("themes: stray file in themes/", add_file(f"{THEMES_REL}/notes.txt"), ["holds only revoked.json"]),
    ("themes: committed .DS_Store", add_file(f"{THEMES_REL}/olympus-dusk/.DS_Store"), ["themes/olympus-dusk/.DS_Store: a .DS_Store is committed"]),
    ("themes: revoked.json missing", lambda head, base: (head / REVOKED_REL).unlink(), ["revoked.json: missing"]),
    ("themes: revoked.json entry reason not a code", lambda head, base: write_json(head, REVOKED_REL, [{"id": "x", "reason": "Because <b>", "revokedAt": "2026-10-02T08:00:00Z"}]),
     ["reason must be a lowercase-hyphenated code"]),
    # public/themes/v1/ and published.json.
    ("v1: published.json missing", lambda head, base: (head / PUBLISHED_REL).unlink(), ["published.json: missing"]),
    ("v1: published.json key outside <id>/<version>/<file>", plant_published_bad_key, ["published.json: key", "must match"]),
    ("v1: file not listed in published.json", add_file(f"{V1_REL}/olympus-dusk/1.0.0/notes.txt"), ["not listed in published.json"]),
    ("v1: committed .DS_Store", add_file(f"{V1_REL}/.DS_Store"), ["public/themes/v1/.DS_Store: a .DS_Store is committed"]),
    ("v1: listed file gone", lambda head, base: (head / V1_REL / "olympus-dusk" / "1.0.0" / "preview-dark.png").unlink(),
     ["lists olympus-dusk/1.0.0/preview-dark.png, which doesn't exist"]),
    ("v1: edited published byte", plant_published_byte_edited, ["sha256 doesn't match published.json"]),
    ("v1: symlink", plant_v1_symlink, ["is a symlink", "public/themes/v1"]),
    # index <-> themes/ <-> files.
    ("cross: themes/<id>/ not in the index", add_file(f"{THEMES_REL}/new-theme/theme.json", dumps(fixture_theme("new-theme"))),
     ["themes/new-theme/", "not in public/themes/v1/index.json"]),
    ("cross: index entry without themes/<id>/", lambda head, base: shutil.rmtree(head / THEMES_REL / "olympus-dusk"),
     ["listed, but themes/olympus-dusk/theme.json doesn't exist"]),
    ("cross: index field differs from theme.json", edit_entry(lambda t: t["name"].__setitem__("en", "Something Else")), ["doesn't match themes/olympus-dusk/theme.json in name"]),
    ("cross: index sha256 differs", edit_entry(lambda t: t["files"]["theme.json"].__setitem__("sha256", "0" * 64)), ["with the sha256 of themes/olympus-dusk/theme.json"]),
    ("cross: preview path not canonical", edit_entry(lambda t: t["previews"].__setitem__("dark", "olympus-dusk/1.0.0/preview-light.png")), ["previews must be olympus-dusk/1.0.0/preview-light.png and"]),
    ("cross: id listed twice", plant_index_duplicate_id, ["id appears more than once"]),
    ("cross: preview not a PNG", bad_preview(b"GIF89a" + b"\0" * 40), ["doesn't start with a PNG signature"]),
    ("cross: preview wrong width", bad_preview(make_png(width=800)), ["800x2", "must be 1200 wide"]),
    ("cross: preview over 500 KB", bad_preview(make_png(height=430, level=0)), ["at most 512000"]),
    ("cross: preview has bytes after IEND", bad_preview(make_png() + b"\0" * 8), ["has 8 bytes after IEND"]),
    ("cross: preview chunk with a bad CRC", bad_preview(png_bad_crc()), ["chunk 1 (IDAT) has a bad CRC"]),
    ("cross: preview IHDR not 13 bytes", bad_preview(make_png(ihdr_extra=b"\0")), ["IHDR is 14 bytes; it must be 13"]),
    ("cross: preview with a text chunk", bad_preview(png_extra_chunk()), ["type b'tEXt', which isn't allowed"]),
    ("cross: preview bit depth not allowed", bad_preview(png_bad_depth()), ["bit depth 3 / colour type 0"]),
    ("cross: index.revoked != revoked.json", lambda head, base: write_json(head, REVOKED_REL, [{"id": "some-theme", "reason": "validator-bypass", "revokedAt": "2026-10-02T08:00:00Z"}]),
     ["revoked doesn't equal themes/revoked.json"]),
    ("cross: revoked id present", plant_revoked_id_present, ["revoked id 'olympus-dusk' is still published"]),
    # Against the base branch.
    ("base: edited published byte, published.json rehashed", plant_published_byte_edited_and_rehashed, ["only gains entries", "preview-light.png"]),
    ("base: published entry dropped", plant_published_entry_dropped, ["only gains entries", "second-theme/1.0.0/preview-dark.png"], MAINTAINER, delisted_tree),
    ("base: reused id", plant_reused_id, ["delisted or revoked; ids are never reused"]),
    ("base: v1 files but no index.json (fail closed)", plant_base_no_index,
     ["base branch: the base has public/themes/v1/published.json but no readable public/themes/v1/index.json; failing closed"]),
    ("base: published before, no published.json (fail closed)", plant_base_no_published,
     ["base branch: the base has themes/ or public/themes/v1/ but no public/themes/v1/published.json; failing closed"]),
    ("base: v1 with an index that isn't #141's (fail closed)", plant_base_v1_other_index,
     ["base branch: the base has themes/ or public/themes/v1/ but no", "failing closed"]),
    ("base: bot PR changes author.github without the label", edit_base_entry(lambda t: t["author"].__setitem__("github", "someone-else")),
     ["author.github changed from 'someone-else' to 'janedoe'", "a bot PR needs the theme-author-change label"], BOT),
    ("base: lower version (maintainer, no rollback label)", no_plant,
     ["version 1.0.0 is lower than the base's 1.0.1"], MAINTAINER, rolled_back_head, new_version_head),
    ("base: lower version (bot, even with the rollback label)", no_plant,
     ["version 1.0.0 is lower than the base's 1.0.1"], PR(BOT_ID, [ROLLBACK_LABEL]), rolled_back_head, new_version_head),
    # PR authorship classes.
    ("authorship: non-maintainer edits public/themes/v1", base_bytes_differ(INDEX_REL), ["isn't a maintainer and may not change public/themes/v1/"], OTHER),
    ("authorship: non-maintainer edits revoked.json", base_bytes_differ(REVOKED_REL), ["isn't a maintainer and may not change themes/revoked.json"], OTHER),
    ("authorship: non-maintainer un-revokes", plant_unrevoke, ["may not un-revoke old-theme; only a maintainer PR"], OTHER),
    ("authorship: non-maintainer changes two themes", base_without_themes("olympus-dusk", "second-theme"), ["isn't a maintainer and may change at most one themes/<id>/"], OTHER, two_themes),
    ("authorship: non-maintainer edits scripts/", add_file("scripts/check_theme_index.py", "# weakened\n"),
     ["PR author (id 12345) isn't a maintainer and may not change scripts/ or .github/"], OTHER),
    ("authorship: bot edits .github/", add_file(".github/workflows/site.yml", "on: push\n"), ["bot PR may not change scripts/ or .github/"], BOT),
    ("authorship: bot changes a hand-written file", add_file("public/_headers", "/*\n"),
     ["bot PR may change only themes/, public/themes/v1/ and generated pages", "public/_headers"], BOT),
    ("authorship: non-maintainer theme PR changes a hand-written file", plant_other_theme_pr_edits_headers,
     ["PR author (id 12345) may change only themes/, public/themes/v1/ and generated pages", "public/_headers"], OTHER),
    ("authorship: bot changes two themes", base_without_themes("olympus-dusk", "second-theme"), ["bot PR may change at most one themes/<id>/"], BOT, two_themes),
    ("authorship: bot edits revoked.json", base_bytes_differ(REVOKED_REL), ["bot PR may not change themes/revoked.json"], BOT),
    ("authorship: bot un-revokes", plant_unrevoke, ["bot PR may not un-revoke old-theme"], BOT),
    ("authorship: bot edits another theme's files", plant_bot_outside, ["bot PR changes public/themes/v1 files outside", "second-theme"], BOT, two_themes),
]


# Changes that must pass: (name, plant(head, base), PR or PUSH, head builder, base builder).
def passes():
    author_change = edit_base_entry(lambda t: t["author"].__setitem__("github", "someone-else"))
    return [
        ("unbroken tree", no_plant, MAINTAINER, None, None),
        ("empty tree (as published after #144)", no_plant, OTHER, empty_tree, empty_tree),
        ("first publication: base without themes/ or v1/", no_plant, MAINTAINER, empty_tree, nothing_published_base),
        ("first publication: base with only #141's empty index", no_plant, MAINTAINER, empty_tree, pre_144_base),
        ("maintainer multi-theme PR", no_plant, MAINTAINER, two_themes, empty_tree),
        ("bot single-theme PR", no_plant, BOT, two_themes, write_tree),
        ("bot single-theme PR with a generated page", add_file("public/themes/gallery/index.html", "<p>x</p>"), BOT, two_themes, write_tree),
        ("non-maintainer PR outside theme data", add_file("public/_headers", "/*\n"), OTHER, None, None),
        ("maintainer PR editing scripts/", add_file("scripts/check_theme_index.py", "# edited\n"), MAINTAINER, None, None),
        ("delisting PR (maintainer)", no_plant, MAINTAINER, delisted_tree, two_themes),
        ("revocation PR (maintainer)", no_plant, MAINTAINER, revoked_tree, two_themes),
        ("un-revocation PR (maintainer)", plant_unrevoke, MAINTAINER, None, None),
        ("author change: push event A->B", author_change, PUSH, None, None),
        ("author change: maintainer PR without the label", author_change, MAINTAINER, None, None),
        ("author change: bot PR with the label", author_change, pr_with(BOT, AUTHOR_CHANGE_LABEL), None, None),
        ("new version of an existing theme (maintainer)", no_plant, MAINTAINER, new_version_head, write_tree),
        ("rollback: maintainer PR with the label", no_plant, pr_with(MAINTAINER, ROLLBACK_LABEL), rolled_back_head, new_version_head),
        ("rollback: push event", no_plant, PUSH, rolled_back_head, new_version_head),
    ]


def listing(root: Path) -> dict:
    out = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            out[path.relative_to(root).as_posix()] = "link:" + os.readlink(path)
        elif path.is_file():
            out[path.relative_to(root).as_posix()] = git_blob_id(path.read_bytes())
    return out


def run_case(plant, pr, head_builder=None, base_builder=None):
    with tempfile.TemporaryDirectory() as tmp:
        head, base = Path(tmp) / "head", Path(tmp) / "base"
        (head_builder or write_tree)(head)
        base.mkdir(exist_ok=True)
        (base_builder or head_builder or write_tree)(base)
        plant(head, base)
        before, after = listing(base), listing(head)
        changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
        return check(head, Snapshot.from_dir(base), None if pr is PUSH else pr, changed)


def git_env():
    env = dict(os.environ)
    env.update(GIT_AUTHOR_NAME="self-test", GIT_AUTHOR_EMAIL="self-test@example.invalid",
               GIT_COMMITTER_NAME="self-test", GIT_COMMITTER_EMAIL="self-test@example.invalid",
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
    return env


def self_test_git(fail) -> None:
    """The git-backed readers CI uses, on a real temporary repository."""
    if not shutil.which("git"):
        fail("git isn't available; the base reader can't be tested")
        return
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp)
        env = git_env()

        def git(*args):
            return subprocess.run(["git", "-C", str(repo), *args], check=True, env=env,
                                  capture_output=True, text=True).stdout.strip()

        write_tree(repo, listed=("olympus-dusk",), delisted=("second-theme",))
        git("init", "-q")
        git("add", "-A")
        git("commit", "-q", "-m", "base")
        base_sha = git("rev-parse", "HEAD")
        from_git, from_dir = Snapshot.from_git(repo, "HEAD"), Snapshot.from_dir(repo)
        if from_git.entries != from_dir.entries:
            fail("Snapshot.from_git and Snapshot.from_dir disagree on the same tree")
        elif from_git.read(PUBLISHED_REL) != (repo / PUBLISHED_REL).read_bytes():
            fail("Snapshot.from_git reads different bytes than the file on disk")
        elif check(repo, from_git, MAINTAINER):
            fail(f"a tree checked against itself from git should pass, got {check(repo, from_git, MAINTAINER)}")
        if head_matches_git(repo):
            fail(f"a clean checkout should match HEAD, got {head_matches_git(repo)}")
        write_file(repo, f"{THEMES_REL}/olympus-dusk/.DS_Store", "x")  # untracked: disk != HEAD
        found = head_matches_git(repo)
        if len(found) != 1 or "differs from HEAD" not in found[0]:
            fail(f"an untracked file under themes/ should make the checkout differ from HEAD, got {found}")
        else:
            print(f"  ok  ci: untracked file in the checkout: {found[0]}")
        (repo / THEMES_REL / "olympus-dusk" / ".DS_Store").unlink()
        try:
            Snapshot.from_git(repo, "0" * 40)
            fail("an unknown base revision was read instead of failing closed")
        except BaseUnavailable as error:
            print(f"  ok  ci: unknown base revision: {str(error)[:120]}")

        # A PR branch and GitHub's merge commit on top of the base.
        git("checkout", "-q", "-b", "pr")
        write_file(repo, "public/_headers", "/*\n  X-Frame-Options: SAMEORIGIN\n")
        git("commit", "-q", "-am", "pr")
        pr_sha = git("rev-parse", "HEAD")
        git("checkout", "-q", "--detach", base_sha)
        git("merge", "-q", "--no-ff", "-m", "merge", pr_sha)
        event = {"pull_request": {"user": {"id": 12345}, "head": {"sha": pr_sha}, "labels": []}}

        def no_fetch(r, sha):  # the objects are local here
            return sha

        base, pr, changed = ci_context(repo, "pull_request", event, "", fetch=no_fetch)
        if base.entries != Snapshot.from_git(repo, base_sha).entries or pr.kind != "other" or changed != ["public/_headers"]:
            fail(f"ci_context on a merge commit: wrong base/PR/changes ({pr.kind}, {changed})")
        else:
            print("  ok  ci: merge commit -> base is its first parent, changes are repo-wide")
        cases = (
            ("PR head isn't the merge's second parent", lambda e: e["pull_request"]["head"].__setitem__("sha", base_sha), "isn't the PR head", ""),
            ("payload without user.id", lambda e: e["pull_request"].pop("user"), "lacks user.id", ""),
            ("non-numeric maintainer id", lambda e: None, "isn't a GitHub numeric user id", "redtear1115"),
        )
        for name, mutate, words, maintainers in cases:
            bad = json.loads(json.dumps(event))
            mutate(bad)
            try:
                ci_context(repo, "pull_request", bad, maintainers, fetch=no_fetch)
                fail(f"ci_context: {name} didn't fail closed")
            except BaseUnavailable as error:
                if words not in str(error):
                    fail(f"ci_context: {name}: wanted {words!r}, got {error}")
                else:
                    print(f"  ok  ci: {name}: {error}")
        git("checkout", "-q", "--detach", base_sha)  # not a merge commit
        try:
            ci_context(repo, "pull_request", event, "", fetch=no_fetch)
            fail("ci_context on a non-merge HEAD didn't fail closed")
        except BaseUnavailable as error:
            if "two-parent merge commit" not in str(error):
                fail(f"ci_context on a non-merge HEAD: wrong message {error}")
            else:
                print(f"  ok  ci: HEAD isn't a merge commit: {error}")


def self_test() -> int:
    failures = 0

    def fail(message):
        nonlocal failures
        print(f"self-test: {message}")
        failures += 1

    # No public/themes/v1/ at all: mandatory, with its own words.
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

    # The bootstrap fixture must be #141's exact blob, or the first-publication case tests nothing.
    with tempfile.TemporaryDirectory() as tmp:
        pre_144_base(Path(tmp))
        if git_blob_id((Path(tmp) / INDEX_REL).read_bytes()) != BOOTSTRAP_INDEX_BLOB:
            fail("the pre-#144 fixture index isn't BOOTSTRAP_INDEX_BLOB")

    for name, plant, pr, head_builder, base_builder in passes():
        problems = run_case(plant, pr, head_builder, base_builder)
        if problems:
            fail(f"{name!r} should pass, got {problems}")
        else:
            print(f"  ok  passes: {name}")

    for rule in RULES:
        name, plant, words = rule[:3]
        pr = rule[3] if len(rule) > 3 else MAINTAINER
        head_builder = rule[4] if len(rule) > 4 else None
        base_builder = rule[5] if len(rule) > 5 else None
        problems = run_case(plant, pr, head_builder, base_builder)
        if len(problems) != 1:
            fail(f"planted {name!r}; wanted exactly 1 problem, got {problems}")
        elif not all(word in problems[0] for word in words):
            fail(f"planted {name!r}; wanted {words!r} in the single problem, got {problems[0]!r}")
        else:
            print(f"  ok  {name}: {problems[0]}")

    # The rev-3 case stated as the real PR shape: a non-maintainer adding published themes.
    problems = run_case(no_plant, OTHER, two_themes, empty_tree)
    if not any("isn't a maintainer and may not change public/themes/v1/" in p for p in problems):
        fail(f"a non-maintainer adding two published themes should fail on public/themes/v1, got {problems}")

    self_test_git(fail)

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

def run(args) -> int:
    if args.self_test:
        return self_test()

    repo = Path(args.repo).resolve()
    base = pr = changed = None
    problems = []
    try:
        if args.ci:
            event_path = os.environ.get("GITHUB_EVENT_PATH", "")
            try:
                event = json.loads(Path(event_path).read_text(encoding="utf-8"))
            except (OSError, ValueError) as error:
                raise BaseUnavailable(f"can't read the event payload ({error})") from error
            base, pr, changed = ci_context(repo, os.environ.get("GITHUB_EVENT_NAME", ""), event,
                                           os.environ.get("THEME_MAINTAINER_IDS"))
            problems += head_matches_git(repo)
        elif args.base:
            base = Snapshot.from_git(repo, args.base)
    except BaseUnavailable as error:
        print(f"::error::base branch: {error}; failing closed")
        return 1

    problems += check(repo, base, pr, changed)
    for problem in problems:
        print(f"::error::{problem}")
    if not problems:
        scope = "against the base" + (f", PR author class {pr.kind}" if pr else "") if base else "this tree only"
        print(f"check_theme_index: ok ({scope})")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=str(ROOT), help="repository root (default: this script's)")
    parser.add_argument("--base", help="compare against this local revision (no PR rules)")
    parser.add_argument("--ci", action="store_true", help="GitHub Actions: fetch the base, apply PR rules")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        return run(args)
    except Exception as error:  # a crash is a failure with a readable reason, never a pass
        print(f"::error::check_theme_index.py crashed: {type(error).__name__}: {error}")
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
