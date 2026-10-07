#!/usr/bin/env python3
"""Checks that vendor/kit-themes/<sha12>/ (scripts/sync_theme_kit.py) still matches the kit's
pinned commit and hasn't drifted or gone stale, without building the kit (Ubuntu CI can't: it's a
Swift package).

Three things this holds vendor/kit-themes/<sha12>/ to:

1. Every file the sync script copies verbatim from the kit (ThemeStyles.json, the four built-ins'
   theme.json, the ThemeFixtures tree, preview.css) byte-matches GitHub's raw copy of the pinned
   commit -- so a hand-edit, or a sync from the wrong commit, is caught even though this script
   can't regenerate the tree itself to compare against.
2. Every file's sha256 matches manifest.json's recorded hash -- so a file edited by hand *without*
   also touching the kit source (which rule 1 wouldn't catch, since the tampered copy might still
   equal... no, rule 1 already catches every one of these paths against GitHub) -- concretely,
   this rule is what catches a hand-edit to a file rule 1 doesn't reach: expected-css/,
   preview-sim.css and the sweep/ theme.json inputs, none of which exist in the kit itself.
3. The **sweep** covers every enum-fragment option/value in the vendored ThemeStyles.json and
   every scalar style option in the vendored ThemeNumbers.swift, parsed by
   sync_theme_kit.parse_scalar_options rather than a hand-kept list -- so a scalar option the kit
   adds later shows up as a missing sweep entry here too, the same way it would in
   sync_theme_kit.py itself, instead of both scripts silently agreeing on a list that's gone
   stale. Both are read from manifest.json's own "sweep" record: a manifest edited to claim
   coverage it doesn't have is still caught, since this rule cross-checks the record's *content*
   against the independently-parsed ThemeStyles.json/ThemeNumbers.swift, not just its hash.
4. The .sim-preview rescoping transform (scripts/rescope_css.py) still passes its own fixture
   (scripts/theme_sim/rescope_fixture.json) and regression cases.

--self-test plants one break of each kind and fails unless every one is caught, so a check that
can't fail doesn't pass for one that works.
"""
import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import rescope_css  # noqa: E402
import sync_theme_kit as sync  # noqa: E402

VENDOR_ROOT = ROOT / "vendor" / "kit-themes"
KIT_RAW = "https://raw.githubusercontent.com/redtear1115/mars-dawn-kit/{sha}/{path}"

# Vendored path -> the kit source path GitHub should serve it from, for every file copied
# verbatim (rule 1). expected-css/, preview-sim.css, sweep/ and manifest.json aren't here: they
# don't exist in the kit, so rule 2 (manifest hash) is what covers them instead.
KIT_SOURCE_PATHS = {
    "ThemeStyles.json": "Sources/MarsDawnThemes/Resources/ThemeStyles.json",
    "ThemeNumbers.swift": "Sources/MarsDawnThemes/ThemeNumbers.swift",
    "preview.css": "Sources/MarsDawnKit/Resources/Preview/preview.css",
}
for _id in sync.BUILT_IN_IDS:
    KIT_SOURCE_PATHS[f"Themes/{_id}/theme.json"] = f"Sources/MarsDawnThemes/Resources/Themes/{_id}/theme.json"


def _vendor_dir() -> Path:
    dirs = sorted(p for p in VENDOR_ROOT.iterdir() if p.is_dir()) if VENDOR_ROOT.is_dir() else []
    assert len(dirs) == 1, f"expected exactly one vendor/kit-themes/<sha>/ directory, found {[d.name for d in dirs]}"
    return dirs[0]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# --- Rule 1: byte-match against GitHub raw at the pinned commit --------------------------------

def fixture_source_paths(vendor: Path) -> dict:
    """Every ThemeFixtures/** path this vendor tree has -> its kit source path (same relative
    layout, under Tests/MarsDawnThemesTests/ThemeFixtures)."""
    out = {}
    fixtures_dir = vendor / "ThemeFixtures"
    if not fixtures_dir.is_dir():
        return out
    for f in fixtures_dir.rglob("*"):
        if f.is_file():
            rel = f.relative_to(vendor)
            out[str(rel)] = f"Tests/MarsDawnThemesTests/ThemeFixtures/{rel.relative_to('ThemeFixtures')}"
    return out


def check_drift(vendor: Path, kit_sha: str, fetch) -> list:
    """`fetch(kit_source_path) -> bytes | None` lets --self-test substitute a fake GitHub without
    a network call."""
    problems = []
    paths = dict(KIT_SOURCE_PATHS)
    paths.update(fixture_source_paths(vendor))
    for vendored_rel, kit_path in sorted(paths.items()):
        local = vendor / vendored_rel
        if not local.is_file():
            problems.append(f"{vendored_rel}: missing from the vendored tree")
            continue
        remote = fetch(kit_path)
        if remote is None:
            problems.append(f"{vendored_rel}: couldn't fetch {kit_path} from GitHub at {kit_sha}")
            continue
        if local.read_bytes() != remote:
            problems.append(f"{vendored_rel}: doesn't byte-match the kit's {kit_path} at {kit_sha}")
    return problems


