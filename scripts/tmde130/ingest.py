#!/usr/bin/env python3
"""Ingestion for /changelog/'s app sections (website #273, plan PLAN-web-tmde-130 slice S1; #368 adds iOS).

Every string the sections put on the site comes from a pinned source and is carried here by program,
never typed:

- the page copy (description, intro, the three section headings, the CLI line, the iOS line, the 1.0.0
  line and the "earlier versions are in English only" line): Grok's two comments on #273 (C1, C2), then
  Aria's comment on #368 (C3), fetched by id with `gh api` and held to the sha256 and `updated_at` in
  sources.json (en, zh-Hant and ja of C1 approved by the owner, comment 6251240241; the other five under
  the standing machine-locale OK; C3 approved by the owner, comment 6796386327). C3's app_h and intro
  replace C1/C2's (put(..., replace=True), the slot row says C3); its ios_h and ios_line are new;
- each version's What's New: the app repo's docs/release-notes/<version>.md (Mac) or
  docs/release-notes/ios-<version>.md (iOS, whose numbers collide with the Mac's) at the pinned commit,
  held to its sha256, with HTML comments stripped and `## <locale>` sections split exactly as the app's
  tools/release/asc.py does before it sends them to App Store Connect. A pin is one commit and the files
  read at it, so files from different commits can be pinned side by side. The app repo is private, so the
  stripped text is vendored into vendor/app-release-notes/whats-new.json (the Mac's under "versions", the
  iOS's under "ios"."versions": other scripts read only the first);
- which locales each Mac version has on the App Store, and that 1.0.0's What's New is empty: the App
  Store Connect read of 2026-10-18 (GET only), passed with --asc and held to its sha256. Every
  non-empty What's New there must equal the release notes text: any difference stops the run (#273
  promised that nothing is picked automatically). Without --asc, a Mac version that was already
  verified that way is carried from the committed whats-new.json, after checking that its release notes
  file still has the pinned sha256, parses to exactly the committed texts, and that its dates are the
  pinned ones; the run says so (it is not re-verified against App Store Connect). A version that is not
  in the committed file as verified needs --asc;
- each version's date: the App Store's public version history (apps.apple.com), as pinned in
  sources.json (the Mac page for Mac versions, ios.dates.url for iOS ones). The live page is read again
  and a different date stops the run;
- a version that is not on the App Store yet is "pending" in sources.json: its What's New is the release
  notes file (sha256 held), its date is the pinned `released` (a due date until the day it ships), and
  neither the ASC read nor the public page is consulted. whats-new.json records it with "pending": true
  and no store date. scripts/check_app_changelog.py --release fails while any version is pending.
  The build leaves a pending version out of every page, Markdown twin, llms file and JSON-LD (it is
  vendored, not published), and scripts/check_app_changelog.py --no-pending-in-public proves that;

When a release lands (the day a pending version is on the App Store), for each version that shipped:
  1. in sources.json, remove `"pending": true` from the version, set `released` to the UTC date of
     the App Store's version history and add `released_at_store` (the timestamp the page gives);
  2. python3 -I -B scripts/tmde130/ingest.py --app-repo PATH --asc FILE   # writes whats-new.json and
     manifest.json (the Mac version needs --asc the first time; the iOS one takes its date from ios.dates.url);
  3. python3 -I -B scripts/build_pages.py   # about 15 minutes; the version now appears on /changelog/
     in all eight locales, in the Markdown twins, llms-full.txt and, for the Mac, the home page's softwareVersion;
  4. python3 -I -B scripts/check_app_changelog.py --self-test --release   # no version left pending;
     python3 -I -B scripts/check_app_changelog.py --no-pending-in-public  # nothing pending left in public/;
  5. git status is clean after the build except for the files you meant to change; commit.

Outputs: vendor/app-release-notes/whats-new.json and manifest.json (sha256 of whats-new.json),
scripts/tmde130/data.py (the page copy the build reads) and scripts/tmde130/slots.json (one row per
shipped string: field x locale -> source).

    python3 -I -B scripts/tmde130/ingest.py --app-repo PATH [--asc FILE]           # verify, write
    python3 -I -B scripts/tmde130/ingest.py --app-repo PATH [--asc FILE] --check   # verify, compare, write nothing
    python3 -I -B scripts/tmde130/ingest.py --self-test                            # offline unit checks

It needs gh, the private app repo and (for a first verification) the ASC read, so it runs locally, never
in CI. CI checks the vendored files with scripts/check_app_changelog.py.
"""
import argparse
import copy as copylib
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
SHARED_LOCALE = {"fr-CA": "fr-FR", "es-MX": "es-ES"}
# C1's section headings (first round) and C2's item labels -> data fields.
C1_FIELDS = [("title", None), ("meta description", "description"), ("頁首說明", "intro"), ("兩區標題", "h2"),
             ("CLI 區開頭", "cli_line"), ("1.0.0 的條目", "first_release"), ("較早版本只有英文說明", "earlier")]
