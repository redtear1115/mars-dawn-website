#!/usr/bin/env node
// Parity check for the theme simulator's JavaScript ports (plan-website-104 W1, design
// theme-ecosystem-design.md §6.2's "a rule that exists in only one of them fails CI").
//
// Plain ES modules, no npm dependency: runs under the `node` already on the CI image.
//
// Reads the kit's theme contract from the ONE vendored source, vendor/kit-themes/<sha12>/
// (scripts/sync_theme_kit.py, WA), the same tree scripts/check_theme_kit.py holds to a manifest
// and to GitHub. This script never embeds a second copy of that data (styles-data.js and
// built-ins.js load it at runtime -- from here in Node, from the copy build_pages.py's
// sync_theme_kit_assets_into_public() places under public/assets/theme-sim/kit/ in the browser).
//
// What this checks:
//   1. The .sim-preview rescoping transform against the shared fixture
//      (scripts/theme_sim/rescope_fixture.json): every selector and stylesheet case, the four
//      rev-4 examples, and the "regressions" (a leading/inline comment, a non-dark @media
//      condition) that exercise the two bugs this port shared with the sync-time Python half
//      before both were fixed. Every selector in every adopted sheet must start with
//      `.sim-preview` (a generator bug can't restyle Submit or the messages panel).
//   2. Every kit fixture (valid/invalid/hostile/publish) and the option sweep: this port's verdict
//      and rule ids must equal expected-messages.json's (exact rule, or wording where
//      expected-messages.json names one), and its generated CSS must equal expected-css/ byte for
//      byte, for every valid fixture, every built-in and every sweep theme.
//   3. Three permanent controls, each reverted immediately after: a lineHeight formatting change,
//      an uppercase-only hex grammar, and a dropped CSS fragment each turn exactly the comparison
//      they touch red, and nothing else.
//   4. The live preview (preview-report.js, website#150): for every invalid/ and publish/ fixture,
//      whether the preview may draw it, against a literal table written below (never read from
//      the module's own constant); that a drawn fixture's CSS carries none of its offending
//      values; that every valid/ fixture previews with exactly its expected CSS, only the scope id
//      differing; that the preview CSS is scoped to PREVIEW_ID; that the generator refuses closed
//      values it never decoded; the scope guard; and the Submit decision under a refusing
//      generator.
//
// Without vendor/kit-themes/<tag>/, none of this can run for real, so this script fails loudly and
// immediately with its own message rather than silently reporting success it didn't earn.

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(here, "..");
const assetsDir = path.join(repoRoot, "public", "assets", "theme-sim");

const { rescopeSelector, rescopeCSS } = await import(path.join(assetsDir, "rescope.js"));
const Validator = await import(path.join(assetsDir, "validator.js"));
const Generator = await import(path.join(assetsDir, "generator.js"));
const StylesData = await import(path.join(assetsDir, "styles-data.js"));
const BuiltIns = await import(path.join(assetsDir, "built-ins.js"));
const Grammar = await import(path.join(assetsDir, "grammar.js"));
const Preview = await import(path.join(assetsDir, "preview-report.js"));
const TextModule = await import(path.join(assetsDir, "text.js"));

let failures = 0;
function ok(label) {
  console.log(`  ok  ${label}`);
}
function bad(label, detail) {
  failures += 1;
  console.log(`FAIL  ${label}${detail ? `: ${detail}` : ""}`);
}

// --- 0. Locate the vendor tree and load it (the one source) -----------------------------------

function findVendorDir() {
  const vendorRoot = path.join(repoRoot, "vendor", "kit-themes");
  if (!existsSync(vendorRoot)) return null;
  const tags = readdirSync(vendorRoot).filter((name) => existsSync(path.join(vendorRoot, name, "ThemeStyles.json")));
  return tags.length === 1 ? path.join(vendorRoot, tags[0]) : null;
}

const vendorDir = findVendorDir();
if (!vendorDir) {
  console.log("FAIL  vendor/kit-themes/<tag>/ThemeStyles.json not found (or more than one <tag>/ present).");
  console.log("Run scripts/sync_theme_kit.py (macOS + a local mars-dawn-kit clone) and commit the result.");
  console.log("Nothing below can run without it, so this check refuses to report a partial pass.");
  process.exit(1);
}
console.log(`Loading the kit's theme contract from ${path.relative(repoRoot, vendorDir)}`);
StylesData.setThemeStyles(JSON.parse(readFileSync(path.join(vendorDir, "ThemeStyles.json"), "utf8")));
BuiltIns.setBuiltIns(
  Object.fromEntries(
    BuiltIns.BUILT_IN_ORDER.map((id) => [id, readFileSync(path.join(vendorDir, "Themes", id, "theme.json"), "utf8")])
  )
);
const { BUILT_IN_ORDER } = BuiltIns;

