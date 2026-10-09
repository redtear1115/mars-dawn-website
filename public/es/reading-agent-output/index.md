# El trabajo de tu agente vuelve como un archivo Markdown.

Le pides a un agente de programación que planifique una migración, escriba una especificación o persiga un bug. Trabaja solo un rato y luego te entrega un archivo: `plan.md`, `SPEC.md`, un informe de avance, un resumen de investigación. Hasta donde puedes comprobar el trabajo, ese archivo es el trabajo.

**Si el agente lo hizo bien, lo averiguas leyendo lo que te entrega. MarsDawn es una app para Mac hecha para esa lectura.**

## Qué dicen quienes construyen agentes

Citado tal como se escribió; nuestra lectura viene después.

- «Building Effective Agents», de Anthropic (Erik S. y Barry Zhang, diciembre de 2024), propone tres principios básicos para construir agentes. Uno es «Prioriza la transparencia mostrando explícitamente los pasos de planificación del agente». Está escrito para quienes construyen agentes. Desde tu lado, esa transparencia es el plan que terminas leyendo.
- El mismo artículo: «Luego, los agentes pueden hacer una pausa para recibir comentarios humanos en puntos de control o cuando encuentran obstáculos». Fíjate en el verbo: *pueden*.
- Chip Huyen, en «Agents» (enero de 2025), sobre por qué la planificación debe estar separada de la ejecución: «Sin supervisión, un agente puede ejecutar esos pasos durante horas, desperdiciando tiempo y dinero en llamadas a la API, antes de que te des cuenta de que no va a ninguna parte». También describe un fallo en el que «el agente está convencido de que completó una tarea cuando no es así». Si le pides que aloje a 50 personas en 30 habitaciones de hotel, ubica a 40 e insiste en que terminó.
- Andrew Ng, sobre el patrón de diseño de planificación en The Batch (abril de 2024): «Por un lado, la planificación es una capacidad muy poderosa; por otro, produce resultados menos predecibles». Es una observación sobre la previsibilidad, no un llamado a la revisión humana, y él espera que la planificación mejore rápido.

**Nuestra conclusión, no la de ellos:** si un agente expone su plan y se detiene en puntos de control, alguien lee ese plan en el punto de control, y casi siempre eres tú. Si un agente puede creer que terminó cuando no es así, su informe de «listo» también necesita un lector. Ninguno de estos autores menciona MarsDawn ni lo recomienda, ni tampoco ninguna otra herramienta de Markdown.

## Por qué cuesta más leerlo de lo que parece

El archivo es largo, y la parte que importa rara vez está arriba. Tiene diagramas Mermaid y fórmulas que cuesta seguir como código fuente. Puede que el agente lo siga reescribiendo cuando vas por la mitad. Suele ser uno de varios archivos, a veces repartidos entre ramas o worktrees. Y cuando encuentras un problema, «la parte del caché se ve rara» deja al agente adivinando; «`docs/plan.md:42` borra la tabla vieja antes de que termine el backfill», no.

## Dónde ayuda MarsDawn

- **Archivos largos:** la pestaña Esquema de la barra lateral (⌃⌘S) lista los títulos. Haz clic en uno y los dos paneles saltan ahí.
- **Diagramas y fórmulas:** Mermaid y KaTeX se dibujan en la vista previa junto al código fuente (⌘2), y los dos paneles se desplazan juntos.
- **Reescrito mientras lees:** cuando el agente reescribe el archivo, MarsDawn lo vuelve a cargar y conserva tu posición, siempre que no tengas cambios propios sin guardar.
- **Varios archivos:** abre la carpeta del agente con Archivo ▸ Abrir carpeta… (⇧⌘O). Los archivos nuevos aparecen en la pestaña Archivos en aproximadamente un segundo y, en un checkout de git, el encabezado indica la rama o el worktree.
- **Comentarios exactos:** Edición ▸ Copiar referencia (⌥⌘C) copia tu posición como `docs/plan.md:42`. Copiar para IA (⌃⌥⌘C) agrega el texto seleccionado debajo. Pega cualquiera de los dos en el chat con el agente.

Dos más para el ciclo: un agente puede ejecutar `marsdawn open plan.md:42` para abrir el archivo en MarsDawn en la línea 42, la que quiere que veas primero, y un archivo revisado se exporta a PDF desde la app o con el comando gratuito `marsdawn export`.

MarsDawn no tiene ningún modelo de IA dentro. No resume el plan, no lo califica ni te dice qué está mal. Tú lees; la app mantiene legible un archivo largo que cambia y te deja señalar la línea exacta.

## Revisar el plan de un agente en cinco minutos

Esto funciona en cualquier editor.

1. Lee solo los títulos. ¿El esquema coincide con lo que pediste? Una sección que falta suele significar trabajo que falta.
2. Busca cada lugar que diga que algo está hecho, que pasa o que se verificó, y comprueba uno tú mismo: abre el archivo, ejecuta la prueba, cuenta las filas.
3. Busca pasos que no se pueden deshacer: borrar datos, migraciones, force-push, cualquier cosa que envíe, pague o publique. Esos esperan tu sí explícito.
4. Lee los diagramas renderizados y compara cada flecha con el texto.
5. Haz una lista de los archivos y sistemas que toca el plan. Pregunta por todo lo que no pediste antes de que se ejecute.
6. Escribe los comentarios como lugar, problema, solución: «`plan.md:88`: el backfill se ejecuta después del borrado. Intercambia los pasos 4 y 5». Un problema por línea.

¿Poco tiempo? Haz el paso 2. Ahí es donde se descubre a un agente que cree que terminó. La versión larga, con un ejemplo completo: [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/).

## Pruébalo

MarsDawn está en el [Mac App Store](https://apps.apple.com/app/id6812925073). También existe la herramienta de línea de comandos gratuita `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Exporta Markdown a PDF sin la app, y `marsdawn open` le permite a tu agente abrir archivos en MarsDawn por ti.

[Línea de comandos](/es/cli/) · [marsdawn para agentes](/es/cli/agents/) · Antes de comprar: [Lo que MarsDawn no hace](/es/limits/)

## Siguiente

- El argumento breve para leer lo que genera la IA: [Por qué lo que genera la IA todavía necesita un lector humano](/es/reviewing-ai-output/).
- Mantener pequeño el contexto del agente mientras revisas: [revisión con pocos tokens](/es/token-efficient-review/).
- Por qué los agentes muestran sus planes: [Anthropic dice que los agentes deben ser transparentes. ¿Quién lee lo que muestran?](/es/agent-transparency/)
- La lista de arriba, paso a paso con un ejemplo: [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/).
- Qué documentos te entregan los distintos tipos de agentes: [Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno](/es/agent-design-patterns/).

## Fuentes

- Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (citado de la versión publicada el 26/09/2026; el artículo ahora indica que buena parte de las herramientas que describe cambió desde diciembre de 2024).
- Chip Huyen, «Agents», 7 de enero de 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, «Agentic Design Patterns Part 4, Planning», The Batch, 10 de abril de 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

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
- [Notas de lectura: Andrew Ng](https://marsdawn.southern-light.dev/es/reading-notes/andrew-ng-design-patterns/index.md): A lo largo de cinco cartas en The Batch, Andrew Ng ordena reflexión, uso de herramientas, planificación y colaboración multiagente según lo fiables y predecibles que le parecen — y qué sugiere ese orden sobre con cuánto cuidado conviene comprobar la salida de cada uno.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Français](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
