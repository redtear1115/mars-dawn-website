// Cookie consent banner. Loaded with `defer` from every page's <head> (build_pages.py's
// render()/render_404()). Same-origin, so it needs no CSP hash, unlike the two small
// inline scripts in <head> (Consent Mode default, then the GTM loader) that run before
// this file can, since this file only runs once the DOM and the deferred load finish.
//
// localStorage key and values must match consent_head_html()/CONSENT_DEFAULT_SCRIPT in
// scripts/build_pages.py, which reads the same key to decide the initial consent state
// on the very next page load.
(function () {
  "use strict";
  var KEY = "md-consent";

  // GTM-KCC7FDWZ's GA4 tag is G-J8S869VKNH; GA4 names its own per-property cookie
  // _ga_<measurement id, without the "G-">. Update this if that tag's measurement ID
  // ever changes (and update the privacy policy's four locales to match).
  var GA_MEASUREMENT_SUFFIX = "J8S869VKNH";
  var GA_COOKIE_NAMES = ["_ga", "_ga_" + GA_MEASUREMENT_SUFFIX];
  // GA4 sets its cookies on the site's own host, marsdawn.southern-light.dev, but a
  // future GTM change could set them on the registrable parent domain instead
  // (southern-light.dev is not a public suffix, so a page here may write and erase
  // cookies scoped to it). Erase on both, plus with no explicit domain at all, so a
  // cookie set any of those three ways during a prior Accept actually goes away.
  var COOKIE_DOMAINS = [null, window.location.hostname, ".southern-light.dev"];

  function storedChoice() {
    try {
      return localStorage.getItem(KEY);
    } catch (e) {
      return null;
    }
  }

  function store(value) {
    try {
      localStorage.setItem(KEY, value);
    } catch (e) {
      // Storage unavailable (private mode, blocked site data, ...): the choice just
      // won't be remembered, and the banner shows again next visit. Not fatal.
    }
  }

  function eraseCookie(name, domain) {
    var expired = "; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    document.cookie = name + "=" + expired + (domain ? "; domain=" + domain : "");
  }

  function eraseAnalyticsCookies() {
    var i, j, name, eqPos, existing;
    // The two names GA4 is configured to use here.
    for (i = 0; i < GA_COOKIE_NAMES.length; i++) {
      for (j = 0; j < COOKIE_DOMAINS.length; j++) {
        eraseCookie(GA_COOKIE_NAMES[i], COOKIE_DOMAINS[j]);
      }
    }
    // Also catch any other _ga/_ga_* cookie actually present (e.g. a second GA4
    // property added to the container later, before this list is updated to match).
    existing = document.cookie.split(";");
    for (i = 0; i < existing.length; i++) {
      eqPos = existing[i].indexOf("=");
      name = (eqPos > -1 ? existing[i].substring(0, eqPos) : existing[i]).replace(/^\s+/, "");
      if (/^_ga(_.*)?$/.test(name)) {
        for (j = 0; j < COOKIE_DOMAINS.length; j++) {
          eraseCookie(name, COOKIE_DOMAINS[j]);
        }
      }
    }
  }

  function grantAnalytics() {
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", { analytics_storage: "granted" });
    }
  }

  function denyAnalytics() {
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", { analytics_storage: "denied" });
    }
    // Revoking consent must stop analytics for the rest of this page view too, not
    // just on the next load: delete any cookie GA already set during an earlier Accept.
    eraseAnalyticsCookies();
  }

  function banner() {
    return document.getElementById("consent-banner");
  }

  // The banner is `position: fixed` at the bottom of the viewport (site.css), so it
  // would otherwise sit on top of whatever is there, including the hero's CTAs on
  // mobile. Reserve exactly its own height as bottom padding on <body>, read from the
  // banner's own rendered height (so it stays correct across locales, viewport widths
  // and text reflow) rather than a guessed constant. The `has-consent-banner` class is
  // what site.css keys the padding off; `--consent-banner-h` is the amount.
  function reserveSpace(show) {
    var root = document.documentElement;
    if (show) {
      var el = banner();
      var h = el ? el.offsetHeight : 0;
      root.style.setProperty("--consent-banner-h", h + "px");
      root.classList.add("has-consent-banner");
    } else {
      root.classList.remove("has-consent-banner");
      root.style.removeProperty("--consent-banner-h");
    }
  }

  function showBanner() {
    var el = banner();
    if (el) {
      el.hidden = false;
      reserveSpace(true);
    }
  }

  function hideBanner() {
    var el = banner();
    if (el) el.hidden = true;
    reserveSpace(false);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var accept = document.getElementById("consent-accept");
    var decline = document.getElementById("consent-decline");
    var reopen = document.getElementById("consent-settings-link");

    // A rotation or a resize (including the mobile URL-bar show/hide that changes
    // viewport height) can change the banner's own height (e.g. its text rewraps),
    // which would leave the reserved space wrong. Re-measure while it's showing.
    window.addEventListener("resize", function () {
      var el = banner();
      if (el && !el.hidden) reserveSpace(true);
    });

    if (accept) {
      accept.addEventListener("click", function () {
        store("accepted");
        grantAnalytics();
        hideBanner();
      });
    }
    if (decline) {
      decline.addEventListener("click", function () {
        store("declined");
        denyAnalytics();
        hideBanner();
      });
    }
    if (reopen) {
      reopen.addEventListener("click", function () {
        showBanner();
      });
    }

    if (!storedChoice()) {
      showBanner();
    }
  });
})();
