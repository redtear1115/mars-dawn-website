#!/usr/bin/env python3
"""Publishes themes/ to public/themes/v1/ (#144; plan-website-104 W3). macOS: runs the kit CLI.

    python3 scripts/build_themes.py                      # builds the pinned kit CLI first
    python3 scripts/build_themes.py --marsdawn-bin PATH  # reuse a CLI built at the pinned commit

For every themes/<id>/theme.json (see scripts/check_theme_index.py for the whole contract):

1. Read it once: a regular file, never through a symlink (O_NOFOLLOW, then fstat), at most 16 KB,
   in a folder named by a valid, non-built-in id. Those exact bytes go to a private temporary file,
   and everything after this step -- the kit's verdict, the copy, the previews -- uses that file,
   so what is validated is what is published.
2. `marsdawn theme validate --require-complete --json` on those bytes: the kit is the authority on
   validity (plan Envelope). The id it reports must equal the folder name.
3. Re-check the id and version against the kit's grammar here too, and the rest of the rules
   check_theme_index.py holds CI to (scenarios, author, a revoked or reused id, author.github
   binding) -- the build refuses anything CI would.
4. Publish `<id>/<version>/`: theme.json plus preview-light.png and preview-dark.png from
   `marsdawn theme preview --width 1200`, **only if that version isn't published yet**. A version
   already in HEAD's published.json is never re-rendered or rewritten; its source bytes must equal
   what was published (bump the version to change a theme).
5. Write published.json (HEAD's entries plus this build's new ones: append-only), index.json
   (sorted by id; `revoked` from themes/revoked.json), then run build_pages.py, then
   check_theme_index.py on the result.

"Published" means in the published.json **committed at HEAD**. Entries only the working tree has
are this build's own pending output: a rerun drops and regenerates them (and deletes their files),
so fixing a theme before committing needs no manual cleanup, while nothing HEAD has published can
be touched. Every write target is resolved and must lie inside public/themes/v1/; files are
created with O_EXCL|O_NOFOLLOW, never through an existing link.

themes/ must be committed first (`git status` clean for themes/): `generatedAt` is the committer
time of the newest commit touching themes/, so the output is a function of HEAD alone and a rerun
on the committed result changes nothing.

Delisting: remove themes/<id>/, commit, rerun. The entry leaves the index; published files and
their published.json entries stay, and the id can never be listed again. Revocation: also add
{id, reason, revokedAt} to themes/revoked.json.

The kit CLI is WA's: scripts/sync_theme_kit.py's KIT_SHA, built by its own build_cli (a detached
worktree of a local kit clone, `swift build --only-use-versions-from-resolved-file`) and
smoke-tested by its own smoke_test; this script adds no second way to build it.
"""
import argparse
import datetime
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import check_theme_index as rules  # noqa: E402
import sync_theme_kit as kit  # noqa: E402

THEMES = ROOT / rules.THEMES_REL
V1 = ROOT / rules.V1_REL


class BuildError(RuntimeError):
    pass


def git(*args) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise BuildError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def head_json(rel: str, default):
    """A JSON file as committed at HEAD; `default` only when HEAD doesn't have it at all."""
    listed = git("ls-tree", "--name-only", "HEAD", "--", rel).strip()
    if not listed:
        return default
    try:
        return rules.strict_json(git("show", f"HEAD:{rel}").encode("utf-8"))
    except ValueError as error:
        raise BuildError(f"HEAD:{rel} isn't valid JSON ({error})") from error


