#!/usr/bin/env python3
"""Ingestion for website #254: /cli/, /cli/agents/ and /changelog/ catch up with marsdawn 0.7.2.

Every string this slice puts on the site comes from a pinned issue comment and is carried here by
program, never typed. Each comment is fetched by id with `gh api` and held to the sha256 and
`updated_at` in sources.json; a comment that changed stops the run.

- A, #254 6233038202 (Grok, 2026-10-17): /cli/'s `open --wait` bullets and version sentence,
  /cli/agents/'s folder `status` bullet, the 0.6.4 changelog entry.
- B, #254 6294978172 (Grok, 2026-10-20): the 0.7.2 and 0.6.1 changelog entries, /cli/'s export
  bullets and version sentence, the `marsdawn theme` section, /cli/agents/'s schema notes.
- C, #286 6280485104 (Grok, 2026-10-20): the 0.7.1 and 0.7.0 changelog entries (its 0.6.4 is void, #286
  6294982770), with Grok's edits in #286 6280891336 section 6c applied by program (each old text must
  occur exactly once), and the ja layout name ハンドブック (#254 6295059627) in place of マニュアル in ja 0.7.1.
- The owner approved A and B for en, zh-Hant and ja on 2026-10-20 (#254 6295102211), and C with those
  edits on 2026-10-21 (#254 6295263711); both are pinned.
- I, #254 6295975448 (Grok, 2026-10-21): the same pieces in zh-Hans, ko, de, fr and es, under the
  standing machine-locale OK. One section per locale (## zh-Hans ...) with items A to F, and E as one
  table. Its changelog entries use ### headings (the page's level since #273); they are read as ##, the
  level the build inserts at, with nothing else changed.
- J, #296 6666104435 (Aria, 2026-11-05): three lines in all eight locales, replacing what A, B and I gave
  for them. `--wait` defaults to 2, so `status` comes without passing it and only `--wait 0` drops it.
  The owner approved J on 2026-11-06 (#296 6683377854).
- K, #355 6666174606 (Aria, 2026-11-05): the 0.7.3 to 0.7.6 changelog entries in en and zh-Hant, approved by
  the owner on 2026-11-06 (#355 6683315581). K_i18n, #355 6684157004 (Aria, 2026-11-06): the same in the
  other six locales, under the standing machine-locale OK. One `## <locale>` section with one md block in
  each; ### headings are read as ##, as in I.

Later approved text (#362): merged PRs after these comments were read put newer approved text into
data.py by hand. Those replacements are the last step of the run (after build, for --check too) and live
in sources.json under "later", grouped by merged PR. Each field names its path (relative to the data dict
build() returns: locale, then the field), the commit whose data.py holds the approved text, the sha256 of
the pinned text it replaces (old_sha256) and of the approved text (new_sha256), and, when the text is
verbatim in an approval comment, that comment's id. An old_sha256 of null means the path is new (the
marsdawn 0.7.7 changelog entries): the parent must exist and the key must not. The comments (id,
updated_at, sha256) are pinned in the same group. A path that is listed twice or not there, pinned text
or approved text that does not hash to the recorded value, a comment that changed, or a field that names a
comment its group does not pin stops the run with exit 1. Only data is patched, not the shared dict.
This layer also carries what the unpinned approved360.json (PR #354) held for #360, so that file and its
step are gone: it still had the zh-Hant text from before #286, which the PR #367 cells here replace.

Writes scripts/cli254/data.py, which scripts/build_pages.py reads (apply_cli254). The text is the
comments' Markdown; the build turns it into HTML with rich_pages.md_inline. Schema notes are HTML in
the source and stay HTML.

    python3 -I -B scripts/cli254/ingest.py           # verify the comments, write data.py
    python3 -I -B scripts/cli254/ingest.py --check   # verify, compare with data.py, write nothing
Exit codes: 0 ok, 1 --check differs, a pinned comment differs, a parse assertion failed, gh api failed
or the later layer stopped.

It needs gh, so it runs locally, never in CI.
"""
import argparse
import ast
import hashlib
import json
import pprint
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
REPO = "redtear1115/mars-dawn-website"
LABELS = {"en": "en", "zh-Hant": "zh-hant", "zh-Hans": "zh-hans", "ja": "ja", "ko": "ko", "de": "de",
          "fr": "fr", "es": "es"}
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
SCHEMA_KEYS = ["open_v4", "open", "error_v3", "error"]


