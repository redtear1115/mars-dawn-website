#!/usr/bin/env python3
"""Static rules for .github/workflows/*.yml and .github/actions/**/action.y*l (#143; plan-website-104
W2, F15; implementation security review H1, M1, M3).

    python3 scripts/check_workflows.py              # every workflow and composite action
    python3 scripts/check_workflows.py --self-test  # plant a break of each rule first

Rules, each with its own message (the self-test requires exactly that message per plant):

1. **expression-in-run** -- no `${{` at all inside a `run:` script (workflows and composite
   actions). Any expression there is spliced into the shell text before it runs: event text,
   `toJSON(github)`, an env value or a step output can all carry attacker-supplied text, and a
   denylist of dangerous contexts misses spellings (`GITHUB.EVENT`, `github['event']`,
   `toJSON(github)`). Pass values through `env:`. No allowlist: nothing in this repo needs one.
2. **expression-in-script** -- no `${{` inside `with.script:` of actions/github-script, for the
   same reason (the script is JavaScript source).
3. **pull-request-target** -- no workflow triggers on `pull_request_target`, which runs with a
   write token and the repository's secrets next to the PR's own data.
4. **unpinned-uses** -- every `uses:` (steps, reusable-workflow jobs, composite-action steps) is a
   local `./` path, a `docker://...@sha256:<64 hex>` image, or `owner/repo[/path]@<40-hex SHA>`.
5. **write-with-kit** -- a job whose `run:` steps (including those of the local composite actions
   it uses, followed recursively) run brew, swift/swiftc/xcodebuild/xcrun, the kit CLI
   (`marsdawn`) or a script that builds or runs it (build_themes.py, sync_theme_kit.py,
   scripts/submission/kit_cli.py, validate.py, stage.py) has no write permission, and declares its
   permissions explicitly (a job that inherits the repository default could be handed write scopes
   by a settings change).
6. **write-checkout-ref** -- in a job with any write permission, an actions/checkout `with.ref`
   doesn't reference `needs.*` or `steps.*`: the commit a write job runs code from must come from
   the trusted gate (an input or a fixed ref), never from a value an earlier, less trusted job
   produced (review H1).
7. **cache-in-build** -- a job that runs stage.py or build_themes.py (the post-approval build)
   uses no actions/cache: a cache entry could have been written by a job that processed submitted
   text (review M1). That build compiles the kit from source.

The files are read by a small YAML reader for the subset they use -- block mappings and
sequences, plain/quoted scalars, `|`/`>` block scalars, one-line flow collections, comments -- which
**fails closed**: anchors, aliases, tags, multi-line flow collections, duplicate keys, tabs in
indentation and anything else it doesn't understand make the file a problem of its own rather than
a pass. (Standard library only. tests/test_workflows_and_form.py compares this reader with PyYAML
where that's installed.)
"""
import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_REL = ".github/workflows"
ACTIONS_REL = ".github/actions"

EXPRESSION_RE = re.compile(r"\$\{\{")
PINNED_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]*)/[A-Za-z0-9._-]+(?:/[A-Za-z0-9._/-]+)?@[0-9a-f]{40}")
DOCKER_PINNED_RE = re.compile(r"docker://[^\s@]+@sha256:[0-9a-f]{64}")
KIT_RE = re.compile(r"\b(?:brew|swift|swiftc|xcodebuild|xcrun|marsdawn)\b"
                    r"|scripts/(?:build_themes|sync_theme_kit)\.py"
                    r"|scripts/submission/(?:kit_cli|validate|stage)\.py", re.I)
BUILD_RE = re.compile(r"scripts/build_themes\.py|scripts/submission/stage\.py", re.I)
JOB_OUTPUT_RE = re.compile(r"\$\{\{[^}]*\b(?:needs|steps)\s*[.\[]", re.I)
MAX_ACTION_DEPTH = 5

