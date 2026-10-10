// Port of ResolvedPalette (ThemePairs.swift, kit origin/release-0.6.1, f1c66e16509e): a palette with
// every colour present (the file's own syntax/diagram groups, or Dawn's for the same appearance
// where the file leaves one out), and the derived tokens a pair can name.

import { mix } from "./contrast.js";

export class MissingFallback extends Error {}

const BASE_FIELDS = ["background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote"];
const SYNTAX_FIELDS = ["keyword", "string", "comment", "number", "function", "type"];
const DIAGRAM_FIELDS = ["node", "nodeBorder", "text", "line", "secondary", "tertiary", "note"];

/** `colors` is one palette object from a theme.json (light or dark): the 9 base fields plus
 * optional `syntax`/`diagram`. `fallback` is the same-shape resolved palette to fill from
 * (Dawn's), or null. Throws MissingFallback if a group is missing from both. */
export function resolvePalette(colors, fallback) {
  const syntax = colors.syntax ?? fallback?.syntax;
  const diagram = colors.diagram ?? fallback?.diagram;
  if (!syntax || !diagram) throw new MissingFallback();
  const resolved = {};
  for (const field of BASE_FIELDS) resolved[field] = colors[field];
  resolved.syntax = syntax;
  resolved.diagram = diagram;
  return resolved;
}

/** Every colour with its CSS custom-property name, in the order the palette block writes them. */
export function cssVariables(palette) {
  const out = BASE_FIELDS.map((f) => [cssVarName(f), palette[f]]);
  for (const f of SYNTAX_FIELDS) out.push([cssVarName(f), palette.syntax[f]]);
  for (const f of DIAGRAM_FIELDS) out.push([`mm-${diagramVar(f)}`, palette.diagram[f]]);
  return out;
}

function cssVarName(field) {
  return { background: "bg", text: "fg", keyword: "hl-keyword", string: "hl-string", comment: "hl-comment",
    number: "hl-number", function: "hl-function", type: "hl-type" }[field] ?? field;
}
function diagramVar(field) {
  return { node: "node", nodeBorder: "border", text: "text", line: "line", secondary: "secondary",
    tertiary: "tertiary", note: "note" }[field];
}

/** The colour a pair token names in this palette, or undefined for an unknown token. */
export function colorFor(palette, token, dark) {
  switch (token) {
    case "background": case "surface": case "text": case "muted": case "border":
    case "heading": case "accent": case "link": case "quote":
      return palette[token];
    case "keyword": case "string": case "comment": case "number": case "function": case "type":
      return palette.syntax[token];
    case "diagram.node": return palette.diagram.node;
    case "diagram.nodeBorder": return palette.diagram.nodeBorder;
    case "diagram.text": return palette.diagram.text;
    case "diagram.line": return palette.diagram.line;
    case "diagram.secondary": return palette.diagram.secondary;
    case "diagram.tertiary": return palette.diagram.tertiary;
    case "diagram.note": return palette.diagram.note;
    case "chip": return dark ? mix(palette.surface, palette.text, 0.1) : palette.surface;
    case "frontMatter": return mix(palette.surface, palette.background, 0.35);
    case "footnoteTarget": return mix(palette.background, palette.accent, 0.18);
    case "paper": return "#FFFFFF";
    default: return undefined;
  }
}

const PALETTE_ROLE_CSS_VAR = {
  background: "bg", surface: "surface", text: "fg", muted: "muted", border: "border", heading: "heading",
  accent: "accent", link: "link", quote: "quote", keyword: "hl-keyword", string: "hl-string",
  comment: "hl-comment", number: "hl-number", function: "hl-function", type: "hl-type",
};

/** var(--…) for a palette role name, as PaletteRole.cssValue does, or undefined for anything that
 * isn't one of the table's own keys (never an inherited name such as "constructor"). The generator
 * refuses on undefined (generator.js roleValue). */
export function roleCSSValue(role) {
  if (typeof role !== "string" || !Object.hasOwn(PALETTE_ROLE_CSS_VAR, role)) return undefined;
  return `var(--${PALETTE_ROLE_CSS_VAR[role]})`;
}

export const PALETTE_ROLES = Object.keys(PALETTE_ROLE_CSS_VAR);
