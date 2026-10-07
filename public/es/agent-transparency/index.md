# Anthropic dice que los agentes deben ser transparentes. ¿Quién lee lo que muestran?

En diciembre de 2024, Anthropic publicó «Building Effective Agents», una guía para quienes construyen agentes de IA. Su resumen enumera tres principios, y uno de ellos es la transparencia. Este artículo trata del otro extremo de ese principio: cuando un agente muestra sus pasos, alguien tiene que leerlos.

**La transparencia la pone el agente. La lectura la pones tú. Anthropic les pide a quienes construyen agentes que muestren los pasos de planificación; para la mayoría de las personas que manejan un agente de programación, esos pasos llegan como un archivo Markdown que alguien tiene que leer en el momento justo.**

## Qué dice la guía

Erik S. y Barry Zhang resumen sus consejos así:

> «Al implementar agentes, intentamos seguir tres principios básicos: mantener la simplicidad en el diseño del agente. Priorizar la transparencia mostrando explícitamente los pasos de planificación del agente. Diseñar con cuidado la interfaz entre el agente y la computadora (ACI) mediante una documentación y unas pruebas exhaustivas de las herramientas».

Son principios de diseño para quienes construyen agentes, no instrucciones para la persona que usa uno. El principio pide que se muestren los pasos. No dice quién los lee.

El mismo artículo describe lo que hace un agente una vez que tiene una tarea: «Una vez que la tarea está clara, los agentes planifican y operan de forma independiente, y posiblemente vuelven al humano para pedir más información o su criterio». Y: «Luego, los agentes pueden hacer una pausa para recibir comentarios humanos en puntos de control o cuando encuentran obstáculos». Fíjate en las palabras *posiblemente* y *pueden*. Los puntos de control se describen como algo que un agente puede tener, no algo que deba tener.

## La mayor parte de la verificación no la haces tú

Es fácil exagerar esto, así que esto es lo que la guía pone primero en realidad. El agente se verifica a sí mismo contra el mundo: «Durante la ejecución, es crucial que los agentes obtengan en cada paso una “verdad de referencia” del entorno (como los resultados de llamadas a herramientas o de la ejecución de código) para evaluar su avance». En esa frase, la verdad de referencia son resultados de pruebas y salidas de herramientas. No una persona.

La guía también es directa sobre el riesgo: «La naturaleza autónoma de los agentes implica costos más altos y la posibilidad de errores que se acumulan». Su respuesta son pruebas exhaustivas en entornos aislados, con salvaguardas. No dice «lee con más cuidado».

Una persona sí aparece más adelante, en el apéndice sobre agentes de programación: «Sin embargo, aunque las pruebas automatizadas ayudan a verificar la funcionalidad, la revisión humana sigue siendo crucial para asegurar que las soluciones se ajusten a los requisitos más amplios del sistema». Esa frase habla de código. Pero el hueco que señala es conocido con cualquier agente: una prueba puede decirte que algo funciona, no que es lo que querías.

## Dónde terminan los pasos

**De aquí en adelante, esta es nuestra lectura, no la de Anthropic.**

Si usas un agente de programación todos los días, sus pasos de planificación no suelen aparecer en un panel. Aparecen como archivos: `plan.md`, una lista de tareas con casillas, un archivo de avance que el agente no deja de reescribir, un resumen al final. La transparencia, desde tu lado, significa más cosas que leer.

Mostrar los pasos es la mitad que le toca al agente. La otra mitad es una persona que los lee cuando importa: antes de que se ejecute la migración, antes de fusionar la rama, antes de aceptar el «listo». Un agente que lo expone todo en un archivo de 600 líneas que nadie abre es transparente en el papel y no tiene supervisión en la práctica.

Harrison Chase planteó algo parecido en 2024, al escribir sobre cómo deberían funcionar los frameworks de agentes y no sobre documentos: «Vas a querer poder observar lo que pasa dentro, ya que es posible que los pasos exactos no se conozcan de antemano». Hablaba de herramientas para quienes construyen agentes. Si eres tú quien maneja el agente, el archivo simple que no deja de escribir suele ser la parte que puedes observar.

Ninguno de estos autores menciona MarsDawn, y ninguno lo recomienda, ni tampoco ninguna otra herramienta de Markdown.

## Por qué esa lectura cuesta más de lo que parece