MESSAGES = {
    "expression-in-run": "`run:` contains a ${{ }} expression; pass the value through env: instead",
    "expression-in-script": "actions/github-script `script:` contains a ${{ }} expression; pass it through env: instead",
    "pull-request-target": "triggers on pull_request_target, which runs with a write token and secrets next to PR data",
    "unpinned-uses": "isn't pinned to a full commit SHA (or a docker sha256 digest, or a local ./ path)",
    "write-with-kit": "runs brew/swift/the kit and has write permission or no explicit permissions",
    "write-checkout-ref": "has write permission and checks out a ref taken from needs.* or steps.*; use the gate's input",
    "cache-in-build": "runs the post-approval build (stage.py/build_themes.py) and uses actions/cache",
    "unreadable": "can't be read by this check's YAML subset; it fails closed",
}


# --- a fail-closed reader for the YAML subset workflows use ---------------------------------------

class YamlSubsetError(ValueError):
    pass


def strip_comment(text: str) -> str:
    """text without a trailing comment: `#` at the start or after whitespace, outside quotes. Inside
    double quotes a backslash escapes the next character; inside single quotes `''` is a quote."""
    quote, i = None, 0
    while i < len(text):
        ch = text[i]
        if quote == '"':
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                quote = None
        elif quote == "'":
            if ch == "'":
                if i + 1 < len(text) and text[i + 1] == "'":
                    i += 2
                    continue
                quote = None
        elif ch in "'\"" and (i == 0 or text[i - 1] in " \t[{,:"):
            quote = ch
        elif ch == "#" and (i == 0 or text[i - 1] in " \t"):
            return text[:i].rstrip()
        i += 1
    return text.rstrip()


def scalar(text: str, where: str):
    text = text.strip()
    if text == "" or text == "~" or text == "null":
        return None if text != "null" else "null"
    if text[0] == '"':
        if len(text) < 2 or text[-1] != '"':
            raise YamlSubsetError(f"{where}: unterminated double-quoted scalar")
        try:
            value = json.loads(text)
        except ValueError:
            raise YamlSubsetError(f"{where}: a double-quoted scalar with an escape this reader doesn't know")
        return value
    if text[0] == "'":
        if len(text) < 2 or text[-1] != "'":
            raise YamlSubsetError(f"{where}: unterminated single-quoted scalar")
        inner = text[1:-1]
        if re.search(r"(?<!')'(?!')", inner.replace("''", "")):
            raise YamlSubsetError(f"{where}: a stray quote inside a single-quoted scalar")
        return inner.replace("''", "'")
    if text[0] in "&*!%@`|>{}[]," or text.startswith(("? ", "- ")) or text == "-":
        raise YamlSubsetError(f"{where}: {text[0]!r} starts a construct this reader doesn't support")
    if ": " in text or text.endswith(":"):
        raise YamlSubsetError(f"{where}: a plain scalar with ': ' in it is ambiguous")
    return text


def parse_flow(text: str, where: str):
    """A one-line flow sequence or mapping; nested flow collections allowed."""
    pos = 0

    def skip_ws():
        nonlocal pos
        while pos < len(text) and text[pos] in " \t":
            pos += 1

    def item(stops):
        nonlocal pos
        skip_ws()
        if pos < len(text) and text[pos] in "[{":
            return collection()
        if pos < len(text) and text[pos] in "'\"":
            quote, start = text[pos], pos
            pos += 1
            while pos < len(text):
                if text[pos] == "\\" and quote == '"':
                    pos += 2
                    continue
                if text[pos] == quote:
                    if quote == "'" and pos + 1 < len(text) and text[pos + 1] == "'":
                        pos += 2
                        continue
                    break
                pos += 1
            if pos >= len(text):
                raise YamlSubsetError(f"{where}: unterminated quote in a flow collection")
            pos += 1
            return scalar(text[start:pos], where)
        start = pos
        while pos < len(text) and text[pos] not in stops:
            if text[pos] == ":" and ":" in stops and (pos + 1 == len(text) or text[pos + 1] in " ,]}"):
                break
            pos += 1
        raw = text[start:pos].strip()
        if not raw:
            raise YamlSubsetError(f"{where}: an empty entry in a flow collection")
        return scalar(raw, where)

    def collection():
        nonlocal pos
        opener = text[pos]
        closer = "]" if opener == "[" else "}"
        pos += 1
        out = [] if opener == "[" else {}
        skip_ws()
        if pos < len(text) and text[pos] == closer:
            pos += 1
            return out
        while True:
            if opener == "[":
                out.append(item(",]"))
            else:
                key = item(",}:")
                skip_ws()
                if pos >= len(text) or text[pos] != ":":
                    raise YamlSubsetError(f"{where}: a flow mapping entry without ':'")
                pos += 1
                if not isinstance(key, str) or key in out:
                    raise YamlSubsetError(f"{where}: a bad or duplicate key in a flow mapping")
                out[key] = item(",}")
            skip_ws()
            if pos < len(text) and text[pos] == ",":
                pos += 1
                continue
            if pos < len(text) and text[pos] == closer:
                pos += 1
                return out
            raise YamlSubsetError(f"{where}: a flow collection that isn't closed on its line")

    value = collection()
    skip_ws()
    if pos != len(text):
        raise YamlSubsetError(f"{where}: text after a flow collection")
    return value


