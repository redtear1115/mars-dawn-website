# Todo lo que hace MarsDawn, en una sola página.

MarsDawn es un editor de Markdown para Mac. Escribes en un lado y lees la página renderizada en el otro, con los diagramas, las fórmulas y el código ya dibujados. No tiene un modelo de IA propio: está hecho para leer lo que escribió un agente y para escribir lo tuyo. Y cuando el trabajo pasa a una mesa, a una reunión o a un archivador, imprime y exporta páginas limpias.

Cada sección de abajo cuenta qué hace la app y enlaza a la página que lo explica con más detalle.

![MarsDawn en vista dividida: el código Markdown a la izquierda y la página renderizada a la derecha.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

En esta captura de pantalla:

1. Una ventana nativa de Mac.
2. El editor de texto de la Mac, con resaltado de Markdown.
3. ⌘1 código, ⌘2 dividido, ⌘3 vista previa.
4. La página se actualiza mientras escribes.

## Lee lo que escribió tu agente

### Código y vista previa, lado a lado

Abre un archivo Markdown y lee la página renderizada junto a su código (⌘2), o cambia a solo código (⌘1) o solo vista previa (⌘3). Los dos paneles se desplazan juntos y la página se actualiza mientras escribes.

[Una app para Mac](/es/native/)

### Esquema y archivos en la barra lateral

La pestaña Esquema de la barra lateral enumera los encabezados de un documento; haz clic en uno para ir a él. Abre una carpeta y la pestaña Archivos muestra lo que contiene; los archivos nuevos aparecen solos mientras un agente escribe en ella. Si la carpeta es un repositorio git, la cabecera nombra la rama o el worktree.

[Leer lo que te devuelve tu agente](/es/reading-agent-output/)

### Señala la línea exacta

Edición ▸ Copiar referencia copia dónde estás como una ruta y una línea, por ejemplo `docs/plan.md:42`. Copiar para IA agrega debajo el texto seleccionado. Pega cualquiera de los dos en el chat del agente.

[Leer lo que te devuelve tu agente](/es/reading-agent-output/)

### Sigue los enlaces entre archivos

Haz clic en la vista previa en un enlace a otro archivo Markdown y MarsDawn lo abre, o lo trae al frente si ya está abierto, y se desplaza hasta el encabezado.

## En papel, entre personas

No todo el trabajo ocurre en una pantalla. Las páginas que MarsDawn imprime y exporta son las mismas que lees en pantalla, así que sirven allí donde la gente se reúne, lee y guarda registros.

### En la reunión

Imprime las páginas, o envía a todos el mismo PDF, y toda la mesa trabaja con el mismo documento en lugar de una sola pantalla compartida. Quien tiene el mismo archivo tiene los mismos saltos de página, así que «la tabla de la página 3» señala una sola cosa. Después, las personas anotan las decisiones, en la copia impresa o en notas. La plantilla de notas de reunión empieza por las decisiones y asigna un responsable a cada tarea.

[Exportación a PDF](/es/pdf/) · [Plantilla de minuta de reunión](/es/templates/meeting-notes/)

### Leer con un bolígrafo

Hay quien asimila mejor con un bolígrafo: subrayar, escribir en el margen, para que se quede. Imprime el documento y hazlo en papel. MarsDawn no tiene una herramienta de anotación propia, así que, si prefieres marcar el PDF, usa la app de PDF que ya tienes.

[Exportación a PDF](/es/pdf/)

### Registros en papel

En algunos sectores todavía se archiva en papel, como la contabilidad. MarsDawn no afirma nada sobre archivo ni cumplimiento normativo. Lo que hace es imprimir y exportar páginas limpias y paginadas: diagramas dibujados, bloques de código cortos sin partir, los colores claros del tema. Úsalas dondequiera que el papel siga siendo el registro.

[Exportación a PDF](/es/pdf/)

### Pasárselo a alguien que no usa Markdown

Un PDF se abre en cualquier parte y no requiere saber Markdown, así que también es el que conviene enviar a un jefe o a un cliente.

[Compartir los PDF exportados](/es/sharing-exported-pdfs/)

## Escribe y da formato

### Markdown sencillo, resaltado

La negrita, la cursiva, el tachado, el código en línea, los enlaces, las citas y las listas de tareas funcionan. El editor colorea la sintaxis de Markdown, y los colores coinciden con el tema de tu vista previa.

[Una app para Mac](/es/native/)

### Zoom, números de línea y barra de estado

Acerca y aleja el código y la vista previa a la vez, del 50 % al 300 %. Junto al código hay un margen con números de línea, y la barra de estado muestra tu línea y columna, además del recuento de palabras y caracteres y el tiempo de lectura del documento o de tu selección.

### Imágenes

Guarda el documento y después arrastra o pega una imagen en el editor. MarsDawn la copia en una carpeta assets junto al documento y escribe el enlace. Las imágenes de la web siguen ocultas hasta que haces clic en Cargar imágenes, así que abrir un documento no le dice a ningún servidor que lo leíste.

[Lo que escribes se queda en tu Mac](/es/yours/)

### El front matter no estorba

Un bloque de front matter al principio de un archivo se muestra como una sección plegada Información del documento en la vista previa y en Vista rápida, y se omite del PDF.

### Ocho idiomas

La app está en inglés, chino tradicional, chino simplificado, japonés, alemán, francés, español y coreano.

[Una app para Mac](/es/native/)

## Diagramas, código y fórmulas

### Diagramas Mermaid

Un bloque de código marcado como `mermaid` se dibuja como un diagrama. Si el diagrama tiene un error, la vista previa muestra su código con el error debajo, y al hacer clic en el mensaje se salta a esa línea.

[Vista previa de Mermaid en Mac](/es/mermaid-preview-mac/)

### Código resaltado

Los bloques de código se resaltan en los lenguajes más comunes. Indica el lenguaje después de la valla de apertura `````.

### Fórmulas

Las fórmulas escritas en sintaxis KaTeX se dibujan en la vista previa y en Vista rápida, y llegan al PDF exportado.

[Por qué lo que produce la IA todavía necesita un lector humano](/es/reviewing-ai-output/)

## Temas, PDF e impresión

### Cuatro temas, claros y oscuros

Amanecer, Clásico, Moderno y Vívido tienen cada uno una versión clara y otra oscura, y MarsDawn sigue el aspecto de tu Mac, salvo que elijas uno en Ajustes. Elige en Visualización ▸ Tema de la vista previa o con el botón de paleta de la barra de herramientas.

[Temas de la vista previa y exportación a PDF](/es/themes/)

### Más temas

Ajustes ▸ Aspecto ▸ Obtener más temas… abre una galería de temas de vista previa adicionales. Instala uno y aparecerá en Visualización ▸ Tema de la vista previa; Eliminar lo quita. La galería solo se conecta a internet mientras está abierta.

[Galería de temas](/es/themes/gallery/) · [Crear un tema](/es/themes/new/)

### Exportar como PDF, o imprimir

Archivo ▸ Exportar como PDF… guarda un PDF paginado, y Archivo ▸ Imprimir… imprime las mismas páginas. Los diagramas Mermaid se dibujan, el código conserva su resaltado, y los saltos de página evitan separar un encabezado de su sección o partir por la mitad un bloque de código corto o un diagrama. El PDF usa siempre los colores claros del tema, aunque estuvieras leyendo en oscuro.

[Exportación a PDF](/es/pdf/)

![Un PDF exportado desde MarsDawn, abierto en su visor de PDF con miniaturas de las páginas.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

En esta captura de pantalla:

1. Diagramas Mermaid, dibujados dentro del PDF.
2. El código conserva su resaltado.

## Archivos, pestañas y Vista rápida

### Ventanas y pestañas

Cada documento se abre en su propia ventana. Elige Ventana ▸ Unir todas las ventanas para reunir las ventanas abiertas como pestañas de una sola. El guardado automático funciona mientras escribes.

[Una app para Mac](/es/native/)

### Vista rápida en el Finder

Selecciona un archivo Markdown en el Finder y presiona la barra espaciadora para leerlo renderizado, con los diagramas incluidos. Vista rápida usa el tema que elegiste en MarsDawn y sigue su ajuste de aspecto.

[Una app para Mac](/es/native/)

### Otros archivos

MarsDawn también abre archivos de texto sin formato (`.txt`, `.log`, código fuente) y PDF. El texto UTF-8 se abre listo para editar, solo como código. Los PDF se abren en un visor con miniaturas de página, zoom y búsqueda.

### Tus archivos siguen siendo tuyos

No hay cuenta, ni sincronización, ni nube. Los documentos se quedan donde los guardas, y MarsDawn no recopila ningún dato sobre ti.

[Lo que escribes se queda en tu Mac](/es/yours/)

## Para agentes y scripts

### Una herramienta de línea de comandos gratuita

La herramienta gratuita `marsdawn` se instala por separado con Homebrew. `marsdawn export` convierte un archivo Markdown en un PDF, renderizado como la vista previa de MarsDawn; no necesita la app. Elige un tema con `--theme` y un tamaño de papel, A4 o Letter. `marsdawn open` abre archivos en la app para que los revises, opcionalmente en una línea, y sí necesita la app instalada.

[Línea de comandos](/es/cli/)

### Una salida que un script puede leer

Con `--json`, los dos comandos devuelven un resultado que un agente o un script pueden analizar.

[marsdawn para agentes](/es/cli/agents/)

### Skill y servidor MCP

Un archivo de skill para agentes enseña a un agente de programación a abrir en MarsDawn lo que escribió, para que lo revises. Para clientes sin shell, un servidor MCP aparte ejecuta la misma exportación.

[Skill para agentes](/es/cli/skill/) · [Servidor MCP](/es/cli/mcp/)

### Sin IA dentro

MarsDawn no tiene un modelo de IA propio. No resume ni califica lo que escribió un agente; mantiene legible un archivo largo y cambiante para que lo leas tú.

[Lo que MarsDawn no hace](/es/limits/)

## Siri y Atajos

Busca MarsDawn en la app Atajos para encontrar tres acciones: Nuevo documento Markdown (a partir de una plantilla), Agregar nota a la bandeja de entrada y Abrir documento reciente. Las notas van a `Inbox.md` en la carpeta que elijas en MarsDawn ▸ Ajustes… ▸ Carpeta de notas.

[Una app para Mac](/es/native/)

## Después de imprimir la página

Una reunión alrededor de páginas impresas, un bolígrafo en el margen, un registro en papel archivado.

[Video de MarsDawn (en inglés), 88 segundos](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## Pruébalo en tu Mac

MarsDawn se descarga gratis. Prueba todo durante 14 días y después desbloquéalo una sola vez por 4,99 USD. Sin suscripción ni cuenta. Requiere macOS 26 o posterior.

[Descárgala y pruébala](https://apps.apple.com/app/id6812925073)

Cómo funciona la prueba: [Pruébalo gratis, paga una vez](/es/pay-once/). Lo que se deja fuera a propósito: [Lo que MarsDawn no hace](/es/limits/).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados y más en la galería. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Quick Look para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Deutsch](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