C2_FIELDS = {"meta": "description", "頁首": "intro", "H2": "h2", "CLI 區開頭": "cli_line",
             "1.0.0": "first_release", "較早版本": "earlier"}
# C3's tables (section C3_HEAD): these two replace the field C1/C2 gave, these two are new.
C3_HEAD = "## 頁面文字（新寫）"
C3_REPLACES = ("app_h", "intro")
C3_NEW = ("ios_h", "ios_line")
FIELDS = ["description", "intro", "app_h", "cli_h", "cli_line", "first_release", "earlier", "ios_h", "ios_line"]
STAMP_UTC = "GMT+0000 (Coordinated Universal Time)"


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


def put(copy: dict, locale: str, field: str, val: str, replace: bool = False) -> None:
    """Set copy[locale][field]. A field set twice stops the run, unless replace says this source
    deliberately takes the field over from an earlier one (C3 over C1/C2): then it must already be there."""
    if field == "h2":
        parts = val.split("` ／ `")
        if len(parts) != 2:
            raise Stop(f"{locale}: the H2 item is not two headings: {val!r}")
        put(copy, locale, "app_h", parts[0], replace)
        put(copy, locale, "cli_h", parts[1], replace)
        return
    if replace and field not in copy[locale]:
        raise Stop(f"{locale}/{field}: nothing to replace")
    if not replace and field in copy[locale]:
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


def md_tables(text: str):
    """(header cells, rows) of each markdown table in text. A row with another number of cells than the
    header, or a table without its |---| line, stops the run."""
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if not lines[i].startswith("|"):
            i += 1
            continue
        j = i
        while j < len(lines) and lines[j].startswith("|"):
            j += 1
        rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines[i:j]]
        if len(rows) < 3 or not all(re.fullmatch(r":?-+:?", c) for c in rows[1]):
            raise Stop(f"C3: the table at line {i + 1} has no header and |---| line")
        if any(len(r) != len(rows[0]) for r in rows):
            raise Stop(f"C3: a row of the table at line {i + 1} has another number of cells than its header")
        yield rows[0], rows[2:]
        i = j


def parse_c3(body: str, copy: dict, slots: list) -> None:
    """Aria's page copy for #368: the tables under C3_HEAD, `語系 | field | ...`, one row per locale.
    C3_REPLACES fields take over from C1/C2 (and their slot rows become C3); C3_NEW fields are added."""
    if body.count("\n" + C3_HEAD + "\n") != 1:
        raise Stop(f"C3: no single {C3_HEAD!r} section")
    section = re.split(r"^## ", body.split("\n" + C3_HEAD + "\n", 1)[1], maxsplit=1, flags=re.M)[0]
    seen = []
    for header, rows in md_tables(section):
        if header[0] != "語系" or not all(f in C3_REPLACES + C3_NEW for f in header[1:]):
            raise Stop(f"C3: unexpected table header {header!r}")
        if sorted(r[0] for r in rows) != sorted(LOCALES):
            raise Stop(f"C3: the table {header!r} does not have each locale exactly once")
        for row in rows:
            locale = row[0]
            for field, val in zip(header[1:], row[1:]):
                replace = field in C3_REPLACES
                put(copy, locale, field, val, replace=replace)
                mine = {"locale": locale, "field": field, "source": "C3", "section": C3_HEAD[3:]}
                if replace:
                    old = [i for i, s in enumerate(slots) if s["locale"] == locale and s["field"] == field]
                    if len(old) != 1:
                        raise Stop(f"C3: {locale}/{field} has {len(old)} slot rows to replace")
                    slots[old[0]] = mine
                else:
                    slots.append(mine)
        seen += header[1:]
    if sorted(seen) != sorted(C3_REPLACES + C3_NEW):
        raise Stop(f"C3: the tables give {seen}, expected {list(C3_REPLACES + C3_NEW)}")


