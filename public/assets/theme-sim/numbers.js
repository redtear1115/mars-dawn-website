// Port of ThemeNumbers.swift (kit origin/release-0.6.1, d6eae71): the bounded numbers of design
// §4.3, and the one way the kit writes a number into CSS. See grammar.js's header note: a port,
// not vendored data.

export const THEME_NUMBERS = {
  bodySize: { range: [14, 18], step: 1 },
  lineHeight: { range: [1.4, 1.9], step: 0.05 },
  headingWeight: { range: [400, 900], step: 50 },
  radius: { range: [0, 16], step: 1 },
  maxWidth: { range: [600, 1000], step: 1 },
  "h1.size": { range: [1.8, 2.4], step: 0.1 },
  "h1.letterSpacing": { range: [-0.03, 0.03], step: 0.005 },
  "h2.letterSpacing": { range: [-0.03, 0.03], step: 0.005 },
  "blockquote.style.width": { range: [2, 4], step: 1 },
  "hr.style.thickness": { range: [1, 4], step: 1 },
};

const SANITY_BOUND = 1_000_000;

/** The value snapped to `step`, or null if it isn't finite or the snapped value is outside
 * `range`. Mirrors the Swift thousandths re-derivation so JS floating point can't disagree. */
export function snapped(name, value) {
  const { range, step } = THEME_NUMBERS[name];
  if (!Number.isFinite(value) || Math.abs(value) > SANITY_BOUND) return null;
  const steps = Math.round(value / step);
  let result = steps * step;
  result = Math.round(result * 1000) / 1000;
  if (result === 0) result = 0; // -0 -> 0
  if (result < range[0] || result > range[1]) return null;
  return result;
}

/** The generator's own check (defence in depth): finite, inside range, on a step. */
export function isAcceptable(name, value) {
  const s = snapped(name, value);
  if (s === null) return false;
  return Math.abs(s - value) <= 1e-9;
}

/** Fixed-point, at most three decimals, `.` separator, no exponent, no trailing zeros, never `-0`. */
export function cssNumber(value) {
  const thousandths = Math.round(value * 1000);
  if (thousandths === 0) return "0";
  const sign = thousandths < 0 ? "-" : "";
  const magnitude = Math.abs(thousandths);
  const whole = Math.floor(magnitude / 1000);
  let fraction = magnitude % 1000;
  if (fraction === 0) return `${sign}${whole}`;
  let digits = 3;
  while (fraction % 10 === 0) {
    fraction /= 10;
    digits -= 1;
  }
  const fractionText = String(fraction).padStart(digits, "0");
  return `${sign}${whole}.${fractionText}`;
}
