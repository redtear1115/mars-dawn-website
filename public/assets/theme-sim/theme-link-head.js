// The theme simulator's hand-off link intake (plan PLAN-web-theme-tuning W2b). A classic,
// synchronous, external script: build_pages.py puts it in /themes/new/'s <head>, in every locale,
// right after <meta charset> and BEFORE the Consent Mode default and the GTM loader, so it runs
// before Google Tag Manager or anything it loads can see the address bar or wrap History.
// Never inline (the CSP's script-src is 'self' plus two hashed scripts only) and never a module
// (a module is deferred, which would let GTM run first). scripts/check_theme_link_head.py holds
// every locale's page to that order.
//
// A hand-off link is `/themes/new/#theme=<payload>`: the payload is the theme's minified JSON as
// UTF-8, in base64url (RFC 4648 §5: A-Z a-z 0-9 - _), without padding. This script:
//   (a) keeps the pristine History.prototype.replaceState before anything can wrap it;
//   (b) reads a `#theme=` fragment, decodes it to bytes (or a refusal) held in this closure, and
//       strips the fragment from the address bar;
//   (c) does the same for a later `#theme=` (a second link pasted into the same tab: popstate and
//       hashchange, no reload), and keeps those events from reaching any later listener (GTM's
//       history listener among them) while they carry a theme link;
//   (d) exposes one global function, takeThemeLinkPayload(onLater), which returns and clears the
//       queued result and registers the callback that receives later ones. The payload itself is
//       never a global and is never pushed to dataLayer.
// Any other fragment (the skip link's #main, say) is left exactly as it is.
//
// The bytes are not trusted: the simulator (app.js) sends them through theme-import.js's
// importThemeBytes, the same guarded path a dropped file takes. This script only enforces the
// link grammar and the size cap, before decoding anything.
//
// The two caps: MAX_DECODED_BYTES is validator.js's MAX_FILE_BYTES (16 * 1024), and
// MAX_ENCODED_LENGTH is ceil(MAX_FILE_BYTES * 4 / 3). This classic script can't import
// validator.js, so it carries the numbers as literals; scripts/check_theme_sim.mjs fails if either
// stops matching MAX_FILE_BYTES.
(function () {
  "use strict";

  var MAX_ENCODED_LENGTH = 21846;
  var MAX_DECODED_BYTES = 16384;
  var PREFIX = "#theme=";
  var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";

  /** Pure: a link payload (the text after `#theme=`) to `{ bytes }` (a Uint8Array) or
   * `{ error }` ("link.tooLarge" or "link.malformed"). Up to two trailing `=` are accepted and
   * ignored; the length cap is checked on what remains, before a single character is decoded. */
  function decodeThemeLinkPayload(payload) {
    if (typeof payload !== "string") return { error: "link.malformed" };
    var end = payload.length;
    for (var pad = 0; pad < 2 && end > 0 && payload.charCodeAt(end - 1) === 61; pad++) end--;
    if (end > MAX_ENCODED_LENGTH) return { error: "link.tooLarge" };
    if (end % 4 === 1) return { error: "link.malformed" };
    var values = [];
    for (var i = 0; i < end; i++) {
      var v = ALPHABET.indexOf(payload.charAt(i));
      if (v < 0) return { error: "link.malformed" };
      values.push(v);
    }
    var length = Math.floor((end * 3) / 4);
    if (length > MAX_DECODED_BYTES) return { error: "link.tooLarge" };
    var bytes = new Uint8Array(length);
    var out = 0;
    for (var j = 0; j < end; j += 4) {
      var n = (values[j] << 18) | ((values[j + 1] || 0) << 12) | ((values[j + 2] || 0) << 6) | (values[j + 3] || 0);
      if (out < length) bytes[out++] = (n >> 16) & 255;
      if (out < length) bytes[out++] = (n >> 8) & 255;
      if (out < length) bytes[out++] = n & 255;
    }
    return { bytes: bytes };
  }

  var win = window;
  var historyProto = win.History && win.History.prototype;
  var replaceState = historyProto && historyProto.replaceState;
  var queued = null;
  var onLater = null;

  /** The fragment of a URL string, including its `#`, or "". */
  function fragmentOf(url) {
    var i = typeof url === "string" ? url.indexOf("#") : -1;
    return i < 0 ? "" : url.slice(i);
  }

  function isThemeFragment(fragment) {
    return typeof fragment === "string" && fragment.slice(0, PREFIX.length) === PREFIX;
  }

  /** The address bar without its fragment, through the pristine replaceState: no navigation, no
   * popstate/hashchange, and nothing that wrapped History later is called. */
  function stripFragment() {
    if (typeof replaceState !== "function") return;
    var loc = win.location;
    try {
      replaceState.call(win.history, win.history.state, "", loc.pathname + loc.search);
    } catch (e) {
      // Leave the address bar alone rather than navigate.
    }
  }

  function deliver(result) {
    if (onLater) {
      try {
        onLater(result);
      } catch (e) {
        // The simulator's own error; the payload is not kept.
      }
    } else {
      queued = result;
    }
  }

  /** Takes a `#theme=` fragment from the address bar, if there is one. */
  function takeFromAddressBar() {
    var fragment = win.location.hash;
    if (!isThemeFragment(fragment)) return false;
    var result = decodeThemeLinkPayload(fragment.slice(PREFIX.length));
    stripFragment();
    deliver(result);
    return true;
  }

  function onNavigation(event) {
    var took = takeFromAddressBar();
    // A hashchange that fires after popstate already took the link still names it in newURL.
    if (took || isThemeFragment(fragmentOf(event && event.newURL))) {
      if (event && typeof event.stopImmediatePropagation === "function") event.stopImmediatePropagation();
    }
  }

  function takeThemeLinkPayload(callback) {
    if (typeof callback === "function") onLater = callback;
    var result = queued;
    queued = null;
    return result;
  }
  // For scripts/check_theme_sim.mjs: the pure decoder and the two caps it enforces.
  takeThemeLinkPayload.decode = decodeThemeLinkPayload;
  takeThemeLinkPayload.limits = { encodedLength: MAX_ENCODED_LENGTH, decodedBytes: MAX_DECODED_BYTES };
  win.takeThemeLinkPayload = takeThemeLinkPayload;

  // Capture phase and registered before any other script on the page, so these run first.
  win.addEventListener("popstate", onNavigation, true);
  win.addEventListener("hashchange", onNavigation, true);
  takeFromAddressBar();
})();
