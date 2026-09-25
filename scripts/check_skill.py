#!/usr/bin/env python3
"""Checks that the site's agent skill is the one the documented marsdawn release prints.

Usage:
    python3 scripts/check_skill.py [--file public/cli/skill/SKILL.md] [--tag 0.5.4]

The kit repository owns the text: `skill/SKILL.md` there is what `marsdawn skill` prints (its
tests hold the two to the same bytes). This fetches that file at KIT_TAG, the release the site
documents, and fails with a diff if the site's copy differs. A tag, not the kit's main, so the site
doesn't drift when main moves; bumping KIT_TAG is part of documenting a new release. No Swift build.

To see it catch a drift, check a copy with one word changed:

    cp public/cli/skill/SKILL.md /tmp/SKILL.md && sed -i '' 's/Open it/Open that/' /tmp/SKILL.md
    python3 scripts/check_skill.py --file /tmp/SKILL.md
"""
import argparse
import difflib
import sys
import urllib.request
from pathlib import Path

KIT_TAG = "0.5.4"
URL = "https://raw.githubusercontent.com/redtear1115/mars-dawn-kit/{tag}/skill/SKILL.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="public/cli/skill/SKILL.md")
    parser.add_argument("--tag", default=KIT_TAG)
    args = parser.parse_args()

    site = Path(args.file).read_bytes()
    url = URL.format(tag=args.tag)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            kit = response.read()
    except Exception as error:  # a missing tag is a failure, not a pass
        print(f"check_skill: can't fetch {url}: {error}", file=sys.stderr)
        return 1
    if site == kit:
        print(f"check_skill: {args.file} matches marsdawn {args.tag}'s skill/SKILL.md")
        return 0
    diff = difflib.unified_diff(
        kit.decode("utf-8", "replace").splitlines(keepends=True),
        site.decode("utf-8", "replace").splitlines(keepends=True),
        fromfile=f"kit {args.tag}: skill/SKILL.md", tofile=args.file,
    )
    sys.stderr.writelines(diff)
    print(f"check_skill: {args.file} differs from marsdawn {args.tag}'s skill/SKILL.md", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
