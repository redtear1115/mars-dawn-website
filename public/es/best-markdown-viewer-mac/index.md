# El mejor visor de Markdown para Mac (2026)

El mejor visor de Markdown depende de lo que leas. Si son notas que escribes tú, basta con una app de notas todo en uno. Si son documentos largos con diagramas y fórmulas, o archivos que un agente de IA reescribe una y otra vez, revisa cómo maneja cada app la recarga en vivo, Mermaid y el PDF. Las apps están en orden alfabético, cada una con para quién es, un defecto honesto y su precio.

## MacDown 3000

El MacDown original ya no se mantiene. MacDown 3000 es la continuación de la comunidad: gratis y de código abierto (MIT), nativo, con Mermaid, MathJax, exportación a PDF, recarga en vivo y Vista rápida.

- Para: quien quiere una vista dividida nativa y gratis.
- Defecto: no está documentado cómo abrir un archivo en una línea desde la línea de comandos.
- Precio: gratis.

## Marked

Marked 3 es una app de vista previa para el Markdown que escribes en otra app. Recarga en cuanto cambia el archivo, admite MathJax y KaTeX, e imprime PDF paginados con números de página. Marked 2 se sigue vendiendo.

- Para: quienes escriben en su propia herramienta y quieren una vista previa e impresión cuidadas.
- Defecto: Vista rápida es una app aparte, Marked QL (9,99 USD).
- Precio: Marked 3 se descarga gratis y luego cuesta 2,99 USD/mes, 29,99 USD/año o 69,99 USD de por vida. Marked 2 cuesta 14,99 USD directo o 13,99 USD en la Mac App Store.

## MarkEdit

Una app nativa, ligera y gratis (CodeMirror en una web view), con Vista rápida.

- Para: quien quiere una herramienta de texto plano rápida que se sienta propia del Mac.
- Defecto: Mermaid y las fórmulas necesitan las extensiones oficiales, y el PDF necesita Pandoc.
- Precio: gratis.

## MarsDawn

Una app nativa para Mac que muestra la fuente y una vista previa en vivo lado a lado, con Mermaid y KaTeX integrados. Cuando un agente guarda el archivo, la ventana abierta toma el cambio como una sola actualización desde el disco que puedes deshacer. `marsdawn open notes.md:120` abre un archivo en una línea, y hay un skill y un servidor MCP para agentes. Vista rápida funciona con o sin la prueba. «Copiar para IA» y «Copiar referencia» pasan texto a un agente. Nada sale de tu Mac a menos que tú lo decidas.

- Para: quien revisa el Markdown que escriben los agentes de IA.
- Defecto: el PDF exportado no tiene números de página.
- Precio: descarga gratis con 14 días de prueba y luego 4,99 USD una sola vez. Sin cuenta. Solo en la Mac App Store.

## Obsidian

Una app de notas construida en torno a una bóveda (vault) de archivos Markdown enlazados, con Mermaid, MathJax, exportación a PDF y recarga en vivo.

- Para: quien arma una base de conocimiento con sus propias notas.
- Defecto: es una app Electron y funciona mejor con archivos dentro de una bóveda.
- Precio: gratis. Sync y Publish son de pago.

## QLMarkdown

Una extensión de Vista rápida: selecciona un archivo .md en el Finder y presiona la barra espaciadora. Mermaid y MathJax son opcionales.

- Para: quien solo quiere echar un vistazo a los archivos en el Finder.
- Defecto: no es una app para leer ni editar, y no tiene exportación a PDF documentada.
- Precio: gratis (GPL-3.0).

## Typora

Una herramienta de escritura donde la vista previa es el documento, con Mermaid, MathJax y exportación a PDF con números de página en el encabezado o el pie.

- Para: quien prefiere escribir en una vista tipo WYSIWYG.
- Defecto: no muestra la fuente y la vista previa lado a lado.
- Precio: 14,99 USD una sola vez, hasta 3 dispositivos.

