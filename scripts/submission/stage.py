#!/usr/bin/env python3
"""The build job of theme-pr.yml (#143; plan-website-104 W2). macOS, no token permissions, kit CLI
from kit_cli.py; runs on a checkout of the target branch with no credentials in its git config.

    SOURCE=issue|pr NUMBER=<n> GATE_SHA256=<hex> THEME_ID=<id> VERSION=<v> AUTHOR_CHANGE=true|false \
        BASE_SHA=<commit> stage.py --theme theme.json --bin MARSDAWN --out DIR

The checkout must be exactly BASE_SHA, the base-branch tip the gate resolved (review H1).
build_themes.py's output is echoed between ::stop-commands:: markers (review L3).

1. The gate's theme.json must have the gate's sha256, id and version.
2. It's written to themes/<id>/theme.json and **committed** locally first (build_themes.py needs
   themes/ committed: index.json's generatedAt is that commit's time), with a fixed bot identity
   and a recorded commit time.
3. scripts/build_themes.py --marsdawn-bin runs the kit's validator again on those bytes, renders the
   previews, writes index.json, published.json and the pages, and runs check_theme_index.py on the
   result. --allow-author-change is passed only when the gate saw the theme-author-change label.
4. Every path that differs from the target branch must be one a bot PR for this id and version may
   change (common.bot_path_kind), added or modified (never deleted), within its size cap. Those files
   go to DIR/files/<path>, listed with their sha256 and size in DIR/manifest.json together with the
   target commit and the commit time; the manifest's own sha256 is the job's output, which the commit
   job checks before trusting anything in the artifact.
"""
import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
from common import Refusal, rules  # noqa: E402

ROOT = common.ROOT


def git(*args, env=None) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise Refusal("git", f"git {args[0]} failed: {result.stderr.strip()[:500]}")
    return result.stdout


def read_regular(path: Path, cap: int) -> bytes:
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise Refusal("input", f"{path.name}: not a regular file")
        data = os.read(fd, cap + 1)
        while len(data) <= cap:
            more = os.read(fd, cap + 1 - len(data))
            if not more:
                break
            data += more
    finally:
        os.close(fd)
    if len(data) > cap:
        raise Refusal("input", f"{path.name}: over {cap} bytes")
    return data


def gate_values() -> dict:
    return {
        "source": common.env_token("SOURCE", re.compile(r"issue|pr")),
        "number": int(common.env_token("NUMBER", common.NUMBER_RE)),
        "sha256": common.env_token("GATE_SHA256", common.SHA256_RE),
        "theme_id": common.env_token("THEME_ID", rules.ID_RE),
        "version": common.env_token("VERSION", rules.VERSION_RE),
        "author_change": common.env_token("AUTHOR_CHANGE", re.compile(r"true|false")) == "true",
        "base_sha": common.env_token("BASE_SHA", common.COMMIT_RE),
    }


def write_source(tid: str, data: bytes) -> None:
    for part in (ROOT / rules.THEMES_REL, ROOT / rules.THEMES_REL / tid):
        if part.is_symlink() or (part.exists() and not part.is_dir()):
            raise Refusal("path", f"{part.relative_to(ROOT)} is a link or not a folder")
    (ROOT / rules.THEMES_REL / tid).mkdir(exist_ok=True)
    target = ROOT / rules.THEMES_REL / tid / "theme.json"
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, "wb") as handle:
        handle.write(data)


def bot_env(epoch: int) -> dict:
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": common.BOT_NAME, "GIT_AUTHOR_EMAIL": common.BOT_EMAIL,
                "GIT_COMMITTER_NAME": common.BOT_NAME, "GIT_COMMITTER_EMAIL": common.BOT_EMAIL,
                "GIT_AUTHOR_DATE": f"{epoch} +0000", "GIT_COMMITTER_DATE": f"{epoch} +0000",
                "PYTHONDONTWRITEBYTECODE": "1"})
    return env


def changed_against(base: str) -> list:
    """[(status, path)] for everything that differs from `base`, the working tree included."""
    git("add", "-A")
    out = git("diff", "--cached", "--name-status", "-z", "--no-renames", base)
    parts = [p for p in out.split("\0") if p]
    if len(parts) % 2:
        raise Refusal("git", "git diff --name-status output didn't pair up")
    return [(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)]


def stage(theme: Path, binary: Path, out: Path, values: dict, build_cmd=None) -> dict:
    data = read_regular(theme, common.MAX_THEME_BYTES)
    if common.sha256(data) != values["sha256"]:
        raise Refusal("hash", "the theme artifact isn't the one the gate approved (sha256 differs)")
    doc = rules.strict_json(data)
    tid, version = values["theme_id"], values["version"]
    if not isinstance(doc, dict) or doc.get("id") != tid or doc.get("version") != version:
        raise Refusal("input", "the theme's id or version isn't the gate's")

    base = git("rev-parse", "HEAD").strip()
    if base != values["base_sha"]:
        raise Refusal("git", "the checkout isn't the base commit the gate resolved")
    if git("status", "--porcelain", "--untracked-files=all").strip():
        raise Refusal("git", "the checkout isn't clean")

    epoch = int(time.time())
    write_source(tid, data)
    git("add", "--", f"{rules.THEMES_REL}/{tid}/theme.json")
    git("commit", "--quiet", "--no-verify", "-m", f"Stage theme {tid} {version}", env=bot_env(epoch))

    cmd = build_cmd or [sys.executable, str(ROOT / "scripts" / "build_themes.py"), "--marsdawn-bin", str(binary)]
    if values["author_change"]:
        cmd += ["--allow-author-change", tid]
    build = subprocess.run(cmd, cwd=str(ROOT), env=bot_env(epoch), timeout=1500, capture_output=True, text=True)
    common.echo_untrusted(build.stdout + build.stderr)
    if build.returncode != 0:
        raise Refusal("build", f"build_themes.py refused or failed (exit {build.returncode}); see its output above")

    files = {}
    for status, path in changed_against(base):
        if status not in ("A", "M"):
            raise Refusal("path", f"the build {'deleted' if status == 'D' else 'changed the type of'} {path}")
        kind = common.bot_path_kind(path, tid, version)
        if kind is None:
            raise Refusal("path", f"the build changed {path}, which a bot theme PR may not change")
        body = read_regular(ROOT / path, common.SIZE_CAPS[kind])
        files[path] = {"sha256": common.sha256(body), "size": len(body)}
        target = out / "files" / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
    missing = sorted(common.required_paths(tid, version) - set(files))
    if missing:
        raise Refusal("path", f"the build didn't produce {', '.join(missing)} (already published, or nothing to add)")

    manifest = {"schema": 1, "source": values["source"], "number": values["number"], "base": base,
                "epoch": epoch, "theme_id": tid, "version": version, "sha256": values["sha256"],
                "files": dict(sorted(files.items()))}
    text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    (out / "manifest.json").write_text(text, encoding="utf-8")
    return {"manifest_sha256": common.sha256(text.encode("utf-8")), "epoch": epoch}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--theme", type=Path, required=True)
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.out.exists():
            shutil.rmtree(args.out)
        args.out.mkdir(parents=True)
        outputs = stage(args.theme, args.bin, args.out, gate_values())
    except (Refusal, ValueError, OSError, subprocess.SubprocessError) as err:
        message = err.message if isinstance(err, Refusal) else type(err).__name__
        common.error(f"stage refused: {message}")
        return 1
    common.write_outputs(outputs)
    print(f"staged {len(json.loads((args.out / 'manifest.json').read_text())['files'])} file(s); "
          f"manifest sha256 {outputs['manifest_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
