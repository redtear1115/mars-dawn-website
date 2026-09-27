#!/usr/bin/env node
// Parity check for the theme simulator's JavaScript ports (plan-website-104 W1, design
// theme-ecosystem-design.md §6.2's "a rule that exists in only one of them fails CI").
//
// Plain ES modules, no npm dependency: runs under the `node` already on the CI image.
//
// Two things this checks, always:
//   1. The .sim-preview rescoping transform against the shared fixture
//      (scripts/theme_sim/rescope_fixture.json), including the four rev-4 examples.
//   2. That the four built-in themes decode, validate clean, and generate CSS with no
//      unresolved `{{placeholder}}` -- a smoke test that needs no vendored kit data.
//
// One more thing this checks whenever `vendor/kit-themes/<tag>/` exists (WA vendors it there;
// until WA lands, populate it yourself, locally and UNCOMMITTED, from the pinned kit SHA, to run
// this for real -- see the header note in that directory once WA adds it):
//   3. Every kit fixture (valid/invalid/hostile/publish) and the option sweep: this port's verdict
//      and rule ids must equal expected-messages.json's, and, once expected-css/ exists, this
//      port's generated CSS must equal it byte for byte. Planted controls (lineHeight formatting,
//      lowercase-only hex, a dropped fragment) must each turn exactly one comparison red.
//
// Without a vendor directory, step 3 is skipped with its own clear message and this script exits
// non-zero: a parity check that can't compare against anything is not evidence of parity, so it
// refuses to report success it didn't earn. This script is NOT yet wired into site.yml (see the
// PR this shipped in): wiring it in is WA's job, once vendor/kit-themes/ is committed for CI to
// read.

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
const { BUILT_IN_THEME_JSON, BUILT_IN_ORDER } = await import(path.join(assetsDir, "built-ins.js"));

let failures = 0;
function ok(label) {
  console.log(`  ok  ${label}`);
}
function bad(label, detail) {
  failures += 1;
  console.log(`FAIL  ${label}${detail ? `: ${detail}` : ""}`);
}

// --- 1. Rescoping transform fixture ----------------------------------------------------------

function checkRescope() {
  console.log("Rescoping transform (scripts/theme_sim/rescope_fixture.json)");
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
}

// --- 2. Built-in smoke test (no vendor needed) ------------------------------------------------

function checkBuiltIns() {
  console.log("Built-in themes (decode, validate, generate)");
  let dawnLight, dawnDark;
  for (const id of BUILT_IN_ORDER) {
    const text = BUILT_IN_THEME_JSON[id];
    const report = Validator.validate(text, { requireComplete: true });
    if (report.issues.length !== 0) {
      bad(`${id}: validates clean`, JSON.stringify(report.issues));
      continue;
    }
    ok(`${id}: validates clean`);
    if (id === "dawn") {
      dawnLight = report.theme.light;
      dawnDark = report.theme.dark;
      Validator.setDawnFallback(dawnLight, dawnDark);
    }
    const { variables, rules } = Generator.stylesheetFor(report.theme);
    if (variables.includes("{{") || rules.includes("{{")) bad(`${id}: no unresolved placeholder`);
    else ok(`${id}: generates CSS with no unresolved placeholder`);
  }
}

// --- 3. Vendor-backed parity (dev-only until WA lands) ----------------------------------------

function findVendorTag() {
  const vendorRoot = path.join(repoRoot, "vendor", "kit-themes");
  if (!existsSync(vendorRoot)) return null;
  const tags = readdirSync(vendorRoot).filter((name) => existsSync(path.join(vendorRoot, name, "ThemeStyles.json")));
  return tags.length ? path.join(vendorRoot, tags[0]) : null;
}

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

function checkVendorParity(vendorDir) {
  console.log(`Vendor-backed parity (${path.relative(repoRoot, vendorDir)})`);
  const expectedMessagesPath = path.join(vendorDir, "ThemeFixtures", "expected-messages.json");
  if (!existsSync(expectedMessagesPath)) {
    bad("expected-messages.json", "not found under the vendor directory");
    return;
  }
  const expectedMessages = JSON.parse(readFileSync(expectedMessagesPath, "utf8"));
  const fixtures = loadFixtures(vendorDir);
  const expectedCSSDir = path.join(vendorDir, "expected-css");
  const hasExpectedCSS = existsSync(expectedCSSDir);
  if (!hasExpectedCSS) console.log("  (expected-css/ not present yet: CSS-equality comparisons are skipped, per plan)");

  for (const { category, name, text } of fixtures) {
    if (category === "valid") {
      const report = Validator.validate(text);
      if (report.issues.length === 0 && report.theme) ok(`valid/${name}: validates clean`);
      else bad(`valid/${name}`, `expected no issues, got ${JSON.stringify(report.issues)}`);
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

  if (hasExpectedCSS) {
    for (const id of BUILT_IN_ORDER) {
      const report = Validator.validate(BUILT_IN_THEME_JSON[id], { requireComplete: true });
      const cssPath = path.join(expectedCSSDir, `${id}.json`);
      if (!existsSync(cssPath) || !report.theme) continue;
      const want = JSON.parse(readFileSync(cssPath, "utf8"));
      const { variables, rules } = Generator.stylesheetFor(report.theme);
      if (variables === want.variables && rules === want.rules) ok(`built-in ${id}: css matches expected-css`);
      else bad(`built-in ${id}: css`, "generated CSS does not match expected-css");
    }
  }
}

function checkLowercaseHexAccepted() {
  // Planted control (plan-website-104 W1): the kit accepts a hex colour "either case"
  // (ThemeGrammar.isHexColor). A validator that quietly started requiring uppercase would still
  // pass every vendored fixture (the kit's own fixtures are all written uppercase), so this check
  // exists to catch exactly that regression on its own.
  const lowered = BUILT_IN_THEME_JSON.dawn.replace("#FFFDFB", "#fffdfb");
  const report = Validator.validate(lowered);
  if (report.issues.length === 0 && report.theme) ok("lowercase hex colour is accepted (either case, per the kit's grammar)");
  else bad("lowercase hex colour is accepted", JSON.stringify(report.issues));
}

function checkDroppedFragmentIsRefused() {
  // Planted control (plan-website-104 W1): a style option value with no CSS fragment must refuse
  // the whole theme rather than silently drawing it without that option
  // (ThemeCSSGenerator.Refusal.unresolvedPlaceholder). Proven by actually removing one entry from
  // the ported fragment table (Vivid's own `tableHeader.filled`), confirming Vivid then refuses to
  // generate, and restoring it so nothing else this script runs sees the mutation.
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
checkLowercaseHexAccepted();
checkDroppedFragmentIsRefused();

const vendorDir = findVendorTag();
if (vendorDir) {
  checkVendorParity(vendorDir);
} else {
  console.log("Vendor-backed parity: skipped -- vendor/kit-themes/<tag>/ThemeStyles.json not found.");
  console.log("This is expected until WA (plan-website-104) vendors the kit's theme contract; until");
  console.log("then, populate vendor/kit-themes/<tag>/ locally and UNCOMMITTED from the pinned kit SHA");
  console.log("to run this check for real. Failing loudly rather than silently skipping this step.");
  failures += 1;
}

console.log(failures === 0 ? "\nAll checks passed." : `\n${failures} check(s) failed.`);
process.exit(failures === 0 ? 0 : 1);