class Stop(SystemExit):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch(pinned: dict) -> str:
    out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{pinned['id']}"], capture_output=True, text=True)
    if out.returncode:
        raise Stop(f"gh api failed for comment {pinned['id']}: {out.stderr.strip()}")
    got = json.loads(out.stdout)
    digest = sha256(got["body"])
    if digest != pinned["sha256"] or got["updated_at"] != pinned["updated_at"]:
        raise Stop(f"comment {pinned['id']} differs from the pinned source: sha256 {digest} vs {pinned['sha256']}, "
                   f"updated_at {got['updated_at']} vs {pinned['updated_at']}")
    if f"/issues/{pinned['issue']}#" not in got["html_url"]:
        raise Stop(f"comment {pinned['id']} is not on #{pinned['issue']}: {got['html_url']}")
    print(f"verified #{pinned['issue']} comment {pinned['id']}: sha256 {digest[:12]} updated_at {got['updated_at']}")
    return got["body"]


def label(line: str):
    """The locale a line names on its own (**en**, **zh-Hant**, ### ja ...), or None."""
    m = re.fullmatch(r"(?:\*\*|#+ )([A-Za-z-]+)(?:\*\*)?\s*", line)
    return LABELS.get(m.group(1)) if m else None


def blocks(body: str):
    """(section, locale, text) for every fenced block, in order. section is the last ###/#### heading
    outside a fence (its number, such as "2a."); locale is the last locale label, reset by a heading."""
    section, locale, fence, out = "", None, None, []
    for line in body.replace("\r\n", "\n").split("\n"):
        if fence is not None:
            if line.strip() == "```":
                out.append((section, locale, "\n".join(fence)))
                fence = None
            else:
                fence.append(line)
            continue
        if line.startswith("```"):
            fence = []
            continue
        loc = label(line)
        if loc:
            locale = loc
        elif re.match(r"#{2,4} ", line):
            section, locale = line.lstrip("#").strip().split(" ")[0], None
    if fence is not None:
        raise Stop("an unclosed fence")
    return out


def table_rows(body: str, section: str):
    """The rows of the Markdown table under the heading that starts with section."""
    lines = body.replace("\r\n", "\n").split("\n")
    start = next(i for i, line in enumerate(lines) if re.match(rf"#{{2,4}} {re.escape(section)}", line))
    rows = []
    for line in lines[start + 1:]:
        if re.match(r"#{2,4} ", line):
            break
        if line.startswith("|"):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def bullets(text: str) -> list:
    lines = text.split("\n")
    if not lines or not all(line.startswith("- ") for line in lines):
        raise Stop(f"not a bullet list: {text!r}")
    return [line[2:] for line in lines]


def one_line(text: str) -> str:
    if "\n" in text or not text.strip():
        raise Stop(f"not one line: {text!r}")
    return text


def entry(text: str, version: str) -> str:
    if not text.startswith(f"## marsdawn {version}\n\n"):
        raise Stop(f"not the {version} entry: {text[:40]!r}")
    return text


def take(found: list, section: str, locale, count: int) -> list:
    got = [text for sec, loc, text in found if sec == section and loc == locale]
    if len(got) != count:
        raise Stop(f"section {section} {locale}: {len(got)} blocks, expected {count}")
    return got


