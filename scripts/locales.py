"""Which locales the site knows, and which of them it builds (website #162).

The site knows eight: the four it serves today (BASE) and de, fr, es and ko (PLANNED), which the
app ships in 1.1.0. A planned locale is known but not built until its copy is complete: nothing is
generated under /<l>/, linked, put in a hreflang set, the sitemap or llms.txt until
`scripts/copy_<l>.py` exists and says `COMPLETE = True`. Until then the site is byte-for-byte what
it was with four. So no English-in-a-German-URL page can go live by accident: a locale's copy is
either all there and switched on, or the locale does not exist as far as the build is concerned.

`COMPLETE = True` is a promise the build then holds the module to (`build_pages.py` refuses to
build, naming what is missing, if the module's shape differs from ja's, any string is empty, or the
locale's legal pages, hero snapshot or theme names are absent) and `check_locales.py` re-checks on
the built site. Flip it last, after the module is filled in.

Read by build_pages.py, render_legal.py, sync_hero_sources.py and the checks that need the enabled
list. check_hreflang.py and check_locales.py write the prefixes out again on purpose: a check that
imports the thing it checks can't catch a mistake in it.
"""
import importlib
import sys
from pathlib import Path

BASE = ("en", "zh-hant", "zh-hans", "ja")
PLANNED = ("de", "fr", "es", "ko")
KNOWN = BASE + PLANNED

# prefix is the URL folder, html_lang the <html lang> and hreflang value, label the language's own
# name in the language switch, og the Open Graph token. colon is what follows a list label in
# generated text (the home page's trait list, a figure's "In this screenshot"): full-width in the
# CJK languages, a no-break space before it in French, as French sets it.
DEFS = {
    "en": {"prefix": "", "html_lang": "en", "label": "English", "root": "/", "og": "en_US", "colon": ": "},
    "zh-hant": {"prefix": "zh-hant/", "html_lang": "zh-Hant", "label": "繁體中文", "root": "/zh-hant/", "og": "zh_TW", "colon": "："},
    "zh-hans": {"prefix": "zh-hans/", "html_lang": "zh-Hans", "label": "简体中文", "root": "/zh-hans/", "og": "zh_CN", "colon": "："},
    "ja": {"prefix": "ja/", "html_lang": "ja", "label": "日本語", "root": "/ja/", "og": "ja_JP", "colon": "："},
    "de": {"prefix": "de/", "html_lang": "de", "label": "Deutsch", "root": "/de/", "og": "de_DE", "colon": ": "},
    "fr": {"prefix": "fr/", "html_lang": "fr", "label": "Français", "root": "/fr/", "og": "fr_FR", "colon": " : "},
    "es": {"prefix": "es/", "html_lang": "es", "label": "Español", "root": "/es/", "og": "es_ES", "colon": ": "},
    "ko": {"prefix": "ko/", "html_lang": "ko", "label": "한국어", "root": "/ko/", "og": "ko_KR", "colon": ": "},
}

SCRIPTS = Path(__file__).resolve().parent


def module_name(locale: str) -> str:
    return "copy_" + locale.replace("-", "_")


def copy_complete(locale: str) -> bool:
    """True when scripts/copy_<l>.py exists and sets COMPLETE = True."""
    if not (SCRIPTS / (module_name(locale) + ".py")).is_file():
        return False
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    sys.dont_write_bytecode = True  # no scripts/__pycache__: CI fails on any untracked file after a build
    return importlib.import_module(module_name(locale)).__dict__.get("COMPLETE") is True


def enabled() -> list:
    return list(BASE) + [locale for locale in PLANNED if copy_complete(locale)]
