# Pasar de HackMD a tu Mac

Tus notas ya son Markdown, así que no hay nada que convertir. Elige una vía según lo que vayas a mover. Las imágenes necesitan un paso aparte, así que lee esa sección antes de eliminar nada en HackMD.

Lo comprobamos con una cuenta gratuita de HackMD en noviembre de 2026. HackMD puede cambiar, y no probamos los planes de pago ni los espacios de equipo.

| Quieres | Tu vía |
|---|---|
| Mover todas tus notas | Descargar todas las notas |
| Mover notas que ya están en GitHub | Clonar el repositorio |
| Mover una o dos notas | Descargar una nota |

## Descargar todas las notas

Los ajustes de notas de HackMD tienen Download all notes, para espacios personales y de equipo. Obtienes un .zip con un archivo .md por nota, con el título de la nota como nombre.

- Las carpetas no se conservan. Todas las notas quedan en el nivel superior.
- Las imágenes no se incluyen. Los archivos .md siguen apuntando a ellas por URL.
- La opción de incluir el título y las etiquetas está activada por defecto y añade un bloque de front matter a cada nota. Desactívala para obtener cada nota tal como se escribió.

Descomprime el archivo y elige Archivo ▸ Abrir carpeta… en MarsDawn para abrir esa carpeta.

## Clonar el repositorio

La sincronización con GitHub de HackMD vincula una nota con un archivo, así que una nota que ya enviaste está en el repositorio. Clónalo y abre la carpeta con Archivo ▸ Abrir carpeta…. La barra lateral muestra el repositorio y su rama.

Si tus notas aún no están en GitHub, no hace falta empezar ahora para esta mudanza. Cada nota se vincula por separado, y el plan gratuito permite 20 envíos al mes. En una cuenta personal gratuita no encontramos forma de enviar todo un espacio de trabajo de una vez.

Después de la mudanza, trata el repositorio como el original. Un envío desde HackMD reemplaza lo que hay en GitHub, aunque GitHub tenga contenido más reciente, y no te avisa.

## Descargar una nota

El menú de la nota la descarga como .md o .html. Elige .md y abre el archivo en MarsDawn.

## Imágenes

Las imágenes que subiste a HackMD están en `https://hackmd.io/_uploads/...`. Quién puede verlas depende del permiso de la nota.

| Tu nota es | Qué pasa en tu Mac | Qué hacer |
|---|---|---|
| Pública | La imagen se carga desde HackMD | Haz clic en Cargar imágenes en la vista previa, o activa Ajustes ▸ Imágenes ▸ Cargar imágenes remotas automáticamente |
| Privada | La imagen devuelve un error, porque MarsDawn no ha iniciado sesión en HackMD | Guarda la imagen desde un navegador con sesión iniciada, ponla junto al archivo .md y cambia la ruta. O haz pública la nota, si todo el mundo puede leerla |

- **Las notas antiguas** pueden usar direcciones `i.imgur.com`.
- **Eliminar una nota elimina sus imágenes.** Sus direcciones dejan de funcionar, así que mueve antes las imágenes.

Si MarsDawn no puede leer una imagen que está junto a tu archivo, usa el botón de la vista previa para darle acceso a la carpeta.

## Cómo se verán tus notas

La mayor parte de la sintaxis de HackMD se lee igual: `==resaltado==`, `^superíndice^`, `~subíndice~`, `[TOC]`, tamaños de imagen como `=300x200`, Mermaid y KaTeX. `{%youtube %}` se muestra como un enlace. Para conservar cada salto de línea como en HackMD, activa Ajustes ▸ Aspecto ▸ Mantener saltos de línea simples.

Los bloques `:::` también funcionan. `:::info`, `:::success`, `:::warning` y `:::danger` se muestran como bloques con una barra de color y un título (Nota, Consejo, Advertencia o Peligro), o con tu propio título si lo escribes después del nombre. `:::spoiler` se muestra como un bloque plegable que se abre al hacer clic. Un bloque `:::` con otro nombre, o sin su `:::` de cierre, se muestra tal como lo escribiste.

Algunas cosas cambian:

- `++insertado++` y los códigos de emoji como `:sparkles:` se muestran tal como los escribiste.
- `{%hackmd id %}` no se expande.
- Los iconos `<i class="fa ...">` no aparecen.

## Para scripts: hackmd-cli

