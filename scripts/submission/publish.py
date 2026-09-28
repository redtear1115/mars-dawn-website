#!/usr/bin/env python3
"""The commit job of theme-pr.yml (#143; plan-website-104 W2). Ubuntu; the only job with write
scopes (contents, pull-requests, issues); runs nothing but this repository's own Python and git --
no kit, no build, no third-party code. The checkout keeps no credentials; the token is handed to the
one `git push` through the environment only.

    SOURCE, NUMBER, GATE_SHA256, THEME_ID, VERSION, LOGIN, USER_ID, AUTHOR_CHANGE, BASE_BRANCH,
    BASE_SHA, MANIFEST_SHA256 (job outputs, re-checked here), GH_TOKEN, GITHUB_REPOSITORY
    publish.py --staged DIR [--dry-run]

1. The artifact's manifest.json must hash to the build job's MANIFEST_SHA256 and agree with the
   gate's values; every file in it must be exactly the files under DIR/files (regular files, no
   links), each with its recorded sha256 and size, on a path a bot PR for this id and version may
   change, within its size cap; previews are whole PNGs of the preview width; themes/<id>/theme.json
   and the published copy are both exactly the gate's bytes; index.json lists this id at this version
   with that sha256, and published.json records the three new files.
2. Those files are written onto a checkout of BASE_SHA, and staged; the staged set must equal the
   manifest's. One commit, by github-actions[bot]'s noreply identity, at the build's commit time (so
   index.json's generatedAt stays the newest themes/ commit's time), message from a file
   (`git commit -F`) holding only the id, version, the issue or PR number, sha256s, the DCO line and
   `Co-authored-by: <login> <<id>+<login>@users.noreply.github.com>`.
3. Pushed to refs/heads/theme/issue-<n> (or theme/pr-<n>) and nowhere else; a pull request into
   BASE_BRANCH is opened (or its body refreshed), labelled theme-author-change when the gate saw that
   label. PR title and body hold no display strings (no name, summary or author name): only the id,
   version, numbers and hashes. Then the issue gets a comment pointing at the PR, or, for a git
   user's PR, that PR gets a comment crediting its author and is closed.

A PR opened with GITHUB_TOKEN starts no workflows: a maintainer closes and reopens it to run
`check` (plan F5; no PAT, no actions: write). The diff and the previews are the review gate.
"""
import argparse
import base64
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
from common import Refusal, rules  # noqa: E402

ROOT = common.ROOT
MAX_MANIFEST_BYTES = 256 * 1024


def values_from_env() -> dict:
    return {
        "source": common.env_token("SOURCE", re.compile(r"issue|pr")),
        "number": int(common.env_token("NUMBER", common.NUMBER_RE)),
        "sha256": common.env_token("GATE_SHA256", common.SHA256_RE),
        "theme_id": common.env_token("THEME_ID", rules.ID_RE),
        "version": common.env_token("VERSION", rules.VERSION_RE),
        "login": common.env_token("LOGIN", common.LOGIN_RE),
        "user_id": int(common.env_token("USER_ID", common.USER_ID_RE)),
        "author_change": common.env_token("AUTHOR_CHANGE", re.compile(r"true|false")) == "true",
        "base_branch": common.env_token("BASE_BRANCH", common.BASE_BRANCH_RE),
        "base_sha": common.env_token("BASE_SHA", common.COMMIT_RE),
        "manifest_sha256": common.env_token("MANIFEST_SHA256", common.SHA256_RE),
    }


def read_regular(path: Path, cap: int) -> bytes:
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise Refusal("artifact", f"{path.name}: not a regular file")
        data = b""
        while len(data) <= cap:
            more = os.read(fd, cap + 1 - len(data))
            if not more:
                break
            data += more
    finally:
        os.close(fd)
    if len(data) > cap:
        raise Refusal("artifact", f"{path.name}: over its size cap")
    return data


