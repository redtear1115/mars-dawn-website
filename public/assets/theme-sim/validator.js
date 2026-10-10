// Port of ThemeValidator.swift + ThemeDocument.swift/ThemeStyle.swift's strict decoding (kit
// origin/release-0.6.1, f1c66e16509e). Not the gate (the kit's Swift validator is); a convenience for
// instant feedback, kept honest by scripts/check_theme_sim.mjs's parity check against the kit's
// own fixtures (design §6, plan-website-104 W1).
//
// A decode-level problem (unknown key, missing field, wrong type, bad enum value, malformed/too-
// deep/duplicate-key JSON) short-circuits to a single issue, exactly as the kit's JSONDecoder-based
// strict decoding does. Business-rule problems (id pattern, colour hex, numeric range, contrast,
// …) accumulate, one issue per problem, after a document decodes structurally.

import { scanJSONStructure, JSONScanError } from "./json-scan.js";
import * as Grammar from "./grammar.js";
import { checkDisplayText, quote as quoteText, NAME_LIMIT, SUMMARY_LIMIT, AUTHOR_NAME_LIMIT, PROBLEM_SUMMARY } from "./text.js";
import { THEME_NUMBERS, snapped as snapNumber, cssNumber } from "./numbers.js";
import { resolvePalette, colorFor, MissingFallback } from "./palette.js";
import { SHARED_PAIRS, OPTION_PAIRS } from "./styles-data.js";
import { ratio, format as formatRatio } from "./contrast.js";
import { fontStackFor } from "./generator.js";

export const MAX_FILE_BYTES = 16 * 1024;

class DecodeFailure extends Error {
  constructor(rule, path, message) {
    super(message);
    this.rule = rule;
    this.path = path;
  }
}
function fail(rule, path, message) {
  throw new DecodeFailure(rule, path, message);
}
function joinPath(path, key) {
  return path ? `${path}.${quoteText(key)}` : quoteText(key);
}

function requireKeys(obj, allowed, path) {
  for (const key of Object.keys(obj)) {
    if (!allowed.includes(key)) fail("schema.unknownKey", path, `unknown key \`${quoteText(key)}\``);
  }
}
function reqField(obj, key, path) {
  if (!(key in obj) || obj[key] === undefined) fail("schema.missing", joinPath(path, key), "is required");
  return obj[key];
}
function reqString(obj, key, path) {
  const v = reqField(obj, key, path);
  if (typeof v !== "string") fail("schema.type", joinPath(path, key), "has the wrong type");
  return v;
}
function optString(obj, key, path) {
  if (!(key in obj) || obj[key] === undefined) return undefined;
  return reqString(obj, key, path);
}
function reqNumber(obj, key, path) {
  const v = reqField(obj, key, path);
  if (typeof v !== "number") fail("schema.type", joinPath(path, key), "has the wrong type");
  return v;
}
function optNumber(obj, key, path) {
  if (!(key in obj) || obj[key] === undefined) return undefined;
  return reqNumber(obj, key, path);
}
function optBool(obj, key, path) {
  if (!(key in obj) || obj[key] === undefined) return undefined;
  const v = obj[key];
  if (typeof v !== "boolean") fail("schema.type", joinPath(path, key), "has the wrong type");
  return v;
}
function asObject(v, path) {
  if (typeof v !== "object" || v === null || Array.isArray(v)) fail("schema.type", path, "has the wrong type");
  return v;
}
function asArray(v, path) {
  if (!Array.isArray(v)) fail("schema.type", path, "has the wrong type");
  return v;
}

const PALETTE_ROLE_VALUES = new Set([
  "background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote",
  "keyword", "string", "comment", "number", "function", "type",
]);
function decodePaletteRole(v, path) {
  if (typeof v !== "string") fail("schema.type", path, "has the wrong type");
  if (!PALETTE_ROLE_VALUES.has(v)) fail("schema.value", path, "is not one of the allowed values");
  return v;
}

