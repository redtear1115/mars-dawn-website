# Una prueba que pasa en un Mac quizá no esté probando lo que crees.

Oferta de Black Friday: la compra única que desbloquea la app está a mitad de precio, 2,49 USD en lugar de 4,99 USD, hasta el 30 de noviembre. Vuelve a 4,99 USD el 1 de diciembre. <!-- sale-line -->

El vibe coding no es algo malo, y MarsDawn también se desarrolla con agentes. Pero el software del que dependes se juzga por lo que viene después de la primera versión: años de mantenimiento y seguridad, que empiezan por comprobar que un cambio no ha roto nada.

**Una prueba pasaba en un Mac mini y fallaba en un MacBook Air. El producto estaba bien. La prueba leía los colores a través del perfil de color de la pantalla, y en el Mac mini pasaba por suerte. Una segunda máquina encontró un error en la prueba, no en el código.**

¿Solo quieres saber con qué archivos extremos u hostiles se prueba MarsDawn? Salta directamente a [Lo que le echamos](#inputs).

## La prueba que fallaba en un MacBook Air

Una ejecución completa de las pruebas del motor de exportación en el runner de macOS 15 de GitHub tarda cerca de una hora: unos 32 minutos para la compilación debug y unos 25 para la release. Para acortarlo, probamos a pasar la mitad de macOS 26 a un MacBook Air propio ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)).

En su primera ejecución allí, falló una prueba. Exporta un PDF con recuadros de aviso (Note, Tip, Warning) y comprueba que cada uno tenga en el borde una barra del color correcto, es decir, con una distancia de color menor que 0,16. En el MacBook Air, las distancias fueron 0,1634, 0,1648 y 0,1796. En un Mac mini, con el mismo commit, el mismo macOS y el mismo Xcode, la prueba pasaba.

Lo primero que pensamos fue que la exportación se había roto. No era así. El PDF no tenía ningún problema; lo que cambiaba entre las dos máquinas era cómo lo leía la prueba.

La prueba convertía cada página del PDF en una imagen y leía los píxeles, y macOS dibuja esa imagen en el espacio de color de la pantalla principal. El Mac mini estaba conectado a un monitor externo corriente; el MacBook Air usaba su pantalla integrada. Llenamos una imagen con un solo naranja y la volvimos a leer: (0,784; 0,278; 0,106) volvía como (0,822; 0,335; 0,179) en el Mac mini y como (0,782; 0,395; 0,221) en el MacBook Air.

Esto es lo importante: en el Mac mini, la prueba tampoco leía los colores correctos. Se desviaba hasta 0,128, justo dentro del límite de 0,16. Pasaba gracias al monitor, no porque midiera bien la barra.

La corrección ([kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)) solo cambia la prueba: dibuja la página en una imagen con un espacio de color sRGB fijo, así que no interviene ninguna pantalla. Ahora las dos máquinas leen los colores de las barras con exactitud, con una distancia de 0,0, tanto en la pantalla integrada del MacBook Air como en el Mac mini. La CI del pull request pasó ([run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)), y una vez que la corrección llegó a la rama del runner del MacBook Air, la batería completa pasó allí también ([run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)). Después la hicimos fallar a propósito: con todos los colores esperados en azul, se puso en rojo en los cinco recuadros de aviso.

Todavía tiene un hueco conocido. Note y Caution usan dos naranjas separados por unos 0,119, dentro del límite de 0,16, así que si se intercambiaran, la prueba probablemente no lo notaría. Lo dejamos por escrito en lugar de fingir que la prueba es completa.

Una prueba que no puede fallar no protege nada, y tampoco una que falla por el motivo equivocado, como el perfil de color de una pantalla. El verde en una máquina te dice que la prueba pasó allí, no que mida lo que dice su nombre.

## Las pruebas son capas de redes

Ninguna prueba lo atrapa todo. Cada capa es una red con una malla distinta, y un error que se escapa por una debería caer en la siguiente:

