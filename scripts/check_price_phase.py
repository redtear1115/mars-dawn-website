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

In the regular phase the early-bird notice must match the approved copy on the home and pay-once
pages, their Markdown twins, and the llms and product-facts files. Outside the regular phase
those files must omit the approved sentences, and all built HTML, Markdown, and text files must
omit the notice markers. JSON-LD Offer prices must match the current price and free download.

It also fails if a private-use KEEP sentinel from price.py reached a built file, which would mean
some text was written without going through price.localize().

--self-test runs price.localize() and this check's own rules against plants, and expects each
plant to fail with its own rule's message.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import price  # noqa: E402
from check_offers import HOMES, SCRIPT, offers  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "public"
SUFFIXES = {".html", ".md", ".txt"}
RULE_OTHER = "states the other phase's price"
RULE_SENTINEL = "has a KEEP sentinel"
RULE_LINE = "has a sale line outside the sale phase"
RULE_NOTE = "states the sale price with no sale line"
RULE_EARLY = "has an early-bird notice outside the regular phase"
TEXT_SUFFIXES = {".md", ".txt"}


EXPECTED_EARLY_BIRD_LINES = {
    "en": "Early-bird price: the one-time unlock is USD 4.99 (no subscription) through 12 January 2027, then USD 9.99 from 13 January 2027.",
    "zh-hant": "早鳥價：一次解鎖為 USD 4.99（非訂閱），至 2027 年 1 月 12 日；2027 年 1 月 13 日起調整為 USD 9.99。",
    "zh-hans": "早鸟价：一次解锁为 USD 4.99（非订阅），至 2027 年 1 月 12 日；2027 年 1 月 13 日起调整为 USD 9.99。",
    "ja": "早期価格：一度きりのロック解除は USD 4.99（サブスクなし）、2027年1月12日まで。2027年1月13日から USD 9.99 になります。",
    "ko": "얼리버드 가격: 한 번만 구입하는 잠금 해제(구독 없음)는 2027년 1월 12일까지 USD 4.99이며, 2027년 1월 13일부터 USD 9.99로 조정됩니다.",
    "de": "Einführungspreis: Die einmalige Freischaltung kostet 4,99 USD (kein Abo) bis zum 12. Januar 2027, ab dem 13. Januar 2027 dann 9,99 USD.",
    "fr": "Tarif de lancement : le déverrouillage unique coûte 4,99 USD (sans abonnement) jusqu’au 12 janvier 2027, puis 9,99 USD à partir du 13 janvier 2027.",
    "es": "Precio de lanzamiento: el desbloqueo único cuesta 4,99 USD (sin suscripción) hasta el 12 de enero de 2027; 9,99 USD a partir del 13 de enero de 2027.",
}


def problems_in(where: str, text: str, phase: str, text_file: bool = False) -> list:
    """This check's rules, applied to one file's text (`text_file`: a .md or .txt file)."""
    found = []
    if price.KEEP_OPEN in text or price.KEEP_CLOSE in text:
        found.append(f"{where}: {RULE_SENTINEL} (written without price.localize())")
    if phase != "sale" and (price.SALE_LINE_RE.search(text) or price.SALE_NOTE_MARK in text):
        found.append(f"{where}: {RULE_LINE}")
    if phase != "regular" and (price.EARLY_BIRD_LINE_RE.search(text) or price.EARLY_BIRD_NOTE_MARK in text):
        found.append(f"{where}: {RULE_EARLY}")
    outside = price.SALE_NOTE_RE.sub("", price.SALE_LINE_RE.sub("", text))
    outside = price.EARLY_BIRD_NOTE_RE.sub("", price.EARLY_BIRD_LINE_RE.sub("", outside))
    if (phase == "sale" and text_file and price.SALE_NOTE_MARK not in text
            and price.pattern(price.SALE).search(outside)):
        found.append(f"{where}: {RULE_NOTE}")
    wrong = price.REGULAR if phase == "sale" else price.SALE
    for m in price.pattern(wrong).finditer(outside):
        line = outside.count("\n", 0, m.start()) + 1
        found.append(f"{where}:{line}: {RULE_OTHER} {m.group(0)!r} in the {phase} phase")
    return found


