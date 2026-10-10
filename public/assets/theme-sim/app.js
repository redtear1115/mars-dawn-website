// The theme simulator's page controller (plan-website-104 W1, design theme-ecosystem-design.md
// §3.4). Plain ES module, no build step, no dependency beyond this page's own theme-sim/*.js.
//
// Controls only produce values the schema can describe (design §3.4: "Nothing else can be typed
// in"): colour pickers (<input type=color>, which only ever yields #rrggbb), closed <select>s,
// and range/number inputs clamped to each option's own bounds. Every control writes into one
// `state` object shaped exactly like a theme.json body; validating and generating both read it
// straight, with no separate "form data" translation step to drift from the schema.

import * as Validator from "./validator.js";
import { PALETTE_ROLES } from "./palette.js";
import { BUILT_IN_THEME_JSON, BUILT_IN_ORDER, loadBuiltIns } from "./built-ins.js";
import { loadThemeStyles } from "./styles-data.js";
import { sampleDocumentHTML } from "./sample-document.js";
import { THEME_NUMBERS } from "./numbers.js";
import { PREVIEW_ID, previewReport, previewOutcome, submitDecision, panelIssues } from "./preview-report.js";

const SCENARIOS = [
  { id: "agent-review", label: "Agent review" },
  { id: "technical-docs", label: "Technical docs" },
  { id: "formal-output", label: "Formal output" },
  { id: "notes-sharing", label: "Notes sharing" },
];
const ALL_ROLES = PALETTE_ROLES;
const STALE_PREVIEW_TEXT = "Preview shows the last version that could be drawn";
const GENERATOR_REFUSED_TEXT = "The preview can't draw this theme, so it can't be submitted.";

/** Loads a built-in as the starting state (only the fields a designer would edit; `id`/`version`
 * are reset to a fresh draft, since a submission can't reuse a built-in's id). */
function stateFromBuiltIn(id) {
  const doc = JSON.parse(BUILT_IN_THEME_JSON[id]);
  doc.id = "my-theme";
  doc.version = "1.0.0";
  doc.name = { en: "" };
  doc.summary = { en: "" };
  doc.author = { name: "" };
  doc.license = "Apache-2.0";
  return doc;
}

function get(obj, path) {
  return path.split(".").reduce((o, k) => (o == null ? undefined : o[k]), obj);
}
function set(obj, path, value) {
  const parts = path.split(".");
  let node = obj;
  for (let i = 0; i < parts.length - 1; i++) {
    if (node[parts[i]] == null || typeof node[parts[i]] !== "object") node[parts[i]] = {};
    node = node[parts[i]];
  }
  node[parts[parts.length - 1]] = value;
}
function unset(obj, path) {
  const parts = path.split(".");
  let node = obj;
  for (let i = 0; i < parts.length - 1; i++) {
    if (node[parts[i]] == null) return;
    node = node[parts[i]];
  }
  delete node[parts[parts.length - 1]];
}

class ThemeSimApp {
  constructor(root, dawnFallback) {
    this.root = root;
    // Dawn's resolved palettes, the same ones mount() gave validator.js's setDawnFallback: the
    // preview fills a palette's missing syntax/diagram colours from them, as validate() does.
    this.dawnFallback = dawnFallback;
    // Passed from the page as plain text via #theme-sim-app's own data-locale attribute (never
    // inline JS -- see boot.js), for whichever future control needs to know the page's locale.
    // Not otherwise read yet: the page copy above the control panel is what varies per locale
    // today; the panel's own labels are English in every locale (a known limitation, tracked
    // separately from this fix).
    this.locale = root.dataset.locale || "en";
    this.state = stateFromBuiltIn("dawn");
    this.lightSheet = new CSSStyleSheet();
    this.baseSheet = null; // adopted once, from the kit's own preview-sim.css
    // The theme text the adopted sheet was drawn from (null until one is drawn). The preview keeps
    // the last sheet that could be drawn; when this differs from the current state, the stale
    // marker says so.
    this.drawnText = null;
    this.lastOutcome = { css: null, generatorRefused: false };
    this.render();
  }