def staged_files(files_dir: Path) -> list:
    """Every path under files_dir; any link, or anything but folders and regular files, refuses."""
    found = []
    for dirpath, dirnames, filenames in os.walk(files_dir, followlinks=False):
        for name in dirnames + filenames:
            full = Path(dirpath) / name
            mode = os.lstat(full).st_mode
            if stat.S_ISLNK(mode):
                raise Refusal("artifact", "the artifact holds a symbolic link")
            if name in filenames:
                if not stat.S_ISREG(mode):
                    raise Refusal("artifact", "the artifact holds something that isn't a regular file")
                found.append(full.relative_to(files_dir).as_posix())
            elif not stat.S_ISDIR(mode):
                raise Refusal("artifact", "the artifact holds something that isn't a folder")
    return sorted(found)


def verify_artifact(staged: Path, values: dict, now=None) -> tuple:
    """(manifest, {path: bytes}) once every rule in step 1 holds."""
    raw = read_regular(staged / "manifest.json", MAX_MANIFEST_BYTES)
    if common.sha256(raw) != values["manifest_sha256"]:
        raise Refusal("artifact", "manifest.json isn't the one the build job produced (sha256 differs)")
    manifest = json.loads(raw.decode("utf-8"))
    tid, version = values["theme_id"], values["version"]
    expected = {"schema": 1, "source": values["source"], "number": values["number"], "base": values["base_sha"],
                "theme_id": tid, "version": version, "sha256": values["sha256"]}
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise Refusal("artifact", f"manifest.json's {key} isn't the gate's")
    epoch = manifest.get("epoch")
    now = int(time.time()) if now is None else now
    if not common.int_not_bool(epoch) or not now - 6 * 3600 <= epoch <= now + 300:
        raise Refusal("artifact", "manifest.json's commit time isn't from this run")
    listed = manifest.get("files")
    if not isinstance(listed, dict) or set(manifest) != set(expected) | {"epoch", "files"}:
        raise Refusal("artifact", "manifest.json has unexpected keys")

    on_disk = staged_files(staged / "files")
    if on_disk != sorted(listed):
        raise Refusal("artifact", "the artifact's files aren't exactly the manifest's")
    contents = {}
    for path in on_disk:
        kind = common.bot_path_kind(path, tid, version)
        if kind is None:
            raise Refusal("path", f"{path}: not a path a bot theme PR for {tid} {version} may change")
        entry = listed[path]
        data = read_regular(staged / "files" / path, common.SIZE_CAPS[kind])
        if not isinstance(entry, dict) or entry.get("sha256") != common.sha256(data) or entry.get("size") != len(data):
            raise Refusal("artifact", f"{path}: its bytes aren't the manifest's")
        if kind == "preview":
            problem, size = rules.png_info(data)
            if problem or size[0] != rules.PREVIEW_WIDTH or not 1 <= size[1] <= rules.PREVIEW_MAX_HEIGHT:
                raise Refusal("artifact", f"{path}: not a whole PNG {rules.PREVIEW_WIDTH} pixels wide")
        contents[path] = data
    missing = sorted(common.required_paths(tid, version) - set(contents))
    if missing:
        raise Refusal("artifact", f"the artifact lacks {', '.join(missing)}")

    source = contents[f"{rules.THEMES_REL}/{tid}/theme.json"]
    v1 = f"{rules.V1_REL}/{tid}/{version}/"
    if common.sha256(source) != values["sha256"] or contents[v1 + "theme.json"] != source:
        raise Refusal("artifact", "the theme files aren't exactly the gate's bytes")
    index = rules.strict_json(contents[rules.INDEX_REL])
    entries = [t for t in index.get("themes", []) if isinstance(t, dict) and t.get("id") == tid]
    if (len(entries) != 1 or entries[0].get("version") != version
            or ((entries[0].get("files") or {}).get("theme.json") or {}).get("sha256") != values["sha256"]):
        raise Refusal("artifact", f"index.json doesn't list {tid} {version} with the gate's sha256")
    published = rules.strict_json(contents[rules.PUBLISHED_REL])
    for name in rules.FILE_NAMES:
        if published.get(f"{tid}/{version}/{name}") != common.sha256(contents[v1 + name]):
            raise Refusal("artifact", f"published.json doesn't record {tid}/{version}/{name}")
    return manifest, contents


def git(*args, env=None, check=True) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, env=env)
    if check and result.returncode != 0:
        raise Refusal("git", f"git {args[0]} failed: {result.stderr.strip()[:500]}")
    return result.stdout