KEY_RE = re.compile(r"""(?P<key>"(?:[^"\\]|\\.)*"|'(?:[^']|'')*'|[^\s'"#&*!|>%@`{}\[\],?-][^:#]*?|-[^\s:#][^:#]*?)\s*:(?:\s+(?P<rest>.*)|$)""")


class Reader:
    def __init__(self, text: str, name: str):
        if "\t" in "".join(re.findall(r"^[ \t]*", text, re.M)):
            raise YamlSubsetError(f"{name}: a tab in indentation")
        self.lines = text.split("\n")
        self.name = name
        self.i = 0
        if self.lines and self.lines[0].strip() == "---":
            self.i = 1

    def where(self, i=None) -> str:
        return f"{self.name}:{(self.i if i is None else i) + 1}"

    def next_significant(self):
        """(index, indent, content) of the next line with content, or None."""
        i = self.i
        while i < len(self.lines):
            raw = self.lines[i]
            content = strip_comment(raw.lstrip(" "))
            if content:
                return i, len(raw) - len(raw.lstrip(" ")), content
            i += 1
        return None

    def document(self):
        nxt = self.next_significant()
        if nxt is None:
            return None
        value = self.block(nxt[1])
        rest = self.next_significant()
        if rest is not None:
            raise YamlSubsetError(f"{self.where(rest[0])}: content this reader couldn't place")
        return value

    def block(self, indent: int):
        nxt = self.next_significant()
        if nxt is None or nxt[1] != indent:
            raise YamlSubsetError(f"{self.where()}: expected a block at indent {indent}")
        content = nxt[2]
        if content == "-" or content.startswith("- "):
            return self.sequence(indent)
        return self.mapping(indent)

    def value_after(self, rest, indent: int, where: str, allow_compact_seq: bool):
        """The value of `key:` (rest is what followed it) or of `- ` (rest is the item text)."""
        if rest is None or rest == "":
            nxt = self.next_significant()
            if nxt is not None and nxt[1] > indent:
                return self.block(nxt[1])
            if (allow_compact_seq and nxt is not None and nxt[1] == indent
                    and (nxt[2] == "-" or nxt[2].startswith("- "))):
                return self.sequence(indent)
            return None
        if rest[0] in "|>":
            return self.block_scalar(rest, indent, where)
        if rest[0] in "[{":
            return parse_flow(rest, where)
        return scalar(rest, where)

    def block_scalar(self, header: str, indent: int, where: str):
        match = re.fullmatch(r"([|>])(-?)", header)
        if not match:
            raise YamlSubsetError(f"{where}: a block scalar header this reader doesn't support ({header!r})")
        style, chomp = match.groups()
        body, content_indent = [], None
        while self.i < len(self.lines):
            raw = self.lines[self.i]
            if raw.strip() == "":
                body.append("")
                self.i += 1
                continue
            line_indent = len(raw) - len(raw.lstrip(" "))
            if line_indent <= indent:
                break
            if content_indent is None:
                content_indent = line_indent
            if line_indent < content_indent:
                raise YamlSubsetError(f"{self.where()}: a block scalar line less indented than its first")
            body.append(raw[content_indent:])
            self.i += 1
        while body and body[-1] == "":
            body.pop()
        if style == "|":
            text = "\n".join(body)
        else:
            paragraphs, current = [], []
            for line in body:
                if line == "":
                    paragraphs.append(" ".join(current))
                    current = []
                else:
                    current.append(line)
            paragraphs.append(" ".join(current))
            text = "\n".join(paragraphs)
        if chomp == "-" or not body:
            return text
        return text + "\n"

    def mapping(self, indent: int) -> dict:
        out = {}
        while True:
            nxt = self.next_significant()
            if nxt is None or nxt[1] < indent:
                return out
            i, line_indent, content = nxt
            if line_indent > indent:
                raise YamlSubsetError(f"{self.where(i)}: unexpected indentation")
            if content == "-" or content.startswith("- "):
                return out  # a compact sequence ends this mapping only where the caller allowed it
            match = KEY_RE.fullmatch(content)
            if not match:
                raise YamlSubsetError(f"{self.where(i)}: not a `key: value` line this reader understands")
            key = scalar(match.group("key"), self.where(i))
            if not isinstance(key, str):
                raise YamlSubsetError(f"{self.where(i)}: an empty key")
            if key in out:
                raise YamlSubsetError(f"{self.where(i)}: duplicate key {key!r}")
            if key == "<<":
                raise YamlSubsetError(f"{self.where(i)}: merge keys aren't supported")
            self.i = i + 1
            out[key] = self.value_after(match.group("rest"), indent, self.where(i), True)

    def sequence(self, indent: int) -> list:
        out = []
        while True:
            nxt = self.next_significant()
            if nxt is None or nxt[1] < indent:
                return out
            i, line_indent, content = nxt
            if line_indent > indent:
                raise YamlSubsetError(f"{self.where(i)}: unexpected indentation")
            if not (content == "-" or content.startswith("- ")):
                return out
            raw = self.lines[i]
            rest = strip_comment(raw[line_indent + 1:]).strip()
            if rest and KEY_RE.fullmatch(rest) and rest[0] not in "'\"[{":
                # `- key: value`: a mapping whose first key sits on the dash line.
                self.lines[i] = raw[:line_indent] + " " + raw[line_indent + 1:]
                item_indent = len(self.lines[i]) - len(self.lines[i].lstrip(" "))
                self.i = i
                out.append(self.mapping(item_indent))
            elif rest.startswith("- "):
                raise YamlSubsetError(f"{self.where(i)}: nested compact sequences aren't supported")
            else:
                self.i = i + 1
                out.append(self.value_after(rest, indent, self.where(i), False))


