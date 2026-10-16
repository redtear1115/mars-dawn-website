# Cómo abrir archivos .md en Mac.

Haz doble clic en él. Si tu Mac lo abre en un editor de texto y ves `#` y `**` en lugar de títulos y negrita, el archivo está bien: un archivo `.md` es texto plano, y ese editor muestra el texto tal cual. Ábrelo en una app que renderice Markdown, como MarsDawn, y haz de esa app la predeterminada para que todos los archivos `.md` se abran allí.

Un archivo `.md` es texto plano. Los títulos, las palabras en negrita, las tablas y los diagramas están escritos como marcas: `#` para un título, `**` alrededor de la negrita, barras verticales para una tabla, un bloque de código `mermaid` para un diagrama. Si lo abres en un editor de texto plano, lees las marcas. Para leer la página como la pensó su autor, algo tiene que renderizarla.

## Abrir un archivo .md en tu Mac

1. **Haz doble clic en el archivo.** Se abre en la app que tu Mac tiene asignada a los archivos `.md`. Sin una app de Markdown, suele ser un editor de texto plano, que muestra las marcas en lugar de la página.
2. **Elige tú la app.** Haz clic en el archivo mientras mantienes pulsada la tecla Control y elige «Abrir con», y luego la app. O elige «Archivo ▸ Obtener información» (⌘I), elige una app en «Abrir con:» y haz clic en «Cambiar todo…» para que todos los archivos de este tipo se abran allí. MarsDawn abre archivos `.md`, `.markdown`, `.mdown`, `.mkd` y `.mkdn`.
3. **Ver sin abrir.** Selecciona el archivo en el Finder y pulsa la barra espaciadora. Con MarsDawn instalado, Vista rápida muestra la página renderizada, con los diagramas incluidos.

## Léelo en MarsDawn

MarsDawn es un editor de Markdown para Mac. Se descarga gratis desde el Mac App Store: prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta. Requiere macOS 26 o posterior.

