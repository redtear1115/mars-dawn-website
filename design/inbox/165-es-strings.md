# #165 Español (es) — tranche 1: terms, site chrome, 404

Source: English read programmatically from `scripts/build_pages.py` / `scripts/templates_pages.py` / `public/404.html` on `main` @ `6fe8435`; app terms from `MarsDawn/Resources/Localizable.xcstrings` on app `release/1.1.0`. Legal pages are in the sibling files `165-privacy.es.md` and `165-support.es.md`.

## 1. Terms checked against the app (release/1.1.0)

| en (app) | es (app) | xcstrings key |
|---|---|---|
| Window | Ventana | `Window` |
| Show Sidebar | Mostrar barra lateral | `Show Sidebar` |
| Preview | Vista previa | `Preview` |
| Editor | Editor | `Editor` |
| Source Only | Solo código | `Source Only` |
| Preview Only | Solo vista previa | `Preview Only` |
| Split | Dividido | `Split` |
| Layout | Disposición | `Layout` |
| Theme | Tema | `Theme` |
| Preview Theme | Tema de la vista previa | `Preview Theme` |
| Appearance | Aspecto | `Appearance` |
| Settings | Ajustes | `Settings` |
| Export as PDF… | Exportar como PDF… | `Export as PDF…` |
| Print… | Imprimir… | `Print…` |
| Save As… | Guardar como… | `Save As…` |
| File | Archivo | `File` |
| View | Visualización | `View` |
| Open Folder… | Abrir carpeta… | `Open Folder…` |
| Folder Access | Acceso a carpetas | `Folder Access` |
| Grant Folder Access… | Dar acceso a la carpeta… | `Grant Folder Access…` |
| Load Images | Cargar imágenes | `Load Images` |
| Load remote images automatically | Cargar imágenes remotas automáticamente | `Load remote images automatically` |
| Notes Folder | Carpeta de notas | `Notes Folder` |
| Run This Document | Ejecutar este documento | `Run This Document` |
| Template | Plantilla | `Template` |
| Copy for AI | Copiar para IA | `Copy for AI` |
| About %@ | Acerca de %@ | `About %@` |
| Start 14-day trial | Comenzar prueba de 14 días | `paywall.button.startTrial` |
| Your free trial has ended | Tu prueba gratuita terminó | `paywall.ended.headline` |
| One-time unlock… | Desbloqueo único… | `paywall.button.unlock` |
| Unlock MarsDawn… | Desbloquear MarsDawn… | `paywall.menu.unlock` |
| MarsDawn is unlocked. Thank you. | MarsDawn está desbloqueado. Gracias. | `paywall.settings.unlocked` |
| Restore Purchases | Restaurar compras | `paywall.button.restore` |
| Quick Look | Vista rápida | in `paywall.ended.body` |
| Shortcuts (app) | Atajos | in `Notes you add with Siri or Shortcuts go ` |
| trial (noun) | prueba | in `paywall.unconfirmed.trialNote` |
| subscription | suscripción | in `paywall.unconfirmed.trialNote` |

## 2. Site chrome (`UI`, `STORE_CHIP`, `TRAIT_LINK`, …)