def commit_message(values: dict, contents: dict) -> str:
    tid, version, n = values["theme_id"], values["version"], values["number"]
    v1 = f"{rules.V1_REL}/{tid}/{version}/"
    where = f"#{n}" if values["source"] == "issue" else f"PR #{n}"
    dco = (f"DCO confirmed in #{n} by {values['login']}" if values["source"] == "issue"
           else f"DCO: Signed-off-by in PR #{n}")
    lines = [
        f"Add theme {tid} {version}",
        "",
        f"Theme: {tid} {version}",
        f"Submission: {where}",
        f"themes/{tid}/theme.json sha256: {values['sha256']}",
        f"preview-light.png sha256: {common.sha256(contents[v1 + 'preview-light.png'])}",
        f"preview-dark.png sha256: {common.sha256(contents[v1 + 'preview-dark.png'])}",
        dco,
        "",
        f"Co-authored-by: {values['login']} <{common.noreply(values['login'], values['user_id'])}>",
    ]
    return "\n".join(lines) + "\n"


def branch_ref(values: dict) -> str:
    ref = f"refs/heads/theme/{values['source']}-{values['number']}"
    if not common.PUSH_REF_RE.fullmatch(ref):
        raise Refusal("git", "refusing to push anywhere but refs/heads/theme/(issue|pr)-<n>")
    return ref


def write_tree(contents: dict) -> None:
    for path, data in sorted(contents.items()):
        target = ROOT / path
        current = ROOT
        for part in Path(path).parts[:-1]:
            current = current / part
            if current.is_symlink() or (current.exists() and not current.is_dir()):
                raise Refusal("path", f"{current.relative_to(ROOT)} is a link or not a folder")
            current.mkdir(exist_ok=True)
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o644)
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)


def make_commit(values: dict, manifest: dict, contents: dict) -> str:
    head = git("rev-parse", "HEAD").strip()
    if head != values["base_sha"]:
        raise Refusal("git", "the checkout isn't the build's base commit")
    if git("status", "--porcelain", "--untracked-files=all").strip():
        raise Refusal("git", "the checkout isn't clean")
    write_tree(contents)
    git("add", "--", *sorted(contents))
    staged = sorted(p for p in git("diff", "--cached", "--name-only", "-z").split("\0") if p)
    if staged != sorted(contents):
        raise Refusal("git", "the staged paths aren't exactly the manifest's")
    epoch = manifest["epoch"]
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": common.BOT_NAME, "GIT_AUTHOR_EMAIL": common.BOT_EMAIL,
                "GIT_COMMITTER_NAME": common.BOT_NAME, "GIT_COMMITTER_EMAIL": common.BOT_EMAIL,
                "GIT_AUTHOR_DATE": f"{epoch} +0000", "GIT_COMMITTER_DATE": f"{epoch} +0000"})
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as handle:
        handle.write(commit_message(values, contents))
        message_file = handle.name
    try:
        git("-c", "commit.gpgsign=false", "commit", "--quiet", "--no-verify", "--cleanup=verbatim",
            "-F", message_file, env=env)
    finally:
        os.unlink(message_file)
    if git("log", "-1", "--format=%ct").strip() != str(epoch):
        raise Refusal("git", "the commit's time isn't the build's")
    return git("rev-parse", "HEAD").strip()


def push(values: dict, token: str, repo: str) -> None:
    """One `git push` with the token in an http.extraheader passed through GIT_CONFIG_* (never in
    argv, never written to .git/config), to the one allowed ref."""
    ref = branch_ref(values)
    header = base64.b64encode(f"x-access-token:{token}".encode()).decode()
    print(f"::add-mask::{header}")
    env = dict(os.environ)
    env.update({"GIT_CONFIG_COUNT": "2",
                "GIT_CONFIG_KEY_0": "http.https://github.com/.extraheader",
                "GIT_CONFIG_VALUE_0": f"AUTHORIZATION: basic {header}",
                "GIT_CONFIG_KEY_1": "credential.helper", "GIT_CONFIG_VALUE_1": "",
                "GIT_TERMINAL_PROMPT": "0"})
    git("push", "--force", "--no-verify", f"https://github.com/{repo}.git", f"HEAD:{ref}", env=env)