def load(text: str, name: str = "<yaml>"):
    """The one document in `text`; a `---` anywhere but the first line, or a `...`, fails."""
    markers = [i for i, line in enumerate(text.split("\n")) if re.fullmatch(r"(?:---|\.\.\.)\s*", line)]
    if markers and markers != [0]:
        raise YamlSubsetError(f"{name}: document markers other than a leading --- aren't supported")
    return Reader(text, name).document()


# --- the rules --------------------------------------------------------------------------------------

def events_of(on) -> set:
    if isinstance(on, str):
        return {on}
    if isinstance(on, list):
        return {e for e in on if isinstance(e, str)}
    if isinstance(on, dict):
        return set(on)
    return set()


def has_write(perms) -> bool:
    if isinstance(perms, str):
        return perms.strip() == "write-all"
    if isinstance(perms, dict):
        return any(isinstance(v, str) and v.strip() == "write" for v in perms.values())
    return False


def pinned(uses) -> bool:
    if not isinstance(uses, str):
        return False
    uses = uses.strip()
    return uses.startswith("./") or bool(PINNED_RE.fullmatch(uses)) or bool(DOCKER_PINNED_RE.fullmatch(uses))


def is_local_action(uses) -> bool:
    return (isinstance(uses, str) and uses.startswith("./")
            and not re.search(r"\.ya?ml$", uses) and ".." not in uses.split("/"))


