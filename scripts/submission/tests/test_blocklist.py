"""The account blocklist (#195): the loader's format rules and fail-closed behaviour, the three gate
modes refusing a blocked opener or author, the neutral comment and label, and the workflow facts the
design depends on (the list is read from the default branch's own checkout; no pull_request_target)."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import support as s
from support import common

import comment
import gate

sys.path.insert(0, str(common.ROOT / "scripts"))
import check_workflows  # noqa: E402

WORKFLOWS = common.ROOT / ".github" / "workflows"
MAINTAINER = ("redtear1115", s.OWNER_ID)
RENAMED = ("renamedjane", s.OPENER[1])   # the opener's account after a rename: same id, another login
SECRET = "SECRET-REASON"


def out_dir():
    return Path(tempfile.mkdtemp(prefix="blocklist-gate-")) / "theme"


def write(content, name="blocklist.json") -> Path:
    path = Path(tempfile.mkdtemp(prefix="blocklist-test-")) / name
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
    return path


def raw(ids=(), logins=(), **extra) -> bytes:
    return json.dumps({"schema": 1, "ids": list(ids), "logins": list(logins), **extra}).encode("utf-8")


def listed(ids=(), logins=()) -> common.Blocklist:
    return common.load_blocklist(write(raw(ids, logins)))


def checkout_with(content=None) -> Path:
    """A stand-in for this checkout (common.ROOT) holding the given blocklist bytes, or none."""
    root = Path(tempfile.mkdtemp(prefix="blocklist-root-"))
    if content is not None:
        target = root / common.BLOCKLIST_REL
        target.parent.mkdir(parents=True)
        target.write_bytes(content)
    return root


class LoadBlocklist(unittest.TestCase):
    def refusal(self, path) -> common.Refusal:
        with self.assertRaises(common.Refusal) as caught:
            common.load_blocklist(path)
        self.assertEqual(caught.exception.code, "blocklist")
        return caught.exception

    def test_the_committed_file_loads(self):
        # CI's guard: a list that would fail closed in the workflows can't be merged unnoticed. Entries
        # may be added; only the format is pinned here.
        path = common.ROOT / common.BLOCKLIST_REL
        self.assertFalse(path.is_symlink())
        self.assertEqual(set(json.loads(path.read_text(encoding="utf-8"))), {"schema", "ids", "logins"})
        self.assertIsInstance(common.load_blocklist(), common.Blocklist)

    def test_an_empty_list_blocks_nobody(self):
        nobody = listed()
        for login, uid in (s.OPENER, s.STRANGER, ("anyone", 1)):
            self.assertFalse(nobody.blocks(login, uid))

    def test_a_valid_list_keeps_ids_and_lowercases_logins(self):
        loaded = listed(ids=[5550001, 999999999999], logins=["JaneDoe", "mallory"])
        self.assertEqual(loaded.ids, frozenset({5550001, 999999999999}))
        self.assertEqual(loaded.logins, frozenset({"janedoe", "mallory"}))

    def test_missing_file(self):
        self.refusal(Path(tempfile.mkdtemp()) / "nope.json")

    def test_a_directory_is_not_a_blocklist(self):
        self.refusal(Path(tempfile.mkdtemp()))

    def test_empty_file(self):
        self.refusal(write(b""))

    def test_not_json(self):
        self.refusal(write(b"{ not json"))

    def test_json_array(self):
        self.refusal(write(b"[]"))

    def test_duplicate_key(self):
        self.refusal(write('{"schema": 1, "ids": [], "ids": [], "logins": []}'))

    def test_extra_key(self):
        self.refusal(write(raw(reasons=[])))

    def test_missing_key(self):
        for key in ("schema", "ids", "logins"):
            doc = json.loads(raw())
            del doc[key]
            with self.subTest(missing=key):
                self.refusal(write(json.dumps(doc)))

    def test_schema_other_than_the_integer_1(self):
        for value in (2, 0, True, "1", 1.0, None):
            doc = json.loads(raw())
            doc["schema"] = value
            with self.subTest(schema=value):
                self.refusal(write(json.dumps(doc)))

    def test_ids_must_be_a_list_of_positive_user_ids(self):
        for ids in (["123"], [True], [0], [-5], [1.5], [None], [[1]], [10 ** 12], 5, "123", {"1": 1}):
            with self.subTest(ids=ids):
                doc = json.loads(raw())
                doc["ids"] = ids
                self.refusal(write(json.dumps(doc)))

    def test_logins_must_be_a_list_of_github_logins(self):
        for logins in ([5], ["bad login"], ["-x"], [""], [None], ["x-"], ["jane\n"], ["a" * 40], ["a--b"], "janedoe", {}):
            with self.subTest(logins=logins):
                doc = json.loads(raw())
                doc["logins"] = logins
                self.refusal(write(json.dumps(doc)))

    def test_a_symlink_to_a_valid_file_is_refused(self):
        target = write(raw())
        link = target.parent / "link.json"
        link.symlink_to(target)
        self.assertEqual(common.load_blocklist(target).ids, frozenset())
        self.refusal(link)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "needs mkfifo")
    def test_a_fifo_is_refused_without_blocking(self):
        path = Path(tempfile.mkdtemp()) / "fifo.json"
        os.mkfifo(path)
        self.refusal(path)

    def test_oversized_file(self):
        self.refusal(write(raw() + b" " * (64 * 1024)))

    def test_exactly_64_kib_is_accepted(self):
        content = raw()
        self.assertEqual(common.load_blocklist(write(content + b" " * (64 * 1024 - len(content)))).ids, frozenset())

    def test_invalid_utf8(self):
        self.refusal(write(b'\xff\xfe{"schema": 1, "ids": [], "logins": []}'))
        self.refusal(write(b'{"schema": 1, "ids": [], "logins": ["\xe9"]}'))

    def test_a_utf8_byte_order_mark_is_refused(self):
        self.refusal(write(b"\xef\xbb\xbf" + raw()))

    def test_deeply_nested_json_is_refused_not_a_crash(self):
        self.refusal(write(b"[" * 60000))

    def test_the_refusal_never_quotes_the_file(self):
        planted = [
            raw(reasons=SECRET),
            raw(ids=[SECRET]),
            raw(logins=[SECRET + " bad login"]),
            ('{"schema": 1, "ids": [], "logins": [], "x": "%s", "x": "%s"}' % (SECRET, SECRET)).encode(),
            ("not json " + SECRET).encode(),
            ('{"schema": "%s", "ids": [], "logins": []}' % SECRET).encode(),
            b"\xff" + SECRET.encode(),
        ]
        messages = set()
        for content in planted:
            refusal = self.refusal(write(content))
            self.assertNotIn(SECRET, refusal.message)
            self.assertNotIn(SECRET, str(refusal))
            messages.add(refusal.message)
        self.assertTrue(all(message.startswith(common.BLOCKLIST_REL) for message in messages))

    def test_login_match_is_ascii_case_insensitive(self):
        self.assertTrue(listed(logins=["JaneDoe"]).blocks("janedoe", 1))
        self.assertTrue(listed(logins=["janedoe"]).blocks("JANEDOE", 1))
        self.assertTrue(listed(logins=["janedoe"]).blocks("JaneDoe", s.STRANGER[1]))
        self.assertFalse(listed(logins=["janedoe"]).blocks("janedoe2", 1))

    def test_login_match_is_not_unicode_folded(self):
        kelvin = "Kevin"            # "Kevin" with the Kelvin sign: str.lower() would fold it to "kevin"
        self.assertEqual(kelvin.lower(), "kevin")
        self.assertEqual(common.ascii_lower(kelvin), kelvin)
        self.assertIsNone(common.LOGIN_RE.fullmatch(kelvin))
        self.refusal(write(raw(logins=[kelvin])))
        self.assertFalse(listed(logins=["kevin"]).blocks(kelvin, 1))

    def test_id_match_survives_a_rename(self):
        blocked = listed(ids=[s.OPENER[1]])
        self.assertTrue(blocked.blocks(*s.OPENER))
        self.assertTrue(blocked.blocks("a-new-login", s.OPENER[1]))
        self.assertFalse(blocked.blocks(*s.STRANGER))
        self.assertFalse(listed(ids=[s.OPENER[1]], logins=["someoneelse"]).blocks("mallory", s.STRANGER[1]))

    def test_odd_inputs_never_match_or_crash(self):
        blocked = listed(ids=[1], logins=["janedoe"])
        self.assertFalse(blocked.blocks("other", True))     # True == 1, but a bool is not an id
        self.assertFalse(blocked.blocks("other", 1.0))
        self.assertFalse(blocked.blocks("other", "1"))
        self.assertFalse(blocked.blocks(None, None))
        self.assertFalse(blocked.blocks(b"janedoe", None))

    def test_the_default_path_is_this_checkouts_file(self):
        with mock.patch.object(common, "ROOT", checkout_with(raw(logins=["janedoe"]))):
            self.assertTrue(common.load_blocklist().blocks(*s.OPENER))
        with mock.patch.object(common, "ROOT", checkout_with(None)):
            self.assertEqual(self.refusal(None).code, "blocklist")


class SubmissionBlocked(unittest.TestCase):
    BLOCKED = {"action": "reject", "reason": "blocked", "number": 7}

    def run_gate(self, blocklist, opener=s.OPENER, body=None, comments=None, open_issues=None, full=True):
        body = s.issue_body(s.theme_text(s.theme_doc())) if body is None else body
        issue = s.issue(body=body, opener=opener)
        routes = {f"/repos/{s.REPO}/issues/7": issue}
        if full:
            routes[f"/repos/{s.REPO}/issues/7/comments"] = list(comments or [])
            routes[f"/repos/{s.REPO}/issues"] = open_issues if open_issues is not None else [issue]
        api = s.FakeGitHub(routes)
        out = out_dir()
        return gate.submission(api, s.issues_event(), out, blocklist), out, api

    def test_blocked_by_login(self):
        outputs, out, api = self.run_gate(listed(logins=["janedoe"]))
        self.assertEqual(outputs, self.BLOCKED)
        self.assertFalse((out / "theme.json").exists())
        self.assertEqual(api.writes, [])

    def test_blocked_even_when_the_bot_already_validated_the_same_theme(self):
        sha = common.sha256(s.expected_bytes(s.theme_text(s.theme_doc())))
        outputs, out, _ = self.run_gate(listed(logins=["janedoe"]), comments=[s.bot_comment(1, "valid", sha)])
        self.assertEqual(outputs, self.BLOCKED)
        self.assertFalse((out / "theme.json").exists())

    def test_blocked_before_the_open_submissions_query(self):
        outputs, out, api = self.run_gate(listed(logins=["janedoe"]), full=False)   # no /issues routes at all
        self.assertEqual(outputs, self.BLOCKED)
        self.assertFalse((out / "theme.json").exists())
        self.assertEqual(api.writes, [])

    def test_blocked_wins_over_too_many_open_submissions(self):
        four = [s.issue(number=n, body="x") for n in (7, 8, 9, 10)]
        self.assertEqual(self.run_gate(listed(logins=["janedoe"]), open_issues=four)[0], self.BLOCKED)

    def test_blocked_wins_over_a_body_that_would_be_rejected_anyway(self):
        for body in ("no theme here", s.issue_body("{ not json"), s.issue_body(s.theme_text(s.theme_doc()), dco=False)):
            outputs, out, _ = self.run_gate(listed(logins=["janedoe"]), body=body)
            self.assertEqual(outputs, self.BLOCKED)
            self.assertFalse((out / "theme.json").exists())

    def test_blocked_by_id_with_a_different_login(self):
        outputs, out, _ = self.run_gate(listed(ids=[s.OPENER[1]]), opener=RENAMED)
        self.assertEqual(outputs, self.BLOCKED)
        self.assertFalse((out / "theme.json").exists())

    def test_blocked_when_the_case_differs(self):
        self.assertEqual(self.run_gate(listed(logins=["JANEDOE"]))[0], self.BLOCKED)
        self.assertEqual(self.run_gate(listed(logins=["janedoe"]), opener=("JaneDoe", s.OPENER[1]))[0], self.BLOCKED)

    def test_unblocked_opener_is_validated_as_before(self):
        text = s.theme_text(s.theme_doc())
        outputs, out, api = self.run_gate(listed(ids=[s.STRANGER[1]], logins=[s.STRANGER[0]]))
        self.assertEqual((outputs["action"], outputs["reason"], outputs["opener"]), ("validate", "changed", "janedoe"))
        self.assertEqual((out / "theme.json").read_bytes(), s.expected_bytes(text))
        self.assertEqual(api.writes, [])

    def test_a_broken_list_stops_the_gate_before_it_reads_anything(self):
        api = s.FakeGitHub({})                       # any GET would be an ApiError, not a Refusal
        with mock.patch.object(common, "ROOT", checkout_with(b"{ broken")):
            with self.assertRaises(common.Refusal) as caught:
                gate.submission(api, s.issues_event(), out_dir())
        self.assertEqual(caught.exception.code, "blocklist")

    def test_without_a_list_argument_the_checkouts_list_decides(self):
        issue = s.issue(body=s.issue_body(s.theme_text(s.theme_doc())))
        api = s.FakeGitHub({f"/repos/{s.REPO}/issues/7": issue})
        with mock.patch.object(common, "ROOT", checkout_with(raw(logins=["janedoe"]))):
            outputs = gate.submission(api, s.issues_event(), out_dir())
        self.assertEqual(outputs, self.BLOCKED)


class ApproveBlocked(unittest.TestCase):
    def setUp(self):
        os.environ.pop("THEME_BASE_BRANCH", None)

    def prepare(self, opener=s.OPENER, comments=None, body=None):
        text = s.theme_text(s.theme_doc(github=opener[0]))
        sha = common.sha256(s.expected_bytes(text))
        issue = s.issue(body=s.issue_body(text) if body is None else body, opener=opener)
        routes = {f"/repos/{s.REPO}/issues/7": issue,
                  f"/repos/{s.REPO}/issues/7/comments": [s.bot_comment(1, "valid", sha)] if comments is None else comments,
                  f"/repos/{s.REPO}/issues/7/events": []}
        routes.update(s.base_routes())
        event = s.issues_event(action="labeled", label=common.APPROVED_LABEL, sender=MAINTAINER)
        return s.FakeGitHub(routes), event, out_dir()

    def refused(self, blocklist, **kwargs):
        api, event, out = self.prepare(**kwargs)
        with self.assertRaises(common.Refusal) as caught:
            gate.approve(api, event, {s.OWNER_ID}, out, blocklist)
        self.assertEqual(caught.exception.code, "blocked", caught.exception.message)
        self.assertFalse((out / "theme.json").exists())
        self.assertEqual(api.writes, [])
        return caught.exception.message

    def test_blocked_by_login(self):
        self.refused(listed(logins=["janedoe"]))

    def test_blocked_by_id_with_a_different_login(self):
        self.refused(listed(ids=[s.OPENER[1]]), opener=RENAMED)

    def test_blocked_when_the_case_differs(self):
        self.refused(listed(logins=["JANEDOE"]))

    def test_blocked_before_the_body_is_read(self):
        self.refused(listed(logins=["janedoe"]), body="no theme here", comments=[])

    def test_the_message_names_the_issue_and_nothing_from_the_list(self):
        message = self.refused(listed(ids=[999, s.OPENER[1]], logins=["janedoe", "evilother"]))
        self.assertIn("#7", message)
        for leaked in ("evilother", "janedoe", "999", str(s.OPENER[1])):
            self.assertNotIn(leaked, message)

    def test_unblocked_opener_still_builds(self):
        api, event, out = self.prepare()
        outputs = gate.approve(api, event, {s.OWNER_ID}, out, listed(ids=[s.STRANGER[1]], logins=[s.STRANGER[0]]))
        self.assertEqual((outputs["action"], outputs["login"], outputs["user_id"]), ("build", "janedoe", s.OPENER[1]))
        self.assertTrue((out / "theme.json").exists())

    def test_other_labels_and_non_maintainers_are_skipped_not_refused(self):
        api, event, out = self.prepare()
        blocklist = listed(logins=["janedoe"])
        event["label"]["name"] = "theme-report"
        self.assertEqual(gate.approve(api, event, {s.OWNER_ID}, out, blocklist)["reason"], "other-label")
        event["label"]["name"] = common.APPROVED_LABEL
        event["sender"] = s.user(*s.STRANGER)
        self.assertEqual(gate.approve(api, event, {s.OWNER_ID}, out, blocklist)["reason"], "sender-not-maintainer")


class FromPrBlocked(unittest.TestCase):
    def prepare(self, author=s.OPENER, extra_file=False):
        theme = s.expected_bytes(s.theme_text(s.theme_doc(github=author[0])))
        routes = s.pr_routes(theme=theme, author=author)
        if extra_file:
            routes[f"/repos/{s.REPO}/pulls/31/files"].append(
                {"filename": ".github/workflows/site.yml", "status": "modified", "sha": "d" * 40})
        event = {"sender": s.user(*MAINTAINER), "inputs": {"pr": "31"}}
        return s.FakeGitHub(routes), event, out_dir()

    def refused(self, blocklist, **kwargs):
        api, event, out = self.prepare(**kwargs)
        with self.assertRaises(common.Refusal) as caught:
            gate.from_pr(api, event, "31", {s.OWNER_ID}, out, blocklist)
        self.assertEqual(caught.exception.code, "blocked", caught.exception.message)
        self.assertFalse((out / "theme.json").exists())
        self.assertEqual(api.writes, [])
        return caught.exception.message

    def test_blocked_by_login(self):
        self.assertIn("PR #31", self.refused(listed(logins=["janedoe"])))

    def test_blocked_by_id_with_a_different_login(self):
        self.refused(listed(ids=[s.OPENER[1]]), author=RENAMED)

    def test_blocked_when_the_case_differs(self):
        self.refused(listed(logins=["JaneDoe"]))

    def test_blocked_before_the_files_are_read(self):
        self.refused(listed(logins=["janedoe"]), extra_file=True)   # would be refused as pr-files otherwise

    def test_the_message_names_nothing_from_the_list(self):
        message = self.refused(listed(ids=[999], logins=["janedoe", "evilother"]))
        for leaked in ("evilother", "janedoe", "999"):
            self.assertNotIn(leaked, message)

    def test_unblocked_author_still_builds(self):
        api, event, out = self.prepare()
        outputs = gate.from_pr(api, event, "31", {s.OWNER_ID}, out, listed(logins=[s.STRANGER[0]]))
        self.assertEqual((outputs["action"], outputs["login"]), ("build", "janedoe"))
        self.assertTrue((out / "theme.json").exists())


class FailClosedMain(unittest.TestCase):
    """gate.main() with a list that can't be loaded: exit 1, an error line, no outputs, no theme file."""

    def run_main(self, mode, event, routes, extra_env=None, broken=True):
        tmp = Path(tempfile.mkdtemp(prefix="blocklist-main-"))
        event_path, output_path = tmp / "event.json", tmp / "github-output"
        event_path.write_text(json.dumps(event), encoding="utf-8")
        env = {"GITHUB_EVENT_PATH": str(event_path), "GITHUB_REPOSITORY": s.REPO, "GITHUB_OUTPUT": str(output_path),
               "THEME_MAINTAINER_IDS": str(s.OWNER_ID), "THEME_BASE_BRANCH": "", "GH_TOKEN": "test-token"}
        env.update(extra_env or {})
        api = s.FakeGitHub(routes)
        stdout = io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.dict(os.environ, env))
            stack.enter_context(mock.patch.object(common.GitHub, "from_env", return_value=api))
            if broken:
                stack.enter_context(mock.patch.object(common, "load_blocklist",
                                                      side_effect=common.Refusal("blocklist", "x")))
            stack.enter_context(contextlib.redirect_stdout(stdout))
            code = gate.main([mode, "--out", str(tmp / "theme")])
        written = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        return code, written, stdout.getvalue(), tmp / "theme"

    def check(self, mode, event, routes, extra_env=None):
        code, written, printed, theme_dir = self.run_main(mode, event, routes, extra_env)
        self.assertEqual(code, 1)
        self.assertEqual(written, "")
        self.assertIn("::error::refused (blocklist)", printed)
        self.assertNotIn(f"gate {mode}:", printed)
        self.assertFalse(theme_dir.exists())
        # The same run with the repo's real (empty) list goes through, so the failure above is the list's.
        code, written, printed, theme_dir = self.run_main(mode, event, routes, extra_env, broken=False)
        self.assertEqual(code, 0, printed)
        self.assertIn("action=", written)

    def test_submission(self):
        issue = s.issue(body=s.issue_body(s.theme_text(s.theme_doc())))
        routes = {f"/repos/{s.REPO}/issues/7": issue, f"/repos/{s.REPO}/issues/7/comments": [],
                  f"/repos/{s.REPO}/issues": [issue]}
        self.check("submission", s.issues_event(), routes)

    def test_approve(self):
        text = s.theme_text(s.theme_doc())
        routes = {f"/repos/{s.REPO}/issues/7": s.issue(body=s.issue_body(text)),
                  f"/repos/{s.REPO}/issues/7/comments": [s.bot_comment(1, "valid", common.sha256(s.expected_bytes(text)))],
                  f"/repos/{s.REPO}/issues/7/events": []}
        routes.update(s.base_routes())
        event = s.issues_event(action="labeled", label=common.APPROVED_LABEL, sender=MAINTAINER)
        self.check("approve", event, routes)

    def test_from_pr(self):
        event = {"sender": s.user(*MAINTAINER), "inputs": {"pr": "31"}}
        self.check("from-pr", event, s.pr_routes(), {"PR_NUMBER": "31"})

    def test_a_missing_list_in_the_checkout_fails_the_real_loader_the_same_way(self):
        issue = s.issue(body=s.issue_body(s.theme_text(s.theme_doc())))
        routes = {f"/repos/{s.REPO}/issues/7": issue}
        with mock.patch.object(common, "ROOT", checkout_with(None)):
            code, written, printed, theme_dir = self.run_main("submission", s.issues_event(), routes, broken=False)
        self.assertEqual(code, 1)
        self.assertEqual(written, "")
        self.assertIn("::error::refused (blocklist)", printed)
        self.assertFalse(theme_dir.exists())


