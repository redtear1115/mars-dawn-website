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

  function grantAnalytics() {
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", { analytics_storage: "granted" });
    }
  }

  function banner() {
    return document.getElementById("consent-banner");
  }

  function showBanner() {
    var el = banner();
    if (el) el.hidden = false;
  }

  function hideBanner() {
    var el = banner();
    if (el) el.hidden = true;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var accept = document.getElementById("consent-accept");
    var decline = document.getElementById("consent-decline");
    var reopen = document.getElementById("consent-settings-link");

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
