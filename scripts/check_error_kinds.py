#!/usr/bin/env python3
"""Checks that the published error schema and exit codes are the ones the documented marsdawn has.

Usage:
    python3 scripts/check_error_kinds.py [--tag 0.7.1] [--kit-file Commands.swift] [--self-test]

The kit owns the failure kinds: `CLIFailure.Code` in Sources/marsdawn/Commands.swift gives each exit
code and the `error` string `--json` prints for it. This fetches that file at KIT_TAG (the same tag
check_skill.py reads) and fails if the built site disagrees with it:

- public/schemas/cli/error.v3.json: its `error` enum must be the kit's kinds: `CLIFailure.Code` in code
  order, then `CLIFailure.SharedKind` (kinds that share a code, e.g. `input_too_large`) as declared. The
  built file is read, not build_pages.py's constant, so a build that didn't write it fails too.
- EXIT_CODES in build_pages.py (the skill's table and the agents page): every code with a kind must
  be the kit's code for that kind, and every kit kind must be listed, by exit code.

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
SCHEMA = Path("public/schemas/cli/error.v3.json")


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


def run(kit_source: str, schema: dict, exit_codes: list) -> list[str]:
    try:
        return problems(kit_kinds(kit_source), schema, exit_codes)
    except ValueError as error:
        return [str(error)]


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
    parser.add_argument("--schema", default=str(SCHEMA))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.kit_file:
        source, origin = Path(args.kit_file).read_text(encoding="utf-8"), args.kit_file
    else:
        url = URL.format(tag=args.tag)
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                source = response.read().decode("utf-8")
        except Exception as error:  # a missing tag is a failure, not a pass
            print(f"check_error_kinds: can't fetch {url}: {error}", file=sys.stderr)
            return 1
        origin = f"marsdawn {args.tag}"
    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    from build_pages import EXIT_CODES

    if args.self_test and self_test(source, schema, EXIT_CODES):
        return 1
    found = run(source, schema, EXIT_CODES)
    if found:
        for problem in found:
            print(f"check_error_kinds: {problem}", file=sys.stderr)
        print(f"check_error_kinds: the site's failure kinds differ from {origin}'s", file=sys.stderr)
        return 1
    print(f"check_error_kinds: {args.schema} and EXIT_CODES match {origin}'s failure kinds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
