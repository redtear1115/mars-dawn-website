#!/usr/bin/env python3
"""Vendors the kit's theme contract into vendor/kit-themes/<sha12>/ (plan-website-104 WA).

The theme simulator (W1, public/assets/theme-sim/) is a JavaScript *port* of the kit's
Sources/MarsDawnThemes: its validator, its CSS generator, and the enum-option fragment table in
ThemeStyles.json. A port can drift from what it copies. This script vendors, from one pinned kit
**commit** (not yet a tag -- see KIT_SHA below), everything a drift check needs to hold the port
to:

- ThemeStyles.json, ThemeNumbers.swift and the four built-in themes' theme.json, byte for byte;
- the validator's own fixtures (valid/invalid/hostile/publish) and expected-messages.json;
- the kit's preview.css, and preview-sim.css, its .sim-preview-scoped twin (scripts/rescope_css.py,
  which shares scripts/theme_sim/rescope_fixture.json with the JS port's own test);
- expected-css/, produced by the real `marsdawn theme css --json` for every valid fixture, every
  built-in, and a generated **sweep**: one theme per enum-fragment value in ThemeStyles.json, and
  one theme per scalar style option (bodySize, lineHeight, ... -- parsed straight out of the
  vendored ThemeNumbers.swift by parse_scalar_options, not a hand-kept mirror, so a scalar option
  the kit adds later is picked up automatically) at min, default, max and a non-integer step
  (which the kit's own validator snaps -- see ThemeNumber.snapped in the kit). "default" here is
  the range's midpoint, snapped to the option's step; there is no other notion of a style option's
  default, since an *absent* option means "no override at all" and has no CSS of its own to compare.

The CLI is built from a detached git worktree of the pinned commit, in a *local clone* of the kit
(default ~/Projects/swift/mars-dawn-kit; override with --kit-repo). The kit isn't tagged at this
SHA yet, so tools/hero-render's `exact: "<tag>"` Package.swift dependency pattern doesn't apply
here. **The worktree is kept until every subprocess call into the binary is done**: `marsdawn`
loads its resources (ThemeStyles.json, Preview/preview.css, ...) through `Bundle.module`, which
reads `*.bundle` directories SwiftPM places next to the binary in `.build/release` -- copying only
the binary out of the worktree, then removing the worktree, leaves it unable to find them (dies
"unable to find bundle named ...", exit 133). The binary is smoke-tested (a real `theme css` call
on a built-in, checked for both a zero exit and JSON output) *before* anything under vendor/ is
touched, and the whole vendored tree is built in a scratch directory and only swapped into place
on success, so a build or smoke-test failure never deletes what's already committed.

Needs macOS + Swift (the kit is built from source). scripts/check_theme_kit.py is the other half,
safe to run on Ubuntu CI: it can't build the kit, so it holds the vendored tree to a recorded
manifest and to GitHub's raw copy of the pinned commit instead.

    python3 scripts/sync_theme_kit.py
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import rescope_css  # noqa: E402

# release-0.6.1 HEAD at the time of this sync: S1-S3 (theme validate) + W0 (theme css / theme
# preview) merged, not tagged yet (the 0.6.1 tag follows 0.6.0 on 10/1 -- plan-website-104 WA).
# Bump this, rerun this script and commit the result when the kit tags 0.6.1 (or moves further).
KIT_SHA = "f1c66e16509e63027b0679bda15eafbb8f3911a0"
KIT_REPO_URL = "https://github.com/redtear1115/mars-dawn-kit"
DEFAULT_KIT_REPO = Path.home() / "Projects" / "swift" / "mars-dawn-kit"

VENDOR_ROOT = ROOT / "vendor" / "kit-themes"
VENDOR = VENDOR_ROOT / KIT_SHA[:12]
BUILT_IN_IDS = ["dawn", "classic", "modern", "vivid"]
FIXTURE_CATEGORIES = ["valid", "invalid", "hostile", "publish"]


class SyncError(RuntimeError):
    """A subprocess failed: always carries its exit code and stderr, so a caller never sees just
    an empty-output JSONDecodeError with no idea why."""


def run(cmd: list, **kwargs) -> subprocess.CompletedProcess:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    except OSError as e:
        # e.g. the binary (or git, or swift) itself doesn't exist at that path: turned into a
        # SyncError like any other failure, rather than a bare traceback with no indication of
        # which command or path was at fault.
        raise SyncError(f"{' '.join(cmd)}: couldn't run it ({e})") from e
    if result.returncode != 0:
        raise SyncError(f"{' '.join(cmd)} (exit {result.returncode}):\n"
                         f"stdout: {result.stdout!r}\nstderr: {result.stderr!r}")
    return result


# --- Parsing ThemeNumbers.swift (the kit's own list of scalar style options) --------------------

def parse_scalar_options(swift_text: str) -> dict:
    """{code: (json_path, lo, hi, step)} for every case of the kit's `ThemeNumber` enum
    (Sources/MarsDawnThemes/ThemeNumbers.swift), parsed from its own case list and its `range`/
    `step` switch statements -- not a hand-kept mirror, so a scalar option the kit adds later is
    picked up here (and, via check_theme_kit.py reading the vendored copy of this same file with
    this same function, in the drift check too) automatically. `code` is the case name lowercased
    (e.g. "h1LetterSpacing" -> "h1letterspacing"), used as this script's short id for the option;
    `json_path` is the case's rawValue (its theme.json path, e.g. "h1.letterSpacing"), which
    defaults to the case name itself when the case has no explicit `= "..."`."""
    decl_section, _, rest = swift_text.partition("var range")
    assert rest, "ThemeNumbers.swift: no `var range` found; kit format changed?"
    case_block = decl_section.split("enum ThemeNumber", 1)[1].split("{", 1)[1]
    cases: dict = {}
    order: list = []
    for line in case_block.splitlines():
        line = line.split("//", 1)[0].strip()
        if not line.startswith("case "):
            continue
        line = line[len("case "):].rstrip()
        m = re.match(r'^([A-Za-z0-9_,\s]+?)(?:\s*=\s*"([^"]*)")?$', line)
        if not m:
            continue
        names = [n.strip() for n in m.group(1).split(",") if n.strip()]
        explicit_path = m.group(2)
        for i, name in enumerate(names):
            # `= "..."` binds only to the last name in a comma list (Swift's own rule).
            path = explicit_path if (explicit_path is not None and i == len(names) - 1) else name
            cases[name] = path
            order.append(name)
    assert order, "ThemeNumbers.swift: no enum cases parsed; kit format changed?"

    def parse_switch_block(text: str, value_parser):
        out = {}
        for line in text.splitlines():
            line = line.split("//", 1)[0].strip()
            m = re.match(r'^case\s+((?:\.[A-Za-z0-9]+\s*,\s*)*\.[A-Za-z0-9]+)\s*:\s*(.+?)\s*$', line)
            if not m:
                continue
            names = [n.strip().lstrip(".") for n in m.group(1).split(",")]
            value = value_parser(m.group(2).strip())
            for n in names:
                out[n] = value
        return out

    range_block, _, after_range = rest.partition("var step")
    assert after_range, "ThemeNumbers.swift: no `var step` found; kit format changed?"

    def parse_range(v: str):
        m = re.match(r'^(-?[\d.]+)\.\.\.(-?[\d.]+)$', v)
        assert m, f"ThemeNumbers.swift: unparseable range literal {v!r}"
        return float(m.group(1)), float(m.group(2))

    ranges = parse_switch_block(range_block, parse_range)
    steps = parse_switch_block(after_range, float)
    missing = ({n for n in order} - set(ranges)) | ({n for n in order} - set(steps))
    assert not missing, f"ThemeNumbers.swift: no range/step parsed for {missing}"

    def as_int_if_whole(v: float):
        # "14" in ThemeNumbers.swift parses to the Python float 14.0; writing that into a sweep
        # theme.json would print "14.0" where the kit's own fixtures (and this file's earlier,
        # hand-mirrored SCALAR_OPTIONS) always wrote "14" -- an int is still exactly the value
        # the kit's Double field decodes, but keeping whole numbers as ints here is what keeps
        # scripts/sync_theme_kit.py's output byte-identical across a hand-mirrored list and a
        # parsed one.
        return int(v) if v == int(v) else v

    return {name.lower(): (cases[name], as_int_if_whole(ranges[name][0]), as_int_if_whole(ranges[name][1]),
                            as_int_if_whole(steps[name])) for name in order}


# --- Building the CLI ------------------------------------------------------------------------

def build_cli(kit_repo: Path, sha: str) -> tuple:
    """Fetches `sha` and builds `marsdawn` in a detached worktree, which is returned *along with*
    the binary path and left in place: the binary needs its resource bundles, which live beside
    it in the worktree's .build/release, so nothing may remove the worktree until every call into
    the binary is done (remove_worktree does that, once the caller is finished). Raises SyncError
    with the build's own stderr on failure, and cleans up after itself in that case."""
    run(["git", "-C", str(kit_repo), "fetch", "origin", sha])
    scratch = Path(tempfile.mkdtemp(prefix="theme-kit-sync-"))
    worktree = scratch / "kit"
    try:
        run(["git", "-C", str(kit_repo), "worktree", "add", "--detach", str(worktree), sha])
    except SyncError:
        shutil.rmtree(scratch, ignore_errors=True)
        raise
    try:
        run(["swift", "build", "-c", "release", "--package-path", str(worktree),
             "--only-use-versions-from-resolved-file"])
    except SyncError:
        remove_worktree(kit_repo, worktree)
        raise
    return worktree, worktree / ".build" / "release" / "marsdawn"


