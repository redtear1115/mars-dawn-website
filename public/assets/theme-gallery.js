// The community gallery's scenario filter and report buttons (mars-dawn-website#145). An external
// module script, loaded with `<script type="module" src="/assets/theme-gallery.js">` -- never
// inline: the site's CSP is `script-src 'self'` plus two sha256-hashed inline scripts (Consent
// Mode default, the GTM loader) ONLY, so an inline `<script type="module">` here would be silently
// blocked in every real browser (the way mars-dawn-website#147's theme-sim bootstrap was) and
// nothing on this page would work. scripts/check_no_inline_scripts.py holds every generated page
// to this.
//
// Every card and every filter button is server-rendered by scripts/build_pages.py at build time,
// from public/themes/v1/index.json, so the gallery's content works with no JavaScript at all:
// every theme shows, all the time. This file adds two things on top: the scenario filter (toggles
// the native `hidden` attribute -- never a `style=` attribute, which the CSP's style-src also
// refuses without 'unsafe-inline') and the Report / Report-by-email buttons' click behaviour.
//
// Report and Report-by-email are real <button>s, never <a href>s (round 2 review, #151): GA4's
// enhanced measurement records an outbound click by the clicked <a>'s own href (`link_url`), so a
// real link carrying a theme's id and version would report that theme to analytics on every
// click -- the one thing the privacy policy says never happens. Each button carries only
// `data-theme-id`/`data-theme-version` (never a URL) and its click handler builds the destination
// here, then opens it with window.open -- exactly like the simulator's own Submit button
// (public/assets/theme-sim/app.js, ThemeSimApp.submit()). No theme data, and nothing about what a
// visitor filters by or reports, is sent anywhere else: this file makes no network request of its
// own, and neither button's URL is ever written into the DOM as an href for anything to read.

const REPORT_BASE = "https://github.com/redtear1115/mars-dawn-website/issues/new";
const SUPPORT_EMAIL = "support@southern-light.dev";

export function reportUrl(themeId, version) {
  const params = new URLSearchParams();
  params.set("template", "theme-report.yml");
  params.set("theme_id", themeId);
  params.set("theme_version", version);
  return `${REPORT_BASE}?${params.toString()}`;
}

export function mailUrl(themeId, version) {
  // Not URLSearchParams: it encodes a space as "+" (application/x-www-form-urlencoded), but a
  // mailto URI's query is defined by RFC 6068, which has no "+ means space" rule -- a mail client
  // reading it strictly would show the subject with literal plus signs instead of spaces
  // (verifier finding, PR #151). encodeURIComponent percent-encodes a space as %20, which RFC
  // 6068 decoding turns back into a space, so this is the one place in this file that builds a
  // query string by hand instead of with URLSearchParams. check_theme_gallery.py decodes this
  // with urllib.parse.unquote (not parse_qs, which is the form-decoding rule) and requires no
  // '+' in the result.
  const subject = encodeURIComponent(`Theme report: ${themeId} ${version}`);
  return `mailto:${SUPPORT_EMAIL}?subject=${subject}`;
}