def page_copy() -> tuple:
    copy = {locale: {} for locale in LOCALES}
    slots = []
    c1 = comment("C1").split("\n## 風險")[0]
    c2 = comment("C2").split("\n## 風險")[0]
    c3 = comment("C3")
    parse_c1(c1, copy, slots)
    parse_c2(c2, copy, slots)
    parse_c3(c3, copy, slots)
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


def notes_path(platform: str, version: str) -> str:
    """Where the app repo keeps a version's release notes: the Mac's as <version>.md, the iOS app's as
    ios-<version>.md (its version numbers collide with the Mac's)."""
    return f"docs/release-notes/{'ios-' if platform == 'ios' else ''}{version}.md"


def pin_of(path: str) -> tuple:
    """(commit, sha256) that sources.json pins for a release notes file."""
    found = [(pin["commit"], pin["files"][path]) for pin in SOURCES["app"]["pins"] if path in pin["files"]]
    if len(found) != 1:
        raise Stop(f"{path} is pinned {len(found)} times in sources.json, expected once")
    return found[0]


def release_notes(app_repo: Path, path: str) -> dict:
    commit, pinned = pin_of(path)
    out = subprocess.run(["git", "-C", str(app_repo), "show", f"{commit}:{path}"], capture_output=True)
    if out.returncode:
        raise Stop(f"git show {commit[:12]}:{path} failed: {out.stderr.decode().strip()}")
    digest = sha256(out.stdout)
    if digest != pinned:
        raise Stop(f"{path} at {commit[:12]} differs from the pinned sha256: {digest}")
    print(f"verified {path} at {commit[:12]}: sha256 {digest[:12]}")
    return parse_release_notes(out.stdout.decode("utf-8"))


def asc_read(path: Path) -> dict:
    raw = path.read_bytes()
    pinned = SOURCES["asc"]
    if sha256(raw) != pinned["sha256"]:
        raise Stop(f"{path} differs from the pinned App Store Connect read: sha256 {sha256(raw)}")
    print(f"verified the App Store Connect read of {pinned['fetched_at']}: sha256 {pinned['sha256'][:12]}")
    return json.loads(raw)


def parse_store_dates(page: str) -> dict:
    """{version: timestamp string} from the text of an App Store version history page."""
    found = {}
    for version, stamp in re.findall(r'"primarySubtitle":"(?:Version )?([0-9.]+)","secondarySubtitle":"([^"]+)"', page):
        if found.setdefault(version, stamp) != stamp:
            raise Stop(f"the App Store page gives version {version} two dates")
    return found


