"""The unlock price the site states, and the one switch that moves it to the sale price (app #103).

The app never hard-codes a price (it shows StoreKit's displayPrice); the site does, in every
locale's copy. Rather than edit approved and ingested copy twice for a seven-day sale, the copy
keeps saying the regular price and build_pages.py passes every page it writes through
`localize()`, which states the current phase's price instead.

PHASE is a committed constant, never read from the clock: public/ is committed and CI rebuilds it
and diffs it against the commit, so the build has to give the same output on any day. Switching
the site to the sale price is a PR that sets PHASE = "sale" (plus SALE_LINES and the regenerated
public/); switching back is a PR that sets it to "regular". Each goes live only with a deploy.

The two forms the copy writes the price in: `USD 4.99` (en, zh-Hant, zh-Hans, ja, ko) and
`4,99 USD` (de, fr, es), with a space or a no-break space between. Other products' prices
(USD 14.99, 19,99 USD) never match: the amount has to start and end at a digit boundary.

The sale line (SALE_LINES, one per locale, written by Grok and approved like any copy) names the
regular price on purpose ("back to USD 4.99 on 1 December"), so it is wrapped in KEEP sentinels
that `localize()` doesn't substitute inside and then strips. In the built page it is
`<p class="sale-line" data-sale-line>`, which check_price_phase.py skips for the same reason.

The Markdown twins, llms.txt, llms-full.txt and product-facts.md state the price too, and agents
quote them, so a sale price there carries the same line (`sale_note_md()`): one line after the
file's H1, ending in `<!-- sale-line -->`, which check_price_phase.py skips and, in the sale phase,
requires in every such file that states the sale price.
"""
import re

TRIAL_DAYS = 14
REGULAR = "4.99"
SALE = "2.49"
SALE_LAST_DAY = "2026-11-30"
PHASES = ("regular", "sale")
PHASE = "sale"

# One line per locale, shown only in the sale phase, on the home page and /pay-once/. Empty until
# the copy is approved; a sale-phase build with any locale missing fails (sale_line_html).
SALE_LINES: dict = {
    'en': 'Black Friday: the one-time unlock is half price, USD 2.49 instead of USD 4.99, through 30 November. It returns to USD 4.99 on 1 December.',
    'zh-hant': '黑色星期五特價：一次解鎖只要半價 USD 2.49（原價 USD 4.99），優惠到 11 月 30 日，12 月 1 日起恢復 USD 4.99。',
    'zh-hans': '黑色星期五特价：一次解锁只要半价 USD 2.49（原价 USD 4.99），优惠到 11 月 30 日，12 月 1 日起恢复 USD 4.99。',
    'ja': 'ブラックフライデーセール：一度きりのロック解除が半額の USD 2.49（通常 USD 4.99）。11月30日まで。12月1日から USD 4.99 に戻ります。',
    'de': 'Black-Friday-Angebot: Der einmalige Kauf zum Freischalten kostet bis 30. November die Hälfte, 2,49 USD statt 4,99 USD. Ab dem 1. Dezember kostet er wieder 4,99 USD.',
    'fr': 'Offre Black Friday : l’achat unique qui déverrouille l’app est à moitié prix, 2,49 USD au lieu de 4,99 USD, jusqu’au 30 novembre. Il repasse à 4,99 USD le 1er décembre.',
    'es': 'Oferta de Black Friday: la compra única que desbloquea la app está a mitad de precio, 2,49 USD en lugar de 4,99 USD, hasta el 30 de noviembre. Vuelve a 4,99 USD el 1 de diciembre.',
    'ko': '블랙 프라이데이 할인: 한 번만 구입하는 잠금 해제가 11월 30일까지 반값인 USD 2.49입니다(정가 USD 4.99). 12월 1일부터는 다시 USD 4.99입니다.',
}

EARLY_BIRD_LINES = {
    "en": "Early-bird price: the one-time unlock is USD 4.99 (no subscription) through 12 January 2027, then USD 9.99 from 13 January 2027.",
    "zh-hant": "早鳥價：一次解鎖為 USD 4.99（非訂閱），至 2027 年 1 月 12 日；2027 年 1 月 13 日起調整為 USD 9.99。",
    "zh-hans": "早鸟价：一次解锁为 USD 4.99（非订阅），至 2027 年 1 月 12 日；2027 年 1 月 13 日起调整为 USD 9.99。",
    "ja": "早期価格：一度きりのロック解除は USD 4.99（サブスクなし）、2027年1月12日まで。2027年1月13日から USD 9.99 になります。",
    "ko": "얼리버드 가격: 한 번만 구입하는 잠금 해제(구독 없음)는 2027년 1월 12일까지 USD 4.99이며, 2027년 1월 13일부터 USD 9.99로 조정됩니다.",
    "de": "Einführungspreis: Die einmalige Freischaltung kostet 4,99 USD (kein Abo) bis zum 12. Januar 2027, ab dem 13. Januar 2027 dann 9,99 USD.",
    "fr": "Tarif de lancement : le déverrouillage unique coûte 4,99 USD (sans abonnement) jusqu’au 12 janvier 2027, puis 9,99 USD à partir du 13 janvier 2027.",
    "es": "Precio de lanzamiento: el desbloqueo único cuesta 4,99 USD (sin suscripción) hasta el 12 de enero de 2027; 9,99 USD a partir del 13 de enero de 2027.",
}

