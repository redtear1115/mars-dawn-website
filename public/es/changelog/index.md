# Historial de cambios

Qué cambió en la herramienta de línea de comandos gratuita marsdawn. Una versión de MarsDawn del Mac App Store se menciona aquí solo cuando tiene una línea propia. No se incluyen las versiones anteriores a la 0.5.1.

## marsdawn 0.6.3

6 de octubre de 2026. MarsDawn está en el Mac App Store.

- Cuando la app no está instalada, `marsdawn open` indica dónde encontrar MarsDawn en el Mac App Store.
- El README y la skill para agentes enseñan `marsdawn open .` y `--folder`: MarsDawn 1.0.0 muestra la carpeta en la barra lateral de la ventana.

## marsdawn 0.5.4

26 de septiembre de 2026. Correcciones de Mermaid, líneas de los errores de diagrama e instalación de la skill.

- En un diagrama de secuencia, la etiqueta de un mensaje que cruza las líneas de vida de otros participantes sigue siendo legible, en la vista previa y en los PDF exportados.
- `marsdawn export` puede con documentos llenos de diagramas Mermaid. Uno con 50 diagramas, que antes fallaba con el código 5, ahora se exporta.
- `marsdawn export --json` agrega `diagramErrorDetails`, con los números de línea de cada error de diagrama: dónde empieza el diagrama en tu documento y, cuando Mermaid indica una, la línea del propio error.
- `marsdawn skill --install` instala la skill para Claude Code en `~/.claude/skills/marsdawn/SKILL.md`, o en otra carpeta con `--dir`. Deja como está un archivo idéntico y solo reemplaza uno distinto con `--force`. Si no, termina con el código 64 (`skill_differs`) y no cambia nada.

## marsdawn 0.5.3

25 de septiembre de 2026. Estado de la carpeta, errores completos de Mermaid y correcciones menores.

- `marsdawn open --folder` puede decir qué pasó con la carpeta. Con una app que responde, espera hasta `--wait` segundos (2 de forma predeterminada), y `--json` da un estado como `attached` o `needsUser`.
- Un diagrama Mermaid que no se puede analizar muestra el mensaje de error completo de Mermaid en lugar de solo su primera línea, con el número de línea contado desde el inicio de tu documento.
- La búsqueda del final de un bloque de front matter se detiene después de 1000 líneas, así que un bloque sin cerrar ya no obliga a recorrer el resto de un documento grande.
- Una app puede darle al enlace de regreso de una nota al pie una etiqueta traducida para la exportación a PDF y la impresión. La etiqueta no se imprime en la página, y `marsdawn export` conserva la etiqueta en inglés.
- El highlight.js incluido ahora está fijado por versión, origen y SHA-256, igual que KaTeX y Mermaid.

## marsdawn 0.5.2

24 de septiembre de 2026. Notas al pie, contraste y carpetas.

- Las notas al pie se muestran en los PDF exportados: referencias numeradas, con las notas después del cuerpo del texto.
- Todos los temas cumplen el contraste WCAG AA, en claro y en oscuro. Clásico ahora es en blanco y negro.
- `marsdawn skill` muestra la skill para agentes que corresponde al marsdawn instalado.
- `marsdawn open` termina con el código 6 (`app_cannot_open_folders`) cuando el MarsDawn que encuentra no puede mostrar una carpeta, en lugar de informar que todo salió bien.
- Los marcadores de posición que se dibujan en las páginas exportadas también están en alemán, francés, español y coreano.
- Un marcador de posición de imagen ya no muestra la ruta absoluta que hay detrás de una ruta relativa muy larga.
- `MARSDAWN_APP_PATH` solo se usa cuando apunta a una app MarsDawn.

## marsdawn 0.5.1

19 de septiembre de 2026. Exportación a PDF y apertura de un archivo desde la línea de comandos.

- La capa de texto de un PDF exportado está reparada para chino, japonés y coreano.
- `marsdawn open --background` abre un archivo sin traer MarsDawn al frente.
- `marsdawn open` acepta una carpeta, y MarsDawn la muestra en la barra lateral de la ventana (MarsDawn 1.0.0 y posteriores).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Markdown para las personas que dirigen el trabajo de los agentes: un editor nativo para Mac con vista previa en vivo, diagramas Mermaid y exportación a PDF. En el Mac App Store.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Ver Markdown en una Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer muestra Markdown solo para lectura por 19,99 USD. MarsDawn edita y muestra la vista previa lado a lado: pruébalo gratis y luego paga 4,99 USD una sola vez en el Mac App Store.
- [Línea de comandos](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [marsdawn para agentes](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [Skill para agentes](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [Servidor MCP](https://marsdawn.southern-light.dev/es/cli/mcp/index.md): marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.
- [Revisión que ahorra tokens](https://marsdawn.southern-light.dev/es/token-efficient-review/index.md): Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.
- [Ver Markdown en otras herramientas frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/markdown-preview-tools/index.md): Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.
- [Temas de la vista previa y exportación a PDF](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa, cada uno con una paleta clara y una oscura, y una sola exportación a PDF e impresión que respeta el que estés usando. Están previstos más temas importables y una galería para compartir los tuyos.
- [Compartir los PDF exportados](https://marsdawn.southern-light.dev/es/sharing-exported-pdfs/index.md): Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.
- [Por qué lo que produce la IA todavía necesita un lector humano](https://marsdawn.southern-light.dev/es/reviewing-ai-output/index.md): El Markdown escrito por una IA tiene que entenderlo una persona, no creerlo a simple vista. MarsDawn pone la página renderizada junto al código fuente y dibuja diagramas Mermaid y fórmulas KaTeX, para que la estructura se lea de un vistazo.
- [Leer lo que te devuelve tu agente](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
- [Transparencia de los agentes](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [Revisar el plan de un agente](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
- [Patrones de diseño de agentes](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in the free marsdawn command-line tool.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): 免費的 marsdawn 命令列工具改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): 無料の marsdawn コマンドラインツールの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich im kostenlosen Befehlszeilenprogramm marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
