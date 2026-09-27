// Port of mars-dawn-kit Sources/MarsDawnThemes/ThemeGrammar.swift (read at origin/release-0.6.1,
// f1c66e16509e). Byte-level (here: UTF-16 code-unit-level, which agrees with the kit's UTF-8 byte
// walk for the ASCII-only grammars below) patterns, kept a line-for-line match to the Swift so the
// two can't drift silently. This is a *port*, hand-kept in sync, not vendored data: unlike
// styles-data.js/built-ins.js (which now load their data from vendor/kit-themes/<tag>/, WA), logic
// has no JSON form in the kit to load instead, so it stays a hand-kept copy, checked for drift by
// scripts/check_theme_sim.mjs's parity run against the vendored fixtures and expected-css.

export const MAX_ID_LENGTH = 32;

function isDigit(c) {
  return c >= "0" && c <= "9";
}
function isLowerLetter(c) {
  return c >= "a" && c <= "z";
}
function isUpperLetter(c) {
  return c >= "A" && c <= "Z";
}
function isLetter(c) {
  return isLowerLetter(c) || isUpperLetter(c);
}
function isLowerAlnum(c) {
  return isLowerLetter(c) || isDigit(c);
}
function isHexDigit(c) {
  return isDigit(c) || (c >= "a" && c <= "f") || (c >= "A" && c <= "F");
}

/** `^[a-z0-9]+(-[a-z0-9]+)*$`, 1...32 chars, ASCII only. */
export function isThemeID(text) {
  if (!text || text.length > MAX_ID_LENGTH) return false;
  let previousWasHyphen = true;
  for (const c of text) {
    if (c.length !== 1 || c.codePointAt(0) > 0x7f) return false;
    if (c === "-") {
      if (previousWasHyphen) return false;
      previousWasHyphen = true;
    } else if (isLowerAlnum(c)) {
      previousWasHyphen = false;
    } else {
      return false;
    }
  }
  return !previousWasHyphen;
}

/** Exactly `#` followed by six ASCII hex digits (either case). */
export function isHexColor(text) {
  if (text.length !== 7 || text[0] !== "#") return false;
  for (let i = 1; i < 7; i++) {
    const c = text[i];
    if (c.codePointAt(0) > 0x7f || !isHexDigit(c)) return false;
  }
  return true;
}

/** Test-only hook (scripts/check_theme_sim.mjs's "lowercase hex is accepted" control): swaps in a
 * replacement for `isHexColor` and returns the previous one, so the check can plant a broken
 * (e.g. uppercase-only) grammar, confirm validation then fails through the real pipeline, and
 * restore the original -- never used at runtime. A function declaration's binding is reassignable
 * from within its own module, and `import * as Grammar` sees the live binding either way, so
 * `Grammar.isHexColor` reflects this from the outside without validator.js changing at all. */
export function __setIsHexColorForTest(fn) {
  const previous = isHexColor;
  isHexColor = fn;
  return previous;
}

/** `MAJOR.MINOR.PATCH`, each 1-4 ASCII digits. */
export function isVersion(text) {
  const parts = text.split(".");
  if (parts.length !== 3) return false;
  return parts.every((part) => {
    if (part.length < 1 || part.length > 4) return false;
    for (const c of part) {
      if (c.codePointAt(0) > 0x7f || !isDigit(c)) return false;
    }
    return true;
  });
}

/** 1-64 ASCII letters, digits, `.`, `-`, `+`, starting with a letter. */
export function isLicense(text) {
  if (text.length < 1 || text.length > 64) return false;
  const first = text[0];
  if (first.codePointAt(0) > 0x7f || !isLetter(first)) return false;
  for (const c of text) {
    if (c.codePointAt(0) > 0x7f) return false;
    if (!(isLetter(c) || isDigit(c) || c === "." || c === "-" || c === "+")) return false;
  }
  return true;
}

/** GitHub's username rule: 1-39 ASCII letters, digits and single hyphens. */
export function isGitHubUsername(text) {
  if (text.length < 1 || text.length > 39) return false;
  let previousWasHyphen = true;
  for (const c of text) {
    if (c.codePointAt(0) > 0x7f) return false;
    if (c === "-") {
      if (previousWasHyphen) return false;
      previousWasHyphen = true;
    } else if (isLetter(c) || isDigit(c)) {
      previousWasHyphen = false;
    } else {
      return false;
    }
  }
  return !previousWasHyphen;
}

/** A BCP-47 subset: `ll`/`lll`, optional `-Ssss` script, optional `-RR` region. */
export function isLocaleKey(text) {
  const parts = text.split("-");
  const language = parts[0];
  if (!language || (language.length !== 2 && language.length !== 3)) return false;
  for (const c of language) if (!isLowerLetter(c)) return false;
  let rest = parts.slice(1);
  if (rest.length && rest[0].length === 4) {
    const script = rest[0];
    if (!isUpperLetter(script[0])) return false;
    for (const c of script.slice(1)) if (!isLowerLetter(c)) return false;
    rest = rest.slice(1);
  }
  if (rest.length) {
    const region = rest[0];
    if (region.length !== 2) return false;
    for (const c of region) if (!isUpperLetter(c)) return false;
    rest = rest.slice(1);
  }
  return rest.length === 0;
}
