#!/usr/bin/env python3
"""Pings IndexNow (used by Bing, Yandex and Seznam) with the URLs that
changed in this deploy, so they get crawled in hours instead of weeks.

Run after a successful `wrangler deploy`, from the `deploy` job in
.github/workflows/site.yml. A failed or skipped ping must never fail the
deploy: every path here either succeeds or prints a GitHub Actions warning
and exits 0.

Reads INDEXNOW_BEFORE_SHA and INDEXNOW_AFTER_SHA from the environment
(never interpolated into a shell command) rather than argv or a hardcoded
`${{ github.event.before }}` in `run:`, so an Actions step never has to
splice event data into a command line. No secret or token is used: the
IndexNow key is a public file already committed to the repo.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from indexnow_urls import changed_files, file_to_url, sitemap_urls  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
HOST = "marsdawn.southern-light.dev"
BASE_URL = f"https://{HOST}"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
ALL_ZEROS = "0" * 40
_HEX = set("0123456789abcdef")


def warn(message: str) -> None:
    print(f"::warning::{message}")


def find_key_file() -> Optional[Path]:
    candidates = sorted(
        p for p in PUBLIC.glob("*.txt")
        if len(p.stem) == 32 and set(p.stem) <= _HEX
    )
    return candidates[0] if candidates else None


def resolve_urls(before: str, after: str) -> list:
    if not before or before == ALL_ZEROS:
        warn("No previous commit for this push (first push or force-push); pinging the whole sitemap.")
        return sitemap_urls()
    try:
        files = changed_files(before, after)
    except Exception as exc:  # e.g. `before` isn't reachable in this checkout
        warn(f"Could not diff against {before}: {exc}. Pinging the whole sitemap instead.")
        return sitemap_urls()
    return sorted({u for f in files if (u := file_to_url(f))})


def main() -> int:
    before = os.environ.get("INDEXNOW_BEFORE_SHA", "")
    after = os.environ.get("INDEXNOW_AFTER_SHA", "")

    key_file = find_key_file()
    if key_file is None:
        warn("No IndexNow key file (public/<32-hex-chars>.txt) found; skipping the ping.")
        return 0

    urls = resolve_urls(before, after)
    if not urls:
        print("No served URLs changed; nothing to ping.")
        return 0

    key = key_file.stem
    body = json.dumps({
        "host": HOST,
        "key": key,
        "keyLocation": f"{BASE_URL}/{key_file.name}",
        "urlList": urls,
    }).encode("utf-8")
    request = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            print(f"IndexNow: HTTP {response.status} for {len(urls)} URL(s).")
    except urllib.error.HTTPError as exc:
        warn(f"IndexNow returned HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:500]}")
    except Exception as exc:  # network error, timeout, DNS, etc.
        warn(f"IndexNow ping failed: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
