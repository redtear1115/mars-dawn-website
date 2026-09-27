#!/usr/bin/env python3
"""Vendors the kit's theme contract into vendor/kit-themes/<sha12>/ (plan-website-104 WA).

The theme simulator (W1, public/assets/theme-sim/) is a JavaScript *port* of the kit's
Sources/MarsDawnThemes: its validator, its CSS generator, and the enum-option fragment table in
ThemeStyles.json. A port can drift from what it copies. This script vendors, from one pinned kit
**commit** (not yet a tag -- see KIT_SHA below), everything a drift check needs to hold the port
to:

- ThemeStyles.json and the four built-in themes' theme.json, byte for byte;
- the validator's own fixtures (valid/invalid/hostile/publish) and expected-messages.json;
- the kit's preview.css, and preview-sim.css, its .sim-preview-scoped twin (scripts/rescope_css.py,
  which shares scripts/theme_sim/rescope_fixture.json with the JS port's own test);
- expected-css/, produced by the real `marsdawn theme css --json` for every valid fixture, every
  built-in, and a generated **sweep**: one theme per enum-fragment value in ThemeStyles.json, and
  one theme per scalar style option at min, default, max and a non-integer step (which the kit's
  own validator snaps -- see ThemeNumber.snapped in the kit). "default" here is the range's
  midpoint, snapped to the option's step; there is no other notion of a style option's default,
  since an *absent* option means "no override at all" and has no CSS of its own to compare.

The CLI is built from a detached git worktree of the pinned commit, in a *local clone* of the kit
(default ~/Projects/swift/mars-dawn-kit; override with --kit-repo), the same way this session's
own build did it: the kit isn't tagged at this SHA yet, so tools/hero-render's `exact: "<tag>"`
Package.swift dependency pattern doesn't apply here. The worktree is removed when the script is
done, whether it succeeds or not.

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

VENDOR = ROOT / "vendor" / "kit-themes" / KIT_SHA[:12]
BUILT_IN_IDS = ["dawn", "classic", "modern", "vivid"]
FIXTURE_CATEGORIES = ["valid", "invalid", "hostile", "publish"]

# ThemeNumber (kit Sources/MarsDawnThemes/ThemeNumbers.swift): (short code, JSON path template,
# range, step). The path template's {v} is filled with the raw (possibly off-step) number; the
# kit itself validates and snaps it -- this script never re-implements that arithmetic.
SCALAR_OPTIONS = {
    "bodysize": ("bodySize", 14, 18, 1),
    "lineheight": ("lineHeight", 1.4, 1.9, 0.05),
    "headingweight": ("headingWeight", 400, 900, 50),
    "radius": ("radius", 0, 16, 1),
    "maxwidth": ("maxWidth", 600, 1000, 1),
    "h1size": ("h1.size", 1.8, 2.4, 0.1),
    "h1letterspacing": ("h1.letterSpacing", -0.03, 0.03, 0.005),
    "h2letterspacing": ("h2.letterSpacing", -0.03, 0.03, 0.005),
    "blockquotebarwidth": ("blockquote.style.width", 2, 4, 1),
    "hrthickness": ("hr.style.thickness", 1, 4, 1),
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


# --- Building the CLI ------------------------------------------------------------------------

def build_cli(kit_repo: Path) -> Path:
    """Builds `marsdawn` at KIT_SHA in a detached worktree, removed on return (or on failure).
    Returns the built binary's path -- copied out of the worktree first, since the worktree
    itself won't survive this function."""
    subprocess.run(["git", "-C", str(kit_repo), "fetch", "origin", KIT_SHA], check=True)
    scratch = Path(tempfile.mkdtemp(prefix="theme-kit-sync-"))
    worktree = scratch / "kit"
    try:
        subprocess.run(["git", "-C", str(kit_repo), "worktree", "add", "--detach", str(worktree), KIT_SHA],
                        check=True)
        try:
            subprocess.run(["swift", "build", "-c", "release", "--package-path", str(worktree),
                             "--only-use-versions-from-resolved-file"], check=True)
            built = worktree / ".build" / "release" / "marsdawn"
            out = scratch / "marsdawn"
            shutil.copy2(built, out)
            out.chmod(0o755)
            return out
        finally:
            subprocess.run(["git", "-C", str(kit_repo), "worktree", "remove", "--force", str(worktree)],
                            check=False)
    except Exception:
        shutil.rmtree(scratch, ignore_errors=True)
        raise


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


def scalar_sweep_themes() -> dict:
    """{name: theme_dict} for every scalar option at min/default/max/step."""
    out = {}
    for code, (path, lo, hi, step) in SCALAR_OPTIONS.items():
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
            if path in ("blockquote.style.width",):
                style = {"blockquote": {"style": {"type": "bar", "width": value}}}
            elif path in ("hr.style.thickness",):
                style = {"hr": {"style": {"type": "line", "thickness": value}}}
            else:
                _set_path(style, path, value)
            theme["style"] = style
            out[name] = theme
    return out


# --- Vendoring ---------------------------------------------------------------------------------

def theme_css_json(binary: Path, theme_path: Path) -> dict:
    result = subprocess.run([str(binary), "theme", "css", str(theme_path), "--json"],
                             capture_output=True, text=True)
    data = json.loads(result.stdout)
    assert data.get("ok"), f"{theme_path}: kit refused it: {data}"
    return {"variables": data["variables"], "rules": data["rules"]}


