// Port of ThemeCSSGenerator.swift (kit origin/release-0.6.1, f1c66e16509e): turns a validated theme's
// style options into the same CSS the kit's ThemeCSSGenerator would emit. See styles-data.js's
// header note on what "port" means here.

import { isThemeID, isHexColor } from "./grammar.js";
import { isAcceptable, cssNumber } from "./numbers.js";
import { FRAGMENTS } from "./styles-data.js";
import { cssVariables, roleCSSValue } from "./palette.js";

export class GeneratorRefusal extends Error {
  constructor(kind, field) {
    super(kind);
    this.kind = kind; // "invalidID" | "invalidColor" | "invalidNumber" | "unresolvedPlaceholder" | "duplicateID"
    //                   | "unknownFontDesign" | "unknownRole" | "invalidAlign" (closed values the
    //                   validator's decode already enforces; refused again here, never omitted)
    this.field = field;
  }
}

const FONT_STACKS = {
  sans: '-apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang TC", "PingFang SC", sans-serif',
  serif: 'ui-serif, "New York", Georgia, "Songti TC", "Songti SC", serif',
  rounded: 'ui-rounded, "SF Pro Rounded", -apple-system, "PingFang TC", "PingFang SC", sans-serif',
};

/** The font stack for a fontDesign, or undefined for anything that isn't one of FONT_STACKS' own
 * keys (an inherited name such as "constructor" never resolves). */
export function fontStackFor(fontDesign) {
  if (typeof fontDesign !== "string" || !Object.hasOwn(FONT_STACKS, fontDesign)) return undefined;
  return FONT_STACKS[fontDesign];
}

const H1_ALIGNS = ["left", "center"];

/** var(--…) for a palette role; refuses anything that isn't a palette role. */
function roleValue(role) {
  const value = roleCSSValue(role);
  if (value === undefined) throw new GeneratorRefusal("unknownRole", String(role));
  return value;
}

/** The palette block for one theme: `:root[data-theme="id"] { … } @media (dark) { … }`. */
export function variableBlock(id, light, dark, fontStack) {
  if (!isThemeID(id)) throw new GeneratorRefusal("invalidID");
  for (const [mode, palette] of [["light", light], ["dark", dark]]) {
    for (const [name, value] of cssVariables(palette)) {
      if (!isHexColor(value)) throw new GeneratorRefusal("invalidColor", `${mode}.${name}`);
    }
  }
  const lightLines = cssVariables(light)
    .map(([name, value]) => `  --${name}: ${value};`)
    .concat(fontStack ? [`  --font-body: ${fontStack};`] : [])
    .join("\n");
  const darkLines = cssVariables(dark).map(([name, value]) => `  --${name}: ${value};`).join("\n");
  return `:root[data-theme="${id}"] {\n${lightLines}\n}\n@media (prefers-color-scheme: dark) {\n  :root[data-theme="${id}"] {\n${darkLines}\n  }\n}`;
}

class OrderedRules {
  constructor() {
    this.order = [];
    this.declarations = new Map();
  }
  add(selector, property, value) {
    for (const rawPart of selector.split(",")) {
      const part = rawPart.trim();
      if (!this.declarations.has(part)) {
        this.order.push(part);
        this.declarations.set(part, []);
      }
      this.declarations.get(part).push({ property, value });
    }
  }
  addFragments(option, value, params) {
    const raw = FRAGMENTS[option]?.[value];
    if (!raw) throw new GeneratorRefusal("unresolvedPlaceholder");
    for (const fragment of raw) {
      for (const [property, rawValue] of fragment.declarations) {
        let v = rawValue;
        for (const [key, replacement] of Object.entries(params)) {
          v = v.split(`{{${key}}}`).join(replacement);
        }
        this.add(fragment.selector, property, v);
      }
    }
  }
  render(id) {
    let out = "";
    for (const selector of this.order) {
      const scoped = `[data-theme="${id}"] ${selector}`;
      const body = this.declarations.get(selector).map((d) => `${d.property}: ${d.value};`).join(" ");
      out += `${scoped} { ${body} }\n`;
    }
    return out;
  }
}

function number(rules, name, value) {
  if (!isAcceptable(name, value)) throw new GeneratorRefusal("invalidNumber", name);
  return cssNumber(value);
}

function applyH1Decoration(decoration, rules) {
  switch (decoration.type) {
    case "rule": return; // default: the base h1 rule already draws it
    case "none": return rules.addFragments("h1Decoration", "none", {});
    case "shortRule": return rules.addFragments("h1Decoration", "shortRule", { color: roleValue(decoration.color) });
    case "gradientBar":
      return rules.addFragments("h1Decoration", "gradientBar", {
        from: roleValue(decoration.from), to: roleValue(decoration.to),
      });
    default: throw new GeneratorRefusal("unresolvedPlaceholder");
  }
}
function applyH2Decoration(decoration, rules) {
  switch (decoration.type) {
    case "rule": return;
    case "none": return rules.addFragments("h2Decoration", "none", {});
    case "dot": return rules.addFragments("h2Decoration", "dot", { color: roleValue(decoration.color) });
    default: throw new GeneratorRefusal("unresolvedPlaceholder");
  }
}