def remove_worktree(kit_repo: Path, worktree: Path) -> None:
    subprocess.run(["git", "-C", str(kit_repo), "worktree", "remove", "--force", str(worktree)],
                    check=False)
    shutil.rmtree(worktree.parent, ignore_errors=True)


def smoke_test(binary: Path, sample_theme: Path) -> None:
    """A real `theme css` call the binary must answer correctly *before* anything under vendor/
    is touched: proves the binary runs at all (its exit code), that it can find its resource
    bundles (a bundle-less binary still starts and still exits 0, printing nothing useful to
    stdout -- checking the JSON and its `ok` field is what actually catches that), and that
    `theme css` itself works, all in one call using the CLI itself, so this can't disagree with
    the calls the rest of this script goes on to make."""
    result = run([str(binary), "theme", "css", str(sample_theme), "--json"])
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise SyncError(f"marsdawn smoke test: not JSON -- stdout: {result.stdout!r} "
                         f"stderr: {result.stderr!r}") from e
    if not data.get("ok"):
        raise SyncError(f"marsdawn smoke test: the CLI refused its own built-in: {data}")


# --- Sweep theme construction ------------------------------------------------------------------

BASE_THEME = {
    "schemaVersion": 1, "id": "placeholder", "version": "1.0.0",
    "name": {"en": "Sweep"}, "summary": {"en": "Generated by scripts/sync_theme_kit.py"},
    "fontDesign": "sans", "scenarios": ["notes-sharing"],
    "light": {
        "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
        "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
        "syntax": {"keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00",
                   "function": "#5B3E8C", "type": "#1F6FB2"},
        "diagram": {"node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C",
                    "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6"},
    },
    "dark": {
        "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
        "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
        "syntax": {"keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572",
                   "function": "#C7A6F5", "type": "#6CB6FF"},
        "diagram": {"node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C",
                    "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322"},
    },
}

