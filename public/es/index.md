Herramientas de frontera para quienes construyen

# Toma el mapa. Lee el amanecer.

Markdown para las personas que dirigen el trabajo de los agentes.

MarsDawn es una app nativa de macOS para leer y revisar Markdown, con vista previa dividida en vivo, diagramas Mermaid, fórmulas KaTeX, Vista Rápida y exportación a PDF; pruébala gratis 14 días y desbloquéala por 4,99 USD una sola vez. En el Mac también abre JSON y YAML con vista previa en árbol.

La página muestra una ventana de MarsDawn interactiva que presenta un fragmento de la guía de bienvenida de la app. En su menú de paleta eliges un aspecto (Sistema, Claro, Oscuro) y, para claro y para oscuro, uno de cuatro temas de vista previa (Amanecer, Clásico, Moderno, Vívido). Su barra de herramientas ofrece tres disposiciones (Código, Dividido, Vista previa).

## Lee lo que escribió tu agente, aunque no estés en tu escritorio

1. En tu Mac, haz que tu agente guarde sus archivos en una carpeta de iCloud Drive.
2. En tu iPhone o iPad, abre MarsDawn y elige el archivo.
3. Para editarlo o exportarlo a PDF, vuelve a tu Mac.

En iPhone y iPad, MarsDawn solo sirve para leer y solo abre archivos Markdown y de texto plano.