## Vista previa de VS Code

La vista previa de Markdown integrada, con Mermaid integrado desde la 1.121 y KaTeX. `code -g file:line` abre un archivo en una línea.

- Para: desarrolladores que ya trabajan todo el día en VS Code.
- Defecto: es una app Electron y no trae exportación a PDF.
- Precio: gratis.

## Comparativa

| App | Precio | Mermaid | Fórmulas | PDF | Recarga en vivo | CLI en una línea | Vista rápida | Tecnología |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | Gratis | Sí | MathJax | Sí | Sí | No documentado | Sí | Nativa |
| Marked 3 | Desde 2,99 USD/mes | Sí | MathJax, KaTeX | Sí, con números de página | Sí | No documentado | Marked QL, 9,99 USD | Nativa |
| MarkEdit | Gratis | Extensión | KaTeX (extensión) | Pandoc | No documentado | No documentado | Sí | Nativa (web view) |
| MarsDawn | 4,99 USD una vez | Sí | KaTeX | Sí, sin números de página | Sí, se puede deshacer | Sí | Sí | Nativa |
| Obsidian | Gratis | Sí | MathJax | Sí | Sí | No documentado | No documentado | Electron |
| QLMarkdown | Gratis | Opcional | MathJax (opcional) | No documentado | No aplica | No aplica | Es una | Nativa |
| Typora | 14,99 USD una vez | Sí | MathJax | Sí, con números de página | No documentado | No documentado | No documentado | Nativa |
| VS Code | Gratis | Sí (1.121+) | KaTeX | No | No documentado | Sí | No documentado | Electron |

## Para quién no es MarsDawn

- Necesitas números de página en tus PDF. Typora y Marked 3 los agregan, MarsDawn no.
- Mantienes una base de conocimiento de notas enlazadas. Obsidian está hecho para eso.
- Nunca sales de VS Code. Su vista previa integrada es gratis, y VS Code está agregando una vista de Markdown experimental a su ventana Agents.
- Solo quieres una vista previa en el Finder. QLMarkdown es gratis.

## Preguntas frecuentes

### ¿Qué visores de Markdown gratis para Mac tienen Mermaid?

MacDown 3000, Obsidian y VS Code (1.121 y posteriores) lo traen integrado. QLMarkdown lo ofrece como opción y MarkEdit mediante una extensión.

### ¿Cuáles exportan PDF con números de página?

Typora y Marked 3. MarsDawn exporta PDF sin números de página.

### ¿Cuáles abren un archivo en una línea concreta desde la línea de comandos?

MarsDawn (`marsdawn open notes.md:120`) y VS Code (`code -g file:line`). En los demás no está documentado.

### ¿Cuáles son apps nativas para Mac y no Electron?

Todas menos Obsidian y VS Code. MarkEdit es nativa, con su zona de edición en una web view.

