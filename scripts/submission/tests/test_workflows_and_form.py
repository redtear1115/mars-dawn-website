"""The issue form, the simulator's Submit URL and the workflows agree with the scripts, and the
workflows keep their job split: which job holds which permission, runs what, on which runner."""
import re
import sys
import unittest

import support as s
from support import common

sys.path.insert(0, str(common.ROOT / "scripts"))
import check_workflows  # noqa: E402

WORKFLOWS = common.ROOT / ".github" / "workflows"
GITHUB_OWNED = re.compile(r"actions/(checkout|upload-artifact|download-artifact|cache/restore|cache/save)@[0-9a-f]{40}")


def load(name):
    return check_workflows.load((WORKFLOWS / name).read_text(encoding="utf-8"), name)


class Form(unittest.TestCase):
    def setUp(self):
        self.form = check_workflows.load((common.ROOT / common.TEMPLATE_REL).read_text(encoding="utf-8"), "form")

    def field(self, fid):
        found = [f for f in self.form["body"] if isinstance(f, dict) and f.get("id") == fid]
        self.assertEqual(len(found), 1, fid)
        return found[0]

    def test_theme_field_is_what_the_parser_reads(self):
        theme = self.field("theme")
        self.assertEqual(theme["type"], "textarea")
        self.assertEqual(theme["attributes"]["label"], common.THEME_HEADING)
        self.assertEqual(theme["attributes"]["render"], "json")
        self.assertEqual(theme["validations"]["required"], "true")

    def test_dco_checkbox_is_required_and_worded_as_the_parser_expects(self):
        dco = self.field("dco")
        self.assertEqual(dco["type"], "checkboxes")
        self.assertEqual(dco["attributes"]["label"], common.DCO_HEADING)
        options = dco["attributes"]["options"]
        self.assertEqual(len(options), 1)
        self.assertEqual(options[0]["label"], common.DCO_LABEL)
        self.assertEqual(options[0]["required"], "true")

    def test_form_says_what_becomes_public_forever(self):
        notes = " ".join(f["attributes"]["value"] for f in self.form["body"] if f.get("type") == "markdown")
        self.assertIn("What becomes public, permanently", notes)
        self.assertIn("GitHub username", notes)
        self.assertIn("never rewritten", notes)
        self.assertIn("permanently", common.DCO_LABEL)

    def test_form_labels_the_issue_as_a_submission(self):
        self.assertEqual(self.form["labels"], [common.SUBMISSION_LABEL])

    def test_simulator_submit_url_names_this_template_and_field(self):
        app = (common.ROOT / "public" / "assets" / "theme-sim" / "app.js").read_text(encoding="utf-8")
        template = common.TEMPLATE_REL.rsplit("/", 1)[1]
        self.assertIn(f'params.set("template", "{template}");', app)
        self.assertIn('params.set("theme", json);', app)
        self.assertIn('"https://github.com/redtear1115/mars-dawn-website/issues/new"', app)