[![Descargar en el App Store](/assets/badges/app-store-es.svg)](https://apps.apple.com/app/id6812925073)

[Más sobre MarsDawn en iPhone y iPad](/es/features/#iphone-ipad)

## Lee lo que escribió tu agente.

1. **El agente escribe.** Tu agente de programación o tu asistente de escritura redacta el Markdown: un README, una especificación, unas notas.
2. **Tú lo revisas en MarsDawn.** Abre el archivo y léelo ya renderizado, con [diagramas Mermaid](/es/mermaid-preview-mac/) y código resaltado, junto al código fuente.
3. **El agente corrige.** Pide cambios. Abre el archivo corregido y léelo de la misma manera.

[Cómo revisar lo que te devuelve tu agente](/es/reading-agent-output/) · [Cómo abrir archivos .md en Mac](/es/view-markdown-on-mac/)

## Revisa el plan de tu agente antes de que se ejecute.

Encuentra el paso fuera de orden, señala su línea y devuélveselo.

1. Mira qué cambió: cuando el agente guarda el plan, la ventana abierta se actualiza desde el disco en un solo paso que puedes deshacer.
2. Salta a la línea: marsdawn open plan-checkout-v2.md:10 lleva la ventana a la línea 10 y hace parpadear el bloque correspondiente.
3. Devuélvelo: «Copiar referencia» (⌥⌘C) copia plan-checkout-v2.md:10; pégalo con tu comentario en el chat del agente.

## Hazlo ahora

La herramienta de línea de comandos gratuita `marsdawn` ya está lista. Instálala con Homebrew:

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` convierte un archivo Markdown en un PDF, renderizado como la vista previa de MarsDawn. No necesita la app.
- `marsdawn open` abre archivos en la app MarsDawn para que los revises.
- `--json` les da a los scripts y a los agentes resultados que pueden analizar.

[Línea de comandos](/es/cli/) · [marsdawn para agentes](/es/cli/agents/) · [Skill para agentes](/es/cli/skill/) · [Servidor MCP](/es/cli/mcp/)

## Qué esperar de MarsDawn

- [Una app para Mac](/es/native/): Ventanas y pestañas nativas, guardado automático, [Vista Rápida](/es/quicklook/).
- [Lo que escribes se queda en tu Mac](/es/yours/): Sin cuenta, sin sincronización, sin nube.
- [Pruébalo gratis, paga una vez](/es/pay-once/): Gratis durante 14 días; después, 4,99 USD una sola vez. Sin suscripción.
- [Funciones](/es/features/): Todo lo que hace MarsDawn, en una sola página.
- [Temas](/es/themes/): Cuatro integrados, más en la galería.

Lo que conviene saber antes de comprar. [Lo que MarsDawn no hace](/es/limits/)

## Cómo encajan las piezas

Lo que hace cada parte hoy, con MarsDawn 1.1.1, marsdawn 0.6.4 y marsdawn-mcp v0.2.4.

| Función | En la app | CLI | MCP / skill | Estado |
|---|---|---|---|---|
| Abrir en una línea | Va a la línea y el bloque de la vista previa parpadea | `marsdawn open notes.md:120` (`--background` no roba el foco) | `open_in_marsdawn`; la skill abre una vez | Disponible |
| Exportar a PDF | Archivo ▸ Exportar como PDF… (⌥⌘E) | `marsdawn export`, sin la app | `export_markdown_to_pdf`; skill | Disponible |
| Resultado JSON | — | `--json` en open y export | MCP devuelve el mismo JSON | Disponible |
| Skill para agentes | — | `marsdawn skill --install` | Enseña a abrir una vez y a exportar | Disponible |
| Servidor MCP | — | Funciona por debajo | marsdawn-mcp: dos herramientas, solo carpetas permitidas | Disponible |
| Copiar para IA, Copiar referencia | Edición ▸ Copiar para IA (⌃⌥⌘C), Copiar referencia (⌥⌘C) | — | — (pégalo en cualquier agente) | Disponible |
| Recarga al guardar | Toma el cambio guardado, se deshace en un paso | — | Skill: no volver a abrir | Disponible |
| Hook de Claude Code | — | Usa `open --background` | Script del hook en /cli/agents/ | Documentado, opcional |

Disponible: en la versión indicada arriba. Documentado, opcional: instrucciones de este sitio que añades tú; no viene en la herramienta. Previsto: aún no existe, sin fecha. Previsto: una opción de carpeta en la herramienta MCP `open_in_marsdawn`. Otras opciones, como `--folder`, están en [Línea de comandos](/es/cli/).

## Si creas apps para Mac con un agente de código

Para desarrolladores independientes de Mac: cómo tu agente abre hoy en MarsDawn lo que escribió.

| Herramienta | Cómo se combinan | Configuración |
|---|---|---|
| Claude Code | La skill hace que abra una vez lo que escribió, en la línea: `marsdawn open plan.md:42`. Un hook opcional abre cada .md que escribe, en segundo plano | `marsdawn skill --install`; el script del hook en /cli/agents/ |
| Codex, Cursor, Xcode | Aún no hay guía de configuración. Cualquier cosa que ejecute un comando de shell puede llamar a `marsdawn open file:line --json`; un agente que carga archivos de instrucciones puede usar SKILL.md (`--dir`), y un cliente solo MCP, marsdawn-mcp | `brew install redtear1115/tap/marsdawn` |

El hook y los comandos: [marsdawn para agentes](/es/cli/agents/) · [Skill para agentes](/es/cli/skill/) · [Lo que MarsDawn no hace](/es/limits/)

¿Dudas entre MarsDawn, la vista previa de VS Code, Obsidian, QLMarkdown y LynxOffice? La comparación recoge lo que indica cada fabricante, lo que le falta a MarsDawn y cuándo no lo necesitas. [Ver la comparación](/es/vs/)

## Tus documentos se quedan en tu Mac

En tu Mac. Leer, editar, renderizar, [exportar a PDF](/es/privacy/#exporting-and-printing) y [la herramienta de línea de comandos marsdawn](/es/privacy/#the-marsdawn-command-line-tool) funcionan aquí, incluso sin conexión; la app nunca sube tus documentos.

Más información: [Política de privacidad](/es/privacy/#what-stays-on-your-mac)

Sin red por omisión. Las imágenes web solo se cargan si haces clic en «Cargar imágenes» o activas «Cargar imágenes remotas automáticamente» en Ajustes; un documento HTML se abre de forma estática, sin ejecutar su código.

Más información: [Política de privacidad](/es/privacy/#when-marsdawn-uses-the-internet)

Solo sale lo que tú eliges. «Copiar para IA» deja el texto en el portapapeles y lo pegas tú; una descarga de tema, un documento que ejecutas con «Visualización › Ejecutar este documento» y el archivo que dejas leer a tu agente solo salen si tú lo decides.

Más información: [Política de privacidad](/es/privacy/#when-marsdawn-uses-the-internet)

## Preguntas y respuestas

### ¿Qué es MarsDawn?

MarsDawn es una app nativa para Mac para leer y revisar el Markdown que escribió tu agente, con el código fuente junto a una vista previa en vivo. Dibuja Mermaid y KaTeX, muestra archivos .md en Vista Rápida y exporta a PDF; también puedes editar el código fuente. En el Mac también abre JSON y YAML con vista previa en árbol.

### ¿MarsDawn es una suscripción?

No. MarsDawn se descarga gratis y incluye 14 días de prueba de todas las funciones. Después, una sola compra dentro de la app por 4,99 USD lo desbloquea para siempre. Nada se renueva y no hay cuenta.

### ¿MarsDawn funciona en iPhone o iPad?

Sí, para leer. En iPhone y iPad, MarsDawn abre archivos Markdown y de texto plano y muestra con formato diagramas de Mermaid, fórmulas, código y tablas, con esquema y temas. No edita ni exporta PDF. Necesita iOS 26 o iPadOS 26 o posterior. Con la misma cuenta de Apple, una prueba y un desbloqueo cubren MarsDawn en Mac, iPhone y iPad.

Más información: [Hoja de ruta](/es/roadmap/)

### ¿Puede Claude Code abrir archivos en MarsDawn?

Sí. La herramienta de línea de comandos gratuita marsdawn tiene un comando open que abre un archivo Markdown en MarsDawn, así que Claude Code, o cualquier agente que pueda ejecutar un comando de shell, puede llamarlo. Un hook opcional de Claude Code puede abrir cada archivo Markdown que Claude escribe o edita.

### ¿MarsDawn sube mis documentos?

No. La app nunca sube tus documentos, no recopila datos sobre ti y no tiene cuentas; tus documentos y ajustes se quedan en tu Mac. Si un documento hace referencia a la web y cargas ese contenido, tu Mac lo obtiene directamente de los servidores que lo alojan, y el desarrollador de MarsDawn no recibe nada de ello.

Más información: [Política de privacidad](/es/privacy/#what-stays-on-your-mac)

### Con MCP o la skill, ¿quién puede ver mis archivos?

MarsDawn no envía nada por sí mismo. La skill es un archivo de texto con instrucciones, la herramienta marsdawn y el servidor MCP se ejecutan en tu Mac, y el servidor MCP solo trabaja en las carpetas que permites. Quien lee tus archivos es tu agente; lo que él y su proveedor de modelos hagan con ellos depende de la política de ese agente, que MarsDawn ni controla ni describe.

Más información: [MCP](/es/cli/mcp/)

### ¿Es seguro abrir un HTML que me enviaron?

Por omisión se abre de forma estática: su código no se ejecuta y no se carga nada desde la web. Si eliges «Visualización › Ejecutar este documento», ese documento se ejecuta y puede enviar datos por la red y leer imágenes, hojas de estilo, fuentes y archivos multimedia de su carpeta. Esa elección nunca se recuerda, así que la próxima vez vuelve a abrirse estático.

Más información: [Política de privacidad](/es/privacy/#when-marsdawn-uses-the-internet)

### ¿La cookie de analítica del sitio tiene que ver con la app?

No. La app y este sitio son cosas distintas: la app no recopila nada y una visita solo puede registrarse en marsdawn.southern-light.dev. En el sitio, Google Analytics empieza denegado y solo pone cookies después de que elijas «Aceptar» en el banner; puedes cambiarlo en «Ajustes de cookies», en el pie de página. Las solicitudes de la app de archivos de tema en /themes/ no se registran.

Más información: [Política de privacidad](/es/privacy/#the-website)

### ¿Por qué usar MarsDawn y no otra app?

Puede que no lo necesites. Si sobre todo escribes tus propias notas, una app de notas como Obsidian te irá mejor. Si pasas el día en VS Code, su vista previa integrada es gratis. Si solo quieres echar un vistazo a los archivos en el Finder, basta con una extensión gratuita de Vista Rápida. Si tus PDF necesitan números de página, MarsDawn no los añade. MarsDawn sirve para leer y revisar el Markdown que escribió un agente: el código fuente junto a una vista previa en vivo, un cambio de tu agente que deshaces en un solo paso y un archivo abierto en la línea exacta. Si no te sirve, escríbenos y cuéntanos por qué.

Más información: [MarsDawn frente a otras herramientas](/es/vs/) · [El mejor visor de Markdown para Mac](/es/best-markdown-viewer-mac/)

### ¿MarsDawn seguirá teniendo mantenimiento?

Sí. Cada actualización desde que MarsDawn llegó a la Mac App Store está en el historial de cambios, y desde el 28 de octubre de 2026 MarsDawn también está en iPhone y iPad, para leer. El núcleo de renderizado de MarsDawn y la herramienta de línea de comandos gratuita marsdawn ya son de código abierto con la licencia Apache-2.0, en mars-dawn-kit. Y si el desarrollador de MarsDawn deja algún día de mantener la app, el código fuente de la propia app se publicará con una licencia de código abierto, para que otros puedan continuarla.

Más información: [Historial de cambios](/es/changelog/) · [Hoja de ruta](/es/roadmap/) · [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)

## La app, tal como es

### [Una app para Mac](/es/native/)

![MarsDawn en vista dividida: el código Markdown a la izquierda y la página renderizada a la derecha.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

En esta captura de pantalla:

1. Una ventana nativa de Mac.
2. El editor de texto de la Mac, con resaltado de Markdown.
3. ⌘1 código, ⌘2 dividido, ⌘3 vista previa.
4. La página se actualiza mientras escribes.

### [Exportación a PDF](/es/pdf/)

![Un PDF exportado desde MarsDawn, abierto en su visor de PDF con miniaturas de las páginas.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

En esta captura de pantalla:

1. Diagramas Mermaid, dibujados dentro del PDF.
2. El código conserva su resaltado.

## Más

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
- [English](https://marsdawn.southern-light.dev/index.md): Read and review your agent's Markdown, JSON and YAML natively on Mac: live preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 檢查 agent 寫的 Markdown、JSON、YAML：Mac 原生 app，即時預覽、Mermaid、KaTeX、快速查看、PDF。免費試用，之後一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 检查代理写的 Markdown、JSON、YAML：Mac 原生 app，实时预览、Mermaid、KaTeX、快速查看、PDF。免费试用，之后一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown・JSON・YAML を確かめる Mac ネイティブアプリ。ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF。無料で試せて、一度だけ USD 4.99。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): Lies Markdown, JSON und YAML deines Agenten nativ auf dem Mac: Live-Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Relisez le Markdown, JSON et YAML de votre agent sur Mac : aperçu en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown, JSON, YAML을 검토하는 Mac 네이티브 앱. 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료 체험 후 한 번만 USD 4.99.
