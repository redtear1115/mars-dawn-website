# Revisar el plan de un agente en cinco minutos

Tu agente escribió un plan y espera tu visto bueno. Tienes cinco minutos, no una hora. Esta es una forma de aprovecharlos que funciona en cualquier editor, incluso en uno de texto plano. MarsDawn ayuda con algunos pasos, y te diremos cuáles. No ayuda con el más importante.

**No leas el plan de arriba abajo. Revisa su estructura, comprueba una afirmación, encuentra lo irreversible, mira los diagramas y el alcance, y escribe comentarios que el agente pueda aplicar. Seis pasos, unos cinco minutos.**

## Por qué importa antes de ejecutarlo

Chip Huyen, al explicar por qué la planificación debe ir separada de la ejecución, pone el costo sin rodeos: «Sin supervisión, un agente puede ejecutar esos pasos durante horas, gastando tiempo y dinero en llamadas a la API, antes de que te des cuenta de que no lleva a ninguna parte». Lo que añadimos nosotros: un plan es el lugar más barato para detectar un error. Corregir una línea de `plan.md` cuesta una frase. Corregir lo que el agente hizo después cuesta una tarde.

## El ejemplo

Le pediste a un agente que moviera los avatares de los usuarios a un almacenamiento de objetos sin romper los enlaces existentes. Te devuelve esto:

```
# Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. ✅ done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.
```

Se lee bien. También borraría todos los avatares antes de copiar uno solo.

## Los seis pasos

**1. Lee solo los encabezados.** *(un minuto aproximadamente)* ¿El plan coincide con lo que pediste? Si falta una sección, normalmente falta trabajo. Aquí: Goal, Steps, Status. Pediste que los enlaces existentes siguieran funcionando, y ningún encabezado habla de los enlaces antiguos ni de cómo deshacer el cambio. Ese es tu primer comentario.

En una terminal, `grep -n '^#' plan.md` muestra solo los encabezados, y la mayoría de los editores también pueden mostrar un esquema. En MarsDawn, la pestaña Esquema de la barra lateral (Visualización ▸ Mostrar barra lateral, ⌃⌘S) los enumera, y un clic te lleva a cada uno.

**2. Encuentra cada lugar que afirme que algo está hecho, que pasó o que se verificó, y comprueba uno tú mismo.** *(un minuto aproximadamente)* Abre el archivo, ejecuta la prueba, cuenta las filas. Chip Huyen describe un fallo en el que «el agente está convencido de haber completado una tarea cuando no es así». En su ejemplo, a un agente se le pide alojar a 50 personas en 30 habitaciones de hotel, acomoda a 40 y dice que terminó.

```
grep -n -i -E 'done|pass|verified|✅' plan.md
```

Aquí encuentra «✅ done» y «All tests pass.» ¿Qué pruebas? ¿Alguna toca los avatares? Ejecútalas, o pregunta. MarsDawn no puede hacer este paso por ti. Nadie más que tú puede.

**3. Busca los pasos que no se pueden deshacer.** *(un minuto aproximadamente)* Borrar datos, migraciones, force-push, cualquier cosa que envíe, pague o publique. Esos esperan tu aprobación explícita. Chip Huyen describe la misma idea desde el lado del sistema: «Si un plan incluye operaciones riesgosas, como actualizar una base de datos o fusionar un cambio de código, el sistema puede pedir aprobación humana explícita antes de ejecutarlas, o dejar que las ejecuten personas». Aquí, el paso 4 borra los originales, y va antes del paso 5, la copia.

**4. Lee los diagramas renderizados y compara cada flecha con el texto.** Un diagrama de flujo que dice «copiar → verificar → borrar» mientras los pasos dicen otra cosa es un hallazgo. Este plan no tiene diagramas, así que hoy te lo saltas. Cuando haya uno, mira la imagen, no el código Mermaid: muchos editores tienen vista previa, y [Cómo ver un archivo Markdown en la Mac](/es/view-markdown-on-mac/) y [Ver Markdown en otros lugares](/es/vs/markdown-preview-tools/) recorren las opciones. En MarsDawn, el diagrama renderizado está junto a su código (⌘2), y un diagrama roto muestra su código con el error debajo, lo que merece un comentario propio.