def generated_at() -> str:
    stamp = git("log", "-1", "--format=%ct", "HEAD", "--", rules.THEMES_REL).strip()
    if not stamp:
        raise BuildError("no commit touches themes/ yet; commit themes/revoked.json first")
    moment = datetime.datetime.fromtimestamp(int(stamp), tz=datetime.timezone.utc)
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def read_theme_file(path: Path) -> bytes:
    """The file's bytes, read once through O_NOFOLLOW and checked to be a regular file of at most
    MAX_THEME_BYTES -- the kit's own reader rules, applied here so the bytes handed to it are the
    ones this script then publishes."""
    for parent in (THEMES, path.parent):
        if parent.is_symlink() or not parent.is_dir():
            raise BuildError(f"{parent.relative_to(ROOT)}: is a symlink or not a folder")
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError as error:
        raise BuildError(f"{path.relative_to(ROOT)}: can't be opened without following a link ({error})") from error
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise BuildError(f"{path.relative_to(ROOT)}: isn't a regular file")
        data = b""
        while len(data) <= rules.MAX_THEME_BYTES:
            chunk = os.read(fd, rules.MAX_THEME_BYTES + 1 - len(data))
            if not chunk:
                break
            data += chunk
    finally:
        os.close(fd)
    if len(data) > rules.MAX_THEME_BYTES:
        raise BuildError(f"{path.relative_to(ROOT)}: larger than {rules.MAX_THEME_BYTES} bytes")
    return data


def run_cli(binary: Path, *args) -> subprocess.CompletedProcess:
    try:
        return subprocess.run([str(binary), *args], capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise BuildError(f"marsdawn {' '.join(args)}: {error}") from error


def kit_validate(binary: Path, file: Path, folder: str) -> None:
    result = run_cli(binary, "theme", "validate", "--require-complete", "--json", str(file))
    try:
        report = json.loads(result.stdout)
    except ValueError:
        raise BuildError(f"themes/{folder}/theme.json: marsdawn theme validate exited {result.returncode} "
                         f"without JSON: {result.stderr.strip()!r}")
    if result.returncode != 0 or report.get("ok") is not True:
        issues = "; ".join(f"{i.get('rule')} at {i.get('path') or '/'}: {i.get('message')}" for i in report.get("issues", []))
        raise BuildError(f"themes/{folder}/theme.json: the kit refuses it (exit {result.returncode}): {issues}")
    if report.get("id") != folder:
        raise BuildError(f"themes/{folder}/theme.json: the kit validated id {report.get('id')!r}, not {folder!r}")


def render_preview(binary: Path, file: Path, appearance: str, out: Path) -> bytes:
    result = run_cli(binary, "theme", "preview", str(file), "--appearance", appearance, "-o", str(out),
                     "--width", str(rules.PREVIEW_WIDTH), "--json")
    if result.returncode != 0:
        raise BuildError(f"marsdawn theme preview {appearance} exited {result.returncode}: "
                         f"{result.stdout.strip()} {result.stderr.strip()}")
    data = out.read_bytes()
    size = rules.png_size(data)
    if size is None or size[0] != rules.PREVIEW_WIDTH or not 1 <= size[1] <= rules.PREVIEW_MAX_HEIGHT:
        raise BuildError(f"{out.name}: not a {rules.PREVIEW_WIDTH}-wide PNG ({size})")
    if len(data) > rules.MAX_PREVIEW_BYTES:
        raise BuildError(f"{out.name}: {len(data)} bytes; previews are at most {rules.MAX_PREVIEW_BYTES}")
    return data


def v1_target(rel: str) -> Path:
    """public/themes/v1/<rel>, refusing anything that resolves elsewhere or passes through a link."""
    if not rules.path_is_safe(rel):
        raise BuildError(f"{rel!r}: not a safe path")
    root = V1.resolve()
    target = V1 / rel
    current = V1
    for part in Path(rel).parts[:-1]:
        current = current / part
        if current.is_symlink():
            raise BuildError(f"{current.relative_to(ROOT)}: is a symlink")
    resolved = target.parent.resolve() / target.name
    try:
        resolved.relative_to(root)
    except ValueError:
        raise BuildError(f"{rel}: resolves outside {rules.V1_REL}")
    return resolved


def write_new(rel: str, data: bytes) -> None:
    target = v1_target(rel)
    target.parent.mkdir(parents=True, exist_ok=True)
    v1_target(rel)  # again, after mkdir: nothing on the way may have become a link
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, "wb") as handle:
        handle.write(data)


def write_generated(rel: str, text: str) -> None:
    """index.json and published.json: replaced atomically, never written through a link."""
    target = v1_target(rel)
    tmp = target.with_name(f".{target.name}.tmp")
    if tmp.exists() or tmp.is_symlink():
        tmp.unlink()
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.replace(tmp, target)


