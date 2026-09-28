#!/usr/bin/env python3
"""The validate job of theme-submission.yml (#143; plan-website-104 W2). macOS, no token
permissions; the kit CLI comes from kit_cli.py (pinned commit, tree hash checked).

    GATE_SHA256=<hex> OPENER=<login> validate.py --bin MARSDAWN --theme FILE --out result.json

The theme file is the gate's artifact; its sha256 must equal the gate's output GATE_SHA256 before
anything else happens. Then `marsdawn theme validate --require-complete --json` on those exact bytes
(the kit is the authority), and, only for a theme the kit accepts, the site's own publishing rules
that the kit doesn't know (id not a built-in's, version without leading zeros, name/summary/author/
scenarios as check_theme_index.py holds themes/ to). result.json:

    {"schema": 1, "sha256": hex, "kit": sha, "verdict": "valid" | "invalid" | "error",
     "issues": [{"rule", "path", "message"}], "authorMatchesOpener": bool}

Messages are the kit's own (the simulator's wording) and may quote submitted text; the comment job
only ever shows them inside a fence. A kit that exits other than 0/1 or prints no JSON is "error".
"""
import argparse
import json
import os
import stat
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
import common  # noqa: E402
import sync_theme_kit as kit  # noqa: E402
from common import rules  # noqa: E402

MAX_ISSUES = 100
MAX_FIELD = 400


def read_regular(path: Path) -> bytes:
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise common.Refusal("input", "the theme artifact isn't a regular file")
        data = os.read(fd, common.MAX_THEME_BYTES + 1)
    finally:
        os.close(fd)
    if len(data) > common.MAX_THEME_BYTES:
        raise common.Refusal("input", "the theme artifact is over the size cap")
    return data


def clip(value) -> str:
    text = value if isinstance(value, str) else ""
    return text if len(text) <= MAX_FIELD else text[:MAX_FIELD] + "..."


def site_issues(data: bytes) -> list:
    """The site's publishing rules on a theme the kit accepted (rule ids prefixed `site.`)."""
    issues = []
    try:
        doc = rules.strict_json(data)
    except (ValueError, UnicodeDecodeError):
        return [{"rule": "site.json", "path": "", "message": "not one JSON object without repeated keys"}]
    tid = doc.get("id") if isinstance(doc, dict) else None
    if not rules.is_theme_id(tid):
        issues.append({"rule": "site.id", "path": "/id", "message": "id isn't a publishable id"})
    elif tid in rules.RESERVED_IDS:
        issues.append({"rule": "site.id", "path": "/id", "message": "id is a built-in theme's, and reserved"})
    problems = []
    rules.check_source_doc(problems, "theme.json", tid if isinstance(tid, str) else "", doc)
    issues += [{"rule": "site.theme", "path": "", "message": problem} for problem in problems]
    return issues


def validate(binary: Path, theme: Path, expected_sha: str, opener: str) -> dict:
    data = read_regular(theme)
    digest = common.sha256(data)
    if digest != expected_sha:
        raise common.Refusal("hash", f"the theme artifact's sha256 {digest} isn't the gate's {expected_sha}")
    result = {"schema": 1, "sha256": digest, "kit": kit.KIT_SHA, "verdict": "error", "issues": [],
              "authorMatchesOpener": False}
    try:
        run = subprocess.run([str(binary), "theme", "validate", "--require-complete", "--json", str(theme)],
                             capture_output=True, text=True, timeout=120)
        report = json.loads(run.stdout)
    except (OSError, subprocess.SubprocessError, ValueError):
        return result
    if run.returncode not in (0, 1) or not isinstance(report, dict) or not isinstance(report.get("issues"), list):
        return result
    issues = [{"rule": clip(i.get("rule")), "path": clip(i.get("path")), "message": clip(i.get("message"))}
              for i in report["issues"] if isinstance(i, dict)]
    kit_ok = run.returncode == 0 and report.get("ok") is True and not issues
    if kit_ok:
        issues = site_issues(data)
    result["issues"] = issues[:MAX_ISSUES]
    result["verdict"] = "valid" if kit_ok and not issues else "invalid"
    try:
        doc = rules.strict_json(data)
        result["authorMatchesOpener"] = isinstance(doc, dict) and common.author_matches(doc, opener)
    except (ValueError, UnicodeDecodeError):
        pass
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--theme", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        expected = common.env_token("GATE_SHA256", common.SHA256_RE)
        opener = common.env_token("OPENER", common.LOGIN_RE)
        result = validate(args.bin, args.theme, expected, opener)
    except common.Refusal as refusal:
        common.error(f"refused ({refusal.code}): {refusal.message}")
        return 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"validate: verdict={result['verdict']} issues={len(result['issues'])} sha256={result['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