  async adoptBaseSheetOnce() {
    if (this.baseSheet) return;
    // The kit's own preview.css, already rescoped to .sim-preview at sync time
    // (scripts/rescope_css.py) -- see build_pages.py's sync_theme_kit_assets_into_public().
    const res = await fetch(new URL("./kit/preview-sim.css", import.meta.url));
    const text = await res.text();
    const sheet = new CSSStyleSheet();
    sheet.replaceSync(text);
    document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];
    this.baseSheet = sheet;
  }

  async recompute() {
    await this.adoptBaseSheetOnce();
    const text = JSON.stringify(this.state);
    const report = Validator.validate(text, { requireComplete: false });
    // The preview draws any draft whose structure is sound (preview-report.js), scoped to the
    // constant PREVIEW_ID; validate() above stays the only gate for Submit.
    const preview = previewReport(text, { fallback: this.dawnFallback });
    const outcome = previewOutcome(report, preview);
    this.lastReport = report;
    this.lastOutcome = outcome;

    if (outcome.css !== null) {
      // Replace the previous generated sheet, never leaving two adopted at once. A draft that
      // can't be drawn leaves the last good sheet in place instead of blanking the preview.
      this.lightSheet.replaceSync(outcome.css);
      if (!document.adoptedStyleSheets.includes(this.lightSheet)) {
        document.adoptedStyleSheets = [...document.adoptedStyleSheets, this.lightSheet];
      }
      this.drawnText = text;
    }
    this.renderMessages(report, preview, outcome);
    const stale = this.root.querySelector("#sim-stale");
    if (stale) stale.hidden = this.drawnText === null || this.drawnText === text;
  }

  renderMessages(report, preview, outcome) {
    const box = this.root.querySelector("#sim-messages");
    box.textContent = "";
    if (report.issues.length === 0 && !outcome.generatorRefused) {
      const p = document.createElement("p");
      p.className = "sim-ok";
      p.textContent = "Every check passes. Ready to submit.";
      box.appendChild(p);
      return;
    }
    if (outcome.generatorRefused) {
      const p = document.createElement("p");
      p.className = "sim-refused";
      p.textContent = GENERATOR_REFUSED_TEXT;
      box.appendChild(p);
    }
    const issues = panelIssues(report, preview);
    if (issues.length === 0) return;
    const list = document.createElement("ul");
    for (const issue of issues) {
      const li = document.createElement("li");
      li.textContent = issue.path ? `${issue.path}: ${issue.message}` : issue.message;
      list.appendChild(li);
    }
    box.appendChild(list);
  }

  colorControl(labelText, path) {
    const label = document.createElement("label");
    label.className = "sim-color-field";
    const span = document.createElement("span");
    span.textContent = labelText;
    const input = document.createElement("input");
    input.type = "color";
    input.value = get(this.state, path) || "#000000";
    input.addEventListener("input", () => {
      set(this.state, path, input.value.toUpperCase());
      this.recompute();
    });
    label.append(span, input);
    return label;
  }

  render() {
    this.root.textContent = "";
    const layout = document.createElement("div");
    layout.className = "sim-layout";

    const controls = document.createElement("div");
    controls.className = "sim-controls";
    controls.append(
      this.buildStartFromSection(),
      this.buildIdentitySection(),
      this.buildScenarioSection(),
      this.buildPaletteSection("light", "Light palette"),
      this.buildPaletteSection("dark", "Dark palette"),
      this.buildStyleSection(),
      this.buildJSONSection(),
      this.buildSubmitSection()
    );

    const preview = document.createElement("div");
    preview.className = "sim-preview-column";
    preview.innerHTML = `
      <div id="sim-messages" class="sim-messages" aria-live="polite"></div>
      <p id="sim-stale" class="sim-stale" role="status" hidden>${STALE_PREVIEW_TEXT}</p>
      <div class="sim-preview-boxes">
        <section aria-label="Light preview">
          <h3 class="sim-preview-label">Light</h3>
          <div class="sim-preview" data-theme="${PREVIEW_ID}" data-appearance="light">${sampleDocumentHTML()}</div>
        </section>
        <section aria-label="Dark preview">
          <h3 class="sim-preview-label">Dark</h3>
          <div class="sim-preview" data-theme="${PREVIEW_ID}" data-appearance="dark">${sampleDocumentHTML()}</div>
        </section>
      </div>
    `;

    layout.append(controls, preview);
    this.root.appendChild(layout);
    this.recompute();
  }

  buildStartFromSection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Start from</legend>";
    const select = document.createElement("select");
    for (const id of BUILT_IN_ORDER) {
      const opt = document.createElement("option");
      opt.value = id;
      opt.textContent = id;
      select.appendChild(opt);
    }
    select.addEventListener("change", () => {
      const keepId = this.state.id;
      const keepVersion = this.state.version;
      this.state = stateFromBuiltIn(select.value);
      this.state.id = keepId;
      this.state.version = keepVersion;
      this.render();
    });
    section.appendChild(select);
    return section;
  }

  buildIdentitySection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Identity</legend>";
    section.append(
      this.textField("Theme id", "id"),
      this.textField("Version", "version"),
      this.textField("Name (English)", "name.en"),
      this.textField("Summary (English)", "summary.en"),
      this.textField("Author name (optional)", "author.name", true),
      this.textField("Author GitHub username (optional)", "author.github", true),
      this.textField("Licence", "license", true)
    );
    return section;
  }

  textField(label, path, optional) {
    const wrap = document.createElement("label");
    wrap.className = "sim-field";
    const span = document.createElement("span");
    span.textContent = label;
    const input = document.createElement("input");
    input.type = "text";
    input.value = get(this.state, path) ?? "";
    input.addEventListener("input", () => {
      if (optional && input.value === "") unset(this.state, path);
      else set(this.state, path, input.value);
      this.recompute();
    });
    wrap.append(span, input);
    return wrap;
  }

  buildScenarioSection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Scenarios (pick 1 or 2)</legend>";
    for (const { id, label } of SCENARIOS) {
      const wrap = document.createElement("label");
      wrap.className = "sim-checkbox-field";
      const input = document.createElement("input");
      input.type = "checkbox";
      input.checked = this.state.scenarios.includes(id);
      input.addEventListener("change", () => {
        const set2 = new Set(this.state.scenarios);
        if (input.checked) set2.add(id);
        else set2.delete(id);
        this.state.scenarios = [...set2];
        this.recompute();
      });
      wrap.append(input, document.createTextNode(label));
      section.appendChild(wrap);
    }
    const fontLabel = document.createElement("label");
    fontLabel.className = "sim-field";
    const fontSpan = document.createElement("span");
    fontSpan.textContent = "Font design";
    const fontSelect = document.createElement("select");
    for (const v of ["sans", "serif", "rounded"]) {
      const opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      if (this.state.fontDesign === v) opt.selected = true;
      fontSelect.appendChild(opt);
    }
    fontSelect.addEventListener("change", () => {
      this.state.fontDesign = fontSelect.value;
      this.recompute();
    });
    fontLabel.append(fontSpan, fontSelect);
    section.appendChild(fontLabel);
    return section;
  }

  buildPaletteSection(mode, title) {
    const section = document.createElement("fieldset");
    section.innerHTML = `<legend>${title}</legend>`;
    const base = document.createElement("div");
    base.className = "sim-color-grid";
    for (const role of ["background", "surface", "text", "muted", "border", "heading", "accent", "link", "quote"]) {
      base.appendChild(this.colorControl(role, `${mode}.${role}`));
    }
    section.appendChild(base);

    const details = document.createElement("details");
    details.innerHTML = "<summary>Syntax colours (recommended for publishing)</summary>";
    const syntaxGrid = document.createElement("div");
    syntaxGrid.className = "sim-color-grid";
    for (const role of ["keyword", "string", "comment", "number", "function", "type"]) {
      if (get(this.state, `${mode}.syntax.${role}`) === undefined) set(this.state, `${mode}.syntax.${role}`, get(this.state, `${mode}.text`));
      syntaxGrid.appendChild(this.colorControl(role, `${mode}.syntax.${role}`));
    }
    details.appendChild(syntaxGrid);
    section.appendChild(details);

    const diagramDetails = document.createElement("details");
    diagramDetails.innerHTML = "<summary>Diagram colours (recommended for publishing)</summary>";
    const diagramGrid = document.createElement("div");
    diagramGrid.className = "sim-color-grid";
    for (const role of ["node", "nodeBorder", "text", "line", "secondary", "tertiary", "note"]) {
      if (get(this.state, `${mode}.diagram.${role}`) === undefined) set(this.state, `${mode}.diagram.${role}`, get(this.state, `${mode}.text`));
      diagramGrid.appendChild(this.colorControl(role, `${mode}.diagram.${role}`));
    }
    diagramDetails.appendChild(diagramGrid);
    section.appendChild(diagramDetails);
    return section;
  }

  roleSelect(path, options = ALL_ROLES) {
    const select = document.createElement("select");
    const current = get(this.state, path);
    for (const role of options) {
      const opt = document.createElement("option");
      opt.value = role;
      opt.textContent = role;
      if (current === role) opt.selected = true;
      select.appendChild(opt);
    }
    select.addEventListener("change", () => {
      set(this.state, path, select.value);
      this.recompute();
    });
    return select;
  }

  numberField(labelText, path, numberName) {
    const wrap = document.createElement("label");
    wrap.className = "sim-field";
    const span = document.createElement("span");
    const { range, step } = THEME_NUMBERS[numberName];
    span.textContent = `${labelText} (${range[0]}–${range[1]})`;
    const input = document.createElement("input");
    input.type = "number";
    input.min = String(range[0]);
    input.max = String(range[1]);
    input.step = String(step);
    const current = get(this.state, path);
    if (current !== undefined) input.value = String(current);
    input.addEventListener("input", () => {
      if (input.value === "") unset(this.state, path);
      else set(this.state, path, Number(input.value));
      this.recompute();
    });
    wrap.append(span, input);
    return wrap;
  }

  /** A bare-boolean style option (h2.italic, blockquote.italic, table.verticalRules,
   * table.rounded, link.underline, syntax.boldKeywords, ...) is three states, not two: unset
   * (take the default), explicit true, or explicit false. A theme can need any of the three --
   * Classic's own theme.json sets `table.verticalRules: false` -- so a plain checkbox (which can
   * only write `true` or remove the field) can't express it. */
  boolField(labelText, path) {
    const wrap = document.createElement("label");
    wrap.className = "sim-field";
    const span = document.createElement("span");
    span.textContent = labelText;
    const select = document.createElement("select");
    const current = get(this.state, path);
    for (const [value, text] of [["", "(default)"], ["true", "On"], ["false", "Off"]]) {
      const opt = document.createElement("option");
      opt.value = value;
      opt.textContent = text;
      const selected = (current === undefined && value === "") || (current === true && value === "true") || (current === false && value === "false");
      if (selected) opt.selected = true;
      select.appendChild(opt);
    }
    select.addEventListener("change", () => {
      if (select.value === "") unset(this.state, path);
      else set(this.state, path, select.value === "true");
      this.recompute();
    });
    wrap.append(span, select);
    return wrap;
  }

  buildStyleSection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Style</legend>";
    if (!this.state.style) this.state.style = {};

    section.append(
      this.numberField("Body size (px)", "style.bodySize", "bodySize"),
      this.numberField("Line height", "style.lineHeight", "lineHeight"),
      this.numberField("Heading weight", "style.headingWeight", "headingWeight"),
      this.numberField("Corner radius (px)", "style.radius", "radius"),
      this.numberField("Max width (px)", "style.maxWidth", "maxWidth")
    );

    // h1
    const h1 = document.createElement("fieldset");
    h1.innerHTML = "<legend>Heading 1</legend>";
    h1.append(
      this.numberField("Size (em)", "style.h1.size", "h1.size"),
      this.numberField("Letter spacing (em)", "style.h1.letterSpacing", "h1.letterSpacing")
    );
    const h1AlignLabel = document.createElement("label");
    h1AlignLabel.className = "sim-field";
    h1AlignLabel.append(document.createTextNode("Align "), this.selectField("style.h1.align", ["left", "center"]));
    h1.appendChild(h1AlignLabel);
    const h1DecLabel = document.createElement("label");
    h1DecLabel.className = "sim-field";
    h1DecLabel.append(document.createTextNode("Decoration "), this.decorationField("style.h1.decoration", ["rule", "none", "shortRule", "gradientBar"]));
    h1.appendChild(h1DecLabel);
    section.appendChild(h1);

    // h2
    const h2 = document.createElement("fieldset");
    h2.innerHTML = "<legend>Heading 2</legend>";
    h2.append(this.numberField("Letter spacing (em)", "style.h2.letterSpacing", "h2.letterSpacing"), this.boolField("Italic", "style.h2.italic"));
    const h2DecLabel = document.createElement("label");
    h2DecLabel.className = "sim-field";
    h2DecLabel.append(document.createTextNode("Decoration "), this.decorationField("style.h2.decoration", ["rule", "none", "dot"]));
    h2.appendChild(h2DecLabel);
    section.appendChild(h2);

    // blockquote
    const bq = document.createElement("fieldset");
    bq.innerHTML = "<legend>Blockquote</legend>";
    bq.append(this.boolField("Italic", "style.blockquote.italic"));
    const bqStyleLabel = document.createElement("label");
    bqStyleLabel.className = "sim-field";
    bqStyleLabel.append(document.createTextNode("Style "), this.decorationField("style.blockquote.style", ["bar", "panel"]));
    bq.appendChild(bqStyleLabel);
    section.appendChild(bq);

    // hr
    const hr = document.createElement("fieldset");
    hr.innerHTML = "<legend>Rule (hr)</legend>";
    const hrStyleLabel = document.createElement("label");
    hrStyleLabel.className = "sim-field";
    hrStyleLabel.append(document.createTextNode("Style "), this.decorationField("style.hr.style", ["line", "shortCentered", "gradient"]));
    hr.appendChild(hrStyleLabel);
    section.appendChild(hr);

    // table
    const table = document.createElement("fieldset");
    table.innerHTML = "<legend>Table</legend>";
    const thLabel = document.createElement("label");
    thLabel.className = "sim-field";
    thLabel.append(document.createTextNode("Header "), this.decorationField("style.table.header", ["surface", "accentRule", "filled"]));
    table.append(thLabel, this.boolField("Vertical rules", "style.table.verticalRules"), this.boolField("Rounded corners", "style.table.rounded"));
    section.appendChild(table);

    // misc roles
    const misc = document.createElement("fieldset");
    misc.innerHTML = "<legend>Other</legend>";
    const lm = document.createElement("label");
    lm.className = "sim-field";
    lm.append(document.createTextNode("List marker colour "), this.optionalRoleSelect("style.listMarker"));
    const ic = document.createElement("label");
    ic.className = "sim-field";
    ic.append(document.createTextNode("Inline code colour "), this.optionalRoleSelect("style.inlineCode", ["text", "keyword", "string", "comment", "number", "function", "type"]));
    misc.append(lm, ic, this.boolField("Underline links", "style.link.underline"), this.boolField("Bold syntax keywords", "style.syntax.boldKeywords"));
    section.appendChild(misc);
    return section;
  }

  selectField(path, values) {
    const select = document.createElement("select");
    const blank = document.createElement("option");
    blank.value = "";
    blank.textContent = "(default)";
    select.appendChild(blank);
    const current = get(this.state, path);
    for (const v of values) {
      const opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      if (current === v) opt.selected = true;
      select.appendChild(opt);
    }
    select.addEventListener("change", () => {
      if (select.value === "") unset(this.state, path);
      else set(this.state, path, select.value);
      this.recompute();
    });
    return select;
  }

  optionalRoleSelect(path, roles = ALL_ROLES) {
    const select = document.createElement("select");
    const blank = document.createElement("option");
    blank.value = "";
    blank.textContent = "(default)";
    select.appendChild(blank);
    const current = get(this.state, path);
    for (const role of roles) {
      const opt = document.createElement("option");
      opt.value = role;
      opt.textContent = role;
      if (current === role) opt.selected = true;
      select.appendChild(opt);
    }
    select.addEventListener("change", () => {
      if (select.value === "") unset(this.state, path);
      else set(this.state, path, select.value);
      this.recompute();
    });
    return select;
  }

  /** A discriminated-union option (h1.decoration, hr.style, table.header, ...): a `type` <select>
   * plus the extra role/number controls each type needs, rebuilt whenever `type` changes. */
  decorationField(path, types) {
    const container = document.createElement("span");
    const typeSelect = document.createElement("select");
    const blank = document.createElement("option");
    blank.value = "";
    blank.textContent = "(default)";
    typeSelect.appendChild(blank);
    for (const t of types) {
      const opt = document.createElement("option");
      opt.value = t;
      opt.textContent = t;
      typeSelect.appendChild(opt);
    }
    const current = get(this.state, path);
    if (current?.type) typeSelect.value = current.type;
    const extra = document.createElement("span");
    extra.className = "sim-decoration-extra";

    const rebuildExtra = () => {
      extra.textContent = "";
      const type = typeSelect.value;
      if (!type) return;
      const roleFields = {
        shortRule: [["color", "accent"]],
        dot: [["color", "accent"]],
        accentRule: [["color", "accent"]],
        shortCentered: [["color", "accent"]],
        line: [["color", "border"]],
        gradientBar: [["from", "accent"], ["to", "heading"]],
        filled: [["background", "heading"], ["text", "background"]],
        gradient: null, // colours[]: a fixed 2-role picker below
      };
      if (type === "bar") {
        extra.appendChild(this.miniNumber(`${path}.width`, "blockquote.style.width", "Width (px)"));
      } else if (type === "line") {
        extra.appendChild(this.miniRole(`${path}.color`, "border"));
        extra.appendChild(this.miniNumber(`${path}.thickness`, "hr.style.thickness", "Thickness (px)"));
      } else if (roleFields[type]) {
        for (const [key, fallback] of roleFields[type]) extra.appendChild(this.miniRole(`${path}.${key}`, fallback));
      } else if (type === "gradient") {
        const p = get(this.state, path) ?? {};
        if (!Array.isArray(p.colors) || p.colors.length < 2) set(this.state, `${path}.colors`, ["accent", "heading"]);
        extra.appendChild(this.miniRole(`${path}.colors.0`, "accent"));
        extra.appendChild(this.miniRole(`${path}.colors.1`, "heading"));
      }
    };

    typeSelect.addEventListener("change", () => {
      if (typeSelect.value === "") unset(this.state, path);
      else set(this.state, path, { type: typeSelect.value });
      rebuildExtra();
      this.recompute();
    });
    rebuildExtra();
    container.append(typeSelect, extra);
    return container;
  }

  miniRole(path, fallback) {
    if (get(this.state, path) === undefined) set(this.state, path, fallback);
    return this.roleSelect(path);
  }
  miniNumber(path, numberName, label) {
    return this.numberField(label, path, numberName);
  }

  buildJSONSection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Export / import JSON</legend>";
    const textarea = document.createElement("textarea");
    textarea.rows = 6;
    textarea.value = JSON.stringify(this.state, null, 2);
    const exportBtn = document.createElement("button");
    exportBtn.type = "button";
    exportBtn.textContent = "Refresh from current theme";
    exportBtn.addEventListener("click", () => {
      textarea.value = JSON.stringify(this.state, null, 2);
    });
    const importBtn = document.createElement("button");
    importBtn.type = "button";
    importBtn.textContent = "Load this JSON";
    importBtn.addEventListener("click", () => {
      try {
        const parsed = JSON.parse(textarea.value);
        this.state = parsed;
        this.render();
      } catch (e) {
        alert(`Not valid JSON: ${e.message}`);
      }
    });
    section.append(textarea, exportBtn, importBtn);
    return section;
  }

  buildSubmitSection() {
    const section = document.createElement("fieldset");
    section.innerHTML = "<legend>Submit</legend>";
    const p = document.createElement("p");
    p.textContent = "Opens a prefilled issue on GitHub. You'll need a GitHub account to submit.";
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "Submit this theme";
    button.addEventListener("click", () => this.submit());
    section.append(p, button);
    return section;
  }

  submit() {
    if (!this.lastReport || !submitDecision(this.lastReport, this.lastOutcome)) {
      alert("Fix every check above before submitting.");
      return;
    }
    const json = JSON.stringify(this.state, null, 2);
    if (json.length > 8000) {
      alert("This theme is too large to submit through a prefilled issue (over 8,000 characters). Simplify it, or open a pull request instead (see the repo's CONTRIBUTING.md).");
      return;
    }
    // Constant base URL + URLSearchParams; `theme` last (design W1). No theme data reaches
    // analytics: this is a plain link, opened with window.open, never sent as a GA link_url.
    const base = "https://github.com/redtear1115/mars-dawn-website/issues/new";
    const params = new URLSearchParams();
    params.set("template", "theme-submission.yml");
    params.set("theme", json);
    window.open(`${base}?${params.toString()}`, "_blank", "noopener");
  }
}

