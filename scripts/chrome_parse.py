"""Reads a built page's header, language switch and footer (website #247) for check_hreflang.py and
check_invariants.py. It knows the markup build_pages.py writes; it does not import build_pages.py, so a
mistake there can't hide itself.

The header has the main navigation and the language switch each in two copies, a wide one and a narrow
one (CSS shows one), so every list is kept per copy:

    nav.site-nav   ul.site-nav-wide, details.site-nav-narrow      -> main_nav["wide"|"narrow"]
    nav.lang       div.lang-wide (ul + details.lang-more),
                   details.lang-narrow (div.lang-panel: ul, hr.lang-sep, ul)   -> lang["wide"|"narrow"]
    footer         nav.footer-nav > section > h3 + ul             -> footer_groups
"""
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Chrome(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []                       # (tag, set of classes), open elements
        self.nav_lang_count = 0
        self.site_nav_count = 0
        self.main_nav = {"wide": [], "narrow": []}     # (href, aria-current)
        self.lang = {"wide": [], "narrow": []}         # (hreflang, href, lang, aria-current)
        self.lang_more_details = 0            # details.lang-more
        self.lang_more_summary = None         # (text, lang attribute) of details.lang-more > summary
        self.lang_narrow_summary = None
        self.lang_seps = 0                    # hr.lang-sep
        self.footer_groups = []               # [heading, [(href or "#button:<id>", aria-current)]]
        self.consent_ids = 0
        self.store_chips = 0
        self.main_hrefs = []
        self.brand = None                     # (href, aria-label, aria-current)
        self.nav_labels = {}                  # "site-nav" / "lang" / "footer-nav" -> aria-label
        self.menu_summary = None
        self.html_lang = None
        self._text = None

    # -- helpers
    def _in(self, tag, cls=None):
        return any(t == tag and (cls is None or cls in c) for t, c in self.stack)

    def _lang_copy(self):
        if self._in("div", "lang-wide"):
            return "wide"
        if self._in("details", "lang-narrow"):
            return "narrow"
        return None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        if "store-chip" in classes:
            self.store_chips += 1
        if tag == "html":
            self.html_lang = a.get("lang")
        if a.get("id") == "consent-settings-link":
            self.consent_ids += 1
        if tag == "nav" and "lang" in classes:
            self.nav_lang_count += 1
            self.nav_labels["lang"] = a.get("aria-label")
        elif tag == "nav" and "site-nav" in classes:
            self.site_nav_count += 1
            self.nav_labels["site-nav"] = a.get("aria-label")
        elif tag == "nav" and "footer-nav" in classes:
            self.nav_labels["footer-nav"] = a.get("aria-label")
        elif tag == "details" and "lang-more" in classes:
            self.lang_more_details += 1
        elif tag == "hr" and "lang-sep" in classes:
            self.lang_seps += 1
        elif tag == "a" and "brand" in classes:
            self.brand = (a.get("href"), a.get("aria-label"), a.get("aria-current"))
        elif tag == "section" and self._in("nav", "footer-nav"):
            self.footer_groups.append([None, []])
        elif tag == "h3" and self._in("nav", "footer-nav") and self.footer_groups:
            self._text = ("h3", [])
        elif tag == "summary":
            self._text = ("summary", [], a.get("lang"), self._summary_owner())
        elif tag == "a":
            href = a.get("href")
            if self._in("main"):
                self.main_hrefs.append(href)
            if self._in("nav", "site-nav"):
                copy = "wide" if self._in("ul", "site-nav-wide") else "narrow" if self._in("details", "site-nav-narrow") else None
                if copy:
                    self.main_nav[copy].append((href, a.get("aria-current")))
            elif self._in("nav", "lang"):
                copy = self._lang_copy()
                if copy:
                    self.lang[copy].append((a.get("hreflang"), href, a.get("lang"), a.get("aria-current")))
            elif self._in("nav", "footer-nav") and self.footer_groups:
                self.footer_groups[-1][1].append((href, a.get("aria-current")))
        elif tag == "button" and a.get("id") and self._in("nav", "footer-nav") and self.footer_groups:
            self.footer_groups[-1][1].append((f"#button:{a['id']}", None))
        if tag not in VOID:
            self.stack.append((tag, classes))

    def _summary_owner(self):
        if self._in("details", "lang-more"):
            return "lang-more"
        if self._in("details", "lang-narrow"):
            return "lang-narrow"
        if self._in("details", "site-nav-narrow"):
            return "site-nav-narrow"
        return None

    def handle_data(self, data):
        if self._text:
            self._text[1].append(data)

    def handle_endtag(self, tag):
        if self._text and self._text[0] == tag:
            text = "".join(self._text[1]).strip()
            if tag == "h3":
                self.footer_groups[-1][0] = text
            else:
                owner = self._text[3]
                if owner == "lang-more":
                    self.lang_more_summary = (text, self._text[2])
                elif owner == "lang-narrow":
                    self.lang_narrow_summary = (text, self._text[2])
                elif owner == "site-nav-narrow":
                    self.menu_summary = text
            self._text = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break


def parse(text: str) -> Chrome:
    chrome = Chrome()
    chrome.feed(text)
    return chrome
