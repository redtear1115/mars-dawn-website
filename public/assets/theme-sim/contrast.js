// Port of ThemeContrast.swift (kit origin/release-0.6.1, d6eae71). WCAG 2.x contrast between
// #RRGGBB colours, and the sRGB color-mix the stylesheet uses. Only ever called with colours
// grammar.js's isHexColor accepted.

function components(hex) {
  const value = parseInt(hex.slice(1), 16) || 0;
  return [(value >> 16) & 0xff, (value >> 8) & 0xff, value & 0xff].map((v) => v / 255);
}

export function luminance(hex) {
  const linear = components(hex).map((v) => (v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4)));
  return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2];
}

export function ratio(a, b) {
  const x = luminance(a);
  const y = luminance(b);
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
}

/** `color-mix(in srgb, a, b amount)`: gamma-encoded interpolation, rounded to the nearest 8-bit
 * value, as WebKit paints it. */
export function mix(a, b, amount) {
  const mixed = components(a).map((ca, i) => {
    const cb = components(b)[i];
    return (ca * (1 - amount) + cb * amount) * 255;
  });
  const hex = mixed.map((v) => Math.round(v).toString(16).padStart(2, "0").toUpperCase());
  return `#${hex.join("")}`;
}

/** Two decimals, truncated (not rounded), so a failing 4.496 never prints as a passing "4.50". */
export function format(r) {
  const hundredths = Math.floor(r * 100 + 1e-9);
  const fraction = hundredths % 100;
  return `${Math.floor(hundredths / 100)}.${fraction < 10 ? "0" : ""}${fraction}`;
}