[Descárgala y pruébala](https://apps.apple.com/app/id6812925073)

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin edición en iPhone o iPad, sin plugins, sin cuentas. Temas, pero sin CSS personalizado. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [Línea de comandos](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [marsdawn para agentes](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [Skill para agentes](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [Servidor MCP](https://marsdawn.southern-light.dev/es/cli/mcp/index.md): marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.
- [Revisión que ahorra tokens](https://marsdawn.southern-light.dev/es/token-efficient-review/index.md): Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.
- [Ver Markdown en otras herramientas frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/markdown-preview-tools/index.md): Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.
- [Temas](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa integrados, en claro y oscuro, y una galería revisada que abres desde Ajustes en MarsDawn para Mac. Vista rápida usa tu tema.
- [Crear un tema](https://marsdawn.southern-light.dev/es/themes/new/index.md): Elige colores y unas pocas opciones de estilo, míralos aplicados en vivo a un documento de ejemplo y envía tu tema como un issue de GitHub. Sin instalación, sin git.
- [Crea un tema con tu agente](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [Galería de temas](https://marsdawn.southern-light.dev/es/themes/gallery/index.md): Explora temas de vista previa para MarsDawn revisados por el desarrollador, fíltralos por escenario y denuncia un problema. Crea el tuyo en el navegador.
- [Compartir los PDF exportados](https://marsdawn.southern-light.dev/es/sharing-exported-pdfs/index.md): Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.
- [Por qué lo que produce la IA todavía necesita un lector humano](https://marsdawn.southern-light.dev/es/reviewing-ai-output/index.md): El Markdown escrito por una IA tiene que entenderlo una persona, no creerlo a simple vista. MarsDawn pone la página renderizada junto al código fuente y dibuja diagramas Mermaid y fórmulas KaTeX, para que la estructura se lea de un vistazo.
- [Leer lo que te devuelve tu agente](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
- [Transparencia de los agentes](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [Revisar el plan de un agente](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
- [Patrones de diseño de agentes](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
- [Historial de cambios](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [Hoja de ruta](https://marsdawn.southern-light.dev/es/roadmap/index.md): Lo que está en marcha y lo que viene para MarsDawn en Mac, iPhone y iPad, por versión. Sin fechas; las ideas sin planificar están marcadas.
- [Notas de lectura de la redacción](https://marsdawn.southern-light.dev/es/reading-notes/index.md): Seis notas breves sobre lo que argumentan de verdad las personas que construyen agentes de IA — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain y Andrew Ng — y qué significa cada una para quien tiene que leer lo que ese agente devuelve.
- [Notas de lectura: Anthropic](https://marsdawn.southern-light.dev/es/reading-notes/anthropic-building-effective-agents/index.md): La guía de Anthropic de diciembre de 2024 para quien construye agentes separa workflows de agentes y describe cinco patrones de workflow, incluido uno en el que una segunda llamada a un LLM revisa la primera. Qué significa eso para lo que aterriza en tu carpeta.
- [Notas de lectura: Chip Huyen](https://marsdawn.southern-light.dev/es/reading-notes/chip-huyen-agents/index.md): El ensayo «Agents» de Chip Huyen de enero de 2025 reparte las acciones de un agente en read-only y write. Por qué esa división es una forma rápida de ver, en un plan, la línea que merece una mirada más atenta antes de aprobar.
- [Notas de lectura: Lilian Weng](https://marsdawn.southern-light.dev/es/reading-notes/lilian-weng-llm-agents/index.md): La encuesta muy citada de Lilian Weng de 2023 describe un agente LLM como un cerebro más planificación, memoria y uso de herramientas. Qué suele dejarte cada parte para leer, y el límite que nombra en planes que no se ajustan a las sorpresas.
- [Notas de lectura: Harrison Chase](https://marsdawn.southern-light.dev/es/reading-notes/harrison-chase-what-is-an-agent/index.md): La definición de agente de Harrison Chase de 2024 y su espectro de comportamiento agentic, y su argumento a favor de la observabilidad a medida que un sistema avanza por él — leído desde quien lee el archivo que te devuelve.
- [Notas de lectura: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/es/reading-notes/langchain-what-is-an-agent/index.md): El «What is an AI agent?» de LangChain de Jess Ou (2026) recoge la definición de 2024 de Harrison Chase y describe un pipeline para evaluar agentes automáticamente. Dónde ese pipeline todavía entrega un paso a una persona — y dónde no.
- [Notas de lectura: Andrew Ng](https://marsdawn.southern-light.dev/es/reading-notes/andrew-ng-design-patterns/index.md): A lo largo de cinco cartas en The Batch, Andrew Ng ordena reflexión, uso de herramientas, planificación y colaboración multiagente según lo fiables y predecibles que le parecen — y qué sugiere ese orden sobre con cuánto cuidado conviene comprobar la salida de cada uno.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
