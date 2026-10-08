// The simulator's fixed sample document (design theme-ecosystem-design.md §3.4): headings, a list,
// a quote, a table, code, a rule, and a hand-made diagram using the `--mm-*` variables (no
// mermaid.min.js -- design W1: "a hand-made SVG using --mm-* variables"). Every element a themed
// class or built-in touches appears here, so the preview shows a style option's effect.
//
// This lives inside `.sim-preview .markdown-body`, the same class the kit's own preview uses, so
// per-theme rules scoped to `.markdown-body` (e.g. `maxWidth`) apply.

export const SAMPLE_DIAGRAM_SVG = `
<svg class="mm-sample" viewBox="0 0 320 110" role="img" aria-label="">
  <g fill="none" stroke="var(--mm-line)" stroke-width="2">
    <path d="M 78 55 L 150 55" marker-end="url(#sim-arrow)"></path>
  </g>
  <defs>
    <marker id="sim-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--mm-line)"></path>
    </marker>
  </defs>
  <g>
    <rect x="8" y="30" width="70" height="50" rx="6" fill="var(--mm-node)" stroke="var(--mm-border)" stroke-width="1.5"></rect>
    <text x="43" y="59" text-anchor="middle" fill="var(--mm-text)" font-size="12">Draft</text>
  </g>
  <g>
    <rect x="150" y="20" width="70" height="70" rx="6" fill="var(--mm-secondary)" stroke="var(--mm-border)" stroke-width="1.5"></rect>
    <text x="185" y="59" text-anchor="middle" fill="var(--mm-text)" font-size="12">Review</text>
  </g>
  <g>
    <rect x="242" y="30" width="70" height="50" rx="6" fill="var(--mm-tertiary)" stroke="var(--mm-border)" stroke-width="1.5"></rect>
    <text x="277" y="59" text-anchor="middle" fill="var(--mm-text)" font-size="12">Publish</text>
  </g>
  <path d="M 220 55 L 242 55" fill="none" stroke="var(--mm-line)" stroke-width="2" marker-end="url(#sim-arrow)"></path>
  <rect x="118" y="88" width="84" height="18" rx="4" fill="var(--mm-note)"></rect>
  <text x="160" y="101" text-anchor="middle" fill="var(--mm-text)" font-size="10">one round of edits</text>
</svg>`.trim();

export function sampleDocumentHTML() {
  return `
<div class="markdown-body">
  <h1>A theme, previewed live</h1>
  <p>This sample document uses every element a style option can touch: headings, a list, a quote, a table, code, a rule and a small diagram.</p>
  <h2>Why this matters</h2>
  <p>Every value you pick below is checked before it draws anything, the same rules the kit's own validator applies. <a href="#">A link looks like this</a>, and <code>inline code</code> sits next to it.</p>
  <ul>
    <li>A first point, drawn with the list marker colour.</li>
    <li>A second point, with <strong>emphasis</strong> and <em>italics</em>.</li>
  </ul>
  <blockquote>
    <p>A quoted line, to show the blockquote style and its colour.</p>
  </blockquote>
  <table>
    <thead><tr><th>Option</th><th>Effect</th></tr></thead>
    <tbody>
      <tr><td>Heading weight</td><td>Bolder or lighter titles</td></tr>
      <tr><td>Radius</td><td>Rounder corners on tables and rules</td></tr>
    </tbody>
  </table>
  <pre><code>function draft(doc) {
  return review(doc);
}</code></pre>
  <hr>
  <div class="mermaid-output">${SAMPLE_DIAGRAM_SVG}</div>
</div>`.trim();
}
