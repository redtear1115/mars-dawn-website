#!/usr/bin/env python3
"""The first job of every theme submission workflow (#143; plan-website-104 W2). Ubuntu, no token
permissions beyond reading this public repo; runs no third-party code.

    gate.py submission --out DIR   # theme-submission.yml: issue opened/edited
    gate.py approve    --out DIR   # theme-approve.yml:    issue labeled
    gate.py from-pr    --out DIR   # theme-from-pr.yml:    workflow_dispatch with PR_NUMBER

Each reads the event from $GITHUB_EVENT_PATH (never from `${{ github.event.* }}` in a shell line),
reads the issue or PR fresh through the API with $GH_TOKEN, and decides. The theme's exact bytes go
to DIR/theme.json (uploaded as an artifact by the workflow) and its sha256 to the job's outputs,
where the next job checks the file against it. Outputs are closed-grammar tokens only
(common.write_outputs).

submission -> action=skip (closed, not a submission, theme unchanged since the last validation) |
reject (reason=too-large/no-theme/json/dco; the comment job says why) | validate.

approve -> action=skip (a label other than theme-approved, or a sender outside the maintainer id
allowlist: nothing happens) | build. Anything else is refused: an ::error:: naming the rule and exit
1, and no pull request. The rules: issue open and labelled theme-submission; body parses; DCO still
ticked; the theme's sha256 equals the sha256 in the latest bot validation comment and that comment's
verdict is valid; author.github equals the issue opener's login (ASCII case-insensitively) unless the
issue has the theme-author-change label; id and version in the site's grammar, id not a built-in's.

from-pr -> build, or refused as above. The sender must be in the maintainer allowlist; PR_NUMBER a
plain integer; the PR open, on this repository, changing exactly one path, themes/<id>/theme.json
(added or modified), whose blob at the PR head is mode 100644, at most 16 KB, and has the blob id the
files API reported; author.github equals the PR author's login unless the PR has theme-author-change;
every commit on the PR carries a Signed-off-by whose email is the PR author's (their noreply
address, or the commit's own author email when GitHub attributes that commit to the PR author). The
PR's code is never checked out or run: only that one blob is read, as data.
"""
import argparse
import base64
import hashlib
import os
import re
import sys
import traceback
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
from common import Refusal, rules  # noqa: E402

THEME_PATH_RE = re.compile(r"themes/([a-z0-9]+(?:-[a-z0-9]+)*)/theme\.json")


def issue_number(event: dict) -> int:
    issue = event.get("issue")
    number = issue.get("number") if isinstance(issue, dict) else None
    if not common.int_not_bool(number) or number <= 0:
        raise Refusal("input", "the event has no issue number")
    return number


def base_branch() -> str:
    """THEME_BASE_BRANCH (repo variable) names the branch bot PRs target: main by default, since the
    issue workflows only ever run from the default branch; a release-<version> branch while one
    collects a milestone's PRs."""
    value = os.environ.get("THEME_BASE_BRANCH", "").strip() or "main"
    if not common.BASE_BRANCH_RE.fullmatch(value):
        raise Refusal("input", "THEME_BASE_BRANCH must be main or release-<version>")
    return value


def publishable(doc: dict) -> tuple:
    """(id, version) of a theme the build could publish, by the site's grammar. The kit decides
    everything else, in the build job."""
    tid, version = doc.get("id"), doc.get("version")
    if not rules.is_theme_id(tid) or tid in rules.RESERVED_IDS:
        raise Refusal("id", "The theme's id isn't a publishable id (lowercase words joined by single hyphens, "
                            "at most 32 characters, not a built-in theme's).")
    if not rules.is_version(version):
        raise Refusal("version", "The theme's version isn't MAJOR.MINOR.PATCH (ASCII numbers, no leading zeros).")
    return tid, version


def write_theme(out: Path, data: bytes) -> None:
    out.mkdir(parents=True, exist_ok=True)
    target = out / "theme.json"
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    with os.fdopen(fd, "wb") as handle:
        handle.write(data)


# --- theme-submission.yml -------------------------------------------------------------------------