function decodeLocalizedText(v, path) {
  const obj = asObject(v, path);
  const strings = {};
  for (const [k, val] of Object.entries(obj)) {
    if (typeof val !== "string") fail("schema.type", joinPath(path, k), "has the wrong type");
    strings[k] = val;
  }
  if (strings.en === undefined) fail("schema.missing", path, "needs an `en` entry");
  return strings;
}

function decodeColors(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote", "syntax", "diagram"], path);
  const out = {};
  for (const key of ["background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote"]) {
    out[key] = reqString(obj, key, path);
  }
  if (obj.syntax !== undefined) {
    const sp = joinPath(path, "syntax");
    const so = asObject(obj.syntax, sp);
    requireKeys(so, ["keyword", "string", "comment", "number", "function", "type"], sp);
    out.syntax = {};
    for (const key of ["keyword", "string", "comment", "number", "function", "type"]) out.syntax[key] = reqString(so, key, sp);
  }
  if (obj.diagram !== undefined) {
    const dp = joinPath(path, "diagram");
    const dobj = asObject(obj.diagram, dp);
    requireKeys(dobj, ["node", "nodeBorder", "text", "line", "secondary", "tertiary", "note"], dp);
    out.diagram = {};
    for (const key of ["node", "nodeBorder", "text", "line", "secondary", "tertiary", "note"]) out.diagram[key] = reqString(dobj, key, dp);
  }
  return out;
}

function decodeAuthor(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["name", "github"], path);
  return { name: reqString(obj, "name", path), github: optString(obj, "github", path) };
}

// --- Style, and its discriminated-union option values ---------------------------------------

function decodeDiscriminated(v, path, allowedByType, build) {
  const obj = asObject(v, path);
  const type = reqString(obj, "type", path);
  const allowed = allowedByType[type];
  if (!allowed) fail("schema.value", joinPath(path, "type"), "is not one of the allowed values");
  requireKeys(obj, ["type", ...allowed], path);
  return build(type, obj, path);
}

function decodeH1Decoration(v, path) {
  return decodeDiscriminated(v, path, { rule: [], none: [], shortRule: ["color"], gradientBar: ["from", "to"] }, (type, obj, p) => {
    if (type === "shortRule") return { type, color: decodePaletteRole(reqField(obj, "color", p), joinPath(p, "color")) };
    if (type === "gradientBar") {
      return {
        type,
        from: decodePaletteRole(reqField(obj, "from", p), joinPath(p, "from")),
        to: decodePaletteRole(reqField(obj, "to", p), joinPath(p, "to")),
      };
    }
    return { type };
  });
}
function decodeH2Decoration(v, path) {
  return decodeDiscriminated(v, path, { rule: [], none: [], dot: ["color"] }, (type, obj, p) => {
    if (type === "dot") return { type, color: decodePaletteRole(reqField(obj, "color", p), joinPath(p, "color")) };
    return { type };
  });
}
function decodeBlockquoteStyle(v, path) {
  return decodeDiscriminated(v, path, { bar: ["width"], panel: [] }, (type, obj, p) => {
    if (type === "bar") return { type, width: optNumber(obj, "width", p) };
    return { type };
  });
}
function decodeHrStyle(v, path) {
  return decodeDiscriminated(v, path, { line: ["color", "thickness"], shortCentered: ["color"], gradient: ["colors"] }, (type, obj, p) => {
    if (type === "line") {
      return {
        type,
        color: obj.color !== undefined ? decodePaletteRole(obj.color, joinPath(p, "color")) : undefined,
        thickness: optNumber(obj, "thickness", p),
      };
    }
    if (type === "shortCentered") return { type, color: decodePaletteRole(reqField(obj, "color", p), joinPath(p, "color")) };
    if (type === "gradient") {
      const arr = asArray(reqField(obj, "colors", p), joinPath(p, "colors"));
      return { type, colors: arr.map((c, i) => decodePaletteRole(c, joinPath(p, "colors") + `[${i}]`)) };
    }
    return { type };
  });
}
function decodeTableHeader(v, path) {
  return decodeDiscriminated(v, path, { surface: [], accentRule: ["color"], filled: ["background", "text", "border"] }, (type, obj, p) => {
    if (type === "accentRule") return { type, color: decodePaletteRole(reqField(obj, "color", p), joinPath(p, "color")) };
    if (type === "filled") {
      return {
        type,
        background: decodePaletteRole(reqField(obj, "background", p), joinPath(p, "background")),
        text: decodePaletteRole(reqField(obj, "text", p), joinPath(p, "text")),
        border: obj.border !== undefined ? decodePaletteRole(obj.border, joinPath(p, "border")) : undefined,
      };
    }
    return { type };
  });
}

