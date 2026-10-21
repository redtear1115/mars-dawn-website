# Historial de cambios

Qué cambió en cada versión de la app MarsDawn del Mac App Store y de la herramienta de línea de comandos gratuita marsdawn. En la app, la fecha es el día en que la versión apareció en el Mac App Store.

## App MarsDawn

### MarsDawn 1.1.1

15 de octubre de 2026

- En alemán, japonés, español y francés, Ajustes > Aspecto > «Obtener más temas…» ahora muestra el filtro de escenario como un menú desplegable con la etiqueta «Escenario», para que quepan las cinco opciones. En inglés, coreano y chino se sigue usando el control segmentado.
- Cuando un tema se retira de la galería, el aviso de «Obtener más temas…» ahora muestra el nombre del tema (por ejemplo, Inkwell Ivory) en lugar de su identificador interno.
- Las secciones details plegables escritas al estilo de GitHub ahora empiezan plegadas, con su resumen visible, en la vista previa y en Vista rápida, y se abren con un clic. La exportación a PDF sigue imprimiendo el contenido de todas las secciones.
- Los documentos que abres desde el Finder, el Dock, Archivo > «Abrir…» o el comando marsdawn open ahora se abren como pestañas en la ventana del frente, igual que los documentos nuevos. Para mantener el comportamiento anterior, elige «Seguir ajuste del sistema» en Ajustes > Aspecto.

Las versiones anteriores solo tienen notas en inglés: [ver el historial en inglés](/changelog/).

## Herramienta de línea de comandos marsdawn

No se incluyen las versiones anteriores a la 0.5.1.

### marsdawn 0.7.2

20 de octubre de 2026. La disposición Guía, los avisos destacados y las fuentes japonesas.

- El valor de `--layout` pasa a ser `handbook`, la disposición Guía de la app: `marsdawn export --layout handbook`. `--layout manual` sigue funcionando, pero está obsoleto.
- Los avisos destacados se muestran, en la vista previa y en los PDF exportados: las alertas de GitHub como `> [!NOTE]` y `> [!WARNING]`, y los contenedores de HackMD como `:::info` y `:::warning`. `:::spoiler` crea una sección plegable.
- Un documento en japonés usa fuentes japonesas para sus kana y kanji. marsdawn toma el idioma de `lang: ja` en el front matter o de la proporción de kana del texto.
- Tras un `export` o un `open` correcto en una terminal, marsdawn muestra una vez una sugerencia en stderr si falta la skill para agentes o está desactualizada. La salida en stdout y con `--json` no cambia. Define `MARSDAWN_NO_SKILL_HINT=1` para no mostrarla.

### marsdawn 0.7.1

20 de octubre de 2026. Una disposición Guía y un tamaño máximo.

- `marsdawn export --layout manual` genera una guía: márgenes más anchos, un lado de encuadernación de 25 mm y cada encabezado de primer nivel en una página nueva, además de una portada con title, subtitle, version, date, author y logo del front matter, una tabla de contenido de los encabezados de nivel 1 y 2 con números de página, números de página `n / N` y marcadores PDF. `--toc-title` fija el título de la página de contenido. `--layout document` sigue siendo el predeterminado.
- `<!--BREAK-->` solo en una línea empieza una página nueva, en ambas disposiciones.
- `marsdawn export` rechaza un archivo de más de 16 MiB: termina con el código 5, informa `input_too_large` con `--json` y no escribe nada.
- La página de vista previa quita los elementos script y noscript; un diagrama Mermaid redibujado conserva su propio SVG.
- Una referencia de carácter que se decodifica como `=` o `^`, como `&#61;`, ya no se empareja con una marca de HackMD.

### marsdawn 0.7.0

18 de octubre de 2026. Markdown de HackMD, saltos de línea y límites para documentos muy grandes.

- Se muestran las marcas en línea de HackMD: `==mark==`, `^sup^` y `~sub~`. Un párrafo con solo `[TOC]` se convierte en una tabla de contenido, se aplican los tamaños de imagen de HackMD, las etiquetas de inserción pasan a ser enlaces https normales, y el lenguaje de un bloque de código se lee antes que las opciones de HackMD como `js=`.
- `marsdawn export --breaks` convierte cada salto de línea dentro de un párrafo en un salto de línea, como HackMD. Sin esta opción, un salto de línea entre dos caracteres chinos o japoneses desaparece, y las líneas se leen como una sola frase. El coreano conserva su espacio, porque separa sus palabras con espacios.
- Los documentos muy grandes tienen límites, en la vista previa y en los PDF exportados. Un bloque de código de más de 128K caracteres no se resalta, y el resaltado se detiene tras 256K caracteres en total. Se dibujan hasta 100 diagramas Mermaid y 1000 fórmulas por actualización; los demás diagramas muestran su código fuente, con una nota, aunque ya se hubieran dibujado antes.
- En un diagrama de secuencia, la etiqueta de un mensaje dentro de un bloque `rect` recibe un halo del color del bloque.
- Una referencia a nota al pie justo encima de una tabla ya no hace fallar `marsdawn export`.
- `marsdawn skill --install` termina con el código 7 (`skill_install_failed`) si no puede crear la carpeta o escribir el archivo, y deja como estaba un SKILL.md existente.

