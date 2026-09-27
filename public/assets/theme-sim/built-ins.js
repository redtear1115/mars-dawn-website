// The four built-in themes' theme.json (kit origin/release-0.6.1, d6eae71,
// Sources/MarsDawnThemes/Resources/Themes/<id>/theme.json), verbatim. Used to seed the simulator's
// "start from a built-in" list and to resolve Dawn's palette as the fallback for a theme that
// leaves out `syntax`/`diagram` (design §4.2, §6.2).

export const BUILT_IN_THEME_JSON = {
  dawn: `{
  "schemaVersion": 1, "id": "dawn", "version": "1.0.0",
  "name": { "en": "Dawn" }, "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans", "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": { "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } } }
}`,
  classic: `{
  "schemaVersion": 1, "id": "classic", "version": "1.0.0",
  "name": { "en": "Classic" }, "summary": { "en": "Elegant serif on paper" },
  "fontDesign": "serif", "scenarios": ["formal-output"],
  "light": {
    "background": "#FCFCFB", "surface": "#F2F2F0", "text": "#1C1C1C", "muted": "#5E5E5E",
    "border": "#DDDDDB", "heading": "#111111", "accent": "#2E2E2E", "link": "#1C1C1C", "quote": "#8C8C8C",
    "syntax": { "keyword": "#1C1C1C", "string": "#4D4D4D", "comment": "#6A6A6A", "number": "#3A3A3A", "function": "#1C1C1C", "type": "#3A3A3A" },
    "diagram": { "node": "#F2F2F0", "nodeBorder": "#5E5E5E", "text": "#1C1C1C", "line": "#6A6A6A", "secondary": "#EAEAE8", "tertiary": "#FCFCFB", "note": "#F6F6F3" }
  },
  "dark": {
    "background": "#171717", "surface": "#222222", "text": "#E6E6E6", "muted": "#A6A6A6",
    "border": "#363636", "heading": "#F2F2F2", "accent": "#D4D4D4", "link": "#EDEDED", "quote": "#7C7C7C",
    "syntax": { "keyword": "#F2F2F2", "string": "#C4C4C4", "comment": "#9C9C9C", "number": "#D4D4D4", "function": "#F2F2F2", "type": "#D4D4D4" },
    "diagram": { "node": "#262626", "nodeBorder": "#A6A6A6", "text": "#E6E6E6", "line": "#9C9C9C", "secondary": "#202020", "tertiary": "#1B1B1B", "note": "#2B2B2B" }
  },
  "style": {
    "bodySize": 16, "lineHeight": 1.75, "headingWeight": 600, "radius": 4, "maxWidth": 720,
    "h1": { "align": "center", "size": 2.2, "letterSpacing": 0.01, "decoration": { "type": "shortRule", "color": "accent" } },
    "h2": { "italic": true },
    "blockquote": { "style": { "type": "bar", "width": 2 }, "italic": true },
    "hr": { "style": { "type": "shortCentered", "color": "accent" } },
    "table": { "header": { "type": "accentRule", "color": "accent" }, "verticalRules": false },
    "link": { "underline": true },
    "syntax": { "boldKeywords": true }
  }
}`,
  modern: `{
  "schemaVersion": 1, "id": "modern", "version": "1.0.0",
  "name": { "en": "Modern" }, "summary": { "en": "Clean and familiar" },
  "fontDesign": "sans", "scenarios": ["technical-docs"],
  "light": {
    "background": "#FFFFFF", "surface": "#F6F8FA", "text": "#1F2328", "muted": "#59636E",
    "border": "#D1D9E0", "heading": "#1F2328", "accent": "#0969DA", "link": "#0969DA", "quote": "#8C939A",
    "syntax": { "keyword": "#CF222E", "string": "#0A3069", "comment": "#59636E", "number": "#0550AE", "function": "#8250DF", "type": "#953800" },
    "diagram": { "node": "#EEF4FC", "nodeBorder": "#0969DA", "text": "#1F2328", "line": "#59636E", "secondary": "#F1ECFB", "tertiary": "#F6F8FA", "note": "#FFF8C5" }
  },
  "dark": {
    "background": "#0D1117", "surface": "#151B23", "text": "#E6EDF3", "muted": "#9198A1",
    "border": "#30363D", "heading": "#F0F6FC", "accent": "#4493F8", "link": "#4493F8", "quote": "#5B636C",
    "syntax": { "keyword": "#FF7B72", "string": "#A5D6FF", "comment": "#9198A1", "number": "#79C0FF", "function": "#D2A8FF", "type": "#FFA657" },
    "diagram": { "node": "#172233", "nodeBorder": "#4493F8", "text": "#E6EDF3", "line": "#9198A1", "secondary": "#221B33", "tertiary": "#151B23", "note": "#2E2A12" }
  },
  "style": {
    "headingWeight": 700, "radius": 6,
    "h1": { "letterSpacing": -0.015 }, "h2": { "letterSpacing": -0.015 },
    "blockquote": { "style": { "type": "bar", "width": 4 } },
    "hr": { "style": { "type": "line", "color": "quote" } },
    "listMarker": "muted"
  }
}`,
  vivid: `{
  "schemaVersion": 1, "id": "vivid", "version": "1.0.0",
  "name": { "en": "Vivid" }, "summary": { "en": "Playful, bright and rounded" },
  "fontDesign": "rounded", "scenarios": ["notes-sharing"],
  "light": {
    "background": "#FFFDF8", "surface": "#F3EEFF", "text": "#2D2A32", "muted": "#6B6475",
    "border": "#E6DCFB", "heading": "#5B3BE0", "accent": "#D5316B", "link": "#087481", "quote": "#FFB020",
    "syntax": { "keyword": "#B8246A", "string": "#07734F", "comment": "#70697C", "number": "#A44D06", "function": "#5B3BE0", "type": "#087481" },
    "diagram": { "node": "#EFE9FF", "nodeBorder": "#6C4BF4", "text": "#2D2A32", "line": "#E8457A", "secondary": "#E0F7F4", "tertiary": "#FFF1F6", "note": "#FFF1CC" }
  },
  "dark": {
    "background": "#1A1625", "surface": "#251F36", "text": "#F1ECFA", "muted": "#AFA6BE",
    "border": "#3A3150", "heading": "#B69CFF", "accent": "#FF7AA2", "link": "#3DD6D0", "quote": "#FFC857",
    "syntax": { "keyword": "#FF7AB8", "string": "#5BE3A8", "comment": "#948BA6", "number": "#FFA657", "function": "#B69CFF", "type": "#3DD6D0" },
    "diagram": { "node": "#2E2548", "nodeBorder": "#B69CFF", "text": "#F1ECFA", "line": "#FF7AA2", "secondary": "#1D3534", "tertiary": "#2A1F2E", "note": "#3D3420" }
  },
  "style": {
    "headingWeight": 800, "radius": 14,
    "h1": { "decoration": { "type": "gradientBar", "from": "accent", "to": "heading" } },
    "h2": { "decoration": { "type": "dot", "color": "accent" } },
    "blockquote": { "style": { "type": "panel" } },
    "inlineCode": "keyword",
    "table": { "header": { "type": "filled", "background": "heading", "text": "background" }, "rounded": true },
    "hr": { "style": { "type": "gradient", "colors": ["accent", "heading", "link"] } }
  }
}`,
};

export const BUILT_IN_ORDER = ["dawn", "classic", "modern", "vivid"];