# One theme.json `style` object per ThemeStyles.json fragment option/value (kit
# Sources/MarsDawnThemes/Resources/ThemeStyles.json's `fragments` table): the sweep must cover
# every one of these, and check_theme_kit.py checks that against the vendored ThemeStyles.json
# itself, not this list -- so a kit-side addition shows up as a missing sweep entry, not a script
# that silently agrees with itself.
ENUM_STYLES = {
    ("h1Decoration", "none"): {"h1": {"decoration": {"type": "none"}}},
    ("h1Decoration", "shortRule"): {"h1": {"decoration": {"type": "shortRule", "color": "accent"}}},
    ("h1Decoration", "gradientBar"): {"h1": {"decoration": {"type": "gradientBar", "from": "accent", "to": "heading"}}},
    ("h2Decoration", "none"): {"h2": {"decoration": {"type": "none"}}},
    ("h2Decoration", "dot"): {"h2": {"decoration": {"type": "dot", "color": "accent"}}},
    ("blockquoteStyle", "bar"): {"blockquote": {"style": {"type": "bar", "width": 3}}},
    ("blockquoteStyle", "panel"): {"blockquote": {"style": {"type": "panel"}}},
    ("hrStyle", "shortCentered"): {"hr": {"style": {"type": "shortCentered", "color": "accent"}}},
    ("hrStyle", "gradient"): {"hr": {"style": {"type": "gradient", "colors": ["accent", "heading", "link"]}}},
    ("tableHeader", "surface"): {"table": {"header": {"type": "surface"}}},
    ("tableHeader", "accentRule"): {"table": {"header": {"type": "accentRule", "color": "accent"}}},
    ("tableHeader", "filled"): {"table": {"header": {"type": "filled", "background": "heading", "text": "background"}}},
}


def _set_path(d: dict, path: str, value) -> None:
    """Sets d["a"]["b"] = value for path "a.b", creating intermediate dicts."""
    parts = path.split(".")
    for p in parts[:-1]:
        d = d.setdefault(p, {})
    d[parts[-1]] = value


def snap_step(value: float, lo: float, hi: float, step: float) -> float:
    steps = round(value / step)
    result = round(steps * step, 6)
    return max(lo, min(hi, result))


