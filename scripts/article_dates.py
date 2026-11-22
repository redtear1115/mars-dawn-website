#!/usr/bin/env python3
"""The dates in the essays' and reading notes' TechArticle JSON-LD, computed from git history.

Usage:
    python3 scripts/article_dates.py            print the table, change nothing
    python3 scripts/article_dates.py --write    write scripts/article_dates.json (commit it)
    python3 scripts/article_dates.py --check    fail unless the json matches what history says
    --ref REF   the branch to read (default origin/main; fetch first)

One rule for every page. The page's English source is its generated file `public/<slug>/index.html`
(a page has no other English file of its own; the Markdown twin is generated from it). On REF's
first-parent history, so a date is when the change reached main:

- datePublished: the commit date (`%cs`) and full 40-char `%H` of the first commit that added that file;
- dateModified:  the commit date and full 40-char `%H` of the last commit where the article's own content
  changed (specifically `<title>...</title>`, `<meta name="description" content="...">`, and
  `<main id="main">...</main>`), ignoring `<script type="application/ld+json">` and site-wide chrome
  (masthead/nav/hreflang/footer/consent-banner).

`build_pages.py` reads the json; it never computes a date and nothing in it is typed by hand.
CI's checkout has no history, so CI cannot rerun this: a page's dates are rewritten by running
`--write` on a full clone after a change reaches main, and the commit that does so is the record.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "scripts" / "article_dates.json"

# The essays and reading notes that carry a TechArticle.
ARTICLE_SLUGS = [
    "token-efficient-review", "sharing-exported-pdfs", "reviewing-ai-output",
    "reading-agent-output", "agent-transparency", "reviewing-agent-plans", "agent-design-patterns",
    "reading-notes",
    "reading-notes/anthropic-building-effective-agents", "reading-notes/chip-huyen-agents",
    "reading-notes/lilian-weng-llm-agents", "reading-notes/harrison-chase-what-is-an-agent",
    "reading-notes/langchain-what-is-an-agent", "reading-notes/andrew-ng-design-patterns",
]


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def extract_article_content(html):
    """Extract the article's own content (title, description, main) for comparison."""
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = title_match.group(1).strip() if title_match else ""

    desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""

    main_match = re.search(r'<main id="main">(.*?)</main>', html, re.DOTALL)
    main = main_match.group(1).strip() if main_match else ""

    return (title, description, main)


def compute(ref):
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("article_dates: this clone is shallow; run it on a full clone")
    out = {"ref": ref, "ref_commit": git("rev-parse", ref).strip(), "pages": {}}
    for slug in ARTICLE_SLUGS:
        source = f"public/{slug}/index.html"
        # Walk git log --first-parent from oldest to newest, reading git show {sha}:{source}
        # and extracting the article's own content to detect real content changes
        log_lines = git("log", "--first-parent", "--format=%H %cs", ref, "--", source).strip().split("\n")
        log_lines = [line for line in log_lines if line]
        if not log_lines:
            sys.exit(f"article_dates: {slug} has no history in {source} on {ref}")

        # Reverse to walk oldest to newest
        log_lines.reverse()

        published_commit = None
        published = None
        modified_commit = None
        modified = None
        prev_content = None

        for line in log_lines:
            parts = line.split()
            commit_hash = parts[0]
            commit_date = parts[1]

            # Read the file at this commit
            try:
                html = git("show", f"{commit_hash}:{source}")
            except subprocess.CalledProcessError:
                # File doesn't exist at this commit (shouldn't happen given we're walking its history)
                continue

            # Extract article content
            content = extract_article_content(html)

            # First commit is published
            if published_commit is None:
                published_commit = commit_hash
                published = commit_date
                modified_commit = commit_hash
                modified = commit_date
                prev_content = content
            else:
                # Check if content changed
                if content != prev_content:
                    modified_commit = commit_hash
                    modified = commit_date
                    prev_content = content

        if published_commit is None:
            sys.exit(f"article_dates: {slug} has no commits in {source} on {ref}")

        out["pages"][slug] = {"source": source, "published": published, "published_commit": published_commit,
                              "modified": modified, "modified_commit": modified_commit}
    return out


def load():
    return json.loads(DATA.read_text())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="origin/main")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = compute(args.ref)
    for slug, page in data["pages"].items():
        print(f"{slug:55} {page['published']} ({page['published_commit'][:8]})  {page['modified']} ({page['modified_commit'][:8]})")
    if args.write:
        DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {DATA.relative_to(ROOT)} from {args.ref} at {data['ref_commit'][:8]}")
    if args.check:
        existing = load()
        if existing.get("pages") != data["pages"]:
            print("article_dates: scripts/article_dates.json differs from git history (run --write)")
            return 1
        print("article_dates.json matches git history: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