def load_action(root: Path, uses: str):
    """(steps, error) of a local composite action."""
    folder = root / uses[2:]
    files = [folder / n for n in ("action.yml", "action.yaml") if (folder / n).is_file()]
    if len(files) != 1 or files[0].is_symlink():
        return None, f"local action {uses!r} has no single action.yml"
    try:
        doc = load(files[0].read_text(encoding="utf-8"), uses)
    except YamlSubsetError as err:
        return None, str(err)
    runs = doc.get("runs") if isinstance(doc, dict) else None
    if not isinstance(runs, dict):
        return None, f"local action {uses!r} has no runs mapping"
    if runs.get("using") != "composite":
        return [], None
    steps = runs.get("steps")
    return (steps, None) if isinstance(steps, list) else (None, f"local action {uses!r}: steps isn't a list")


def flatten(steps, root: Path, where: str, problems: list, depth=0) -> list:
    """Every step dict the job runs, local composite actions expanded recursively."""
    out = []
    for step in steps:
        if not isinstance(step, dict):
            continue
        out.append(step)
        uses = step.get("uses")
        if is_local_action(uses):
            if depth >= MAX_ACTION_DEPTH:
                problems.append(("unreadable", f"{where}: {MESSAGES['unreadable']} (local actions nest too deep)"))
                continue
            inner, error = load_action(root, uses)
            if error:
                problems.append(("unreadable", f"{where}: {MESSAGES['unreadable']} ({error})"))
                continue
            out += flatten(inner, root, where, problems, depth + 1)
    return out


def check_steps(steps, where: str, problems: list) -> None:
    """The per-step rules, on steps written in this file (not expanded)."""
    if not isinstance(steps, list):
        problems.append(("unreadable", f"{where}: {MESSAGES['unreadable']} (steps isn't a list)"))
        return
    for n, step in enumerate(steps, 1):
        here = f"{where} step {n}"
        if not isinstance(step, dict):
            problems.append(("unreadable", f"{here}: {MESSAGES['unreadable']} (not a mapping)"))
            continue
        uses = step.get("uses")
        if uses is not None and not pinned(uses):
            problems.append(("unpinned-uses", f"{here}: uses {uses!r} {MESSAGES['unpinned-uses']}"))
        run = step.get("run")
        if run is not None:
            if not isinstance(run, str):
                problems.append(("unreadable", f"{here}: {MESSAGES['unreadable']} (run isn't a string)"))
            elif EXPRESSION_RE.search(run):
                problems.append(("expression-in-run", f"{here}: {MESSAGES['expression-in-run']}"))
        if isinstance(uses, str) and uses.lower().startswith("actions/github-script@"):
            script = (step.get("with") or {}).get("script") if isinstance(step.get("with"), dict) else None
            if isinstance(script, str) and EXPRESSION_RE.search(script):
                problems.append(("expression-in-script", f"{here}: {MESSAGES['expression-in-script']}"))