function decodeH1(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["size", "letterSpacing", "align", "decoration"], path);
  const align = optString(obj, "align", path);
  if (align !== undefined && align !== "left" && align !== "center") fail("schema.value", joinPath(path, "align"), "is not one of the allowed values");
  return {
    size: optNumber(obj, "size", path),
    letterSpacing: optNumber(obj, "letterSpacing", path),
    align,
    decoration: obj.decoration !== undefined ? decodeH1Decoration(obj.decoration, joinPath(path, "decoration")) : undefined,
  };
}
function decodeH2(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["letterSpacing", "decoration", "italic"], path);
  return {
    letterSpacing: optNumber(obj, "letterSpacing", path),
    decoration: obj.decoration !== undefined ? decodeH2Decoration(obj.decoration, joinPath(path, "decoration")) : undefined,
    italic: optBool(obj, "italic", path),
  };
}
function decodeBlockquote(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["style", "italic"], path);
  return {
    style: obj.style !== undefined ? decodeBlockquoteStyle(obj.style, joinPath(path, "style")) : undefined,
    italic: optBool(obj, "italic", path),
  };
}
function decodeHr(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["style"], path);
  return { style: obj.style !== undefined ? decodeHrStyle(obj.style, joinPath(path, "style")) : undefined };
}
function decodeTable(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["header", "verticalRules", "rounded"], path);
  return {
    header: obj.header !== undefined ? decodeTableHeader(obj.header, joinPath(path, "header")) : undefined,
    verticalRules: optBool(obj, "verticalRules", path),
    rounded: optBool(obj, "rounded", path),
  };
}
function decodeLinkOptions(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["underline"], path);
  return { underline: optBool(obj, "underline", path) };
}
function decodeSyntaxOptions(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, ["boldKeywords"], path);
  return { boldKeywords: optBool(obj, "boldKeywords", path) };
}

const STYLE_KEYS = ["bodySize", "lineHeight", "headingWeight", "radius", "maxWidth", "h1", "h2", "blockquote", "hr", "table",
  "listMarker", "inlineCode", "link", "syntax"];

function decodeStyle(v, path) {
  const obj = asObject(v, path);
  requireKeys(obj, STYLE_KEYS, path);
  return {
    bodySize: optNumber(obj, "bodySize", path),
    lineHeight: optNumber(obj, "lineHeight", path),
    headingWeight: optNumber(obj, "headingWeight", path),
    radius: optNumber(obj, "radius", path),
    maxWidth: optNumber(obj, "maxWidth", path),
    h1: obj.h1 !== undefined ? decodeH1(obj.h1, joinPath(path, "h1")) : undefined,
    h2: obj.h2 !== undefined ? decodeH2(obj.h2, joinPath(path, "h2")) : undefined,
    blockquote: obj.blockquote !== undefined ? decodeBlockquote(obj.blockquote, joinPath(path, "blockquote")) : undefined,
    hr: obj.hr !== undefined ? decodeHr(obj.hr, joinPath(path, "hr")) : undefined,
    table: obj.table !== undefined ? decodeTable(obj.table, joinPath(path, "table")) : undefined,
    listMarker: obj.listMarker !== undefined ? decodePaletteRole(obj.listMarker, joinPath(path, "listMarker")) : undefined,
    inlineCode: obj.inlineCode !== undefined ? decodePaletteRole(obj.inlineCode, joinPath(path, "inlineCode")) : undefined,
    link: obj.link !== undefined ? decodeLinkOptions(obj.link, joinPath(path, "link")) : undefined,
    syntax: obj.syntax !== undefined ? decodeSyntaxOptions(obj.syntax, joinPath(path, "syntax")) : undefined,
  };
}