def store_dates(url: str) -> dict:
    """{version: UTC timestamp} from the App Store's public version history at url (the Mac page, or the
    iPhone page for iOS versions)."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return parse_store_dates(r.read().decode("utf-8"))


def check_store_date(v: str, pinned: dict, live: dict) -> None:
    """The public page still gives this version the pinned timestamp, and `released` is its UTC date."""
    stamp = pinned.get("released_at_store")
    if stamp is None:
        raise Stop(f"{v}: not pending, but sources.json has no released_at_store for it")
    if live.get(v) != stamp:
        raise Stop(f"{v}: the App Store page now says {live.get(v)!r}, pinned {stamp!r}")
    if not stamp.endswith(STAMP_UTC) or \
            datetime.datetime.strptime(stamp[:24], "%a %b %d %Y %H:%M:%S").date().isoformat() != pinned["released"]:
        raise Stop(f"{v}: released {pinned['released']} is not the UTC date of {stamp!r}")


def bullets_ok(v: str, loc: str, text: str) -> None:
    if text and not all(line.startswith("- ") for line in text.split("\n")):
        raise Stop(f"{v} {loc}: a line of the What's New is not a bullet")


def pending_entry(app_repo: Path, platform: str, pinned: dict) -> dict:
    """A version not on the App Store yet: the release notes file's text (all eight site locales, none
    empty, fr-CA and es-MX equal to the locale they share), the pinned due date, no store date."""
    v = pinned["version"]
    if "released_at_store" in pinned:
        raise Stop(f"{v}: pending, but sources.json also has a store date for it")
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", pinned["released"]):
            raise ValueError
        datetime.date.fromisoformat(pinned["released"])
    except ValueError:
        raise Stop(f"{v}: released {pinned['released']!r} is not a date")
    notes = release_notes(app_repo, notes_path(platform, v))
    lacking = sorted(l for l in list(ASC_LOCALE) + list(SHARED_LOCALE) if not notes.get(l))
    if lacking:
        raise Stop(f"{v} ({platform}): no What's New in {', '.join(lacking)} in the release notes")
    for shared, owner in SHARED_LOCALE.items():
        if notes[shared] != notes[owner]:
            raise Stop(f"{v} ({platform}): {shared} is not the same text as {owner}")
    texts = {}
    for loc in sorted(ASC_LOCALE):
        bullets_ok(v, loc, notes[loc])
        texts[loc] = notes[loc]
    entry = {"version": v}
    if platform == "mac":
        entry["asc_version_id"] = None
    entry.update({"released": pinned["released"], "released_at_store": None, "pending": True, "whatsNew": texts})
    return entry


def asc_entry(app_repo: Path, pinned: dict, asc: dict, live: dict) -> dict:
    """A Mac version on the App Store: its ASC record, its public date, and its release notes equal to
    the What's New the App Store has."""
    v = pinned["version"]
    on_store = asc["versions"].get(v)
    if on_store is None or on_store["state"] != "READY_FOR_DISTRIBUTION":
        raise Stop(f"{v} is not on the App Store in the ASC read")
    check_store_date(v, pinned, live)
    locs = on_store["localizations"]
    empty = sorted(loc for loc, rec in locs.items() if not rec["whatsNew"])
    if empty and (v != SOURCES["first_version"] or len(empty) != len(locs)):
        raise Stop(f"{v}: unexpected empty What's New in {', '.join(empty)}")
    notes = release_notes(app_repo, notes_path("mac", v)) if not empty else {}
    texts = {}
    for loc in sorted(locs):
        text = locs[loc]["whatsNew"]
        if text and notes.get(loc) != text:
            raise Stop(f"{v} {loc}: App Store Connect's What's New differs from docs/release-notes/{v}.md")
        if loc in ASC_LOCALE:
            bullets_ok(v, loc, text)
            texts[loc] = notes.get(loc, "")
    return {"version": v, "asc_version_id": on_store["id"], "released": pinned["released"],
            "released_at_store": pinned["released_at_store"], "whatsNew": texts}


def carried_entry(app_repo: Path, pinned: dict, committed: dict, live: dict) -> dict:
    """A Mac version that was verified against ASC when it was committed, taken from the committed file
    when no ASC read is given. What can be checked again is: the public date, the pinned dates, and that
    the pinned release notes file still gives each committed locale exactly its committed text. The ASC
    facts (the version id, which locales the App Store has) are carried as they are."""
    v = pinned["version"]
    old = [e for e in committed.get("versions", []) if e["version"] == v]
    if len(old) != 1 or old[0].get("pending") or old[0].get("asc_version_id") is None:
        raise Stop(f"{v}: no --asc given, and the committed whats-new.json has no verified entry for it to carry")
    old = old[0]
    check_store_date(v, pinned, live)
    if old["released"] != pinned["released"] or old["released_at_store"] != pinned["released_at_store"]:
        raise Stop(f"{v}: the committed dates differ from sources.json")
    texts = old["whatsNew"]
    if not texts or not set(texts) <= set(ASC_LOCALE):
        raise Stop(f"{v}: the committed What's New has unexpected locales: {sorted(texts)}")
    empty = all(not t for t in texts.values())
    if empty and v != SOURCES["first_version"]:
        raise Stop(f"{v}: the committed What's New is empty")
    notes = {} if empty else release_notes(app_repo, notes_path("mac", v))
    for loc, text in texts.items():
        if text != notes.get(loc, ""):
            raise Stop(f"{v} {loc}: the committed What's New differs from docs/release-notes/{v}.md at its pin")
        bullets_ok(v, loc, text)
    return old


def store_entry(app_repo: Path, platform: str, pinned: dict, live: dict) -> dict:
    """An iOS version that is on the App Store: its release notes file (no ASC read exists for iOS) and
    the date of the iPhone page. Nothing in the repo has this path yet; the pending path is the live one."""
    v = pinned["version"]
    check_store_date(v, pinned, live)
    notes = release_notes(app_repo, notes_path(platform, v))
    texts = {}
    for loc in sorted(ASC_LOCALE):
        if not notes.get(loc):
            raise Stop(f"{v} ({platform}): no What's New in {loc} in the release notes")
        bullets_ok(v, loc, notes[loc])
        texts[loc] = notes[loc]
    return {"version": v, "released": pinned["released"], "released_at_store": pinned["released_at_store"],
            "whatsNew": texts}


