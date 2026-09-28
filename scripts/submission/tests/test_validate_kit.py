"""validate.py and kit_cli.py against a stand-in `marsdawn` (a small script answering like the kit
CLI); tests/test_integration.py uses the real one where it's available."""
import json
import os
import shutil
import stat
import sys
import tempfile
import unittest
from pathlib import Path

import support as s
from support import common

import kit_cli
import validate

FAKE_MARSDAWN = """#!{python}
import json, os, sys
args = sys.argv[1:]
mode = os.environ.get("FAKE_KIT", "ok")
if args == ["--version"]:
    print(os.environ.get("FAKE_VERSION", {version!r}))
    sys.exit(0)
if args[:2] == ["theme", "css"]:
    print(json.dumps({{"ok": True, "id": "dawn", "variables": "", "rules": ""}}))
    sys.exit(0)
if args[:2] == ["theme", "validate"]:
    if mode == "garbage":
        print("Segmentation fault")
        sys.exit(139)
    if mode == "invalid":
        print(json.dumps({{"ok": False, "issues": [{{"rule": "schema.unknownKey", "path": "/x",
                                                     "message": "unknown key `" + os.environ.get("HOSTILE", "") + "`"}}]}}))
        sys.exit(1)
    doc = json.loads(open(args[-1]).read())
    print(json.dumps({{"ok": True, "id": doc.get("id"), "issues": []}}))
    sys.exit(0)
sys.exit(64)
"""


def fake_binary(folder: Path) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "marsdawn"
    path.write_text(FAKE_MARSDAWN.format(python=sys.executable, version=kit_cli.expected_version()))
    path.chmod(0o755)
    return path


class Validate(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="validate-test-"))
        self.bin = fake_binary(self.tmp / "bin")

    def tearDown(self):
        os.environ.pop("FAKE_KIT", None)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_validate(self, doc, mode="ok", opener="janedoe"):
        os.environ["FAKE_KIT"] = mode
        os.environ["HOSTILE"] = s.HOSTILE
        data = s.expected_bytes(s.theme_text(doc))
        theme = self.tmp / "theme.json"
        theme.write_bytes(data)
        return validate.validate(self.bin, theme, common.sha256(data), opener)

    def test_kit_ok_and_site_rules_ok_is_valid(self):
        result = self.run_validate(s.theme_doc())
        self.assertEqual((result["verdict"], result["issues"], result["authorMatchesOpener"]), ("valid", [], True))

    def test_kit_invalid_keeps_its_messages(self):
        result = self.run_validate(s.theme_doc(), mode="invalid")
        self.assertEqual(result["verdict"], "invalid")
        self.assertEqual(result["issues"][0]["rule"], "schema.unknownKey")
        self.assertIn("$(id)", result["issues"][0]["message"])

    def test_garbage_from_the_kit_is_an_error_not_a_pass(self):
        self.assertEqual(self.run_validate(s.theme_doc(), mode="garbage")["verdict"], "error")

    def test_built_in_id_fails_the_site_rules(self):
        result = self.run_validate(s.theme_doc(tid="dawn"))
        self.assertEqual(result["verdict"], "invalid")
        self.assertEqual(result["issues"][0]["rule"], "site.id")

    def test_leading_zero_version_fails_the_site_rules(self):
        result = self.run_validate(s.theme_doc(version="01.0.0"))
        self.assertEqual(result["verdict"], "invalid")
        self.assertTrue(any("leading zeros" in i["message"] for i in result["issues"]))

    def test_author_mismatch_is_noted_not_failed(self):
        result = self.run_validate(s.theme_doc(github="someoneelse"))
        self.assertEqual((result["verdict"], result["authorMatchesOpener"]), ("valid", False))

    def test_artifact_with_other_bytes_is_refused(self):
        theme = self.tmp / "theme.json"
        theme.write_bytes(b"{}\n")
        with self.assertRaises(common.Refusal) as caught:
            validate.validate(self.bin, theme, "0" * 64, "janedoe")
        self.assertEqual(caught.exception.code, "hash")

    def test_symlinked_artifact_is_refused(self):
        target = self.tmp / "real.json"
        target.write_bytes(b"{}\n")
        os.symlink(target, self.tmp / "link.json")
        with self.assertRaises(OSError):
            validate.validate(self.bin, self.tmp / "link.json", common.sha256(b"{}\n"), "janedoe")


class KitCli(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="kit-cli-test-"))
        self.dir = self.tmp / "kit-cli"
        fake_binary(self.dir / "bin")
        bundle = self.dir / "bin" / "MarsDawnKit_MarsDawnThemes.bundle"
        bundle.mkdir()
        (bundle / "ThemeStyles.json").write_text("{}")
        (self.dir / "tree.sha256").write_text(kit_cli.tree_hash(self.dir / "bin") + "\n")

    def tearDown(self):
        os.environ.pop("FAKE_VERSION", None)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_recorded_tree_verifies(self):
        self.assertEqual(kit_cli.verify(self.dir), self.dir / "bin" / "marsdawn")

    def test_cache_key_is_the_pinned_commit(self):
        self.assertRegex(kit_cli.cache_key(), r"^theme-kit-cli-v1-[0-9a-f]{40}$")

    def test_changed_resource_fails_the_tree_hash(self):
        (self.dir / "bin" / "MarsDawnKit_MarsDawnThemes.bundle" / "ThemeStyles.json").write_text('{"x": 1}')
        with self.assertRaises(kit_cli.KitError) as caught:
            kit_cli.verify(self.dir)
        self.assertIn("tree hash", str(caught.exception))

    def test_added_file_fails_the_tree_hash(self):
        (self.dir / "bin" / "extra.dylib").write_bytes(b"\0")
        with self.assertRaises(kit_cli.KitError):
            kit_cli.verify(self.dir)

    def test_exec_bit_change_fails_the_tree_hash(self):
        path = self.dir / "bin" / "MarsDawnKit_MarsDawnThemes.bundle" / "ThemeStyles.json"
        path.chmod(path.stat().st_mode | stat.S_IXUSR)
        with self.assertRaises(kit_cli.KitError):
            kit_cli.verify(self.dir)

    def test_other_version_is_refused(self):
        os.environ["FAKE_VERSION"] = "0.0.1"
        with self.assertRaises(kit_cli.KitError) as caught:
            kit_cli.verify(self.dir)
        self.assertIn("--version", str(caught.exception))

    def test_missing_record_is_refused(self):
        (self.dir / "tree.sha256").unlink()
        with self.assertRaises(kit_cli.KitError):
            kit_cli.verify(self.dir)


if __name__ == "__main__":
    unittest.main()
