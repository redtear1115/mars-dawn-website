#!/usr/bin/env python3
"""Checks public/_redirects: the site's same-site redirects, which Cloudflare reads and never serves.

Usage:
    python3 scripts/check_redirects.py [--root public] [--phase pre-launch|launched]
    python3 scripts/check_redirects.py --self-test

The redirect that matters is `/go/app-store`, the one link the site publishes for the Mac App Store
listing: posts and READMEs link to it, and when its destination changes (launch day, then the App
Store Connect campaign token), every published link keeps working. The rules, from the app repo's
docs/website-plan.md §5.3:

- every line is `source destination [status]`; anything else Cloudflare silently ignores, so it
  fails here instead;
- a source is a plain same-site path (no splats or placeholders: the list is fixed) that no file
  answers, so a redirect can't shadow a page;
- a destination is either a same-site path that exists, or an external URL on the allow-list below
  (only apps.apple.com, and only in the listing form check_links.py holds the pages to), so there
  is no open redirect;
- an external destination carries no query string or fragment: nothing here adds tracking
  parameters to a destination;
- the status is a redirect (301, 302, 307 or 308), never a rewrite;
- `/go/app-store` exists in both phases. Before launch (`AVAILABILITY` in build_pages.py is
  PreOrder, as check_invariants.py reads it) nothing may send a visitor to the listing, so no
  destination is on apps.apple.com. After launch `/go/app-store` goes to the listing.

`--self-test` plants one break of each kind in a copy of public/ and fails unless the rule for
that break reports it (any other rule firing doesn't count, or a broken rule could hide behind a
neighbour); it also checks that an unbroken file passes in each phase first, so a check that can't
pass can't pass as catching everything. `--phase` overrides the phase read from build_pages.py; the self-test uses it
to plant a launched-phase break on a pre-launch build.
"""
import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_PAGES = ROOT / "scripts" / "build_pages.py"

REDIRECTS_FILE = "_redirects"
GO_APP_STORE = "/go/app-store"
STATUSES = {301, 302, 307, 308}
LISTING_HOST = "apps.apple.com"
# Same form as check_links.py: country-less, no slug, no query.
LISTING_FORM = re.compile(r"^https://apps\.apple\.com/app/id\d+$")
ALLOWED_HOSTS = {LISTING_HOST}


def phase_from_build():
    source = BUILD_PAGES.read_text()
    match = re.search(r'^AVAILABILITY = "([^"]+)"', source, re.MULTILINE)
    if not match:
        sys.exit("check_redirects: no AVAILABILITY in scripts/build_pages.py")
    value = match.group(1)
    if value.endswith("/InStock"):
        return "launched"
    if value.endswith("/PreOrder"):
        return "pre-launch"
    sys.exit(f"check_redirects: AVAILABILITY is {value!r}, which is neither PreOrder nor InStock")


def serves(root: Path, path: str) -> bool:
    """True if a same-site path (query and fragment stripped) is answered by a file."""
    plain = re.split(r"[?#]", path, maxsplit=1)[0]
    file = root / plain.lstrip("/")
    if plain.endswith("/"):
        file = file / "index.html"
    return file.is_file()