| key | en | es |
|---|---|---|
| `home` | MarsDawn | MarsDawn |
| `privacy` | Privacy Policy | Política de privacidad |
| `support` | Support | Soporte |
| `cli` | Command Line | Línea de comandos |
| `agents` | marsdawn for agents | marsdawn para agentes |
| `using_cli` | Using the CLI | Usar la CLI |
| `markdown-to-pdf` | Markdown to PDF | De Markdown a PDF |
| `skill` | Agent skill | Skill para agentes |
| `view-markdown-on-mac` | View Markdown on a Mac | Ver Markdown en un Mac |
| `vs-macmd-viewer` | MacMD Viewer vs. MarsDawn | MacMD Viewer frente a MarsDawn |
| `updated` | Last updated {UPDATED} | Última actualización: {UPDATED} |
| `tagline` | Read what your agent wrote. | Lee lo que escribió tu agente. |
| `slogan` | A new dawn for Markdown. | Un nuevo amanecer para Markdown. |
| `footer_store` | MarsDawn is on the <a href="{LISTING_URL}">Mac App Store</a>. | MarsDawn está en el <a href="{LISTING_URL}">Mac App Store</a>. |
| `footer_nav` | Site | Sitio |
| `more` | More | Más |
| `yours` | Your writing stays on your Mac | Lo que escribes se queda en tu Mac |
| `pay-once` | Try free, pay once | Pruébalo gratis, paga una vez |
| `pdf` | PDF export | Exportación a PDF |
| `native` | A Mac app | Una app para Mac |
| `limits` | What MarsDawn doesn't do | Lo que MarsDawn no hace |
| `mcp` | MCP server | Servidor MCP |
| `token-efficient-review` | Token-efficient review | Revisión que ahorra tokens |
| `vs-markdown-preview-tools` | Viewing Markdown elsewhere vs. MarsDawn | Ver Markdown en otras herramientas frente a MarsDawn |
| `themes` | Preview themes and PDF export | Temas de la vista previa y exportación a PDF |
| `sharing-exported-pdfs` | Sharing exported PDFs | Compartir los PDF exportados |
| `reviewing-ai-output` | Why AI output still needs a human reader | Por qué lo que produce la IA todavía necesita un lector humano |
| `reading-agent-output` | Reading what your agent hands back | Leer lo que te devuelve tu agente |
| `agent-transparency` | Agent transparency | Transparencia de los agentes |
| `reviewing-agent-plans` | Reviewing an agent plan | Revisar el plan de un agente |
| `agent-design-patterns` | Agent design patterns | Patrones de diseño de agentes |
| `changelog` | Changelog | Historial de cambios |
| `consent_text` | This site uses analytics cookies to see how visitors use it. They stay off unless you accept. | Este sitio usa cookies de analítica para ver cómo lo usan los visitantes. Permanecen desactivadas a menos que las aceptes. |
| `consent_accept` | Accept | Aceptar |
| `consent_decline` | Decline | Rechazar |
| `consent_aria` | Cookie consent | Consentimiento de cookies |
| `cookie_settings` | Cookie settings | Ajustes de cookies |
| `view_markdown_source` | View the Markdown source | Ver el código Markdown |
| `templates` | Templates | Plantillas |
| `templates-spec` | Spec template | Plantilla de especificación |
| `templates-flowchart` | Flowchart template | Plantilla de diagrama de flujo |
| `templates-meeting-notes` | Meeting notes template | Plantilla de notas de reunión |
| `STORE_CHIP` | On the Mac App Store | En el Mac App Store |
| `TRAIT_LINK.yours` title | Your writing stays on your Mac | Lo que escribes se queda en tu Mac |
| `TRAIT_LINK.yours` line | No account, no sync, no cloud. | Sin cuenta, sin sincronización, sin nube. |
| `TRAIT_LINK.pay-once` title | Try free, pay once | Pruébalo gratis, paga una vez |
| `TRAIT_LINK.pay-once` line | Free for 14 days, then USD 4.99 once. No subscription. | Gratis durante 14 días; después, 4,99 USD una sola vez. Sin suscripción. |
| `TRAIT_LINK.pdf` title | PDF export | Exportación a PDF |
| `TRAIT_LINK.pdf` line | Diagrams, highlighted code, careful page breaks. | Diagramas, código resaltado, saltos de página cuidados. |
| `TRAIT_LINK.native` title | A Mac app | Una app para Mac |
| `TRAIT_LINK.native` line | Native windows, tabs, autosave, Quick Look. | Ventanas y pestañas nativas, guardado automático, Vista rápida. |
| `TRAIT_LINK.limits` title | What MarsDawn doesn't do | Lo que MarsDawn no hace |
| `TRAIT_LINK.limits` line | Know before you buy. | Lo que conviene saber antes de comprar. |
| `TRAIT_NAV_HEADING` | What to expect from MarsDawn | Qué esperar de MarsDawn |
| `FIGURE_LIST_LABEL` | In this screenshot | En esta captura de pantalla |
| `SKIP_LABEL` | Skip to content | Saltar al contenido |
| `TOC_LABEL.privacy` | On this page | En esta página |
| `TOC_LABEL.support` | Jump to a question | Ir a una pregunta |
| `LOCALES.label` | English | Español |
| `html_lang` / `OG_LOCALE` | en / en_US | es / es_ES |

