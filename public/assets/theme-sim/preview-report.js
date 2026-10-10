// What the simulator's live preview may draw, and when a theme may be submitted (website#150,
// plan PLAN-web-theme-tuning W1). DOM-free on purpose, so scripts/check_theme_sim.mjs tests exactly
// what the page runs.
//
// The preview no longer waits for a fully valid theme. A draft is drawn whenever its *structure*
// is sound: it decodes, its schema version is 1, every colour is #RRGGBB and every bounded number
// is in range. Identity, scenario, completeness and contrast problems are still listed, and still
// block Submit, but they never blank the preview. The CSS is generated under a constant scope id
// (PREVIEW_ID), never the draft's own id, so nothing the designer types as an id reaches the CSS.
//
// `validate()` (validator.js) is untouched and stays the only gate for Submit; this module only
// decides what the preview may show.

import { decodeThemeText, checkStyle, colorFields, checkContrast } from "./validator.js";
import { isHexColor } from "./grammar.js";
import { resolvePalette, MissingFallback } from "./palette.js";
import { stylesheetFor, GeneratorRefusal } from "./generator.js";
import { rescopeCSS, SIM_PREVIEW_WRAPPER } from "./rescope.js";

/** The scope id every preview stylesheet is generated under, and the preview boxes' data-theme.
 * Matches the id grammar, so the generator accepts it. */
export const PREVIEW_ID = "preview";

/** Rule ids that stop the preview from drawing the current draft: anything that means the
 * document didn't decode, or that a value which reaches the CSS isn't one the generator may write.
 * Every other rule id (id.pattern, version.pattern, locale.key, text.*, author.github,
 * license.pattern, scenarios.*, option.role, palette.incomplete, contrast.*) is advisory: listed,
 * and blocking Submit through validate(), but the preview still draws. */
export const PREVIEW_BLOCKING_RULES = Object.freeze([
  "file.tooLarge",
  "json.malformed",
  "json.duplicateKey",
  "json.tooDeep",
  "schema.unknownKey",
  "schema.missing",
  "schema.type",
  "schema.value",
  "schema.version",
  "color.hex",
  "number.range",
  "option.gradientStops",
]);

function blocks(rule) {
  return PREVIEW_BLOCKING_RULES.includes(rule);
}

/** The preview's view of a theme.json text.
 *
 * `fallback` is Dawn's resolved `{ light, dark }` palettes (the same ones given to
 * validator.js's setDawnFallback), used for a palette that leaves out syntax/diagram.
 *
 * Returns `{ rule, previewable, document, light, dark, advisories }`: `rule` is the first blocking
 * rule id or null; `document` is the normalised document (numbers snapped as validate() snaps
 * them); `advisories` are the contrast issues, computed whatever the identity or completeness
 * issues are (empty when the colours themselves aren't valid). */
export function previewReport(text, { fallback } = {}) {
  const none = { previewable: false, document: null, light: null, dark: null, advisories: [] };
  const decoded = decodeThemeText(text);
  if (decoded.issue) return { rule: decoded.issue.rule, ...none };
  const doc = decoded.document;
  if (doc.schemaVersion !== 1) return { rule: "schema.version", ...none };

  const issues = [];
  let colorsValid = true;
  for (const [mode, colors] of [["light", doc.light], ["dark", doc.dark]]) {
    for (const [field, value] of colorFields(colors)) {
      if (!isHexColor(value)) {
        colorsValid = false;
        issues.push({ rule: "color.hex", path: `${mode}.${field}` });
      }
    }
  }
  const normalized = { ...doc };
  if (doc.style) normalized.style = checkStyle(doc.style, issues);

  let light = null;
  let dark = null;
  let advisories = [];
  if (colorsValid) {
    try {
      light = resolvePalette(doc.light, fallback?.light);
      dark = resolvePalette(doc.dark, fallback?.dark);
      advisories = checkContrast(normalized.style, doc.scenarios, light, dark);
    } catch (e) {
      if (!(e instanceof MissingFallback)) throw e;
      issues.push({ rule: "schema.missing", path: "light" });
      light = null;
      dark = null;
    }
  }

  const first = issues.find((i) => blocks(i.rule));
  const rule = first ? first.rule : null;
  const previewable = rule === null;
  return {
    rule,
    previewable,
    document: previewable ? normalized : null,
    light: previewable ? light : null,
    dark: previewable ? dark : null,
    advisories,
  };
}

