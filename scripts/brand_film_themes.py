"""The second brand film's section, on /features/ and /themes/ (website #228's film, owner 2026-10-15).

"After the page is printed": a meeting around printed pages, a pen in the margin, a paper record on file.
88 seconds, English on screen in every locale (the lines are burned into the picture). As with the first
film (brand_film.py): zh-Hant, zh-Hans and ja add a WebVTT track in their own language, `default`; the
other locales have none. The poster shows first, a click plays with sound, no autoplay, preload="none":
the 8 MB film is fetched only when a visitor asks.

Files, under public/assets/film/ (hand-placed, not generated):
  marsdawn-themes-film-en-1080p30.mp4   the film, from the brands-film repo (out/mars-dawn-themes/web/)
  marsdawn-themes-film-en-poster.jpg    the frame at 45.5 s (the meeting, every marker on the Decisions row), 1280 px wide
  marsdawn-themes-film-<zh-hant|zh-hans|ja>.vtt   the translation tracks (projects/mars-dawn-themes/captions/)

The heading and the one-line caption of en and zh-Hant are the owner-approved text (approved_copy.FILM_THEMES,
loaded from the vault draft); the other six locales' are machine drafts (needs-i18n) below. The section moves
nothing of its own, so reduced motion needs no rule. Its styles are appended to public/assets/annotations.css
by build_pages.py (both pages already link it); the CSP's `media-src 'self'` allows the film and its tracks.
"""
import approved_copy

FILM = "/assets/film/marsdawn-themes-film-en-1080p30.mp4"
POSTER = "/assets/film/marsdawn-themes-film-en-poster.jpg"
DURATION_SECONDS = 88
DURATION_ISO = "PT1M28S"
# VideoObject.uploadDate. MUST be set to the deploy date when the film goes live (it is 2026-10-15, the day the
# film was finished, until then).
UPLOAD_DATE = "2026-10-15"
MARK = "<!--film-themes-->"

TRACKS = {
    "zh-hant": ("/assets/film/marsdawn-themes-film-zh-hant.vtt", "zh-Hant", "繁體中文"),
    "zh-hans": ("/assets/film/marsdawn-themes-film-zh-hans.vtt", "zh-Hans", "简体中文"),
    "ja": ("/assets/film/marsdawn-themes-film-ja.vtt", "ja", "日本語"),
}

# (the video's accessible name, fallback text for a browser that cannot play it).
LABELS = {
    "en": ("MarsDawn film, 88 seconds", "Your browser cannot play this video."),
    "zh-hant": ("MarsDawn 影片，88 秒", "你的瀏覽器無法播放這支影片。"),
    "zh-hans": ("MarsDawn 影片，88 秒", "你的浏览器无法播放这支影片。"),
    "ja": ("MarsDawn の動画（88 秒）", "お使いのブラウザではこの動画を再生できません。"),
    "de": ("MarsDawn-Film (Englisch), 88 Sekunden", "Dein Browser kann dieses Video nicht abspielen."),
    "fr": ("Film MarsDawn (en anglais), 88 secondes", "Votre navigateur ne peut pas lire cette vidéo."),
    "es": ("Video de MarsDawn (en inglés), 88 segundos", "Tu navegador no puede reproducir este video."),
    "ko": ("MarsDawn 영상(영어), 88초", "이 브라우저에서는 영상을 재생할 수 없습니다."),
}

# (heading, caption). en and zh-Hant: approved. The rest: machine drafts, needs-i18n (Grok reviews them).
TEXT = {
    "en": (approved_copy.FILM_THEMES["en"]["heading"], approved_copy.FILM_THEMES["en"]["caption"]),
    "zh-hant": (approved_copy.FILM_THEMES["zh-hant"]["heading"], approved_copy.FILM_THEMES["zh-hant"]["caption"]),
    "zh-hans": ("页面印出来之后", "大家围着印出来的页面开会，有人拿笔在页边写字，纸质记录收进档案。"),
    "ja": ("ページを印刷したあと", "印刷したページを囲んで会議をし、余白にペンで書き込み、紙の記録をファイルに綴じる。"),
    "de": ("Nachdem die Seite gedruckt ist", "Eine Besprechung rund um gedruckte Seiten, ein Stift am Rand, eine Papierakte im Ordner."),
    "fr": ("Une fois la page imprimée", "Une réunion autour de pages imprimées, un stylo dans la marge, un dossier papier classé."),
    "es": ("Después de imprimir la página", "Una reunión alrededor de páginas impresas, un bolígrafo en el margen, un registro en papel archivado."),
    "ko": ("페이지를 인쇄한 뒤", "인쇄한 페이지를 둘러싼 회의, 여백에 펜으로 쓰는 글씨, 서류철에 보관되는 종이 기록."),
}


def section_html(locale: str) -> str:
    heading, caption = TEXT[locale]
    label, fallback = LABELS[locale]
    track = ""
    if locale in TRACKS:
        src, lang, name = TRACKS[locale]
        track = f'\n<track kind="subtitles" src="{src}" srclang="{lang}" label="{name}" default>'
    return (
        '<section class="film-themes" aria-labelledby="film-themes-h">\n'
        f'<h2 id="film-themes-h">{heading}</h2>\n'
        f"<p>{caption}</p>\n"
        f'<video controls preload="none" playsinline width="1920" height="1080" poster="{POSTER}" aria-label="{label}">\n'
        f'<source src="{FILM}" type="video/mp4">{track}\n'
        f"<p>{fallback}</p>\n"
        "</video>\n"
        "</section>"
    )


def section_markdown_html(locale: str, base_url: str) -> str:
    """The same section for the Markdown twin, which cannot carry a video: heading, caption and a link."""
    heading, caption = TEXT[locale]
    label, _ = LABELS[locale]
    return f'<h2>{heading}</h2>\n<p>{caption}</p>\n<p><a href="{base_url}{FILM}">{label}</a></p>'


def video_object(locale: str, base_url: str) -> dict:
    heading, caption = TEXT[locale]
    return {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": heading,
        "description": caption,
        "thumbnailUrl": base_url + POSTER,
        "uploadDate": UPLOAD_DATE,
        "duration": DURATION_ISO,
        "contentUrl": base_url + FILM,
    }


CSS = """/* The second brand film's section on /features/ and /themes/ (scripts/brand_film_themes.py). It has no
   animation or transition of its own, so there is no reduced-motion rule to write. */
.film-themes { margin-top: 48px; }
.film-themes h2 { margin-top: 0; }
/* --w-media (site.css): the same edges as the hero window, the loop and the screenshot plates. */
.film-themes video {
  display: block;
  width: max(100%, var(--w-media));
  margin-inline: calc((100% - max(100%, var(--w-media))) / 2);
  aspect-ratio: 16 / 9;
  height: auto;
  border-radius: var(--r-plate);
  background: #000;
}
"""
