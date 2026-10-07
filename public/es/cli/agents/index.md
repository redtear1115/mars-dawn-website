# marsdawn para agentes

Una referencia para agentes de IA y scripts que llaman a la herramienta de línea de comandos `marsdawn`. Cada ejemplo de esta página se ejecutó con la herramienta compilada desde el código fuente actual.

**Para convertir un archivo Markdown en PDF, ejecuta `marsdawn export notes.md --json` y lee un objeto JSON de stdout.** Los diagramas Mermaid y el código resaltado se renderizan igual que en la app MarsDawn. `export` no necesita la app; `open`, sí.

## Qué hace

- `export` renderiza un archivo Markdown como un PDF paginado, con el mismo exportador que la app MarsDawn. No se abre ninguna ventana.
- `open` abre uno o varios archivos Markdown en la app MarsDawn para que una persona los revise; puede indicar la línea en la que debe abrirse cada archivo y mostrar una carpeta en la barra lateral de la ventana.

## Qué no hace

- No lee Markdown desde stdin. Pasa una ruta de archivo.
- No escribe el PDF en stdout. El PDF siempre va a un archivo; stdout solo lleva el resultado.
- No reemplaza un archivo existente a menos que pases `--force`.
- No carga imágenes de la web a menos que pases `--allow-remote-images`, y en ese caso solo por https.
- `open` no funciona si la app MarsDawn no está instalada; termina con el código 3. `export` no necesita la app. La app está en el [Mac App Store](https://apps.apple.com/app/id6812925073).
- MarsDawn 1.0 abre el archivo en la línea que indica `open`.
- Solo funciona en macOS.

## export

```
marsdawn export notes.md --json
```

Escribe `notes.pdf` junto a `notes.md`. Opciones:

- `-o, --output <path>`: dónde escribir el PDF. De forma predeterminada, la ruta de entrada con la extensión `.pdf`.
- `--theme <dawn|classic|modern|vivid>`: la paleta clara del tema. De forma predeterminada, `$MARSDAWN_THEME` y, si no, `dawn`.
- `--paper <a4|letter>`: tamaño de papel. De forma predeterminada, `a4`.
- `--allow-remote-images`: carga imágenes https de la web durante el renderizado.
- `--force`: reemplaza el archivo de salida si existe.
- `--json`: imprime un objeto JSON en stdout en lugar de texto.

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

Éxito, código de salida 0:

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`: ruta absoluta del PDF que se escribió.
- `pages`: número de páginas.
- `theme` y `paper`: los valores usados.
- `diagramErrors`: un mensaje por cada diagrama Mermaid que no se pudo renderizar. El PDF se escribe de todos modos.

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json
```

- `path:line` indica la línea en la que abrir. Una columna después, como en `notes.md:120:8`, se ignora. Un argumento que nombra un archivo existente siempre es ese nombre de archivo completo, así que un archivo llamado `weird:12` se abre tal cual.
- `--line <n>` indica la línea para un solo archivo, incluida una ruta que termina en dos puntos y dígitos. Necesita exactamente un archivo.
- Las líneas van de 1 a 999999999. Cualquier otro valor es un error de uso.
- Las líneas se agregaron en marsdawn 0.3.0. MarsDawn 1.0 abre el archivo en esa línea.
- Una carpeta como argumento se abre en la barra lateral de la ventana en lugar de como documento, así que `marsdawn open .` muestra la carpeta actual; `--folder <path>` hace lo mismo junto con archivos. La barra lateral de una ventana muestra una sola carpeta: indicar dos es un error de uso, igual que usar `--folder` dos veces, aunque sea para la misma carpeta; la misma carpeta repetida como argumento cuenta una vez. `--line` con una carpeta es un error de uso, porque una carpeta no tiene líneas. No existe `-a`: pasarlo es un error de uso que remite a `--folder`.
- `--background` abre sin traer MarsDawn al frente, para un agente que abre archivos mientras la persona trabaja en otra cosa. El JSON es el mismo en ambos casos.
- Las carpetas y `--background` se agregaron en marsdawn 0.5.1.

Éxito, código de salida 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`: un objeto por archivo, en el orden dado. `path` es la ruta absoluta del archivo; `line` solo aparece cuando se pidió una línea.
- `app`: ruta de la app MarsDawn que los abrió.

Con una carpeta (marsdawn 0.5.1 y posterior), código de salida 0:

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/project","requested":true},"ok":true,"opened":[{"path":"/path/to/project/notes.md"}]}
```

- `folder`: solo aparece cuando se dio una carpeta. `path` es su ruta absoluta. `requested` siempre es `true`: marsdawn le pidió a MarsDawn que mostrara la carpeta y no puede saber si la barra lateral la muestra, porque la app puede pedirle acceso a la persona primero. Infórmalo como solicitado, no como hecho.
- `opened` está vacío cuando solo se dio una carpeta.

marsdawn 0.2.x imprimía `opened` como una lista de rutas en texto. Revisa `marsdawn --version` si necesitas manejar ambos casos.

## Abrir archivos mientras Claude Code los edita

Un [hook de Claude Code](https://code.claude.com/docs/en/hooks) opcional: después de que Claude escribe o edita un archivo Markdown, lo abre en MarsDawn en segundo plano, una vez por archivo y por sesión. Está desactivado hasta que lo agregas, proyecto por proyecto, porque una ventana que no pediste se lleva tu atención. Ejecuta un comando de shell y no gasta tokens del modelo.

Necesita marsdawn 0.5.1 o posterior, por `--background`, y la app MarsDawn.

Guarda esto como `.claude/hooks/marsdawn-open.sh` en tu proyecto y hazlo ejecutable con `chmod +x`:

```
#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2>/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2>/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || { [ -x /opt/homebrew/bin/marsdawn ] && echo /opt/homebrew/bin/marsdawn; }) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${TMPDIR:-/tmp}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2>/dev/null && exit 0
echo "$file" >> "$seen"

"$marsdawn" open --background "$file" >/dev/null 2>&1 || true
exit 0
```

Luego agrega el hook a `.claude/settings.json` en el proyecto, o a `.claude/settings.local.json` para que sea solo tuyo:

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/marsdawn-open.sh" }
        ]
      }
    ]
  }
}
```

- Se ejecuta después de las herramientas Write y Edit de Claude. Los archivos que no terminan en `.md` o `.markdown` no se tocan.
- Cada archivo se abre una vez por sesión de Claude Code, sin importar cuántas veces Claude lo edite. La lista vive en `$TMPDIR/marsdawn-hook/`, un archivo por sesión, así que una sesión nueva vuelve a abrir el archivo.
- `--background` evita que MarsDawn pase al frente: la ventana en la que trabajabas conserva el foco.
- Nunca le estorba a Claude. Cada ruta termina con 0, y si marsdawn o la app MarsDawn no están instalados, no pasa nada.
- Lee la entrada del hook con `/usr/bin/jq`, que viene con macOS 26, la versión que necesita la app MarsDawn.
- Para desactivarlo, quita la entrada del archivo de configuración.

## Errores

Con `--json`, un error imprime un objeto JSON en stdout y termina con su código:

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: la entrada no existe, es una carpeta o no es texto UTF-8; o una ruta de `--folder` no existe o no es una carpeta.
- `3`, `app_not_installed`: MarsDawn no está instalado. Solo `open` devuelve este código.
- `4`, `output_exists`: el archivo de salida existe. Pasa `--force`.
- `5`, `export_failed`: la exportación en sí falló.
- `6`, `app_cannot_open_folders`: esta versión de MarsDawn no puede mostrar una carpeta, así que no se abrió nada. Solo `open` devuelve este código.
- `64`: error de uso, como una opción desconocida, un valor no válido, una línea fuera de rango, `--line` con más de un archivo o con una carpeta, más de una carpeta o `-a`. Este se imprime como texto en stderr, incluso con `--json`.

## Esquemas JSON

JSON Schema (draft 2020-12) para cada resultado de `--json`:

- [export.v1.json](/schemas/cli/export.v1.json): éxito de export
- [open.v3.json](/schemas/cli/open.v3.json): éxito de open, marsdawn 0.5.1 y posterior, incluida una carpeta mostrada en la barra lateral
- [error.v2.json](/schemas/cli/error.v2.json): error, ambos comandos, marsdawn 0.5.2 y posterior
- [open.v2.json](/schemas/cli/open.v2.json): éxito de open, marsdawn 0.3.0 a 0.5.0
- [open.v1.json](/schemas/cli/open.v1.json): éxito de open, marsdawn 0.2.x, donde `opened` era una lista de rutas
- [error.v1.json](/schemas/cli/error.v1.json): error, ambos comandos, marsdawn 0.5.1 y anterior

## Variables de entorno

- `MARSDAWN_THEME`: el tema que usa `export` cuando no se pasa `--theme`. Un valor desconocido vuelve a `dawn` sin error.

## Requisitos

- La herramienta funciona en macOS 15 o posterior. En chips de Apple, Homebrew instala un bottle precompilado y no se necesita nada más. Compilarla tú mismo, en una Mac con Intel o desde el código fuente, requiere Swift 6.2 o posterior, que viene con Xcode 26 o posterior.
- La app MarsDawn requiere macOS 26 o posterior.

## Instalación

Con Homebrew. En chips de Apple instala un bottle precompilado en segundos, sin necesidad de Xcode. En una Mac con Intel compila marsdawn desde el código fuente, lo que tarda unos minutos y requiere Xcode 26 o posterior.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

O compílala desde [el código fuente](https://github.com/redtear1115/mars-dawn-kit). La primera compilación descarga las dependencias y compila, lo que también tarda unos minutos.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` imprime el número de versión, como `0.3.0`, y termina con el código 0.