// --- The scope guard ----------------------------------------------------------------------------

/** True when one rescoped selector can only match the preview wrapper or something inside it:
 * `.sim-preview`, optionally followed by attribute compounds (`[data-theme="…"]`,
 * `[data-appearance="dark"]`), then either nothing or a descendant/child step. Refuses a longer
 * class name (`.sim-previewX`) and the sibling combinators (`.sim-preview ~ *`, `.sim-preview + *`),
 * which would reach the controls, the messages panel or Submit. */
export function selectorStaysInside(selector) {
  const s = selector.trim();
  if (!s.startsWith(SIM_PREVIEW_WRAPPER)) return false;
  let i = SIM_PREVIEW_WRAPPER.length;
  while (s[i] === "[") {
    const close = s.indexOf("]", i);
    if (close === -1) return false;
    i = close + 1;
  }
  if (i === s.length) return true;
  const rest = s.slice(i);
  const step = rest.match(/^(\s+>\s*|\s*>\s*|\s+)/);
  if (!step) return false; // e.g. `.sim-previewX`, `.sim-preview:hover`, `.sim-preview.foo`
  const after = rest.slice(step[0].length);
  if (after === "") return false;
  if (after[0] === "~" || after[0] === "+" || after[0] === ">" || after[0] === ",") return false;
  return true;
}

/** Throws a GeneratorRefusal("escapedScope") unless every selector in `css` (rescopeCSS output:
 * one rule per line start) stays inside the preview wrapper. */
export function assertScopedToPreview(css) {
  for (const line of css.split("\n")) {
    const brace = line.indexOf("{");
    if (brace === -1) continue;
    const header = line.slice(0, brace);
    if (header.trim() === "") throw new GeneratorRefusal("escapedScope", line);
    for (const selector of header.split(",")) {
      if (!selectorStaysInside(selector)) throw new GeneratorRefusal("escapedScope", selector.trim());
    }
  }
}

// --- Generating the preview's stylesheet ------------------------------------------------------

/** The generator's own `{ variables, rules }` for a previewable report, scoped to PREVIEW_ID.
 * `generate` defaults to the real generator; check_theme_sim.mjs passes a refusing one to test the
 * Submit decision. Throws whatever the generator throws. */
export function previewThemeCSS(report, generate = stylesheetFor) {
  if (!report.previewable) throw new Error("previewThemeCSS: report is not previewable");
  return generate({ document: { ...report.document, id: PREVIEW_ID }, light: report.light, dark: report.dark });
}

/** The stylesheet text the page adopts: the preview CSS rescoped under .sim-preview and checked by
 * the scope guard. Throws a GeneratorRefusal (or the generator's own) instead of returning CSS
 * that escapes the preview. */
export function previewSheetText(report, generate = stylesheetFor) {
  const { variables, rules } = previewThemeCSS(report, generate);
  const rescoped = rescopeCSS(variables, SIM_PREVIEW_WRAPPER) + rescopeCSS(rules, SIM_PREVIEW_WRAPPER);
  assertScopedToPreview(rescoped);
  return rescoped;
}

/** Runs the preview path for one draft: `{ css, generatorRefused }`. `css` is the sheet to adopt,
 * or null when the draft isn't drawn. `generatorRefused` is true when validate() reports no issues
 * but the preview path still won't draw it (the generator or the scope guard refused), the one
 * case where a theme that passes every check must not be submitted. */
export function previewOutcome(validateReport, report, generate = stylesheetFor) {
  const clean = validateReport.issues.length === 0;
  if (!report.previewable) return { css: null, generatorRefused: clean };
  try {
    return { css: previewSheetText(report, generate), generatorRefused: false };
  } catch {
    return { css: null, generatorRefused: clean };
  }
}

/** Whether Submit may open the issue form: validate() is clean and the preview path didn't refuse. */
export function submitDecision(validateReport, outcome) {
  return validateReport.issues.length === 0 && !outcome.generatorRefused;
}

/** The issues the panel lists: validate()'s own, then any contrast advisory validate() didn't
 * report (validate() skips contrast while earlier issues exist), de-duplicated by (path, rule). */
export function panelIssues(validateReport, report) {
  const seen = new Set(validateReport.issues.map((i) => `${i.path}\u0000${i.rule}`));
  const out = [...validateReport.issues];
  for (const a of report.advisories) {
    const key = `${a.path}\u0000${a.rule}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(a);
  }
  return out;
}