def scan_v1() -> dict:
    """{rel: path} for every file under public/themes/v1/; any link there stops the build."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(V1, followlinks=False):
        for name in dirnames + filenames:
            full = Path(dirpath) / name
            rel = full.relative_to(V1).as_posix()
            if full.is_symlink():
                raise BuildError(f"{rules.V1_REL}/{rel}: is a symlink; remove it")
            if name in filenames and name != ".DS_Store":
                found[rel] = full
    return found


def collect(binary: Path, work: Path, published: dict, previous: dict, revoked_ids: set,
            author_changes: set) -> list:
    """Validates every theme and returns [(doc, data, private_copy)] sorted by id. Raises
    BuildError listing every problem found (all themes are checked before anything is written)."""
    problems = []
    snap = rules.Snapshot.from_dir(ROOT)
    rules.check_sources(problems, snap)
    if problems:
        raise BuildError("\n".join(problems))
    ever_published = {k.split("/", 1)[0] for k in published}
    out = []
    for folder in sorted(p.name for p in THEMES.iterdir() if p.is_dir() and not p.is_symlink()):
        try:
            data = read_theme_file(THEMES / folder / "theme.json")
            copy = work / folder / "theme.json"
            copy.parent.mkdir()
            copy.write_bytes(data)
            kit_validate(binary, copy, folder)
            doc = rules.strict_json(data)
            if not rules.is_theme_id(doc["id"]) or doc["id"] != folder or folder in rules.RESERVED_IDS:
                raise BuildError(f"themes/{folder}/theme.json: id {doc['id']!r} isn't a publishable id for this folder")
            if not rules.is_version(doc["version"]):
                raise BuildError(f"themes/{folder}/theme.json: version {doc['version']!r} isn't MAJOR.MINOR.PATCH")
            if folder in revoked_ids:
                raise BuildError(f"themes/{folder}/: id {folder!r} is revoked; it can't be published")
            if folder in ever_published and folder not in previous:
                raise BuildError(f"themes/{folder}/: id {folder!r} was published before and delisted or revoked; ids are never reused")
            old = previous.get(folder)
            if old is not None and folder not in author_changes:
                entry = rules.index_entry(doc, "")
                if rules.github_of(old) != rules.github_of(entry):
                    raise BuildError(f"themes/{folder}/: author.github changed from {rules.github_of(old)!r}; "
                                     f"pass --allow-author-change {folder} only with the {rules.AUTHOR_CHANGE_LABEL} label")
            rel = f"{folder}/{doc['version']}/theme.json"
            if rel in published and published[rel] != rules.sha256(data):
                raise BuildError(f"themes/{folder}/theme.json: version {doc['version']} is already published with "
                                 f"different bytes; published files never change, so bump the version")
            out.append((doc, data, copy))
        except BuildError as error:
            problems.append(str(error))
    if problems:
        raise BuildError("\n".join(problems))
    return out


def build(binary: Path, author_changes: set) -> None:
    if git("status", "--porcelain", "--", rules.THEMES_REL).strip():
        raise BuildError("themes/ has uncommitted changes; commit them first (generatedAt is the "
                         "newest themes/ commit's time, so the build depends on HEAD alone)")
    if not V1.is_dir() or V1.is_symlink():
        raise BuildError(f"{rules.V1_REL}: missing or a symlink")

    published = head_json(rules.PUBLISHED_REL, None)
    head_index = head_json(rules.INDEX_REL, {})
    if published is None:
        if head_index.get("themes"):
            raise BuildError(f"HEAD lists themes but has no {rules.PUBLISHED_REL}; refusing to guess what was published")
        published = {}
    if not isinstance(published, dict):
        raise BuildError(f"HEAD:{rules.PUBLISHED_REL} isn't an object")
    previous = {t["id"]: t for t in head_index.get("themes", []) if isinstance(t, dict) and "id" in t}

    problems = []
    revoked = rules.check_revoked_source(problems, rules.Snapshot.from_dir(ROOT))
    if revoked is None:
        raise BuildError("\n".join(problems))

    on_disk = scan_v1()
    # Everything HEAD published must be on disk, unchanged, before anything is written.
    for rel, digest in sorted(published.items()):
        path = on_disk.get(rel)
        if path is None or rules.sha256(path.read_bytes()) != digest:
            raise BuildError(f"{rules.V1_REL}/{rel}: missing or changed since it was published; restore it from HEAD")

    with tempfile.TemporaryDirectory(prefix="build-themes-") as tmp:
        work = Path(tmp)
        themes = collect(binary, work, published, previous, {r["id"] for r in revoked}, author_changes)

        new_files = {}
        for doc, data, copy in themes:
            base = f"{doc['id']}/{doc['version']}/"
            if base + "theme.json" in published:
                for name in rules.FILE_NAMES:
                    if base + name not in published:
                        raise BuildError(f"{base}{name}: HEAD published {base}theme.json without it")
                print(f"{doc['id']} {doc['version']}: already published, not re-rendered")
                continue
            new_files[base + "theme.json"] = data
            for appearance in ("light", "dark"):
                png = render_preview(binary, copy, appearance, work / f"{doc['id']}-{appearance}.png")
                new_files[f"{base}preview-{appearance}.png"] = png
            print(f"{doc['id']} {doc['version']}: validated and rendered")

        # Pending output from an earlier, uncommitted run: never published, so drop it.
        for rel in sorted(set(on_disk) - set(published) - {"index.json", "published.json"}):
            v1_target(rel).unlink()
        for dirpath, dirnames, filenames in os.walk(V1, topdown=False):
            if Path(dirpath) != V1 and not os.listdir(dirpath):
                os.rmdir(dirpath)

        for rel, data in sorted(new_files.items()):
            write_new(rel, data)

    all_published = dict(published)
    all_published.update({rel: rules.sha256(data) for rel, data in new_files.items()})
    index = {
        "schemaVersion": 1,
        "generatedAt": generated_at(),
        "themes": [rules.index_entry(doc, rules.sha256(data)) for doc, data, _ in themes],
        "revoked": revoked,
    }
    write_generated("published.json", rules.dumps(dict(sorted(all_published.items()))))
    write_generated("index.json", rules.dumps(index))
    print(f"{rules.INDEX_REL}: {len(index['themes'])} theme(s), {len(revoked)} revoked, "
          f"{len(new_files)} new file(s), generatedAt {index['generatedAt']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--kit-repo", type=Path, default=kit.DEFAULT_KIT_REPO,
                        help="local clone of mars-dawn-kit to build the pinned commit from")
    parser.add_argument("--marsdawn-bin", type=Path, default=None,
                        help="a marsdawn built at the pinned commit, inside its build tree")
    parser.add_argument("--allow-author-change", action="append", default=[], metavar="ID",
                        help=f"let this id's author.github change (only with the {rules.AUTHOR_CHANGE_LABEL} label)")
    args = parser.parse_args()

    built_worktree = None
    try:
        if args.marsdawn_bin:
            binary = args.marsdawn_bin
            version = run_cli(binary, "--version")
            if version.returncode != 0:
                raise BuildError(f"{binary}: --version failed")
        else:
            if not args.kit_repo.is_dir():
                raise BuildError(f"{args.kit_repo} isn't a directory; pass --kit-repo")
            print(f"Building marsdawn at {kit.KIT_SHA} from {args.kit_repo} ...")
            built_worktree, binary = kit.build_cli(args.kit_repo, kit.KIT_SHA)
        kit.smoke_test(binary, ROOT / "vendor" / "kit-themes" / kit.KIT_SHA[:12] / "Themes" / "dawn" / "theme.json")
        build(binary, set(args.allow_author_change))
    except (BuildError, kit.SyncError) as error:
        for line in str(error).splitlines():
            print(f"::error::{line}", file=sys.stderr)
        return 1
    finally:
        if built_worktree is not None:
            kit.remove_worktree(args.kit_repo, built_worktree)

    pages = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_pages.py")], capture_output=True, text=True)
    if pages.returncode != 0:
        print(f"::error::build_pages.py failed:\n{pages.stderr}", file=sys.stderr)
        return 1
    print("build_pages.py: pages regenerated")

    problems = rules.check(ROOT)
    for problem in problems:
        print(f"::error::{problem}", file=sys.stderr)
    if problems:
        return 1
    print("check_theme_index.py: ok on the result")
    return 0


if __name__ == "__main__":
    sys.exit(main())
