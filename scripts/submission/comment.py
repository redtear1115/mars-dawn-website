#!/usr/bin/env python3
"""The comment job of theme-submission.yml (#143; plan-website-104 W2). Ubuntu, `issues: write`
only, runs nothing but this repository's own Python (no third-party code, no kit).

    NUMBER=<n> GATE_ACTION=reject|validate GATE_REASON=<code> GATE_SHA256=<hex> \
        comment.py [--result result.json]

Writes the submission's one validation comment, or updates it in place: the comment authored by
github-actions[bot] (id, login and type all checked) whose first line is the marker

    <!-- marsdawn-theme-validation v1 verdict=<valid|invalid|rejected|error> sha256=<hex|none> -->

theme-approve.yml approves only the theme whose sha256 is in the latest such comment with verdict
valid. Everything outside the fence is fixed text, numbers, a hex digest or a closed-grammar token;
the kit's messages (which can quote the submission) are only ever inside one fenced block, fenced
longer than any backtick run in them, and cut inside the fence so the closing fence always stays.
A result.json that is missing, malformed, or for another sha256 than the gate's makes the verdict
"error": the comment never claims more than the gate's own digest proves.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

MAX_RESULT_BYTES = 1024 * 1024
FENCE_LIMIT = 20000

REJECTIONS = {
    "too-large": f"The issue body is larger than {common.MAX_BODY_BYTES} bytes, so the theme wasn't read. "
                 f"Submitting from the simulator keeps a theme well under that.",
    "no-theme": f"No theme was found in the **{common.THEME_HEADING}** field. Use **Submit** in the simulator "
                f"({common.SIMULATOR_URL}) so the field is filled in, or paste the theme's JSON into that field.",
    "json": f"The **{common.THEME_HEADING}** field isn't one valid JSON object (or it repeats a key). "
            f"Paste the JSON exactly as the simulator exports it.",
    "dco": f"Tick the **{common.DCO_HEADING}** box by editing this issue; the theme is checked once it's ticked.",
}


def marker(verdict: str, sha) -> str:
    line = f"<!-- marsdawn-theme-validation v1 verdict={verdict} sha256={sha or 'none'} -->"
    assert common.MARKER_RE.fullmatch(line)
    return line


def load_result(path, expected_sha: str):
    """The validate job's result.json, or None when it can't vouch for exactly expected_sha."""
    if path is None:
        return None
    path = Path(path)
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_RESULT_BYTES:
            return None
        result = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if (not isinstance(result, dict) or result.get("schema") != 1 or result.get("sha256") != expected_sha
            or result.get("verdict") not in ("valid", "invalid", "error") or not isinstance(result.get("issues"), list)
            or not common.fullmatch(common.COMMIT_RE, result.get("kit"))):
        return None
    for issue in result["issues"]:
        if not isinstance(issue, dict) or not all(isinstance(issue.get(k), str) for k in ("rule", "path", "message")):
            return None
    return result


def issue_lines(issues: list) -> str:
    lines = []
    for issue in issues:
        where = f" at {issue['path']}" if issue["path"] else ""
        lines.append(f"{issue['message']}  [{issue['rule']}{where}]")
    return "\n".join(lines)


def body_for(action: str, reason: str, sha, result) -> str:
    if action == "reject":
        text = REJECTIONS.get(reason, "The submission couldn't be read.")
        return "\n".join([marker("rejected", None), "**Theme check: not run.**", "", text, ""])
    if result is None or result["verdict"] == "error":
        return "\n".join([
            marker("error", sha), "**Theme check: couldn't run.**", "",
            "The validator didn't produce a result for this theme. That's a problem with the workflow, not "
            "necessarily with your theme; a maintainer will look at the run. Editing the issue tries again.", "",
            f"Theme sha256: `{sha}`", ""])
    kit = result["kit"][:12]
    if result["verdict"] == "valid":
        lines = [
            marker("valid", sha), "**Theme check: passed.**", "",
            f"The kit's validator (`marsdawn theme validate --require-complete`, kit `{kit}`) and the gallery's "
            f"publishing rules accept this theme.", "",
            f"Validated theme sha256: `{sha}`", "",
            "A maintainer will review the look, the name, the summary and the author line. If you edit the "
            "theme, it's checked again, and only the version with the sha256 above can be approved.",
        ]
        if not result.get("authorMatchesOpener"):
            lines += ["", "Note: `author.github` in the theme isn't the GitHub account that opened this issue. "
                          "Approval needs the two to match, unless a maintainer decides otherwise."]
        return "\n".join(lines + [""])
    count = len(result["issues"])
    return "\n".join([
        marker("invalid", sha), f"**Theme check: {count} problem{'s' if count != 1 else ''}.**", "",
        f"Fix {'them' if count != 1 else 'it'} in the simulator ({common.SIMULATOR_URL}), then edit this issue's "
        f"**{common.THEME_HEADING}** field with the new JSON. The messages are the ones the simulator shows "
        f"(kit `{kit}`):", "",
        common.fenced(issue_lines(result["issues"]), FENCE_LIMIT), "",
        f"Checked theme sha256: `{sha}`", ""])


def upsert(api, number: int, body: str) -> str:
    found = common.validation_comments(common.issue_comments(api, number))
    if found:
        comment = found[-1][0]
        cid = comment.get("id")
        if not common.int_not_bool(cid):
            raise common.ApiError(0, "the validation comment has no id")
        if comment.get("body") == body:
            return "unchanged"
        api.request("PATCH", f"/repos/{{repo}}/issues/comments/{cid}", {"body": body})
        return "updated"
    api.request("POST", f"/repos/{{repo}}/issues/{number}/comments", {"body": body})
    return "created"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--result", type=Path, default=None)
    args = parser.parse_args(argv)
    try:
        number = int(common.env_token("NUMBER", common.NUMBER_RE))
        action = common.env_token("GATE_ACTION", re.compile(r"reject|validate"))
        reason = common.env_token("GATE_REASON", re.compile(r"[a-z-]{1,40}"))
        sha = None
        if action == "validate":
            sha = common.env_token("GATE_SHA256", common.SHA256_RE)
        result = load_result(args.result, sha) if sha else None
        body = body_for(action, reason, sha, result)
        outcome = upsert(common.GitHub.from_env(), number, body)
    except common.Refusal as refusal:
        common.error(f"refused ({refusal.code}): {refusal.message}")
        return 1
    except common.ApiError as err:
        common.error(f"GitHub API: {err}")
        return 1
    print(f"validation comment on #{number}: {outcome}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