def committed_notes() -> dict:
    path = VENDOR / "whats-new.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def newest_first(entries: list) -> list:
    versions = [e["version"] for e in entries]
    if len(set(versions)) != len(versions):
        raise Stop(f"a version appears twice in sources.json: {versions}")
    return sorted(entries, key=lambda r: [int(n) for n in r["version"].split(".")], reverse=True)


def notes_json(app_repo: Path, asc_path) -> dict:
    asc = asc_read(asc_path) if asc_path else None
    committed = committed_notes()
    mac, carried, live = [], [], None
    for pinned in SOURCES["versions"]:
        if pinned.get("pending"):
            mac.append(pending_entry(app_repo, "mac", pinned))
            continue
        live = live if live is not None else store_dates(SOURCES["dates"]["url"])
        if asc is not None:
            mac.append(asc_entry(app_repo, pinned, asc, live))
        else:
            mac.append(carried_entry(app_repo, pinned, committed, live))
            carried.append(pinned["version"])
    if carried:
        print(f"ASC read not given: carried {', '.join(carried)} from the committed file "
              f"(not re-verified against App Store Connect)")
    ios, live = [], None
    for pinned in SOURCES["ios"]["versions"]:
        if pinned.get("pending"):
            ios.append(pending_entry(app_repo, "ios", pinned))
            continue
        live = live if live is not None else store_dates(SOURCES["ios"]["dates"]["url"])
        ios.append(store_entry(app_repo, "ios", pinned, live))
    return {"source": {"app_repo": SOURCES["app"]["repo"], "pins": SOURCES["app"]["pins"],
                       "asc_read": SOURCES["asc"]["fetched_at"],
                       "dates": SOURCES["dates"]["url"], "dates_read": SOURCES["dates"]["read"],
                       "ios_dates": SOURCES["ios"]["dates"]["url"], "ios_dates_read": SOURCES["ios"]["dates"]["read"]},
            "locale_map": ASC_LOCALE, "versions": newest_first(mac), "ios": {"versions": newest_first(ios)}}


def outputs(app_repo: Path, asc_path) -> dict:
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


