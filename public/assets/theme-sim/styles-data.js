// The kit's ThemeStyles.json (Sources/MarsDawnThemes/Resources/ThemeStyles.json): the CSS
// fragments each enum option value contributes, and the composed foreground/background pairs the
// shared stylesheet and each option value draw (design §4.3/§6.3).
//
// This used to embed a hand-kept copy of that data. It now has exactly one source: the vendored
// tree WA's scripts/sync_theme_kit.py writes to vendor/kit-themes/<tag>/ThemeStyles.json, which
// build_pages.py's sync_theme_kit_assets_into_public() copies, unmodified, to
// public/assets/theme-sim/kit/ThemeStyles.json -- the only copy the browser can fetch, since it
// can never read vendor/. scripts/check_theme_sim.mjs (Node) reads the vendored file directly.
//
// FRAGMENTS/SHARED_PAIRS/OPTION_PAIRS start empty and are set once, by setThemeStyles/loadThemeStyles
// below, before anything in generator.js or validator.js runs. They're `let` bindings so that a
// module which only ever does `import { FRAGMENTS } from "./styles-data.js"` sees this module's
// own later reassignment (a live binding), without re-importing.

export let FRAGMENTS = {};
export let SHARED_PAIRS = [];
export let OPTION_PAIRS = {};

/** Sets this module's data from an already-parsed ThemeStyles.json object
 * (`{ fragments, pairs: { shared, options } }`). Used by Node (scripts/check_theme_sim.mjs), which
 * reads the vendored file straight off disk instead of fetching it. */
export function setThemeStyles(data) {
  FRAGMENTS = data.fragments;
  SHARED_PAIRS = data.pairs.shared;
  OPTION_PAIRS = data.pairs.options;
}

/** Fetches and sets this module's data from a URL (the browser's own copy, under
 * ./kit/ThemeStyles.json -- see build_pages.py's sync_theme_kit_assets_into_public()). */
export async function loadThemeStyles(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`loadThemeStyles: ${url} -> HTTP ${res.status}`);
  setThemeStyles(await res.json());
}