class JobSplit(unittest.TestCase):
    def jobs(self, name):
        return load(name)["jobs"]

    def uses(self, job):
        return [step["uses"] for step in job.get("steps", []) if "uses" in step]

    def test_issue_workflows_trigger_only_on_issue_events(self):
        self.assertEqual(load("theme-submission.yml")["on"], {"issues": {"types": ["opened", "edited"]}})
        self.assertEqual(load("theme-approve.yml")["on"], {"issues": {"types": ["labeled"]}})
        self.assertEqual(list(load("theme-from-pr.yml")["on"]), ["workflow_dispatch"])
        self.assertEqual(list(load("theme-pr.yml")["on"]), ["workflow_call"])

    def test_every_workflow_defaults_to_no_permissions(self):
        for name in ("theme-submission.yml", "theme-approve.yml", "theme-from-pr.yml", "theme-pr.yml"):
            self.assertEqual(load(name)["permissions"], {}, name)

    def test_submission_jobs(self):
        jobs = self.jobs("theme-submission.yml")
        self.assertEqual(list(jobs), ["gate", "validate", "comment"])
        self.assertEqual((jobs["gate"]["runs-on"], jobs["gate"]["permissions"]), ("ubuntu-24.04", {}))
        self.assertEqual((jobs["validate"]["runs-on"], jobs["validate"]["permissions"]), ("macos-15", {}))
        self.assertEqual((jobs["comment"]["runs-on"], jobs["comment"]["permissions"]), ("ubuntu-24.04", {"issues": "write"}))
        for job in jobs.values():
            self.assertEqual(job["timeout-minutes"], "15")
        self.assertEqual(load("theme-submission.yml")["concurrency"],
                         {"group": "theme-submission-${{ github.event.issue.number }}", "cancel-in-progress": "true"})

    def test_pr_jobs(self):
        jobs = self.jobs("theme-pr.yml")
        self.assertEqual((jobs["build"]["runs-on"], jobs["build"]["permissions"]), ("macos-15", {}))
        self.assertEqual((jobs["commit"]["runs-on"], jobs["commit"]["permissions"]),
                         ("ubuntu-24.04", {"contents": "write", "pull-requests": "write", "issues": "write"}))
        for name in ("theme-approve.yml", "theme-from-pr.yml"):
            gate_job = self.jobs(name)["gate"]
            self.assertEqual((gate_job["runs-on"], gate_job["permissions"]), ("ubuntu-24.04", {}), name)
            publish_job = self.jobs(name)["publish"]
            self.assertEqual(publish_job["uses"], "./.github/workflows/theme-pr.yml")

    def test_write_jobs_run_no_third_party_code_and_no_kit(self):
        for name, job_id in (("theme-submission.yml", "comment"), ("theme-pr.yml", "commit")):
            job = self.jobs(name)[job_id]
            for uses in self.uses(job):
                self.assertRegex(uses, r"^actions/(checkout|download-artifact)@[0-9a-f]{40}$", f"{name} {job_id}")
            runs = " ".join(step.get("run", "") for step in job["steps"])
            self.assertIsNone(check_workflows.KIT_RE.search(runs), f"{name} {job_id}")
            self.assertEqual(re.findall(r"scripts/\S+\.py", runs),
                             ["scripts/submission/comment.py"] if job_id == "comment" else ["scripts/submission/publish.py"])

    def test_every_action_is_github_owned_and_pinned(self):
        for path in sorted(WORKFLOWS.glob("theme-*.yml")):
            for job in load(path.name)["jobs"].values():
                for uses in self.uses(job):
                    self.assertRegex(uses, GITHUB_OWNED, path.name)

    def test_checkouts_keep_no_credentials(self):
        for path in sorted(WORKFLOWS.glob("theme-*.yml")):
            for job in load(path.name)["jobs"].values():
                for step in job.get("steps", []):
                    if str(step.get("uses", "")).startswith("actions/checkout@"):
                        self.assertEqual(step["with"]["persist-credentials"], "false", path.name)

    def test_the_token_reaches_only_the_scripts_that_call_the_api(self):
        for path in sorted(WORKFLOWS.glob("theme-*.yml")):
            for job_id, job in load(path.name)["jobs"].items():
                for step in job.get("steps", []):
                    if "GH_TOKEN" in (step.get("env") or {}):
                        self.assertRegex(step["run"], r"scripts/submission/(gate|comment|publish)\.py", f"{path.name} {job_id}")
                        self.assertNotRegex(job["runs-on"], "macos", f"{path.name} {job_id}")

    def test_nothing_runs_on_a_self_hosted_runner(self):
        for path in sorted(WORKFLOWS.glob("theme-*.yml")):
            for job in load(path.name)["jobs"].values():
                self.assertNotIn("self-hosted", str(job.get("runs-on", "")), path.name)

    def test_repo_workflows_pass_the_static_check(self):
        self.assertEqual(check_workflows.check_dir(common.ROOT), [])


class Reader(unittest.TestCase):
    def test_self_test_plants_are_all_red(self):
        self.assertEqual(check_workflows.self_test(), 0)

    def test_reader_matches_pyyaml_where_installed(self):
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML isn't installed (CI); run locally to compare")

        def norm(v):
            if isinstance(v, dict):
                return {("on" if k is True else str(k)): norm(x) for k, x in v.items()}
            if isinstance(v, list):
                return [norm(x) for x in v]
            if isinstance(v, bool):
                return "true" if v else "false"
            return v if v is None else str(v)

        files = sorted(WORKFLOWS.glob("*.yml")) + [common.ROOT / common.TEMPLATE_REL]
        for path in files:
            text = path.read_text(encoding="utf-8")
            self.assertEqual(norm(check_workflows.load(text, path.name)), norm(yaml.safe_load(text)), path.name)

    def test_reader_refuses_what_it_doesnt_understand(self):
        for text in ("a: &x 1\nb: *x\n", "a: !!str 1\n", "a: [1,\n  2]\n", "a: 1\na: 2\n", "a:\n\t- 1\n",
                     "---\na: 1\n---\nb: 2\n", "? a\n: 1\n", "a: b: c\n", "<<: {a: 1}\n"):
            with self.assertRaises(check_workflows.YamlSubsetError, msg=repr(text)):
                check_workflows.load(text, "t")


if __name__ == "__main__":
    unittest.main()
