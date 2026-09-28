"""Synthetic GitHub event payloads, API responses and theme fixtures for the submission tests."""
import base64
import copy
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))
import common  # noqa: E402
from common import rules  # noqa: E402

REPO = "redtear1115/mars-dawn-website"
OWNER_ID = 16503101
OPENER = ("janedoe", 5550001)
STRANGER = ("mallory", 6660002)

# Every string a hostile submission might use to break out of where it's put (plan W2 Done-when).
HOSTILE = "```````````` ${{ github.token }} $(id) `id` @org/team [x](//e.x) <!-- x --> ‮"


def theme_doc(tid="olympus-dusk", version="1.0.0", github="janedoe", name="Olympus Dusk") -> dict:
    doc = rules.fixture_theme(tid, version, github)
    doc["name"] = {"en": name}
    return doc


def theme_text(doc: dict) -> str:
    return json.dumps(doc, indent=2, ensure_ascii=False)


def issue_body(theme: str, dco=True, fenced=True, crlf=False) -> str:
    field = f"```json\n{theme}\n```" if fenced else theme
    body = (f"### {common.THEME_HEADING}\n\n{field}\n\n### {common.DCO_HEADING}\n\n"
            f"- [{'X' if dco else ' '}] {common.DCO_LABEL}")
    return body.replace("\n", "\r\n") if crlf else body


def expected_bytes(theme: str) -> bytes:
    return (theme.strip("\n") + "\n").encode("utf-8")


def user(login, uid, kind="User") -> dict:
    return {"login": login, "id": uid, "type": kind}


def issue(number=7, body="", state="open", opener=OPENER, labels=(common.SUBMISSION_LABEL,)) -> dict:
    return {"number": number, "state": state, "body": body, "user": user(*opener),
            "labels": [{"name": name} for name in labels]}


def bot_comment(cid, verdict, sha, extra="") -> dict:
    marker = f"<!-- marsdawn-theme-validation v1 verdict={verdict} sha256={sha or 'none'} -->"
    return {"id": cid, "body": marker + "\n" + extra, "user": user(common.BOT_LOGIN, common.BOT_ID, "Bot")}


def person_comment(cid, body, who=STRANGER) -> dict:
    return {"id": cid, "body": body, "user": user(*who)}


def issues_event(number=7, action="opened", label=None, sender=OPENER) -> dict:
    event = {"action": action, "issue": {"number": number}, "sender": user(*sender)}
    if label is not None:
        event["label"] = {"name": label}
    return event


class FakeGitHub(common.GitHub):
    """Serves GET from a {path: response} table (list endpoints paginated 100 per page) and records
    every write. A path missing from the table is a 404, so a test sees any unexpected call."""

    def __init__(self, routes=None):
        super().__init__("test-token", REPO)
        self.routes = dict(routes or {})
        self.writes = []

    def request(self, method, path, body=None):
        path = path.replace("{repo}", self.repo)
        if method != "GET":
            self.writes.append((method, path, copy.deepcopy(body)))
            if method == "POST" and path.endswith("/pulls"):
                return {"number": 901}
            return {}
        parts = urlsplit(path)
        if parts.path not in self.routes:
            raise common.ApiError(404, f"GET {parts.path}: HTTP 404")
        value = copy.deepcopy(self.routes[parts.path])
        query = parse_qs(parts.query)
        if isinstance(value, list) and "page" in query:
            page = int(query["page"][0])
            return value[(page - 1) * 100:page * 100]
        return value


# --- a git user's pull request, as the API describes it -----------------------------------------------

def pr_routes(number=31, theme: bytes = None, author=OPENER, files=None, mode="100644", commits=None,
              labels=(), state="open", base_repo=REPO, tid="olympus-dusk") -> dict:
    theme = theme if theme is not None else expected_bytes(theme_text(theme_doc(tid)))
    blob = rules.git_blob_id(theme)
    head = "a" * 40
    trees = {"root": "1" * 40, "themes": "2" * 40, "folder": "3" * 40}
    login, uid = author
    if commits is None:
        commits = [signed_commit("b" * 40, login, uid)]
    if files is None:
        files = [{"filename": f"themes/{tid}/theme.json", "status": "added", "sha": blob}]
    return {
        f"/repos/{REPO}/pulls/{number}": {"number": number, "state": state, "user": user(login, uid),
                                           "head": {"sha": head}, "base": {"repo": {"full_name": base_repo}},
                                           "labels": [{"name": n} for n in labels], "commits": len(commits)},
        f"/repos/{REPO}/pulls/{number}/files": files,
        f"/repos/{REPO}/pulls/{number}/commits": commits,
        f"/repos/{REPO}/git/commits/{head}": {"tree": {"sha": trees["root"]}},
        f"/repos/{REPO}/git/trees/{trees['root']}": {"tree": [{"path": "themes", "type": "tree", "sha": trees["themes"]}]},
        f"/repos/{REPO}/git/trees/{trees['themes']}": {"tree": [{"path": tid, "type": "tree", "sha": trees["folder"]}]},
        f"/repos/{REPO}/git/trees/{trees['folder']}": {"tree": [{"path": "theme.json", "type": "blob", "mode": mode,
                                                                 "sha": blob, "size": len(theme)}]},
        f"/repos/{REPO}/git/blobs/{blob}": {"encoding": "base64", "content": base64.b64encode(theme).decode()},
    }


def signed_commit(sha, login, uid, email=None, signoff=True, gh_author_id=None) -> dict:
    email = email or common.noreply(login, uid)
    message = "Add my theme\n"
    if signoff:
        message += f"\nSigned-off-by: Jane Doe <{email}>\n"
    return {"sha": sha, "commit": {"message": message, "author": {"name": "Jane Doe", "email": email}},
            "author": {"id": gh_author_id if gh_author_id is not None else uid, "login": login}}
