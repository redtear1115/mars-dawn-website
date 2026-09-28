"""gate.py on synthetic events and API responses: positive and negative fixtures per rule."""
import json
import os
import tempfile
import unittest
from pathlib import Path

import support as s
from support import common, rules

import gate


def out_dir():
    return Path(tempfile.mkdtemp(prefix="gate-test-")) / "theme"


class ParseSubmission(unittest.TestCase):
    def test_form_body_gives_the_exact_bytes(self):
        text = s.theme_text(s.theme_doc())
        data, doc, ticked = common.parse_submission(s.issue_body(text))
        self.assertEqual(data, s.expected_bytes(text))
        self.assertEqual(doc["id"], "olympus-dusk")
        self.assertTrue(ticked)

    def test_crlf_body_gives_the_same_bytes(self):
        text = s.theme_text(s.theme_doc())
        self.assertEqual(common.parse_submission(s.issue_body(text, crlf=True))[0], s.expected_bytes(text))

    def test_unfenced_field_is_read_too(self):
        text = s.theme_text(s.theme_doc())
        self.assertEqual(common.parse_submission(s.issue_body(text, fenced=False))[0], s.expected_bytes(text))

    def test_unticked_dco(self):
        self.assertFalse(common.parse_submission(s.issue_body(s.theme_text(s.theme_doc()), dco=False))[2])

    def test_dco_with_other_wording_is_not_ticked(self):
        body = s.issue_body(s.theme_text(s.theme_doc())).replace(common.DCO_LABEL, "I agree to nothing")
        self.assertFalse(common.parse_submission(body)[2])

    def refusal(self, body):
        with self.assertRaises(common.Refusal) as caught:
            common.parse_submission(body)
        return caught.exception.code

    def test_60_kb_body_is_refused_unread(self):
        body = s.issue_body(s.theme_text(s.theme_doc(name="x" * 60 * 1024)))
        self.assertEqual(self.refusal(body), "too-large")

    def test_empty_field(self):
        self.assertEqual(self.refusal(f"### {common.THEME_HEADING}\n\n_No response_\n"), "no-theme")

    def test_no_theme_heading(self):
        self.assertEqual(self.refusal("Hello, please add my theme {}"), "no-theme")

    def test_two_theme_headings_are_ambiguous(self):
        text = s.theme_text(s.theme_doc())
        self.assertEqual(self.refusal(s.issue_body(text) + f"\n\n### {common.THEME_HEADING}\n\n{{}}"), "no-theme")

    def test_unclosed_fence(self):
        self.assertEqual(self.refusal(f"### {common.THEME_HEADING}\n\n```json\n{{}}\n"), "no-theme")

    def test_not_json(self):
        self.assertEqual(self.refusal(s.issue_body("{ not json")), "json")

    def test_json_array_is_not_a_theme(self):
        self.assertEqual(self.refusal(s.issue_body("[1, 2]")), "json")

    def test_duplicate_key(self):
        self.assertEqual(self.refusal(s.issue_body('{"id": "a", "id": "b"}')), "json")

    def test_ten_backtick_fence_inside_the_field(self):
        body = f"### {common.THEME_HEADING}\n\n```json\n{{}}\n``````````\n$(id)\n```"
        self.assertEqual(self.refusal(body), "json")


