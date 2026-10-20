#!/usr/bin/env python3
"""The built site states the unlock price of the current phase in scripts/price.py, and only that.

In the regular phase no page may say the sale price; in the sale phase no page may still say the
regular one (app #103). Both forms the copy uses count (`USD 4.99`, `4,99 USD`), in every page,
Markdown twin and llms file under public/. The sale line (`<p class="sale-line" data-sale-line>`)
is skipped: it names the regular price on purpose ("back to USD 4.99 on 1 December"). Outside
the sale phase there must be no sale line at all.

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


def problems_in(where: str, text: str, phase: str) -> list:
    """This check's rules, applied to one file's text."""
    found = []
    if price.KEEP_OPEN in text or price.KEEP_CLOSE in text:
        found.append(f"{where}: {RULE_SENTINEL} (written without price.localize())")
    if phase != "sale" and price.SALE_LINE_RE.search(text):
        found.append(f"{where}: {RULE_LINE}")
    outside = price.SALE_LINE_RE.sub("", text)
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
        problems += problems_in(str(path.relative_to(SITE)), path.read_text(encoding="utf-8"), price.PHASE)
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

    # This check's rules: each plant must fail with its own rule, and the good pages must pass.
    def red(name, text, phase, rule):
        found = problems_in("plant", text, phase)
        expect(name, any(rule in p for p in found) and all(rule in p for p in found), str(found))

    def green(name, text, phase):
        found = problems_in("plant", text, phase)
        expect(name, not found, str(found))

    green("a localized sale page passes, sale line and all", sale_page, "sale")
    green("a regular page passes", "<p>unlock it once for USD 4.99.</p>", "regular")
    red("sale phase, regular price outside the sale line", sale_page + "<p>for USD 4.99.</p>", "sale", RULE_OTHER)
    red("sale phase, 4,99 USD left in a de/fr/es page", "<p>für 4,99 USD frei.</p>", "sale", RULE_OTHER)
    red("regular phase, sale price left behind", "<p>for USD 2.49.</p>", "regular", RULE_OTHER)
    red("regular phase, 2,49 USD left in a de/fr/es page", "<p>und 2,49 USD</p>", "regular", RULE_OTHER)
    red("regular phase, a sale line left behind", '<p class="sale-line" data-sale-line>x</p>', "regular", RULE_LINE)
    red("a KEEP sentinel that reached the output", f"<p>{price.KEEP_OPEN}x{price.KEEP_CLOSE}</p>", "regular", RULE_SENTINEL)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else main())
