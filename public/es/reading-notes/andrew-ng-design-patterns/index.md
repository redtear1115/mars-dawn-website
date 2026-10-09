# Andrew Ng ordena sus propios patrones de diseño según lo predecibles que son

**A lo largo de cinco cartas en The Batch a principios de 2024, Andrew Ng describió cuatro patrones de diseño agentic — reflexión, uso de herramientas, planificación y colaboración multiagente — y, de forma poco habitual, dijo a sus lectores sin rodeos cuáles le parecen más fiables y cuáles le cuesta predecir.**

## Lo que sostienen las cartas

`/agent-design-patterns/` ya cubre qué es cada uno de los cuatro patrones, qué documentos suele entregarte cada uno (nuestra inferencia), y el propio veredicto de Ng sobre la planificación, citado de la Parte 4: «while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.» Esta nota añade el mismo orden desde las dos cartas que esa página deja fuera: la Parte 3, escrita una semana antes de la Parte 4, donde enuncia el orden por adelantado, y la Parte 5, donde lo extiende al patrón que la Parte 4 no menciona — la colaboración multiagente. Al introducir el uso de herramientas, en la Parte 3, escribe:

> “In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.”

Dos semanas después, al cerrar la serie con la colaboración multiagente, confirma el mismo orden desde el otro lado:

> “Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.”

Lo dice sobre lo bien que cada patrón mejora los resultados de sus aplicaciones, no sobre con cuánto cuidado una persona debería comprobar su salida — nada en esta serie pide revisión humana, y nada menciona MarsDawn ni recomienda ninguna herramienta Markdown.

## Nuestra lectura, no la de Ng

El orden de Ng habla de calidad y previsibilidad de la salida desde la silla de quien construye, pero encaja, a grandes rasgos, con cuánta atención merece la pista en papel de cada patrón desde la tuya. Reflexión y uso de herramientas, los dos que encuentra más fiables, suelen entregarte algo que describe trabajo ya hecho — un borrador revisado, un informe de lo que corrió — así que comprobar una afirmación contra la salida real suele cubrir el riesgo. Planificación y colaboración multiagente, los dos que le cuesta predecir, suelen entregarte algo escrito antes de que ocurra el trabajo, o repartido en varios archivos de varios agentes: un plan que espera el visto bueno, o un traspaso entre agentes que la ejecución aún no ha probado. Según su propio relato, esos dos son exactamente los documentos donde la brecha entre lo escrito y lo que realmente pasará es más ancha — el mismo punto que `/reviewing-agent-plans/` saca del ensayo de Chip Huyen, en su sección «Por qué molestarse antes de que corra»: pillar un problema antes de que nada haya corrido es el sitio más barato para pillararlo.

## Dónde ayuda MarsDawn y dónde no

MarsDawn no sabe cuál de los cuatro patrones de Ng produjo un archivo dado, no ordena nada por previsibilidad y no tiene ningún modelo de IA dentro — no hará la comprobación que su orden sugiere que vale la pena. Mantiene el archivo legible mientras tú la haces: la pestaña Esquema (Visualización ▸ Mostrar barra lateral, ⌃⌘S) muestra la forma de un plan largo, el código y la vista previa renderizada van lado a lado (⌘2), y para un traspaso multiagente, abrir la carpeta compartida con Archivo ▸ Abrir carpeta… (⇧⌘O) muestra archivos nuevos en la pestaña Archivos en cerca de un segundo a medida que distintos agentes los escriben, con el encabezado nombrando la rama git o el worktree para que dos archivos con el mismo nombre de agentes distintos no se confundan.

## Probarlo

MarsDawn está en el Mac App Store. La herramienta de línea de comandos gratuita `marsdawn` ya funciona hoy:

```
brew install redtear1115/tap/marsdawn
```

Exporta Markdown a PDF sin la app.

[Línea de comandos](/es/cli/) · Antes de comprar: [Lo que MarsDawn no hace](/es/limits/)

## Siguiente

- Lo que cada patrón suele entregarte, completo: [Cuatro patrones de diseño de agentes y los documentos que cada uno te entrega](/es/agent-design-patterns/)
- La revisión de cinco minutos de un plan antes de que corra: [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/)
- Volver a la serie: [Notas de lectura de la redacción](/es/reading-notes/)

## Fuentes

