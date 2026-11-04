# MacMD Viewer o MarsDawn.

Las dos son apps de Mac para leer Markdown como una página terminada. MacMD Viewer abre un archivo `.md` y lo muestra; es de solo lectura por diseño y nunca guarda cambios en tu archivo. MarsDawn pone un editor junto al mismo tipo de vista previa renderizada, para que escribas y revises en una sola ventana. Esta página las compara lado a lado, fila por fila, con una fuente para cada dato sobre MacMD Viewer, y dice cuándo MacMD Viewer es la mejor opción.

Comprobado con el sitio y el repositorio propios de MacMD Viewer el 15 de octubre de 2026 (versión 1.7.0, publicada el 10 de octubre de 2026). Si algo de aquí está desactualizado, avísanos en la dirección de la [página de soporte](/es/support/).

## Qué es y qué hace

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Qué es | Un visor: «de solo lectura, nunca guarda cambios en tu archivo fuente» [[S1](#s1), [S9](#s9)] | Un editor con vista previa en vivo: Markdown a la izquierda, la página renderizada a la derecha, en tres disposiciones (código, dividido, vista previa) |
| Edición | No [[S1](#s1), [S7](#s7), [S9](#s9)] | Sí. La página renderizada en sí no se puede editar; editas el código fuente que tiene al lado |
| Vista previa en vivo | Renderiza el archivo; se recarga cuando otro editor guarda el archivo [[S9](#s9)] | Se actualiza mientras escribes. Cuando otra app cambia el archivo, MarsDawn lo recarga y mantiene tu posición, siempre que no tengas ediciones propias sin guardar. |
| Mermaid | Sí: diagramas de flujo, de secuencia y de estados, diagramas de Gantt, gráficos circulares y más, sin conexión [[S1](#s1), [S3](#s3), [S7](#s7)] | Sí |
| Matemáticas | No: su README dice que «no renderiza matemáticas (LaTeX/KaTeX)» [[S7](#s7)] | Sí, KaTeX |
| Resaltado de código | Sí [[S1](#s1), [S9](#s9)] | Sí |
| Temas | 12 temas de documento [[S1](#s1), [S7](#s7)] | 4 integrados (Amanecer, Clásico, Moderno, Vívido), cada uno con paleta clara y oscura, y más en la galería de temas |
| Pestañas | Sí, opcionales y desactivadas por defecto (desde 1.6.0) [[S5](#s5), [S8](#s8)] | Sí |
| Exportación a PDF | Sí, una sola página continua, con el tema actual, sin marca de agua [[S3](#s3), [S9](#s9)] | Sí, páginas paginadas con la paleta clara del tema; los saltos de página evitan partir bloques de código cortos |
| Impresión | Sí, mediante el diálogo de impresión de macOS [[S3](#s3), [S9](#s9)] | Sí |
| Vista Rápida en el Finder | Sí, incluida; la activas en Ajustes del Sistema; usa tu tema [[S4](#s4)] | Sí, funciona con o sin la prueba; usa tu tema |
| Mermaid y matemáticas en Vista Rápida | Mermaid: sí [[S4](#s4)]. Matemáticas: no, no las renderiza [[S7](#s7)] | Sí, se dibujan las dos cosas |
| Línea de comandos | No se describe ninguna herramienta de línea de comandos independiente. Tiene un esquema de URL `markdownviewer://` y un plug-in de Claude Code con hooks que abren archivos en el visor [[S6](#s6)] | La herramienta gratuita `marsdawn`: `marsdawn export` genera un PDF sin la app, `marsdawn open` abre un archivo en una línea |
| Idiomas de la interfaz | No se indican en sus propios materiales [[S1](#s1), [S3](#s3), [S7](#s7)] | inglés, chino tradicional, chino simplificado, japonés, alemán, francés, español y coreano |
| Requisitos | macOS 14 (Sonoma) o posterior; Apple silicon e Intel [[S1](#s1), [S7](#s7)] | macOS 26 (Tahoe) o posterior |
| Otras plataformas | Solo Mac [[S1](#s1)] | Mac, y iPhone y iPad solo para leer |

## Precio y forma de compra

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Dónde se compra | Su propio sitio, Homebrew o Setapp; sin ficha en el Mac App Store [[S2](#s2), [S7](#s7)] | Solo en el Mac App Store |
| Precio | 19,99 USD una sola vez, para una Mac activa (se puede pasar a otra Mac); Family Pack por 39,99 USD para 3; 10 claves por 129 USD [[S2](#s2)] | Descarga gratuita y luego 4,99 USD una sola vez |
| Probarlo primero | Sin prueba ni versión gratuita; reembolso completo en 14 días en compra directa [[S2](#s2)] | Prueba gratuita de 14 días con todo activado |
| Reembolsos | A través de su propio soporte, en 14 días [[S2](#s2)] | A través de Apple |
| Actualizaciones | Las actualizaciones dentro de la versión principal actual son gratuitas [[S2](#s2)]; la descarga directa se actualiza sola con Sparkle [[S7](#s7)] | A través del Mac App Store |
| Cuenta necesaria | No [[S2](#s2)] | No |
| Suscripción | No [[S1](#s1), [S2](#s2)] | No |

## Qué cambia si dejas de probar o de pagar

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Después | Sin prueba; una vez comprada, sigue funcionando | Si no la desbloqueas pasados 14 días, los documentos se abren con su contenido cubierto; tus archivos no se tocan, y Vista Rápida y la exportación gratuita de `marsdawn` siguen funcionando |

## Fuentes

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## Cuál elegir

**Elige MacMD Viewer si** solo lees Markdown y quieres la garantía de que nunca se modifica tu archivo: nunca guarda cambios en él [[S1](#s1)]. También encaja mejor si tu Mac usa macOS 14 o 15, ya que MarsDawn necesita macOS 26 [[S1](#s1), [S7](#s7)]; si prefieres comprar en el sitio de un desarrollador, en Homebrew o en Setapp antes que en el Mac App Store [[S2](#s2), [S7](#s7)]; si quieres que los archivos que edita un agente se abran solos en el visor, algo que consigue con hooks para Claude Code, Cursor y Windsurf [[S6](#s6)]; o si quieres un PDF de una sola página continua en lugar de páginas paginadas [[S9](#s9)]. No tiene prueba, pero sí un reembolso de 14 días [[S2](#s2)].

**Elige MarsDawn si** el Markdown vuelve para otra pasada. El plan, el README o la especificación de un agente suele necesitar una corrección, una frase reformulada o una sección nueva, y en MarsDawn lo haces en la ventana donde ya estás leyendo. También cubre las matemáticas (KaTeX), que MacMD Viewer dice que no renderiza [[S7](#s7)]; viene en ocho idiomas de interfaz; tiene una línea de comandos `marsdawn` gratuita que exporta un PDF sin la app; y su precio es de 4,99 USD tras una prueba de 14 días en la que todo funciona.

**Cualquiera sirve si** lees Markdown en una Mac reciente, quieres diagramas Mermaid bien dibujados y quieres Vista Rápida en el Finder. Las dos lo hacen.

**Y puedes usar las dos.** No son excluyentes: nada te impide tener un visor de solo lectura para lo que solo lees y un editor para lo que escribes.

## Preguntas

### ¿MacMD Viewer edita archivos?

No. Es de solo lectura y, en sus propias palabras, nunca guarda cambios en tu archivo fuente [[S1](#s1), [S9](#s9)]. Puede abrir el archivo en tu editor de texto (menú Archivo, ⇧⌘E, desde 1.7.0), lo que entrega el archivo a otra app [[S5](#s5)].

### ¿MacMD Viewer está en el Mac App Store?

Sus propias páginas citan su sitio, Homebrew y Setapp, y no mencionan el Mac App Store [[S2](#s2), [S7](#s7)]. MarsDawn está solo en el Mac App Store.

### ¿Puede MarsDawn abrir los mismos archivos?

Sí. Abre archivos `.md`, y también archivos de texto plano y PDF: el texto se abre listo para editar como UTF-8, y los PDF se abren en un visor. En el Mac también abre JSON y YAML como documentos editables, con vista previa en árbol.

### ¿Y si tengo macOS 14 o 15?

MacMD Viewer funciona en macOS 14 o posterior [[S1](#s1)]. MarsDawn necesita macOS 26 o posterior, y la herramienta gratuita de línea de comandos `marsdawn` aún puede exportar un PDF.

### ¿Por qué una cuesta 19,99 USD y la otra 4,99 USD?

Se diferencian en lo que obtienes y en cómo pagas. MacMD Viewer es una compra única con reembolso de 14 días y sin prueba [[S2](#s2)]. MarsDawn es una descarga gratuita con una prueba de 14 días y luego un desbloqueo único. Ninguna de las dos es una suscripción.

## Pruébalo hoy, gratis

MarsDawn está en el Mac App Store. La herramienta de línea de comandos gratuita `marsdawn` también renderiza cualquier archivo Markdown como PDF, con diagramas Mermaid y código resaltado, y no necesita nada más instalado:

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## Siguiente

- La guía completa: [Markdown a PDF](/es/markdown-to-pdf/).
- Lo que MarsDawn no hace: [la lista](/es/limits/).
- Todas las opciones de la herramienta de línea de comandos: [Línea de comandos](/es/cli/).
- Comparado con leer Markdown en VS Code, un navegador o Claude Desktop: [cómo se comparan](/es/vs/markdown-preview-tools/).
- Todo lo que hace MarsDawn, en una sola página: [Funciones](/es/features/).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Revisa el Markdown, JSON y YAML de tu agente en tu Mac: vista previa en vivo, Mermaid, KaTeX, Vista Rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor nativo para Mac de Markdown, JSON y YAML: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista Rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin edición en iPhone o iPad, sin plugins, sin cuentas. Temas, pero sin CSS personalizado. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista Rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista Rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista Rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista Rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
