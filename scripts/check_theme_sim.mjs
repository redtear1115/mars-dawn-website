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

checkRescope();
checkBuiltIns();
checkVendorParity();
checkLowercaseHexControl();
checkLineHeightFormattingChangeIsRed();
checkDroppedFragmentIsRefused();

console.log(failures === 0 ? "\nAll checks passed." : `\n${failures} check(s) failed.`);
process.exit(failures === 0 ? 0 : 1);
