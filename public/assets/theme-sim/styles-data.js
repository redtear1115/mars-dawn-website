// Port of Sources/MarsDawnThemes/Resources/ThemeStyles.json (kit origin/release-0.6.1, d6eae71):
// the CSS fragments each enum option value contributes, and the composed foreground/background
// pairs the shared stylesheet and each option value draw (design §4.3/§6.3).
//
// This is a *port*, hand-kept in sync with the kit's data file, exercised against it in
// scripts/check_theme_sim.mjs's parity check (dev-only until WA vendors the real file for CI to
// drift-check against). It is not the vendored copy WA's scripts/sync_theme_kit.py will write to
// vendor/kit-themes/<tag>/ThemeStyles.json -- see that script's own docstring once it lands.

export const FRAGMENTS = {
  h1Decoration: {
    none: [{ selector: "h1", declarations: [["border-bottom", "0"], ["padding-bottom", "0"]] }],
    shortRule: [
      { selector: "h1", declarations: [["border-bottom", "0"], ["padding-bottom", "0"]] },
      {
        selector: "h1::after",
        declarations: [
          ["content", '""'], ["display", "block"], ["width", "48px"], ["height", "1px"],
          ["margin", "0.5em auto 0"], ["background", "{{color}}"],
        ],
      },
    ],
    gradientBar: [
      {
        selector: "h1",
        declarations: [
          ["border-bottom", "0"], ["padding-bottom", "0.15em"],
          ["background-image", "linear-gradient(90deg, {{from}}, {{to}})"],
          ["background-size", "64px 4px"], ["background-repeat", "no-repeat"], ["background-position", "left bottom"],
        ],
      },
    ],
  },
  h2Decoration: {
    none: [{ selector: "h2", declarations: [["border-bottom", "0"], ["padding-bottom", "0"]] }],
    dot: [
      { selector: "h2", declarations: [["border-bottom", "0"], ["padding-bottom", "0"]] },
      {
        selector: "h2::before",
        declarations: [
          ["content", '""'], ["display", "inline-block"], ["width", "0.5em"], ["height", "0.5em"],
          ["margin-right", "0.45em"], ["border-radius", "50%"], ["background", "{{color}}"],
          ["vertical-align", "0.12em"],
        ],
      },
    ],
  },
  blockquoteStyle: {
    bar: [{ selector: "blockquote", declarations: [["border-left-width", "{{width}}px"]] }],
    panel: [
      {
        selector: "blockquote",
        declarations: [
          ["border-left", "0"], ["padding", "0.6em 1em"], ["background", "var(--surface)"],
          ["border-radius", "var(--radius)"], ["color", "var(--fg)"],
        ],
      },
    ],
  },
  hrStyle: {
    shortCentered: [
      {
        selector: "hr",
        declarations: [["height", "1px"], ["width", "30%"], ["margin", "2.4em auto"], ["background", "{{color}}"]],
      },
    ],
    gradient: [
      {
        selector: "hr",
        declarations: [["height", "4px"], ["border-radius", "2px"], ["background", "linear-gradient(90deg, {{colors}})"]],
      },
    ],
  },
  tableHeader: {
    surface: [{ selector: "th", declarations: [["background", "var(--surface)"]] }],
    accentRule: [{ selector: "th", declarations: [["background", "transparent"], ["border-bottom", "2px solid {{color}}"]] }],
    filled: [{ selector: "th", declarations: [["background", "{{background}}"], ["color", "{{text}}"], ["border-color", "{{border}}"]] }],
  },
};

