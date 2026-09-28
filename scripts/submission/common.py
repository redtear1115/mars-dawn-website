"""Shared pieces of the theme submission workflows (#143; plan-website-104 W2).

Everything here treats issue bodies, comments, PR data and theme files as **data**: nothing from
them is ever spliced into a shell line, a workflow expression, a git ref or an output file without
passing a closed-grammar check first. The workflows (.github/workflows/theme-*.yml) only call these
scripts, passing event data through the event payload file ($GITHUB_EVENT_PATH) or `env:`.

Standard library only. Python 3.9+ (a local Mac's /usr/bin/python3) and 3.12 (ubuntu-24.04).
"""
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import check_theme_index as rules  # noqa: E402

# --- identities and names -------------------------------------------------------------------------

BOT_ID = rules.BOT_ID                    # github-actions[bot]
BOT_LOGIN = "github-actions[bot]"
BOT_NAME = "github-actions[bot]"
BOT_EMAIL = f"{BOT_ID}+github-actions[bot]@users.noreply.github.com"

SUBMISSION_LABEL = "theme-submission"
APPROVED_LABEL = "theme-approved"
AUTHOR_CHANGE_LABEL = rules.AUTHOR_CHANGE_LABEL

TEMPLATE_REL = ".github/ISSUE_TEMPLATE/theme-submission.yml"
SIMULATOR_URL = "https://marsdawn.southern-light.dev/themes/new/"

# The issue form's two headings and the DCO checkbox's exact label, as GitHub renders a submitted
# form ("### <label>" per field, "- [X] <label>" per ticked box). tests/test_template.py holds the
# template file to these strings, so the form and the parser can't drift apart.
THEME_HEADING = "Theme"
DCO_HEADING = "Developer Certificate of Origin"
DCO_LABEL = ("I certify the Developer Certificate of Origin 1.1 (https://developercertificate.org) for this "
             "theme: it is my own work or I have the right to submit it, and I release it under Apache-2.0. "
             "I understand that my GitHub username and the theme's author, name and summary become public "
             "permanently.")

MAX_BODY_BYTES = 16 * 1024               # plan W2 gate: the issue body, as the API returns it
MAX_THEME_BYTES = rules.MAX_THEME_BYTES  # the kit's and the site's cap on a theme.json
MAX_COMMENT_PAGES = 30                   # 3 000 comments: far past any real submission thread
MAX_PR_COMMITS = 250                     # the API's own cap on a PR's commit list

# The one bot comment per submission issue starts with this line. Found by author (id + login +
# type) *and* this exact first line; a person can type the marker but can't be the bot.
MARKER_RE = re.compile(r"<!-- marsdawn-theme-validation v1 verdict=(valid|invalid|rejected|error) "
                       r"sha256=([0-9a-f]{64}|none) -->")

NUMBER_RE = re.compile(r"[1-9][0-9]{0,9}")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
COMMIT_RE = rules.COMMIT_RE
LOGIN_RE = rules.LOGIN_RE
USER_ID_RE = re.compile(r"[1-9][0-9]{0,11}")
REPO_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})/[A-Za-z0-9._-]{1,100}")
# Branches a bot PR may target, and the only refs the commit job may push.
BASE_BRANCH_RE = re.compile(r"main|release-[0-9]+(?:\.[0-9]+){1,3}")
PUSH_REF_RE = re.compile(r"refs/heads/theme/(?:issue|pr)-[1-9][0-9]{0,9}")


class Refusal(Exception):
    """A submission the flow won't take, with a code from a closed list and a message that holds
    no submitted text (only fixed words, numbers, hex digests and closed-grammar ids/logins)."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ascii_lower(text: str) -> str:
    return rules.ascii_lower(text)


def fullmatch(pattern, value) -> bool:
    return isinstance(value, str) and bool(pattern.fullmatch(value))


def int_not_bool(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


# --- the issue body ---------------------------------------------------------------------------------

def split_sections(body: str) -> dict:
    """{heading: [lines]} for every `### heading` line, in a body with \\r\\n already folded to \\n.
    A heading seen twice keeps only its first section, and the parse fails closed: the second one
    makes the section ambiguous, so it's reported as missing (a Refusal upstream)."""
    sections, current, seen_twice = {}, None, set()
    for line in body.split("\n"):
        if line.startswith("### "):
            heading = line[4:].strip()
            if heading in sections:
                seen_twice.add(heading)
                current = None
                continue
            sections[heading] = []
            current = heading
        elif current is not None:
            sections[current].append(line)
    for heading in seen_twice:
        sections.pop(heading, None)
    return sections