def check(root: Path, where: str) -> list:
    problems = []
    file = root / REDIRECTS_FILE
    if not file.is_file():
        return [f"no {REDIRECTS_FILE} under {root}"]
    seen = {}
    for number, raw in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) not in (2, 3):
            problems.append(f"line {number}: {raw!r} isn't `source destination [status]`")
            continue
        source, destination = fields[0], fields[1]
        status = fields[2] if len(fields) == 3 else "302"
        if not source.startswith("/") or source.startswith("//") or re.search(r"[*:?#]", source):
            problems.append(f"line {number}: source {source!r} isn't a plain same-site path")
        elif serves(root, source):
            problems.append(f"line {number}: source {source} is a file the site serves; a redirect would shadow it")
        if source in seen:
            problems.append(f"line {number}: source {source} already redirected on line {seen[source]}")
        seen.setdefault(source, number)
        if not status.isdigit() or int(status) not in STATUSES:
            problems.append(f"line {number}: status {status!r} isn't a redirect (301, 302, 307 or 308)")
        if destination.startswith("/") and not destination.startswith("//"):
            if not serves(root, destination):
                problems.append(f"line {number}: destination {destination} is no page of this site")
        else:
            host = re.match(r"^https://([^/?#]+)", destination)
            if not host or host.group(1) not in ALLOWED_HOSTS:
                problems.append(f"line {number}: destination {destination} is off the allow-list ({', '.join(sorted(ALLOWED_HOSTS))})")
            elif re.search(r"[?#]", destination):
                problems.append(f"line {number}: destination {destination} carries a query or fragment; no tracking parameters")
            elif host.group(1) == LISTING_HOST and not LISTING_FORM.match(destination):
                problems.append(f"line {number}: destination {destination} isn't the listing form https://apps.apple.com/app/id<digits>")
            if where == "pre-launch" and host and host.group(1) == LISTING_HOST:
                problems.append(f"line {number}: {source} sends visitors to {LISTING_HOST} before launch")
        if source == GO_APP_STORE and where == "launched" and not LISTING_FORM.match(destination):
            problems.append(f"line {number}: after launch {GO_APP_STORE} must go to the listing, not {destination}")
    if GO_APP_STORE not in seen:
        problems.append(f"{GO_APP_STORE} isn't redirected; it's the link the site publishes for the listing")
    return problems


LISTING = "https://apps.apple.com/app/id6812925073"

# (what is planted, the phase it's checked in, the whole _redirects body, the words the rule for
# it prints). The self-test looks for those words, not just for any problem: a plant that two
# rules catch would otherwise keep passing after one of them broke.
PLANTS = [
    ("an open redirect to another host", "pre-launch", f"{GO_APP_STORE} https://example.com/ 302\n", "off the allow-list"),
    ("a tracking parameter on the destination", "launched", f"{GO_APP_STORE} {LISTING}?pt=1&ct=website 302\n", "no tracking parameters"),
    ("the listing as a destination before launch", "pre-launch", f"{GO_APP_STORE} {LISTING} 302\n", "before launch"),
    ("a same-site destination that doesn't exist", "pre-launch", f"{GO_APP_STORE} /nowhere/ 302\n", "no page of this site"),
    ("a rewrite status instead of a redirect", "pre-launch", f"{GO_APP_STORE} / 404\n", "isn't a redirect"),
    ("the home page as the destination after launch", "launched", f"{GO_APP_STORE} / 302\n", "must go to the listing"),
    ("a redirect that shadows a page", "pre-launch", f"{GO_APP_STORE} / 302\n/privacy/ / 302\n", "would shadow it"),
    ("a line Cloudflare would ignore", "pre-launch", f"{GO_APP_STORE} / 302\n/go/cli\n", "isn't `source destination [status]`"),
    ("no /go/app-store at all", "pre-launch", "/go/cli / 302\n", "isn't redirected"),
]

# What has to pass, per phase, or the plants above prove nothing.
FIXTURES = [
    ("pre-launch", f"{GO_APP_STORE} / 302\n"),
    ("launched", f"{GO_APP_STORE} {LISTING} 302\n"),
]


def self_test(root: Path) -> int:
    failures = 0
    with tempfile.TemporaryDirectory() as scratch:
        copy = Path(scratch) / "site"
        shutil.copytree(root, copy)
        target = copy / REDIRECTS_FILE
        for where, body in FIXTURES:
            target.write_text(body)
            problems = check(copy, where)
            if problems:
                failures += 1
                print(f"self-test: the {where} fixture doesn't pass: {problems}")
        for what, where, body, words in PLANTS:
            target.write_text(body)
            problems = check(copy, where)
            if not any(words in problem for problem in problems):
                failures += 1
                print(f"self-test: planted {what} ({where}); wanted {words!r}, got {problems}")
    print(f"self-test: {len(FIXTURES)} fixtures, {len(PLANTS)} plants, {failures} failures")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT / "public"))
    parser.add_argument("--phase", choices=["pre-launch", "launched"])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    where = args.phase or phase_from_build()
    problems = check(root, where)
    for problem in problems:
        print(f"check_redirects: {problem}")
    print(f"{REDIRECTS_FILE} checked in the {where} phase: {len(problems)} problems")
    rc = 1 if problems else 0
    if args.self_test:
        rc = self_test(root) or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
