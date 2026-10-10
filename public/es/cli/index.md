# Línea de comandos

La herramienta de línea de comandos gratuita `marsdawn`: exporta Markdown a PDF desde una shell o un agente LLM y, si tienes instalada la app MarsDawn, abre archivos en ella.

**marsdawn es gratis y se distribuye por separado del Mac App Store.** Instálalo con Homebrew: en una Mac con chip de Apple llega listo para usar. `export` funciona por sí solo; `open` necesita la app MarsDawn.

¿Llamas a marsdawn desde un agente de IA o un script? Consulta [marsdawn para agentes](/es/cli/agents/) para ver la salida JSON, sus esquemas y todos los códigos de salida, o [el servidor MCP](/es/cli/mcp/) si tu agente llama a herramientas por MCP.

## Instalación

Con [Homebrew](https://brew.sh):

```
brew tap redtear1115/tap && brew install marsdawn
```

¿Usas un agente de programación? [Agrega la skill de marsdawn](/es/cli/skill/): un solo archivo que le enseña a abrir lo que escribió en MarsDawn para que lo revises, y a exportar PDF.

En una Mac con chip de Apple, Homebrew instala una copia precompilada en segundos, sin nada más que instalar. En una Mac con Intel, compila marsdawn desde el código fuente, lo que toma unos minutos y requiere Xcode 26 o posterior (Swift 6.2). La herramienta funciona en macOS 15 o posterior.

O compílala desde [el código fuente](https://github.com/redtear1115/mars-dawn-kit) con Swift Package Manager:

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

Revisa qué versión tienes con `marsdawn --version`.

## Comandos

### marsdawn open

Abre uno o varios archivos Markdown en la app MarsDawn para que los revises. Necesita la app instalada: sin ella, `marsdawn open` termina con el código 3 e indica que MarsDawn no está instalado. `export` no necesita la app. La app está en el [Mac App Store](https://apps.apple.com/app/id6812925073).

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .
```

- `path:line`: le pide a MarsDawn que vaya a esa línea. Una columna después, como en `notes.md:120:8`, se ignora. Si existe un archivo con el nombre completo, el argumento es ese archivo.
- `--line <n>`: lo mismo para un solo archivo, y la manera de pedir una línea en una ruta que termina en dos puntos y dígitos. Requiere exactamente un archivo.
- Las líneas van de 1 a 999999999.
- MarsDawn 1.0 abre el archivo en esa línea.
- Una carpeta como argumento se abre en la barra lateral de la ventana en lugar de como documento: `marsdawn open .` muestra la carpeta actual. `--folder <path>` hace lo mismo junto con archivos. La barra lateral de una ventana muestra una carpeta, así que indicar dos es un error de uso.
- `--background`: abrir sin traer MarsDawn al frente.
- `--json`: mostrar un resultado JSON en lugar de texto.

Las líneas llegaron con marsdawn 0.3.0, y las carpetas y `--background` con la 0.5.1.

### marsdawn export

Convierte un archivo Markdown en un PDF paginado, con el mismo exportador que usa la exportación a PDF de MarsDawn. No necesita la app MarsDawn. Las imágenes relativas se resuelven a partir de la carpeta del archivo de entrada.

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`: dónde escribir el PDF. De forma predeterminada, la ruta de entrada con la extensión `.pdf`.
- `--theme <dawn|classic|modern|vivid>`: la paleta clara del tema de la vista previa. De forma predeterminada, `$MARSDAWN_THEME` y, si no, `dawn`.
- `--paper <a4|letter>`: tamaño del papel. De forma predeterminada, `a4`.
- `--allow-remote-images`: cargar imágenes de la web durante el renderizado. Desactivado de forma predeterminada.
- `--force`: reemplazar el archivo de salida si ya existe.
- `--json`: mostrar un resultado JSON en lugar de texto.

## La variable $MARSDAWN_THEME

Cuando no se pasa `--theme`, `export` lee la variable de entorno `$MARSDAWN_THEME`. Su valor debe ser `dawn`, `classic`, `modern` o `vivid`; cualquier otro vuelve a `dawn`. La CLI no lee el ajuste de tema de la propia app, porque leer el contenedor de otra app puede hacer que macOS muestre un aviso de privacidad.

## Sobrescribir archivos

`export` se niega a reemplazar un archivo de salida existente a menos que pases `--force`.

## Códigos de salida

| Código | Significado | Qué hacer |
|---|---|---|
| `0` | éxito. | Con `--json`, lee la única línea JSON en stdout |
| `2` | no se encontró la entrada. | Revisa la ruta y el nombre del archivo |
| `3` | MarsDawn no está instalado (solo `open`). | Instala la app, o usa `export`, que no la necesita |
| `4` | la salida ya existe (pasa `--force`). | Pasa `--force` para reemplazarlo, o `-o` para escribir en otro lugar |
| `5` | falló la exportación. | Lee `message` en el resultado JSON |
| `6` | este MarsDawn no puede mostrar una carpeta, así que no se abrió nada (solo `open`). |  |
| `64` | error de uso, incluidos una línea fuera de rango, `--line` con más de un archivo o con una carpeta, o más de una carpeta. | Corrige la opción o el valor; este error sale como texto en stderr, incluso con `--json` |

## Salida --json

Si todo sale bien, `marsdawn open --json` muestra `ok`, `opened` (una lista con el `path` de cada archivo, más `line` cuando se pidió una), `app` (la ruta de la app) y, cuando se indicó una carpeta, `folder`. `marsdawn export --json` muestra `ok`, `output`, `pages`, `theme`, `paper` y `diagramErrors`. Si algo falla, ambos muestran `ok`, `error` y `message`.

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): MarsDawn es un editor Markdown nativo para Mac: vista previa en vivo, Mermaid, KaTeX, Vista rápida, exportación PDF. Pruébalo gratis; luego, 4,99 USD una vez.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Ver Markdown en una Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.
- [Quick Look para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer muestra Markdown solo para lectura por 19,99 USD. MarsDawn edita y muestra la vista previa lado a lado: pruébalo gratis y luego paga 4,99 USD una sola vez en el Mac App Store.
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
- [Notas de lectura: Andrew Ng](https://marsdawn.southern-light.dev/es/reading-notes/andrew-ng-design-patterns/index.md): A lo largo de cinco cartas en The Batch, Andrew Ng ordena reflexión, uso de herramientas, planificación y colaboración multiagente según lo fiables y predecibles que le parecen — y qué sugiere ese orden sobre con cuánto cuidado conviene comprobar la salida de cada uno.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [Français](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