def enum_sweep_themes() -> dict:
    """{name: theme_dict} for every (option, value) in ENUM_STYLES."""
    out = {}
    for (option, value), style in ENUM_STYLES.items():
        name = f"enum__{option}__{value}"
        theme = json.loads(json.dumps(BASE_THEME))
        theme["id"] = f"sw-{option}-{value}".lower()[:32].rstrip("-")
        theme["style"] = style
        out[name] = theme
    return out


def scalar_sweep_themes(scalar_options: dict) -> dict:
    """{name: theme_dict} for every scalar option (from parse_scalar_options) at
    min/default/max/step."""
    out = {}
    for code, (path, lo, hi, step) in scalar_options.items():
        mid = snap_step((lo + hi) / 2, lo, hi, step)
        # A raw value not on the option's step grid, so the kit's own snapping is exercised for
        # real (rather than this script guessing what it snaps to).
        offset = step / 2 if step != 1 else 0.37
        off_step = mid + offset
        if off_step > hi:
            off_step = mid - offset
        cases = {"min": lo, "default": mid, "max": hi, "step": off_step}
        for case, value in cases.items():
            name = f"scalar__{code}__{case}"
            theme = json.loads(json.dumps(BASE_THEME))
            theme["id"] = f"sw-{code}-{case}".lower()[:32].rstrip("-")
            style = {}
            if path == "blockquote.style.width":
                style = {"blockquote": {"style": {"type": "bar", "width": value}}}
            elif path == "hr.style.thickness":
                style = {"hr": {"style": {"type": "line", "thickness": value}}}
            else:
                _set_path(style, path, value)
            theme["style"] = style
            out[name] = theme
    return out


# --- Vendoring ---------------------------------------------------------------------------------

def theme_css_json(binary: Path, theme_path: Path) -> dict:
    result = run([str(binary), "theme", "css", str(theme_path), "--json"])
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise SyncError(f"{theme_path}: marsdawn theme css printed non-JSON with --json -- "
                         f"stdout: {result.stdout!r} stderr: {result.stderr!r}") from e
    if not data.get("ok"):
        raise SyncError(f"{theme_path}: kit refused it: {data}")
    return {"variables": data["variables"], "rules": data["rules"]}


