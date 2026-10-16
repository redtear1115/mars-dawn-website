"""Pages made from structured copy, the same renderer for every locale (website #227 and its follow-ups).

The copy is data: en and zh-Hant come from approved_copy.py (loaded from the owner-approved vault
drafts, never retyped); the other six locales' machine drafts (needs-i18n) are dicts of the same shape
in each copy_<l>.py. This module only turns strings into HTML:

  md_inline(text)      the Markdown the drafts use, inline: `code`, **bold**, [text](url), a few kept
                       <a href="/..."> tags, and the table sources "[S1, S9]" (links to the list
                       under the tables, #s1 ...)
  md_blocks(text)      paragraphs, "- " bullet lists and "1. " numbered lists
  open_md_page(copy)   /view-markdown-on-mac/
  mermaid_page(copy)   /mermaid-preview-mac/

A link's address is written in the copy with its locale's prefix already (/zh-hant/pdf/), so nothing
here rewrites an address. The Mac App Store link is the page's LISTING_URL (build_pages turns it into
the campaign form for HTML and keeps it plain in the Markdown twin).
"""
import re
from xml.sax.saxutils import escape

_NUMBER = re.compile(r"^\d+\. ")
_TOKEN = re.compile(
    r"`([^`]+)`"                                  # 1 code
    r"|\*\*(.+?)\*\*"                             # 2 bold
    r"|\[([^\]]+)\]\(([^)\s]+)\)"                 # 3, 4 link
    r"|\[(S\d+(?:, S\d+)*)\]"                     # 5 table sources
    r'|(<a href="/[^"]*">)|(</a>)'                # 6, 7 an <a> the copy carries itself
)


def md_inline(text: str) -> str:
    out = []
    pos = 0
    for m in _TOKEN.finditer(text):
        out.append(escape(text[pos:m.start()]))
        code, bold, label, url, sources, a_open, a_close = m.groups()
        if code is not None:
            out.append(f"<code>{escape(code)}</code>")
        elif bold is not None:
            out.append(f"<strong>{md_inline(bold)}</strong>")
        elif label is not None:
            out.append(f'<a href="{escape(url, {chr(34): "&quot;"})}">{md_inline(label)}</a>')
        elif sources is not None:
            refs = ", ".join(f'<a href="#{s.lower()}">{s}</a>' for s in sources.split(", "))
            out.append(f"[{refs}]")
        else:
            out.append(a_open or a_close)
        pos = m.end()
    out.append(escape(text[pos:]))
    return "".join(out)


def md_blocks(text: str, listing_url: str = "") -> str:
    """HTML for paragraphs and lists. {App Store 連結} in the drafts stands for the listing."""
    text = text.replace("{App Store 連結}", listing_url)
    parts = []
    for chunk in re.split(r"\n\s*\n", text.strip()):
        lines = chunk.split("\n")
        if all(line.startswith("- ") for line in lines):
            items = "\n".join(f"  <li>{md_inline(line[2:])}</li>" for line in lines)
            parts.append(f"<ul>\n{items}\n</ul>")
        elif all(re.match(r"\d+\. ", line) for line in lines):
            items = "\n".join("  <li>%s</li>" % md_inline(_NUMBER.sub("", line)) for line in lines)
            parts.append(f"<ol>\n{items}\n</ol>")
        else:
            parts.append(f"<p>{md_inline(' '.join(lines))}</p>")
    return "\n".join(parts)


def attr(text: str) -> str:
    """Text for a title, a meta description or an og: attribute (the page's own quoting)."""
    return escape(text, {'"': "&quot;"})


def _faq(items) -> str:
    return "\n".join(f"<h3>{escape(question)}</h3>\n<p>{md_inline(answer)}</p>" for question, answer in items)


def open_md_page(copy: dict, listing_url: str, brew: str) -> dict:
    """/view-markdown-on-mac/. The sections that were on the page before the 2026-10-15 revision
    (the opening paragraph, "Read it in MarsDawn", the agent paragraph, the PDF section and the Next
    list) are the *_html entries, kept as they were; the rest is the approved copy."""
    mermaid_item = copy["read_mermaid"][2:]
    body = f"""
<section class="intro">
  <h1>{escape(copy["h1"])}</h1>
  <p>{md_inline(copy["short"])}</p>
</section>
<p>{copy["opening_html"]}</p>
<h2>{escape(copy["steps_h2"])}</h2>
{md_blocks(copy["steps"])}
<h2>{copy["read_h2"]}</h2>
<p>{copy["read_p1_html"]}</p>
<p><a href="{listing_url}">{copy["download"]}</a></p>
<p>{copy["read_p2_html"]}</p>
<ul>
  <li>{copy["read_b1_html"]}</li>
  <li>{md_inline(mermaid_item)}</li>
  <li>{copy["read_b4_html"]}</li>
</ul>
<p>{copy["agents_html"]}</p>
<h2>{copy["pdf_h2"]}</h2>
<p>{copy["pdf_p1_html"]}</p>
<pre><code>{brew}
marsdawn export notes.md
open notes.pdf</code></pre>
<p>{copy["pdf_p2_html"]}</p>
<h2>{escape(copy["faq_h2"])}</h2>
{_faq(copy["faq"])}
<h2>{copy["next_h2"]}</h2>
<ul>
{chr(10).join(f"  <li>{item}</li>" for item in copy["next_items_html"])}
  <li>{md_inline(copy["next_new"][2:])}</li>
</ul>
"""
    return {"title": attr(copy["title"]), "description": attr(copy["description"]), "body": body}