const DOCUMENT_KEYS = ["schemaVersion", "id", "version", "name", "summary", "fontDesign", "scenarios", "author", "license", "light", "dark", "style"];
const SCENARIOS = ["agent-review", "technical-docs", "formal-output", "notes-sharing"];
const FONT_DESIGNS = ["sans", "serif", "rounded"];

/** Decodes a theme.json object (already JSON.parsed) into a ThemeDocument-shaped JS object, or
 * throws a single DecodeFailure, mirroring the kit's strict, order-sensitive decode. */
export function decodeThemeDocument(raw) {
  const obj = asObject(raw, "");
  requireKeys(obj, DOCUMENT_KEYS, "");
  const schemaVersion = reqNumber(obj, "schemaVersion", "");
  const id = reqString(obj, "id", "");
  const version = reqString(obj, "version", "");
  const name = decodeLocalizedText(reqField(obj, "name", ""), "name");
  const summary = decodeLocalizedText(reqField(obj, "summary", ""), "summary");
  const fontDesignRaw = reqString(obj, "fontDesign", "");
  if (!FONT_DESIGNS.includes(fontDesignRaw)) fail("schema.value", "fontDesign", "is not one of the allowed values");
  const scenariosArr = asArray(reqField(obj, "scenarios", ""), "scenarios");
  const scenarios = scenariosArr.map((s, i) => {
    if (typeof s !== "string" || !SCENARIOS.includes(s)) fail("schema.value", `scenarios[${i}]`, "is not one of the allowed values");
    return s;
  });
  const author = obj.author !== undefined ? decodeAuthor(obj.author, "author") : undefined;
  const license = optString(obj, "license", "");
  const light = decodeColors(reqField(obj, "light", ""), "light");
  const dark = decodeColors(reqField(obj, "dark", ""), "dark");
  const style = obj.style !== undefined ? decodeStyle(obj.style, "style") : undefined;
  return { schemaVersion, id, version, name, summary, fontDesign: fontDesignRaw, scenarios, author, license, light, dark, style };
}

// --- Style number snapping --------------------------------------------------------------------

function snap(value, name, path, issues) {
  if (value === undefined) return undefined;
  const s = snapNumber(name, value);
  if (s === null) {
    const { range, step } = THEME_NUMBERS[name];
    issues.push({
      rule: "number.range", path,
      message: `must be a number from ${cssNumber(range[0])} to ${cssNumber(range[1])} (in steps of ${cssNumber(step)})`,
    });
    return value;
  }
  return s;
}

const INLINE_CODE_ROLES = new Set(["text", "keyword", "string", "comment", "number", "function", "type"]);

/** Snaps every bounded number in `style` (pushing `number.range`, `option.gradientStops` and
 * `option.role` issues as it goes) and returns the normalised copy. Exported for preview-report.js. */
export function checkStyle(style, issues) {
  const s = { ...style };
  s.bodySize = snap(style.bodySize, "bodySize", "style.bodySize", issues);
  s.lineHeight = snap(style.lineHeight, "lineHeight", "style.lineHeight", issues);
  s.headingWeight = snap(style.headingWeight, "headingWeight", "style.headingWeight", issues);
  s.radius = snap(style.radius, "radius", "style.radius", issues);
  s.maxWidth = snap(style.maxWidth, "maxWidth", "style.maxWidth", issues);
  if (style.h1) {
    s.h1 = { ...style.h1 };
    s.h1.size = snap(style.h1.size, "h1.size", "style.h1.size", issues);
    s.h1.letterSpacing = snap(style.h1.letterSpacing, "h1.letterSpacing", "style.h1.letterSpacing", issues);
  }
  if (style.h2) {
    s.h2 = { ...style.h2 };
    s.h2.letterSpacing = snap(style.h2.letterSpacing, "h2.letterSpacing", "style.h2.letterSpacing", issues);
  }
  if (style.blockquote?.style?.type === "bar") {
    s.blockquote = { ...style.blockquote, style: { ...style.blockquote.style } };
    s.blockquote.style.width = snap(style.blockquote.style.width, "blockquote.style.width", "style.blockquote.style.width", issues);
  }
  if (style.hr?.style?.type === "line") {
    s.hr = { ...style.hr, style: { ...style.hr.style } };
    s.hr.style.thickness = snap(style.hr.style.thickness, "hr.style.thickness", "style.hr.style.thickness", issues);
  } else if (style.hr?.style?.type === "gradient" && ![2, 3].includes(style.hr.style.colors.length)) {
    issues.push({ rule: "option.gradientStops", path: "style.hr.style.colors", message: "a gradient takes two or three colour roles" });
  }
  if (style.inlineCode !== undefined && !INLINE_CODE_ROLES.has(style.inlineCode)) {
    issues.push({ rule: "option.role", path: "style.inlineCode", message: "must be text or a syntax role (keyword, string, comment, number, function, type)" });
  }
  return s;
}