def extract_theme(lines: list) -> bytes:
    """The theme field's text as the exact bytes to validate and publish: GitHub fences a
    `render: json` field, so the text between the first fence line and its matching closing fence,
    or, for a body edited by hand, the whole field. One trailing newline is added, as every file in
    the repo ends with one. Refusal("no-theme") when the field is empty."""
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    if not lines or (len(lines) == 1 and lines[0].strip() == "_No response_"):
        raise Refusal("no-theme", "The Theme field is empty.")
    opening = re.fullmatch(r"(`{3,})(?:json)?", lines[0].strip())
    if opening:
        fence = opening.group(1)
        if len(lines) < 2 or lines[-1].strip() != fence:
            raise Refusal("no-theme", "The Theme field's code block isn't closed.")
        lines = lines[1:-1]
    text = "\n".join(lines).strip("\n")
    if not text.strip():
        raise Refusal("no-theme", "The Theme field is empty.")
    return (text + "\n").encode("utf-8")


def dco_ticked(lines: list) -> bool:
    for line in lines:
        match = re.fullmatch(r"- \[([ xX])\] (.*)", line.strip())
        if match and match.group(2).strip() == DCO_LABEL:
            return match.group(1) in "xX"
    return False


def parse_submission(body) -> tuple:
    """(theme bytes, parsed theme object, dco ticked) from an issue body, or a Refusal whose code
    is one of: too-large, no-theme, json, dco."""
    if body is None:
        body = ""
    if not isinstance(body, str):
        raise Refusal("no-theme", "The issue has no body.")
    if len(body.encode("utf-8")) > MAX_BODY_BYTES:
        raise Refusal("too-large", f"The issue body is larger than {MAX_BODY_BYTES} bytes, so it wasn't read.")
    sections = split_sections(body.replace("\r\n", "\n").replace("\r", "\n"))
    if THEME_HEADING not in sections:
        raise Refusal("no-theme", f"The issue has no single `### {THEME_HEADING}` section.")
    data = extract_theme(sections[THEME_HEADING])
    if len(data) > MAX_THEME_BYTES:
        raise Refusal("too-large", f"The theme is larger than {MAX_THEME_BYTES} bytes.")
    try:
        doc = rules.strict_json(data)
    except (ValueError, UnicodeDecodeError):
        raise Refusal("json", "The Theme field isn't one valid JSON object (or it repeats a key).")
    if not isinstance(doc, dict):
        raise Refusal("json", "The Theme field isn't one valid JSON object (or it repeats a key).")
    ticked = DCO_HEADING in sections and dco_ticked(sections[DCO_HEADING])
    return data, doc, ticked


# --- Markdown fences for bot comments -------------------------------------------------------------

def fence_for(text: str) -> str:
    """A backtick fence longer than any backtick run in `text`, so nothing inside can close it."""
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def fenced(text: str, limit: int) -> str:
    """`text` in a fenced block of at most `limit` characters. A too-long text is cut *inside* the
    fence and marked, and the closing fence is always kept, so a truncation can never leave the rest
    of the comment inside an unclosed block (or let the text close it early)."""
    text = text.replace("\r", "")
    note = "\n[... truncated]"
    fence = fence_for(text + note)
    budget = limit - 2 * len(fence) - len("text") - 2 - len(note)
    if budget < 0:
        raise ValueError("limit too small for a fenced block")
    if len(text) > budget:
        text = text[:budget] + note
    return f"{fence}text\n{text}\n{fence}"


# --- GitHub Actions plumbing ----------------------------------------------------------------------