def check_workflow(text: str, name: str, root: Path = None) -> list:
    """[(rule, message)] for one workflow file's text."""
    root = root or ROOT
    try:
        doc = load(text, name)
    except YamlSubsetError as err:
        return [("unreadable", f"{name}: {MESSAGES['unreadable']} ({err})")]
    if not isinstance(doc, dict):
        return [("unreadable", f"{name}: {MESSAGES['unreadable']} (the top level isn't a mapping)")]
    problems = []
    if "pull_request_target" in events_of(doc.get("on")):
        problems.append(("pull-request-target", f"{name}: {MESSAGES['pull-request-target']}"))
    jobs = doc.get("jobs")
    if not isinstance(jobs, dict):
        return problems + [("unreadable", f"{name}: {MESSAGES['unreadable']} (no jobs mapping)")]
    for job_id, job in jobs.items():
        where = f"{name}: job {job_id}"
        if not isinstance(job, dict):
            problems.append(("unreadable", f"{where}: {MESSAGES['unreadable']} (not a mapping)"))
            continue
        uses = job.get("uses")
        if uses is not None and not pinned(uses):
            problems.append(("unpinned-uses", f"{where}: uses {uses!r} {MESSAGES['unpinned-uses']}"))
        steps = job.get("steps") or []
        check_steps(steps, where, problems)
        if not isinstance(steps, list):
            continue
        every = flatten(steps, root, where, problems)
        runs = "\n".join(s["run"] for s in every if isinstance(s.get("run"), str))
        perms = job["permissions"] if "permissions" in job else doc.get("permissions", KeyError)
        writes = perms is KeyError or perms is None or has_write(perms)
        if KIT_RE.search(runs) and writes:
            problems.append(("write-with-kit", f"{where} {MESSAGES['write-with-kit']}"))
        if has_write(perms):
            for step in every:
                if str(step.get("uses", "")).lower().startswith("actions/checkout@"):
                    ref = (step.get("with") or {}).get("ref") if isinstance(step.get("with"), dict) else None
                    if isinstance(ref, str) and JOB_OUTPUT_RE.search(ref):
                        problems.append(("write-checkout-ref", f"{where} {MESSAGES['write-checkout-ref']}"))
        if BUILD_RE.search(runs) and any(str(s.get("uses", "")).lower().startswith("actions/cache") for s in every):
            problems.append(("cache-in-build", f"{where} {MESSAGES['cache-in-build']}"))
    return problems


def check_action(text: str, name: str) -> list:
    """The per-step rules on a composite action's own steps."""
    try:
        doc = load(text, name)
    except YamlSubsetError as err:
        return [("unreadable", f"{name}: {MESSAGES['unreadable']} ({err})")]
    runs = doc.get("runs") if isinstance(doc, dict) else None
    if not isinstance(runs, dict):
        return [("unreadable", f"{name}: {MESSAGES['unreadable']} (no runs mapping)")]
    problems = []
    if runs.get("using") == "composite":
        check_steps(runs.get("steps"), name, problems)
    return problems


def check_dir(root: Path) -> list:
    folder = root / WORKFLOWS_REL
    files = sorted(p for p in folder.iterdir() if p.suffix in (".yml", ".yaml")) if folder.is_dir() else []
    if not files:
        return [("unreadable", f"{WORKFLOWS_REL}: no workflow files found")]
    problems = []
    for path in files:
        if path.is_symlink() or not path.is_file():
            problems.append(("unreadable", f"{WORKFLOWS_REL}/{path.name}: not a regular file"))
            continue
        problems += check_workflow(path.read_text(encoding="utf-8"), f"{WORKFLOWS_REL}/{path.name}", root)
    actions = root / ACTIONS_REL
    if actions.is_dir():
        for path in sorted(p for p in actions.rglob("*") if p.name in ("action.yml", "action.yaml")):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or not path.is_file():
                problems.append(("unreadable", f"{rel}: not a regular file"))
                continue
            problems += check_action(path.read_text(encoding="utf-8"), rel)
    return problems


# --- self-test ---------------------------------------------------------------------------------------

CLEAN = """\
name: Clean
on:
  pull_request:
    branches: [main]
permissions: {}
jobs:
  build:
    runs-on: macos-15
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
      - name: Build
        env:
          TITLE: ${{ github.event.pull_request.title }}
        run: |
          swift build
          echo "$TITLE"
  comment:
    runs-on: ubuntu-24.04
    permissions:
      issues: write
    steps:
      - run: python3 scripts/submission/comment.py
"""

SHA40 = "55cc8345863c7cc4c66a329aec7e433d2d1c52a9"
ECHO = '          echo "$TITLE"\n'