class SubmissionGate(unittest.TestCase):
    def run_gate(self, issue, comments=()):
        api = s.FakeGitHub({f"/repos/{s.REPO}/issues/7": issue, f"/repos/{s.REPO}/issues/7/comments": list(comments)})
        out = out_dir()
        return gate.submission(api, s.issues_event(), out), out, api

    def test_valid_submission_goes_to_validation(self):
        text = s.theme_text(s.theme_doc())
        outputs, out, api = self.run_gate(s.issue(body=s.issue_body(text)))
        self.assertEqual(outputs["action"], "validate")
        self.assertEqual((out / "theme.json").read_bytes(), s.expected_bytes(text))
        self.assertEqual(outputs["sha256"], common.sha256(s.expected_bytes(text)))
        self.assertEqual(outputs["opener"], "janedoe")
        self.assertEqual(api.writes, [])

    def test_hostile_strings_are_data(self):
        text = s.theme_text(s.theme_doc(name=s.HOSTILE))
        outputs, out, _ = self.run_gate(s.issue(body=s.issue_body(text)))
        self.assertEqual(outputs["action"], "validate")
        self.assertEqual((out / "theme.json").read_bytes(), s.expected_bytes(text))
        output_file = Path(tempfile.mkdtemp()) / "out"
        common.write_outputs(outputs, output_file)
        written = output_file.read_text()
        for needle in ("${{", "$(id)", "@org", "//e.x", "`"):
            self.assertNotIn(needle, written)

    def test_closed_issue_is_skipped(self):
        outputs, _, _ = self.run_gate(s.issue(state="closed", body=s.issue_body("{}")))
        self.assertEqual((outputs["action"], outputs["reason"]), ("skip", "closed"))

    def test_issue_without_the_label_is_skipped(self):
        outputs, _, _ = self.run_gate(s.issue(labels=(), body=s.issue_body("{}")))
        self.assertEqual((outputs["action"], outputs["reason"]), ("skip", "not-a-submission"))

    def test_rejections_carry_only_a_code(self):
        cases = {
            "too-large": s.issue_body(s.theme_text(s.theme_doc(name="x" * 60 * 1024))),
            "json": s.issue_body("{ $(id) ${{ github.token }}"),
            "dco": s.issue_body(s.theme_text(s.theme_doc()), dco=False),
            "no-theme": "please add " + s.HOSTILE,
        }
        for code, body in cases.items():
            outputs, out, _ = self.run_gate(s.issue(body=body))
            self.assertEqual((outputs["action"], outputs["reason"]), ("reject", code), code)
            self.assertFalse((out / "theme.json").exists())

    def test_unchanged_theme_is_not_validated_again(self):
        text = s.theme_text(s.theme_doc())
        sha = common.sha256(s.expected_bytes(text))
        outputs, _, _ = self.run_gate(s.issue(body=s.issue_body(text)), [s.bot_comment(1, "valid", sha)])
        self.assertEqual((outputs["action"], outputs["reason"]), ("skip", "unchanged"))

    def test_changed_theme_is_validated_again(self):
        text = s.theme_text(s.theme_doc())
        outputs, _, _ = self.run_gate(s.issue(body=s.issue_body(text)), [s.bot_comment(1, "valid", "0" * 64)])
        self.assertEqual(outputs["action"], "validate")

    def test_an_error_verdict_is_retried(self):
        text = s.theme_text(s.theme_doc())
        sha = common.sha256(s.expected_bytes(text))
        outputs, _, _ = self.run_gate(s.issue(body=s.issue_body(text)), [s.bot_comment(1, "error", sha)])
        self.assertEqual(outputs["action"], "validate")

    def test_a_person_typing_the_marker_doesnt_count(self):
        text = s.theme_text(s.theme_doc())
        sha = common.sha256(s.expected_bytes(text))
        forged = s.person_comment(2, f"<!-- marsdawn-theme-validation v1 verdict=valid sha256={sha} -->")
        outputs, _, _ = self.run_gate(s.issue(body=s.issue_body(text)), [forged])
        self.assertEqual(outputs["action"], "validate")