// --- Contrast -----------------------------------------------------------------------------------

function fieldName(token) {
  return ["keyword", "string", "comment", "number", "function", "type"].includes(token) ? `syntax.${token}` : token;
}

function selections(style) {
  const out = [];
  if (!style) return out;
  const h1d = style.h1?.decoration;
  if (h1d?.type === "none") out.push({ option: "h1Decoration", value: "none", params: {} });
  else if (h1d?.type === "shortRule") out.push({ option: "h1Decoration", value: "shortRule", params: { color: [h1d.color] } });
  else if (h1d?.type === "gradientBar") out.push({ option: "h1Decoration", value: "gradientBar", params: { from: [h1d.from], to: [h1d.to] } });
  const h2d = style.h2?.decoration;
  if (h2d?.type === "none") out.push({ option: "h2Decoration", value: "none", params: {} });
  else if (h2d?.type === "dot") out.push({ option: "h2Decoration", value: "dot", params: { color: [h2d.color] } });
  const bq = style.blockquote?.style;
  if (bq?.type === "bar") out.push({ option: "blockquoteStyle", value: "bar", params: {} });
  else if (bq?.type === "panel") out.push({ option: "blockquoteStyle", value: "panel", params: {} });
  const hr = style.hr?.style;
  if (hr?.type === "line") out.push({ option: "hrStyle", value: "line", params: { color: [hr.color ?? "border"] } });
  else if (hr?.type === "shortCentered") out.push({ option: "hrStyle", value: "shortCentered", params: { color: [hr.color] } });
  else if (hr?.type === "gradient") out.push({ option: "hrStyle", value: "gradient", params: { colors: hr.colors } });
  const th = style.table?.header;
  if (th?.type === "surface") out.push({ option: "tableHeader", value: "surface", params: {} });
  else if (th?.type === "accentRule") out.push({ option: "tableHeader", value: "accentRule", params: { color: [th.color] } });
  else if (th?.type === "filled") out.push({ option: "tableHeader", value: "filled", params: { background: [th.background], text: [th.text], border: [th.border ?? th.background] } });
  if (style.listMarker) out.push({ option: "listMarker", value: "role", params: { color: [style.listMarker] } });
  if (style.inlineCode) out.push({ option: "inlineCode", value: "role", params: { color: [style.inlineCode] } });
  return out;
}
function expandToken(token, params) {
  if (!(token.startsWith("{{") && token.endsWith("}}"))) return [token];
  const name = token.slice(2, -2);
  return params[name] ?? [];
}

/** Every composed pair a theme with `style` draws in one palette. */
function pairsFor(style, palette, dark) {
  const sels = selections(style);
  const replaced = new Set();
  const declared = [];
  for (const sel of sels) {
    const option = OPTION_PAIRS[sel.option]?.[sel.value];
    if (!option) continue;
    for (const r of option.replaces ?? []) replaced.add(r);
    for (const pair of option.pairs) {
      for (const fg of expandToken(pair.fg, sel.params)) {
        for (const bg of expandToken(pair.bg, sel.params)) declared.push({ ...pair, fg, bg });
      }
    }
  }
  const shared = SHARED_PAIRS.filter((p) => !replaced.has(p.id ?? "")).map((p) => ({ ...p, fg: p.fg, bg: p.bg }));
  const out = [];
  for (const pair of [...shared, ...declared]) {
    if (pair.modes && !pair.modes.includes(dark ? "dark" : "light")) continue;
    if (pair.kind === "nontext" && pair.fg === "border") continue;
    const fg = colorFor(palette, pair.fg, dark);
    const bg = colorFor(palette, pair.bg, dark);
    if (fg === undefined || bg === undefined) continue;
    out.push({
      id: pair.id, element: pair.element, fgToken: pair.fg, bgToken: pair.bg,
      foreground: fg, background: bg, kind: pair.kind, notice: !!pair.notice, baseline: !!pair.baseline, dark,
      threshold: pair.kind === "text" ? 4.5 : 3.0, ratio: ratio(fg, bg),
    });
  }
  return out;
}