[Descarga MarsDawn gratis en el Mac App Store](https://apps.apple.com/app/id6812925073)

Abre un archivo `.md` y lee la página renderizada junto al código fuente:

- La vista previa se actualiza mientras escribes, y los dos paneles se desplazan juntos.
- Los diagramas de flujo y de secuencia de [Mermaid](/es/mermaid-preview-mac/) se dibujan en la vista previa, y los bloques de código se resaltan.
- Cuando quieras cambiar algo, el código fuente está ahí mismo. MarsDawn es un editor, no solo un visor.

Si un agente de IA escribió el archivo, este es el ciclo para el que está hecho MarsDawn: el agente escribe, tú lo lees renderizado y el agente lo corrige. Consulta [la página de inicio](/es/) y [marsdawn para agentes](/es/cli/agents/) si quieres que un agente abra archivos por ti. Para saber por qué importa esa lectura y cómo revisar un plan, consulta [Leer lo que te devuelve tu agente](/es/reading-agent-output/) y [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/).

## Sin la app: conviértelo en PDF

La herramienta de línea de comandos gratuita `marsdawn` renderiza un archivo Markdown como PDF, que cualquier Mac puede abrir. Las tablas, las fórmulas, los diagramas Mermaid y el código resaltado salen renderizados, y no necesita nada más instalado, ni siquiera la app MarsDawn.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` escribe `notes.pdf` junto al archivo Markdown, y `open` lo muestra en tu visor de PDF. Requiere macOS 15 o posterior. La guía paso a paso, con una página exportada real, está en [Markdown a PDF](/es/markdown-to-pdf/).

## Preguntas

### ¿Qué es un archivo .md?

Un archivo `.md` es un archivo de texto plano escrito en Markdown, una forma de marcar el texto con caracteres sencillos: `#` para un título, `**` alrededor de la negrita, una barra vertical para una celda de tabla. Las extensiones `.markdown`, `.mdown`, `.mkd` y `.mkdn` significan lo mismo. Los desarrolladores lo usan para los README y la documentación, y los agentes de IA suelen devolver sus planes e informes como archivos `.md`.

### ¿Por qué mi archivo .md se abre como texto plano, con marcas # y **?

Porque es texto plano, y un editor de texto plano lo muestra tal cual. El archivo no tiene ningún problema. Para ver títulos, negrita, tablas y diagramas, ábrelo en una app que renderice Markdown. En MarsDawn, la página renderizada está junto al código fuente.

### ¿Por qué se abre con caracteres ilegibles?

Los caracteres ilegibles suelen significar que el archivo se guardó con una codificación de texto distinta de UTF-8 y que la app que lo abrió acertó mal. La solución es guardar una copia en UTF-8. MarsDawn abre en solo lectura un archivo de texto plano que no está en UTF-8, indica en una barra en la parte superior de la ventana la codificación con la que lo leyó y ofrece allí «Guardar como UTF-8…», o «Archivo ▸ Guardar como…» (⌥⇧⌘S), para escribir una copia en UTF-8 que puedes editar.

### ¿Puedo convertir un archivo .md en PDF?

Sí. En MarsDawn, elige «Archivo ▸ Exportar como PDF…» (⌥⌘E) o «Archivo ▸ Imprimir…»; las páginas se paginan, los diagramas se dibujan y el código se resalta, con los colores claros del tema. Sin la app, la herramienta de línea de comandos gratuita `marsdawn export` genera el mismo PDF: `marsdawn export notes.md`. Consulta [Exportación a PDF](/es/pdf/) y [De Markdown a PDF](/es/markdown-to-pdf/).

### ¿Puedo abrir los archivos .md que escribió mi agente de IA?

Sí, para eso está hecho MarsDawn. Abre el archivo y lee la página renderizada junto a su código fuente; cuando el agente lo revise, ábrelo de nuevo. Un agente también puede ejecutar `marsdawn open plan.md` para abrir el archivo en MarsDawn por ti. Consulta [Leer lo que te devuelve tu agente](/es/reading-agent-output/).

## Siguiente

- Todas las opciones de la herramienta de línea de comandos: [Línea de comandos](/es/cli/).
- Lo que MarsDawn no hace: [la lista](/es/limits/).
- Leer Markdown en VS Code, un navegador o Claude Desktop: [cómo se comparan](/es/vs/markdown-preview-tools/).
- Diagramas en un archivo Markdown: [Vista previa de Mermaid en Mac](/es/mermaid-preview-mac/).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Markdown para las personas que dirigen el trabajo de los agentes: un editor nativo para Mac con vista previa en vivo, diagramas Mermaid y exportación a PDF. En el Mac App Store.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados y más en la galería. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [Línea de comandos](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [marsdawn para agentes](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [Skill para agentes](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [Servidor MCP](https://marsdawn.southern-light.dev/es/cli/mcp/index.md): marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.
- [Revisión que ahorra tokens](https://marsdawn.southern-light.dev/es/token-efficient-review/index.md): Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.
- [Ver Markdown en otras herramientas frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/markdown-preview-tools/index.md): Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.
- [Temas de la vista previa y exportación a PDF](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa, cada uno con una paleta clara y una oscura, y una sola exportación a PDF e impresión que respeta el que estés usando. Crea tu propio tema en el navegador y explora la galería de la comunidad.
- [Crear un tema](https://marsdawn.southern-light.dev/es/themes/new/index.md): Elige colores y unas pocas opciones de estilo, míralos aplicados en vivo a un documento de ejemplo y envía tu tema como un issue de GitHub. Sin instalación, sin git.
- [Crea un tema con tu agente](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
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
- [Notas de lectura: Andrew Ng](https://marsdawn.southern-light.dev/es/reading-notes/andrew-ng-design-patterns/index.md): A lo largo de cinco cartas en The Batch, Andrew Ng ordena reflexión, uso de herramientas, planificación y colaboración multiagente según lo fiables y predecibles que le parecen — y qué sugiere ese orden sobre con cuánto cuidado conviene comprobar la salida de cada uno.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [日本語](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Français](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [한국어](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