- **PDF de referencia:** el motor de exportación (el proyecto de código abierto [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit), que también hace funcionar el comando `marsdawn`) exporta documentos de ejemplo, y el texto de cada página se compara con una copia guardada. Esto atrapa contenido que desaparece sin avisar o un número de páginas que cambia.
- **Sistemas y compilaciones distintos:** el motor se ejecuta en macOS 15, la versión más antigua que admite, y en macOS 26, con la que se distribuye la app, cada uno como compilación debug y release. La batería completa de la app se ejecuta en cuatro combinaciones: firmada y sin firmar, cada una con el paywall desactivado y activado. Esto atrapa lo que solo se rompe en un sistema más antiguo, o solo en la compilación que reciben de verdad los clientes.
- **Hardware real:** la CI de la app corre en Mac propios (tanto el Mac mini como el MacBook Air), y probar la batería del motor en ese MacBook Air ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240), sigue siendo un borrador abierto) es lo que atrapó el fallo del perfil de color de arriba. Una segunda máquina atrapa las pruebas que solo pasan por la máquina en la que se ejecutan.
- **Controles negativos:** la CI de la app guarda 22 copias rotas a propósito de un script de limpieza y 20 de un script de ejecución de pruebas, a cada una le falta una comprobación de seguridad, y las pruebas tienen que fallar con todas. El script de limpieza borra compilaciones antiguas y copias de trabajo de un Mac, así que una sola comprobación que falte podría borrar lo que no debe. Si una copia rota pasa, lo que está roto es la prueba.
- **Otro par de ojos:** nuestra práctica es que un agente aparte verifique un cambio antes de fusionarlo, como en kit #242, y los cambios que afectan a cómo se usa la app pasan antes por una revisión de escenarios. Esto atrapa el «terminado» que no lo está, y el código que funciona, pero en la situación equivocada.
- **Una persona fusiona.** La persona que desarrolla MarsDawn revisa y fusiona cada cambio; ningún agente ni bot fusiona nada.

## Lo que le echamos

Esas redes valen tanto como lo que se echa en ellas. Algunas de las entradas con las que las pruebas alimentan al motor, y lo que cada prueba garantiza:

- **Archivos muy grandes.** Medido en nuestra máquina de pruebas, con una compilación release: un documento de 2 MB se muestra en menos de un segundo y medio, y uno de 5 MB demasiado complejo para maquetar se abre igualmente como texto sin formato en menos de un segundo. Lo que pase de 16 MB se muestra como texto sin analizarlo en absoluto.
- **Cientos de miles de líneas.** Unos 3 MB de líneas de una sola palabra, cerca de 800 000, se detectan como demasiado a mitad de camino: el motor deja de leer ahí y muestra el archivo como texto sin formato.
- **Marcas que nunca se cierran.** Un megabyte de marcas de apertura de sección sin cierre, o decenas de miles apiladas unas dentro de otras, no debe tardar más de unas dos veces lo que tarda un megabyte de texto sin formato. A partir del octavo nivel, nada se anida más.
- **Fórmulas.** Una fórmula mal escrita muestra un error en su sitio en lugar de romper la página. Una de más de 10 000 caracteres se queda tal como está escrita, solo se dibujan a la vez las primeras 1000 de un documento, y nada dentro de una fórmula puede convertirse en un enlace, una imagen o marcado de la página.
- **HTML hostil dentro de Markdown.** Los scripts se eliminan y nunca se ejecutan, y los marcos incrustados se quitan antes de que la página los muestre. Las imágenes remotas siguen desactivadas a menos que las permitas, e incluso entonces solo cargan las seguras (HTTPS). Una copia de control tiene quitado el filtro de scripts, y la prueba tiene que fallar con ella.
- **Un archivo de tema hostil.** Se rechaza, y el mensaje de error nunca repite caracteres de control ocultos ni enlaces del archivo. Los archivos de tema de más de 16 KB ni siquiera se leen.

Nada de esto es gratis. El límite de tiempo de una ejecución del motor ha pasado de 30 minutos a 45, luego a 50, luego a 70 y ahora a 90. macOS 15 llegó dos veces al límite de 50 minutos con todas las pruebas pasando, y más tarde llegó a 70 minutos en su último paso, con todos los pasos anteriores pasando.

