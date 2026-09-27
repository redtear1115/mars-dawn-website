// Port of JSONStructureScan.swift (kit origin/release-0.6.1, d6eae71): a pre-pass over a
// theme.json's text, before JSON.parse sees it. JSON.parse silently keeps one value of a repeated
// object key, so this walks the grammar itself and refuses a repeat, and refuses nesting deeper
// than any theme needs.
//
// Operates on a JS string (UTF-16), not bytes; theme.json is JSON text, so the structural
// characters this cares about are always single ASCII code units regardless of encoding.

export const MAX_DEPTH = 16;

export class JSONScanError extends Error {
  constructor(kind, extra) {
    super(kind);
    this.kind = kind; // "duplicateKey" | "tooDeep" | "malformed"
    Object.assign(this, extra);
  }
}

/** Throws JSONScanError on a duplicate key or excessive nesting; otherwise returns silently. */
export function scanJSONStructure(text) {
  let index = 0;
  const stack = []; // { kind: "object", keys: Set, path: string[], pendingKey: string|null } | { kind: "array", path, index }

  function skipWhitespace() {
    while (index < text.length && " \t\n\r".includes(text[index])) index++;
  }
  function currentPath() {
    const top = stack[stack.length - 1];
    if (!top) return [];
    if (top.kind === "object") return [...top.path, top.pendingKey ?? ""];
    return [...top.path, String(top.index)];
  }
  function readString() {
    if (text[index] !== '"') throw new JSONScanError("malformed");
    index++;
    let out = "";
    while (index < text.length) {
      const ch = text[index];
      if (ch === '"') {
        index++;
        return out;
      }
      if (ch.charCodeAt(0) < 0x20) throw new JSONScanError("malformed");
      if (ch === "\\") {
        index++;
        if (index >= text.length) throw new JSONScanError("malformed");
        const esc = text[index];
        index++;
        switch (esc) {
          case '"': out += '"'; break;
          case "\\": out += "\\"; break;
          case "/": out += "/"; break;
          case "b": out += "\b"; break;
          case "f": out += "\f"; break;
          case "n": out += "\n"; break;
          case "r": out += "\r"; break;
          case "t": out += "\t"; break;
          case "u": {
            if (index + 4 > text.length) throw new JSONScanError("malformed");
            const hex = text.slice(index, index + 4);
            if (!/^[0-9a-fA-F]{4}$/.test(hex)) throw new JSONScanError("malformed");
            out += String.fromCharCode(parseInt(hex, 16));
            index += 4;
            break;
          }
          default:
            throw new JSONScanError("malformed");
        }
        continue;
      }
      out += ch;
      index++;
    }
    throw new JSONScanError("malformed");
  }
  function skipScalarLiteral() {
    const start = index;
    while (index < text.length) {
      const c = text[index];
      const isLiteral = (c >= "0" && c <= "9") || (c >= "a" && c <= "z") || c === "-" || c === "+" || c === "." || c === "E";
      if (!isLiteral) break;
      index++;
    }
    if (index === start) throw new JSONScanError("malformed");
  }
  function valueEnded() {
    const top = stack.pop();
    if (!top) return;
    if (top.kind === "object") stack.push({ ...top, pendingKey: null });
    else stack.push({ ...top, index: top.index + 1 });
  }
  function beginValue() {
    skipWhitespace();
    if (index >= text.length) throw new JSONScanError("malformed");
    const c = text[index];
    if (c === "{") {
      if (stack.length >= MAX_DEPTH) throw new JSONScanError("tooDeep");
      stack.push({ kind: "object", keys: new Set(), path: currentPath(), pendingKey: null });
      index++;
    } else if (c === "[") {
      if (stack.length >= MAX_DEPTH) throw new JSONScanError("tooDeep");
      stack.push({ kind: "array", path: currentPath(), index: 0 });
      index++;
    } else if (c === '"') {
      readString();
      valueEnded();
    } else {
      skipScalarLiteral();
      valueEnded();
    }
  }

  beginValue();
  while (stack.length) {
    skipWhitespace();
    if (index >= text.length) throw new JSONScanError("malformed");
    const c = text[index];
    const top = stack[stack.length - 1];
    if (top.kind === "object") {
      if (top.pendingKey === null) {
        if (c === "}") {
          index++;
          stack.pop();
          valueEnded();
          continue;
        }
        if (c === "," && top.keys.size > 0) {
          index++;
          skipWhitespace();
        } else if (top.keys.size > 0) {
          throw new JSONScanError("malformed");
        }
        const key = readString();
        if (top.keys.has(key)) throw new JSONScanError("duplicateKey", { path: top.path, key });
        top.keys.add(key);
        skipWhitespace();
        if (text[index] !== ":") throw new JSONScanError("malformed");
        index++;
        top.pendingKey = key;
        beginValue();
      } else {
        throw new JSONScanError("malformed");
      }
    } else {
      if (c === "]") {
        index++;
        stack.pop();
        valueEnded();
        continue;
      }
      if (top.index > 0) {
        if (c !== ",") throw new JSONScanError("malformed");
        index++;
      }
      beginValue();
    }
  }
  skipWhitespace();
  if (index !== text.length) throw new JSONScanError("malformed");
}
