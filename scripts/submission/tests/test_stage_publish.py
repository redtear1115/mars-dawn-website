"""stage.py (build job) then publish.py (commit job) on throwaway git repositories, with a stand-in
for build_themes.py: the artifact rules, the commit's text and identity, and every refusal.

tests/test_integration.py runs the real build_themes.py and kit instead, where a kit CLI is at hand.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

import support as s
from support import common, rules

import publish
import stage

TID, VERSION = "olympus-dusk", "1.0.0"

# A stand-in for build_themes.py: publishes themes/<id>/theme.json the way the real one lays it out,
# plus one generated page. PLANT (env) makes it misbehave in one way.
FAKE_BUILD = r'''
import json, os, sys, hashlib
from pathlib import Path
sys.path.insert(0, os.environ["SCRIPTS"])
import check_theme_index as rules
root = Path.cwd()
plant = os.environ.get("PLANT", "")
doc = json.loads((root / "themes" / "olympus-dusk" / "theme.json").read_text())
data = (root / "themes" / "olympus-dusk" / "theme.json").read_bytes()
base = f"{doc['id']}/{doc['version']}/"
v1 = root / "public" / "themes" / "v1"
(v1 / base).mkdir(parents=True, exist_ok=True)
files = {"theme.json": data, "preview-light.png": rules.make_png(), "preview-dark.png": rules.make_png(height=3)}
if plant == "bad-png":
    files["preview-dark.png"] = b"GIF89a"
for name, body in files.items():
    (v1 / base / name).write_bytes(body)
published = json.loads((v1 / "published.json").read_text())
published.update({base + n: hashlib.sha256(b).hexdigest() for n, b in files.items()})
(v1 / "published.json").write_text(rules.dumps(dict(sorted(published.items()))))
index = {"schemaVersion": 1, "generatedAt": "2026-10-01T00:00:00Z",
         "themes": [rules.index_entry(doc, hashlib.sha256(data).hexdigest())], "revoked": []}
(v1 / "index.json").write_text(rules.dumps(index))
(root / "public" / "themes" / "index.html").write_text("<p>gallery</p>\n")
if plant == "outside":
    (root / "scripts" / "evil.py").write_text("print('x')\n")
if plant == "delete":
    (root / "public" / "themes" / "old.html").unlink()
if plant == "fail":
    sys.exit(3)
'''


def git(repo, *args, env=None):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise AssertionError(f"git {args}: {result.stderr}")
    return result.stdout


def make_repo() -> Path:
    repo = Path(tempfile.mkdtemp(prefix="theme-stage-")) / "site"
    for rel, text in {
        "themes/revoked.json": "[]\n",
        "public/themes/v1/index.json": rules.dumps({"schemaVersion": 1, "generatedAt": "2026-09-01T00:00:00Z",
                                                    "themes": [], "revoked": []}),
        "public/themes/v1/published.json": "{}\n",
        "public/themes/index.html": "<p>empty</p>\n",
        "public/themes/old.html": "<p>old</p>\n",
        "scripts/keep.py": "\n",
        "fake_build.py": FAKE_BUILD,
    }.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    git(repo.parent, "init", "--quiet", "-b", "main", str(repo))
    git(repo, "add", "-A")
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.com", GIT_COMMITTER_NAME="t",
               GIT_COMMITTER_EMAIL="t@example.com")
    git(repo, "commit", "--quiet", "-m", "base", env=env)
    return repo


def gate_values(data: bytes, **over) -> dict:
    values = {"source": "issue", "number": 7, "sha256": common.sha256(data), "theme_id": TID, "version": VERSION,
              "author_change": False}
    values.update(over)
    return values


class Staged(unittest.TestCase):
    """Runs stage.stage() in a throwaway repo with the fake build; returns what it produced."""

    def setUp(self):
        self.repo = make_repo()
        self.base = git(self.repo, "rev-parse", "HEAD").strip()
        self.data = s.expected_bytes(s.theme_text(s.theme_doc()))
        self.theme = self.repo.parent / "theme.json"
        self.theme.write_bytes(self.data)
        self.out = self.repo.parent / "staged"
        self.out.mkdir()
        self._roots = (stage.ROOT, publish.ROOT)
        stage.ROOT = self.repo
        os.environ["SCRIPTS"] = str(common.ROOT / "scripts")

    def tearDown(self):
        stage.ROOT, publish.ROOT = self._roots
        os.environ.pop("PLANT", None)
        shutil.rmtree(self.repo.parent, ignore_errors=True)

    def run_stage(self, plant="", **over):
        if plant:
            os.environ["PLANT"] = plant
        return stage.stage(self.theme, Path("/nonexistent/marsdawn"), self.out, gate_values(self.data, **over),
                           build_cmd=[sys.executable, str(self.repo / "fake_build.py")])

    def refused(self, code, plant="", **over):
        with self.assertRaises(common.Refusal) as caught:
            self.run_stage(plant, **over)
        self.assertEqual(caught.exception.code, code, caught.exception.message)
        return caught.exception.message


class Stage(Staged):
    def test_stage_commits_the_theme_first_and_lists_only_allowed_paths(self):
        before = int(time.time())
        outputs = self.run_stage()
        manifest_text = (self.out / "manifest.json").read_text()
        manifest = json.loads(manifest_text)
        self.assertEqual(outputs["manifest_sha256"], common.sha256(manifest_text.encode()))
        self.assertEqual(outputs["base_sha"], self.base)
        self.assertEqual(manifest["base"], self.base)
        self.assertGreaterEqual(manifest["epoch"], before)
        self.assertEqual(sorted(manifest["files"]), sorted(common.required_paths(TID, VERSION) | {"public/themes/index.html"}))
        # The theme was committed before the build ran, as the bot, at the recorded time.
        log = git(self.repo, "log", "-1", "--format=%an <%ae> %ct", "--", "themes").strip()
        self.assertEqual(log, f"{common.BOT_NAME} <{common.BOT_EMAIL}> {manifest['epoch']}")
        self.assertEqual((self.out / "files" / f"themes/{TID}/theme.json").read_bytes(), self.data)

    def test_other_bytes_than_the_gates_are_refused(self):
        self.theme.write_bytes(self.data.replace(b"Olympus", b"Olympos"))
        self.refused("hash")

    def test_other_id_than_the_gates_is_refused(self):
        self.refused("input", theme_id="other-theme")

    def test_a_build_that_writes_outside_the_theme_is_refused(self):
        self.assertIn("scripts/evil.py", self.refused("path", plant="outside"))

    def test_a_build_that_deletes_is_refused(self):
        self.assertIn("deleted", self.refused("path", plant="delete"))

    def test_a_failed_build_is_refused(self):
        self.refused("build", plant="fail")

    def test_a_dirty_checkout_is_refused(self):
        (self.repo / "stray.txt").write_text("x")
        self.refused("git")


class Publish(Staged):
    """The artifact goes from stage.py to publish.py in a fresh clone of the base commit."""

    def setUp(self):
        super().setUp()
        outputs = self.run_stage()
        self.clone = self.repo.parent / "clone"
        git(self.repo.parent, "clone", "--quiet", str(self.repo), str(self.clone))
        git(self.clone, "checkout", "--quiet", "--detach", self.base)
        publish.ROOT = self.clone
        self.values = dict(gate_values(self.data), login="janedoe", user_id=s.OPENER[1], base_branch="main",
                           base_sha=self.base, manifest_sha256=outputs["manifest_sha256"])

    def refused(self, code, values=None):
        with self.assertRaises(common.Refusal) as caught:
            manifest, contents = publish.verify_artifact(self.out, values or self.values)
            publish.make_commit(values or self.values, manifest, contents)
        self.assertEqual(caught.exception.code, code, caught.exception.message)
        return caught.exception.message

    def test_commit_has_the_bot_identity_the_build_time_and_only_the_allowed_text(self):
        manifest, contents = publish.verify_artifact(self.out, self.values)
        sha = publish.make_commit(self.values, manifest, contents)
        info = git(self.clone, "log", "-1", "--format=%an <%ae>%n%cn <%ce>%n%ct%n%B", sha)
        lines = info.split("\n")
        self.assertEqual(lines[0], f"{common.BOT_NAME} <{common.BOT_EMAIL}>")
        self.assertEqual(lines[1], f"{common.BOT_NAME} <{common.BOT_EMAIL}>")
        self.assertEqual(lines[2], str(manifest["epoch"]))
        message = "\n".join(lines[3:]).rstrip("\n") + "\n"
        v1 = f"public/themes/v1/{TID}/{VERSION}/"
        self.assertEqual(message, "\n".join([
            f"Add theme {TID} {VERSION}", "",
            f"Theme: {TID} {VERSION}",
            "Submission: #7",
            f"themes/{TID}/theme.json sha256: {common.sha256(self.data)}",
            f"preview-light.png sha256: {common.sha256(contents[v1 + 'preview-light.png'])}",
            f"preview-dark.png sha256: {common.sha256(contents[v1 + 'preview-dark.png'])}",
            "DCO confirmed in #7 by janedoe", "",
            f"Co-authored-by: janedoe <{s.OPENER[1]}+janedoe@users.noreply.github.com>", ""]))
        changed = sorted(p for p in git(self.clone, "diff", "--name-only", self.base, sha).split("\n") if p)
        self.assertEqual(changed, sorted(contents))
        self.assertEqual(git(self.clone, "show", f"{sha}:themes/{TID}/theme.json").encode(), self.data)
        # The commit gets exactly the build's bytes, file for file.
        for path, data in contents.items():
            self.assertEqual((self.clone / path).read_bytes(), data)

    def test_pr_path_message_cites_the_pr_and_its_dco_source(self):
        values = dict(self.values, source="pr", number=31)
        manifest = json.loads((self.out / "manifest.json").read_text())
        contents = {p: (self.out / "files" / p).read_bytes() for p in manifest["files"]}
        message = publish.commit_message(values, contents)
        self.assertIn("Submission: PR #31\n", message)
        self.assertIn("DCO: Signed-off-by in PR #31\n", message)
        self.assertNotIn("DCO confirmed in", message)
        self.assertTrue(message.endswith(f"Co-authored-by: janedoe <{s.OPENER[1]}+janedoe@users.noreply.github.com>\n"))
        self.assertEqual(publish.branch_ref(values), "refs/heads/theme/pr-31")
        title, body = publish.pr_text(values, contents)
        self.assertEqual(title, f"Theme {TID} {VERSION} (from PR #31)")

    def test_pr_title_and_body_hold_no_display_strings(self):
        manifest, contents = publish.verify_artifact(self.out, self.values)
        title, body = publish.pr_text(self.values, contents)
        for text in (title, body):
            self.assertNotIn("Olympus Dusk", text)
            self.assertNotIn("Jane Doe", text)
            self.assertNotIn("Cool violet", text)
        self.assertIn("close and reopen", body)

    def test_open_pr_and_follow_up(self):
        manifest, contents = publish.verify_artifact(self.out, self.values)
        api = s.FakeGitHub({f"/repos/{s.REPO}/pulls": []})
        number, created = publish.open_pr(api, dict(self.values, author_change=True), contents)
        publish.follow_up(api, self.values, number, created)
        methods = [(m, p) for m, p, _ in api.writes]
        self.assertEqual(methods, [("POST", f"/repos/{s.REPO}/pulls"), ("POST", f"/repos/{s.REPO}/issues/901/labels"),
                                   ("POST", f"/repos/{s.REPO}/issues/7/comments")])
        self.assertEqual(api.writes[0][2]["head"], "theme/issue-7")
        self.assertEqual(api.writes[0][2]["base"], "main")
        self.assertEqual(api.writes[1][2], {"labels": [common.AUTHOR_CHANGE_LABEL]})

    def test_git_users_pr_is_closed_with_credit(self):
        api = s.FakeGitHub()
        publish.follow_up(api, dict(self.values, source="pr", number=31), 901, True)
        self.assertEqual([(m, p) for m, p, _ in api.writes],
                         [("POST", f"/repos/{s.REPO}/issues/31/comments"), ("PATCH", f"/repos/{s.REPO}/pulls/31")])
        self.assertEqual(api.writes[1][2], {"state": "closed"})

    def test_push_ref_is_only_ever_a_theme_branch(self):
        self.assertEqual(publish.branch_ref(self.values), "refs/heads/theme/issue-7")
        for bad in ({"source": "issue", "number": "7:refs/heads/main"}, {"source": "../main", "number": 7}):
            with self.assertRaises(common.Refusal):
                publish.branch_ref(bad)

    def test_manifest_from_elsewhere_is_refused(self):
        self.refused("artifact", dict(self.values, manifest_sha256="0" * 64))

    def test_extra_file_is_refused(self):
        path = self.out / "files" / "scripts" / "evil.py"
        path.parent.mkdir(parents=True)
        path.write_text("x")
        self.refused("artifact")

    def test_listed_extra_path_is_refused_by_path_rules(self):
        manifest = json.loads((self.out / "manifest.json").read_text())
        for rel in (".github/workflows/site.yml", "public/_headers", "themes/revoked.json",
                    "public/themes/v1/other-theme/1.0.0/theme.json", "themes/other-theme/theme.json"):
            path = self.out / "files" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"{}\n")
            manifest["files"][rel] = {"sha256": common.sha256(b"{}\n"), "size": 3}
            text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
            (self.out / "manifest.json").write_text(text)
            message = self.refused("path", dict(self.values, manifest_sha256=common.sha256(text.encode())))
            self.assertIn(rel, message)
            path.unlink()
            del manifest["files"][rel]

    def test_symlink_in_the_artifact_is_refused(self):
        os.symlink("/etc/passwd", self.out / "files" / "public" / "link.html")
        self.assertIn("symbolic link", self.refused("artifact"))

    def test_changed_byte_is_refused(self):
        target = self.out / "files" / "public" / "themes" / "index.html"
        target.write_text("<p>gallery!</p>\n")
        self.refused("artifact")

    def test_bad_preview_is_refused(self):
        self.tearDown()
        self.setUp_with_plant("bad-png")
        self.assertIn("PNG", self.refused("artifact"))

    def setUp_with_plant(self, plant):
        Staged.setUp(self)
        os.environ["PLANT"] = plant
        outputs = self.run_stage()
        self.clone = self.repo.parent / "clone"
        git(self.repo.parent, "clone", "--quiet", str(self.repo), str(self.clone))
        publish.ROOT = self.clone
        self.values = dict(gate_values(self.data), login="janedoe", user_id=s.OPENER[1], base_branch="main",
                           base_sha=self.base, manifest_sha256=outputs["manifest_sha256"])

    def test_gate_values_must_match_the_manifest(self):
        for key, value in (("theme_id", "other-theme"), ("version", "1.0.1"), ("number", 8), ("sha256", "0" * 64),
                           ("base_sha", "f" * 40), ("source", "pr")):
            self.refused("artifact", dict(self.values, **{key: value}))

    def test_stale_manifest_time_is_refused(self):
        manifest, contents = publish.verify_artifact(self.out, self.values)
        with self.assertRaises(common.Refusal):
            publish.verify_artifact(self.out, self.values, now=manifest["epoch"] + 7 * 3600)

    def test_checkout_at_another_commit_is_refused(self):
        (self.clone / "extra.txt").write_text("x")
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@e", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@e")
        git(self.clone, "add", "-A")
        git(self.clone, "commit", "--quiet", "-m", "moved", env=env)
        self.assertIn("base commit", self.refused("git"))

    def test_env_values_are_checked_again(self):
        env = {"SOURCE": "issue", "NUMBER": "7", "GATE_SHA256": "a" * 64, "THEME_ID": TID, "VERSION": VERSION,
               "LOGIN": "janedoe", "USER_ID": "5550001", "AUTHOR_CHANGE": "false", "BASE_BRANCH": "main",
               "BASE_SHA": "b" * 40, "MANIFEST_SHA256": "c" * 64}
        saved = {k: os.environ.get(k) for k in env}
        try:
            os.environ.update(env)
            self.assertEqual(publish.values_from_env()["user_id"], 5550001)
            for key, bad in (("LOGIN", "jane doe"), ("LOGIN", "@org/team"), ("BASE_BRANCH", "release"),
                             ("NUMBER", "7 && id"), ("THEME_ID", "Dawn"), ("SOURCE", "push")):
                os.environ[key] = bad
                with self.assertRaises(common.Refusal):
                    publish.values_from_env()
                os.environ[key] = env[key]
        finally:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value


if __name__ == "__main__":
    unittest.main()