def _real_fetch(kit_sha: str):
    def fetch(kit_path: str):
        url = KIT_RAW.format(sha=kit_sha, path=kit_path)
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return resp.read()
        except urllib.error.URLError:
            return None
    return fetch


# --- Rule 2: manifest hashes ---------------------------------------------------------------

def check_manifest_hashes(vendor: Path, manifest: dict) -> list:
    problems = []
    for rel, want in sorted(manifest.get("files", {}).items()):
        path = vendor / rel
        if not path.is_file():
            problems.append(f"{rel}: missing (manifest.json expects it)")
            continue
        got = sha256_bytes(path.read_bytes())
        if got != want:
            problems.append(f"{rel}: doesn't match manifest.json's recorded sha256 (hand-edited, or stale)")
    # And the reverse: nothing on disk that the manifest doesn't know about.
    on_disk = {str(f.relative_to(vendor)) for f in vendor.rglob("*") if f.is_file() and f.name != "manifest.json"}
    for rel in sorted(on_disk - set(manifest.get("files", {}))):
        problems.append(f"{rel}: on disk but not recorded in manifest.json (stale sync, or hand-added)")
    return problems


# --- Rule 3: sweep coverage ------------------------------------------------------------------

def check_sweep_coverage(vendor: Path, manifest: dict) -> list:
    problems = []
    styles = json.loads((vendor / "ThemeStyles.json").read_text(encoding="utf-8"))
    swept_enum = manifest.get("sweep", {}).get("enum", {})
    for option, values in styles.get("fragments", {}).items():
        covered = set(swept_enum.get(option, []))
        for value in values:
            if value not in covered:
                problems.append(f"sweep: no theme covers {option}={value} (ThemeStyles.json has it, the sweep doesn't)")
            elif not (vendor / "expected-css" / f"sweep__enum__{option}__{value}.json").is_file():
                problems.append(f"sweep: {option}={value} is recorded as swept but its expected-css file is missing")
    swept_scalar = manifest.get("sweep", {}).get("scalar", {})
    scalar_options = sync.parse_scalar_options((vendor / "ThemeNumbers.swift").read_text(encoding="utf-8"))
    for code in scalar_options:
        cases = set(swept_scalar.get(code, []))
        for case in ("min", "default", "max", "step"):
            if case not in cases:
                problems.append(f"sweep: scalar option {code!r} has no {case!r} case")
            elif not (vendor / "expected-css" / f"sweep__scalar__{code}__{case}.json").is_file():
                problems.append(f"sweep: {code} {case} is recorded as swept but its expected-css file is missing")
    return problems


# --- Rule 4: the Python rescoping transform ---------------------------------------------------

def check_rescope() -> list:
    return [f"rescope_css: {m}" for m in rescope_css.self_test()]


# --- Wiring --------------------------------------------------------------------------------

def all_checks(vendor: Path, manifest: dict, fetch) -> dict:
    """{rule name: [problems]} so --self-test can plant into exactly one rule and confirm the
    others stay quiet."""
    return {
        "drift": check_drift(vendor, manifest["kit_sha"], fetch),
        "manifest_hashes": check_manifest_hashes(vendor, manifest),
        "sweep_coverage": check_sweep_coverage(vendor, manifest),
        "rescope": check_rescope(),
    }