function scenarioChecks(scenario) {
  switch (scenario) {
    case "agent-review": return { fields: ["text", "heading", "link", "accent", "muted"], against: "background", modes: [false, true] };
    case "technical-docs": return { fields: ["keyword", "string", "comment", "number", "function", "type"], against: "surface", modes: [false, true] };
    case "formal-output": return { fields: ["text", "heading", "link", "accent", "muted"], against: "background", modes: [false] };
    case "notes-sharing": return { fields: [], against: "background", modes: [] };
    default: return { fields: [], against: "background", modes: [] };
  }
}

function pairKey(a, b, dark) {
  return (a < b ? `${a}|${b}` : `${b}|${a}`) + `|${dark}`;
}

export function checkContrast(style, scenarios, light, dark) {
  const order = [];
  const groups = new Map();
  for (const [palette, isDark] of [[light, false], [dark, true]]) {
    for (const pair of pairsFor(style, palette, isDark)) {
      const key = pairKey(pair.foreground, pair.background, isDark);
      if (!groups.has(key)) {
        order.push(key);
        groups.set(key, { pairs: [], needed: 0, ratio: pair.ratio });
      }
      const g = groups.get(key);
      g.pairs.push(pair);
      g.needed = Math.max(g.needed, pair.threshold);
    }
  }
  function mode(d) { return d ? "dark" : "light"; }
  function pairIssue(rule, group, pair) {
    const notice = rule === "contrast.pair" && pair.notice ? " (notice text must stay readable in every scenario)" : "";
    return {
      rule, path: `${mode(pair.dark)}.${fieldName(pair.fgToken)}`,
      message: `${mode(pair.dark)} ${pair.element}: \`${fieldName(pair.fgToken)}\` ${pair.foreground} is ${formatRatio(group.ratio)}:1 against \`${fieldName(pair.bgToken)}\` ${pair.background}, needs ${cssNumber(group.needed)}:1${notice}`,
    };
  }
  const issues = [];
  const reported = new Map();
  for (const key of order) {
    const g = groups.get(key);
    if (g.ratio >= g.needed) continue;
    const pair = g.pairs.find((p) => p.baseline);
    if (!pair) continue;
    issues.push(pairIssue("contrast.baseline", g, pair));
    reported.set(key, g.needed);
  }
  for (const scenario of scenarios) {
    const check = scenarioChecks(scenario);
    for (const isDark of check.modes) {
      const palette = isDark ? dark : light;
      const bg = colorFor(palette, check.against, isDark);
      if (bg === undefined) continue;
      for (const token of check.fields) {
        const fg = colorFor(palette, token, isDark);
        if (fg === undefined) continue;
        const key = pairKey(fg, bg, isDark);
        const r = ratio(fg, bg);
        if (r >= 4.5 || reported.has(key)) continue;
        issues.push({
          rule: "contrast.scenario", path: `${mode(isDark)}.${fieldName(token)}`,
          message: `\`${scenario}\`: ${mode(isDark)} \`${fieldName(token)}\` ${fg} is ${formatRatio(r)}:1 against \`${check.against}\`, needs 4.5:1`,
        });
        reported.set(key, 4.5);
      }
    }
  }
  for (const key of order) {
    const g = groups.get(key);
    if (g.ratio >= g.needed) continue;
    const covered = reported.get(key);
    if (covered !== undefined && covered >= g.needed) continue;
    const strictest = g.pairs.filter((p) => p.threshold === g.needed);
    const pair = strictest.find((p) => p.notice) ?? strictest[0];
    issues.push(pairIssue("contrast.pair", g, pair));
    reported.set(key, g.needed);
  }
  return issues;
}