def parse_a(body: str, locales: list, data: dict) -> None:
    found = blocks(body)
    for loc in locales:
        d = data[loc]
        o1, o2, o3, since = take(found, "1.", loc, 4)
        d["open_items"] = [b for t in (o1, o2, o3) for b in bullets(t)]
        d["open_since"] = one_line(since)
        (folder,) = take(found, "2.", loc, 1)
        d["agents_folder_items"] = bullets(folder)
        (cl,) = take(found, "3.", loc, 1)
        d["changelog"]["0.6.4"] = entry(cl, "0.6.4")


def parse_b(body: str, locales: list, data: dict, shared: dict) -> None:
    found = blocks(body)
    (example,) = take(found, "2b.", None, 1)
    shared["theme_example"] = example
    for loc in locales:
        d = data[loc]
        c072, c061 = take(found, "1.", loc, 2)
        d["changelog"]["0.7.2"] = entry(c072, "0.7.2")
        d["changelog"]["0.6.1"] = entry(c061, "0.6.1")
        items, after_json, since = take(found, "2a.", loc, 3)
        d["export_items"] = bullets(items)
        d["export_after_json"] = bullets(after_json)
        d["export_since"] = one_line(since)
        (theme,) = take(found, "2b.", loc, 1)
        if not theme.startswith("### marsdawn theme\n\n"):
            raise Stop(f"{loc}: the theme section has no heading")
        d["theme_section"] = theme
    rows = table_rows(body, "3.")
    head, rows = rows[0], [r for r in rows[2:]]
    cols = {LABELS[h]: i for i, h in enumerate(head) if h in LABELS}
    for loc in locales:
        notes = {}
        for row in rows:
            key = re.match(r"`(\w+)`", row[0]).group(1)
            notes[key] = row[cols[loc]]
        if sorted(notes) != sorted(SCHEMA_KEYS):
            raise Stop(f"{loc}: schema note keys {sorted(notes)}")
        data[loc]["schema_notes"] = notes


EDIT = re.compile(r"(`+) ?(.+?) ?\1 → (`+) ?(.+?) ?\3")


def parse_c(body: str, edits: str, locales: list, data: dict) -> None:
    found = blocks(body)
    lines = edits.replace("\r\n", "\n").split("\n")
    start = lines.index(next(line for line in lines if line.startswith("### 6c.")))
    todo = {}
    for line in lines[start + 1:]:
        if line.startswith("#"):
            break
        m = re.match(r"- \[ \] (\S+) (0\.7\.[01])：(.*)$", line)
        if m:
            pairs = [(e.group(2), e.group(4)) for e in EDIT.finditer(m.group(3))]
            if not pairs:
                raise Stop(f"6c: no edit in {line!r}")
            todo[(LABELS[m.group(1)], m.group(2))] = pairs
    if sorted(todo) != [("en", "0.7.1"), ("ja", "0.7.1"), ("zh-hant", "0.7.0")]:
        raise Stop(f"6c: unexpected edits {sorted(todo)}")
    todo[("ja", "0.7.1")].append(("マニュアル", "ハンドブック"))
    for loc in locales:
        (text,) = take(found, "2.", loc, 1)
        parts = re.split(r"(?m)^(?=## marsdawn )", text)
        got = {re.match(r"## marsdawn (\S+)", part).group(1): part.rstrip("\n") for part in parts if part.strip()}
        if sorted(got) != ["0.6.4", "0.7.0", "0.7.1"]:
            raise Stop(f"C {loc}: versions {sorted(got)}")
        for v in ("0.7.1", "0.7.0"):
            entry_text = entry(got[v], v)
            for old, new in todo.get((loc, v), []):
                if old.endswith("…") and new.endswith("…"):
                    old, new = old[:-1], new[:-1]
                n = entry_text.count(old)
                if n != 1 and not (old == "マニュアル" and n >= 1):
                    raise Stop(f"C {loc} {v}: {old!r} found {n} times")
                entry_text = entry_text.replace(old, new)
            data[loc]["changelog"][v] = entry_text