## Siguiente

- Una skill de un solo archivo para agentes que leen instrucciones en lugar de usar una shell: [la skill de marsdawn](/es/cli/skill/).
- Un servidor MCP que envuelve este mismo `export`: [marsdawn-mcp](/es/cli/mcp/).
- Por qué este resultado JSON sale barato para el contexto del propio agente: [revisión con pocos tokens](/es/token-efficient-review/).

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
- [Historial de cambios](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en la herramienta de línea de comandos gratuita marsdawn.
- [Plantillas](https://marsdawn.southern-light.dev/es/templates/index.md): Plantillas de Markdown para los documentos que escribe un agente y lees tú: una especificación, un diagrama de flujo y una minuta de reunión, cada una con un prompt para tu agente.
- [Plantilla de especificación](https://marsdawn.southern-light.dev/es/templates/spec/index.md): Una plantilla de especificación en Markdown con requisitos, un diagrama de flujo Mermaid y criterios de aceptación. Tu agente la completa; tú la revisas en MarsDawn.
- [Plantilla de diagrama de flujo](https://marsdawn.southern-light.dev/es/templates/flowchart/index.md): Una plantilla de diagrama de flujo Mermaid en Markdown, con los pasos escritos debajo. Previsualízala en la Mac y expórtala a PDF.
- [Plantilla de minuta de reunión](https://marsdawn.southern-light.dev/es/templates/meeting-notes/index.md): Una plantilla de minuta de reunión en Markdown con decisiones y tareas, cada una con un responsable. Tu agente la redacta; tú la revisas en MarsDawn.
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Français](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