### marsdawn 0.6.4

13 de octubre de 2026. Bloques `<details>` plegables.

- Un bloque `<details>` al estilo de GitHub con líneas en blanco dentro se muestra como un solo elemento plegable, en la vista previa y en los PDF exportados. Antes se partía en la primera línea en blanco.
- La exportación a PDF abre todos los bloques `<details>` antes de imprimir, salvo el front matter.
- La vista previa conserva su posición de desplazamiento cuando abres o cierras un bloque `<details>`.

### marsdawn 0.6.3

6 de octubre de 2026. MarsDawn está en el Mac App Store.

- Cuando la app no está instalada, `marsdawn open` indica dónde encontrar MarsDawn en el Mac App Store.
- El README y la skill para agentes enseñan `marsdawn open .` y `--folder`: MarsDawn 1.0.0 muestra la carpeta en la barra lateral de la ventana.

### marsdawn 0.6.1

29 de septiembre de 2026. Comprobar un tema.

- `marsdawn theme validate` comprueba un `theme.json` con las reglas que usa la app. Termina con el código 0 si el tema es válido y con 1 si no, y enumera cada problema. `--require-complete` exige también los colores de sintaxis y de diagramas.
- `marsdawn theme css` muestra el CSS que usa la vista previa para un tema válido, y `marsdawn theme preview` genera con él un documento de ejemplo en un PNG, claro u oscuro.

### marsdawn 0.5.4

26 de septiembre de 2026. Correcciones de Mermaid, líneas de los errores de diagrama e instalación de la skill.

- En un diagrama de secuencia, la etiqueta de un mensaje que cruza las líneas de vida de otros participantes sigue siendo legible, en la vista previa y en los PDF exportados.
- `marsdawn export` puede con documentos llenos de diagramas Mermaid. Uno con 50 diagramas, que antes fallaba con el código 5, ahora se exporta.
- `marsdawn export --json` agrega `diagramErrorDetails`, con los números de línea de cada error de diagrama: dónde empieza el diagrama en tu documento y, cuando Mermaid indica una, la línea del propio error.
- `marsdawn skill --install` instala la skill para Claude Code en `~/.claude/skills/marsdawn/SKILL.md`, o en otra carpeta con `--dir`. Deja como está un archivo idéntico y solo reemplaza uno distinto con `--force`. Si no, termina con el código 64 (`skill_differs`) y no cambia nada.

### marsdawn 0.5.3

25 de septiembre de 2026. Estado de la carpeta, errores completos de Mermaid y correcciones menores.

- `marsdawn open --folder` puede decir qué pasó con la carpeta. Con una app que responde, espera hasta `--wait` segundos (2 de forma predeterminada), y `--json` da un estado como `attached` o `needsUser`.
- Un diagrama Mermaid que no se puede analizar muestra el mensaje de error completo de Mermaid en lugar de solo su primera línea, con el número de línea contado desde el inicio de tu documento.
- La búsqueda del final de un bloque de front matter se detiene después de 1000 líneas, así que un bloque sin cerrar ya no obliga a recorrer el resto de un documento grande.
- Una app puede darle al enlace de regreso de una nota al pie una etiqueta traducida para la exportación a PDF y la impresión. La etiqueta no se imprime en la página, y `marsdawn export` conserva la etiqueta en inglés.
- El highlight.js incluido ahora está fijado por versión, origen y SHA-256, igual que KaTeX y Mermaid.

### marsdawn 0.5.2

24 de septiembre de 2026. Notas al pie, contraste y carpetas.

- Las notas al pie se muestran en los PDF exportados: referencias numeradas, con las notas después del cuerpo del texto.
- Todos los temas cumplen el contraste WCAG AA, en claro y en oscuro. Clásico ahora es en blanco y negro.
- `marsdawn skill` muestra la skill para agentes que corresponde al marsdawn instalado.
- `marsdawn open` termina con el código 6 (`app_cannot_open_folders`) cuando el MarsDawn que encuentra no puede mostrar una carpeta, en lugar de informar que todo salió bien.
- Los marcadores de posición que se dibujan en las páginas exportadas también están en alemán, francés, español y coreano.
- Un marcador de posición de imagen ya no muestra la ruta absoluta que hay detrás de una ruta relativa muy larga.
- `MARSDAWN_APP_PATH` solo se usa cuando apunta a una app MarsDawn.

### marsdawn 0.5.1

19 de septiembre de 2026. Exportación a PDF y apertura de un archivo desde la línea de comandos.

- La capa de texto de un PDF exportado está reparada para chino, japonés y coreano.
- `marsdawn open --background` abre un archivo sin traer MarsDawn al frente.
- `marsdawn open` acepta una carpeta, y MarsDawn la muestra en la barra lateral de la ventana (MarsDawn 1.0.0 y posteriores).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados y más en la galería. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [El mejor visor de Markdown para Mac (2026)](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Deutsch](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