def self_test(vendor: Path) -> int:
    import copy
    import tempfile

    manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))
    fake_fetch = _real_fetch(manifest["kit_sha"])
    # Cache every remote fetch once, up front, so every plant below re-checks drift against the
    # same responses instead of hitting the network again per plant.
    cache = {}
    def cached_fetch(kit_path):
        if kit_path not in cache:
            cache[kit_path] = fake_fetch(kit_path)
        return cache[kit_path]

    baseline = all_checks(vendor, manifest, cached_fetch)
    failed_rules = {rule: probs for rule, probs in baseline.items() if probs}
    if failed_rules:
        print("self-test: the real tree already fails:", failed_rules, file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        tmp_vendor = Path(tmp) / vendor.name
        import shutil
        shutil.copytree(vendor, tmp_vendor)

        def run_with(mutate) -> dict:
            work = Path(tmp) / "work"
            if work.exists():
                shutil.rmtree(work)
            shutil.copytree(tmp_vendor, work)
            m = mutate(work)
            return all_checks(work, m if m is not None else manifest, cached_fetch)

        def plant_drift(work):
            f = work / "ThemeStyles.json"
            f.write_text(f.read_text(encoding="utf-8") + " ", encoding="utf-8")
            # Update the manifest's recorded hash for this one file too, so rule 2 (manifest
            # hashes) doesn't also fire and this plant proves rule 1 (drift vs. GitHub) alone.
            m = copy.deepcopy(manifest)
            m["files"]["ThemeStyles.json"] = sha256_bytes(f.read_bytes())
            return m

        def plant_manifest(work):
            f = work / "expected-css" / "dawn.json"
            f.write_text(f.read_text(encoding="utf-8") + " ", encoding="utf-8")
            return None  # manifest unchanged: now stale for this one file

        def plant_uncovered_enum(work):
            m = copy.deepcopy(manifest)
            option = next(iter(m["sweep"]["enum"]))
            removed = m["sweep"]["enum"][option].pop()
            rel = f"expected-css/sweep__enum__{option}__{removed}.json"
            (work / rel).unlink()
            del m["files"][rel]  # else rule 2 (manifest hashes) also fires, on the same plant
            return m

        def plant_uncovered_scalar(work):
            m = copy.deepcopy(manifest)
            code = next(iter(m["sweep"]["scalar"]))
            m["sweep"]["scalar"][code].remove("max")
            rel = f"expected-css/sweep__scalar__{code}__max.json"
            (work / rel).unlink()
            del m["files"][rel]
            return m

        def plant_rescope(work):
            # Doesn't touch `work` at all: rescope_css.py's own fixture is what this rule reads
            # from disk (scripts/theme_sim/rescope_fixture.json), so the plant lives there.
            fixture_path = ROOT / "scripts" / "theme_sim" / "rescope_fixture.json"
            original = fixture_path.read_text(encoding="utf-8")
            data = json.loads(original)
            data["selectors"][0]["expected"] = "TAMPERED"
            fixture_path.write_text(json.dumps(data), encoding="utf-8")
            try:
                return all_checks(work, manifest, cached_fetch)
            finally:
                fixture_path.write_text(original, encoding="utf-8")

        plants = {
            "drift": (plant_drift, "drift"),
            "manifest_hashes": (plant_manifest, "manifest_hashes"),
            "sweep_coverage (enum)": (plant_uncovered_enum, "sweep_coverage"),
            "sweep_coverage (scalar)": (plant_uncovered_scalar, "sweep_coverage"),
        }
        failures = 0
        for label, (mutate, expected_rule) in plants.items():
            result = run_with(mutate)
            other_rules_broke = {r: p for r, p in result.items() if p and r != expected_rule}
            if result.get(expected_rule) and not other_rules_broke:
                print(f"  caught: {label} ({expected_rule} only)")
            elif result.get(expected_rule):
                print(f"  MISSED (wrong rule(s) also fired): {label}: {other_rules_broke}", file=sys.stderr)
                failures += 1
            else:
                print(f"  MISSED: {label}", file=sys.stderr)
                failures += 1

        # rescope is checked separately: it doesn't read `vendor` at all, only the shared fixture.
        rescope_result = plant_rescope(vendor)
        if rescope_result["rescope"] and not any(p for r, p in rescope_result.items() if r != "rescope"):
            print("  caught: a tampered rescope_fixture.json (rescope only)")
        else:
            print("  MISSED: a tampered rescope_fixture.json", file=sys.stderr)
            failures += 1
        # Prove the restore worked: the real tree must be back to green.
        restored = all_checks(vendor, manifest, cached_fetch)
        if any(p for p in restored.values()):
            print(f"  MISSED: rescope_fixture.json restore left the tree broken: {restored}", file=sys.stderr)
            failures += 1

    print(f"self-test: {len(plants) + 1} plants, {failures} missed")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--self-test", action="store_true",
                         help="plant one break of each kind and confirm every one is caught, by its own rule alone")
    args = parser.parse_args()

    if not VENDOR_ROOT.is_dir():
        print("::error::vendor/kit-themes/ is missing; run python3 scripts/sync_theme_kit.py", file=sys.stderr)
        return 1
    vendor = _vendor_dir()
    manifest = json.loads((vendor / "manifest.json").read_text(encoding="utf-8"))

    if args.self_test:
        return self_test(vendor)

    results = all_checks(vendor, manifest, _real_fetch(manifest["kit_sha"]))
    problems = [p for probs in results.values() for p in probs]
    for p in problems:
        print(f"::error::{p}")
    if problems:
        print(f"{len(problems)} problem(s). Rerun scripts/sync_theme_kit.py and commit the result.")
        return 1
    n = len(manifest.get("files", {}))
    print(f"vendor/kit-themes/{vendor.name}/ ({n} files) matches kit {manifest['kit_sha']}: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
