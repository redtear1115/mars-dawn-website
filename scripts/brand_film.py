"""The brand film's section on the home page (website #159): its own section directly below the hero.

The film is English in every locale (its on-screen lines are burned into the picture). zh-Hant,
zh-Hans and ja add a WebVTT track in their own language, `default`, so the translation shows
without a click; the other locales have none. The poster shows first and a click plays with sound:
no autoplay, `preload="none"`, so the film's 3 MB is fetched only when a visitor asks. Only the
poster (a downsized JPEG) is part of first load.

Files, under public/assets/film/ (hand-placed, not generated):
  marsdawn-film-en-1080p30.mp4   the film, from the brand-films repo (out/mars-dawn/web/)
  marsdawn-film-en-poster.jpg    its poster: the frame at 20.0 s ("Read what your agent wrote."), 1280 px wide
  marsdawn-film-<zh-hant|zh-hans|ja>.vtt   the translation tracks, copied from #159's comment

The section moves nothing of its own: no transition, no animation, so reduced motion needs no
rule. Its styles are appended to public/assets/loop.css by build_pages.py (one stylesheet less to fetch); the CSP's `media-src 'self'` allows the
film and its tracks (public/_headers).
"""

FILM = "/assets/film/marsdawn-film-en-1080p30.mp4"
POSTER = "/assets/film/marsdawn-film-en-poster.jpg"
DURATION_SECONDS = 54

# Locale -> (track file, srclang, the track's label in its own language). Locales not listed have
# no track: they watch the English film as it is.
TRACKS = {
    "zh-hant": ("/assets/film/marsdawn-film-zh-hant.vtt", "zh-Hant", "繁體中文"),
    "zh-hans": ("/assets/film/marsdawn-film-zh-hans.vtt", "zh-Hans", "简体中文"),
    "ja": ("/assets/film/marsdawn-film-ja.vtt", "ja", "日本語"),
}

# (heading, the video's accessible name, fallback text for a browser that cannot play it).
COPY = {
    "en": ("Watch the film", "MarsDawn film, 54 seconds", "Your browser cannot play this video."),
    "zh-hant": ("觀看影片", "MarsDawn 影片，54 秒", "你的瀏覽器無法播放這支影片。"),
    "zh-hans": ("观看影片", "MarsDawn 影片，54 秒", "你的浏览器无法播放这支影片。"),
    "ja": ("動画を見る", "MarsDawn の動画（54 秒）", "お使いのブラウザではこの動画を再生できません。"),
    "de": ("Den Film ansehen", "MarsDawn-Film, 54 Sekunden", "Dein Browser kann dieses Video nicht abspielen."),
    "fr": ("Voir le film", "Film MarsDawn, 54 secondes", "Votre navigateur ne peut pas lire cette vidéo."),
    "es": ("Ver el vídeo", "Vídeo de MarsDawn, 54 segundos", "Tu navegador no puede reproducir este vídeo."),
    "ko": ("영상 보기", "MarsDawn 영상, 54초", "이 브라우저에서는 영상을 재생할 수 없습니다."),
}


def film_html(locale: str) -> str:
    heading, label, fallback = COPY[locale]
    track = ""
    if locale in TRACKS:
        src, lang, name = TRACKS[locale]
        track = f'\n<track kind="subtitles" src="{src}" srclang="{lang}" label="{name}" default>'
    return (
        '<section class="film" aria-labelledby="film-h">\n'
        f'<h2 id="film-h">{heading}</h2>\n'
        f'<video controls preload="none" playsinline width="1920" height="1080" poster="{POSTER}" aria-label="{label}">\n'
        f'<source src="{FILM}" type="video/mp4">{track}\n'
        f"<p>{fallback}</p>\n"
        "</video>\n"
        "</section>"
    )


CSS = """/* The home page's brand film (scripts/brand_film.py, website #159). It has no animation or
   transition of its own, so there is no reduced-motion rule to write. */
.film { margin-top: 56px; }
.film h2 { margin-top: 0; }
/* --w-media (site.css): the same edges as the hero window, the loop and the screenshot plates. */
.film video {
  display: block;
  width: max(100%, var(--w-media));
  margin-inline: calc((100% - max(100%, var(--w-media))) / 2);
  aspect-ratio: 16 / 9;
  height: auto;
  border-radius: var(--r-plate);
  background: #000;
}
"""