# --- offline self-test: the parts no real data exercises yet (the iOS date path), and every stop ---------
def self_test() -> bool:
    global SOURCES, release_notes, store_dates
    saved = (SOURCES, release_notes, store_dates)
    ok = True

    def stops(label: str, fn, needle: str) -> None:
        nonlocal ok
        try:
            fn()
        except Stop as e:
            if needle in str(e):
                print(f"self-test: {label}: stopped as it should")
                return
            print(f"self-test: {label}: stopped, but with {e}")
        else:
            print(f"self-test: {label}: did not stop")
        ok = False

    def expect(label: str, got, want) -> None:
        nonlocal ok
        if got != want:
            print(f"self-test: {label}: got {got!r}, wanted {want!r}")
            ok = False
        else:
            print(f"self-test: {label}: ok")

    stamp = "Thu Oct 29 2026 10:20:30 GMT+0000 (Coordinated Universal Time)"
    page = ('x"primarySubtitle":"1.0.1","secondarySubtitle":"%s"y"primarySubtitle":"Version 1.0.0","secondarySubtitle":"Mon Oct 26 '
            '2026 01:02:03 GMT+0000 (Coordinated Universal Time)"' % stamp)
    try:
        # 1. the page parser and the date rule
        live = parse_store_dates(page)
        expect("parse_store_dates", sorted(live), ["1.0.0", "1.0.1"])
        stops("two dates for one version", lambda: parse_store_dates(page + page.replace("29 2026", "30 2026", 1)),
              "two dates")
        pinned = {"version": "1.0.1", "released": "2026-10-29", "released_at_store": stamp}
        check_store_date("1.0.1", pinned, live)
        stops("a different date on the page", lambda: check_store_date("1.0.1", pinned, {"1.0.1": stamp.replace("29", "30", 1)}),
              "now says")
        stops("a version the page lacks", lambda: check_store_date("1.0.2", {**pinned, "version": "1.0.2"}, live), "now says")
        stops("released is not the UTC date", lambda: check_store_date("1.0.1", {**pinned, "released": "2026-10-30"}, live),
              "not the UTC date")
        stops("no pinned store date", lambda: check_store_date("1.0.1", {"version": "1.0.1", "released": "2026-10-29"}, live),
              "no released_at_store")

        # 2. release notes of the right shape, to drive pending and iOS entries without the app repo
        text = {loc: "- one\n- two" for loc in list(ASC_LOCALE) + list(SHARED_LOCALE)}
        asked = []

        def fake_notes(repo, path):
            asked.append(path)
            return dict(fake_notes.value)
        fake_notes.value = text
        release_notes = fake_notes
        expect("notes_path mac", notes_path("mac", "1.0.2"), "docs/release-notes/1.0.2.md")
        expect("notes_path ios", notes_path("ios", "1.0.2"), "docs/release-notes/ios-1.0.2.md")
        pend = pending_entry(Path("."), "ios", {"version": "1.0.2", "pending": True, "released": "2026-11-23"})
        expect("pending ios entry", (pend["pending"], pend["released_at_store"], "asc_version_id" in pend, asked[-1]),
               (True, None, False, "docs/release-notes/ios-1.0.2.md"))
        pend = pending_entry(Path("."), "mac", {"version": "1.2.2", "pending": True, "released": "2026-11-23"})
        expect("pending mac entry", (pend["pending"], pend["released_at_store"], pend["asc_version_id"]), (True, None, None))
        for bad, why, needle in (({**text, "ja": ""}, "a locale with no text", "no What's New in ja"),
                                 ({**text, "fr-CA": "- other"}, "fr-CA unlike fr-FR", "fr-CA is not the same"),
                                 ({**text, "ko": "one\n- two"}, "a line that is not a bullet", "not a bullet")):
            fake_notes.value = bad
            stops(f"pending: {why}", lambda: pending_entry(Path("."), "mac", {"version": "1.2.2", "pending": True,
                                                                              "released": "2026-11-23"}), needle)
        fake_notes.value = text
        stops("pending with a store date", lambda: pending_entry(Path("."), "mac", {"version": "1.2.2", "pending": True,
              "released": "2026-11-23", "released_at_store": stamp}), "also has a store date")
        stops("pending with a bad date", lambda: pending_entry(Path("."), "mac", {"version": "1.2.2", "pending": True,
              "released": "2026-13-23"}), "is not a date")

        # 3. an iOS version that is no longer pending reads the iPhone page, not the Mac one
        urls = []

        def fake_dates(url):
            urls.append(url)
            return live
        store_dates = fake_dates
        SOURCES = copylib.deepcopy(saved[0])
        SOURCES["ios"]["versions"] = [{"version": "1.0.1", "released": "2026-10-29", "released_at_store": stamp}]
        SOURCES["versions"] = []
        full = notes_json(Path("."), None)
        expect("the iOS date read is the iPhone page", urls, [SOURCES["ios"]["dates"]["url"]])
        expect("an iOS entry has no pending flag", ("pending" in full["ios"]["versions"][0], full["ios"]["versions"][0]["released_at_store"]),
               (False, stamp))
        SOURCES["ios"]["versions"][0]["released_at_store"] = stamp.replace("29", "28", 1)
        stops("an iOS date that differs from the page", lambda: notes_json(Path("."), None), "now says")

        # 4. carrying a Mac version without the ASC read
        SOURCES = copylib.deepcopy(saved[0])
        mac = {"version": "1.0.1", "released": "2026-10-29", "released_at_store": stamp}
        committed = {"versions": [{"version": "1.0.1", "asc_version_id": "id1", "released": "2026-10-29",
                                   "released_at_store": stamp, "whatsNew": {"en-US": "- one\n- two"}}]}
        SOURCES["first_version"] = "1.0.0"
        SOURCES["app"]["pins"] = [{"commit": "c", "files": {"docs/release-notes/1.0.1.md": "s"}}]
        fake_notes.value = {"en-US": "- one\n- two"}
        expect("carry returns the committed entry", carried_entry(Path("."), mac, committed, live), committed["versions"][0])
        fake_notes.value = {"en-US": "- one\n- twO"}
        stops("carry: release notes changed", lambda: carried_entry(Path("."), mac, committed, live), "differs from docs/release-notes")
        fake_notes.value = {"en-US": "- one\n- two"}
        stops("carry: not in the committed file", lambda: carried_entry(Path("."), mac, {"versions": []}, live), "no verified entry")
        pending = {"versions": [{**committed["versions"][0], "pending": True}]}
        stops("carry: committed as pending", lambda: carried_entry(Path("."), mac, pending, live), "no verified entry")
        stops("carry: sources.json's released is not the store date's", lambda: carried_entry(
              Path("."), {**mac, "released": "2026-10-28"}, committed, live), "not the UTC date")
        moved = {"versions": [{**committed["versions"][0], "released": "2026-10-28"}]}
        stops("carry: committed date is not the pinned one", lambda: carried_entry(Path("."), mac, moved, live), "committed dates differ")
        stops("carry: the public page moved", lambda: carried_entry(Path("."), mac, committed, {"1.0.1": "x"}), "now says")

        # 5. C3 over C1/C2
        def rows(fields, cells):
            head = "| 語系 | " + " | ".join(fields) + " |\n|---|" + "---|" * len(fields) + "\n"
            return head + "".join(f"| {loc} | " + " | ".join(f"{c}-{loc}" for c in cells) + " |\n" for loc in LOCALES)

        body = ("## x\nprose\n\n" + C3_HEAD + "\n\ntext\n\n" + rows(["app_h", "ios_h", "ios_line"], ["a", "h", "l"]) + "\n"
                + rows(["intro"], ["i"]) + "\n## after\n| 語系 | zzz |\n|---|---|\n| en | q |\n")

        def base():
            return ({loc: {"app_h": "old", "intro": "old", "cli_h": "k"} for loc in LOCALES},
                    [{"locale": loc, "field": f, "source": "C1", "section": "s"} for loc in LOCALES for f in ("app_h", "intro", "cli_h")])
        c, s = base()
        parse_c3(body, c, s)
        expect("C3 replaces app_h and intro, adds ios_h and ios_line", sorted(c["ko"]), ["app_h", "cli_h", "intro", "ios_h", "ios_line"])
        expect("C3 values", (c["ko"]["app_h"], c["ko"]["intro"], c["ko"]["cli_h"]), ("a-ko", "i-ko", "k"))
        expect("slot rows of replaced fields say C3, others stay",
               sorted({(r["field"], r["source"]) for r in s}),
               [("app_h", "C3"), ("cli_h", "C1"), ("intro", "C3"), ("ios_h", "C3"), ("ios_line", "C3")])
        expect("no slot row is added for a replaced field", len(s), 8 * 3 + 8 * 2)
        c, s = base()
        c["en"].pop("app_h")
        stops("C3: nothing to replace", lambda: parse_c3(body, c, s), "nothing to replace")
        c, s = base()
        c["en"]["ios_h"] = "already"
        stops("C3: a new field that already exists", lambda: parse_c3(body, c, s), "appears twice")
        c, s = base()
        stops("C3: a locale missing", lambda: parse_c3(body.replace("| ko | a-ko | h-ko | l-ko |\n", ""), c, s), "exactly once")
        c, s = base()
        stops("C3: a field given twice", lambda: parse_c3(
              body.replace("\n## after", "\n" + rows(["intro"], ["j"]) + "\n## after"), c, s), "the tables give")
        c, s = base()
        stops("C3: no section", lambda: parse_c3(body.replace(C3_HEAD, "## other"), c, s), "no single")
        # a value that is not one trimmed line is as bad as in C1/C2
        c, s = base()
        stops("C3: an empty cell", lambda: parse_c3(body.replace("a-ko", ""), c, s), "not one trimmed line")
    finally:
        SOURCES, release_notes, store_dates = saved
    print("self-test:", "ok" if ok else "FAILED")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--app-repo", type=Path, help="a clone of the app repo that has the pinned commits")
    ap.add_argument("--asc", type=Path, help="the pinned App Store Connect read (JSON). Without it, Mac versions "
                                             "already verified against it are carried from the committed file")
    ap.add_argument("--check", action="store_true", help="compare with the committed files, write nothing")
    ap.add_argument("--self-test", action="store_true", help="offline checks of the rules; needs no other argument")
    args = ap.parse_args()
    if args.self_test:
        return 0 if self_test() else 1
    if args.app_repo is None:
        ap.error("--app-repo is required")
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
