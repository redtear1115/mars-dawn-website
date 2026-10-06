"""Spanish (es) page copy for the MarsDawn site, tranche 2 (#165).

Same shape as scripts/copy_ja.py: build(k) returns the tables build_pages.py keeps per locale.
Translated from the en copy on main @ 6fe8435. Neutral, Latin-American-leaning Spanish, tú (no
vosotros). UI terms follow the app's es strings (release/1.1.0): Vista rápida (Quick Look),
Archivo, Visualización, Ajustes, Atajos, prueba (trial), desbloquear (unlock); «» quotes.
Built-in theme names stay English. Inline build_pages.py tables are returned under their own keys.
"""


def build(k) -> dict:
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn: un editor de Markdown para Mac, con vista previa en vivo',
        "description": 'Markdown para las personas que dirigen el trabajo de los agentes: un editor nativo para Mac con vista previa en vivo, diagramas Mermaid y exportación a PDF. En el Mac App Store.',
        "intro": """
<section class="intro hero">
  <p class="kicker">Herramientas de frontera para quienes construyen</p>
  <h1><span>Toma el mapa.</span> <span>Lee el amanecer.</span></h1>
  <p>Markdown para las personas que dirigen el trabajo de los agentes.</p>
</section>
""",
        "body": """
<h2 class="loop-title">Lee lo que escribió tu agente.</h2>
<ol class="loop-steps">
  <li><strong>El agente escribe.</strong> Tu agente de programación o tu asistente de escritura redacta el Markdown: un README, una especificación, unas notas.</li>
  <li><strong>Tú lo revisas en MarsDawn.</strong> Abre el archivo y léelo ya renderizado, con diagramas Mermaid y código resaltado, junto al código fuente.</li>
  <li><strong>El agente corrige.</strong> Pide cambios. Abre el archivo corregido y léelo de la misma manera.</li>
</ol>
<p><a href="/es/reading-agent-output/">Cómo revisar lo que te devuelve tu agente</a>.</p>
""",
    }
    pages['yours'] = {
        "title": 'Un editor de Markdown para Mac sin cuenta y sin nube · MarsDawn',
        "description": 'MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.',
        "intro": """
<section class="intro">
  <h1>Lo que escribes se queda en tu Mac.</h1>
  <p>MarsDawn no tiene cuenta, ni sincronización, ni nube. Abre un archivo, tú escribes y lo guarda donde elegiste.</p>
</section>
""",
        "body": """
<h2>Qué significa</h2>
<ul>
  <li>No hay ninguna cuenta que crear ni en la que iniciar sesión.</li>
  <li>Nada se sincroniza con una nube. Tus documentos se quedan donde los guardas.</li>
  <li>No se rastrea nada. MarsDawn no recopila ningún dato sobre ti, y su etiqueta de privacidad en el App Store dice «Datos no recopilados».</li>
  <li>Las imágenes web siguen bloqueadas hasta que decides cargarlas, así que abrir un documento nunca le avisa a un servidor de que lo estás leyendo. Cuando sí las cargas, se cargan solo por https.</li>
  <li>Las imágenes locales aparecen en la vista previa en cuanto das acceso a su carpeta.</li>
</ul>
<p>Los detalles están en la <a href="/es/privacy/">política de privacidad</a>.</p>
""",
    }
    pages['pay-once'] = {
        "title": 'Pruébalo gratis y paga una sola vez · MarsDawn',
        "description": 'MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 4,99 USD. Sin suscripción y sin cuenta.',
        "intro": """
<section class="intro">
  <h1>Pruébalo todo. Después, paga una vez.</h1>
  <p>MarsDawn se descarga gratis. Comienza la prueba de 14 días y todas las funciones están disponibles; para seguir usándolo después, una sola compra de 4,99 USD lo desbloquea. No hay suscripción ni cuenta.</p>
</section>
""",
        "body": """
<h2>Cómo funciona</h2>
<ol class="loop-steps">
  <li><strong>Descárgalo gratis.</strong> MarsDawn se descarga gratis desde el Mac App Store.</li>
  <li><strong>Prueba todo durante 14 días.</strong> Comienza la prueba y todo MarsDawn funciona durante 14 días: todos los temas y disposiciones, la exportación a PDF y la impresión, y las acciones de Siri y Atajos. Vista rápida en el Finder funciona con o sin prueba.</li>
  <li><strong>Desbloquéalo una vez.</strong> Para seguir usándolo después, desbloquéalo una sola vez por 4,99 USD. Es una compra dentro de la app, no una suscripción: nada se renueva y nada se te cobra más adelante.</li>
</ol>
<ul>
  <li>La prueba tampoco te cobra nada. Cuando termina, no se compra nada a menos que elijas desbloquear.</li>
  <li>No hay cuenta. MarsDawn nunca te pide que crees una.</li>
</ul>
<h2>Qué funciona y cuándo</h2>
<!--compare:pay-once-states-->
<p>Antes de que comiences la prueba, MarsDawn muestra la oferta de prueba. Comenzarla no cuesta nada.</p>
<p>Los archivos PDF que abres en MarsDawn se bloquean de la misma manera cuando termina la prueba.</p>
<h2>Si no lo desbloqueas</h2>
<ul>
  <li>Después de 14 días, y hasta que lo desbloquees, no puedes leer, editar, exportar ni imprimir documentos en MarsDawn. Un documento se sigue abriendo, pero su contenido queda cubierto.</li>
  <li>Tus archivos no cambian. Son archivos normales en tu Mac, y Vista rápida en el Finder los sigue mostrando.</li>
  <li>La <a href="/es/cli/">herramienta de línea de comandos <code>marsdawn</code></a>, que es gratis, los sigue exportando a PDF, con prueba o sin ella.</li>
  <li>Si hay un documento abierto en MarsDawn cuando termina la prueba, el texto que escribiste no se pierde: usa Archivo ▸ Guardar como… para conservarlo.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Exporta Markdown a PDF en tu Mac, con diagramas · MarsDawn',
        "description": 'Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos y tablas.',
        "intro": """
<section class="intro">
  <h1>El PDF se ve como la página que escribiste.</h1>
  <p>Exporta como PDF o imprime, con los colores claros de tu tema. Los diagramas y el código resaltado se conservan, y los saltos de página evitan separar lo que va junto.</p>
</section>
""",
        "body": """
<h2>Qué significa</h2>
<ul>
  <li>Los diagramas Mermaid se dibujan dentro del PDF.</li>
  <li>Los bloques de código conservan su resaltado de sintaxis.</li>
  <li>Los saltos de página evitan dejar un encabezado al final de una página o partir código, tablas y diagramas.</li>
  <li>Con cualquier disposición. La exportación funciona incluso cuando solo se muestra el código.</li>
</ul>
<p>La <a href="/es/cli/">herramienta de línea de comandos marsdawn</a>, que es gratis, usa el mismo exportador, así que un script o un agente de IA obtiene el mismo PDF.</p>
""",
    }
    pages['native'] = {
        "title": 'Una app nativa de Markdown para Mac: pestañas, Vista rápida · MarsDawn',
        "description": 'Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en el Mac.',
        "intro": """
<section class="intro">
  <h1>Hecho con las piezas del propio Mac.</h1>
  <p>Las ventanas, las pestañas, los menús y el editor de texto son los del Mac. La página renderizada la dibuja WebKit, el motor detrás de Safari.</p>
</section>
""",
        "body": """
<h2>Qué significa</h2>
<h3>Edición</h3>
<ul>
  <li>Disposiciones de código, dividida y vista previa, a una tecla de distancia (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>Los dos paneles se desplazan juntos, así que el párrafo que estás editando sigue a la vista.</li>
  <li>Resaltado de sintaxis Markdown en el editor, a juego con tu tema de la vista previa.</li>
</ul>
<h3>El resto del Mac</h3>
<ul>
  <li>Ventanas y pestañas nativas, guardado automático e historial de versiones.</li>
  <li>Vista rápida: presiona la barra espaciadora sobre un archivo Markdown en el Finder para ver una vista previa, con diagramas incluidos.</li>
  <li>Siri y Atajos: crea un documento nuevo a partir de una plantilla, agrega una línea a la bandeja de entrada de tus notas o vuelve a abrir un documento reciente.</li>
  <li>Inglés, chino tradicional, chino simplificado, japonés, alemán, francés, español y coreano.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'Lo que MarsDawn no hace · MarsDawn',
        "description": 'Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados. Lo que conviene saber antes de comprar.',
        "intro": """
<section class="intro">
  <h1>Lo que MarsDawn no hace.</h1>
  <p>Algunas cosas quedaron fuera a propósito. Si necesitas alguna, es mejor saberlo ahora que después de comprar.</p>
</section>
""",
        "body": """
<h2>Lo que queda fuera</h2>
<h3>Dispositivos y personas</h3>
<ul>
  <li><strong>Sincronización:</strong> MarsDawn no sincroniza tus documentos. Se quedan donde los guardas; para usar uno en otro Mac, guárdalo en una carpeta que ya sincronices.</li>
  <li><strong>iPhone y iPad:</strong> no hay app para ellos; MarsDawn es para el Mac.</li>
  <li><strong>Compartir:</strong> no hay cuentas ni edición compartida, porque MarsDawn es para una persona en su propio Mac.</li>
  <li><strong>Sistema:</strong> MarsDawn necesita macOS 26 o posterior.</li>
</ul>
<h3>Archivos y funciones</h3>
<ul>
  <li><strong>Edición:</strong> escribes Markdown a la izquierda y lees la página a la derecha; la página en sí no se puede editar.</li>
  <li><strong>Formatos:</strong> MarsDawn exporta a PDF e imprime, pero no exporta archivos de Word.</li>
  <li><strong>Otros archivos:</strong> los archivos de texto simple y los PDF se abren en modo de solo lectura.</li>
  <li><strong>Temas:</strong> incluye Dawn, Classic, Modern y Vivid, cada uno en claro y oscuro, y todavía no puedes instalar otros; consulta <a href="/es/themes/">temas de la vista previa y exportación a PDF</a> para ver lo que está planeado.</li>
  <li><strong>Plugins:</strong> MarsDawn no tiene plugins ni extensiones.</li>
</ul>
<h2>Después de la prueba</h2>
<p>Si no desbloqueas MarsDawn cuando termina la prueba de 14 días, no puedes leer, editar, exportar ni imprimir documentos en la app: se abren con el contenido cubierto. Tus archivos se quedan como están, Vista rápida los sigue mostrando y la herramienta de línea de comandos gratuita los sigue exportando. La <a href="/es/pay-once/">página de la prueba y el desbloqueo</a> pone las tres etapas lado a lado.</p>
""",
    }
    pages['changelog'] = {
        "title": 'Historial de cambios · MarsDawn',
        "description": 'Qué cambió en la herramienta de línea de comandos gratuita marsdawn.',
        "body": """
<section class="intro">
  <h1>Historial de cambios</h1>
  <p>Qué cambió en la herramienta de línea de comandos gratuita marsdawn. Una versión de MarsDawn del Mac App Store se menciona aquí solo cuando tiene una línea propia. No se incluyen las versiones anteriores a la 0.5.1.</p>
</section>

<h2>marsdawn 0.6.3</h2>
<p>6 de octubre de 2026. MarsDawn está en el Mac App Store.</p>
<ul>
  <li>Cuando la app no está instalada, <code>marsdawn open</code> indica dónde encontrar MarsDawn en el Mac App Store.</li>
  <li>El README y la skill para agentes enseñan <code>marsdawn open .</code> y <code>--folder</code>: MarsDawn 1.0.0 muestra la carpeta en la barra lateral de la ventana.</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>26 de septiembre de 2026. Correcciones de Mermaid, líneas de los errores de diagrama e instalación de la skill.</p>
<ul>
  <li>En un diagrama de secuencia, la etiqueta de un mensaje que cruza las líneas de vida de otros participantes sigue siendo legible, en la vista previa y en los PDF exportados.</li>
  <li><code>marsdawn export</code> puede con documentos llenos de diagramas Mermaid. Uno con 50 diagramas, que antes fallaba con el código 5, ahora se exporta.</li>
  <li><code>marsdawn export --json</code> agrega <code>diagramErrorDetails</code>, con los números de línea de cada error de diagrama: dónde empieza el diagrama en tu documento y, cuando Mermaid indica una, la línea del propio error.</li>
  <li><code>marsdawn skill --install</code> instala la skill para Claude Code en <code>~/.claude/skills/marsdawn/SKILL.md</code>, o en otra carpeta con <code>--dir</code>. Deja como está un archivo idéntico y solo reemplaza uno distinto con <code>--force</code>. Si no, termina con el código 64 (<code>skill_differs</code>) y no cambia nada.</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>25 de septiembre de 2026. Estado de la carpeta, errores completos de Mermaid y correcciones menores.</p>
<ul>
  <li><code>marsdawn open --folder</code> puede decir qué pasó con la carpeta. Con una app que responde, espera hasta <code>--wait</code> segundos (2 de forma predeterminada), y <code>--json</code> da un estado como <code>attached</code> o <code>needsUser</code>.</li>
  <li>Un diagrama Mermaid que no se puede analizar muestra el mensaje de error completo de Mermaid en lugar de solo su primera línea, con el número de línea contado desde el inicio de tu documento.</li>
  <li>La búsqueda del final de un bloque de front matter se detiene después de 1000 líneas, así que un bloque sin cerrar ya no obliga a recorrer el resto de un documento grande.</li>
  <li>Una app puede darle al enlace de regreso de una nota al pie una etiqueta traducida para la exportación a PDF y la impresión. La etiqueta no se imprime en la página, y <code>marsdawn export</code> conserva la etiqueta en inglés.</li>
  <li>El highlight.js incluido ahora está fijado por versión, origen y SHA-256, igual que KaTeX y Mermaid.</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>24 de septiembre de 2026. Notas al pie, contraste y carpetas.</p>
<ul>
  <li>Las notas al pie se muestran en los PDF exportados: referencias numeradas, con las notas después del cuerpo del texto.</li>
  <li>Todos los temas cumplen el contraste WCAG AA, en claro y en oscuro. Classic ahora es en blanco y negro.</li>
  <li><code>marsdawn skill</code> muestra la skill para agentes que corresponde al marsdawn instalado.</li>
  <li><code>marsdawn open</code> termina con el código 6 (<code>app_cannot_open_folders</code>) cuando el MarsDawn que encuentra no puede mostrar una carpeta, en lugar de informar que todo salió bien.</li>
  <li>Los marcadores de posición que se dibujan en las páginas exportadas también están en alemán, francés, español y coreano.</li>
  <li>Un marcador de posición de imagen ya no muestra la ruta absoluta que hay detrás de una ruta relativa muy larga.</li>
  <li><code>MARSDAWN_APP_PATH</code> solo se usa cuando apunta a una app MarsDawn.</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>19 de septiembre de 2026. Exportación a PDF y apertura de un archivo desde la línea de comandos.</p>
<ul>
  <li>La capa de texto de un PDF exportado está reparada para chino, japonés y coreano.</li>
  <li><code>marsdawn open --background</code> abre un archivo sin traer MarsDawn al frente.</li>
  <li><code>marsdawn open</code> acepta una carpeta, y MarsDawn la muestra en la barra lateral de la ventana (MarsDawn 1.0.0 y posteriores).</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn: una herramienta de línea de comandos gratuita de Markdown a PDF · MarsDawn',
        "description": 'La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.',
        "body": f"""
<section class="intro">
  <h1>Línea de comandos</h1>
  <p>La herramienta de línea de comandos gratuita <code>marsdawn</code>: exporta Markdown a PDF desde una shell o un agente LLM y, si tienes instalada la app MarsDawn, abre archivos en ella.</p>
</section>

<div class="summary"><p><strong>marsdawn es gratis y se distribuye por separado del Mac App Store.</strong> Instálalo con Homebrew: en un Mac con chip de Apple llega listo para usar. <code>export</code> funciona por sí solo; <code>open</code> necesita la app MarsDawn.</p></div>

<p>¿Llamas a marsdawn desde un agente de IA o un script? Consulta <a href="/es/cli/agents/">marsdawn para agentes</a> para ver la salida JSON, sus esquemas y todos los códigos de salida, o <a href="/es/cli/mcp/">el servidor MCP</a> si tu agente llama a herramientas por MCP.</p>

<h2>Instalación</h2>
<p>Con <a href="https://brew.sh">Homebrew</a>:</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>¿Usas un agente de programación? <a href="/es/cli/skill/">Agrega la skill de marsdawn</a>: un solo archivo que le enseña a abrir lo que escribió en MarsDawn para que lo revises, y a exportar PDF.</p>
<p>En un Mac con chip de Apple, Homebrew instala una copia precompilada en segundos, sin nada más que instalar. En un Mac con Intel, compila marsdawn desde el código fuente, lo que toma unos minutos y requiere Xcode 26 o posterior (Swift 6.2). La herramienta funciona en macOS 15 o posterior.</p>
<p>O compílala desde <a href="{k.KIT_URL}">el código fuente</a> con Swift Package Manager:</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Revisa qué versión tienes con <code>marsdawn --version</code>.</p>

<h2>Comandos</h2>

<h3>marsdawn open</h3>
<p>Abre uno o varios archivos Markdown en la app MarsDawn para que los revises. Necesita la app instalada: sin ella, <code>marsdawn open</code> termina con el código 3 e indica que MarsDawn no está instalado. <code>export</code> no necesita la app. La app está en el <a href="{k.LISTING_URL}">Mac App Store</a>.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code>: le pide a MarsDawn que vaya a esa línea. Una columna después, como en <code>notes.md:120:8</code>, se ignora. Si existe un archivo con el nombre completo, el argumento es ese archivo.</li>
  <li><code>--line &lt;n&gt;</code>: lo mismo para un solo archivo, y la manera de pedir una línea en una ruta que termina en dos puntos y dígitos. Requiere exactamente un archivo.</li>
  <li>Las líneas van de 1 a 999999999.</li>
  <li>MarsDawn 1.0 abre el archivo en esa línea.</li>
  <li>Una carpeta como argumento se abre en la barra lateral de la ventana en lugar de como documento: <code>marsdawn open .</code> muestra la carpeta actual. <code>--folder &lt;path&gt;</code> hace lo mismo junto con archivos. La barra lateral de una ventana muestra una carpeta, así que indicar dos es un error de uso.</li>
  <li><code>--background</code>: abrir sin traer MarsDawn al frente.</li>
  <li><code>--json</code>: mostrar un resultado JSON en lugar de texto.</li>
</ul>
<p>Las líneas llegaron con marsdawn 0.3.0, y las carpetas y <code>--background</code> con la 0.5.1.</p>

<h3>marsdawn export</h3>
<p>Convierte un archivo Markdown en un PDF paginado, con el mismo exportador que usa la exportación a PDF de MarsDawn. No necesita la app MarsDawn. Las imágenes relativas se resuelven a partir de la carpeta del archivo de entrada.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: dónde escribir el PDF. De forma predeterminada, la ruta de entrada con la extensión <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: la paleta clara del tema de la vista previa. De forma predeterminada, <code>$MARSDAWN_THEME</code> y, si no, <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: tamaño del papel. De forma predeterminada, <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: cargar imágenes de la web durante el renderizado. Desactivado de forma predeterminada.</li>
  <li><code>--force</code>: reemplazar el archivo de salida si ya existe.</li>
  <li><code>--json</code>: mostrar un resultado JSON en lugar de texto.</li>
</ul>

<h2>La variable $MARSDAWN_THEME</h2>
<p>Cuando no se pasa <code>--theme</code>, <code>export</code> lee la variable de entorno <code>$MARSDAWN_THEME</code>. Su valor debe ser <code>dawn</code>, <code>classic</code>, <code>modern</code> o <code>vivid</code>; cualquier otro vuelve a <code>dawn</code>. La CLI no lee el ajuste de tema de la propia app, porque leer el contenedor de otra app puede hacer que macOS muestre un aviso de privacidad.</p>

<h2>Sobrescribir archivos</h2>
<p><code>export</code> se niega a reemplazar un archivo de salida existente a menos que pases <code>--force</code>.</p>

<h2>Códigos de salida</h2>
<!--exit-table-->
<ul>
  <li><code>0</code>: éxito.</li>
  <li><code>2</code>: no se encontró la entrada.</li>
  <li><code>3</code>: MarsDawn no está instalado (solo <code>open</code>).</li>
  <li><code>4</code>: la salida ya existe (pasa <code>--force</code>).</li>
  <li><code>5</code>: falló la exportación.</li>
  <li><code>6</code>: este MarsDawn no puede mostrar una carpeta, así que no se abrió nada (solo <code>open</code>).</li>
  <li><code>64</code>: error de uso, incluidos una línea fuera de rango, <code>--line</code> con más de un archivo o con una carpeta, o más de una carpeta.</li>
</ul>

<h2>Salida --json</h2>
<p>Si todo sale bien, <code>marsdawn open --json</code> muestra <code>ok</code>, <code>opened</code> (una lista con el <code>path</code> de cada archivo, más <code>line</code> cuando se pidió una), <code>app</code> (la ruta de la app) y, cuando se indicó una carpeta, <code>folder</code>. <code>marsdawn export --json</code> muestra <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> y <code>diagramErrors</code>. Si algo falla, ambos muestran <code>ok</code>, <code>error</code> y <code>message</code>.</p>
""",
    }

    figures = {
        'index': {"alt": 'MarsDawn en vista dividida: el código Markdown a la izquierda y la página renderizada a la derecha.', "callouts": []},
        'yours': {"alt": 'MarsDawn muestra un documento con el tema Classic, con la vista previa ocupando toda la ventana.',
                  "callouts": ['Un archivo en tu Mac, guardado donde tú elijas.', 'Toda la barra de herramientas son temas y disposiciones; no hay nada en lo que iniciar sesión.']},
        'pay-once': {"alt": 'MarsDawn con el tema Vivid, con el código Markdown a la izquierda y la página renderizada a la derecha.',
                     "callouts": ['Resaltado de Markdown en el editor, incluido.', 'Todos los temas y todas las disposiciones están incluidos.', 'Diagramas Mermaid, incluidos.', 'Resaltado de código, incluido.']},
        'pdf': {"alt": 'Un PDF exportado desde MarsDawn, abierto en su visor de PDF con miniaturas de las páginas.',
                "callouts": ['Diagramas Mermaid, dibujados dentro del PDF.', 'El código conserva su resaltado.']},
        'native': {"alt": 'MarsDawn en vista dividida: el código Markdown a la izquierda y la página renderizada a la derecha.',
                   "callouts": ['Una ventana nativa de Mac.', 'El editor de texto del Mac, con resaltado de Markdown.', '⌘1 código, ⌘2 dividido, ⌘3 vista previa.', 'La página se actualiza mientras escribes.']},
        'limits': {"alt": 'MarsDawn en modo oscuro, con el código Markdown a la izquierda y la página renderizada a la derecha.',
                   "callouts": ['Un documento por ventana, en este Mac.', 'Aquí escribes Markdown.', 'La barra de herramientas tiene temas y disposiciones, y no hay menú de plugins.', 'La página es para leer, no para editar.']},
    }
    home = {
        "cta_cli": 'Instala la CLI gratuita',
        "cta_store": 'Ver en el Mac App Store',
        "install_h": 'Hazlo ahora',
        "install_lede": 'La herramienta de línea de comandos gratuita <code>marsdawn</code> ya está lista. Instálala con Homebrew:',
        "install_caps": [
            '<code>marsdawn export</code> convierte un archivo Markdown en un PDF, renderizado como la vista previa de MarsDawn. No necesita la app.',
            '<code>marsdawn open</code> abre archivos en la app MarsDawn para que los revises.',
            '<code>--json</code> les da a los scripts y a los agentes resultados que pueden analizar.',
        ],
        "proof_h": 'La app, tal como es',
    }
    compare_tables = {
        'pay-once-states': {
            "head": ['', 'Prueba (días 1 a 14)', 'Prueba terminada, sin desbloquear', 'Desbloqueado'],
            "rows": [
                ['Abrir un documento en MarsDawn', 'Sí', 'Se abre, con el contenido cubierto', 'Sí'],
                ['Leer y editar en MarsDawn (código, vista previa, Mermaid, fórmulas)', 'Sí', 'No', 'Sí'],
                ['Exportar como PDF e imprimir desde MarsDawn', 'Sí', 'No', 'Sí'],
                ['Conservar el texto escrito con Archivo ▸ Guardar como…', 'Sí', 'Sí, en una ventana abierta cuando terminó la prueba', 'Sí'],
                ['Acciones de Siri y Atajos', 'Sí', 'No', 'Sí'],
                ['Vista rápida en el Finder, con diagramas Mermaid y fórmulas', 'Sí', 'Sí, sin cambios', 'Sí'],
                ['<code>marsdawn export</code> (herramienta de línea de comandos gratuita): PDF con diagramas y fórmulas', 'Sí', 'Sí, sin cambios', 'Sí'],
                ['Tus archivos en el disco', 'Como los guardaste', 'Como los guardaste; el bloqueo nunca los cambia', 'Como los guardaste'],
            ],
        },
    }
    exit_table_head = ['Código', 'Significado', 'Qué hacer']
    exit_remedy = {
        "0": 'Con <code>--json</code>, lee la única línea JSON en stdout',
        "2": 'Revisa la ruta y el nombre del archivo',
        "3": 'Instala la app, o usa <code>export</code>, que no la necesita',
        "4": 'Pasa <code>--force</code> para reemplazarlo, o <code>-o</code> para escribir en otro lugar',
        "5": 'Lee <code>message</code> en el resultado JSON',
        "64": 'Corrige la opción o el valor; este error sale como texto en stderr, incluso con <code>--json</code>',
    }
    app_ui_languages = 'inglés, chino tradicional, chino simplificado, japonés, alemán, francés, español y coreano'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages,
    }
