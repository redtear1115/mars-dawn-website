// Pure logic for which theme id the simulator's live-preview wrapper should scope to (mars-dawn-
// website PR #147 round 2, verifier item (c)): the generator's CSS is scoped to the theme's own id
// (`[data-theme="<id>"]`, rescoped to `.sim-preview[data-theme="<id>"]`), so the preview element's
// own `data-theme` attribute has to carry that same id -- a hard-coded placeholder id (e.g. "sim")
// never matches any real theme's generated rules, so nothing the designer picks ever visibly
// applies. DOM-free on purpose, so scripts/check_theme_sim.mjs can exercise it without a browser.

/** The id the preview wrapper's `data-theme` should show, given the latest validation report
 * (validator.js's `{ issues, theme }`) and the id it currently shows.
 *
 * Returns the validated theme's own, normalised id when the report validates clean; otherwise
 * returns `previousId` unchanged. An invalid or empty id in the form must never invent a new scope
 * to switch the preview to -- there is no generated CSS for an id that never validated, so keeping
 * the last id that did validate leaves the preview showing that theme (if its stylesheet is still
 * adopted) rather than snapping to an empty, permanently-unstyled scope on every keystroke. */
export function previewThemeIdFor(report, previousId) {
  return report.theme ? report.theme.document.id : previousId;
}