OUTPUT_VALUE_RE = re.compile(r"[A-Za-z0-9._/-]{0,200}")


def write_outputs(values: dict, path=None) -> None:
    """Appends key=value lines to $GITHUB_OUTPUT. Every value must be a closed-grammar token (no
    spaces, newlines or shell/Markdown metacharacters), so nothing submitted can reach a later job
    through an output unless it already passed a stricter check."""
    path = path or os.environ.get("GITHUB_OUTPUT")
    lines = []
    for key, value in values.items():
        value = str(value)
        if not re.fullmatch(r"[a-z][a-z0-9_]{0,39}", key) or not OUTPUT_VALUE_RE.fullmatch(value):
            raise ValueError(f"refusing to write output {key!r}: not a closed-grammar token")
        lines.append(f"{key}={value}\n")
    if path:
        with open(path, "a", encoding="utf-8") as handle:
            handle.writelines(lines)
    else:
        sys.stdout.writelines(lines)


def env_token(name: str, pattern) -> str:
    """An environment variable that must match `pattern` in full (job outputs and inputs arrive this
    way; each is checked again where it's used, whatever produced it)."""
    value = os.environ.get(name, "")
    if not pattern.fullmatch(value):
        raise Refusal("input", f"{name} isn't in the expected form")
    return value


def load_event(path=None) -> dict:
    path = path or os.environ.get("GITHUB_EVENT_PATH")
    if not path:
        raise Refusal("input", "GITHUB_EVENT_PATH isn't set")
    with open(path, encoding="utf-8") as handle:
        event = json.load(handle)
    if not isinstance(event, dict):
        raise Refusal("input", "the event payload isn't an object")
    return event


def maintainers() -> set:
    try:
        return set(rules.parse_maintainers(os.environ.get("THEME_MAINTAINER_IDS")))
    except ValueError as error:
        raise Refusal("input", str(error))


def error(message: str) -> None:
    """A GitHub Actions error annotation. Messages here never carry submitted text, but `%`, CR and
    LF are still escaped per the workflow-command rules so one can't start a second command."""
    text = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error::{text}")


def notice(message: str) -> None:
    text = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice::{text}")


# --- the GitHub REST API --------------------------------------------------------------------------

class ApiError(RuntimeError):
    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status = status


class GitHub:
    """A minimal REST client (urllib). The token comes from the environment (GH_TOKEN), never from
    argv; the repository is $GITHUB_REPOSITORY, checked against REPO_RE."""

    def __init__(self, token: str, repo: str, api: str = "https://api.github.com"):
        if not REPO_RE.fullmatch(repo or ""):
            raise Refusal("input", "GITHUB_REPOSITORY isn't owner/name")
        self.token = token
        self.repo = repo
        self.api = api

    @classmethod
    def from_env(cls):
        return cls(os.environ.get("GH_TOKEN", ""), os.environ.get("GITHUB_REPOSITORY", ""))

    def request(self, method: str, path: str, body=None):
        url = self.api + path.replace("{repo}", self.repo)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        req.add_header("User-Agent", "mars-dawn-website-theme-submission")
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read(8 * 1024 * 1024 + 1)
                if len(raw) > 8 * 1024 * 1024:
                    raise ApiError(response.status, f"{method} {path}: response over 8 MB")
                return json.loads(raw.decode("utf-8")) if raw else None
        except urllib.error.HTTPError as err:
            raise ApiError(err.code, f"{method} {path}: HTTP {err.code}") from None
        except (urllib.error.URLError, TimeoutError, ValueError) as err:
            raise ApiError(0, f"{method} {path}: {type(err).__name__}") from None

    def get(self, path: str):
        return self.request("GET", path)

    def paginate(self, path: str, max_pages: int) -> list:
        """Every item of a list endpoint, 100 per page; more than max_pages pages fails closed."""
        out = []
        sep = "&" if "?" in path else "?"
        for page in range(1, max_pages + 1):
            items = self.get(f"{path}{sep}per_page=100&page={page}")
            if not isinstance(items, list):
                raise ApiError(0, f"GET {path}: not a list")
            out.extend(items)
            if len(items) < 100:
                return out
        raise ApiError(0, f"GET {path}: more than {max_pages} pages; refusing to guess")