**5. Haz una lista de los archivos y sistemas que toca el plan, y pregunta por todo lo que no pediste.** *(pasos 4 y 5 juntos, un minuto aproximadamente)* Aquí: la configuración de almacenamiento, las plantillas, una carpeta en el servidor, un bucket. ¿Quién puede leer el bucket? No dijiste que debiera ser público. Si abriste la carpeta de trabajo del agente en MarsDawn (Archivo ▸ Abrir carpeta…, ⇧⌘O), los archivos nuevos que escribe aparecen en la pestaña Archivos en un segundo aproximadamente, y el encabezado muestra la rama de git o el worktree, para que sepas qué copia de trabajo estás revisando.

**6. Escribe tus comentarios como lugar, problema y solución, un problema por línea.** *(el último minuto)*

```
plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.
```

Cualquier editor con números de línea sirve. En MarsDawn, Edición ▸ Copiar referencia (⌥⌘C) copia tu posición como `plan.md:10`, y Copiar para IA (⌃⌥⌘C) añade debajo el texto seleccionado.

## Si tienes un minuto

Haz el paso 2. Ahí es donde atrapas a un agente que cree que ya terminó.

## Cuando cinco minutos no bastan

A veces no puedes saber si un paso es correcto, porque está fuera de lo que conoces. Jess Ou, en el artículo explicativo de LangChain sobre agentes de 2026, lo dice en dos frases: «No delegues un juicio que no puedes evaluar. Si tú no reconocerías una buena respuesta, el agente tampoco». Lo que concluimos nosotros: si no puedes juzgar un paso, eso no es motivo para aprobarlo más rápido. Es motivo para preguntarle a alguien que sí pueda.

## Qué hace MarsDawn aquí, y qué no

MarsDawn no incluye ningún modelo de IA. No encontrará los problemas de este plan, y no hace ni el paso 2 ni el paso 3. Mantiene el archivo legible mientras trabajas: el esquema para el paso 1, los diagramas renderizados para el paso 4, la pestaña Archivos para el paso 5, las referencias de línea para el paso 6. Y si el agente revisa el plan mientras lo lees, MarsDawn lo recarga y conserva tu posición, siempre que no tengas cambios sin guardar.

Cuando el plan esté decidido, si alguien más necesita verlo, [Compartir PDF exportados](/es/sharing-exported-pdfs/) y [Markdown a PDF](/es/markdown-to-pdf/) explican cómo enviarlo en PDF.

## Pruébalo

MarsDawn está en el [Mac App Store](https://apps.apple.com/app/id6812925073). También existe la herramienta de línea de comandos gratuita `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Exporta Markdown a PDF sin la app.

[Línea de comandos](/es/cli/) · Antes de comprar, conviene saber: [Lo que MarsDawn no hace](/es/limits/)

## Para seguir leyendo

- Por qué lo que entrega un agente es difícil de leer: [Leer lo que te entrega tu agente](/es/reading-agent-output/).
- Por qué los agentes exponen sus planes: [Anthropic quiere agentes transparentes. ¿Quién lee lo que exponen?](/es/agent-transparency/)
- Los planes no son lo único que entregan los agentes: [Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno](/es/agent-design-patterns/).

## Fuentes

- Chip Huyen, «Agents», 7 de enero de 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou, «What is an AI agent?», LangChain, 31 de julio de 2026: [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

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
- [Transparencia de los agentes](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
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
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [Deutsch](https://marsdawn.southern-light.dev/de/reviewing-agent-plans/index.md): Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.
- [Français](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [한국어](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
