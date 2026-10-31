"""The 30-second mars-dawn-agents home page film (website #335).

Layout decided in #327: Daphne's issuecomment-6542253169 and Ray's
issuecomment-6542248332. Copy approved in #335 issuecomment-6537988090 /
6541001486. Both Chinese locales play the Traditional Chinese film (Ray's decision E);
other locales play English. The music-only film has burned-in captions, with optional
caption tracks shared by its desktop 16:9 and phone 9:16 versions.

Assets are hand-placed under public/assets/film/. Playback requires a click,
preload="none"; styles are appended to loop.css by build_pages.py, with no inline styles.
"""

import html

DURATION_SECONDS = 30
# Planned go-live, a placeholder: set to the real deploy time when the film goes live.
# Google wants a full ISO 8601 datetime with an offset (brand_film_themes.py / #256).
UPLOAD_DATE = "2026-11-02T10:00:00+08:00"

# (heading, accessible name, browser fallback, figcaption).
COPY = {
    "en": ('Watch the film', 'Video: MarsDawn on Mac and iPhone, 30 seconds', 'Your browser cannot play this video.', '30 seconds: your agent writes on the Mac, you read on iPhone.'),
    "zh-hant": ('觀看影片', '影片：Mac 與 iPhone 上的 MarsDawn，30 秒', '你的瀏覽器無法播放這支影片。', '30 秒：agent 在 Mac 上寫，你在 iPhone 上讀。'),
    "zh-hans": ('观看影片', '视频：Mac 与 iPhone 上的 MarsDawn，30 秒，繁体中文字幕', '你的浏览器无法播放这支影片。', '30 秒：代理在 Mac 上写，你在 iPhone 上读。（繁体中文字幕）'),
    "ja": ('動画を見る', '動画：Mac と iPhone の MarsDawn、30 秒、英語字幕', 'お使いのブラウザではこの動画を再生できません。', '30 秒：エージェントが Mac で書き、あなたは iPhone で読む。（英語字幕）'),
    "ko": ('영상 보기', '동영상: Mac과 iPhone의 MarsDawn, 30초, 영어 자막', '이 브라우저에서는 영상을 재생할 수 없습니다.', '30초: 에이전트는 Mac에서 쓰고, 나는 iPhone에서 읽습니다. (영어 자막)'),
    "de": ('Den Film ansehen', 'Video: MarsDawn auf Mac und iPhone, 30 Sekunden, englische Untertitel', 'Dein Browser kann dieses Video nicht abspielen.', '30 Sekunden: Dein Agent schreibt auf dem Mac, du liest auf dem iPhone. (Englische Untertitel)'),
    "fr": ('Voir le film', 'Vidéo\xa0: MarsDawn sur Mac et iPhone, 30 secondes, sous-titres en anglais', 'Votre navigateur ne peut pas lire cette vidéo.', '30 secondes\xa0: votre agent écrit sur le Mac, vous lisez sur iPhone. (Sous-titres en anglais)'),
    "es": ('Ver el video', 'Vídeo: MarsDawn en Mac y iPhone, 30 segundos, subtítulos en inglés', 'Tu navegador no puede reproducir este video.', '30 segundos: tu agente escribe en el Mac y tú lees en el iPhone. (Subtítulos en inglés)'),
}


def _film_language(locale: str) -> str:
    return "zh-Hant" if locale in ("zh-hant", "zh-hans") else "en"


def film_html(locale: str) -> str:
    heading, label, fallback, caption = (html.escape(value, quote=True) for value in COPY[locale])
    language = _film_language(locale)
    track_label = {"zh-hant": "繁體中文", "zh-hans": "繁体中文"}.get(locale, "English")
    track = (
        f'<track kind="captions" src="/assets/film/mars-dawn-agents-{language}.vtt" '
        f'srclang="{language}" label="{html.escape(track_label, quote=True)}">'
    )
    videos = []
    for shape, width, height, prefix in (
        ("wide", 1920, 1080, "mars-dawn-agents-16x9"),
        ("tall", 1080, 1920, "mars-dawn-agents"),
    ):
        videos.append(
            f'<video class="film-{shape}" controls preload="none" playsinline width="{width}" height="{height}" '
            f'poster="/assets/film/{prefix}-poster-{language}.jpg" aria-label="{label}">\n'
            f'<source src="/assets/film/{prefix}-{language}.mp4" type="video/mp4">\n'
            f'{track}\n'
            f'<p>{fallback}</p>\n'
            '</video>'
        )
    return (
        '<section class="film" aria-labelledby="film-h">\n'
        f'<h2 id="film-h">{heading}</h2>\n'
        '<figure class="film-figure">\n'
        + "\n".join(videos)
        + f'\n<figcaption>{caption}</figcaption>\n'
        '</figure>\n'
        '</section>'
    )


def video_object(locale: str, base_url: str) -> dict:
    language = _film_language(locale)
    if language == "zh-Hant":
        name = "MarsDawn：任何 agent，任何地方"
        description = "用手機交代下去，agent 在 Mac 上動筆，Mac 版 MarsDawn 打開它寫的 Markdown 和 HTML。在 iPhone 或 iPad 上讀同一份計畫，修改回到 Mac。"
    else:
        name = "MarsDawn: work with any agent, anywhere"
        description = "Send the task from your phone. Your agent writes on your Mac, and MarsDawn for Mac opens its Markdown and HTML. Read the same plan on your iPhone or iPad; editing stays on the Mac."
    return {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": name,
        "description": description,
        "inLanguage": language,
        "duration": "PT30S",
        "uploadDate": UPLOAD_DATE,
        "width": 1920,
        "height": 1080,
        "contentUrl": f"{base_url}/assets/film/mars-dawn-agents-16x9-{language}.mp4",
        "thumbnailUrl": [
            f"{base_url}/assets/film/mars-dawn-agents-16x9-poster-{language}.jpg",
            f"{base_url}/assets/film/mars-dawn-agents-poster-{language}.jpg",
        ],
    }


CSS = """/* The home page's agents film (scripts/brand_film.py, website #335).
   No animation or transition of its own, so no reduced-motion rule is needed. */
.film { margin-top: 56px; }
.film h2 { margin-top: 0; }
.film figure { margin: 0; }
.film video {
  display: block;
  height: auto;
  border-radius: var(--r-plate);
  background: #000;
}
.film video.film-wide {
  width: max(100%, var(--w-media));
  margin-inline: calc((100% - max(100%, var(--w-media))) / 2);
  aspect-ratio: 16 / 9;
}
.film video.film-tall {
  aspect-ratio: 9 / 16;
  width: min(100%, calc(80svh * 9 / 16));
  margin-inline: auto;
}
.film figcaption { margin-top: 12px; }
@media (min-width: 900px) {
  .film video.film-tall { display: none; }
}
@media (max-width: 899.98px) {
  .film video.film-wide { display: none; }
  .film figcaption { text-align: center; }
}
"""