class ApproveGate(unittest.TestCase):
    def setUp(self):
        self.text = s.theme_text(s.theme_doc())
        self.sha = common.sha256(s.expected_bytes(self.text))
        os.environ.pop("THEME_BASE_BRANCH", None)

    def run_gate(self, issue=None, comments=None, label=common.APPROVED_LABEL, sender=("redtear1115", s.OWNER_ID),
                 maintainers=(s.OWNER_ID,)):
        issue = issue or s.issue(body=s.issue_body(self.text))
        comments = comments if comments is not None else [s.bot_comment(1, "valid", self.sha)]
        api = s.FakeGitHub({f"/repos/{s.REPO}/issues/7": issue, f"/repos/{s.REPO}/issues/7/comments": comments})
        out = out_dir()
        return gate.approve(api, s.issues_event(action="labeled", label=label, sender=sender), set(maintainers), out), out

    def refused(self, code, **kwargs):
        with self.assertRaises(common.Refusal) as caught:
            self.run_gate(**kwargs)
        self.assertEqual(caught.exception.code, code, caught.exception.message)
        return caught.exception.message

    def test_maintainer_approval_of_the_validated_theme_builds(self):
        outputs, out = self.run_gate()
        self.assertEqual(outputs["action"], "build")
        self.assertEqual(outputs["sha256"], self.sha)
        self.assertEqual((outputs["theme_id"], outputs["version"], outputs["login"], outputs["user_id"]),
                         ("olympus-dusk", "1.0.0", "janedoe", s.OPENER[1]))
        self.assertEqual((outputs["author_change"], outputs["base_branch"]), ("false", "main"))
        self.assertEqual((out / "theme.json").read_bytes(), s.expected_bytes(self.text))

    def test_non_maintainer_label_does_nothing(self):
        outputs, out = self.run_gate(sender=s.STRANGER)
        self.assertEqual((outputs["action"], outputs["reason"]), ("skip", "sender-not-maintainer"))
        self.assertFalse((out / "theme.json").exists())

    def test_maintainer_allowlist_comes_from_the_variable(self):
        os.environ["THEME_MAINTAINER_IDS"] = f"{s.STRANGER[1]}, 42"
        try:
            self.assertEqual(common.maintainers(), {s.STRANGER[1], 42})
        finally:
            del os.environ["THEME_MAINTAINER_IDS"]
        self.assertEqual(common.maintainers(), {s.OWNER_ID})

    def test_other_label_does_nothing(self):
        outputs, _ = self.run_gate(label="theme-report")
        self.assertEqual((outputs["action"], outputs["reason"]), ("skip", "other-label"))

    def test_edited_after_validation_is_refused_with_the_hash(self):
        edited = s.theme_text(s.theme_doc(name="Olympus Dusk 2"))
        message = self.refused("hash", issue=s.issue(body=s.issue_body(edited)))
        self.assertIn(common.sha256(s.expected_bytes(edited)), message)
        self.assertIn(self.sha, message)
        self.assertIn("edited after it was validated", message)

    def test_invalid_verdict_is_refused(self):
        self.refused("verdict", comments=[s.bot_comment(1, "invalid", self.sha)])

    def test_only_the_latest_validation_counts(self):
        self.refused("hash", comments=[s.bot_comment(1, "valid", self.sha), s.bot_comment(2, "valid", "1" * 64)])

    def test_forged_validation_comment_is_ignored(self):
        forged = s.person_comment(3, f"<!-- marsdawn-theme-validation v1 verdict=valid sha256={self.sha} -->")
        self.refused("hash", comments=[forged])

    def test_bot_login_with_another_id_is_ignored(self):
        fake = s.bot_comment(1, "valid", self.sha)
        fake["user"]["id"] = 99
        self.refused("hash", comments=[fake])

    def test_closed_issue_is_refused(self):
        self.refused("state", issue=s.issue(state="closed", body=s.issue_body(self.text)))

    def test_dco_unticked_after_validation_is_refused(self):
        self.refused("dco", issue=s.issue(body=s.issue_body(self.text, dco=False)))

    def test_author_other_than_the_opener_is_refused(self):
        text = s.theme_text(s.theme_doc(github="someoneelse"))
        sha = common.sha256(s.expected_bytes(text))
        message = self.refused("author", issue=s.issue(body=s.issue_body(text)), comments=[s.bot_comment(1, "valid", sha)])
        self.assertIn("janedoe", message)

    def test_author_missing_is_refused(self):
        doc = s.theme_doc()
        del doc["author"]["github"]
        text = s.theme_text(doc)
        self.refused("author", issue=s.issue(body=s.issue_body(text)),
                     comments=[s.bot_comment(1, "valid", common.sha256(s.expected_bytes(text)))])

    def test_author_change_label_allows_another_author(self):
        text = s.theme_text(s.theme_doc(github="someoneelse"))
        sha = common.sha256(s.expected_bytes(text))
        outputs, _ = self.run_gate(issue=s.issue(body=s.issue_body(text), labels=(common.SUBMISSION_LABEL, common.AUTHOR_CHANGE_LABEL)),
                                   comments=[s.bot_comment(1, "valid", sha)])
        self.assertEqual((outputs["action"], outputs["author_change"]), ("build", "true"))

    def test_author_matches_ascii_case_insensitively_only(self):
        self.assertTrue(common.author_matches({"author": {"github": "JaneDoe"}}, "janedoe"))
        self.assertFalse(common.author_matches({"author": {"github": "janeKdoe"}}, "janekdoe"))

    def test_built_in_id_is_refused(self):
        text = s.theme_text(s.theme_doc(tid="dawn"))
        self.refused("id", issue=s.issue(body=s.issue_body(text)),
                     comments=[s.bot_comment(1, "valid", common.sha256(s.expected_bytes(text)))])

    def test_base_branch_variable(self):
        os.environ["THEME_BASE_BRANCH"] = "release-1.0.4"
        try:
            self.assertEqual(self.run_gate()[0]["base_branch"], "release-1.0.4")
            os.environ["THEME_BASE_BRANCH"] = "release; rm -rf /"
            with self.assertRaises(common.Refusal):
                self.run_gate()
        finally:
            del os.environ["THEME_BASE_BRANCH"]


