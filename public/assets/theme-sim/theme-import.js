// The one guarded path every theme.json import goes through: paste, drop, the file picker and the
// "Load this JSON" button (plan PLAN-web-theme-tuning W2a). DOM-free on purpose, so
// scripts/check_theme_sim.mjs tests exactly what the page runs.
//
// Order (fixed by the plan):
//   1. bytes only (drop, file picker): UTF-8 decode, refusing invalid UTF-8 (`decodeThemeBytes`);
//      a paste is already a string and starts at 2;
//   2. validator.js's decodeThemeText: the 16 KiB byte cap, the duplicate-key/depth scan,
//      JSON.parse and the strict decode, the same stages validate() runs;
//   3. the `__proto__` guard: decode drops a `__proto__` key inside name/summary without reporting
//      it (decodeLocalizedText copies with plain assignment), so the raw JSON is walked for one;
//   4. schemaVersion must be 1 (decode alone accepts any number);
//   5. the result is the *decoded* document, never the raw parse.
// Any failure returns `{ issue }` and the caller leaves its state alone.

import { decodeThemeText, schemaVersionIssue, MAX_FILE_BYTES } from "./validator.js";
import { quote as quoteText } from "./text.js";

export { MAX_FILE_BYTES };

/** The rule id of the guard's own refusal (not a validate() rule: validate() never sees it). */
export const PROTO_KEY_RULE = "import.protoKey";
export const PROTO_KEY_MESSAGE = "is not an allowed key name";

/** The refusal for a file over the byte cap, worded as validate()'s own file.tooLarge. */
export function tooLargeIssue() {
  return { rule: "file.tooLarge", path: "", message: `the file is larger than ${MAX_FILE_BYTES} bytes` };
}

/** UTF-8 text from a file's bytes (an ArrayBuffer or a typed array), or `{ issue }` when the bytes
 * aren't valid UTF-8. */
export function decodeThemeBytes(bytes) {
  try {
    return { text: new TextDecoder("utf-8", { fatal: true }).decode(bytes) };
  } catch {
    return { issue: { rule: "file.encoding", path: "", message: "the file is not valid UTF-8" } };
  }
}

/** The path of the first own `__proto__` key anywhere in an already-parsed JSON value, or null.
 * Paths are written as validator.js writes them (keys quoted for display, `[i]` for array items). */
export function findProtoKey(value, path = "") {
  if (Array.isArray(value)) {
    for (let i = 0; i < value.length; i++) {
      const hit = findProtoKey(value[i], `${path}[${i}]`);
      if (hit !== null) return hit;
    }
    return null;
  }
  if (value === null || typeof value !== "object") return null;
  for (const key of Object.keys(value)) {
    const here = path ? `${path}.${quoteText(key)}` : quoteText(key);
    if (key === "__proto__") return here;
    const hit = findProtoKey(value[key], here);
    if (hit !== null) return hit;
  }
  return null;
}

/** Guards one theme.json text. Returns `{ document }` (the decoded document, as plain JSON data)
 * or `{ issue }` (`{ rule, path, message }`), never throwing for a string input. */
export function importThemeText(text) {
  if (typeof text !== "string") return { issue: { rule: "json.malformed", path: "", message: "the file is not valid JSON" } };
  const decoded = decodeThemeText(text);
  if (decoded.issue) return { issue: decoded.issue };
  const protoPath = findProtoKey(JSON.parse(text));
  if (protoPath !== null) return { issue: { rule: PROTO_KEY_RULE, path: protoPath, message: PROTO_KEY_MESSAGE } };
  const versionIssue = schemaVersionIssue(decoded.document);
  if (versionIssue) return { issue: versionIssue };
  // Plain data: decode leaves absent optional fields as `undefined`; the state holds only what the
  // file had, so Copy JSON gives back what came in.
  return { document: JSON.parse(JSON.stringify(decoded.document)) };
}

/** Guards one file's bytes: UTF-8 first, then importThemeText. */
export function importThemeBytes(bytes) {
  const decoded = decodeThemeBytes(bytes);
  if (decoded.issue) return { issue: decoded.issue };
  return importThemeText(decoded.text);
}