// --- 1. Rescoping transform fixture ----------------------------------------------------------

function checkRescope() {
  console.log("\nRescoping transform (scripts/theme_sim/rescope_fixture.json)");
  const fixturePath = path.join(repoRoot, "scripts", "theme_sim", "rescope_fixture.json");
  const fixture = JSON.parse(readFileSync(fixturePath, "utf8"));
  for (const c of fixture.selectors) {
    const got = rescopeSelector(c.selector, c.wrapper ?? fixture.wrapper);
    if (got === c.expected) ok(`selector ${c.name}`);
    else bad(`selector ${c.name}`, `got ${JSON.stringify(got)}, expected ${JSON.stringify(c.expected)}`);
  }
  for (const sheet of fixture.stylesheets) {
    const rescoped = rescopeCSS(sheet.css, fixture.wrapper);
    for (const expectedSelector of sheet.expectedSelectors) {
      if (rescoped.includes(expectedSelector)) ok(`stylesheet ${sheet.name}: contains ${expectedSelector}`);
      else bad(`stylesheet ${sheet.name}`, `missing selector ${JSON.stringify(expectedSelector)} in:\n${rescoped}`);
    }
    // Every selector in the rescoped output must live under the wrapper (security property W1
    // Done-when: "a test asserts every selector in every adopted sheet starts with .sim-preview").
    for (const line of rescoped.split("\n")) {
      const brace = line.indexOf("{");
      if (brace === -1) continue;
      const selectorList = line.slice(0, brace).trim();
      if (!selectorList) continue;
      for (const sel of selectorList.split(",")) {
        if (!sel.trim().startsWith(".sim-preview")) bad(`stylesheet ${sheet.name}: scope escape`, JSON.stringify(sel));
      }
    }
  }
  // Regressions: cases whose correctly-rescoped output legitimately contains a line that doesn't
  // start with .sim-preview (an @media wrapper condition, which names no element), so they're
  // checked by exact equality instead of the generic per-line assertion above.
  for (const r of fixture.regressions ?? []) {
    const got = rescopeCSS(r.css, fixture.wrapper);
    if (got === r.expected) ok(`regression ${r.name}`);
    else bad(`regression ${r.name}`, `got ${JSON.stringify(got)}, expected ${JSON.stringify(r.expected)}`);
  }
}

// --- 2. Built-in smoke test ---------------------------------------------------------------------

function checkBuiltIns() {
  console.log("\nBuilt-in themes (decode, validate, generate)");
  for (const id of BUILT_IN_ORDER) {
    const text = BuiltIns.BUILT_IN_THEME_JSON[id];
    const report = Validator.validate(text, { requireComplete: true });
    if (report.issues.length !== 0) {
      bad(`${id}: validates clean`, JSON.stringify(report.issues));
      continue;
    }
    ok(`${id}: validates clean`);
    if (id === "dawn") Validator.setDawnFallback(report.theme.light, report.theme.dark);
    try {
      const { variables, rules } = Generator.stylesheetFor(report.theme);
      if (variables.includes("{{") || rules.includes("{{")) bad(`${id}: no unresolved placeholder`);
      else ok(`${id}: generates CSS with no unresolved placeholder`);
    } catch (e) {
      // A validated theme that the generator then refuses is a real bug (the generator re-checks
      // everything the validator already passed, defence in depth) -- but it's this one fixture's
      // bug, not a reason to crash the whole run and hide every other result. See
      // Generator.GeneratorRefusal.
      bad(`${id}: generates CSS with no unresolved placeholder`, `generator refused a validated theme: ${e}`);
    }
  }
}

// --- 3. Vendor-backed parity: every fixture, every built-in, the whole sweep -------------------

function loadFixtures(dir) {
  const out = [];
  for (const category of ["valid", "invalid", "hostile", "publish"]) {
    const categoryDir = path.join(dir, "ThemeFixtures", category);
    if (!existsSync(categoryDir)) continue;
    for (const name of readdirSync(categoryDir)) {
      if (!name.endsWith(".json")) continue;
      out.push({ category, name, text: readFileSync(path.join(categoryDir, name), "utf8") });
    }
  }
  return out;
}

// A fixture's expected rule is its filename before "--" (kit ThemeFixtureTests.swift's own
// convention: "invalid themes named `<rule>--<case>.json` that must fail with **exactly** that
// rule").
function ruleOf(name) {
  return name.replace(/\.json$/, "").split("--", 1)[0];
}

function expectCSSMatch(label, expectedCSSDir, expectedCSSName, report) {
  const cssPath = path.join(expectedCSSDir, expectedCSSName);
  if (!existsSync(cssPath) || !report.theme) return;
  const want = JSON.parse(readFileSync(cssPath, "utf8"));
  // A validated theme that the generator then refuses (Generator.GeneratorRefusal) is a real bug
  // worth a red line of its own -- never a crash that hides every fixture after it.
  try {
    const { variables, rules } = Generator.stylesheetFor(report.theme);
    if (variables === want.variables && rules === want.rules) ok(`${label}: css matches expected-css`);
    else bad(`${label}: css`, "generated CSS does not match expected-css");
  } catch (e) {
    bad(`${label}: css`, `generator refused a validated theme: ${e}`);
  }
}

