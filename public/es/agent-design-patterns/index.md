# Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno

En marzo de 2024, Andrew Ng describió en su boletín, The Batch, cuatro patrones de diseño para agentes de IA: reflexión, uso de herramientas, planificación y colaboración multiagente. Normalmente se explican desde el lado de quien construye agentes, como formas de obtener mejores resultados de un modelo. Este artículo mira desde el otro lado. Si usas un agente basado en uno de estos patrones, ¿qué llega a tu carpeta y qué deberías leer primero?

**Los cuatro patrones son de Andrew Ng. Los documentos que suele entregarte cada uno, y qué revisar en ellos, son deducción nuestra. Él no escribe sobre ninguna de las dos cosas, y en esta serie no defiende la revisión humana.**

## Los cuatro patrones, en breve

Ng los describe en «Agentic Design Patterns Part 1». En resumen: con la **reflexión**, el modelo revisa su propio trabajo y lo mejora. Con el **uso de herramientas**, puede llamar a herramientas como la búsqueda web o la ejecución de código. Con la **planificación**, elabora un plan de varios pasos y lo ejecuta. Con la **colaboración multiagente**, varios agentes se reparten el trabajo y lo discuten.

En la parte 1 muestra la mejora en un benchmark de programación, HumanEval, con resultados que su equipo reunió de varios grupos de investigación: «GPT-3.5 (zero-shot) acertaba el 48,1 %. GPT-4 (zero-shot) lo hace mejor, con un 67,0 %. Sin embargo, la mejora de GPT-3.5 a GPT-4 queda eclipsada al incorporar un flujo de trabajo agéntico iterativo. De hecho, dentro de un bucle de agente, GPT-3.5 alcanza hasta un 95,1 %». Estas cifras corresponden a un solo benchmark de programación, y 95,1 % es el mejor caso («hasta»). Muestran que los flujos de trabajo con agentes pueden mejorar el resultado. No dicen nada sobre quién lo comprueba.

**A partir de aquí, los documentos y las comprobaciones son nuestra lectura, no la de Ng.** Además, los agentes reales mezclan patrones. Un agente de programación puede planificar, ejecutar herramientas y revisar su propio trabajo en una misma sesión, así que a menudo recibirás los cuatro tipos de archivo.

## 1. Reflexión: un borrador que ya se revisó a sí mismo

El artículo de Ng sobre la reflexión la plantea como automatizar los comentarios que, de otro modo, daría una persona: «¿Y si automatizamos el paso de los comentarios críticos, de modo que el modelo critique automáticamente su propia salida y mejore su respuesta?».

**Lo que suele entregarte:** un documento revisado, a veces con una sección de autoevaluación o líneas como «casos límite revisados de nuevo».

**Qué revisar:** el resultado frente a *tu* pedido, no frente a la autocrítica del agente. La autoevaluación puede equivocarse a su manera. Chip Huyen: «Un modo interesante de fallo de planificación se debe a errores en la reflexión. El agente está convencido de haber completado una tarea cuando no es así». Lilian Weng, en su blog Lil’Log en junio de 2023, entonces en OpenAI, sobre los modelos de esa época: «La falta de conocimiento experto puede impedir que los LLM conozcan sus defectos y, por lo tanto, que juzguen bien si los resultados de una tarea son correctos». (En el estudio que describía, la evaluación de resultados hecha por un LLM y la de expertos humanos no coincidían). Si dice «verificado», comprueba una cosa tú mismo.

## 2. Uso de herramientas: un informe de lo que se ejecutó

**Lo que suele entregarte:** un resumen de lo que el agente ejecutó o buscó y de lo que obtuvo. «Ejecuté la suite de pruebas: todo pasa». Una tabla de resultados. Enlaces que encontró.

La guía de Anthropic presenta los resultados de las herramientas como la comprobación que el agente hace de sí mismo: «Durante la ejecución, es crucial que los agentes obtengan del entorno, en cada paso, una “verdad de referencia” (como los resultados de llamadas a herramientas o la ejecución de código) para evaluar su avance». Esa comprobación ocurre dentro del agente. Lo que te llega a ti es su relato de ella.

**Qué revisar:** que cada afirmación remita a una salida que puedas ver. Compara una cifra del resumen con la salida real. Abre uno de los enlaces.

## 3. Planificación: `plan.md`

**Lo que suele entregarte:** un plan, una especificación, una lista de tareas que el agente va marcando.

Ng es franco sobre este patrón en la parte 4:

> «Por un lado, la planificación es una capacidad muy potente; por otro, produce resultados menos predecibles. En mi experiencia, aunque consigo que los patrones agénticos de reflexión y uso de herramientas funcionen de forma fiable y mejoren el rendimiento de mis aplicaciones, la planificación es una tecnología menos madura, y me cuesta predecir de antemano qué va a hacer».