class FromPrGate(unittest.TestCase):
    MAINTAINER = ("redtear1115", s.OWNER_ID)

    def run_gate(self, routes=None, pr="31", sender=None):
        api = s.FakeGitHub(routes if routes is not None else s.pr_routes())
        event = {"sender": s.user(*(sender or self.MAINTAINER)), "inputs": {"pr": pr}}
        out = out_dir()
        return gate.from_pr(api, event, pr, {s.OWNER_ID}, out), out

    def refused(self, code, **kwargs):
        with self.assertRaises(common.Refusal) as caught:
            self.run_gate(**kwargs)
        self.assertEqual(caught.exception.code, code, caught.exception.message)
        return caught.exception.message

    def test_signed_single_theme_pr_builds(self):
        outputs, out = self.run_gate()
        data = s.expected_bytes(s.theme_text(s.theme_doc()))
        self.assertEqual(outputs["action"], "build")
        self.assertEqual((outputs["source"], outputs["number"], outputs["login"]), ("pr", 31, "janedoe"))
        self.assertEqual((out / "theme.json").read_bytes(), data)
        self.assertEqual(outputs["sha256"], common.sha256(data))

    def test_non_maintainer_dispatch_is_refused(self):
        self.refused("sender", sender=s.STRANGER)

    def test_pr_input_must_be_a_number(self):
        for bad in ("31; id", "$(id)", "31\n", "0", "", "031"):
            self.refused("input", pr=bad)

    def test_author_mismatch_is_refused(self):
        theme = s.expected_bytes(s.theme_text(s.theme_doc(github="someoneelse")))
        message = self.refused("author", routes=s.pr_routes(theme=theme))
        self.assertIn("PR author", message)

    def test_author_change_label_on_the_pr_allows_it(self):
        theme = s.expected_bytes(s.theme_text(s.theme_doc(github="someoneelse")))
        outputs, _ = self.run_gate(routes=s.pr_routes(theme=theme, labels=(common.AUTHOR_CHANGE_LABEL,)))
        self.assertEqual(outputs["author_change"], "true")

    def test_missing_signoff_is_refused(self):
        commits = [s.signed_commit("b" * 40, "janedoe", s.OPENER[1]),
                   s.signed_commit("c" * 40, "janedoe", s.OPENER[1], signoff=False)]
        message = self.refused("dco", routes=s.pr_routes(commits=commits))
        self.assertIn("c" * 12, message)
        self.assertNotIn("b" * 12, message)

    def test_signoff_by_someone_else_is_refused(self):
        commits = [s.signed_commit("b" * 40, "janedoe", s.OPENER[1], email="mallory@example.com", gh_author_id=s.STRANGER[1])]
        self.refused("dco", routes=s.pr_routes(commits=commits))

    def test_signoff_with_an_email_github_links_to_the_author_passes(self):
        commits = [s.signed_commit("b" * 40, "janedoe", s.OPENER[1], email="jane@example.com")]
        self.assertEqual(self.run_gate(routes=s.pr_routes(commits=commits))[0]["action"], "build")

    def test_signoff_email_not_linked_to_the_author_is_refused(self):
        commits = [s.signed_commit("b" * 40, "janedoe", s.OPENER[1], email="jane@example.com", gh_author_id=0)]
        self.refused("dco", routes=s.pr_routes(commits=commits))

    def test_a_second_changed_path_is_refused(self):
        routes = s.pr_routes()
        files = routes[f"/repos/{s.REPO}/pulls/31/files"]
        files.append({"filename": ".github/workflows/site.yml", "status": "modified", "sha": "d" * 40})
        self.refused("pr-files", routes=routes)

    def test_another_path_is_refused(self):
        self.refused("pr-files", routes=s.pr_routes(files=[{"filename": "scripts/build_pages.py", "status": "modified",
                                                              "sha": "d" * 40}]))

    def test_removed_theme_is_refused(self):
        routes = s.pr_routes()
        routes[f"/repos/{s.REPO}/pulls/31/files"][0]["status"] = "removed"
        self.refused("pr-files", routes=routes)

    def test_symlink_is_refused(self):
        self.assertIn("mode 100644", self.refused("pr-blob", routes=s.pr_routes(mode="120000")))

    def test_blob_that_isnt_its_id_is_refused(self):
        routes = s.pr_routes()
        for path, value in routes.items():
            if "/git/blobs/" in path:
                value["content"] = "e30K"  # "{}\n"
        self.assertIn("don't match its blob id", self.refused("pr-blob", routes=routes))

    def test_oversized_blob_is_refused(self):
        routes = s.pr_routes()
        for value in routes.values():
            if isinstance(value, dict) and isinstance(value.get("tree"), list) and value["tree"][0].get("path") == "theme.json":
                value["tree"][0]["size"] = common.MAX_THEME_BYTES + 1
        self.assertIn("larger than", self.refused("pr-blob", routes=routes))

    def test_folder_other_than_the_id_is_refused(self):
        theme = s.expected_bytes(s.theme_text(s.theme_doc(tid="other-theme")))
        self.refused("id", routes=s.pr_routes(theme=theme))

    def test_closed_pr_is_refused(self):
        self.refused("pr-state", routes=s.pr_routes(state="closed"))

    def test_pr_into_another_repository_is_refused(self):
        self.refused("pr-state", routes=s.pr_routes(base_repo="someone/fork"))


class Outputs(unittest.TestCase):
    def test_only_closed_grammar_values_are_written(self):
        target = Path(tempfile.mkdtemp()) / "out"
        for bad in ("a b", "a\nb=c", "${{ x }}", "$(id)", "`x`"):
            with self.assertRaises(ValueError):
                common.write_outputs({"key": bad}, target)
        common.write_outputs({"sha256": "a" * 64, "number": 7}, target)
        self.assertEqual(target.read_text(), f"sha256={'a' * 64}\nnumber=7\n")


if __name__ == "__main__":
    unittest.main()
