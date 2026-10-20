#!/usr/bin/env python3
"""Checks that the published error schema and exit codes are the ones the documented marsdawn has.

Usage:
    python3 scripts/check_error_kinds.py [--tag 0.7.2] [--kit-file Commands.swift] [--kit-main main.swift] [--self-test]

The kit owns the failure kinds: `CLIFailure.Code` in Sources/marsdawn/Commands.swift gives each exit
code and the `error` string `--json` prints for it. This fetches that file at KIT_TAG (the same tag
check_skill.py reads) and fails if the built site disagrees with it:

- public/schemas/cli/error.v3.json: its `error` enum must be the kit's kinds: `CLIFailure.Code` in code
  order, then `CLIFailure.SharedKind` (kinds that share a code, e.g. `input_too_large`) as declared. The
  built file is read, not build_pages.py's constant, so a build that didn't write it fails too.
- EXIT_CODES in build_pages.py (the skill's table and the agents page): every code with a kind must
  be the kit's code for that kind, and every kit kind must be listed, by exit code.
- public/schemas/cli/error.v4.json (#295): v3's kinds, then the usage errors that print a kind with
  --json. Those are the kit's other `*Failure` types with `static let exitCode: Int32 = 64` (a
  `static let kind`, or the raw values of their `enum Kind`), in declaration order, each counted only
  if main.swift's `finish()` prints JSON for it. main.swift is fetched at the same tag.

error.v1.json and error.v2.json aren't compared: each is frozen at its release's kinds and never changes.

--self-test plants one drift of each kind into copies of the inputs and fails if any passes.
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_skill import KIT_TAG  # noqa: E402

URL = "https://raw.githubusercontent.com/redtear1115/mars-dawn-kit/{tag}/Sources/marsdawn/Commands.swift"
MAIN_URL = "https://raw.githubusercontent.com/redtear1115/mars-dawn-kit/{tag}/Sources/marsdawn/main.swift"
SCHEMA = Path("public/schemas/cli/error.v3.json")
SCHEMA_V4 = Path("public/schemas/cli/error.v4.json")


def kit_kinds(source: str) -> list[tuple[int, str]]:
    """(exit code, kind) pairs: CLIFailure.Code in code order, then CLIFailure.SharedKind as declared.

    A shared kind reports another kind's exit code (`input_too_large` exits 5, like `export_failed`).
    """
    enum = re.search(r"enum Code: Int32 \{(.*?)\n    \}\n", source, re.S)
    if not enum:
        raise ValueError("no `enum Code: Int32` in the kit source")
    body = enum.group(1)
    codes = dict(re.findall(r"case (\w+) = (\d+)", body))
    kinds = dict(re.findall(r'case \.(\w+): "([a-z_]+)"', body))
    if not codes or set(codes) != set(kinds):
        raise ValueError(f"codes {sorted(codes)} and kinds {sorted(kinds)} name different cases")
    pairs = sorted((int(codes[name]), kinds[name]) for name in codes)
    shared = re.search(r"enum SharedKind: String, CaseIterable \{(.*?)\n    \}\n", source, re.S)
    if shared:
        body = shared.group(1)
        raw = re.findall(r'case (\w+) = "([a-z_]+)"', body)
        owner = dict(re.findall(r"case \.(\w+): \.(\w+)", body))
        if not raw or set(owner) != {name for name, _ in raw} or not set(owner.values()) <= set(codes):
            raise ValueError(f"shared kinds {raw} and their codes {owner} don't line up with the Code cases")
        pairs += [(int(codes[owner[name]]), kind) for name, kind in raw]
    return pairs


def kit_usage_kinds(source: str, main_source: str) -> list[str]:
    """The kinds of the usage errors (exit 64) that main.swift prints as JSON, in declaration order."""
    kinds = []
    for m in re.finditer(r"\nstruct (\w+Failure): Error, CustomStringConvertible \{(.*?)\n\}\n", source, re.S):
        name, body = m.groups()
        if name == "CLIFailure" or not re.search(r"static let exitCode: Int32 = 64\b", body):
            continue
        single = re.findall(r'static let kind = "([a-z_]+)"', body)
        enum = re.search(r"enum Kind: String \{(.*?)\n    \}\n", body, re.S)
        found = single + (re.findall(r'case \w+ = "([a-z_]+)"', enum.group(1)) if enum else [])
        if not found:
            raise ValueError(f"{name} exits 64 but names no kind")
        block = re.search(rf"if let failure = error as\? {name} \{{(.*?)\n    \}}\n", main_source, re.S)
        if block and "printJSON(" in block.group(1) and "if wantsJSON" in block.group(1):
            kinds += found
    if not kinds:
        raise ValueError("no usage error in the kit prints JSON")
    return kinds


def problems_v4(kit: list[tuple[int, str]], usage: list[str], schema_v4: dict) -> list[str]:
    enum = schema_v4.get("properties", {}).get("error", {}).get("enum")
    want = [kind for _, kind in kit] + usage
    return [] if enum == want else [f"error.v4.json enum {enum} != kit kinds {want}"]


def problems(kit: list[tuple[int, str]], schema: dict, exit_codes: list) -> list[str]:
    found = []
    enum = schema.get("properties", {}).get("error", {}).get("enum")
    if enum != [kind for _, kind in kit]:
        found.append(f"error.v3.json enum {enum} != kit kinds {[kind for _, kind in kit]}")
    site = [(code, kind) for code, kind, _ in exit_codes if kind]
    by_code = sorted(kit, key=lambda pair: pair[0])  # stable: a shared kind follows the kind it shares a code with
    if site != by_code:
        found.append(f"EXIT_CODES {site} != kit {by_code}")
    return found


def run(kit_source: str, schema: dict, exit_codes: list, main_source: str = None, schema_v4: dict = None) -> list[str]:
    try:
        kit = kit_kinds(kit_source)
        found = problems(kit, schema, exit_codes)
        if main_source is not None:
            found += problems_v4(kit, kit_usage_kinds(kit_source, main_source), schema_v4)
        return found
    except ValueError as error:
        return [str(error)]


def self_test_v4(kit_source: str, main_source: str, schema: dict, exit_codes: list, schema_v4: dict) -> int:
    usage = kit_usage_kinds(kit_source, main_source)
    if len(usage) < 3:
        print(f"check_error_kinds: self-test: parsed only usage kinds {usage}", file=sys.stderr)
        return 1
    short = json.loads(json.dumps(schema_v4))
    short["properties"]["error"]["enum"].remove(usage[0])
    extra = json.loads(json.dumps(schema_v4))
    extra["properties"]["error"]["enum"].append("planted_kind")
    no_json = re.sub(r"(if let failure = error as\? WaitRangeFailure \{.*?)printJSON\(", r"\1print(", main_source, 1, re.S)
    added = kit_source.replace('case differs = "skill_differs"', 'case differs = "skill_differs"\n        case planted = "skill_planted"', 1)
    not_usage = re.sub(r"(struct WaitRangeFailure.*?static let exitCode: Int32 = )64", r"\g<1>2", kit_source, 1, re.S)
    drifts = {
        "a usage kind missing from error.v4.json": (kit_source, main_source, short),
        "an extra kind in error.v4.json": (kit_source, main_source, extra),
        "main.swift stops printing JSON for a usage error": (kit_source, no_json, schema_v4),
        "a usage kind added to the kit": (added, main_source, schema_v4),
        "a usage error that no longer exits 64": (not_usage, main_source, schema_v4),
    }
    failed = 0
    for name, (k, m, v4) in drifts.items():
        if k == kit_source and m == main_source and v4 is schema_v4:
            print(f"check_error_kinds: self-test: {name}: plant didn't change anything", file=sys.stderr)
            failed += 1
        elif not run(k, schema, exit_codes, m, v4):
            print(f"check_error_kinds: self-test: {name} went unnoticed", file=sys.stderr)
            failed += 1
    if failed:
        return 1
    print(f"check_error_kinds: self-test: all {len(drifts)} planted error.v4 drifts caught")
    return 0


def self_test(kit_source: str, schema: dict, exit_codes: list) -> int:
    kit = kit_kinds(kit_source)
    if len(kit) < 5:  # a parser that finds nothing would make every comparison vacuous
        print(f"check_error_kinds: self-test: parsed only {kit}", file=sys.stderr)
        return 1
    extra_case = kit_source.replace(
        "        var kind: String {",
        "        case planted = 7\n\n        var kind: String {", 1).replace(
        "            switch self {",
        '            switch self {\n            case .planted: "planted_kind"', 1)
    renamed = kit_source.replace(f'"{kit[-1][1]}"', '"renamed_kind"', 1)
    short_schema = json.loads(json.dumps(schema))
    short_schema["properties"]["error"]["enum"] = short_schema["properties"]["error"]["enum"][:-1]
    renumbered = [(code + 1 if kind == kit[-1][1] else code, kind, meaning) for code, kind, meaning in exit_codes]
    missing_row = [row for row in exit_codes if row[1] != kit[-1][1]]
    drifts = {
        "a kind added to the kit": (extra_case, schema, exit_codes),
        "a kind renamed in the kit": (renamed, schema, exit_codes),
        "a kind missing from error.v3.json": (kit_source, short_schema, exit_codes),
        "an exit code renumbered on the site": (kit_source, schema, renumbered),
        "an exit code missing on the site": (kit_source, schema, missing_row),
        "a shared kind moved to another code in the kit": (
            kit_source.replace("case .inputTooLarge: .exportFailed", "case .inputTooLarge: .outputExists", 1),
            schema, exit_codes),
        "no Code enum in the kit source": ("struct Nothing {}", schema, exit_codes),
    }
    failed = 0
    for name, planted in drifts.items():
        if planted[0] == kit_source and planted[1] is schema and planted[2] is exit_codes:
            print(f"check_error_kinds: self-test: {name}: plant didn't change anything", file=sys.stderr)
            failed += 1
        elif not run(*planted):
            print(f"check_error_kinds: self-test: {name} went unnoticed", file=sys.stderr)
            failed += 1
    if failed:
        return 1
    print(f"check_error_kinds: self-test: all {len(drifts)} planted drifts caught")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", default=KIT_TAG)
    parser.add_argument("--kit-file", help="read Commands.swift from here instead of the kit at --tag")
    parser.add_argument("--kit-main", help="read main.swift from here instead of the kit at --tag")
    parser.add_argument("--schema", default=str(SCHEMA))
    parser.add_argument("--schema-v4", default=str(SCHEMA_V4))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    def fetch(local, template):
        if local:
            return Path(local).read_text(encoding="utf-8")
        url = template.format(tag=args.tag)
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return response.read().decode("utf-8")
        except Exception as error:  # a missing tag is a failure, not a pass
            print(f"check_error_kinds: can't fetch {url}: {error}", file=sys.stderr)
            return None

    source, main_source = fetch(args.kit_file, URL), fetch(args.kit_main, MAIN_URL)
    if source is None or main_source is None:
        return 1
    origin = args.kit_file or f"marsdawn {args.tag}"
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    schema_v4 = json.loads(Path(args.schema_v4).read_text(encoding="utf-8"))
    from build_pages import EXIT_CODES

    if args.self_test and (self_test(source, schema, EXIT_CODES)
                           or self_test_v4(source, main_source, schema, EXIT_CODES, schema_v4)):
        return 1
    found = run(source, schema, EXIT_CODES, main_source, schema_v4)
    if found:
        for problem in found:
            print(f"check_error_kinds: {problem}", file=sys.stderr)
        print(f"check_error_kinds: the site's failure kinds differ from {origin}'s", file=sys.stderr)
        return 1
    print(f"check_error_kinds: {args.schema}, {args.schema_v4} and EXIT_CODES match {origin}'s failure kinds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