def submission(api, event: dict, out: Path) -> dict:
    number = issue_number(event)
    issue = api.get(f"/repos/{{repo}}/issues/{number}")
    if not isinstance(issue, dict) or "pull_request" in issue:
        return {"action": "skip", "reason": "not-an-issue", "number": number}
    if issue.get("state") != "open":
        return {"action": "skip", "reason": "closed", "number": number}
    if common.SUBMISSION_LABEL not in common.label_names(issue):
        return {"action": "skip", "reason": "not-a-submission", "number": number}
    login, _ = common.user_of(issue)
    try:
        data, _doc, ticked = common.parse_submission(issue.get("body"))
        if not ticked:
            raise Refusal("dco", "The Developer Certificate of Origin box isn't ticked.")
    except Refusal as refusal:
        return {"action": "reject", "reason": refusal.code, "number": number}
    digest = common.sha256(data)
    found = common.validation_comments(common.issue_comments(api, number))
    if found:
        _, verdict, sha = found[-1]
        if sha == digest and verdict in ("valid", "invalid"):
            return {"action": "skip", "reason": "unchanged", "number": number, "sha256": digest}
    write_theme(out, data)
    return {"action": "validate", "reason": "changed", "number": number, "sha256": digest, "opener": login}


# --- theme-approve.yml ----------------------------------------------------------------------------

def approve(api, event: dict, maintainers: set, out: Path) -> dict:
    number = issue_number(event)
    label = event.get("label")
    if not isinstance(label, dict) or label.get("name") != common.APPROVED_LABEL:
        return {"action": "skip", "reason": "other-label", "number": number}
    sender = event.get("sender")
    sender_id = sender.get("id") if isinstance(sender, dict) else None
    if not common.int_not_bool(sender_id) or sender_id not in maintainers:
        return {"action": "skip", "reason": "sender-not-maintainer", "number": number}

    issue = api.get(f"/repos/{{repo}}/issues/{number}")
    if not isinstance(issue, dict) or "pull_request" in issue:
        raise Refusal("state", f"#{number} isn't an issue")
    if issue.get("state") != "open":
        raise Refusal("state", f"#{number} is closed; only an open submission can be approved")
    labels = common.label_names(issue)
    if common.SUBMISSION_LABEL not in labels:
        raise Refusal("state", f"#{number} doesn't have the {common.SUBMISSION_LABEL} label")
    login, uid = common.user_of(issue)
    data, doc, ticked = common.parse_submission(issue.get("body"))
    if not ticked:
        raise Refusal("dco", f"#{number}: the Developer Certificate of Origin box isn't ticked any more")
    digest = common.sha256(data)

    found = common.validation_comments(common.issue_comments(api, number))
    if not found:
        raise Refusal("hash", f"#{number} has no validation comment from {common.BOT_LOGIN}; wait for it, then label again")
    _, verdict, sha = found[-1]
    if sha != digest:
        raise Refusal("hash", f"#{number}: the theme's sha256 is {digest}, but the latest validation comment is for "
                              f"{sha or 'no theme'}; the issue was edited after it was validated. Wait for the new "
                              f"validation comment, then remove and add {common.APPROVED_LABEL} again")
    if verdict != "valid":
        raise Refusal("verdict", f"#{number}: the latest validation comment (sha256 {digest}) says {verdict}, not valid")

    author_change = common.AUTHOR_CHANGE_LABEL in labels
    if not author_change and not common.author_matches(doc, login):
        raise Refusal("author", f"#{number}: author.github isn't the login of the account that opened the issue "
                                f"({login}); add {common.AUTHOR_CHANGE_LABEL} if that is intended")
    tid, version = publishable(doc)
    write_theme(out, data)
    return {"action": "build", "source": "issue", "number": number, "sha256": digest, "theme_id": tid,
            "version": version, "login": login, "user_id": uid,
            "author_change": "true" if author_change else "false", "base_branch": base_branch()}


# --- theme-from-pr.yml ----------------------------------------------------------------------------