function checkVendorParity() {
  console.log(`\nVendor-backed parity (${path.relative(repoRoot, vendorDir)})`);
  const expectedMessages = JSON.parse(readFileSync(path.join(vendorDir, "ThemeFixtures", "expected-messages.json"), "utf8"));
  const expectedCSSDir = path.join(vendorDir, "expected-css");

  for (const { category, name, text } of loadFixtures(vendorDir)) {
    if (category === "valid") {
      const report = Validator.validate(text);
      if (report.issues.length === 0 && report.theme) ok(`valid/${name}: validates clean`);
      else bad(`valid/${name}`, `expected no issues, got ${JSON.stringify(report.issues)}`);
      expectCSSMatch(`valid/${name}`, expectedCSSDir, `valid__${name}`, report);
      continue;
    }
    if (category === "hostile") {
      const report = Validator.validate(text);
      if (report.issues.length > 0 && !report.theme) ok(`hostile/${name}: refused`);
      else bad(`hostile/${name}`, "expected at least one issue and no theme");
      for (const issue of report.issues) {
        const combined = `${issue.rule} ${issue.path} ${issue.message}`;
        if (/[\u0000-\u001f\u007f]/.test(combined)) bad(`hostile/${name}: control character survived`, combined);
        if (combined.includes("https://") || combined.includes("@someuser")) bad(`hostile/${name}: attacker text survived`, combined);
      }
      continue;
    }
    // invalid/ and publish/: exactly one rule, the one the filename names.
    const expectedRule = ruleOf(name);
    const requireComplete = category === "publish";
    const report = Validator.validate(text, { requireComplete });
    const gotRules = [...new Set(report.issues.map((i) => i.rule))];
    if (report.theme === null && gotRules.length === 1 && gotRules[0] === expectedRule) {
      ok(`${category}/${name}: exactly ${expectedRule}`);
    } else {
      bad(`${category}/${name}`, `want only [${expectedRule}], got ${JSON.stringify(report.issues)}`);
    }
    const wantMessage = expectedMessages[name];
    if (wantMessage) {
      if (report.issues.some((i) => i.message === wantMessage)) ok(`${category}/${name}: message matches expected-messages.json`);
      else bad(`${category}/${name}: message`, `no issue says ${JSON.stringify(wantMessage)}; got ${JSON.stringify(report.issues.map((i) => i.message))}`);
    }
    if (category === "publish") {
      const loaded = Validator.validate(text);
      if (loaded.issues.length === 0 && loaded.theme) ok(`publish/${name}: loads without requireComplete`);
      else bad(`publish/${name}: loads without requireComplete`, JSON.stringify(loaded.issues));
    }
  }

  for (const id of BUILT_IN_ORDER) {
    const report = Validator.validate(BuiltIns.BUILT_IN_THEME_JSON[id], { requireComplete: true });
    expectCSSMatch(`built-in ${id}`, expectedCSSDir, `${id}.json`, report);
  }

  const sweepDir = path.join(vendorDir, "sweep");
  if (existsSync(sweepDir)) {
    for (const name of readdirSync(sweepDir)) {
      if (!name.endsWith(".json")) continue;
      const text = readFileSync(path.join(sweepDir, name), "utf8");
      const report = Validator.validate(text);
      if (report.issues.length === 0 && report.theme) ok(`sweep/${name}: validates clean`);
      else bad(`sweep/${name}`, `expected no issues, got ${JSON.stringify(report.issues)}`);
      expectCSSMatch(`sweep/${name}`, expectedCSSDir, `sweep__${name}`, report);
    }
  }
}

// --- 4. Permanent controls, each reverted immediately after --------------------------------------

