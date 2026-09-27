// The theme simulator's page controller (plan-website-104 W1, design theme-ecosystem-design.md
// §3.4). Plain ES module, no build step, no dependency beyond this page's own theme-sim/*.js.
//
// Controls only produce values the schema can describe (design §3.4: "Nothing else can be typed
// in"): colour pickers (<input type=color>, which only ever yields #rrggbb), closed <select>s,
// and range/number inputs clamped to each option's own bounds. Every control writes into one
// `state` object shaped exactly like a theme.json body; validating and generating both read it
// straight, with no separate "form data" translation step to drift from the schema.

import * as Validator from "./validator.js";
import * as Generator from "./generator.js";
import { PALETTE_ROLES } from "./palette.js";
import { rescopeCSS } from "./rescope.js";
import { BUILT_IN_THEME_JSON, BUILT_IN_ORDER } from "./built-ins.js";
import { sampleDocumentHTML } from "./sample-document.js";
import { THEME_NUMBERS } from "./numbers.js";

const SCENARIOS = [
  { id: "agent-review", label: "Agent review" },
  { id: "technical-docs", label: "Technical docs" },
  { id: "formal-output", label: "Formal output" },
  { id: "notes-sharing", label: "Notes sharing" },
];
const ALL_ROLES = PALETTE_ROLES;

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
  constructor(root) {
    this.root = root;
    this.state = stateFromBuiltIn("dawn");
    this.lightSheet = new CSSStyleSheet();
    this.baseSheet = null; // adopted once, from sim-preview-base.css
    this.render();
  }

  async adoptBaseSheetOnce() {
    if (this.baseSheet) return;
    const res = await fetch(new URL("./sim-preview-base.css", import.meta.url));
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
    this.lastReport = report;
    this.renderMessages(report);

    // Replace the previous generated sheet, never leaving two adopted at once.
    document.adoptedStyleSheets = document.adoptedStyleSheets.filter((s) => s !== this.lightSheet);
    if (report.theme) {
      try {
        const { variables, rules } = Generator.stylesheetFor(report.theme);
        const rescoped = rescopeCSS(variables, ".sim-preview") + rescopeCSS(rules, ".sim-preview");
        // Security property (W1 Done-when): every selector in the adopted sheet must live under
        // .sim-preview, so a generator bug can't restyle Submit, the messages panel or anything
        // else on the page.
        for (const line of rescoped.split("\n")) {
          const brace = line.indexOf("{");
          if (brace <= 0) continue;
          const selectors = line.slice(0, brace).split(",");
          if (selectors.some((s) => !s.trim().startsWith(".sim-preview"))) {
            throw new Error("generated CSS escaped .sim-preview -- refusing to adopt it");
          }
        }
        this.lightSheet.replaceSync(rescoped);
        document.adoptedStyleSheets = [...document.adoptedStyleSheets, this.lightSheet];
      } catch (e) {
        console.error(e);
      }
    }
  }

  renderMessages(report) {
    const box = this.root.querySelector("#sim-messages");
    box.textContent = "";
    if (report.issues.length === 0) {
      const p = document.createElement("p");
      p.className = "sim-ok";
      p.textContent = "Every check passes. Ready to submit.";
      box.appendChild(p);
      return;
    }
    const list = document.createElement("ul");
    for (const issue of report.issues) {
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
      <div class="sim-preview-boxes">
        <section aria-label="Light preview">
          <h3 class="sim-preview-label">Light</h3>
          <div class="sim-preview" data-theme="sim" data-appearance="light">${sampleDocumentHTML()}</div>
        </section>
        <section aria-label="Dark preview">
          <h3 class="sim-preview-label">Dark</h3>
          <div class="sim-preview" data-theme="sim" data-appearance="dark">${sampleDocumentHTML()}</div>
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
    if (!this.lastReport || this.lastReport.issues.length > 0) {
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

export function mount(root) {
  return new ThemeSimApp(root);
}
