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

- datePublished: the commit date (`%cs`) of the first commit that added that file;
- dateModified:  the commit date of the last commit that changed it.

`build_pages.py` reads the json; it never computes a date and nothing in it is typed by hand.
CI's checkout has no history, so CI cannot rerun this: a page's dates are rewritten by running
`--write` on a full clone after a change reaches main, and the commit that does so is the record.
"""
import argparse
import json
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


def compute(ref):
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("article_dates: this clone is shallow; run it on a full clone")
    out = {"ref": ref, "ref_commit": git("rev-parse", ref).strip(), "pages": {}}
    for slug in ARTICLE_SLUGS:
        source = f"public/{slug}/index.html"
        log = git("log", "--first-parent", "--format=%cs %h", ref, "--", source).split("\n")
        log = [line for line in log if line]
        if not log:
            sys.exit(f"article_dates: {source} has no history on {ref}")
        (modified, modified_commit), (published, published_commit) = log[0].split(), log[-1].split()
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
        print(f"{slug:55} {page['published']} ({page['published_commit']})  {page['modified']} ({page['modified_commit']})")
    if args.write:
        DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {DATA.relative_to(ROOT)} from {args.ref} at {data['ref_commit'][:8]}")
    if args.check:
        if load() != data:
            print("article_dates: scripts/article_dates.json differs from git history (run --write)")
            return 1
        print("article_dates.json matches git history: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