También es optimista: «Pero el campo sigue avanzando rápido, y estoy seguro de que las capacidades de planificación mejorarán pronto».

**Qué revisar:** el plan antes de que se ejecute, con [la revisión de cinco minutos](/es/reviewing-agent-plans/): estructura, una afirmación, pasos irreversibles, diagramas, alcance. Si el agente reescribe el plan a mitad de camino, compáralo con la versión que aprobaste; si está en git, `git diff plan.md` muestra qué cambió. En MarsDawn, la pestaña Esquema muestra la estructura de un plan largo, y un plan reescrito se recarga sin que pierdas tu posición, siempre que no tengas cambios sin guardar.

## 4. Colaboración multiagente: varios archivos, varios autores

**Lo que suele entregarte:** una especificación de un agente, notas de implementación de otro, una revisión de un tercero, y resúmenes que pasan de uno a otro. A veces cada uno trabaja en su propia rama o worktree.

**Qué revisar:** los traspasos. Donde un agente resume el trabajo de otro, busca un requisito que no haya pasado. Busca dos archivos que se contradigan, y decide cuál manda antes de que alguien construya sobre el otro. En MarsDawn, abre la carpeta compartida con Archivo ▸ Abrir carpeta… (⇧⌘O): los archivos nuevos aparecen en la pestaña Archivos en un segundo aproximadamente, a medida que los agentes los escriben, y en una copia de trabajo de git el encabezado muestra la rama o el worktree, para que dos ventanas con el mismo nombre de archivo en ramas distintas no parezcan iguales. Cuando el resultado tiene que llegar a personas que no leen Markdown, [Compartir PDF exportados](/es/sharing-exported-pdfs/) cubre ese paso.

## De un vistazo

| Patrón (Ng) | Lo que suele entregarte (deducción nuestra) | Qué leer primero (sugerencia nuestra) |
|---|---|---|
| Reflexión | Un borrador revisado, quizá con una autoevaluación | El resultado frente a tu pedido; comprueba un «verificado» |
| Uso de herramientas | Un informe de lo que se ejecutó y lo que obtuvo | Una afirmación rastreada hasta la salida real |
| Planificación | `plan.md`, una especificación, una lista de tareas | La revisión de cinco minutos, antes de ejecutar |
| Colaboración multiagente | Varios archivos de varios agentes, quizá en varias ramas | Los traspasos, y qué archivo manda |

Ninguno de los autores citados aquí menciona MarsDawn ni lo recomienda, ni a ninguna otra herramienta de Markdown. MarsDawn no incluye ningún modelo de IA: no sabe qué modelo produjo un archivo, y no hará estas comprobaciones por ti. Mantiene los archivos legibles mientras tú las haces.

## Pruébalo

MarsDawn está en el [Mac App Store](https://apps.apple.com/app/id6812925073). También existe la herramienta de línea de comandos gratuita `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Exporta Markdown a PDF sin la app: consulta [Markdown a PDF](/es/markdown-to-pdf/).

[Línea de comandos](/es/cli/) · Antes de comprar, conviene saber: [Lo que MarsDawn no hace](/es/limits/)

## Para seguir leyendo

- Por qué lo que entrega un agente es difícil de leer, con una lista de comprobación: [Leer lo que te entrega tu agente](/es/reading-agent-output/).
- La comprobación del plan completa: [Revisar el plan de un agente en cinco minutos](/es/reviewing-agent-plans/).
- Lo que la transparencia te pide, y lo que no: [Anthropic quiere agentes transparentes. ¿Quién lee lo que exponen?](/es/agent-transparency/)

## Fuentes

- Andrew Ng, «Agentic Design Patterns Part 1», The Batch, 20 de marzo de 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, «Agentic Design Patterns Part 2, Reflection», The Batch, 27 de marzo de 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, «Agentic Design Patterns Part 4, Planning», The Batch, 10 de abril de 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, «Agents», 7 de enero de 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, «LLM Powered Autonomous Agents», Lil’Log, 23 de junio de 2023: [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (citado según la versión en línea del 26/09/2026).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Editor de Markdown nativo para Mac: vista previa en vivo junto al código, Mermaid, KaTeX, Vista rápida, exportación a PDF. Pruébalo gratis, 4,99 USD una vez.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Ver Markdown en una Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.
- [Quick Look para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Presiona la barra espaciadora sobre un archivo Markdown en el Finder para leerlo renderizado, con diagramas Mermaid, fórmulas KaTeX y código resaltado. Vista rápida de MarsDawn no queda bloqueada por la prueba.
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
- [Transparencia de los agentes](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [Revisar el plan de un agente](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
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
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Français](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