# (rule, name, [(old, new), ...]): each edit of CLEAN must match exactly once.
SYNTHETIC_PLANTS = [
    ("expression-in-run", "issue body spliced into a shell line", [(ECHO, '          echo "${{ github.event.issue.body }}"\n')]),
    ("expression-in-run", "event read with index syntax", [(ECHO, "          echo \"${{ github['event'].issue.title }}\"\n")]),
    ("expression-in-run", "upper-case GITHUB.EVENT", [(ECHO, '          echo "${{ GITHUB.EVENT.issue.title }}"\n')]),
    ("expression-in-run", "toJSON(github)", [(ECHO, "          echo '${{ toJSON(github) }}'\n")]),
    ("expression-in-run", "env value in run", [(ECHO, '          echo "${{ env.T }}"\n')]),
    ("expression-in-script", "step output in a github-script script",
     [("      - run: python3 scripts/submission/comment.py\n",
       f"      - uses: actions/github-script@{SHA40}\n        with:\n"
       "          script: console.log(\"${{ steps.x.outputs.y }}\")\n")]),
    ("pull-request-target", "pull_request_target trigger", [("  pull_request:\n", "  pull_request_target:\n")]),
    ("unpinned-uses", "action pinned to a tag",
     [("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", "actions/checkout@v7")]),
    ("unpinned-uses", "action pinned to a short SHA",
     [("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1", "actions/checkout@3d3c42e")]),
    ("write-with-kit", "contents: write in the job that runs swift", [("      contents: read\n", "      contents: write\n")]),
    ("write-with-kit", "kit job without its own permissions and no workflow default",
     [("permissions: {}\njobs:\n  build:\n    runs-on: macos-15\n    permissions:\n      contents: read\n",
       "jobs:\n  build:\n    runs-on: macos-15\n")]),
    ("write-with-kit", "write-all in a job running brew",
     [("    permissions:\n      contents: read\n    steps:\n",
       "    permissions: write-all\n    steps:\n      - run: brew install jq\n")]),
    ("write-checkout-ref", "write job checks out a ref from needs.*",
     [("      - run: python3 scripts/submission/comment.py\n",
       "      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1\n        with:\n"
       "          ref: ${{ needs.build.outputs.sha }}\n      - run: python3 scripts/submission/comment.py\n")]),
    ("cache-in-build", "the post-approval build restores a cache",
     [("          swift build\n", "          python3 scripts/build_themes.py\n"),
      ("      - name: Build\n", f"      - uses: actions/cache/restore@{SHA40}\n        with:\n          path: x\n"
                               "          key: y\n      - name: Build\n")]),
    ("unreadable", "a YAML anchor", [("    runs-on: macos-15\n", "    runs-on: &os macos-15\n")]),
    ("unreadable", "a duplicate key", [("    runs-on: ubuntu-24.04\n", "    runs-on: ubuntu-24.04\n    runs-on: ubuntu-22.04\n")]),
]

CHECKOUT = "      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1\n"
KIT_ACTION = ("name: Build the kit\ndescription: plant\nruns:\n  using: composite\n  steps:\n"
              "    - run: swift build -c release\n      shell: bash\n")
EXPR_ACTION = ("name: Echo\ndescription: plant\ninputs:\n  x:\n    description: x\nruns:\n  using: composite\n"
               "  steps:\n    - run: echo \"${{ inputs.x }}\"\n      shell: bash\n")