El archivo es largo, y lo que importa rara vez está arriba. El diagrama que explica el cambio es código Mermaid, no una imagen (cómo verlo dibujado se explica en [Cómo ver un archivo Markdown en Mac](/es/view-markdown-on-mac/)). Puede que el agente reescriba el archivo cuando vas por la mitad. A menudo hay más de un archivo, a veces en distintas ramas o worktrees. Y cuando detectas un problema, «la parte del caché se ve rara» deja al agente adivinando. La versión larga está en [Leer lo que te devuelve tu agente](/es/reading-agent-output/).

## Dónde encaja MarsDawn y dónde no

MarsDawn es una app para Mac hecha para esa lectura. No hace más transparente a un agente y no tiene ningún modelo de IA dentro: no va a resumir el plan ni a decirte si está bien. Lo que sí hace:

- **Archivos largos:** Visualización ▸ Mostrar barra lateral (⌃⌘S) abre la pestaña Esquema, que lista los títulos. Haz clic en uno para saltar ahí.
- **Diagramas y fórmulas:** el código fuente y la página renderizada quedan lado a lado (⌘2) y se desplazan juntos, con Mermaid y KaTeX dibujados. Si un diagrama tiene un error, la vista previa muestra su código con el error debajo.
- **Reescrito mientras lees:** cuando el agente reescribe el archivo, MarsDawn lo vuelve a cargar y conserva tu posición, siempre que no tengas cambios propios sin guardar.
- **Varios archivos:** abre la carpeta del agente con Archivo ▸ Abrir carpeta… (⇧⌘O). Los archivos nuevos aparecen en la pestaña Archivos en aproximadamente un segundo y, en un checkout de git, el encabezado indica la rama o el worktree.
- **Señalar una línea:** Edición ▸ Copiar referencia (⌥⌘C) copia tu posición como `docs/plan.md:42`, y Copiar para IA (⌃⌥⌘C) agrega el texto seleccionado debajo, listo para pegar en el chat con el agente.

La lectura la sigues haciendo tú. MarsDawn mantiene legible un archivo largo que cambia mientras la haces.

## Pruébalo

MarsDawn está en el [Mac App Store](https://apps.apple.com/app/id6812925073). También existe la herramienta de línea de comandos gratuita `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Exporta Markdown a PDF sin la app.

[Línea de comandos](/es/cli/) · Antes de comprar: [Lo que MarsDawn no hace](/es/limits/)

## Siguiente

- Por qué cuesta leer lo que entrega un agente, con una lista de verificación: [Leer lo que te devuelve tu agente](/es/reading-agent-output/).
- La lista, paso a paso con un ejemplo: [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/).
- Qué documentos te entregan los distintos tipos de agentes: [Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno](/es/agent-design-patterns/).
- El argumento breve para leer lo que genera la IA: [Por qué lo que genera la IA todavía necesita un lector humano](/es/reviewing-ai-output/).

## Fuentes

- Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (citado de la versión publicada el 26/09/2026; el artículo ahora indica que buena parte de las herramientas que describe cambió desde diciembre de 2024).
- Harrison Chase, «What is an agent?», LangChain, 28 de junio de 2024, copia archivada: [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (la dirección original ahora muestra otro artículo, de 2026).

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
- [Temas de la vista previa y exportación a PDF](https://marsdawn.southern-light.dev/es/themes/index.md): Cuatro temas de vista previa, cada uno con una paleta clara y una oscura, y una sola exportación a PDF e impresión que respeta el que estés usando. Crea tu propio tema en el navegador y explora la galería de la comunidad.
- [Crear un tema](https://marsdawn.southern-light.dev/es/themes/new/index.md): Elige colores y unas pocas opciones de estilo, míralos aplicados en vivo a un documento de ejemplo y envía tu tema como un issue de GitHub. Sin instalación, sin git.
- [Galería de temas](https://marsdawn.southern-light.dev/es/themes/gallery/index.md): Explora temas de vista previa que la comunidad envió para MarsDawn, fíltralos por escenario y denuncia un problema. Crea el tuyo en el navegador, sin instalación y sin git.
- [Compartir los PDF exportados](https://marsdawn.southern-light.dev/es/sharing-exported-pdfs/index.md): Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.
- [Por qué lo que produce la IA todavía necesita un lector humano](https://marsdawn.southern-light.dev/es/reviewing-ai-output/index.md): El Markdown escrito por una IA tiene que entenderlo una persona, no creerlo a simple vista. MarsDawn pone la página renderizada junto al código fuente y dibuja diagramas Mermaid y fórmulas KaTeX, para que la estructura se lea de un vistazo.
- [Leer lo que te devuelve tu agente](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
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
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Français](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
