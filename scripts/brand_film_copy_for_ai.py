"""The 18-second Copy for AI film on /copy-for-ai/ (website #366, for the page of #364).

Placement and shape: Daphne's #366 issuecomment-6703324764 (directly under the sample, no heading of
its own, 16:9, width and height on the element so the page does not shift, styles in the stylesheet).
Playback: the approved comment #366 issuecomment-6768077041 (Ray approved the film on 11-10): muted
autoplay, loop, playsinline and controls; with prefers-reduced-motion only the poster; the phone gets
the 720p file and the desktop the 1080p one. That replaces Daphne's earlier "no autoplay".

The film's words are burned into the picture, so there is no caption track. Only the English and
Traditional Chinese films exist: the zh-hant page plays the Traditional Chinese one and the other seven
languages play the English one. The film adds no copy of its own: the accessible name is the page's own
name for the feature ("Copy for AI", "拷貝給 AI", ...), the fallback text is the one the other films use.

Files, under public/assets/film/ (hand-placed, byte for byte what the brand-films repo exports to
out/mars-dawn-copy-for-ai/web/):
  marsdawn-copy-for-ai-<en|zh-Hant>-1080p30.mp4   1920x1080, 18.0 s, 1.9 MB / 1.8 MB
  marsdawn-copy-for-ai-<en|zh-Hant>-720p30.mp4    1280x720, 18.0 s, 1.1 MB
  marsdawn-copy-for-ai-<en|zh-Hant>-poster.jpg    1920x1080, the last frame (logo and App Store badge)

How it plays (public/assets/copy-for-ai-film.js, an external script: the CSP allows no other):
  - `media` on the <source> of a <video> works in Chromium and not in WebKit (measured with Playwright
    on /copy-for-ai/, 390 and 1280 px wide: Chromium picked the file named for the phone, WebKit always the
    default one), so Safari would send a phone the 1080p file. The script chooses the file for a
    phone-width window in every engine, from the `data-small` attribute.
  - The HTML has no `autoplay` attribute, and `preload="none"`. A browser starts an `autoplay` video
    before any script can say "reduced motion", so the script starts the film instead, and only when
    the visitor has not asked for less motion. Without the script, or with reduced motion, the page shows
    the poster and the controls play the film. The film's bytes are fetched when it plays.

The styles are in public/assets/site.css (.film-copy-ai), next to the sample's own rule.
"""

import html

FILM = "/assets/film/marsdawn-copy-for-ai-{lang}-1080p30.mp4"
FILM_SMALL = "/assets/film/marsdawn-copy-for-ai-{lang}-720p30.mp4"
POSTER = "/assets/film/marsdawn-copy-for-ai-{lang}-poster.jpg"
SCRIPT = "/assets/copy-for-ai-film.js"
DURATION_ISO = "PT18S"
NAME = "Copy for AI | MarsDawn"
# Planned go-live (the milestone's due date), a placeholder: set it to the real time the page reaches
# production when it is merged. Google wants a full ISO 8601 datetime with an offset (brand_film_themes.py, #256).
UPLOAD_DATE = "2026-11-17T10:00:00+08:00"
MARK = "<!--film-copy-for-ai-->"

# Text for a browser that cannot play the film: the same words the other films use (brand_film_mac.COPY).
FALLBACK = {
    "en": "Your browser cannot play this video.",
    "zh-hant": "你的瀏覽器無法播放這支影片。",
    "zh-hans": "你的浏览器无法播放这支影片。",
    "ja": "お使いのブラウザではこの動画を再生できません。",
    "ko": "이 브라우저에서는 영상을 재생할 수 없습니다.",
    "de": "Dein Browser kann dieses Video nicht abspielen.",
    "fr": "Votre navigateur ne peut pas lire cette vidéo.",
    "es": "Tu navegador no puede reproducir este video.",
}


def film_language(locale: str) -> str:
    return "zh-Hant" if locale == "zh-hant" else "en"


def _label(feature: str) -> str:
    return f"{feature} | MarsDawn"


def section_html(locale: str, feature: str) -> str:
    """The film for `locale`'s page. `feature` is that page's own name for the feature."""
    language = film_language(locale)
    label = html.escape(_label(feature), quote=True)
    return (
        '<figure class="film-copy-ai">\n'
        f'<video controls muted loop playsinline preload="none" width="1920" height="1080" '
        f'poster="{POSTER.format(lang=language)}" data-small="{FILM_SMALL.format(lang=language)}" aria-label="{label}">\n'
        f'<source src="{FILM.format(lang=language)}" type="video/mp4">\n'
        f"<p>{html.escape(FALLBACK[locale])}</p>\n"
        "</video>\n"
        "</figure>"
    )


def section_markdown_html(locale: str, base_url: str, feature: str) -> str:
    """The same place in the Markdown twin, which cannot carry a video: a link to the film."""
    language = film_language(locale)
    return f'<p><a href="{base_url}{FILM.format(lang=language)}">{html.escape(_label(feature))}</a></p>'


def video_object(locale: str, base_url: str, description: str) -> dict:
    """The film's VideoObject. `description` is the page's lede, as plain text."""
    language = film_language(locale)
    return {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": NAME,
        "description": description,
        "inLanguage": language,
        "duration": DURATION_ISO,
        "uploadDate": UPLOAD_DATE,
        "width": 1920,
        "height": 1080,
        "contentUrl": f"{base_url}{FILM.format(lang=language)}",
        "thumbnailUrl": f"{base_url}{POSTER.format(lang=language)}",
    }
