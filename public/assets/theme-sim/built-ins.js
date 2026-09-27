// The four built-in themes' theme.json (Sources/MarsDawnThemes/Resources/Themes/<id>/theme.json).
// Used to seed the simulator's "start from a built-in" list and to resolve Dawn's palette as the
// fallback for a theme that leaves out `syntax`/`diagram` (design §4.2, §6.2).
//
// This used to embed the four files' text verbatim. It now has exactly one source, the same
// vendored tree styles-data.js reads from -- see that file's header. BUILT_IN_THEME_JSON starts
// empty and is set once, by setBuiltIns/loadBuiltIns below, before anything reads it.

export const BUILT_IN_ORDER = ["dawn", "classic", "modern", "vivid"];
export let BUILT_IN_THEME_JSON = {};

/** Sets this module's data from `{ id: theme.json text }`. Used by Node
 * (scripts/check_theme_sim.mjs), which reads the vendored files straight off disk. */
export function setBuiltIns(map) {
  BUILT_IN_THEME_JSON = map;
}

/** Fetches each built-in's theme.json as text from `${baseURL}<id>.json` (the browser's own copy,
 * under ./kit/themes/ -- see build_pages.py's sync_theme_kit_assets_into_public()). */
export async function loadBuiltIns(baseURL) {
  const entries = await Promise.all(
    BUILT_IN_ORDER.map(async (id) => {
      const res = await fetch(new URL(`${id}.json`, baseURL));
      if (!res.ok) throw new Error(`loadBuiltIns: ${id} -> HTTP ${res.status}`);
      return [id, await res.text()];
    })
  );
  setBuiltIns(Object.fromEntries(entries));
}