// The preview lightbox (owner request, 2026-10-10). Each preview is a server-rendered
// <a class="theme-preview" href="...preview-light.png"> around its <img>, so with no JavaScript
// (or no <dialog>) a click simply opens the full-size file. With both, the click opens it here
// instead, at the image's natural size, in a modal <dialog>: the browser itself gives us Esc to
// close, a focus trap (everything behind a modal dialog is inert), and the top layer, so none of
// that is re-implemented. What this adds: a visible, localised Close button (the label comes from
// the list's data-close-label, server-rendered per locale), a click on the dark area around the
// image closes it, and focus goes back to the preview that opened it. The dialog's image is the
// same URL as the card's own, so opening it costs no second download. The dialog is created on
// first use, not in the page's HTML, so a page without JavaScript carries nothing extra. All
// styling is in theme-gallery.css (classes only: the CSP has no 'unsafe-inline' for styles).
function createLightbox(closeLabel) {
  const dialog = document.createElement("dialog");
  dialog.className = "theme-lightbox";

  const scroller = document.createElement("div");
  scroller.className = "theme-lightbox-scroll";
  const image = document.createElement("img");
  image.className = "theme-lightbox-img";
  scroller.append(image);

  const close = document.createElement("button");
  close.type = "button";
  close.className = "theme-lightbox-close";
  close.textContent = closeLabel;

  // Close comes first in the DOM so showModal() puts focus on it (browsers that make a scroller
  // keyboard-focusable would otherwise pick the scroller); the scroller is still a tab stop
  // (tabindex), so the arrow keys, Space and PageUp/Down scroll an image taller than the window.
  scroller.tabIndex = 0;
  close.autofocus = true;
  dialog.append(close, scroller);
  document.body.append(dialog);

  close.addEventListener("click", () => dialog.close());
  // The area around (or, for a small image, beside) the picture is the scroller itself.
  scroller.addEventListener("click", (event) => {
    if (event.target === scroller) dialog.close();
  });
  return { dialog, scroller, image };
}

function setUpLightbox(list) {
  if (typeof HTMLDialogElement === "undefined" || typeof HTMLDialogElement.prototype.showModal !== "function") {
    return;
  }
  let box = null;
  let opener = null;
  list.dataset.lightbox = "";

  list.addEventListener("click", (event) => {
    const link = event.target.closest("a.theme-preview");
    if (!link) return;
    // Leave "open in a new tab/window" and "save as" gestures to the browser.
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }
    event.preventDefault();
    if (!box) {
      box = createLightbox(list.dataset.closeLabel || "Close");
      box.dialog.addEventListener("close", () => {
        box.image.removeAttribute("src");
        if (opener && opener.isConnected) opener.focus();
        opener = null;
      });
    }
    const thumb = link.querySelector("img");
    opener = link;
    box.image.alt = thumb ? thumb.alt : "";
    box.image.src = link.href;
    box.dialog.setAttribute("aria-label", box.image.alt);
    box.scroller.scrollTop = 0;
    box.scroller.scrollLeft = 0;
    box.dialog.showModal();
  });
}

// Split out from module-load time (rather than run directly below) so this file can be imported
// under plain `node`, with no DOM at all, to test reportUrl()/mailUrl() in isolation -- the same
// pattern scripts/check_theme_sim.mjs already uses for the simulator's own pure-logic modules.
// scripts/check_theme_gallery.py does exactly that.
function boot() {
  const filter = document.getElementById("theme-gallery-filter");
  const list = document.getElementById("theme-gallery-cards");

  if (filter && list) {
    const cards = Array.from(list.querySelectorAll(".theme-card"));
    const buttons = Array.from(filter.querySelectorAll(".theme-filter-btn"));

    function apply(scenario) {
      for (const card of cards) {
        const scenarios = (card.dataset.scenarios || "").split(" ").filter(Boolean);
        card.hidden = scenario !== "all" && !scenarios.includes(scenario);
      }
      for (const button of buttons) {
        button.setAttribute("aria-pressed", String(button.dataset.scenario === scenario));
      }
    }

    for (const button of buttons) {
      button.addEventListener("click", () => apply(button.dataset.scenario));
    }
  }

  if (list) {
    setUpLightbox(list);
    list.addEventListener("click", (event) => {
      const reportButton = event.target.closest(".theme-report");
      const mailButton = event.target.closest(".theme-report-mail");
      const button = reportButton || mailButton;
      if (!button) return;
      const themeId = button.dataset.themeId || "";
      const version = button.dataset.themeVersion || "";
      const url = reportButton ? reportUrl(themeId, version) : mailUrl(themeId, version);
      window.open(url, "_blank", "noopener");
    });
  }
}

if (typeof document !== "undefined") {
  boot();
}