def early_bird_problems() -> list:
    problems = []
    if price.EARLY_BIRD_LINES != EXPECTED_EARLY_BIRD_LINES:
        problems.append("price.EARLY_BIRD_LINES differs from the approved early-bird copy")

    def built_text(path: Path) -> str:
        if not path.is_file():
            problems.append(f"{path.relative_to(SITE)}: missing built file")
            return ""
        text = path.read_text(encoding="utf-8")
        if price.PHASE != "regular" and any(line in text for line in EXPECTED_EARLY_BIRD_LINES.values()):
            problems.append(f"{path.relative_to(SITE)}: {RULE_EARLY} (approved copy)")
        return text

    def check_note(path: Path, sentence: str) -> None:
        notes = price.EARLY_BIRD_NOTE_RE.findall(built_text(path))
        if price.PHASE == "regular" and notes != [f"{sentence} {price.EARLY_BIRD_NOTE_MARK}"]:
            problems.append(f"{path.relative_to(SITE)}: expected one approved early-bird note")

    for locale, sentence in EXPECTED_EARLY_BIRD_LINES.items():
        root = SITE if locale == "en" else SITE / locale
        for folder in (root, root / "pay-once"):
            page = folder / "index.html"
            paragraphs = price.EARLY_BIRD_LINE_RE.findall(built_text(page))
            if price.PHASE == "regular" and paragraphs != [sentence]:
                problems.append(f"{page.relative_to(SITE)}: expected one approved early-bird paragraph")
            check_note(folder / "index.md", sentence)
    for name in ("llms.txt", "llms-full.txt", "product-facts.md"):
        check_note(SITE / name, EXPECTED_EARLY_BIRD_LINES["en"])
    if price.PHASE != "regular":
        markers = ("data-early-bird", "early-bird-line", price.EARLY_BIRD_NOTE_MARK)
        for path in sorted(SITE.rglob("*")):
            if path.suffix in SUFFIXES and path.is_file():
                text = path.read_text(encoding="utf-8")
                if any(marker in text for marker in markers):
                    problems.append(f"{path.relative_to(SITE)}: {RULE_EARLY} (notice marker)")
    return problems


def offer_price_problems(where: str, text: str) -> list:
    problems = []
    current = price.current()
    prices = []
    for block in SCRIPT.findall(text):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            problems.append(f"{where}: JSON-LD doesn't parse: {exc}")
            continue
        for offer in offers(data):
            amount = str(offer.get("price"))
            prices.append(amount)
            expected = "0" if offer.get("name") == "Free download with a 14-day trial" else current
            if amount == "9.99" or amount != expected:
                problems.append(f"{where}: Offer price {amount!r}, expected {expected!r}")
    if where in HOMES and sorted(prices) != ["0", current]:
        problems.append(f"{where}: expected Offer prices '0' and {current!r}")
    return problems


def main() -> int:
    problems = early_bird_problems()
    checked = 0
    for path in sorted(SITE.rglob("*")):
        if path.suffix not in SUFFIXES or not path.is_file():
            continue
        checked += 1
        where = str(path.relative_to(SITE))
        text = path.read_text(encoding="utf-8")
        problems += problems_in(where, text, price.PHASE, path.suffix in TEXT_SUFFIXES)
        if path.suffix == ".html":
            problems += offer_price_problems(where, text)
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
    if price.PHASE == "sale":
        expect("the default sale phase omits the early-bird paragraph", price.early_bird_html("en") == "")
        expect("the default sale phase omits the early-bird note", price.early_bird_note_md() == "")
    early_bird = price.early_bird_html("en", "regular")
    approved = EXPECTED_EARLY_BIRD_LINES["en"]
    expect("the early-bird paragraph contains the approved copy and price",
           approved in early_bird and "USD 4.99" in early_bird)
    regular_early_bird = price.localize(early_bird, "regular")
    expect("regular localization keeps the approved early-bird copy", approved in regular_early_bird)
    expect("sale localization keeps the approved early-bird copy", approved in price.localize(early_bird, "sale"))
    green("regular phase, early-bird paragraph", regular_early_bird, "regular")
    red("sale phase, early-bird paragraph", regular_early_bird, "sale", RULE_EARLY)
    red("sale phase, early-bird note",
        price.localize(price.early_bird_note_md(phase="regular"), "regular"), "sale", RULE_EARLY, text_file=True)
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