# --- the bot's validation comment -----------------------------------------------------------------

def is_bot_comment(comment) -> bool:
    user = comment.get("user") if isinstance(comment, dict) else None
    return (isinstance(user, dict) and user.get("id") == BOT_ID and user.get("login") == BOT_LOGIN
            and user.get("type") == "Bot")


def marker_of(comment):
    """(verdict, sha256 or None) for a bot comment whose first line is the marker, else None."""
    if not is_bot_comment(comment):
        return None
    body = comment.get("body")
    if not isinstance(body, str):
        return None
    match = MARKER_RE.fullmatch(body.split("\n", 1)[0].rstrip("\r"))
    if not match:
        return None
    return match.group(1), (None if match.group(2) == "none" else match.group(2))


def validation_comments(comments: list) -> list:
    """[(comment, verdict, sha)] for the bot's marker comments, oldest first."""
    out = []
    for comment in comments:
        marker = marker_of(comment)
        if marker is not None:
            out.append((comment, marker[0], marker[1]))
    return out


def issue_comments(api: GitHub, number: int) -> list:
    return api.paginate(f"/repos/{{repo}}/issues/{number}/comments", MAX_COMMENT_PAGES)


def label_names(issue_or_pr) -> set:
    labels = issue_or_pr.get("labels") if isinstance(issue_or_pr, dict) else None
    return {label.get("name") for label in labels or [] if isinstance(label, dict) and isinstance(label.get("name"), str)}


def user_of(obj) -> tuple:
    """(login, id) of an issue's or PR's `user`, both checked against their grammars."""
    user = obj.get("user") if isinstance(obj, dict) else None
    login = user.get("login") if isinstance(user, dict) else None
    uid = user.get("id") if isinstance(user, dict) else None
    if not fullmatch(LOGIN_RE, login) or not int_not_bool(uid) or uid <= 0:
        raise Refusal("input", "the author's login or id isn't in the expected form")
    return login, uid


def noreply(login: str, uid: int) -> str:
    return f"{uid}+{login}@users.noreply.github.com"


def author_github(doc: dict):
    author = doc.get("author")
    github = author.get("github") if isinstance(author, dict) else None
    return github if isinstance(github, str) else None


def author_matches(doc: dict, login: str) -> bool:
    github = author_github(doc)
    return github is not None and fullmatch(LOGIN_RE, github) and ascii_lower(github) == ascii_lower(login)


# --- what a bot theme PR may contain --------------------------------------------------------------

# Size caps per kind of file a bot PR carries (a page is build_pages.py output).
SIZE_CAPS = {"source": MAX_THEME_BYTES, "theme": MAX_THEME_BYTES, "preview": rules.MAX_PREVIEW_BYTES,
             "index": 1024 * 1024, "published": 1024 * 1024, "page": 4 * 1024 * 1024}


def bot_path_kind(path: str, tid: str, version: str):
    """The kind of a path a bot PR for theme `tid` `version` may change, or None. The same set
    check_theme_index.py's bot class allows (one themes/<id>/, that id's v1 folder, index.json,
    published.json, generated pages), narrowed to exactly this id and version."""
    if path == f"{rules.THEMES_REL}/{tid}/theme.json":
        return "source"
    base = f"{rules.V1_REL}/{tid}/{version}/"
    if path == base + "theme.json":
        return "theme"
    if path in (base + "preview-light.png", base + "preview-dark.png"):
        return "preview"
    if path == rules.INDEX_REL:
        return "index"
    if path == rules.PUBLISHED_REL:
        return "published"
    if rules.is_generated_page(path) and rules.path_is_safe(path):
        return "page"
    return None


def required_paths(tid: str, version: str) -> set:
    base = f"{rules.V1_REL}/{tid}/{version}/"
    return {f"{rules.THEMES_REL}/{tid}/theme.json", base + "theme.json", base + "preview-light.png",
            base + "preview-dark.png", rules.INDEX_REL, rules.PUBLISHED_REL}
