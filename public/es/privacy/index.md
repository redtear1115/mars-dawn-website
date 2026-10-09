# Política de privacidad

Cómo trata tu información MarsDawn, el editor de Markdown para macOS.

Última actualización: 2026-10-10

> **La app MarsDawn no recopila ningún dato sobre ti.** No hay cuenta, ni publicidad, ni seguimiento. Tus documentos y tus ajustes se quedan en tu Mac.

## El sitio web

La app y este sitio web son dos cosas distintas. La app no recopila nada. Una visita solo puede registrarse aquí, en marsdawn.southern-light.dev.

Este sitio usa **Google Analytics 4**, cargado mediante **Google Tag Manager**. Todos los visitantes empiezan con la analítica denegada: el modo de consentimiento (Consent Mode) de Google solo envía un ping sin cookies, sin cookie de analítica y sin identificador persistente, hasta que eliges *Aceptar* en el aviso. Si eliges *Rechazar*, o no eliges nada, todo sigue así; y si eliges *Rechazar* después de haber aceptado, la analítica se desactiva de inmediato y se eliminan las cookies que se indican abajo. Puedes cambiar tu elección en cualquier momento con el enlace «Ajustes de cookies» del pie de cada página. La elección en sí se guarda solo en el almacenamiento local de tu navegador, nunca en una cookie nuestra.

Una vez que aceptas, Google Analytics instala sus propias cookies (`_ga` y `_ga_<measurement id>`) y registra:

- **Páginas vistas y referente.** Qué página se vio y, cuando el navegador la envía, la dirección de procedencia.
- **Ubicación aproximada, dispositivo y navegador.** Una ubicación aproximada derivada de tu dirección IP (como mucho, a nivel de ciudad), tu tipo de dispositivo, tu sistema operativo y tu navegador. Nada de ello es lo bastante preciso para identificarte.
- **Clics salientes y profundidad de desplazamiento.** La medición mejorada de Google Analytics registra los clics que salen del sitio, como el enlace al Mac App Store, y hasta dónde te desplazas en una página.
- **Direcciones IP.** Google Analytics 4 no registra ni almacena direcciones IP.
- **Lo que no se registra.** Ninguna cuenta, porque el sitio no tiene. Ningún documento, ni nada de lo que escribes. Ninguna publicidad entre sitios, ni ningún perfil tuyo. Las solicitudes que hace la app de archivos de tema en `/themes/` se omiten y no se reenvían. El simulador de temas y la galería en `/themes/new/` y `/themes/gallery/` se ejecutan por completo en tu navegador y tampoco envían datos de tema a Google Analytics.
- **Conservación.** Google conserva estos datos durante 14 meses y después los elimina.
- **Dónde se tratan.** Google Tag Manager y Google Analytics los opera Google; tus datos pueden tratarse en Estados Unidos y en otros países donde Google opera.
- **El proveedor de alojamiento.** Cloudflare aloja el sitio y, como cualquier proveedor de alojamiento, ve tu dirección IP mientras responde a la solicitud. Ese registro pertenece al proveedor. No es la analítica descrita arriba.

## Lo que se queda en tu Mac

- **Tus documentos.** MarsDawn solo lee y escribe los archivos y carpetas que abres, guardas o eliges. La app nunca los sube a ningún sitio.
- **Tus ajustes.** El aspecto, el tema de la vista previa, la disposición de las ventanas y la preferencia de imágenes se guardan en las preferencias propias de la app, en tu Mac.
- **El acceso a carpetas que concedes.** Cuando dejas que MarsDawn muestre imágenes o archivos de página de una carpeta, o eliges una carpeta de notas, la app guarda un marcador de macOS para poder volver a abrir esa carpeta. Una carpeta que abres en la barra lateral sigue siendo legible y modificable por MarsDawn hasta que la eliminas en Ajustes, no solo mientras su ventana está abierta. Puedes eliminar carpetas en cualquier momento en MarsDawn › Ajustes.

## Cuándo usa MarsDawn internet

MarsDawn funciona totalmente sin conexión. Solo se conecta a internet **cuando tú lo eliges**, para un documento que hace referencia a la web o para la galería de temas. Para los documentos:

- **Documentos Markdown.** Las imágenes web están bloqueadas por omisión. Solo se cargan después de que hagas clic en *Cargar imágenes* en la vista previa, o si activas *Cargar imágenes remotas automáticamente* en Ajustes. Nada más de lo que menciona un documento Markdown se carga desde la web.
- **Documentos HTML.** Un documento HTML se abre de forma estática: su código no se ejecuta y no se carga nada desde la web. Si un documento contiene código que podría ejecutarse, puedes elegir *Visualización › Ejecutar este documento* para ese documento. Su propio código se ejecuta entonces hasta que lo detengas, el documento se vuelva a cargar o cierres la ventana. Esa elección nunca se recuerda y no es un ajuste. Mientras se ejecuta, el documento puede enviar datos por la red y leer imágenes, hojas de estilo, tipos de letra y archivos multimedia de su carpeta y de las carpetas que contiene. El código descargado de la web nunca se ejecuta.

MarsDawn carga contenido web solo por https. Una dirección http simple nunca se carga, con ningún ajuste, y MarsDawn no la reescribe a https. En un documento Markdown, la vista previa muestra un marcador de posición en su lugar.

Cuando se carga contenido web, tu Mac lo solicita directamente a los servidores que lo alojan. Como en cualquier solicitud web, esos servidores pueden ver así tu dirección IP y lo que se solicitó. El desarrollador de MarsDawn no recibe nada de esta información.

Los enlaces en los que haces clic en la vista previa se abren en tu navegador web predeterminado, según las prácticas de privacidad de ese navegador. El audio y el video nunca se reproducen solos.

Si abres *Ajustes › Aspecto › Obtener más temas…*, eliges *Buscar actualizaciones de temas* o instalas o actualizas un tema, MarsDawn descarga la lista de temas, las vistas previas y los archivos de los temas desde marsdawn.southern-light.dev. Los temas se actualizan automáticamente solo durante estas descargas, nunca en segundo plano. La solicitud no incluye cuenta, identificador, cookie ni datos de documentos; como en cualquier solicitud web, nuestro proveedor de alojamiento, Cloudflare, ve tu dirección IP y qué archivos se solicitaron. *Denunciar tema…* no envía ninguna solicitud desde la app: solo abre un enlace de GitHub o de correo electrónico en tu navegador o en tu app de correo.

## Siri, Atajos y Spotlight

MarsDawn ofrece acciones para Siri, la app Atajos y Spotlight, como crear un documento o agregar una nota. Cuando las usas, el texto que proporcionas se pasa a MarsDawn en tu Mac y se guarda solo donde indica la acción (un documento nuevo, o el archivo `Inbox.md` de la carpeta de notas que elegiste). Lo que dictas a Siri lo trata Apple según la [Política de privacidad de Apple](https://www.apple.com/legal/privacy/).

## Exportar e imprimir

La exportación a PDF y la impresión se hacen en tu Mac. El PDF se guarda donde tú elijas. La impresión pasa por macOS hasta la impresora que selecciones.

## La herramienta de línea de comandos marsdawn

La herramienta de línea de comandos opcional `marsdawn`, que se distribuye por separado, también se ejecuta por completo en tu Mac. Lee el archivo Markdown que indicas y escribe el PDF que pides. Solo carga imágenes web cuando pasas `--allow-remote-images`.

## Menores

La app MarsDawn no recopila datos de nadie, menores incluidos. Una visita registrada en el sitio web no es una cuenta y no se usa para identificar a nadie.

## Compras

MarsDawn se vende a través del Mac App Store. Apple procesa la compra según sus propias condiciones, y el desarrollador nunca recibe tus datos de pago.

## Cambios en esta política

Si alguna vez MarsDawn empieza a tratar los datos de otra manera, esta página se actualizará antes de que salga esa versión, y la fecha de arriba cambiará.

## Contacto

Preguntas sobre privacidad: [support@southern-light.dev](mailto:support@southern-light.dev)

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Markdown para las personas que dirigen el trabajo de los agentes: un editor nativo para Mac con vista previa en vivo, diagramas Mermaid y exportación a PDF. En el Mac App Store.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
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
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Deutsch](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Français](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [한국어](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