// --- Top-level validate ---------------------------------------------------------------------

let dawnFallbackCache;
/** Set once at startup with the built-in Dawn theme's resolved light/dark palettes (from the
 * generator port's own copy), so a theme that leaves out syntax/diagram can fall back to it, as
 * the app does. Call this before validating any theme that might need the fallback. */
export function setDawnFallback(light, dark) {
  dawnFallbackCache = { light, dark };
}

/** Every colour field of one palette as `[field, value]`, in report order. Exported for
 * preview-report.js. */
export function colorFields(colors) {
  const fields = [
    ["background", colors.background], ["surface", colors.surface], ["text", colors.text], ["muted", colors.muted],
    ["border", colors.border], ["heading", colors.heading], ["accent", colors.accent], ["link", colors.link], ["quote", colors.quote],
  ];
  if (colors.syntax) for (const k of ["keyword", "string", "comment", "number", "function", "type"]) fields.push([`syntax.${k}`, colors.syntax[k]]);
  if (colors.diagram) for (const k of ["node", "nodeBorder", "text", "line", "secondary", "tertiary", "note"]) fields.push([`diagram.${k}`, colors.diagram[k]]);
  return fields;
}

/** Validates an already-decoded document. Returns `{ issues, theme }`; `theme` is non-null exactly
 * when `issues` is empty. */
export function validateDocument(document, { requireComplete = false } = {}) {
  if (document.schemaVersion !== 1) {
    const message = document.schemaVersion > 1
      ? `schemaVersion ${document.schemaVersion} needs a newer MarsDawn; this one understands 1`
      : "schemaVersion must be 1";
    return { issues: [{ rule: "schema.version", path: "schemaVersion", message }], theme: null };
  }
  const issues = [];
  const normalized = { ...document };

  if (!Grammar.isThemeID(document.id)) {
    issues.push({ rule: "id.pattern", path: "id", message: `must be 1–${Grammar.MAX_ID_LENGTH} lowercase ASCII letters and digits, in runs joined by single hyphens` });
  }
  if (!Grammar.isVersion(document.version)) {
    issues.push({ rule: "version.pattern", path: "version", message: "must be MAJOR.MINOR.PATCH, for example 1.0.0" });
  }
  normalized.name = checkLocalized(document.name, "name", NAME_LIMIT, issues);
  normalized.summary = checkLocalized(document.summary, "summary", SUMMARY_LIMIT, issues);
  if (document.author) {
    const { normalized: cleanName, problems } = checkDisplayText(document.author.name, AUTHOR_NAME_LIMIT);
    for (const p of problems) issues.push(displayIssue(p, "author.name", AUTHOR_NAME_LIMIT));
    normalized.author = { ...document.author, name: cleanName };
    if (document.author.github && !Grammar.isGitHubUsername(document.author.github)) {
      issues.push({ rule: "author.github", path: "author.github", message: "must be a GitHub username: 1–39 ASCII letters, digits and single hyphens" });
    }
  }
  if (document.license && !Grammar.isLicense(document.license)) {
    issues.push({ rule: "license.pattern", path: "license", message: "must be an SPDX licence identifier, for example Apache-2.0" });
  }
  if (document.scenarios.length < 1 || document.scenarios.length > 2) {
    issues.push({ rule: "scenarios.count", path: "scenarios", message: "must list one or two scenarios" });
  } else if (new Set(document.scenarios).size !== document.scenarios.length) {
    issues.push({ rule: "scenarios.duplicate", path: "scenarios", message: "lists the same scenario twice" });
  }

  let colorsValid = true;
  for (const [mode, colors] of [["light", document.light], ["dark", document.dark]]) {
    for (const [field, value] of colorFields(colors)) {
      if (!Grammar.isHexColor(value)) {
        colorsValid = false;
        issues.push({ rule: "color.hex", path: `${mode}.${field}`, message: "must be # followed by six hex digits, for example #1C1C1C" });
      }
    }
  }

  if (document.style) normalized.style = checkStyle(document.style, issues);

  if (requireComplete) {
    for (const [mode, colors] of [["light", document.light], ["dark", document.dark]]) {
      for (const [group, present] of [["syntax", !!colors.syntax], ["diagram", !!colors.diagram]]) {
        if (!present) issues.push({ rule: "palette.incomplete", path: `${mode}.${group}`, message: "is required for a published theme; add all of its colours" });
      }
    }
  }

  if (colorsValid) {
    try {
      const light = resolvePalette(document.light, dawnFallbackCache?.light);
      const dark = resolvePalette(document.dark, dawnFallbackCache?.dark);
      if (issues.length === 0) {
        const contrast = checkContrast(normalized.style, document.scenarios, light, dark);
        if (contrast.length === 0) return { issues: [], theme: { document: normalized, light, dark } };
        issues.push(...contrast);
      }
    } catch (e) {
      if (e instanceof MissingFallback) {
        issues.push({ rule: "schema.missing", path: "light", message: "needs its syntax and diagram colours (no fallback is available)" });
      } else throw e;
    }
  }
  return { issues, theme: null };
}