## 3. 404 page (`public/404.html`)

| element | en | es |
|---|---|---|
| title | Page not found · MarsDawn | Página no encontrada · MarsDawn |
| h1 | Lost among the stars. | Perdido entre las estrellas. |
| body | This path isn’t on the map. A quiet neighbor pointed the way home. | Este camino no está en el mapa. Un vecino discreto señaló el camino de vuelta a casa. |
| back | Back to MarsDawn | Volver a MarsDawn |
| alt | A small craft drifts in a Martian dawn sky while a friendly alien points toward the planet’s bright limb. | Una pequeña nave flota en el cielo del amanecer marciano mientras un extraterrestre amistoso señala el borde brillante del planeta. |
| aria_language | Language | Idioma |
| aria_site | Site | Sitio |

## 4. Paste-ready for `copy_es.py` (same shape as `copy_ja.py`)

```python
    ui = {'home': 'MarsDawn', 'privacy': 'Política de privacidad', 'support': 'Soporte', 'cli': 'Línea de comandos', 'agents': 'marsdawn para agentes', 'using_cli': 'Usar la CLI', 'markdown-to-pdf': 'De Markdown a PDF', 'skill': 'Skill para agentes', 'view-markdown-on-mac': 'Ver Markdown en un Mac', 'vs-macmd-viewer': 'MacMD Viewer frente a MarsDawn', 'updated': f'Última actualización: {k.UPDATED}', 'tagline': 'Lee lo que escribió tu agente.', 'slogan': 'Un nuevo amanecer para Markdown.', 'footer_store': f'MarsDawn está en el <a href="{k.LISTING_URL}">Mac App Store</a>.', 'footer_nav': 'Sitio', 'more': 'Más', 'yours': 'Lo que escribes se queda en tu Mac', 'pay-once': 'Pruébalo gratis, paga una vez', 'pdf': 'Exportación a PDF', 'native': 'Una app para Mac', 'limits': 'Lo que MarsDawn no hace', 'mcp': 'Servidor MCP', 'token-efficient-review': 'Revisión que ahorra tokens', 'vs-markdown-preview-tools': 'Ver Markdown en otras herramientas frente a MarsDawn', 'themes': 'Temas de la vista previa y exportación a PDF', 'sharing-exported-pdfs': 'Compartir los PDF exportados', 'reviewing-ai-output': 'Por qué lo que produce la IA todavía necesita un lector humano', 'reading-agent-output': 'Leer lo que te devuelve tu agente', 'agent-transparency': 'Transparencia de los agentes', 'reviewing-agent-plans': 'Revisar el plan de un agente', 'agent-design-patterns': 'Patrones de diseño de agentes', 'changelog': 'Historial de cambios', 'consent_text': 'Este sitio usa cookies de analítica para ver cómo lo usan los visitantes. Permanecen desactivadas a menos que las aceptes.', 'consent_accept': 'Aceptar', 'consent_decline': 'Rechazar', 'consent_aria': 'Consentimiento de cookies', 'cookie_settings': 'Ajustes de cookies', 'view_markdown_source': 'Ver el código Markdown'}
    store_chip = 'En el Mac App Store'
    trait_link = {'yours': ('Lo que escribes se queda en tu Mac', 'Sin cuenta, sin sincronización, sin nube.'), 'pay-once': ('Pruébalo gratis, paga una vez', 'Gratis durante 14 días; después, 4,99 USD una sola vez. Sin suscripción.'), 'pdf': ('Exportación a PDF', 'Diagramas, código resaltado, saltos de página cuidados.'), 'native': ('Una app para Mac', 'Ventanas y pestañas nativas, guardado automático, Vista rápida.'), 'limits': ('Lo que MarsDawn no hace', 'Lo que conviene saber antes de comprar.')}
    trait_nav_heading = 'Qué esperar de MarsDawn'
    figure_list_label = 'En esta captura de pantalla'
    # templates_pages.py UI entries
    templates_ui = {'templates': 'Plantillas', 'templates-spec': 'Plantilla de especificación', 'templates-flowchart': 'Plantilla de diagrama de flujo', 'templates-meeting-notes': 'Plantilla de notas de reunión'}
```

Co-authored-by: Grok <grok@southern-light.dev>