/** The per-theme style rules for one theme: `{ css, selectors }`. `style` may be null/undefined. */
export function checkedRules(id, style) {
  if (!isThemeID(id)) throw new GeneratorRefusal("invalidID");
  if (!style) return { css: "", selectors: [] };
  const rules = new OrderedRules();
  const vars = [];
  if (style.headingWeight != null) vars.push(["--heading-weight", number(rules, "headingWeight", style.headingWeight)]);
  if (style.bodySize != null) vars.push(["--body-size", `${number(rules, "bodySize", style.bodySize)}px`]);
  if (style.lineHeight != null) vars.push(["--line-height", number(rules, "lineHeight", style.lineHeight)]);
  if (style.radius != null) vars.push(["--radius", `${number(rules, "radius", style.radius)}px`]);

  if (style.maxWidth != null) rules.add(".markdown-body", "max-width", `${number(rules, "maxWidth", style.maxWidth)}px`);

  if (style.h1) {
    const h1 = style.h1;
    if (h1.align != null) {
      if (!H1_ALIGNS.includes(h1.align)) throw new GeneratorRefusal("invalidAlign", "h1.align");
      rules.add("h1", "text-align", h1.align);
    }
    if (h1.size != null) rules.add("h1", "font-size", `${number(rules, "h1.size", h1.size)}em`);
    if (h1.letterSpacing != null) rules.add("h1", "letter-spacing", `${number(rules, "h1.letterSpacing", h1.letterSpacing)}em`);
    if (h1.decoration) applyH1Decoration(h1.decoration, rules);
  }
  if (style.h2) {
    const h2 = style.h2;
    if (h2.letterSpacing != null) rules.add("h2", "letter-spacing", `${number(rules, "h2.letterSpacing", h2.letterSpacing)}em`);
    if (h2.italic) rules.add("h2", "font-style", "italic");
    if (h2.decoration) applyH2Decoration(h2.decoration, rules);
  }
  if (style.blockquote) {
    const bq = style.blockquote;
    if (bq.italic) rules.add("blockquote", "font-style", "italic");
    if (bq.style) {
      if (bq.style.type === "bar") {
        const width = number(rules, "blockquote.style.width", bq.style.width ?? 3);
        rules.addFragments("blockquoteStyle", "bar", { width });
      } else if (bq.style.type === "panel") {
        rules.addFragments("blockquoteStyle", "panel", {});
      }
    }
  }
  if (style.hr?.style) {
    const value = style.hr.style;
    if (value.type === "line") {
      if (value.thickness != null) rules.add("hr", "height", `${number(rules, "hr.style.thickness", value.thickness)}px`);
      rules.add("hr", "background", roleValue(value.color ?? "border"));
    } else if (value.type === "shortCentered") {
      rules.addFragments("hrStyle", "shortCentered", { color: roleValue(value.color) });
    } else if (value.type === "gradient") {
      if (value.colors.length < 2 || value.colors.length > 3) throw new GeneratorRefusal("unresolvedPlaceholder");
      rules.addFragments("hrStyle", "gradient", { colors: value.colors.map((role) => roleValue(role)).join(", ") });
    }
  }
  if (style.table) {
    const table = style.table;
    if (table.header) {
      const h = table.header;
      if (h.type === "surface") rules.addFragments("tableHeader", "surface", {});
      else if (h.type === "accentRule") rules.addFragments("tableHeader", "accentRule", { color: roleValue(h.color) });
      else if (h.type === "filled") {
        rules.addFragments("tableHeader", "filled", {
          background: roleValue(h.background), text: roleValue(h.text), border: roleValue(h.border ?? h.background),
        });
      }
    }
    if (table.verticalRules === false) {
      rules.add("th, td", "border-left", "0");
      rules.add("th, td", "border-right", "0");
    }
    if (table.rounded) rules.add("table", "border-radius", "var(--radius)");
  }
  if (style.listMarker) rules.add("li::marker", "color", roleValue(style.listMarker));
  if (style.inlineCode) rules.add("code:not(pre code)", "color", roleValue(style.inlineCode));
  if (style.link?.underline) {
    rules.add("a", "text-decoration", "underline");
    rules.add("a", "text-underline-offset", "0.15em");
    rules.add("a", "text-decoration-thickness", "1px");
  }
  if (style.syntax?.boldKeywords) rules.add(".hljs-keyword, .hljs-title", "font-weight", "650");

  let css = "";
  if (vars.length) {
    css += `:root[data-theme="${id}"] {\n`;
    css += vars.map(([k, v]) => `  ${k}: ${v};`).join("\n");
    css += "\n}\n";
  }
  css += rules.render(id);
  if (css.includes("{{")) throw new GeneratorRefusal("unresolvedPlaceholder");
  return { css, selectors: rules.order.slice() };
}

/** `generate` never throws: a refusal yields empty output, like the kit's own convenience entry. */
export function generate(id, style) {
  try {
    return checkedRules(id, style);
  } catch {
    return { css: "", selectors: [] };
  }
}

/** The whole theme CSS for one validated theme: `{ variables, rules }`. */
export function stylesheetFor(validated) {
  const id = validated.document.id;
  const fontStack = fontStackFor(validated.document.fontDesign);
  if (fontStack === undefined) throw new GeneratorRefusal("unknownFontDesign", "fontDesign");
  const variables = variableBlock(id, validated.light, validated.dark, fontStack);
  const rules = checkedRules(id, validated.document.style).css;
  return { variables, rules };
}
