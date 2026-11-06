"""The shared HTML-only pricing.md card; page assembly handles the price phase."""
from html import escape as html_escape

import price

# Badge, price, quote, three list items, CTA. Amounts and trial length belong to price.py.
STRINGS = {
    "en": (
        "No subscription", "USD {price}, once",
        "Free to download. Every feature free for {trial_days} days.",
        "One Apple Account, one purchase, on Mac, iPhone and iPad.",
        "No account, and nothing renews.",
        "Quick Look in Finder works with or without the trial.",
        "Get MarsDawn on the Mac App Store",
    ),
    "zh-hant": (
        "不用訂閱", "一次 USD {price}", "免費下載，{trial_days} 天內所有功能免費試用。",
        "同一個 Apple 帳號，一次購買，Mac、iPhone、iPad 都能用。",
        "不需要帳號，也不會續訂。", "Finder 的快速查看不論試用與否都能用。",
        "到 Mac App Store 下載 MarsDawn",
    ),
    "ja": (
        "サブスクなし", "USD {price} の買い切り",
        "無料でダウンロード。{trial_days}日間はすべての機能を無料で試せます。",
        "同じ Apple Account なら、1 回の購入で Mac、iPhone、iPad のすべてで使えます。",
        "アカウント不要、自動更新もありません。",
        "Finder のクイックルックは試用期間に関係なく使えます。",
        "Mac App Store で MarsDawn を入手",
    ),
    "zh-hans": (
        "无需订阅", "一次 USD {price}", "免费下载，{trial_days} 天内所有功能免费试用。",
        "同一个 Apple 账户，一次购买，Mac、iPhone、iPad 都能用。",
        "不需要账户，也不会续订。", "访达的快速查看不论有没有试用都能用。",
        "到 Mac App Store 下载 MarsDawn",
    ),
    "ko": (
        "구독 없음", "한 번만 USD {price}",
        "무료로 다운로드하고, {trial_days}일 동안 모든 기능을 무료로 써 보세요.",
        "같은 Apple 계정으로 한 번 구입하면 Mac, iPhone, iPad에서 모두 쓸 수 있습니다.",
        "계정이 필요 없고, 자동 갱신도 없습니다.",
        "Finder의 훑어보기는 체험 여부와 관계없이 쓸 수 있습니다.",
        "Mac App Store에서 MarsDawn 받기",
    ),
    "de": (
        "Kein Abo", "{price} USD, einmalig",
        "Kostenlos laden. {trial_days} Tage lang alle Funktionen gratis.",
        "Ein Apple Account, ein Kauf: für Mac, iPhone und iPad.",
        "Kein Konto, und nichts verlängert sich.",
        "Die Übersicht im Finder funktioniert mit und ohne Test.",
        "MarsDawn im Mac App Store laden",
    ),
    "fr": (
        "Sans abonnement", "{price} USD, une seule fois",
        "Téléchargement gratuit. Toutes les fonctions gratuites pendant {trial_days} jours.",
        "Un même compte Apple, un seul achat, sur Mac, iPhone et iPad.",
        "Aucun compte, et rien ne se renouvelle.",
        "Coup d’œil dans le Finder fonctionne avec ou sans essai.",
        "Obtenir MarsDawn sur le Mac App Store",
    ),
    "es": (
        "Sin suscripción", "{price} USD, un solo pago",
        "Descarga gratis. Todas las funciones gratis durante {trial_days} días.",
        "Una misma cuenta de Apple, una sola compra, en Mac, iPhone y iPad.",
        "Sin cuenta, y nada se renueva.",
        "Vista rápida en el Finder funciona con o sin la prueba.",
        "Consigue MarsDawn en el Mac App Store",
    ),
}

for _locale, _patterns in STRINGS.items():
    assert len(_patterns) == 7, _locale
    for _pattern in _patterns:
        assert not any(value in _pattern for value in (
            price.REGULAR, price.REGULAR.replace(".", ","), str(price.TRIAL_DAYS)
        )), (_locale, _pattern)
    assert "{price}" in _patterns[1] and "{trial_days}" in _patterns[2], _locale


def html(locale: str, href: str) -> str:
    """Render regular-price copy; the page pipeline applies any sale phase later."""
    amount = price.REGULAR.replace(".", ",") if locale in {"de", "fr", "es"} else price.REGULAR
    badge, amount_text, quote, *rest = (
        html_escape(pattern.format(price=amount, trial_days=price.TRIAL_DAYS))
        for pattern in STRINGS[locale]
    )
    items = "\n".join(f"      <li>{item}</li>" for item in rest[:3])
    href = html_escape(href, quote=True)
    return f'''<section class="price-card" aria-labelledby="price-title">
  <div class="price-card__bar" aria-hidden="true"><span class="price-card__dots"></span>pricing.md</div>
  <div class="price-card__body">
    <div class="price-card__head"><h2 id="price-title">MarsDawn</h2><p class="price-card__badge">{badge}</p></div>
    <p class="price-card__price">{amount_text}</p>
    <blockquote>{quote}</blockquote>
    <ul>
{items}
    </ul>
    <p class="price-card__action"><a class="price-card__cta" href="{href}">{rest[3]}</a></p>
  </div>
</section>'''