def tree_entry(api, tree_sha: str, name: str, kind: str) -> dict:
    if not common.COMMIT_RE.fullmatch(tree_sha or ""):
        raise Refusal("pr-tree", "a tree id from the API isn't a SHA-1")
    tree = api.get(f"/repos/{{repo}}/git/trees/{tree_sha}")
    entries = [e for e in (tree or {}).get("tree", []) if isinstance(e, dict) and e.get("path") == name]
    if len(entries) != 1 or entries[0].get("type") != kind:
        raise Refusal("pr-tree", f"the PR head has no single {kind} {name!r} where expected")
    return entries[0]


def signoff_ok(item: dict, login: str, uid: int) -> bool:
    """A Signed-off-by trailer by the PR author: its email is the author's noreply address, or the
    commit's own author email when GitHub attributes the commit to the PR author's account."""
    commit = item.get("commit") if isinstance(item, dict) else None
    message = commit.get("message") if isinstance(commit, dict) else None
    if not isinstance(message, str):
        return False
    allowed = {common.ascii_lower(common.noreply(login, uid)),
               common.ascii_lower(f"{login}@users.noreply.github.com")}
    gh_author = item.get("author")
    git_author = commit.get("author")
    if (isinstance(gh_author, dict) and gh_author.get("id") == uid and isinstance(git_author, dict)
            and isinstance(git_author.get("email"), str)):
        allowed.add(common.ascii_lower(git_author["email"]))
    for match in re.finditer(r"^Signed-off-by: [^\n<>]+ <([^<>\s]+)>[ \t]*$", message, re.MULTILINE):
        if common.ascii_lower(match.group(1)) in allowed:
            return True
    return False


