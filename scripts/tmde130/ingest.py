#!/usr/bin/env python3
"""Ingestion for /changelog/'s app section (website #273, plan PLAN-web-tmde-130 slice S1).

Every string the section puts on the site comes from a pinned source and is carried here by program,
never typed:

- the page copy (description, intro, the two section headings, the CLI line, the 1.0.0 line and the
  "earlier versions are in English only" line): Grok's two comments on #273, fetched by id with
  `gh api` and held to the sha256 and `updated_at` in sources.json (en, zh-Hant and ja approved by
  the owner, comment 6251240241; the other five under the standing machine-locale OK);
- each app version's What's New: the app repo's docs/release-notes/<version>.md at the pinned
  commit, held to its sha256, with HTML comments stripped and `## <locale>` sections split exactly as
  the app's tools/release/asc.py does before it sends them to App Store Connect. The app repo is
  private, so the stripped text is vendored into vendor/app-release-notes/whats-new.json;
- which locales each version has on the App Store, and that 1.0.0's What's New is empty: the App
  Store Connect read of 2026-10-18 (GET only), passed with --asc and held to its sha256. Every
  non-empty What's New there must equal the release notes text: any difference stops the run (#273
  promised that nothing is picked automatically);
- each version's date: the App Store's public version history (apps.apple.com), as pinned in
  sources.json. The live page is read again and a different date stops the run.

Outputs: vendor/app-release-notes/whats-new.json and manifest.json (sha256 of whats-new.json),
scripts/tmde130/data.py (the page copy the build reads) and scripts/tmde130/slots.json (one row per
shipped string: field x locale -> source).

    python3 -I -B scripts/tmde130/ingest.py --app-repo PATH --asc FILE            # verify, write
    python3 -I -B scripts/tmde130/ingest.py --app-repo PATH --asc FILE --check    # verify, compare, write nothing

It needs gh, the private app repo and the ASC read, so it runs locally, never in CI. CI checks the
vendored files with scripts/check_app_changelog.py.
"""
import argparse
import datetime
import hashlib
import html
import json
import pprint
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
VENDOR = ROOT / "vendor" / "app-release-notes"
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
REPO = "redtear1115/mars-dawn-website"
LOCALES = ["en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko"]
# Comment labels -> site locales.
LABEL_LOCALE = {"en": "en", "zh-Hant": "zh-hant", "zh-Hans": "zh-hans", "ja": "ja", "ko": "ko", "de": "de", "fr": "fr", "es": "es"}
# App Store locales -> site locales (fr-CA and es-MX share fr-FR's and es-ES's text and have no page).
ASC_LOCALE = {"en-US": "en", "zh-Hant": "zh-hant", "zh-Hans": "zh-hans", "ja": "ja",
              "de-DE": "de", "fr-FR": "fr", "es-ES": "es", "ko": "ko"}
# C1's section headings (first round) and C2's item labels -> data fields.
C1_FIELDS = [("title", None), ("meta description", "description"), ("頁首說明", "intro"), ("兩區標題", "h2"),
             ("CLI 區開頭", "cli_line"), ("1.0.0 的條目", "first_release"), ("較早版本只有英文說明", "earlier")]
C2_FIELDS = {"meta": "description", "頁首": "intro", "H2": "h2", "CLI 區開頭": "cli_line",
             "1.0.0": "first_release", "較早版本": "earlier"}
FIELDS = ["description", "intro", "app_h", "cli_h", "cli_line", "first_release", "earlier"]


class Stop(SystemExit):
    pass


def sha256(data) -> str:
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def comment(key: str) -> str:
    pinned = SOURCES["comments"][key]
    out = subprocess.run(["gh", "api", f"repos/{REPO}/issues/comments/{pinned['id']}"], capture_output=True, text=True)
    if out.returncode:
        raise Stop(f"gh api failed for comment {pinned['id']}: {out.stderr.strip()}")
    got = json.loads(out.stdout)
    digest = sha256(got["body"])
    if digest != pinned["sha256"] or got["updated_at"] != pinned["updated_at"]:
        raise Stop(f"comment {pinned['id']} differs from the pinned source: sha256 {digest} vs {pinned['sha256']}, "
                   f"updated_at {got['updated_at']} vs {pinned['updated_at']}")
    print(f"verified comment {pinned['id']} ({key}): sha256 {digest[:12]} updated_at {got['updated_at']}")
    return got["body"]


def inline(text: str) -> str:
    """A pinned value as HTML: escaped, with [text](url) as a link. Nothing else is converted."""
    out, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)\s]+)\)", text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        out.append(f'<a href="{html.escape(m.group(2))}">{html.escape(m.group(1), quote=False)}</a>')
        pos = m.end()
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


ITEM = re.compile(r"^- \[ \] (?P<label>[^：（`]+?)(?:（[^）]*）)?(?:：(?:`(?P<val>.*)`(?:（不變）)?)?)?$")