def sync(kit_checkout: Path, binary: Path) -> None:
    if VENDOR.exists():
        shutil.rmtree(VENDOR)
    (VENDOR / "expected-css").mkdir(parents=True)
    (VENDOR / "sweep").mkdir(parents=True)
    (VENDOR / "ThemeFixtures").mkdir(parents=True)
    (VENDOR / "Themes").mkdir(parents=True)

    themes_src = kit_checkout / "Sources" / "MarsDawnThemes"

    # ThemeStyles.json, verbatim.
    shutil.copy2(themes_src / "Resources" / "ThemeStyles.json", VENDOR / "ThemeStyles.json")

    # The four built-ins' theme.json, verbatim.
    for theme_id in BUILT_IN_IDS:
        src = themes_src / "Resources" / "Themes" / theme_id / "theme.json"
        (VENDOR / "Themes" / theme_id).mkdir(parents=True)
        shutil.copy2(src, VENDOR / "Themes" / theme_id / "theme.json")

    # The validator's fixtures, verbatim.
    fixtures_src = kit_checkout / "Tests" / "MarsDawnThemesTests" / "ThemeFixtures"
    for category in FIXTURE_CATEGORIES:
        (VENDOR / "ThemeFixtures" / category).mkdir(parents=True)
        for f in sorted((fixtures_src / category).glob("*.json")):
            shutil.copy2(f, VENDOR / "ThemeFixtures" / category / f.name)
    shutil.copy2(fixtures_src / "expected-messages.json", VENDOR / "ThemeFixtures" / "expected-messages.json")

    # preview.css, verbatim, and its .sim-preview-scoped twin.
    preview_css = (kit_checkout / "Sources" / "MarsDawnKit" / "Resources" / "Preview" / "preview.css").read_text(encoding="utf-8")
    (VENDOR / "preview.css").write_text(preview_css, encoding="utf-8")
    (VENDOR / "preview-sim.css").write_text(rescope_css.rescope_css(preview_css), encoding="utf-8")

    # expected-css/: built-ins (bare <id>.json, the name public/assets/theme-sim's own parity
    # check -- scripts/check_theme_sim.mjs -- already reads), every valid fixture, and the sweep.
    for theme_id in BUILT_IN_IDS:
        css = theme_css_json(binary, VENDOR / "Themes" / theme_id / "theme.json")
        (VENDOR / "expected-css" / f"{theme_id}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for f in sorted((VENDOR / "ThemeFixtures" / "valid").glob("*.json")):
        css = theme_css_json(binary, f)
        (VENDOR / "expected-css" / f"valid__{f.stem}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    sweep_manifest = {"enum": {}, "scalar": {}}
    for name, theme in {**enum_sweep_themes(), **scalar_sweep_themes()}.items():
        theme_path = VENDOR / "sweep" / f"{name}.json"
        theme_path.write_text(json.dumps(theme, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        css = theme_css_json(binary, theme_path)
        (VENDOR / "expected-css" / f"sweep__{name}.json").write_text(json.dumps(css, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        kind, rest = name.split("__", 1)
        if kind == "enum":
            option, value = rest.split("__", 1)
            sweep_manifest["enum"].setdefault(option, []).append(value)
        else:
            code, case = rest.split("__", 1)
            sweep_manifest["scalar"].setdefault(code, []).append(case)

    cli_version = subprocess.run([str(binary), "--version"], capture_output=True, text=True).stdout.strip()

    # manifest.json: every vendored/generated file's sha256, the pinned commit, and what the
    # sweep covers -- read back by check_theme_kit.py, never by this script.
    files = {}
    for f in sorted(VENDOR.rglob("*")):
        if f.is_file():
            files[str(f.relative_to(VENDOR))] = sha256_bytes(f.read_bytes())
    manifest = {
        "kit_sha": KIT_SHA,
        "kit_commit_url": f"{KIT_REPO_URL}/commit/{KIT_SHA}",
        "cli_version": cli_version,
        "sweep": sweep_manifest,
        "files": files,
    }
    (VENDOR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Vendored {len(files) + 1} file(s) to {VENDOR.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--kit-repo", type=Path, default=DEFAULT_KIT_REPO,
                         help="local clone of mars-dawn-kit to build the pinned commit from")
    parser.add_argument("--kit-checkout", type=Path, default=None,
                         help="reuse an existing checkout of the pinned commit instead of making one")
    parser.add_argument("--marsdawn-bin", type=Path, default=None,
                         help="reuse an already-built marsdawn binary instead of building one")
    args = parser.parse_args()

    missed = rescope_css.self_test()
    if missed:
        print("scripts/rescope_css.py fails its own fixture; not syncing:", file=sys.stderr)
        for m in missed:
            print(f"  {m}", file=sys.stderr)
        return 1

    scratch = None
    try:
        if args.kit_checkout and args.marsdawn_bin:
            kit_checkout, binary = args.kit_checkout, args.marsdawn_bin
        else:
            if not args.kit_repo.is_dir():
                print(f"::error::{args.kit_repo} isn't a directory; pass --kit-repo", file=sys.stderr)
                return 1
            print(f"Building marsdawn at {KIT_SHA} from {args.kit_repo} ...")
            binary = build_cli(args.kit_repo)
            scratch = binary.parent
            kit_checkout = scratch / "kit-src"
            # The worktree used to build is gone; re-fetch the tree read-only for the resources
            # this script also copies (ThemeStyles.json, fixtures, preview.css).
            subprocess.run(["git", "-C", str(args.kit_repo), "worktree", "add", "--detach",
                             str(kit_checkout), KIT_SHA], check=True)
        sync(kit_checkout, binary)
    finally:
        if scratch is not None:
            kit_checkout_dir = scratch / "kit-src"
            if kit_checkout_dir.exists():
                subprocess.run(["git", "-C", str(args.kit_repo), "worktree", "remove", "--force",
                                 str(kit_checkout_dir)], check=False)
            shutil.rmtree(scratch, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