`hackmd-cli` no tiene un comando que exporte todo de una vez. Exporta una nota y la imprime, así que primero listas tus notas y luego las recorres en un bucle. Necesitas Node.js, `jq` y un token de API creado en los ajustes de HackMD. Si no necesitas un script, Download all notes es más sencillo.

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<tu token>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **Las carpetas no se trasladan.** La lista de notas no indica en qué carpeta está cada una, así que todos los archivos quedan en el mismo lugar.
- **Las imágenes siguen siendo enlaces de `hackmd.io`.** Trátalas como en la sección Imágenes de arriba.
- **Los nombres de archivo son los ID de las notas,** no sus títulos.
- **El plan gratuito permite 400 llamadas a la API cada 30 días.** La lista usa una llamada, y cada nota una más.

Solo lo probamos en una cuenta con pocas notas, así que no sabemos qué pasa con una lista muy larga. Elimina el token en los ajustes de HackMD cuando termines.

## Escribir en equipo

MarsDawn no tiene edición compartida. Si necesitas escribir con otras personas en directo, sigue usando HackMD. Si tu equipo guarda sus documentos en git, cada persona puede abrir el mismo repositorio en su propio MarsDawn y terminar el documento entre todos. Consulta Revisar documentos en equipo con git.

## Preguntas

### ¿Puedo descargar todas mis notas de HackMD de una vez?

Sí. Download all notes te da un .zip de archivos .md. No conserva las carpetas ni incluye las imágenes.

### ¿Por qué faltan mis imágenes en MarsDawn?

MarsDawn retiene las imágenes de la web hasta que haces clic en Cargar imágenes. Si la nota es privada, la imagen no puede cargarse, así que guárdala junto a tu archivo.

### ¿Tengo que dejar HackMD?

No. Para escribir en equipo, HackMD sigue siendo la mejor opción. MarsDawn sirve para leer y revisar en tu Mac.

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Revisa el Markdown, JSON y YAML de tu agente en tu Mac: vista previa en vivo, Mermaid, KaTeX, Vista Rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor nativo para Mac de Markdown, JSON y YAML: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Imprimir y PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Previsualiza tu Markdown y luego imprímelo o guárdalo como PDF en tu Mac, con la disposición Documento, Guía o Folleto, con diagramas y código resaltado.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista Rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin edición en iPhone o iPad, sin plugins, sin cuentas. Temas, pero sin CSS personalizado. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista Rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista Rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista Rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista Rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [Copiar para IA](https://marsdawn.southern-light.dev/es/copy-for-ai/index.md): Copia el texto seleccionado con su ruta de archivo y números de línea, y pégalo en Claude Code o en cualquier agente. En tu Mac, sin IDE ni plugins.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026, salvo la celda de PDF de MarsDawn, actualizada el 7 de noviembre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [El mejor visor de Markdown para Mac (2026)](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista Rápida y nativo o Electron, y para quién es cada uno.
- [Línea de comandos](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [marsdawn para agentes](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [Skill para agentes](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [Servidor MCP](https://marsdawn.southern-light.dev/es/cli/mcp/index.md): marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.
- [Revisión que ahorra tokens](https://marsdawn.southern-light.dev/es/token-efficient-review/index.md): Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.
- [Ver Markdown en otras herramientas frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/markdown-preview-tools/index.md): Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.
- [Temas](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa integrados, en claro y oscuro, y una galería revisada que abres desde Ajustes en MarsDawn para Mac. Vista Rápida usa tu tema.
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
- [English](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/from-hackmd/index.md): Lade deine HackMD-Notizen als .md herunter und lies sie in MarsDawn auf dem Mac. Alle Notizen herunterladen, ein GitHub-Repository nutzen und Bilder retten.
- [Français](https://marsdawn.southern-light.dev/fr/from-hackmd/index.md): Téléchargez vos notes HackMD en .md et lisez-les dans MarsDawn sur votre Mac. Comment tout télécharger, partir d’un dépôt GitHub et garder vos images.
- [한국어](https://marsdawn.southern-light.dev/ko/from-hackmd/index.md): HackMD 노트를 .md로 내려받아 Mac의 MarsDawn에서 읽는 방법입니다. 모든 노트 다운로드, GitHub 저장소에서 옮기기, 이미지 처리 방법을 정리했습니다.