def parse_i(body: str, locales: list, data: dict) -> None:
    text = body.replace("\r\n", "\n")
    parts = re.split(r"(?m)^## ", text)
    by_loc = {}
    for part in parts:
        head = part.split("\n", 1)[0].strip()
        if head in LABELS and LABELS[head] in locales:
            by_loc[LABELS[head]] = part
    if sorted(by_loc) != sorted(locales):
        raise Stop(f"I: locale sections {sorted(by_loc)}")
    for loc in locales:
        found = []
        item, fence = None, None
        for line in by_loc[loc].split("\n"):
            if fence is not None:
                if line.strip() == "```":
                    found.append((item, "\n".join(fence)))
                    fence = None
                else:
                    fence.append(line)
                continue
            if line.startswith("```"):
                fence = []
                continue
            m = re.match(r"\*\*([A-F])\. ", line)
            if m:
                item = m.group(1)
        got = {k: [t for i, t in found if i == k] for k in "ABCDF"}
        counts = {k: len(v) for k, v in got.items()}
        if counts != {"A": 1, "B": 3, "C": 1, "D": 1, "F": 2}:
            raise Stop(f"I {loc}: blocks per item {counts}")
        d = data[loc]
        items, _, since = got["A"][0].partition("\n\n")
        d["open_items"] = bullets(items)
        d["open_since"] = one_line(since)
        d["export_items"] = bullets(got["B"][0])
        d["export_after_json"] = bullets(got["B"][1])
        d["export_since"] = one_line(got["B"][2])
        if not got["C"][0].startswith("### marsdawn theme\n\n"):
            raise Stop(f"I {loc}: the theme section has no heading")
        d["theme_section"] = got["C"][0]
        d["agents_folder_items"] = bullets(got["D"][0])
        entries = "\n\n".join(got["F"])
        for chunk in re.split(r"(?m)^(?=### marsdawn )", entries):
            if not chunk.strip():
                continue
            v = re.match(r"### marsdawn (\S+)\n\n", chunk).group(1)
            if v in d["changelog"]:
                raise Stop(f"I {loc}: {v} twice")
            d["changelog"][v] = entry(chunk[1:].rstrip("\n"), v)
        if sorted(d["changelog"]) != ["0.6.1", "0.6.4", "0.7.0", "0.7.1", "0.7.2"]:
            raise Stop(f"I {loc}: changelog versions {sorted(d['changelog'])}")
    rows = table_rows(body, "E.")
    head, rows = rows[0], rows[2:]
    cols = {LABELS[h]: i for i, h in enumerate(head) if h in LABELS}
    for loc in locales:
        notes = {re.match(r"`(\w+)`", row[0]).group(1): row[cols[loc]] for row in rows}
        if sorted(notes) != sorted(SCHEMA_KEYS):
            raise Stop(f"I {loc}: schema note keys {sorted(notes)}")
        data[loc]["schema_notes"] = notes


def apply_295(data: dict) -> None:
    """Apply the owner's supplied #295 snapshots, pinned locally without network metadata.

    Remote comment ids/updated_at were not supplied for both files. Keep their exact bodies
    and hashes rather than inventing remote pins; these override #254's older schema notes.
    """
    for pin in SOURCES["local_copy_295"]:
        body = (HERE / pin["path"]).read_text(encoding="utf-8")
        if sha256(body) != pin["sha256"]:
            raise Stop(f"#295 local copy differs: {pin['path']}")
        rows = table_rows(body, "1.")
        cols = {LABELS[h]: i for i, h in enumerate(rows[0]) if h in LABELS}
        for row in rows[2:]:
            key = re.match(r"`(\w+)`", row[0]).group(1)
            for loc in pin["locales"]:
                data[loc]["schema_notes"][key] = row[cols[loc]]