class CommentBlocked(unittest.TestCase):
    def run_main(self, reason, comments=()):
        api = s.FakeGitHub({f"/repos/{s.REPO}/issues/7/comments": list(comments)})
        env = {"NUMBER": "7", "GATE_ACTION": "reject", "GATE_REASON": reason}
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.dict(os.environ, env))
            from_env = stack.enter_context(mock.patch.object(common.GitHub, "from_env", return_value=api))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            code = comment.main([])
        return code, api, from_env

    def test_the_body_is_the_neutral_fixed_text(self):
        body = comment.body_for("reject", "blocked", None, None)
        self.assertEqual(common.MARKER_RE.fullmatch(body.split("\n")[0]).group(1, 2), ("rejected", "none"))
        self.assertIn(comment.REJECTIONS["blocked"], body)
        for word in ("list", "block", "reason"):
            self.assertNotIn(word, body.lower())

    def test_a_blocked_rejection_comments_then_adds_the_label(self):
        code, api, from_env = self.run_main("blocked")
        self.assertEqual(code, 0)
        self.assertEqual(api.writes, [
            ("POST", f"/repos/{s.REPO}/issues/7/comments", {"body": comment.body_for("reject", "blocked", None, None)}),
            ("POST", f"/repos/{s.REPO}/issues/7/labels", {"labels": ["theme-blocked"]}),
        ])
        self.assertEqual(from_env.call_count, 1)

    def test_the_label_is_added_even_when_the_comment_is_already_there(self):
        body = comment.body_for("reject", "blocked", None, None)
        existing = {"id": 5, "body": body, "user": s.user(common.BOT_LOGIN, common.BOT_ID, "Bot")}
        code, api, _ = self.run_main("blocked", [existing])
        self.assertEqual(code, 0)
        self.assertEqual(api.writes, [("POST", f"/repos/{s.REPO}/issues/7/labels", {"labels": ["theme-blocked"]})])

    def test_another_rejection_adds_no_label(self):
        code, api, _ = self.run_main("dco")
        self.assertEqual(code, 0)
        self.assertEqual([(method, path.rsplit("/", 1)[1]) for method, path, _ in api.writes], [("POST", "comments")])

    def test_no_other_rejection_reason_adds_a_label(self):
        self.assertEqual(common.BLOCKED_LABEL, "theme-blocked")
        for reason in ("too-large", "no-theme", "json", "site-rules", "too-many"):
            _, api, _ = self.run_main(reason)
            self.assertEqual([path.rsplit("/", 1)[1] for _, path, _ in api.writes], ["comments"], reason)