# Plants on the repository's real files: (rule, file, [(old, new), ...], {extra file: text}).
REAL_PLANTS = [
    ("expression-in-run", "theme-submission.yml",
     [('gate.py submission --out "$RUNNER_TEMP/theme"',
       'gate.py submission --out "$RUNNER_TEMP/theme" --title "${{ github.event.issue.title }}"')], {}),
    ("pull-request-target", "site.yml",
     [("  pull_request:\n    branches: [main, release, \"release-*\"]\n",
       "  pull_request_target:\n    branches: [main, release, \"release-*\"]\n")], {}),
    ("unpinned-uses", "theme-submission.yml",
     [("actions/cache/restore@55cc8345863c7cc4c66a329aec7e433d2d1c52a9", "actions/cache/restore@v6")], {}),
    ("write-with-kit", "theme-submission.yml",
     [("    runs-on: macos-15\n    timeout-minutes: 15\n    permissions: {}\n",
       "    runs-on: macos-15\n    timeout-minutes: 15\n    permissions:\n      issues: write\n")], {}),
    ("write-with-kit", "theme-pr.yml",
     [("    runs-on: macos-15\n    timeout-minutes: 45\n    permissions: {}\n",
       "    runs-on: macos-15\n    timeout-minutes: 45\n    permissions:\n      contents: write\n")], {}),
    ("write-with-kit", "theme-pr.yml (a composite action running swift in the commit job)",
     [("      - name: Commit, push theme/<source>-<n> and open the pull request\n",
       "      - uses: ./.github/actions/kit-build\n      - name: Commit, push theme/<source>-<n> and open the pull request\n")],
     {".github/actions/kit-build/action.yml": KIT_ACTION}),
    ("write-checkout-ref", "theme-pr.yml",
     [("      issues: write\n    steps:\n" + CHECKOUT + "        with:\n          ref: ${{ inputs.base_sha }}\n",
       "      issues: write\n    steps:\n" + CHECKOUT + "        with:\n          ref: ${{ needs.build.outputs.base_sha }}\n")], {}),
    ("cache-in-build", "theme-pr.yml",
     [("      # swift-tools 6.2 needs Xcode 26",
       f"      - uses: actions/cache/restore@{SHA40} # v6.1.0\n        with:\n          path: x\n          key: y\n"
       "      # swift-tools 6.2 needs Xcode 26")], {}),
    ("expression-in-run", "site.yml (a composite action with an expression in run:)",
     [], {".github/actions/echo/action.yml": EXPR_ACTION}),
]


def apply(text: str, edits: list, label: str, failures: list):
    for old, new in edits:
        if text.count(old) != 1:
            failures.append(f"plant {label!r}: an edit matches {text.count(old)} times, not once")
            return None
        text = text.replace(old, new)
    return text


def expect(rule: str, label: str, got: list, failures: list) -> None:
    if [r for r, _ in got] != [rule] or MESSAGES[rule] not in got[0][1]:
        failures.append(f"plant {label!r}: expected exactly one {rule!r} problem, got {got}")
    else:
        print(f"  red as expected [{rule}] {label}: {got[0][1]}")


def self_test() -> int:
    failures = []
    baseline = check_workflow(CLEAN, "clean.yml")
    if baseline:
        failures.append(f"the clean workflow isn't clean: {baseline}")
    for rule, label, edits in SYNTHETIC_PLANTS:
        text = apply(CLEAN, edits, label, failures)
        if text is not None:
            expect(rule, label, check_workflow(text, "plant.yml"), failures)
    real = check_dir(ROOT)
    if real:
        failures.append(f"the repository's own workflows aren't clean: {real}")
    for rule, label, edits, extra in REAL_PLANTS:
        filename = label.split(" ", 1)[0]
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(ROOT / ".github", Path(tmp) / ".github")
            path = Path(tmp) / WORKFLOWS_REL / filename
            text = apply(path.read_text(encoding="utf-8"), edits, label, failures)
            if text is None:
                continue
            path.write_text(text, encoding="utf-8")
            for rel, body in extra.items():
                (Path(tmp) / rel).parent.mkdir(parents=True, exist_ok=True)
                (Path(tmp) / rel).write_text(body, encoding="utf-8")
            expect(rule, label, check_dir(Path(tmp)), failures)
    for failure in failures:
        print(f"::error::check_workflows.py --self-test: {failure}")
    if failures:
        return 1
    print(f"check_workflows.py --self-test: {len(SYNTHETIC_PLANTS) + len(REAL_PLANTS)} plants each red with their own rule")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    problems = check_dir(ROOT)
    for _, message in problems:
        print(f"::error::{message}")
    if problems:
        return 1
    count = len([p for p in (ROOT / WORKFLOWS_REL).iterdir() if p.suffix in (".yml", ".yaml")])
    print(f"check_workflows.py: {count} workflow(s) clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