function checkLocalized(text, field, limit, issues) {
  const normalized = {};
  for (const key of Object.keys(text).sort()) {
    const value = text[key];
    const path = `${field}.${quoteText(key)}`;
    if (!Grammar.isLocaleKey(key)) {
      issues.push({ rule: "locale.key", path, message: `\`${quoteText(key)}\` is not a language tag such as en, zh-Hant or pt-BR` });
    }
    const { normalized: clean, problems } = checkDisplayText(value, limit);
    for (const p of problems) issues.push(displayIssue(p, path, limit));
    normalized[key] = clean;
  }
  return normalized;
}
function displayIssue(problem, path, limit) {
  const suffix = problem === "text.length" ? ` (at most ${limit} characters)` : "";
  return { rule: problem, path, message: PROBLEM_SUMMARY[problem] + suffix };
}

/** The stages of `validate` before any business rule: size cap, duplicate-key/depth pre-pass and
 * strict decode. Returns `{ issue }` (the single issue `validate` reports for that stage) or
 * `{ document }`. Shared with preview-report.js so the two can't disagree about decoding. */
export function decodeThemeText(text) {
  const byteLength = new TextEncoder().encode(text).length;
  if (byteLength > MAX_FILE_BYTES) {
    return { issue: { rule: "file.tooLarge", path: "", message: `the file is larger than ${MAX_FILE_BYTES} bytes` } };
  }
  try {
    scanJSONStructure(text);
  } catch (e) {
    if (e instanceof JSONScanError) {
      if (e.kind === "duplicateKey") {
        const location = e.path.map(quoteText).join(".");
        return { issue: { rule: "json.duplicateKey", path: location, message: `the key \`${quoteText(e.key)}\` appears more than once in the same object` } };
      }
      if (e.kind === "tooDeep") {
        return { issue: { rule: "json.tooDeep", path: "", message: "the JSON nests deeper than 16 levels" } };
      }
      return { issue: { rule: "json.malformed", path: "", message: "the file is not valid JSON" } };
    }
    throw e;
  }
  let raw;
  try {
    raw = JSON.parse(text);
  } catch {
    return { issue: { rule: "json.malformed", path: "", message: "the file is not valid JSON" } };
  }
  try {
    return { document: decodeThemeDocument(raw) };
  } catch (e) {
    if (e instanceof DecodeFailure) return { issue: { rule: e.rule, path: e.path, message: e.message } };
    throw e;
  }
}

/** Validates the raw text of a theme.json: size cap, duplicate-key/depth pre-pass, strict decode,
 * then every business rule. */
export function validate(text, { requireComplete = false } = {}) {
  const decoded = decodeThemeText(text);
  if (decoded.issue) return { issues: [decoded.issue], theme: null };
  return validateDocument(decoded.document, { requireComplete });
}

export { fontStackFor };