# Private-use code points: never in copy, so they can't collide with real text.
KEEP_OPEN = ""
KEEP_CLOSE = ""
SALE_LINE_RE = re.compile(r'<p class="sale-line" data-sale-line>.*?</p>', re.DOTALL)
SALE_NOTE_MARK = "<!-- sale-line -->"
SALE_NOTE_RE = re.compile(r"^.*<!-- sale-line -->$", re.MULTILINE)

EARLY_BIRD_LINE_RE = re.compile(r'<p class="early-bird-line" data-early-bird>(.*?)</p>', re.DOTALL)
EARLY_BIRD_NOTE_MARK = "<!-- early-bird -->"
EARLY_BIRD_NOTE_RE = re.compile(r"^.*<!-- early-bird -->$", re.MULTILINE)

assert PHASE in PHASES, f"price.PHASE is {PHASE!r}, want one of {PHASES}"


def current() -> str:
    """The unlock price in the current phase, as JSON-LD writes it ("4.99")."""
    return SALE if PHASE == "sale" else REGULAR


def other() -> str:
    """The price the built site must not state anywhere in the current phase."""
    return REGULAR if PHASE == "sale" else SALE


def pattern(amount: str) -> re.Pattern:
    """`USD 4.99` or `4,99 USD` (space or no-break space), and not part of a longer number."""
    whole, cents = amount.split(".")
    return re.compile(
        rf"(?<![\d.,])(?:(USD[  ]){whole}\.{cents}|{whole},{cents}([  ]USD))(?![\d])")


def _substitute(text: str, old: str, new: str) -> str:
    new_whole, new_cents = new.split(".")

    def repl(m: re.Match) -> str:
        if m.group(1) is not None:
            return f"{m.group(1)}{new_whole}.{new_cents}"
        return f"{new_whole},{new_cents}{m.group(2)}"

    return pattern(old).sub(repl, text)


def localize(text: str, phase: str = None) -> str:
    """`text` with the regular price replaced by `phase`'s (default PHASE), outside KEEP spans."""
    phase = PHASE if phase is None else phase
    assert phase in PHASES, phase
    if phase == "regular" and KEEP_OPEN not in text:
        return text
    out = []
    for i, part in enumerate(re.split(f"[{KEEP_OPEN}{KEEP_CLOSE}]", text)):
        # Even parts are outside a KEEP span, odd parts inside one.
        out.append(_substitute(part, REGULAR, SALE) if phase == "sale" and i % 2 == 0 else part)
    return "".join(out)


def sale_line_html(locale: str, phase: str = None, lines: dict = None) -> str:
    """The sale line for `locale`'s page, or "" outside the sale phase."""
    phase = PHASE if phase is None else phase
    lines = SALE_LINES if lines is None else lines
    if phase != "sale":
        return ""
    assert locale in lines, f"price.PHASE is 'sale' but SALE_LINES has no {locale!r} line"
    return f'{KEEP_OPEN}<p class="sale-line" data-sale-line>{lines[locale]}</p>{KEEP_CLOSE}\n'


def early_bird_html(locale: str) -> str:
    """The early-bird notice for this locale, protected from phase localization."""
    assert locale in EARLY_BIRD_LINES, f"EARLY_BIRD_LINES has no {locale!r} line"
    return f'{KEEP_OPEN}<p class="early-bird-line" data-early-bird>{EARLY_BIRD_LINES[locale]}</p>{KEEP_CLOSE}\n'


def early_bird_note_md(locale: str = "en") -> str:
    """The Markdown notice line, protected from phase localization."""
    assert locale in EARLY_BIRD_LINES, f"EARLY_BIRD_LINES has no {locale!r} line"
    return f"{KEEP_OPEN}{EARLY_BIRD_LINES[locale]} {EARLY_BIRD_NOTE_MARK}{KEEP_CLOSE}\n"


def sale_note_md(text: str, locale: str = "en", phase: str = None, lines: dict = None) -> str:
    """Markdown or plain `text` with `locale`'s sale line after its H1, in the sale phase.

    Only a text that states the price gets one. It goes after the first `# ` heading, and after
    the `>` summary that follows it if there is one (llms.txt's form); with no H1, at the top.
    """
    phase = PHASE if phase is None else phase
    lines = SALE_LINES if lines is None else lines
    if phase != "sale" or not pattern(REGULAR).search(text):
        return text
    assert locale in lines, f"price.PHASE is 'sale' but SALE_LINES has no {locale!r} line"
    note = f"{KEEP_OPEN}{lines[locale]} {SALE_NOTE_MARK}{KEEP_CLOSE}\n"
    return insert_price_note(text, note)


def insert_price_note(text: str, note: str) -> str:
    """Place a price note after the H1 and its optional blockquote summary."""
    h1 = re.search(r"^# .*\n", text, re.MULTILINE)
    if h1 is None:
        return note + "\n" + text
    at = h1.end()
    summary = re.match(r"\n(?:>.*\n)+", text[at:])
    if summary:
        at += summary.end()
    rest = text[at:]
    return text[:at] + "\n" + note + ("" if rest.startswith("\n") else "\n") + rest