SPLIT_SHOT_MARK = "<!--shot:split-->"


def mermaid_page(copy: dict, listing_url: str) -> dict:
    """/mermaid-preview-mac/: the diagram as text, where it is drawn, when it has a mistake, what
    to know. SPLIT_SHOT_MARK becomes the split-view screenshot (build_pages.split_shot_html)."""
    body = f"""
<section class="intro">
  <h1>{escape(copy["h1"])}</h1>
  <p>{md_inline(copy["intro"])}</p>
</section>
<h2>{escape(copy["example_h2"])}</h2>
{md_blocks(copy["example"])}
<pre><code>{escape(copy["code"])}</code></pre>
{md_blocks(copy["after"])}
{SPLIT_SHOT_MARK}
<h2>{escape(copy["where_h2"])}</h2>
{md_blocks(copy["where"])}
<h2>{escape(copy["error_h2"])}</h2>
{md_blocks(copy["error"])}
<h2>{escape(copy["know_h2"])}</h2>
{md_blocks(copy["know"])}
<h2>{escape(copy["next_h2"])}</h2>
{md_blocks(copy["next"])}
<h2>{escape(copy["try_h2"])}</h2>
{md_blocks(copy["try"], listing_url)}
"""
    return {"title": attr(copy["title"]), "description": attr(copy["description"]), "body": body}


# --- /vs/macmd-viewer/ (the 2026-10-15 revision) ---------------------------------------------
VS_KEYS = ("macmd-features", "macmd-buying", "macmd-after")


def vs_compare(copy: dict) -> dict:
    """The page's three comparison tables, in the shape of build_pages.COMPARE_TABLES for one locale:
    the cells are HTML, and a [S#] source mark in a cell links to the list under the tables."""
    return {key: {"head": table["head"], "rows": [[md_inline(cell) for cell in row] for row in table["rows"]]}
            for key, table in zip(VS_KEYS, copy["tables"])}


def vs_macmd_page(copy: dict, brew: str) -> dict:
    """/vs/macmd-viewer/. The tables are marks (<!--compare:...-->) that all_pages() fills; the
    "Try it today" section and the "Next" list are the ones the page had before, kept as HTML."""
    parts = ['<section class="intro">', f'  <h1>{escape(copy["h1"])}</h1>']
    parts += [f"  <p>{md_inline(p)}</p>" for p in copy["intro"]] + ["</section>"]
    for key, table in zip(VS_KEYS, copy["tables"]):
        parts += [f'<h2>{escape(table["h2"])}</h2>', f"<!--compare:{key}-->"]
    sources = "\n".join(f'  <li id="{sid.lower()}">{sid} · <a href="{url}">{escape(url)}</a></li>' for sid, url in copy["sources"])
    parts += [f'<h2>{escape(copy["sources_h2"])}</h2>', f'<ul class="sources">\n{sources}\n</ul>',
              f'<h2>{escape(copy["pick_h2"])}</h2>'] + [f"<p>{md_inline(p)}</p>" for p in copy["pick"]]
    parts += [f'<h2>{escape(copy["faq_h2"])}</h2>', _faq(copy["faq"])]
    parts += [f'<h2>{copy["try_h2"]}</h2>', f'<p>{copy["try_p_html"]}</p>',
              f"<pre><code>{brew}\nmarsdawn export notes.md\nopen notes.pdf</code></pre>", f'<h2>{copy["next_h2"]}</h2>']
    items = [f"  <li>{item}</li>" for item in copy["next_items_html"]] + [f"  <li>{md_inline(copy['features_item'][2:])}</li>"]
    parts += ["<ul>", *items, "</ul>"]
    return {"title": attr(copy["title"]), "description": attr(copy["description"]), "body": "\n".join(parts) + "\n"}
