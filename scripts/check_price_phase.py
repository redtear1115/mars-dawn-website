#!/usr/bin/env python3
"""The built site states the unlock price of the current phase in scripts/price.py, and only that.

In the regular phase no page may say the sale price; in the sale phase no page may still say the
regular one (app #103). Both forms the copy uses count (`USD 4.99`, `4,99 USD`), in every page,
Markdown twin and llms file under public/. The sale line (`<p class="sale-line" data-sale-line>`)
is skipped: it names the regular price on purpose ("back to USD 4.99 on 1 December"). Outside
the sale phase there must be no sale line at all.

The Markdown twins and the llms and product-facts files carry the line as a line ending in
`<!-- sale-line -->` (price.sale_note_md()), skipped the same way. In the sale phase every .md or
.txt file that states the sale price must carry one, so no agent quotes 2.49 with no end date.

It also fails if a private-use KEEP sentinel from price.py reached a built file, which would mean
some text was written without going through price.localize().

--self-test runs price.localize() and this check's own rules against plants, and expects each
plant to fail with its own rule's message.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import price  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "public"
SUFFIXES = {".html", ".md", ".txt"}
RULE_OTHER = "states the other phase's price"
RULE_SENTINEL = "has a KEEP sentinel"
RULE_LINE = "has a sale line outside the sale phase"
RULE_NOTE = "states the sale price with no sale line"
TEXT_SUFFIXES = {".md", ".txt"}


def problems_in(where: str, text: str, phase: str, text_file: bool = False) -> list:
    """This check's rules, applied to one file's text (`text_file`: a .md or .txt file)."""
    found = []
    if price.KEEP_OPEN in text or price.KEEP_CLOSE in text:
        found.append(f"{where}: {RULE_SENTINEL} (written without price.localize())")
    if phase != "sale" and (price.SALE_LINE_RE.search(text) or price.SALE_NOTE_MARK in text):
        found.append(f"{where}: {RULE_LINE}")
    outside = price.SALE_NOTE_RE.sub("", price.SALE_LINE_RE.sub("", text))
    if (phase == "sale" and text_file and price.SALE_NOTE_MARK not in text
            and price.pattern(price.SALE).search(outside)):
        found.append(f"{where}: {RULE_NOTE}")
    wrong = price.REGULAR if phase == "sale" else price.SALE
    for m in price.pattern(wrong).finditer(outside):
        line = outside.count("\n", 0, m.start()) + 1
        found.append(f"{where}:{line}: {RULE_OTHER} {m.group(0)!r} in the {phase} phase")
    return found


def main() -> int:
    problems = []
    checked = 0
    for path in sorted(SITE.rglob("*")):
        if path.suffix not in SUFFIXES or not path.is_file():
            continue
        checked += 1
        problems += problems_in(str(path.relative_to(SITE)), path.read_text(encoding="utf-8"), price.PHASE,
                                path.suffix in TEXT_SUFFIXES)
    for problem in problems:
        print(f"check_price_phase: {problem}")
    print(f"{checked} files checked in the {price.PHASE} phase (unlock USD {price.current()}): {len(problems)} problems")
    return 1 if problems else 0


def self_test() -> int:
    line = {"en": "Half price through 30 November, then back to USD 4.99."}
    keep = price.sale_line_html("en", "sale", line)
    sale_page = price.localize(f"<p>unlock it once for USD 4.99.</p>\n{keep}<p>Typora: USD 14.99</p>", "sale")
    failed = 0

    def expect(name, ok, detail=""):
        nonlocal failed
        print(f"check_price_phase self-test: {'ok' if ok else 'FAIL'}: {name}{': ' + detail if detail else ''}")
        failed += not ok

    # price.localize()
    expect("regular phase leaves text alone", price.localize("USD 4.99 · 4,99 USD", "regular") == "USD 4.99 · 4,99 USD")
    expect("sale phase moves USD 4.99", price.localize("for USD 4.99.", "sale") == "for USD 2.49.")
    expect("sale phase moves 4,99 USD and keeps a no-break space",
           price.localize("pour 4,99 USD.", "sale") == "pour 2,49 USD.")
    expect("other products' prices are untouched",
           price.localize("USD 14.99, 14,99 USD, USD 4.995", "sale") == "USD 14.99, 14,99 USD, USD 4.995")
    expect("the sale line keeps the regular price", "back to USD 4.99." in sale_page, sale_page)
    expect("the sentinels are stripped", price.KEEP_OPEN not in sale_page and price.KEEP_CLOSE not in sale_page)
    expect("the sale line is only rendered in the sale phase", price.sale_line_html("en", "regular", line) == "")
    try:
        price.sale_line_html("ja", "sale", line)
        expect("a sale-phase build refuses a locale with no sale line", False)
    except AssertionError as exc:
        expect("a sale-phase build refuses a locale with no sale line", "no 'ja' line" in str(exc), str(exc))

    # price.sale_note_md()
    def note(text, phase="sale", locale="en"):
        return price.localize(price.sale_note_md(text, locale, phase, line), phase)

    twin = "Eyebrow\n\n# Pay once\n\nUnlock it once for USD 4.99.\n"
    llms = "# MarsDawn\n\n> Free to try, USD 4.99 once.\n\n## Docs\n- x: USD 4.99 once.\n"
    tagged = f"{line['en']} {price.SALE_NOTE_MARK}"
    expect("a twin gets the sale line after its H1",
           note(twin) == f"Eyebrow\n\n# Pay once\n\n{tagged}\n\nUnlock it once for USD 2.49.\n", repr(note(twin)))
    expect("llms.txt gets it after the H1's summary",
           note(llms) == f"# MarsDawn\n\n> Free to try, USD 2.49 once.\n\n{tagged}\n\n## Docs\n- x: USD 2.49 once.\n",
           repr(note(llms)))
    expect("a text with no H1 gets it at the top",
           note("for USD 4.99.\n") == f"{tagged}\n\nfor USD 2.49.\n", repr(note("for USD 4.99.\n")))
    expect("a text with no price gets none", note(twin.replace("USD 4.99", "once")) == twin.replace("USD 4.99", "once"))
    expect("the regular phase adds none", note(twin, "regular") == twin)
    try:
        note(twin, "sale", "ja")
        expect("a sale-phase twin refuses a locale with no sale line", False)
    except AssertionError as exc:
        expect("a sale-phase twin refuses a locale with no sale line", "no 'ja' line" in str(exc), str(exc))

    # This check's rules: each plant must fail with its own rule, and the good pages must pass.
    def red(name, text, phase, rule, text_file=False):
        found = problems_in("plant", text, phase, text_file)
        expect(name, any(rule in p for p in found) and all(rule in p for p in found), str(found))

    def green(name, text, phase, text_file=False):
        found = problems_in("plant", text, phase, text_file)
        expect(name, not found, str(found))

    green("a localized sale page passes, sale line and all", sale_page, "sale")
    green("a regular page passes", "<p>unlock it once for USD 4.99.</p>", "regular")
    red("sale phase, regular price outside the sale line", sale_page + "<p>for USD 4.99.</p>", "sale", RULE_OTHER)
    red("sale phase, 4,99 USD left in a de/fr/es page", "<p>für 4,99 USD frei.</p>", "sale", RULE_OTHER)
    red("regular phase, sale price left behind", "<p>for USD 2.49.</p>", "regular", RULE_OTHER)
    red("regular phase, 2,49 USD left in a de/fr/es page", "<p>und 2,49 USD</p>", "regular", RULE_OTHER)
    red("regular phase, a sale line left behind", '<p class="sale-line" data-sale-line>x</p>', "regular", RULE_LINE)
    red("a KEEP sentinel that reached the output", f"<p>{price.KEEP_OPEN}x{price.KEEP_CLOSE}</p>", "regular", RULE_SENTINEL)
    green("a sale-phase twin with its sale line passes", note(twin), "sale", True)
    green("sale-phase llms.txt with its sale line passes", note(llms), "sale", True)
    red("sale phase, a twin stating the sale price with no sale line",
        price.localize(twin, "sale"), "sale", RULE_NOTE, True)
    red("sale phase, the regular price outside a twin's sale line",
        note(twin) + "Still USD 4.99.\n", "sale", RULE_OTHER, True)
    red("regular phase, a twin's sale line left behind",
        f"# Pay once\n\nback soon {price.SALE_NOTE_MARK}\n\nUSD 4.99\n", "regular", RULE_LINE, True)
    green("an HTML page may state the sale price with no sale line", "<p>for USD 2.49.</p>", "sale")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else main())