def pr_text(values: dict, contents: dict) -> tuple:
    tid, version, n = values["theme_id"], values["version"], values["number"]
    v1 = f"{rules.V1_REL}/{tid}/{version}/"
    origin = f"submission issue #{n}" if values["source"] == "issue" else f"pull request #{n}"
    title = f"Theme {tid} {version} ({'#' if values['source'] == 'issue' else 'from PR #'}{n})"
    body = "\n".join([
        f"Adds theme `{tid}` {version} from {origin}, built by the theme submission workflow.",
        "",
        f"- `themes/{tid}/theme.json` sha256 `{values['sha256']}`",
        f"- `preview-light.png` sha256 `{common.sha256(contents[v1 + 'preview-light.png'])}`",
        f"- `preview-dark.png` sha256 `{common.sha256(contents[v1 + 'preview-dark.png'])}`",
        "",
        "Review the theme file, both previews and the index entry: they are the review gate. A pull "
        "request opened by the workflow token starts no workflows, so **close and reopen this pull "
        "request to run `check`**, and merge only when it's green.",
        "",
    ])
    return title, body


def open_pr(api, values: dict, contents: dict) -> tuple:
    """(pr number, created?) for the bot branch's open PR into BASE_BRANCH."""
    title, body = pr_text(values, contents)
    owner = api.repo.split("/")[0]
    branch = branch_ref(values)[len("refs/heads/"):]
    existing = api.get(f"/repos/{{repo}}/pulls?state=open&head={owner}:{branch}")
    existing = [p for p in existing or [] if isinstance(p, dict) and ((p.get("head") or {}).get("ref") == branch)]
    if existing:
        number = existing[0].get("number")
        if not common.int_not_bool(number):
            raise common.ApiError(0, "the open PR has no number")
        api.request("PATCH", f"/repos/{{repo}}/pulls/{number}", {"title": title, "body": body,
                                                                "base": values["base_branch"]})
        created = False
    else:
        pr = api.request("POST", "/repos/{repo}/pulls", {"title": title, "head": branch, "base": values["base_branch"],
                                                         "body": body, "maintainer_can_modify": False})
        number = (pr or {}).get("number")
        if not common.int_not_bool(number):
            raise common.ApiError(0, "the new PR has no number")
        created = True
    if values["author_change"]:
        api.request("POST", f"/repos/{{repo}}/issues/{number}/labels", {"labels": [common.AUTHOR_CHANGE_LABEL]})
    return number, created


def follow_up(api, values: dict, pr_number: int, created: bool) -> None:
    n = values["number"]
    if values["source"] == "issue":
        verb = "opened" if created else "updated"
        api.request("POST", f"/repos/{{repo}}/issues/{n}/comments", {"body": (
            f"Approved: pull request #{pr_number} was {verb} with this theme, and you as co-author. It's "
            f"published once it's reviewed and merged.")})
        return
    api.request("POST", f"/repos/{{repo}}/issues/{n}/comments", {"body": (
        f"Thanks! This theme continues in #{pr_number}, built from this pull request's theme.json with you as "
        f"co-author (DCO: your Signed-off-by here). Closing this one in its favour.")})
    api.request("PATCH", f"/repos/{{repo}}/pulls/{n}", {"state": "closed"})


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--staged", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true", help="verify and commit, but don't push or call the API")
    args = parser.parse_args(argv)
    try:
        values = values_from_env()
        manifest, contents = verify_artifact(args.staged, values)
        sha = make_commit(values, manifest, contents)
        print(f"committed {sha} with {len(contents)} file(s)")
        if args.dry_run:
            return 0
        api = common.GitHub.from_env()
        push(values, api.token, api.repo)
        pr_number, created = open_pr(api, values, contents)
        follow_up(api, values, pr_number, created)
        print(f"pull request #{pr_number} {'opened' if created else 'updated'}")
    except (Refusal, ValueError, OSError, subprocess.SubprocessError) as err:
        message = err.message if isinstance(err, Refusal) else type(err).__name__
        common.error(f"publish refused: {message}")
        return 1
    except common.ApiError as err:
        common.error(f"GitHub API: {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