function checkLowercaseHexControl() {
  console.log("\nControls");
  // The kit accepts a hex colour "either case" (ThemeGrammar.isHexColor). A validator that
  // quietly started requiring uppercase would still pass every vendored fixture (the kit's own
  // fixtures are all written uppercase), so this control exists to catch exactly that regression
  // on its own, and to prove it actually would: first the permanent regression guard (a lowered
  // built-in validates clean through the real, unmodified pipeline), then the plant itself (an
  // uppercase-only grammar swapped in through grammar.js's own test hook -- a live binding, so
  // validator.js's `Grammar.isHexColor` calls see it without validator.js changing at all),
  // confirming the same lowered theme is then refused, before restoring the real grammar and
  // reconfirming green.
  const lowered = BuiltIns.BUILT_IN_THEME_JSON.dawn.replace("#FFFDFB", "#fffdfb");
  const before = Validator.validate(lowered);
  if (before.issues.length === 0 && before.theme) ok("lowercase hex colour is accepted (either case, per the kit's grammar)");
  else bad("lowercase hex colour is accepted", JSON.stringify(before.issues));

  const previous = Grammar.__setIsHexColorForTest((text) => /^#[0-9A-F]{6}$/.test(text));
  const planted = Validator.validate(lowered);
  Grammar.__setIsHexColorForTest(previous);
  if (planted.issues.some((i) => i.rule === "color.hex") && !planted.theme) {
    ok("an uppercase-only hex grammar turns the lowercase-colour check red (color.hex)");
  } else {
    bad("an uppercase-only hex grammar turns the lowercase-colour check red", JSON.stringify(planted.issues));
  }
  const restored = Validator.validate(lowered);
  if (restored.issues.length === 0 && restored.theme) ok("hex grammar restored after the control");
  else bad("hex grammar restored after the control", JSON.stringify(restored.issues));
}

function checkLineHeightFormattingChangeIsRed() {
  // Planted control: a formatting bug in the number-to-CSS conversion (numbers.js's cssNumber)
  // must turn the classic built-in's css-parity check red, since Classic sets lineHeight: 1.75.
  const report = Validator.validate(BuiltIns.BUILT_IN_THEME_JSON.classic, { requireComplete: true });
  const expectedCSSDir = path.join(vendorDir, "expected-css");
  const want = JSON.parse(readFileSync(path.join(expectedCSSDir, "classic.json"), "utf8"));
  let good;
  try {
    good = Generator.stylesheetFor(report.theme);
  } catch (e) {
    bad("lineHeight formatting control: baseline", `generator refused classic: ${e}`);
    return;
  }
  if (good.rules !== want.rules) {
    bad("lineHeight formatting control: baseline", "classic's css doesn't match expected-css before any mutation");
    return;
  }
  // The mutation: format with a trailing zero the kit's formatter never emits (1.750 vs 1.75).
  const mutated = good.rules.replace("--line-height: 1.75;", "--line-height: 1.750;");
  if (mutated !== want.rules) ok("lineHeight formatting change turns the css-parity check red");
  else bad("lineHeight formatting change turns the css-parity check red", "mutation had no effect");
}

function checkDroppedFragmentIsRefused() {
  // A style option value with no CSS fragment must refuse the whole theme rather than silently
  // drawing it without that option (ThemeCSSGenerator.Refusal.unresolvedPlaceholder). Proven by
  // actually removing one entry from the loaded fragment table (Vivid's own `tableHeader.filled`),
  // confirming Vivid then refuses to generate, and restoring it so nothing else this script runs
  // sees the mutation.
  const removed = StylesData.FRAGMENTS.tableHeader.filled;
  delete StylesData.FRAGMENTS.tableHeader.filled;
  try {
    Generator.checkedRules("vivid", { table: { header: { type: "filled", background: "heading", text: "background" } } });
    bad("a style option with a dropped fragment is refused", "did not throw");
  } catch (e) {
    if (e instanceof Generator.GeneratorRefusal && e.kind === "unresolvedPlaceholder") {
      ok("a style option with a dropped fragment is refused (unresolvedPlaceholder)");
    } else {
      bad("a style option with a dropped fragment is refused", `wrong error: ${e}`);
    }
  } finally {
    StylesData.FRAGMENTS.tableHeader.filled = removed;
  }
  // Prove the restore worked, so this control can't leave the suite silently broken behind it.
  const { css } = Generator.checkedRules("vivid", { table: { header: { type: "filled", background: "heading", text: "background" } } });
  if (css.includes("var(--heading)")) ok("fragment table restored after the control");
  else bad("fragment table restored after the control", "tableHeader.filled still missing");
}

// --- 5. The live preview (preview-report.js, website#150) ---------------------------------------

// Whether the preview may draw each invalid/ and publish/ fixture. Written out by hand, on purpose:
// a table derived from preview-report.js's PREVIEW_BLOCKING_RULES would agree with any change to
// it, so it could never catch one. A rule that blocks the preview means the document doesn't decode
// or a value that reaches the CSS isn't one the generator may write; everything else is listed but
// drawn.
const EXPECTED_PREVIEWABLE = {
  "invalid/author.github--hyphen-edges.json": true,
  "invalid/color.hex--arabic-indic.json": false,
  "invalid/color.hex--css-injection.json": false,
  "invalid/color.hex--full-width.json": false,
  "invalid/color.hex--named.json": false,
  "invalid/color.hex--nul.json": false,
  "invalid/color.hex--short.json": false,
  "invalid/color.hex--trailing-newline.json": false,
  "invalid/color.hex--url.json": false,
  "invalid/color.hex--var.json": false,
  "invalid/contrast.baseline--dark-text.json": true,
  "invalid/contrast.pair--mm-text-equals-mm-node.json": true,
  "invalid/contrast.pair--muted-equals-surface.json": true,
  "invalid/contrast.scenario--formal-output-accent.json": true,
  "invalid/id.pattern--33-chars.json": true,
  "invalid/id.pattern--carriage-return.json": true,
  "invalid/id.pattern--combining-mark.json": true,
  "invalid/id.pattern--double-hyphen.json": true,
  "invalid/id.pattern--full-width.json": true,
  "invalid/id.pattern--leading-hyphen.json": true,
  "invalid/id.pattern--newline.json": true,
  "invalid/id.pattern--nul.json": true,
  "invalid/id.pattern--quote-injection.json": true,
  "invalid/id.pattern--trailing-hyphen.json": true,
  "invalid/id.pattern--uppercase.json": true,
  "invalid/json.duplicateKey--accent.json": false,
  "invalid/json.duplicateKey--escaped-spelling.json": false,
  "invalid/json.malformed--truncated.json": false,
  "invalid/json.tooDeep--nested.json": false,
  "invalid/license.pattern--spaces.json": true,
  "invalid/locale.key--underscore.json": true,
  "invalid/number.range--body-size.json": false,
  "invalid/number.range--huge.json": false,
  "invalid/number.range--line-height-snaps-outside.json": false,
  "invalid/number.range--negative-huge.json": false,
  "invalid/option.gradientStops--one.json": false,
  "invalid/option.role--inline-code-accent.json": true,
  "invalid/scenarios.count--none.json": true,
  "invalid/scenarios.count--three.json": true,
  "invalid/scenarios.duplicate--twice.json": true,
  "invalid/schema.missing--english-name.json": false,
  "invalid/schema.missing--light.json": false,
  "invalid/schema.type--schema-version-string.json": false,
  "invalid/schema.unknownKey--nested-option.json": false,
  "invalid/schema.unknownKey--palette.json": false,
  "invalid/schema.unknownKey--style.json": false,
  "invalid/schema.unknownKey--top-level.json": false,
  "invalid/schema.value--font-design.json": false,
  "invalid/schema.value--palette-role.json": false,
  "invalid/schema.version--two.json": false,
  "invalid/text.bidi--override.json": true,
  "invalid/text.combining--zalgo.json": true,
  "invalid/text.control--line-separator.json": true,
  "invalid/text.control--tab.json": true,
  "invalid/text.empty--summary.json": true,
  "invalid/text.invisible--bom.json": true,
  "invalid/text.length--name.json": true,
  "invalid/text.url--author.json": true,
  "invalid/text.url--summary.json": true,
  "invalid/version.pattern--two-parts.json": true,
  "publish/palette.incomplete--no-diagram.json": true,
  "publish/palette.incomplete--no-syntax.json": true,
};

// Rules whose named field is, by design, a value the preview draws: a validated #RRGGBB colour
// (contrast.*) or a closed palette-role name (option.role), or a group that is absent
// (palette.incomplete). Their "offending value" is not foreign text, so the substring check below
// doesn't apply to them; it covers every rule whose field never reaches the CSS.
function drawnByDesign(rule) {
  return rule.startsWith("contrast.") || rule === "option.role" || rule === "palette.incomplete";
}

/** The raw value at a validator issue path (`a.b`, `a.b[2]`, keys as text.js's quote() shows
 * them), or undefined. */
function valueAtPath(raw, issuePath) {
  let node = raw;
  for (const segment of issuePath.split(".")) {
    const m = segment.match(/^(.*?)((?:\[\d+\])*)$/);
    const key = m[1];
    if (key !== "") {
      if (node === null || typeof node !== "object") return undefined;
      const match = Object.keys(node).find((k) => TextModule.quote(k) === key);
      if (match === undefined) return undefined;
      node = node[match];
    }
    for (const idx of m[2].match(/\d+/g) ?? []) {
      if (!Array.isArray(node)) return undefined;
      node = node[Number(idx)];
    }
  }
  return node;
}
function stringLeaves(value) {
  if (typeof value === "string") return [value];
  if (Array.isArray(value)) return value.flatMap(stringLeaves);
  if (value && typeof value === "object") return Object.values(value).flatMap(stringLeaves);
  return [];
}

function dawnFallback() {
  const dawn = Validator.validate(BuiltIns.BUILT_IN_THEME_JSON.dawn, { requireComplete: true });
  return { light: dawn.theme.light, dark: dawn.theme.dark };
}

function checkPreviewFixtures() {
  console.log("\nPreview: which fixtures the preview draws (expected from the literal table)");
  const fallback = dawnFallback();
  const seen = new Set();
  for (const { category, name, text } of loadFixtures(vendorDir)) {
    if (category !== "invalid" && category !== "publish") continue;
    const key = `${category}/${name}`;
    seen.add(key);
    const expected = EXPECTED_PREVIEWABLE[key];
    const report = Preview.previewReport(text, { fallback });
    const line = `${key}: previewable expected ${expected} actual ${report.previewable} (rule ${report.rule})`;
    if (expected === undefined) {
      bad(line, "no entry in EXPECTED_PREVIEWABLE");
      continue;
    }
    if (report.previewable === expected) ok(line);
    else bad(line);
    if (!report.previewable) continue;

    // Drawn: none of the fixture's offending values may reach the CSS.
    let css;
    try {
      css = Preview.previewSheetText(report);
    } catch (e) {
      bad(`${key}: previewable but the preview path refused it`, String(e));
      continue;
    }
    const validated = Validator.validate(text, { requireComplete: category === "publish" });
    const raw = JSON.parse(text);
    for (const issue of validated.issues) {
      if (drawnByDesign(issue.rule)) {
        ok(`${key}: ${issue.rule} at ${issue.path} names a value drawn by design (substring check n/a)`);
        continue;
      }
      const value = valueAtPath(raw, issue.path);
      if (value === undefined) {
        bad(`${key}: offending value at ${issue.path}`, "the issue path resolves to nothing in the fixture");
        continue;
      }
      const leaves = stringLeaves(value).filter((v) => v !== "");
      if (leaves.length === 0) {
        ok(`${key}: ${issue.rule} at ${issue.path} holds no text (${JSON.stringify(value)}), nothing to leak`);
        continue;
      }
      const leaked = leaves.filter((v) => css.includes(v));
      if (leaked.length === 0) ok(`${key}: CSS carries none of ${JSON.stringify(leaves)} (${issue.rule} at ${issue.path})`);
      else bad(`${key}: CSS carries the offending value`, JSON.stringify(leaked));
    }
  }
  for (const key of Object.keys(EXPECTED_PREVIEWABLE)) {
    if (!seen.has(key)) bad(`EXPECTED_PREVIEWABLE names ${key}`, "no such fixture");
  }
}

function checkPreviewValidFixtures() {
  console.log("\nPreview: every valid/ fixture previews with its expected CSS, only the scope id differing");
  const fallback = dawnFallback();
  const expectedCSSDir = path.join(vendorDir, "expected-css");
  for (const { category, name, text } of loadFixtures(vendorDir)) {
    if (category !== "valid") continue;
    const report = Preview.previewReport(text, { fallback });
    if (!report.previewable) {
      bad(`valid/${name}: previewable`, `rule ${report.rule}`);
      continue;
    }
    const id = JSON.parse(text).id;
    const want = JSON.parse(readFileSync(path.join(expectedCSSDir, `valid__${name}`), "utf8"));
    const swap = (css) => css.split(`[data-theme="${id}"]`).join(`[data-theme="${Preview.PREVIEW_ID}"]`);
    let got;
    try {
      got = Preview.previewThemeCSS(report);
    } catch (e) {
      bad(`valid/${name}: preview css`, `generator refused: ${e}`);
      continue;
    }
    if (got.variables === swap(want.variables) && got.rules === swap(want.rules)) ok(`valid/${name}: preview css equals expected-css with the scope id swapped`);
    else bad(`valid/${name}: preview css`, "differs from expected-css beyond the scope id");
    try {
      Preview.previewSheetText(report);
      ok(`valid/${name}: rescoped preview sheet passes the scope guard`);
    } catch (e) {
      bad(`valid/${name}: rescoped preview sheet passes the scope guard`, String(e));
    }
  }
}

function checkPreviewScope() {
  // Replaces the retired preview-theme.js check: the preview boxes' data-theme is the constant
  // PREVIEW_ID, so every drawn sheet must be scoped to exactly that id, whatever id the draft has.
  console.log("\nPreview: CSS is scoped to PREVIEW_ID");
  const fallback = dawnFallback();
  if (Grammar.isThemeID(Preview.PREVIEW_ID)) ok(`PREVIEW_ID ${JSON.stringify(Preview.PREVIEW_ID)} matches the id grammar`);
  else bad("PREVIEW_ID matches the id grammar", JSON.stringify(Preview.PREVIEW_ID));
  for (const id of BUILT_IN_ORDER) {
    const draft = JSON.parse(BuiltIns.BUILT_IN_THEME_JSON[id]);
    draft.id = "Not A Valid Id\"]";
    const report = Preview.previewReport(JSON.stringify(draft), { fallback });
    if (!report.previewable) {
      bad(`${id} with a broken id: previewable`, `rule ${report.rule}`);
      continue;
    }
    const css = Preview.previewSheetText(report);
    const scopes = new Set([...css.matchAll(/\[data-theme="([^"]*)"\]/g)].map((m) => m[1]));
    if (scopes.size === 1 && scopes.has(Preview.PREVIEW_ID)) ok(`${id} with a broken id: every [data-theme] in the sheet is ${JSON.stringify(Preview.PREVIEW_ID)}`);
    else bad(`${id} with a broken id: scope`, JSON.stringify([...scopes]));
  }
}

function checkPreviewAdvisories() {
  // F2: contrast is reported even while identity fields are empty (the page's starting state).
  console.log("\nPreview: contrast advisories while identity is empty");
  const fallback = dawnFallback();
  const draft = JSON.parse(BuiltIns.BUILT_IN_THEME_JSON.dawn);
  draft.name = { en: "" };
  draft.summary = { en: "" };
  draft.author = { name: "" };
  draft.light.background = "#FFF4E0";
  const text = JSON.stringify(draft);
  const validated = Validator.validate(text);
  const report = Preview.previewReport(text, { fallback });
  const panel = Preview.panelIssues(validated, report).map((i) => `${i.path}: ${i.message}`);
  const hidden = validated.issues.some((i) => i.rule.startsWith("contrast."));
  if (!hidden) ok("validate() alone lists no contrast issue while identity is empty (F2)");
  else bad("validate() alone lists no contrast issue while identity is empty", JSON.stringify(validated.issues));
  for (const want of ["4.40:1", "2.81:1"]) {
    if (panel.some((m) => m.includes(want))) ok(`the panel lists the ${want} contrast message`);
    else bad(`the panel lists the ${want} contrast message`, JSON.stringify(panel));
  }
  const keys = Preview.panelIssues(validated, report).map((i) => `${i.path}|${i.rule}`);
  if (new Set(keys).size === keys.length) ok("the panel lists each (path, rule) once");
  else bad("the panel lists each (path, rule) once", JSON.stringify(keys));
  // Once identity is filled, validate() itself reports contrast: the advisories add nothing.
  draft.name = { en: "N" };
  draft.summary = { en: "S" };
  draft.author = { name: "A" };
  const t2 = JSON.stringify(draft);
  const v2 = Validator.validate(t2);
  const p2 = Preview.panelIssues(v2, Preview.previewReport(t2, { fallback }));
  if (p2.length === v2.issues.length && v2.issues.length > 0) ok(`identity filled: the panel shows validate()'s ${v2.issues.length} issue(s), no duplicate advisory`);
  else bad("identity filled: no duplicate advisory", `${p2.length} vs ${v2.issues.length}`);
}

function checkGeneratorRefusesClosedValues() {
  // Defence in depth (SR W1-2): decodeThemeDocument enforces these closed values; a document that
  // bypasses decode must still be refused by the generator, never written raw or omitted.
  console.log("\nGenerator: closed values outside their list are refused");
  const dawn = Validator.validate(BuiltIns.BUILT_IN_THEME_JSON.dawn, { requireComplete: true }).theme;
  const cases = [
    ["fontDesign \"constructor\"", { ...dawn, document: { ...dawn.document, fontDesign: "constructor" } }, "unknownFontDesign"],
    ["fontDesign \"toString\"", { ...dawn, document: { ...dawn.document, fontDesign: "toString" } }, "unknownFontDesign"],
    ["listMarker role \"constructor\"", { ...dawn, document: { ...dawn.document, style: { listMarker: "constructor" } } }, "unknownRole"],
    ["hr gradient role \"nope\"", { ...dawn, document: { ...dawn.document, style: { hr: { style: { type: "gradient", colors: ["accent", "nope"] } } } } }, "unknownRole"],
    ["h1.align \"x;}\"", { ...dawn, document: { ...dawn.document, style: { h1: { align: "x;}" } } } }, "invalidAlign"],
  ];
  for (const [label, theme, kind] of cases) {
    try {
      const out = Generator.stylesheetFor(theme);
      bad(`${label} is refused (${kind})`, `generated ${JSON.stringify((out.variables + out.rules).slice(0, 120))}…`);
    } catch (e) {
      if (e instanceof Generator.GeneratorRefusal && e.kind === kind) ok(`${label} is refused (${kind})`);
      else bad(`${label} is refused (${kind})`, `wrong error: ${e}`);
    }
  }
}

function checkScopeGuard() {
  console.log("\nScope guard");
  for (const sel of [".sim-previewX h1", ".sim-preview ~ *", ".sim-preview + *", ".sim-preview[data-theme=\"preview\"] ~ button", ".sim-preview.foo", ""]) {
    if (!Preview.selectorStaysInside(sel)) ok(`refuses ${JSON.stringify(sel)}`);
    else bad(`refuses ${JSON.stringify(sel)}`);
  }
  for (const sheet of [".sim-previewX { color: red; }\n", ".sim-preview ~ * { color: red; }\n", ".sim-preview + * { color: red; }\n"]) {
    try {
      Preview.assertScopedToPreview(sheet);
      bad(`assertScopedToPreview refuses ${JSON.stringify(sheet.trim())}`);
    } catch (e) {
      if (e instanceof Generator.GeneratorRefusal && e.kind === "escapedScope") ok(`assertScopedToPreview refuses ${JSON.stringify(sheet.trim())}`);
      else bad(`assertScopedToPreview refuses ${JSON.stringify(sheet.trim())}`, String(e));
    }
  }
  // Every selector the built-ins, the valid fixtures and the option sweep produce is accepted.
  const fallback = dawnFallback();
  const texts = BUILT_IN_ORDER.map((id) => [`built-in ${id}`, BuiltIns.BUILT_IN_THEME_JSON[id]]);
  for (const { category, name, text } of loadFixtures(vendorDir)) if (category === "valid") texts.push([`valid/${name}`, text]);
  const sweepDir = path.join(vendorDir, "sweep");
  if (existsSync(sweepDir)) for (const name of readdirSync(sweepDir)) if (name.endsWith(".json")) texts.push([`sweep/${name}`, readFileSync(path.join(sweepDir, name), "utf8")]);
  let selectors = 0;
  let refused = [];
  for (const [label, text] of texts) {
    const report = Preview.previewReport(text, { fallback });
    if (!report.previewable) {
      refused.push(`${label} (not previewable: ${report.rule})`);
      continue;
    }
    const { variables, rules } = Preview.previewThemeCSS(report);
    const css = rescopeCSS(variables) + rescopeCSS(rules);
    for (const line of css.split("\n")) {
      const brace = line.indexOf("{");
      if (brace === -1) continue;
      for (const sel of line.slice(0, brace).split(",")) {
        selectors += 1;
        if (!Preview.selectorStaysInside(sel)) refused.push(`${label}: ${sel.trim()}`);
      }
    }
  }
  if (refused.length === 0) ok(`accepts all ${selectors} selectors from ${texts.length} built-in, valid and sweep themes`);
  else bad("accepts every built-in, valid and sweep selector", JSON.stringify(refused.slice(0, 10)));
}

function checkSubmitDecision() {
  console.log("\nSubmit decision");
  const fallback = dawnFallback();
  const text = BuiltIns.BUILT_IN_THEME_JSON.classic;
  const validated = Validator.validate(text);
  if (validated.issues.length !== 0) {
    bad("submit decision: setup", JSON.stringify(validated.issues));
    return;
  }
  const report = Preview.previewReport(text, { fallback });
  const refusing = () => {
    throw new Generator.GeneratorRefusal("planted");
  };
  const planted = Preview.previewOutcome(validated, report, refusing);
  if (planted.generatorRefused && planted.css === null && Preview.submitDecision(validated, planted) === false) ok("a refusing generator on a validate-clean theme: generatorRefused, submitDecision false");
  else bad("a refusing generator on a validate-clean theme", JSON.stringify({ generatorRefused: planted.generatorRefused, submit: Preview.submitDecision(validated, planted) }));
  const real = Preview.previewOutcome(validated, report);
  if (!real.generatorRefused && real.css && Preview.submitDecision(validated, real) === true) ok("the real generator on the same theme: submitDecision true");
  else bad("the real generator on the same theme: submitDecision true", JSON.stringify({ generatorRefused: real.generatorRefused }));
  // A guard refusal counts too: a generator whose CSS escapes the wrapper.
  const escaping = () => ({ variables: ":root[data-theme=\"preview\"] { --bg: #000000; }", rules: "[data-theme=\"preview\"] ~ * { color: red; }\n" });
  const escaped = Preview.previewOutcome(validated, report, escaping);
  if (escaped.generatorRefused && Preview.submitDecision(validated, escaped) === false) ok("CSS that escapes .sim-preview on a validate-clean theme: generatorRefused, submitDecision false");
  else bad("CSS that escapes .sim-preview counts as a refusal", JSON.stringify(escaped));
  // An issue in validate() alone blocks Submit, whatever the preview does.
  const withIssue = { issues: [{ rule: "text.empty", path: "name.en", message: "is empty" }], theme: null };
  if (Preview.submitDecision(withIssue, real) === false) ok("a validate() issue blocks Submit even when the preview draws");
  else bad("a validate() issue blocks Submit even when the preview draws");
}

checkRescope();
checkBuiltIns();
checkVendorParity();
checkLowercaseHexControl();
checkLineHeightFormattingChangeIsRed();
checkDroppedFragmentIsRefused();
checkPreviewFixtures();
checkPreviewValidFixtures();
checkPreviewScope();
checkPreviewAdvisories();
checkGeneratorRefusesClosedValues();
checkScopeGuard();
checkSubmitDecision();

console.log(failures === 0 ? "\nAll checks passed." : `\n${failures} check(s) failed.`);
process.exit(failures === 0 ? 0 : 1);
