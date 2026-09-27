// The rescoping transform (design theme-ecosystem-design.md §3.4, plan slice WA/W1, rev-4 rule).
//
// Turns a stylesheet written for the kit's own preview page (`:root`, `html`, `body`, and rules
// scoped by `[data-theme="…"]`) into one that can be adopted alongside the real page without ever
// touching anything outside a wrapper element, `.sim-preview` by default:
//
//   :root                        -> .sim-preview
//   html                         -> .sim-preview
//   body                         -> .sim-preview
//   :root[data-theme="x"]        -> .sim-preview[data-theme="x"]
//   [data-theme="x"] h1          -> .sim-preview[data-theme="x"] h1
//   [data-theme="x"] .foo        -> .sim-preview[data-theme="x"] .foo
//   [data-theme] .foo            -> .sim-preview[data-theme] .foo
//   [data-theme="x"] h2::before  -> .sim-preview[data-theme="x"] h2::before
//   .foo (anything else)         -> .sim-preview .foo
//
// A selector's leading `[data-theme…]` compound (with or without `:root`) merges onto the wrapper
// as ONE compound selector; only the remainder gets a descendant prefix. This is what lets a
// theme's per-theme rules (`[data-theme="x"] h1 { … }`) still work once `[data-theme="x"]` moves
// from the document root down onto `.sim-preview` -- the compound has to travel together, not get
// split into two descendant steps (`.sim-preview [data-theme="x"] h1` would never match anything,
// because nothing inside `.sim-preview` also carries `data-theme` as a separate descendant).
//
// `@media (prefers-color-scheme: dark) { … }` becomes the same rules under
// `.sim-preview[data-appearance="dark"]` (dark-block `:root[data-theme="x"]` becomes
// `.sim-preview[data-appearance="dark"][data-theme="x"]`): pass that compound as `wrapper` and the
// same merge rule does the rest, since the wrapper itself is just another compound to merge onto.
//
// This file is the runtime (JS) half. The sync-time (Python) transform WA writes will share
// `scripts/theme_sim/rescope_fixture.json` with this module's test (see check_theme_sim.mjs),
// so neither one can drift from the other or from this comment.

const DEFAULT_WRAPPER = ".sim-preview";
const DARK_WRAPPER = '.sim-preview[data-appearance="dark"]';
const ROOT_LIKE = new Set([":root", "html", "body"]);
// A leading compound that is *only* `:root`, `:root[data-theme…]`, or `[data-theme…]` on its own,
// with nothing else attached (no other attribute, class or pseudo-class in the compound).
const LEADING_ATTR = /^:root(\[data-theme(?:="[^"]*")?\])?$|^(\[data-theme(?:="[^"]*")?\])$/;

/** The index of the first top-level whitespace in `selector` (not inside `[...]` or `(...)`), or -1. */
function topLevelSpace(selector) {
  let depth = 0;
  for (let i = 0; i < selector.length; i++) {
    const c = selector[i];
    if (c === "[" || c === "(") depth++;
    else if (c === "]" || c === ")") depth--;
    else if (depth === 0 && /\s/.test(c)) return i;
  }
  return -1;
}

/** Rescopes one simple/compound selector (no commas). `wrapper` is the compound to merge onto or
 * replace the leading `:root`/`html`/`body`/`[data-theme…]`, `.sim-preview` by default. */
export function rescopeSelector(selector, wrapper = DEFAULT_WRAPPER) {
  const trimmed = selector.trim();
  const idx = topLevelSpace(trimmed);
  const head = idx === -1 ? trimmed : trimmed.slice(0, idx);
  const rest = idx === -1 ? "" : trimmed.slice(idx); // includes its own leading whitespace/combinator

  if (ROOT_LIKE.has(head)) {
    return rest ? wrapper + rest : wrapper;
  }
  const match = head.match(LEADING_ATTR);
  if (match) {
    const attr = match[1] || match[2] || "";
    return wrapper + attr + rest;
  }
  return `${wrapper} ${trimmed}`;
}

/** Rescopes a comma-separated selector list. */
export function rescopeSelectorList(selectorList, wrapper = DEFAULT_WRAPPER) {
  return selectorList
    .split(",")
    .map((part) => rescopeSelector(part, wrapper))
    .join(", ");
}

/** Splits `css` into top-level rules and `@media` blocks, tolerant of nested braces (declaration
 * values in this kit's generated CSS never contain `{`/`}`, so a naive brace counter is enough). */
function splitTopLevel(css) {
  const blocks = [];
  let i = 0;
  while (i < css.length) {
    while (i < css.length && /\s/.test(css[i])) i++;
    if (i >= css.length) break;
    const headerStart = i;
    let depth = 0;
    while (i < css.length) {
      const c = css[i];
      if (c === "{") {
        if (depth === 0) {
          const header = css.slice(headerStart, i).trim();
          const bodyStart = i + 1;
          let bodyDepth = 1;
          i = bodyStart;
          while (i < css.length && bodyDepth > 0) {
            if (css[i] === "{") bodyDepth++;
            else if (css[i] === "}") bodyDepth--;
            if (bodyDepth > 0) i++;
          }
          blocks.push({ header, body: css.slice(bodyStart, i) });
          i++; // consume the closing brace
          break;
        }
        depth++;
      } else if (c === "}") {
        depth--;
      }
      i++;
    }
  }
  return blocks;
}

const DARK_MEDIA = /^@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)$/;

/** Rescopes a whole stylesheet: every top-level rule under `wrapper`, every rule inside
 * `@media (prefers-color-scheme: dark) { … }` unwrapped under `.sim-preview[data-appearance="dark"]`
 * (or `wrapper` with that attribute merged on, if `wrapper` already carries a leading compound). */
export function rescopeCSS(css, wrapper = DEFAULT_WRAPPER) {
  let out = "";
  for (const { header, body } of splitTopLevel(css)) {
    if (DARK_MEDIA.test(header)) {
      const darkWrapper = wrapper === DEFAULT_WRAPPER ? DARK_WRAPPER : mergeDarkAttribute(wrapper);
      for (const inner of splitTopLevel(body)) {
        out += `${rescopeSelectorList(inner.header, darkWrapper)} {${inner.body}}\n`;
      }
      continue;
    }
    out += `${rescopeSelectorList(header, wrapper)} {${body}}\n`;
  }
  return out;
}

function mergeDarkAttribute(wrapper) {
  return wrapper.includes('data-appearance="dark"') ? wrapper : `${wrapper}[data-appearance="dark"]`;
}

export const SIM_PREVIEW_WRAPPER = DEFAULT_WRAPPER;
export const SIM_PREVIEW_DARK_WRAPPER = DARK_WRAPPER;
