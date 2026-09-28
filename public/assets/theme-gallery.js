// The community gallery's scenario filter (mars-dawn-website#145). An external module script,
// loaded with `<script type="module" src="/assets/theme-gallery.js">` -- never inline: the site's
// CSP is `script-src 'self'` plus two sha256-hashed inline scripts (Consent Mode default, the GTM
// loader) ONLY, so an inline `<script type="module">` here would be silently blocked in every
// real browser (the way mars-dawn-website#147's theme-sim bootstrap was) and the filter would
// never do anything. scripts/check_no_inline_scripts.py holds every generated page to this.
//
// Every card and every filter button is server-rendered by scripts/build_pages.py at build time,
// from public/themes/v1/index.json, so the gallery works with no JavaScript at all: every theme
// shows, all the time. This file only adds the filtering on top, by toggling the native `hidden`
// attribute -- never a `style=` attribute, which the CSP's style-src also refuses without
// 'unsafe-inline'. No theme data, and nothing about what a visitor filters by, is sent anywhere:
// this file makes no network request of its own.

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
