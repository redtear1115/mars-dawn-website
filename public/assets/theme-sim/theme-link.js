// Copy link's half of the hand-off link (plan PLAN-web-theme-tuning W2b). DOM-free, so
// scripts/check_theme_sim.mjs tests exactly what the page runs. The other half, reading a link,
// is theme-link-head.js, a classic script that runs in <head> before analytics loads.
//
// Link grammar: `<origin><path>#theme=<payload>`, the payload being the theme's minified JSON
// (`JSON.stringify(state)`) as UTF-8 in base64url (RFC 4648 §5: `+` -> `-`, `/` -> `_`), without
// padding. No query: the link keeps the page's own path, and so its locale.

/** The base64url payload (no padding) of one JSON text. */
export function encodeThemeLinkPayload(text) {
  const bytes = new TextEncoder().encode(text);
  let binary = "";
  for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

/** The hand-off link for a theme state, on the page at `origin` + `pathname`. */
export function themeLink(origin, pathname, state) {
  return `${origin}${pathname}#theme=${encodeThemeLinkPayload(JSON.stringify(state))}`;
}