export const SHARED_PAIRS = [
  { id: "body-text", element: "body text", fg: "text", bg: "background", kind: "text", baseline: true },
  { id: "muted-text", element: "muted text", fg: "muted", bg: "background", kind: "text" },
  { id: "headings", element: "headings", fg: "heading", bg: "background", kind: "text" },
  { id: "links", element: "links", fg: "link", bg: "background", kind: "text" },
  { id: "inline-code", element: "inline code", fg: "text", bg: "chip", kind: "text" },
  { id: "code-block-text", element: "code block text", fg: "text", bg: "surface", kind: "text" },
  { id: "syntax-keyword", element: "syntax keyword in a code block", fg: "keyword", bg: "surface", kind: "text" },
  { id: "syntax-string", element: "syntax string in a code block", fg: "string", bg: "surface", kind: "text" },
  { id: "syntax-comment", element: "syntax comment in a code block", fg: "comment", bg: "surface", kind: "text" },
  { id: "syntax-number", element: "syntax number in a code block", fg: "number", bg: "surface", kind: "text" },
  { id: "syntax-function", element: "syntax function in a code block", fg: "function", bg: "surface", kind: "text" },
  { id: "syntax-type", element: "syntax type in a code block", fg: "type", bg: "surface", kind: "text" },
  { id: "syntax-meta", element: "syntax meta in a code block", fg: "muted", bg: "surface", kind: "text" },
  { id: "table-header", element: "table header", fg: "text", bg: "surface", kind: "text" },
  { id: "table-cell", element: "table cell", fg: "text", bg: "background", kind: "text" },
  { id: "blockquote-text", element: "blockquote text", fg: "muted", bg: "background", kind: "text" },
  { id: "front-matter-label", element: "front matter label", fg: "muted", bg: "frontMatter", kind: "text" },
  { id: "front-matter-value", element: "front matter value", fg: "text", bg: "frontMatter", kind: "text" },
  { id: "banner-text", element: "banner and placeholder text", fg: "muted", bg: "surface", kind: "text", notice: true },
  { id: "banner-button", element: "banner button", fg: "background", bg: "accent", kind: "text", notice: true },
  { id: "error-text", element: "math and diagram errors", fg: "keyword", bg: "background", kind: "text", notice: true },
  { id: "footnote-target", element: "body text on a footnote highlight", fg: "text", bg: "footnoteTarget", kind: "text", baseline: true },
  { id: "diagram-label-node", element: "diagram label on node", fg: "diagram.text", bg: "diagram.node", kind: "text" },
  { id: "diagram-label-secondary", element: "diagram label on secondary", fg: "diagram.text", bg: "diagram.secondary", kind: "text" },
  { id: "diagram-label-tertiary", element: "diagram label on tertiary", fg: "diagram.text", bg: "diagram.tertiary", kind: "text" },
  { id: "diagram-label-note", element: "diagram label on note", fg: "diagram.text", bg: "diagram.note", kind: "text" },
  { id: "diagram-label-edge", element: "diagram label on edge label", fg: "diagram.text", bg: "background", kind: "text" },
  { id: "diagram-cluster-label", element: "diagram cluster label", fg: "heading", bg: "diagram.tertiary", kind: "text" },
  { id: "diagram-title", element: "diagram title", fg: "heading", bg: "background", kind: "text" },
  { id: "sequence-number", element: "sequence number", fg: "background", bg: "diagram.text", kind: "text" },
  { id: "pie-label-1", element: "pie slice 1 label", fg: "background", bg: "accent", kind: "text" },
  { id: "pie-label-2", element: "pie slice 2 label", fg: "background", bg: "function", kind: "text" },
  { id: "pie-label-3", element: "pie slice 3 label", fg: "background", bg: "string", kind: "text" },
  { id: "pie-label-4", element: "pie slice 4 label", fg: "background", bg: "number", kind: "text" },
  { id: "pie-label-5", element: "pie slice 5 label", fg: "background", bg: "type", kind: "text" },
  { id: "pie-label-6", element: "pie slice 6 label", fg: "background", bg: "link", kind: "text" },
  { id: "pie-slice-1", element: "pie slice 1", fg: "accent", bg: "background", kind: "nontext" },
  { id: "pie-slice-2", element: "pie slice 2", fg: "function", bg: "background", kind: "nontext" },
  { id: "pie-slice-3", element: "pie slice 3", fg: "string", bg: "background", kind: "nontext" },
  { id: "pie-slice-4", element: "pie slice 4", fg: "number", bg: "background", kind: "nontext" },
  { id: "pie-slice-5", element: "pie slice 5", fg: "type", bg: "background", kind: "nontext" },
  { id: "pie-slice-6", element: "pie slice 6", fg: "link", bg: "background", kind: "nontext" },
  { id: "pdf-text", element: "PDF text on white paper", fg: "text", bg: "paper", kind: "text", modes: ["light"] },
  { id: "pdf-muted", element: "PDF muted on white paper", fg: "muted", bg: "paper", kind: "text", modes: ["light"] },
  { id: "pdf-headings", element: "PDF headings on white paper", fg: "heading", bg: "paper", kind: "text", modes: ["light"] },
  { id: "pdf-links", element: "PDF links on white paper", fg: "link", bg: "paper", kind: "text", modes: ["light"] },
  { id: "list-marker", element: "list marker", fg: "accent", bg: "background", kind: "nontext" },
  { id: "task-checkbox", element: "task checkbox", fg: "accent", bg: "background", kind: "nontext" },
  { id: "blockquote-bar", element: "blockquote bar", fg: "quote", bg: "background", kind: "nontext" },
  { id: "diagram-lines", element: "diagram lines", fg: "diagram.line", bg: "background", kind: "nontext" },
  { id: "diagram-node-border", element: "diagram node border", fg: "diagram.nodeBorder", bg: "diagram.node", kind: "nontext" },
];

