// The theme simulator's bootstrap (mars-dawn-website#142). An external module script, loaded with
// `<script type="module" src="/assets/theme-sim/boot.js">` -- never inline: the site's CSP is
// `script-src 'self'` plus two sha256-hashed inline scripts (Consent Mode default, the GTM loader)
// ONLY (public/_headers), so an inline `<script type="module">` here is silently blocked in every
// real browser (mars-dawn-website#147, caught by the verifier) and the simulator never mounts.
// This file carries no page-specific text of its own; whatever it needs from the page comes off
// #theme-sim-app's own data-* attributes (data-locale), read as plain text via .dataset, never
// interpolated into JS. scripts/check_no_inline_scripts.py holds every generated page to having no
// inline script beyond the CSP's own hashed pair.

import { mount } from "./app.js";

const root = document.getElementById("theme-sim-app");
if (root) mount(root);