def items(lines: list):
    """(label, value) for each check-box item: the value in backticks on the item's own line, or the
    fenced block right under it."""
    i = 0
    while i < len(lines):
        m = ITEM.match(lines[i])
        if m:
            val = m.group("val")
            if val is None:
                if i + 1 >= len(lines) or lines[i + 1] != "```":
                    raise Stop(f"item {lines[i]!r} has no value")
                end = lines.index("```", i + 2)
                val = "\n".join(lines[i + 2:end])
                i = end
            yield m.group("label").strip(), val
        i += 1


def put(copy: dict, locale: str, field: str, val: str) -> None:
    if field == "h2":
        parts = val.split("` ／ `")
        if len(parts) != 2:
            raise Stop(f"{locale}: the H2 item is not two headings: {val!r}")
        put(copy, locale, "app_h", parts[0])
        put(copy, locale, "cli_h", parts[1])
        return
    if field in copy[locale]:
        raise Stop(f"{locale}/{field} appears twice")
    if "\n" in val or not val.strip() or val != val.strip():
        raise Stop(f"{locale}/{field}: not one trimmed line: {val!r}")
    copy[locale][field] = val


def parse_c1(body: str, copy: dict, slots: list) -> None:
    sections = re.split(r"^### ", body, flags=re.M)[1:]
    seen = set()
    for section in sections:
        head, *lines = section.split("\n")
        match = [f for prefix, f in C1_FIELDS if head.startswith(prefix)]
        if len(match) != 1:
            raise Stop(f"C1: unknown section {head!r}")
        field = match[0]
        seen.add(head)
        for label, val in items(lines):
            locale = LABEL_LOCALE[label]
            if field is None:
                continue          # the titles are unchanged ("不變") and stay as the build has them
            put(copy, locale, field, val)
            for f in (["app_h", "cli_h"] if field == "h2" else [field]):
                slots.append({"locale": locale, "field": f, "source": "C1", "section": head})
    if len(seen) != len(C1_FIELDS):
        raise Stop(f"C1: {len(seen)} sections, expected {len(C1_FIELDS)}")


def parse_c2(body: str, copy: dict, slots: list) -> None:
    sections = re.split(r"^### ", body, flags=re.M)[1:]
    for section in sections:
        head, *lines = section.split("\n")
        if head not in LABEL_LOCALE:
            raise Stop(f"C2: unknown section {head!r}")
        locale = LABEL_LOCALE[head]
        for label, val in items(lines):
            if label not in C2_FIELDS:
                raise Stop(f"C2 {head}: unknown item {label!r}")
            field = C2_FIELDS[label]
            put(copy, locale, field, val)
            for f in (["app_h", "cli_h"] if field == "h2" else [field]):
                slots.append({"locale": locale, "field": f, "source": "C2", "section": head})
    # The "## 風險" part of C2 has no ### sections; anything after the last locale section is cut by split.


def page_copy() -> tuple:
    copy = {locale: {} for locale in LOCALES}
    slots = []
    c1 = comment("C1").split("\n## 風險")[0]
    c2 = comment("C2").split("\n## 風險")[0]
    parse_c1(c1, copy, slots)
    parse_c2(c2, copy, slots)
    for locale in LOCALES:
        need = [f for f in FIELDS if f not in ("first_release", "earlier")]
        missing = [f for f in need if f not in copy[locale]]
        if missing:
            raise Stop(f"{locale}: no {', '.join(missing)} in the pinned comments")
    data = {locale: {field: inline(val) for field, val in copy[locale].items()} for locale in LOCALES}
    return data, slots


# --- the app's release notes, split as tools/release/asc.py does (strip_comments, parse_release_notes) ---
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def strip_comments(text: str) -> str:
    mark = "\x00"
    if mark in text:
        raise Stop("the release notes contain a NUL character")
    text = COMMENT_RE.sub(mark, text)
    if "<!--" in text:
        raise Stop("the release notes have an unclosed <!-- comment")
    kept = []
    for line in text.splitlines():
        if mark in line and not line.replace(mark, "").strip():
            continue
        kept.append(line.replace(mark, ""))
    return "\n".join(kept)


def parse_release_notes(text: str) -> dict:
    notes, current, lines = {}, None, []
    for line in strip_comments(text).splitlines():
        m = re.match(r"##\s+([A-Za-z]{2,3}(?:-[A-Za-z0-9]+)*)(\s+\(.*\))?\s*$", line)
        if m:
            if current is not None:
                notes[current] = "\n".join(lines).strip()
            current, lines = m.group(1), []
            if current in notes:
                raise Stop(f"locale {current} appears twice in the release notes")
        elif current is not None:
            lines.append(line)
    if current is not None:
        notes[current] = "\n".join(lines).strip()
    return notes


def release_notes(app_repo: Path, version: str) -> dict:
    app = SOURCES["app"]
    path = f"docs/release-notes/{version}.md"
    out = subprocess.run(["git", "-C", str(app_repo), "show", f"{app['commit']}:{path}"], capture_output=True)
    if out.returncode:
        raise Stop(f"git show {app['commit'][:12]}:{path} failed: {out.stderr.decode().strip()}")
    digest = sha256(out.stdout)
    if digest != app["files"][path]:
        raise Stop(f"{path} at {app['commit'][:12]} differs from the pinned sha256: {digest}")
    print(f"verified {path} at {app['commit'][:12]}: sha256 {digest[:12]}")
    return parse_release_notes(out.stdout.decode("utf-8"))