def from_pr(api, event: dict, pr_text: str, maintainers: set, out: Path) -> dict:
    sender = event.get("sender")
    sender_id = sender.get("id") if isinstance(sender, dict) else None
    if not common.int_not_bool(sender_id) or sender_id not in maintainers:
        raise Refusal("sender", "only a maintainer (THEME_MAINTAINER_IDS) may run theme-from-pr")
    if not common.NUMBER_RE.fullmatch(pr_text or ""):
        raise Refusal("input", "the pr input must be a plain pull request number")
    number = int(pr_text)

    pr = api.get(f"/repos/{{repo}}/pulls/{number}")
    if not isinstance(pr, dict) or pr.get("state") != "open":
        raise Refusal("pr-state", f"PR #{number} isn't open")
    base_repo = ((pr.get("base") or {}).get("repo") or {}).get("full_name")
    if base_repo != api.repo:
        raise Refusal("pr-state", f"PR #{number} isn't a pull request into this repository")
    login, uid = common.user_of(pr)
    head_sha = (pr.get("head") or {}).get("sha")
    if not common.COMMIT_RE.fullmatch(head_sha or ""):
        raise Refusal("pr-state", f"PR #{number}: the head isn't a commit id")

    files = api.paginate(f"/repos/{{repo}}/pulls/{number}/files", 30)
    if len(files) != 1:
        raise Refusal("pr-files", f"PR #{number} changes {len(files)} paths; a theme PR changes exactly one, "
                                  f"themes/<id>/theme.json")
    entry = files[0] if isinstance(files[0], dict) else {}
    match = THEME_PATH_RE.fullmatch(entry.get("filename") or "")
    if not match or entry.get("status") not in ("added", "modified"):
        raise Refusal("pr-files", f"PR #{number}: the one changed path must be an added or modified themes/<id>/theme.json")
    folder = match.group(1)
    blob_sha = entry.get("sha")

    commit = api.get(f"/repos/{{repo}}/git/commits/{head_sha}")
    tree_sha = ((commit or {}).get("tree") or {}).get("sha")
    themes_tree = tree_entry(api, tree_sha, "themes", "tree")
    folder_tree = tree_entry(api, themes_tree.get("sha"), folder, "tree")
    blob_entry = tree_entry(api, folder_tree.get("sha"), "theme.json", "blob")
    if blob_entry.get("mode") != "100644":
        raise Refusal("pr-blob", f"PR #{number}: themes/{folder}/theme.json must be a regular file (mode 100644), "
                                 f"not a link or executable")
    if blob_entry.get("sha") != blob_sha or not common.COMMIT_RE.fullmatch(blob_sha or ""):
        raise Refusal("pr-blob", f"PR #{number}: the tree and the files list disagree about theme.json")
    size = blob_entry.get("size")
    if not common.int_not_bool(size) or size > common.MAX_THEME_BYTES:
        raise Refusal("pr-blob", f"PR #{number}: theme.json is larger than {common.MAX_THEME_BYTES} bytes")
    blob = api.get(f"/repos/{{repo}}/git/blobs/{blob_sha}")
    if not isinstance(blob, dict) or blob.get("encoding") != "base64" or not isinstance(blob.get("content"), str):
        raise Refusal("pr-blob", f"PR #{number}: theme.json couldn't be read as a blob")
    data = base64.b64decode(blob["content"], validate=False)
    if len(data) > common.MAX_THEME_BYTES or rules.git_blob_id(data) != blob_sha:
        raise Refusal("pr-blob", f"PR #{number}: theme.json's bytes don't match its blob id")
    try:
        doc = rules.strict_json(data)
    except (ValueError, UnicodeDecodeError):
        doc = None
    if not isinstance(doc, dict):
        raise Refusal("json", f"PR #{number}: theme.json isn't one valid JSON object (or it repeats a key)")
    tid, version = publishable(doc)
    if tid != folder:
        raise Refusal("id", f"PR #{number}: the theme's id isn't its folder name {folder}")

    labels = common.label_names(pr)
    author_change = common.AUTHOR_CHANGE_LABEL in labels
    if not author_change and not common.author_matches(doc, login):
        raise Refusal("author", f"PR #{number}: author.github isn't the PR author's login ({login}); add "
                                f"{common.AUTHOR_CHANGE_LABEL} to the PR if that is intended")

    count = pr.get("commits")
    if not common.int_not_bool(count) or count > common.MAX_PR_COMMITS:
        raise Refusal("dco", f"PR #{number} has more than {common.MAX_PR_COMMITS} commits; squash it first")
    commits = api.paginate(f"/repos/{{repo}}/pulls/{number}/commits", 3)
    if not commits or len(commits) != count:
        raise Refusal("dco", f"PR #{number}: its commit list couldn't be read whole")
    unsigned = [str(c.get("sha", ""))[:12] for c in commits if not signoff_ok(c, login, uid)]
    if unsigned:
        shown = ", ".join(s for s in unsigned if re.fullmatch(r"[0-9a-f]{12}", s))
        raise Refusal("dco", f"PR #{number}: commit(s) {shown} have no Signed-off-by from the PR author ({login}); "
                             f"sign off every commit (git commit -s) with your GitHub noreply address or an "
                             f"email GitHub links to your account")

    write_theme(out, data)
    return {"action": "build", "source": "pr", "number": number, "sha256": common.sha256(data), "theme_id": tid,
            "version": version, "login": login, "user_id": uid,
            "author_change": "true" if author_change else "false", "base_branch": base_branch()}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("mode", choices=("submission", "approve", "from-pr"))
    parser.add_argument("--out", type=Path, required=True, help="where theme.json is written")
    args = parser.parse_args(argv)
    try:
        api = common.GitHub.from_env()
        event = common.load_event()
        if args.mode == "submission":
            outputs = submission(api, event, args.out)
        elif args.mode == "approve":
            outputs = approve(api, event, common.maintainers(), args.out)
        else:
            outputs = from_pr(api, event, os.environ.get("PR_NUMBER", ""), common.maintainers(), args.out)
    except Refusal as refusal:
        common.error(f"refused ({refusal.code}): {refusal.message}")
        return 1
    except common.ApiError as err:
        common.error(f"GitHub API: {err} -- failing closed")
        return 1
    except Exception as err:  # a crash is a failure with a readable reason, never a pass
        common.error(f"gate.py crashed: {type(err).__name__}")
        traceback.print_exc()
        return 1
    common.write_outputs(outputs)
    print(f"gate {args.mode}: action={outputs['action']} reason={outputs.get('reason', '-')}")
    if outputs["action"] == "skip":
        common.notice(f"theme {args.mode}: nothing to do ({outputs['reason']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