def apply_296(body: str, locales: list, data: dict) -> None:
    """J: under each locale, in order, /cli/agents/'s `folder` item, its `status` item and /cli/'s --json item."""
    found = blocks(body)
    for locale in locales:
        lines = [text for _, loc, text in found if loc == locale]
        if len(lines) != 3:
            raise Stop(f"J: {locale} has {len(lines)} blocks, not 3")
        folder, status, json_item = (bullets(one_line(text))[0] for text in lines)
        if not folder.startswith("`folder`") or "`status`" not in status or "--json" not in json_item:
            raise Stop(f"J: {locale}'s blocks are not the three expected lines")
        d = data[locale]
        if len(d["agents_folder_items"]) != 1 or len(d["open_items"]) != 3 or "--json" not in d["open_items"][2]:
            raise Stop(f"J: {locale}'s earlier items are not the ones J replaces")
        d["agents_folder_line"] = folder
        d["agents_folder_items"] = [status]
        d["open_items"][2] = json_item


NEW_355 = ["0.7.6", "0.7.5", "0.7.4", "0.7.3"]


def apply_355(body: str, locales: list, data: dict) -> None:
    """K and K_i18n: each locale's section holds one block with the four entries, newest first."""
    names = {name.lower(): site for name, site in LABELS.items()}
    sections = {}
    for part in re.split(r"(?m)^## ", body.replace("\r\n", "\n")):
        head = part.split("\n", 1)[0].strip().lower()
        if head in names and names[head] in locales:
            sections[names[head]] = part
    if sorted(sections) != sorted(locales):
        raise Stop(f"K: locale sections {sorted(sections)}")
    for locale in locales:
        found = re.findall(r"(?ms)^```md\n(.*?)\n```$", sections[locale])
        if len(found) != 1:
            raise Stop(f"K {locale}: {len(found)} blocks")
        chunks = re.split(r"(?m)^(?=### marsdawn )", found[0])
        chunks = [chunk.rstrip("\n") for chunk in chunks if chunk.strip()]
        versions = [re.match(r"### marsdawn (\S+)\n\n", chunk).group(1) for chunk in chunks]
        if versions != NEW_355:
            raise Stop(f"K {locale}: versions {versions}")
        for version, chunk in zip(versions, chunks):
            data[locale]["changelog"][version] = entry(chunk[1:], version)


def build() -> tuple:
    c = SOURCES["comments"]
    fetch(c["approval"])
    fetch(c["approval_c"])
    fetch(c["ja_name"])
    approved = ["en", "zh-hant", "ja"]
    data = {loc: {"changelog": {}} for loc in approved}
    shared = {}
    parse_a(fetch(c["A"]), approved, data)
    parse_b(fetch(c["B"]), approved, data, shared)
    parse_c(fetch(c["C"]), fetch(c["C_edits"]), approved, data)
    machine = ["zh-hans", "ko", "de", "fr", "es"]
    for loc in machine:
        data[loc] = {"changelog": {}}
    parse_i(fetch(c["I"]), machine, data)
    apply_295(data)
    fetch(c["approval_296"])
    apply_296(fetch(c["J"]), approved + machine, data)
    fetch(c["approval_355"])
    apply_355(fetch(c["K"]), ["en", "zh-hant"], data)
    apply_355(fetch(c["K_i18n"]), ["zh-hans", "ja", "ko", "de", "fr", "es"], data)
    return data, shared


# ---- later approved text (#362) ----------------------------------------------------------------

def value_sha256(value) -> str:
    return sha256(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True))


def data_at(commit: str) -> dict:
    """DATA of scripts/cli254/data.py at a commit, read from the git object (a literal, never executed)."""
    out = subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:scripts/cli254/data.py"], capture_output=True)
    if out.returncode:
        raise Stop(f"git show {commit}:scripts/cli254/data.py failed: {out.stderr.decode(errors='replace')[:200]}")
    for node in ast.parse(out.stdout.decode("utf-8")).body:
        if isinstance(node, ast.Assign) and [getattr(t, "id", None) for t in node.targets] == ["DATA"]:
            return ast.literal_eval(node.value)
    raise Stop(f"no DATA in scripts/cli254/data.py at {commit}")


def at_path(node, path: list, where: str):
    for part in path:
        try:
            node = node[part]
        except (KeyError, IndexError, TypeError):
            raise Stop(f"{where}: path {'/'.join(map(str, path))} not found at {part!r}")
    return node


