"""comment.py and the fence rules: hostile kit messages stay inside one fence; the marker binds the
verdict to the gate's sha256; only the bot's own marker comment is ever edited."""
import json
import re
import tempfile
import unittest
from pathlib import Path

import support as s
from support import common

import comment

SHA = "ab" * 32
KIT = "f1c66e16509e63027b0679bda15eafbb8f3911a0"


def result(verdict="invalid", issues=None, sha=SHA, **extra):
    data = {"schema": 1, "sha256": sha, "kit": KIT, "verdict": verdict, "issues": issues or [],
            "authorMatchesOpener": True}
    data.update(extra)
    return data


def write_result(data) -> Path:
    path = Path(tempfile.mkdtemp()) / "result.json"
    path.write_text(json.dumps(data))
    return path


def outside_fences(body: str) -> str:
    """The comment with every fenced block removed (fences matched by their exact backtick run)."""
    out, fence = [], None
    for line in body.split("\n"):
        if fence is None:
            match = re.fullmatch(r"(`{3,})text", line)
            if match:
                fence = match.group(1)
                continue
            out.append(line)
        elif line == fence:
            fence = None
    assert fence is None, "a fence was left open"
    return "\n".join(out)


class Fences(unittest.TestCase):
    def test_fence_is_longer_than_any_backtick_run(self):
        self.assertEqual(common.fence_for("no ticks"), "```")
        self.assertEqual(common.fence_for("a ` b"), "```")
        self.assertEqual(common.fence_for("x" + "`" * 10 + "y"), "`" * 11)

    def test_hostile_text_cant_close_the_fence(self):
        block = common.fenced(s.HOSTILE + "\n" + "`" * 12 + "\n# heading", 5000)
        fence = block.split("\n", 1)[0][:-len("text")]
        self.assertGreater(len(fence), 12)
        self.assertTrue(block.endswith("\n" + fence))
        inner = block[len(fence) + len("text") + 1:-len(fence) - 1]
        self.assertNotIn("\n" + fence + "\n", "\n" + inner + "\n")

    def test_truncation_keeps_the_closing_fence(self):
        text = ("`" * 20 + "x" * 50 + "\n") * 2000
        block = common.fenced(text, 3000)
        fence = "`" * 21
        self.assertLessEqual(len(block), 3000)
        self.assertTrue(block.startswith(fence + "text\n"))
        self.assertTrue(block.endswith("[... truncated]\n" + fence))

    def test_truncation_never_splits_inside_the_fence_marker(self):
        for limit in range(120, 400, 7):
            block = common.fenced("`" * 40 + "\n" + "y" * 500, limit)
            self.assertLessEqual(len(block), limit)
            self.assertTrue(block.endswith("\n" + "`" * 41))


class Bodies(unittest.TestCase):
    def test_every_rejection_is_fixed_text(self):
        for reason in comment.REJECTIONS:
            body = comment.body_for("reject", reason, None, None)
            self.assertEqual(common.MARKER_RE.fullmatch(body.split("\n")[0]).group(1, 2), ("rejected", "none"))
            self.assertIn(comment.REJECTIONS[reason], body)

    def test_valid_body_names_the_sha(self):
        body = comment.body_for("validate", "changed", SHA, result("valid"))
        self.assertEqual(common.MARKER_RE.fullmatch(body.split("\n")[0]).group(1, 2), ("valid", SHA))
        self.assertIn(f"`{SHA}`", body)
        self.assertNotIn("author.github` in the theme isn't", body)

    def test_valid_body_notes_an_author_mismatch(self):
        body = comment.body_for("validate", "changed", SHA, result("valid", authorMatchesOpener=False))
        self.assertIn("isn't the GitHub account that opened this issue", body)

    def test_hostile_kit_messages_stay_in_the_fence(self):
        issues = [{"rule": "schema.unknownKey", "path": "/" + s.HOSTILE, "message": f"unknown key `{s.HOSTILE}`"}] * 3
        body = comment.body_for("validate", "changed", SHA, result("invalid", issues))
        outside = outside_fences(body)
        for needle in ("${{", "$(id)", "@org", "//e.x", "<!-- x", "‮"):
            self.assertNotIn(needle, outside)
        self.assertIn("$(id)", body)
        self.assertEqual(body.split("\n")[0], f"<!-- marsdawn-theme-validation v1 verdict=invalid sha256={SHA} -->")

    def test_huge_result_is_cut_inside_the_fence(self):
        issues = [{"rule": "r", "path": "", "message": "`" * 30 + "m" * 390}] * 100
        body = comment.body_for("validate", "changed", SHA, result("invalid", issues))
        self.assertLess(len(body), 65536)
        outside_fences(body)  # asserts every fence is closed
        self.assertIn("[... truncated]", body)

    def test_error_when_the_result_cant_vouch_for_the_sha(self):
        for data in (result("valid", sha="cd" * 32), {"schema": 2}, result("valid", kit="main"),
                     result("valid", issues=[{"rule": 1}])):
            loaded = comment.load_result(write_result(data), SHA)
            self.assertIsNone(loaded)
            body = comment.body_for("validate", "changed", SHA, loaded)
            self.assertTrue(body.startswith(f"<!-- marsdawn-theme-validation v1 verdict=error sha256={SHA} -->"))
        self.assertIsNone(comment.load_result(Path("/nonexistent/result.json"), SHA))
        self.assertEqual(comment.load_result(write_result(result("valid")), SHA)["verdict"], "valid")


class Upsert(unittest.TestCase):
    def api(self, comments):
        return s.FakeGitHub({f"/repos/{s.REPO}/issues/7/comments": comments})

    def test_first_comment_is_created(self):
        api = self.api([s.person_comment(1, "hello")])
        self.assertEqual(comment.upsert(api, 7, "BODY"), "created")
        self.assertEqual(api.writes, [("POST", f"/repos/{s.REPO}/issues/7/comments", {"body": "BODY"})])

    def test_the_bots_marker_comment_is_updated(self):
        api = self.api([s.bot_comment(11, "invalid", SHA), s.person_comment(12, "hello")])
        self.assertEqual(comment.upsert(api, 7, "BODY"), "updated")
        self.assertEqual(api.writes, [("PATCH", f"/repos/{s.REPO}/issues/comments/11", {"body": "BODY"})])

    def test_a_persons_marker_comment_is_never_edited(self):
        forged = s.person_comment(21, f"<!-- marsdawn-theme-validation v1 verdict=valid sha256={SHA} -->")
        api = self.api([forged])
        self.assertEqual(comment.upsert(api, 7, "BODY"), "created")
        self.assertEqual(api.writes[0][0], "POST")

    def test_the_bots_other_comments_are_left_alone(self):
        other = {"id": 31, "body": "Approved: pull request #9", "user": s.user(common.BOT_LOGIN, common.BOT_ID, "Bot")}
        api = self.api([other])
        self.assertEqual(comment.upsert(api, 7, "BODY"), "created")

    def test_unchanged_body_isnt_rewritten(self):
        existing = s.bot_comment(11, "valid", SHA)
        api = self.api([existing])
        self.assertEqual(comment.upsert(api, 7, existing["body"]), "unchanged")
        self.assertEqual(api.writes, [])


if __name__ == "__main__":
    unittest.main()