def sync(kit_checkout: Path, binary: Path, dest: Path) -> None:
    """Writes the whole vendored tree into `dest`, a fresh empty directory. Never touches the
    real vendor/kit-themes/<sha12>/: the caller only replaces that with `dest` once this returns
    without raising."""
    (dest / "expected-css").mkdir(parents=True)
    (dest / "sweep").mkdir(parents=True)
    (dest / "ThemeFixtures").mkdir(parents=True)
    (dest / "Themes").mkdir(parents=True)

    themes_src = kit_checkout / "Sources" / "MarsDawnThemes"

    # ThemeStyles.json and ThemeNumbers.swift, verbatim.
    shutil.copy2(themes_src / "Resources" / "ThemeStyles.json", dest / "ThemeStyles.json")
    shutil.copy2(themes_src / "ThemeNumbers.swift", dest / "ThemeNumbers.swift")
    scalar_options = parse_scalar_options((dest / "ThemeNumbers.swift").read_text(encoding="utf-8"))

    # The four built-ins' theme.json, verbatim.
    for theme_id in BUILT_IN_IDS:
        src = themes_src / "Resources" / "Themes" / theme_id / "theme.json"
        (dest / "Themes" / theme_id).mkdir(parents=True)
        shutil.copy2(src, dest / "Themes" / theme_id / "theme.json")

    # The validator's fixtures, verbatim.
    fixtures_src = kit_checkout / "Tests" / "MarsDawnThemesTests" / "ThemeFixtures"
    for category in FIXTURE_CATEGORIES:
        (dest / "ThemeFixtures" / category).mkdir(parents=True)
        for f in sorted((fixtures_src / category).glob("*.json")):
            shutil.copy2(f, dest / "ThemeFixtures" / category / f.name)
    shutil.copy2(fixtures_src / "expected-messages.json", dest / "ThemeFixtures" / "expected-messages.json")

    # preview.css, verbatim, and its .sim-preview-scoped twin.
    preview_css = (kit_checkout / "Sources" / "MarsDawnKit" / "Resources" / "Preview" / "preview.css").read_text(encoding="utf-8")
    (dest / "preview.css").write_text(preview_css, encoding="utf-8")
    (dest / "preview-sim.css").write_text(rescope_css.rescope_css(preview_css), encoding="utf-8")

    # expected-css/: built-ins (bare <id>.json, the name public/assets/theme-sim's own parity
    # check -- scripts/check_theme_sim.mjs -- already reads), every valid fixture, and the sweep.
    for theme_id in BUILT_IN_IDS:
        css = theme_css_json(binary, dest / "Themes" / theme_id / "theme.json")
        (dest / "expected-css" / f"{theme_id}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for f in sorted((dest / "ThemeFixtures" / "valid").glob("*.json")):
        css = theme_css_json(binary, f)
        (dest / "expected-css" / f"valid__{f.stem}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    sweep_manifest = {"enum": {}, "scalar": {}}
    all_sweep = {**enum_sweep_themes(), **scalar_sweep_themes(scalar_options)}
    for name, theme in all_sweep.items():
        theme_path = dest / "sweep" / f"{name}.json"
        theme_path.write_text(json.dumps(theme, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        css = theme_css_json(binary, theme_path)
        (dest / "expected-css" / f"sweep__{name}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        kind, rest = name.split("__", 1)
        if kind == "enum":
            option, value = rest.split("__", 1)
            sweep_manifest["enum"].setdefault(option, []).append(value)
        else:
            code, case = rest.split("__", 1)
            sweep_manifest["scalar"].setdefault(code, []).append(case)

    cli_version = run([str(binary), "--version"]).stdout.strip()

    # manifest.json: every vendored/generated file's sha256, the pinned commit, and what the
    # sweep covers -- read back by check_theme_kit.py, never by this script.
    files = {}
    for f in sorted(dest.rglob("*")):
        if f.is_file():
            files[str(f.relative_to(dest))] = hashlib.sha256(f.read_bytes()).hexdigest()
    manifest = {
        "kit_sha": KIT_SHA,
        "kit_commit_url": f"{KIT_REPO_URL}/commit/{KIT_SHA}",
        "cli_version": cli_version,
        "sweep": sweep_manifest,
        "files": files,
    }
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Vendored {len(files) + 1} file(s)")


def publish(dest: Path) -> None:
    """Swaps `dest` into vendor/kit-themes/<sha12>/, replacing whatever was there. Only called
    after sync() has returned successfully, so a build or a bad theme never deletes the tree
    that's already committed."""
    VENDOR_ROOT.mkdir(parents=True, exist_ok=True)
    if VENDOR.exists():
        backup = VENDOR.with_name(VENDOR.name + ".old")
        if backup.exists():
            shutil.rmtree(backup)
        VENDOR.rename(backup)
        shutil.move(str(dest), str(VENDOR))
        shutil.rmtree(backup)
    else:
        shutil.move(str(dest), str(VENDOR))
    print(f"Published to {VENDOR.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--kit-repo", type=Path, default=DEFAULT_KIT_REPO,
                         help="local clone of mars-dawn-kit to build the pinned commit from")
    parser.add_argument("--kit-checkout", type=Path, default=None,
                         help="reuse an existing checkout of the pinned commit instead of making one")
    parser.add_argument("--marsdawn-bin", type=Path, default=None,
                         help="reuse an already-built marsdawn binary instead of building one "
                              "(must still live inside its build tree, next to its *.bundle dirs)")
    args = parser.parse_args()

    missed = rescope_css.self_test()
    if missed:
        print("scripts/rescope_css.py fails its own fixture; not syncing:", file=sys.stderr)
        for m in missed:
            print(f"  {m}", file=sys.stderr)
        return 1

    built_worktree = None
    try:
        if args.kit_checkout and args.marsdawn_bin:
            kit_checkout, binary = args.kit_checkout, args.marsdawn_bin
        else:
            if not args.kit_repo.is_dir():
                print(f"::error::{args.kit_repo} isn't a directory; pass --kit-repo", file=sys.stderr)
                return 1
            print(f"Building marsdawn at {KIT_SHA} from {args.kit_repo} ...")
            built_worktree, binary = build_cli(args.kit_repo, KIT_SHA)
            kit_checkout = built_worktree

        smoke_test(binary, kit_checkout / "Sources" / "MarsDawnThemes" / "Resources" / "Themes" / "dawn" / "theme.json")

        with tempfile.TemporaryDirectory(dir=ROOT / "vendor" if (ROOT / "vendor").is_dir() else ROOT) as tmp:
            work = Path(tmp) / KIT_SHA[:12]
            sync(kit_checkout, binary, work)
            publish(work)
    except SyncError as e:
        print(f"::error::{e}", file=sys.stderr)
        return 1
    finally:
        if built_worktree is not None:
            remove_worktree(args.kit_repo, built_worktree)
    return 0


if __name__ == "__main__":
    sys.exit(main())