def load(name):
    return check_workflows.load((WORKFLOWS / name).read_text(encoding="utf-8"), name)


class Workflows(unittest.TestCase):
    GATES = ("theme-submission.yml", "theme-approve.yml", "theme-from-pr.yml")

    def test_gate_jobs_check_out_the_triggering_default_branch_commit(self):
        for name in self.GATES:
            steps = load(name)["jobs"]["gate"]["steps"]
            checkouts = [st for st in steps if str(st.get("uses", "")).startswith("actions/checkout@")]
            self.assertEqual(len(checkouts), 1, name)
            self.assertFalse({"ref", "repository", "path"} & set(checkouts[0]["with"]), name)
            runs = " ".join(st.get("run", "") for st in steps)
            self.assertIn("scripts/submission/gate.py", runs, name)

    def test_no_theme_workflow_runs_on_pull_request_target(self):
        names = sorted(path.name for path in WORKFLOWS.glob("theme-*.yml"))
        self.assertIn("theme-submission.yml", names)
        for name in names:
            self.assertNotIn("pull_request_target", str(load(name)["on"]), name)

    def test_the_comment_job_still_holds_only_issues_write_and_the_gate_jobs_nothing(self):
        self.assertEqual(load("theme-submission.yml")["jobs"]["comment"]["permissions"], {"issues": "write"})
        for name in self.GATES:
            self.assertEqual(load(name)["jobs"]["gate"]["permissions"], {}, name)


if __name__ == "__main__":
    unittest.main()
