#!/usr/bin/env python3
"""The kit CLI for the submission workflows' macOS jobs (#143; plan-website-104 W2, F7).

    kit_cli.py key                 # prints key=<cache key>: the pinned kit commit, nothing else
    kit_cli.py build  --dir DIR    # build marsdawn at the pinned commit into DIR (a cache miss)
    kit_cli.py verify --dir DIR    # check DIR before any use; prints bin=<path to marsdawn>

`build` is scripts/sync_theme_kit.py's own build (build_cli: a detached worktree of the pinned
KIT_SHA, `swift build -c release --only-use-versions-from-resolved-file`), from a fresh clone of the
kit's public repository; this adds no second way to build it. It copies the binary and the resource
bundles SwiftPM puts beside it (Bundle.module finds them next to the executable) into DIR/bin, and
records DIR/tree.sha256: one hash over every file's path, mode and sha256 there.

`verify` runs before the binary is used, whether DIR was just built or restored from the Actions
cache: the tree hash must equal the recorded one (a partial or altered restore fails), `marsdawn
--version` must equal the vendored contract's cli_version (vendor/kit-themes/<sha12>/manifest.json,
as build_themes.py requires), and the same smoke test sync_theme_kit.py runs must pass. The cache key
is the kit commit plus the runner's OS and architecture (the workflow adds those).

What the recorded hash does and doesn't prove: it's written by the job that built the binary, into
the same cache entry, so it detects corruption and a restore that doesn't match what was saved; it
isn't an independent attestation against a writer that could create that cache entry itself. Cache
entries are immutable once created and are only created by the kit-building steps of workflows on
the default branch (see .github/workflows/theme-*.yml).
"""
import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import sync_theme_kit as kit  # noqa: E402

ROOT = common.ROOT
VENDOR = ROOT / "vendor" / "kit-themes" / kit.KIT_SHA[:12]
KIT_CLONE_URL = kit.KIT_REPO_URL + ".git"


class KitError(RuntimeError):
    pass


def cache_key() -> str:
    return f"theme-kit-cli-v1-{kit.KIT_SHA}"


def tree_hash(root: Path) -> str:
    """sha256 over every entry under root, sorted: kind, mode bits, path and content hash (or link
    target). Any added, removed, renamed, re-moded or changed file changes it."""
    digest = hashlib.sha256()
    entries = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        for name in dirnames + filenames:
            entries.append(Path(dirpath) / name)
    for path in sorted(entries, key=lambda p: p.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix().encode("utf-8")
        info = os.lstat(path)
        if stat.S_ISLNK(info.st_mode):
            digest.update(b"L\0" + rel + b"\0" + os.readlink(path).encode("utf-8") + b"\n")
        elif stat.S_ISDIR(info.st_mode):
            digest.update(b"D\0" + rel + b"\n")
        elif stat.S_ISREG(info.st_mode):
            mode = b"x" if info.st_mode & 0o111 else b"-"
            digest.update(b"F\0" + mode + b"\0" + rel + b"\0" + hashlib.sha256(path.read_bytes()).hexdigest().encode() + b"\n")
        else:
            raise KitError(f"{rel.decode()}: not a file, folder or link")
    return digest.hexdigest()


def expected_version() -> str:
    return json.loads((VENDOR / "manifest.json").read_text(encoding="utf-8"))["cli_version"]


def build(dest: Path) -> None:
    if dest.exists():
        raise KitError(f"{dest} already exists")
    scratch = Path(tempfile.mkdtemp(prefix="theme-kit-clone-"))
    repo = scratch / "kit"
    worktree = None
    try:
        kit.run(["git", "clone", "--quiet", "--no-checkout", "--filter=blob:none", KIT_CLONE_URL, str(repo)])
        worktree, binary = kit.build_cli(repo, kit.KIT_SHA)
        release = binary.parent
        (dest / "bin").mkdir(parents=True)
        shutil.copy2(binary, dest / "bin" / "marsdawn")
        bundles = sorted(p for p in release.iterdir() if p.suffix == ".bundle" and p.is_dir())
        if not bundles:
            raise KitError(f"no resource bundles beside {binary}")
        for bundle in bundles:
            shutil.copytree(bundle, dest / "bin" / bundle.name, symlinks=True)
        (dest / "tree.sha256").write_text(tree_hash(dest / "bin") + "\n", encoding="utf-8")
    finally:
        if worktree is not None:
            kit.remove_worktree(repo, worktree)
        shutil.rmtree(scratch, ignore_errors=True)


def verify(dest: Path) -> Path:
    bin_dir, recorded = dest / "bin", dest / "tree.sha256"
    if bin_dir.is_symlink() or not bin_dir.is_dir() or recorded.is_symlink() or not recorded.is_file():
        raise KitError(f"{dest}: no bin/ folder and tree.sha256 file")
    want = recorded.read_text(encoding="utf-8").strip()
    got = tree_hash(bin_dir)
    if not common.SHA256_RE.fullmatch(want) or got != want:
        raise KitError(f"{dest}: the kit CLI's tree hash is {got}, but {want!r} was recorded when it was built")
    binary = bin_dir / "marsdawn"
    info = os.lstat(binary)
    if not stat.S_ISREG(info.st_mode) or not info.st_mode & 0o100:
        raise KitError(f"{binary}: not an executable regular file")
    version = subprocess.run([str(binary), "--version"], capture_output=True, text=True, timeout=60)
    if version.returncode != 0 or version.stdout.strip() != expected_version():
        raise KitError(f"marsdawn --version says {version.stdout.strip()!r}; the vendored contract at "
                       f"{kit.KIT_SHA[:12]} was made with {expected_version()!r}")
    kit.smoke_test(binary, VENDOR / "Themes" / "dawn" / "theme.json")
    return binary


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("key", "build", "verify"))
    parser.add_argument("--dir", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "key":
            common.write_outputs({"key": cache_key()})
            return 0
        if args.dir is None:
            raise KitError("--dir is required")
        if args.command == "build":
            build(args.dir)
            print(f"built marsdawn at {kit.KIT_SHA} into {args.dir}")
            return 0
        binary = verify(args.dir)
        common.write_outputs({"bin": str(binary)})
        print(f"marsdawn at {kit.KIT_SHA[:12]}: tree hash, version and smoke test ok")
        return 0
    except (KitError, kit.SyncError, OSError, subprocess.SubprocessError, ValueError) as err:
        common.error(f"kit CLI: {err}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
