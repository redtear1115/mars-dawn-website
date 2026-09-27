// Port of ThemeText.swift (kit origin/release-0.6.1, d6eae71): display-string rules for `name`,
// `summary`, `author.name`, and the message-safe quoting of attacker-chosen text.

export const NAME_LIMIT = 48;
export const SUMMARY_LIMIT = 120;
export const AUTHOR_NAME_LIMIT = 64;
export const MAX_COMBINING_RUN = 3;

const BIDI_CONTROLS = new Set([
  0x202a, 0x202b, 0x202c, 0x202d, 0x202e, 0x2066, 0x2067, 0x2068, 0x2069, 0x200e, 0x200f, 0x061c,
]);
const INVISIBLES = new Set([0xfeff, 0x200b, 0x2060]);

// Unicode general-category checks the browser can do natively via \p{} regexes (ES2018+).
const RE_WHITESPACE_ONLY = /^\p{White_Space}*$/u;
const RE_CONTROL_OR_SEPARATOR = /\p{Cc}|\p{Zl}|\p{Zp}/u;
const RE_COMBINING = /\p{Mn}|\p{Mc}|\p{Me}/u;

/** The NFC form of `text` and every rule it breaks (Problem order below). An empty `problems`
 * list means the string is fine as a display string. */
export function checkDisplayText(text, limit) {
  const normalized = text.normalize("NFC");
  const found = new Set();
  const scalars = Array.from(normalized); // code-point iteration, like Swift's unicodeScalars
  if (RE_WHITESPACE_ONLY.test(normalized)) found.add("text.empty");
  if (scalars.length > limit) found.add("text.length");
  let combiningRun = 0;
  for (const scalar of scalars) {
    if (RE_CONTROL_OR_SEPARATOR.test(scalar)) found.add("text.control");
    const cp = scalar.codePointAt(0);
    if (BIDI_CONTROLS.has(cp)) found.add("text.bidi");
    if (INVISIBLES.has(cp)) found.add("text.invisible");
    if (RE_COMBINING.test(scalar)) {
      combiningRun += 1;
      if (combiningRun > MAX_COMBINING_RUN) found.add("text.combining");
    } else {
      combiningRun = 0;
    }
  }
  const lowered = normalized.toLowerCase();
  if (lowered.includes("://") || lowered.includes("www.")) found.add("text.url");
  const order = ["text.empty", "text.length", "text.control", "text.bidi", "text.invisible", "text.combining", "text.url"];
  return { normalized, problems: order.filter((p) => found.has(p)) };
}

export const PROBLEM_SUMMARY = {
  "text.empty": "is empty",
  "text.length": "is too long",
  "text.control": "contains a control character or a line break",
  "text.bidi": "contains a bidirectional control character",
  "text.invisible": "contains an invisible format character",
  "text.combining": "stacks too many combining marks on one character",
  "text.url": "contains a link",
};

const QUOTE_CAP = 64;

function isPlainQuoteScalar(cp) {
  if ((cp >= 0x30 && cp <= 0x39) || (cp >= 0x41 && cp <= 0x5a) || (cp >= 0x61 && cp <= 0x7a)) return true;
  return [0x20, 0x5f, 0x2e, 0x2c, 0x2d, 0x23, 0x25, 0x2b, 0x3d].includes(cp);
}

/** Makes text that came from a theme file safe to repeat in a validation message. */
export function quote(text) {
  const scalars = Array.from(text);
  let out = "";
  let shown = 0;
  for (const scalar of scalars) {
    if (shown === QUOTE_CAP) {
      out += `...(${scalars.length - QUOTE_CAP} more)`;
      break;
    }
    shown += 1;
    const cp = scalar.codePointAt(0);
    if (isPlainQuoteScalar(cp)) {
      out += scalar;
    } else {
      out += `\\u{${cp.toString(16).toUpperCase()}}`;
    }
  }
  return out;
}