- Andrew Ng, “Agentic Design Patterns Part 1,” The Batch, March 20, 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, “Agentic Design Patterns Part 3: Tool Use,” The Batch, April 3, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/) (obtenido y citado el 2026-09-26).
- Andrew Ng, “Agentic Design Patterns Part 4: Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/) (cita reutilizada literalmente de `design/inbox/276-agent-blog-series.md`, ya citada en `/agent-design-patterns/`).
- Andrew Ng, “Agentic Design Patterns Part 5, Multi-Agent Collaboration,” The Batch, April 17, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/) (obtenido y citado el 2026-09-26).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Editor de Markdown nativo para Mac: vista previa en vivo junto al código, Mermaid, KaTeX, Vista rápida, exportación a PDF. Pruébalo gratis, 4,99 USD una vez.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Ver Markdown en una Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.
- [Quick Look para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Presiona la barra espaciadora sobre un archivo Markdown en el Finder para leerlo renderizado, con diagramas Mermaid, fórmulas KaTeX y código resaltado. Vista rápida de MarsDawn no queda bloqueada por la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer muestra Markdown solo para lectura por 19,99 USD. MarsDawn edita y muestra la vista previa lado a lado: pruébalo gratis y luego paga 4,99 USD una sola vez en el Mac App Store.
- [Línea de comandos](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [marsdawn para agentes](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [Skill para agentes](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [Servidor MCP](https://marsdawn.southern-light.dev/es/cli/mcp/index.md): marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.
- [Revisión que ahorra tokens](https://marsdawn.southern-light.dev/es/token-efficient-review/index.md): Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.
- [Ver Markdown en otras herramientas frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/markdown-preview-tools/index.md): Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.
- [Temas de la vista previa y exportación a PDF](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa, cada uno con una paleta clara y una oscura, y una sola exportación a PDF e impresión que respeta el que estés usando. Crea tu propio tema en el navegador y explora la galería de la comunidad.
- [Crear un tema](https://marsdawn.southern-light.dev/es/themes/new/index.md): Elige colores y unas pocas opciones de estilo, míralos aplicados en vivo a un documento de ejemplo y envía tu tema como un issue de GitHub. Sin instalación, sin git.
- [Galería de temas](https://marsdawn.southern-light.dev/es/themes/gallery/index.md): Explora temas de vista previa que la comunidad envió para MarsDawn, fíltralos por escenario y denuncia un problema. Crea el tuyo en el navegador, sin instalación y sin git.
- [Compartir los PDF exportados](https://marsdawn.southern-light.dev/es/sharing-exported-pdfs/index.md): Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.
- [Por qué lo que produce la IA todavía necesita un lector humano](https://marsdawn.southern-light.dev/es/reviewing-ai-output/index.md): El Markdown escrito por una IA tiene que entenderlo una persona, no creerlo a simple vista. MarsDawn pone la página renderizada junto al código fuente y dibuja diagramas Mermaid y fórmulas KaTeX, para que la estructura se lea de un vistazo.
- [Leer lo que te devuelve tu agente](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
- [Transparencia de los agentes](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [Revisar el plan de un agente](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
- [Patrones de diseño de agentes](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
- [Historial de cambios](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en la herramienta de línea de comandos gratuita marsdawn.
- [Notas de lectura de la redacción](https://marsdawn.southern-light.dev/es/reading-notes/index.md): Seis notas breves sobre lo que argumentan de verdad las personas que construyen agentes de IA — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain y Andrew Ng — y qué significa cada una para quien tiene que leer lo que ese agente devuelve.
- [Notas de lectura: Anthropic](https://marsdawn.southern-light.dev/es/reading-notes/anthropic-building-effective-agents/index.md): La guía de Anthropic de diciembre de 2024 para quien construye agentes separa workflows de agentes y describe cinco patrones de workflow, incluido uno en el que una segunda llamada a un LLM revisa la primera. Qué significa eso para lo que aterriza en tu carpeta.
- [Notas de lectura: Chip Huyen](https://marsdawn.southern-light.dev/es/reading-notes/chip-huyen-agents/index.md): El ensayo «Agents» de Chip Huyen de enero de 2025 reparte las acciones de un agente en read-only y write. Por qué esa división es una forma rápida de ver, en un plan, la línea que merece una mirada más atenta antes de aprobar.
- [Notas de lectura: Lilian Weng](https://marsdawn.southern-light.dev/es/reading-notes/lilian-weng-llm-agents/index.md): La encuesta muy citada de Lilian Weng de 2023 describe un agente LLM como un cerebro más planificación, memoria y uso de herramientas. Qué suele dejarte cada parte para leer, y el límite que nombra en planes que no se ajustan a las sorpresas.
- [Notas de lectura: Harrison Chase](https://marsdawn.southern-light.dev/es/reading-notes/harrison-chase-what-is-an-agent/index.md): La definición de agente de Harrison Chase de 2024 y su espectro de comportamiento agentic, y su argumento a favor de la observabilidad a medida que un sistema avanza por él — leído desde quien lee el archivo que te devuelve.
- [Notas de lectura: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/es/reading-notes/langchain-what-is-an-agent/index.md): El «What is an AI agent?» de LangChain de Jess Ou (2026) recoge la definición de 2024 de Harrison Chase y describe un pipeline para evaluar agentes automáticamente. Dónde ese pipeline todavía entrega un paso a una persona — y dónde no.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-notes/andrew-ng-design-patterns/index.md): Über fünf Briefe in The Batch ordnet Andrew Ng Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit danach, wie verlässlich und vorhersagbar er jedes findet — und was diese Rangfolge dazu nahelegt, wie genau man die Ausgabe jedes Musters prüfen sollte.
- [Français](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