def asc_read(path: Path) -> dict:
    raw = path.read_bytes()
    pinned = SOURCES["asc"]
    if sha256(raw) != pinned["sha256"]:
        raise Stop(f"{path} differs from the pinned App Store Connect read: sha256 {sha256(raw)}")
    print(f"verified the App Store Connect read of {pinned['fetched_at']}: sha256 {pinned['sha256'][:12]}")
    return json.loads(raw)


def store_dates() -> dict:
    """{version: UTC timestamp} from the App Store's public version history."""
    req = urllib.request.Request(SOURCES["dates"]["url"], headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        page = r.read().decode("utf-8")
    found = {}
    for version, stamp in re.findall(r'"primarySubtitle":"(?:Version )?([0-9.]+)","secondarySubtitle":"([^"]+)"', page):
        if found.setdefault(version, stamp) != stamp:
            raise Stop(f"the App Store page gives version {version} two dates")
    return found


def notes_json(app_repo: Path, asc_path: Path) -> dict:
    asc = asc_read(asc_path)
    live = store_dates()
    versions = []
    for pinned in SOURCES["versions"]:
        v = pinned["version"]
        on_store = asc["versions"].get(v)
        if on_store is None or on_store["state"] != "READY_FOR_DISTRIBUTION":
            raise Stop(f"{v} is not on the App Store in the ASC read")
        if live.get(v) != pinned["released_at_store"]:
            raise Stop(f"{v}: the App Store page now says {live.get(v)!r}, pinned {pinned['released_at_store']!r}")
        stamp = pinned["released_at_store"]
        if not stamp.endswith("GMT+0000 (Coordinated Universal Time)") or \
                datetime.datetime.strptime(stamp[:24], "%a %b %d %Y %H:%M:%S").date().isoformat() != pinned["released"]:
            raise Stop(f"{v}: released {pinned['released']} is not the UTC date of {stamp!r}")
        locs = on_store["localizations"]
        empty = sorted(loc for loc, rec in locs.items() if not rec["whatsNew"])
        if empty and (v != SOURCES["first_version"] or len(empty) != len(locs)):
            raise Stop(f"{v}: unexpected empty What's New in {', '.join(empty)}")
        notes = release_notes(app_repo, v) if not empty else {}
        texts = {}
        for loc in sorted(locs):
            text = locs[loc]["whatsNew"]
            if text and notes.get(loc) != text:
                raise Stop(f"{v} {loc}: App Store Connect's What's New differs from docs/release-notes/{v}.md")
            if loc in ASC_LOCALE:
                if text and not all(line.startswith("- ") for line in text.split("\n")):
                    raise Stop(f"{v} {loc}: a line of the What's New is not a bullet")
                texts[loc] = notes.get(loc, "")
        versions.append({"version": v, "asc_version_id": on_store["id"], "released": pinned["released"],
                         "released_at_store": pinned["released_at_store"], "whatsNew": texts})
    versions.sort(key=lambda r: [int(n) for n in r["version"].split(".")], reverse=True)
    return {"source": {"app_repo": SOURCES["app"]["repo"], "commit": SOURCES["app"]["commit"],
                       "files": SOURCES["app"]["files"], "asc_read": SOURCES["asc"]["fetched_at"],
                       "dates": SOURCES["dates"]["url"], "dates_read": SOURCES["dates"]["read"]},
            "locale_map": ASC_LOCALE, "versions": versions}


def outputs(app_repo: Path, asc_path: Path) -> dict:
    data, slots = page_copy()
    notes = json.dumps(notes_json(app_repo, asc_path), ensure_ascii=False, indent=1) + "\n"
    manifest = json.dumps({"whats-new.json": sha256(notes)}, indent=1) + "\n"
    header = ('"""Generated by scripts/tmde130/ingest.py from the comments pinned in sources.json. Do not edit:\n'
              'change the pin and run the ingester again."""\n\n')
    return {
        VENDOR / "whats-new.json": notes,
        VENDOR / "manifest.json": manifest,
        HERE / "data.py": header + "DATA = " + pprint.pformat(data, width=120, sort_dicts=False) + "\n",
        HERE / "slots.json": json.dumps(slots, ensure_ascii=False, indent=1) + "\n",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--app-repo", required=True, type=Path, help="a clone of the app repo that has the pinned commit")
    ap.add_argument("--asc", required=True, type=Path, help="the pinned App Store Connect read (JSON)")
    ap.add_argument("--check", action="store_true", help="compare with the committed files, write nothing")
    args = ap.parse_args()
    files = outputs(args.app_repo, args.asc)
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, text in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            print("differs from its sources: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"ok: {len(files)} files match their pinned sources")
        return 0
    VENDOR.mkdir(parents=True, exist_ok=True)
    for path, text in files.items():
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