## Cuatro hábitos que puedes copiar

1. **Separa el agente que escribe del agente que comprueba.** Dale al que comprueba el cambio y lo que significa «terminado», sin la explicación del agente que lo escribió, y pídele que ejecute él mismo las pruebas y diga qué no comprobó. En kit #242, el agente verificador ejecutó la prueba antigua en el MacBook Air para verla fallar antes de dar por buena la nueva. Cuesta los tokens de una segunda sesión.
2. **Mira fallar cada prueba una vez.** El verde solo vale algo si has visto esa misma prueba ponerse en rojo cuando lo que comprueba estaba realmente mal. Así que, antes de fiarte de una marca verde, rompe lo que protege (o pídeselo al agente), mira cómo se pone en rojo, déjalo como estaba y mira cómo vuelve al verde. Los agentes escriben muy bien pruebas que pasan; justo por eso necesitas verlas fallar.
3. **Ejecuta tus pruebas en un segundo entorno.** ¿No tienes un segundo Mac? Una matriz de CI con dos versiones del sistema, o con una compilación debug y otra release, es un buen comienzo. Buscas pruebas que solo pasan por casualidad.
4. **Trata «no se ejecutó ninguna prueba» como un fallo.** El `unittest` de Python 3.9 termina con éxito cuando no encuentra ninguna prueba, así que una errata en una ruta te da una marca verde. Nuestra CI lee el número de pruebas y falla si es cero, y comprueba que el resumen diga «0 failed», no solo el código de salida. Añadimos esa comprobación después de que una verificación independiente encontrara ese hueco en nuestra propia CI.

## En pocas palabras

Que una app se haya hecho con vibe coding importa menos que si alguien sigue probándola y manteniéndola. Vale la pena comprobarlo al elegir software: ¿explica cómo se prueba?, ¿cuándo se actualizó por última vez?

Deja que el agente sea rápido. La comprobación, déjasela a pruebas que miden lo correcto y a una persona que lee el resultado.

## Siguiente

- Por qué una persona todavía tiene que leer lo que escribió un agente: [Por qué lo que produce la IA todavía necesita un lector humano](/es/reviewing-ai-output/).
- Cómo leer los planes e informes que te devuelve un agente: [Leer lo que te devuelve tu agente](/es/reading-agent-output/).

## Fuentes

- La prueba que fallaba y su causa: [mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241).
- La corrección y su verificación independiente: [mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242).
- Probar la CI en un MacBook Air (borrador abierto), con tiempos de ejecución: [mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240).
- La CI del motor de exportación, con el historial de su límite de tiempo en los comentarios: [ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml).
- El repositorio de la app es privado; los detalles de la app que aparecen arriba salen de su flujo de CI y de sus scripts de prueba.

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Revisa el Markdown, JSON y YAML de tu agente en tu Mac: vista previa en vivo, Mermaid, KaTeX, Vista Rápida y PDF. Pruébalo gratis y luego 2,49 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor nativo para Mac de Markdown, JSON y YAML: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 2,49 USD. Sin suscripción y sin cuenta.
- [Imprimir y PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Previsualiza tu Markdown y luego imprímelo o guárdalo como PDF en tu Mac, con la disposición Documento, Guía o Folleto, con diagramas y código resaltado.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista Rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin edición en iPhone o iPad, sin plugins, sin cuentas. Temas, pero sin CSS personalizado. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista Rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista Rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista Rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista Rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [Copiar para IA](https://marsdawn.southern-light.dev/es/copy-for-ai/index.md): Copia el texto seleccionado con su ruta de archivo y números de línea, y pégalo en Claude Code o en cualquier agente. En tu Mac, sin IDE ni plugins.
- [Pasar de HackMD a tu Mac](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026, salvo la celda de PDF de MarsDawn, actualizada el 7 de noviembre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 2,49 USD una sola vez.
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
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