export const OPTION_PAIRS = {
  h1Decoration: {
    none: { pairs: [] },
    shortRule: { pairs: [{ element: "h1 short rule", fg: "{{color}}", bg: "background", kind: "nontext" }] },
    gradientBar: {
      pairs: [
        { element: "h1 gradient bar start", fg: "{{from}}", bg: "background", kind: "nontext" },
        { element: "h1 gradient bar end", fg: "{{to}}", bg: "background", kind: "nontext" },
      ],
    },
  },
  h2Decoration: {
    none: { pairs: [] },
    dot: { pairs: [{ element: "h2 dot", fg: "{{color}}", bg: "background", kind: "nontext" }] },
  },
  blockquoteStyle: {
    bar: { pairs: [] },
    panel: {
      replaces: ["blockquote-text", "blockquote-bar"],
      pairs: [
        { element: "blockquote text on its panel", fg: "text", bg: "surface", kind: "text" },
        { element: "link in a panel quote", fg: "link", bg: "surface", kind: "text" },
        { element: "marker, checkbox or rule in a panel quote", fg: "accent", bg: "surface", kind: "nontext" },
      ],
    },
  },
  hrStyle: {
    line: { pairs: [{ element: "rule", fg: "{{color}}", bg: "background", kind: "nontext" }] },
    shortCentered: { pairs: [{ element: "rule", fg: "{{color}}", bg: "background", kind: "nontext" }] },
    gradient: { pairs: [{ element: "rule gradient stop", fg: "{{colors}}", bg: "background", kind: "nontext" }] },
  },
  tableHeader: {
    surface: { replaces: ["table-header"], pairs: [{ element: "table header", fg: "text", bg: "surface", kind: "text" }] },
    accentRule: {
      replaces: ["table-header"],
      pairs: [
        { element: "table header", fg: "text", bg: "background", kind: "text" },
        { element: "table header rule", fg: "{{color}}", bg: "background", kind: "nontext" },
      ],
    },
    filled: {
      replaces: ["table-header"],
      pairs: [{ element: "filled table header", fg: "{{text}}", bg: "{{background}}", kind: "text" }],
    },
  },
  listMarker: {
    role: { replaces: ["list-marker"], pairs: [{ element: "list marker", fg: "{{color}}", bg: "background", kind: "nontext" }] },
  },
  inlineCode: {
    role: { pairs: [{ element: "inline code (coloured)", fg: "{{color}}", bg: "chip", kind: "text" }] },
  },
};