/** Loads the kit's theme contract (ThemeStyles.json, the four built-ins) from this page's own
 * copy under ./kit/ -- see build_pages.py's sync_theme_kit_assets_into_public(), which puts it
 * there from vendor/kit-themes/<tag>/ (scripts/sync_theme_kit.py) -- then builds the page. Both
 * loads must finish before anything reads FRAGMENTS/SHARED_PAIRS/OPTION_PAIRS/BUILT_IN_THEME_JSON,
 * so `mount` is async; the container's own "needs JavaScript" fallback text stays on screen for
 * the brief moment this takes, and ThemeSimApp's own render() clears it once construction starts. */
export async function mount(root) {
  const kitBase = new URL("./kit/", import.meta.url);
  await Promise.all([
    loadThemeStyles(new URL("ThemeStyles.json", kitBase)),
    loadBuiltIns(new URL("themes/", kitBase)),
  ]);
  // Dawn's validated palettes as the fallback for a palette without syntax/diagram colours,
  // exactly as scripts/check_theme_sim.mjs sets it, so validate() here resolves like CI.
  const dawn = Validator.validate(BUILT_IN_THEME_JSON.dawn, { requireComplete: true });
  if (!dawn.theme) throw new Error("mount: the built-in Dawn theme did not validate");
  Validator.setDawnFallback(dawn.theme.light, dawn.theme.dark);
  return new ThemeSimApp(root, { light: dawn.theme.light, dark: dawn.theme.dark });
}