def pinned_comment(pin: dict, pr: int) -> None:
    """A later-layer approval comment (GET by id), held to its pinned sha256 and updated_at. Unlike fetch()
    it does not check the issue: these comments sit on PRs and on other issues."""
    out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{pin['id']}"], capture_output=True, text=True)
    if out.returncode:
        raise Stop(f"gh api failed for comment {pin['id']} (later, PR #{pr}): {out.stderr.strip()}")
    got = json.loads(out.stdout)
    digest = sha256(got["body"])
    if digest != pin["sha256"] or got["updated_at"] != pin["updated_at"]:
        raise Stop(f"comment {pin['id']} (later, PR #{pr}) differs from the pinned source: sha256 {digest} vs {pin['sha256']}, "
                   f"updated_at {got['updated_at']} vs {pin['updated_at']}")


def apply_later(out: dict) -> None:
    """Replace the pinned text with the approved text the merged PRs put into data.py (sources.json "later"),
    or add it where old_sha256 is null. Every failure here exits 1."""
    blobs, seen = {}, set()
    kinds = {"comment": 0, "pr": 0}
    later = SOURCES.get("later")
    if not later or not later.get("prs"):
        raise Stop('sources.json has no "later" layer: the approved text would be put back to the pinned text')
    for group in later["prs"]:
        pr = group["pr"]
        pins = group.get("comments", [])
        for pin in pins:
            pinned_comment(pin, pr)
        known = {pin["id"] for pin in pins}
        for field in group["fields"]:
            path, where = field["path"], f"later PR #{pr}"
            name = "/".join(map(str, path))
            if tuple(path) in seen:
                raise Stop(f"{where}: path {name} is listed twice")
            seen.add(tuple(path))
            if not set(field.get("comments", [])) <= known:
                raise Stop(f"{where}: {name} names a comment that the group does not pin")
            if field["old_sha256"] is None:
                parent = at_path(out, path[:-1], where)
                if not isinstance(parent, dict) or path[-1] in parent:
                    raise Stop(f"{where}: {name} has old_sha256 null, so its parent must be a dict without that key")
            else:
                old = at_path(out, path, where)
                if value_sha256(old) != field["old_sha256"]:
                    raise Stop(f"{where}: {name} is not the pinned text any more (sha256 {value_sha256(old)} vs {field['old_sha256']})")
            commit = field["commit"]
            if commit not in blobs:
                blobs[commit] = data_at(commit)
            new = at_path(blobs[commit], path, f"{where} at {commit[:9]}")
            if value_sha256(new) != field["new_sha256"]:
                raise Stop(f"{where}: approved text at {commit[:9]} for {name} does not match the pinned sha256 "
                           f"{field['new_sha256']} (got {value_sha256(new)})")
            at_path(out, path[:-1], where)[path[-1]] = new
            kinds["comment" if field.get("comments") else "pr"] += 1
    print(f"applied {sum(kinds.values())} later replacements: {kinds['comment']} pinned to an approval comment, {kinds['pr']} to a merged PR")


def render(data: dict, shared: dict) -> str:
    pins = {k: {f: v[f] for f in ("issue", "id", "sha256")} for k, v in SOURCES["comments"].items()}
    return ('"""Generated by scripts/cli254/ingest.py from the pinned comments in sources.json. Do not edit by hand."""\n\n'
            f"SOURCES = {pprint.pformat(pins, width=110, sort_dicts=True)}\n\n"
            f"SHARED = {pprint.pformat(shared, width=110, sort_dicts=True)}\n\n"
            f"DATA = {pprint.pformat(data, width=110, sort_dicts=True)}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    data, shared = build()
    apply_later(data)
    text = render(data, shared)
    target = HERE / "data.py"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("data.py differs from what the pinned comments give", file=sys.stderr)
            return 1
        print("data.py matches the pinned comments")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target.relative_to(HERE.parent.parent)}: {', '.join(sorted(data))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
