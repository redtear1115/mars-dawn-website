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
        "description": 'Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.',
        "intro": """
<section class="intro">
  <h1>Hecho con las piezas del propio Mac.</h1>
  <p>Las ventanas, las pestañas, los menús y el editor de texto son los de la Mac. La página renderizada la dibuja WebKit, el motor detrás de Safari.</p>
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
<h3>El resto de la Mac</h3>
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
  <li><strong>iPhone y iPad:</strong> no hay app para ellos; MarsDawn es para la Mac.</li>
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

<div class="summary"><p><strong>marsdawn es gratis y se distribuye por separado del Mac App Store.</strong> Instálalo con Homebrew: en una Mac con chip de Apple llega listo para usar. <code>export</code> funciona por sí solo; <code>open</code> necesita la app MarsDawn.</p></div>

<p>¿Llamas a marsdawn desde un agente de IA o un script? Consulta <a href="/es/cli/agents/">marsdawn para agentes</a> para ver la salida JSON, sus esquemas y todos los códigos de salida, o <a href="/es/cli/mcp/">el servidor MCP</a> si tu agente llama a herramientas por MCP.</p>

<h2>Instalación</h2>
<p>Con <a href="https://brew.sh">Homebrew</a>:</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>¿Usas un agente de programación? <a href="/es/cli/skill/">Agrega la skill de marsdawn</a>: un solo archivo que le enseña a abrir lo que escribió en MarsDawn para que lo revises, y a exportar PDF.</p>
<p>En una Mac con chip de Apple, Homebrew instala una copia precompilada en segundos, sin nada más que instalar. En una Mac con Intel, compila marsdawn desde el código fuente, lo que toma unos minutos y requiere Xcode 26 o posterior (Swift 6.2). La herramienta funciona en macOS 15 o posterior.</p>
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
                   "callouts": ['Una ventana nativa de Mac.', 'El editor de texto de la Mac, con resaltado de Markdown.', '⌘1 código, ⌘2 dividido, ⌘3 vista previa.', 'La página se actualiza mientras escribes.']},
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
    # markdown-to-pdf shows /assets/cli/plan-es.png, which does not exist yet. Before this ships,
    # export example_plan with marsdawn 0.5.0 the way EXAMPLE_PLAN's comment in build_pages.py
    # describes, or fall back to plan-en.png with EXAMPLE_PLAN['en'].
    example_plan = '# Plan: exportaciones más rápidas\n\nUn agente escribió este plan. Tú lo revisas y luego lo conviertes en PDF.\n\n## Pasos\n\n| Paso | Responsable | Estado |\n|------|-------------|--------|\n| Medir las páginas lentas | Agente | Hecho |\n| Guardar en caché los diagramas renderizados | Agente | En revisión |\n\nEl objetivo es $t < 2\\,\\text{s}$ para un documento de 50 páginas:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Borrador --> Revisión --> Publicación\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'

    pages['markdown-to-pdf'] = {
        "title": 'Markdown a PDF en Mac, desde la línea de comandos · MarsDawn',
        "description": 'Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.',
        "body": f"""
<section class="intro">
  <h1>Markdown a PDF en Mac, desde la línea de comandos.</h1>
  <p>La herramienta gratuita <code>marsdawn</code> convierte un archivo Markdown en un PDF con un solo comando. Las tablas, las fórmulas, los diagramas Mermaid y el código resaltado salen tal como se leen en el código fuente, y no necesita nada más instalado, ni siquiera la app MarsDawn.</p>
</section>
<h2>Instálala</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>En una Mac con chip de Apple, Homebrew instala una copia precompilada en segundos. En una Mac con Intel, la compila desde el código fuente, lo que tarda unos minutos y requiere Xcode 26 o posterior. Funciona en macOS 15 o posterior, y <code>marsdawn --version</code> muestra la versión que instalaste.</p>
<h2>Guarda un documento</h2>
<p>Pega esto en un archivo llamado <code>plan.md</code>:</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>Expórtalo</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>Escribe <code>plan.pdf</code> junto al archivo fuente e indica dónde quedó:</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>Esta es esa página, capturada de una ejecución real de <code>marsdawn</code> 0.5.0:</p>
<p><img class="pdf-page" src="/assets/cli/plan-es.png" alt="El PDF exportado: el título, una tabla de pasos, una fórmula en línea y otra destacada, un diagrama Borrador, Revisión, Publicación y una línea de Swift resaltada." width="989" height="930"></p>
<h2>Elige un tema, un tamaño de papel y un nombre de archivo</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>: dawn, classic, modern o vivid, con los colores claros del tema. Sin esta opción, <code>export</code> usa <code>$MARSDAWN_THEME</code> y, si no existe, dawn.</li>
  <li><code>--paper</code>: a4 o letter. El valor predeterminado es a4.</li>
  <li><code>-o</code>: dónde escribir el PDF, en lugar de junto al archivo fuente.</li>
  <li><code>--allow-remote-images</code>: carga imágenes de la web durante el renderizado. Quedan desactivadas a menos que la indiques.</li>
</ul>
<h2>Si no funciona</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew está compilando <code>marsdawn</code> desde el código fuente, como hace en una Mac con Intel. Instala Xcode 26 o posterior desde el App Store y vuelve a ejecutar la instalación.</li>
  <li><code>marsdawn: No such file: …</code> La ruta no apunta a un archivo. Revisa el nombre o ejecuta el comando desde la carpeta donde está el archivo.</li>
  <li><code>… already exists. Pass --force to replace it.</code> Ya existe un PDF con ese nombre. Agrega <code>--force</code> para reemplazarlo, u <code>-o</code> para escribirlo en otro lugar.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> No reconoce el tema o el tamaño de papel. Los temas son dawn, classic, modern y vivid; el papel es a4 o letter.</li>
</ul>
<h2>Siguiente</h2>
<ul>
  <li>Todas las opciones y el JSON que imprime: <a href="/es/cli/">Línea de comandos</a>.</li>
  <li>Para que un agente de programación lo haga por ti: <a href="/es/cli/skill/">la skill de agente de marsdawn</a>.</li>
  <li>Los cuatro temas de vista previa y hacia dónde va la exportación a PDF: <a href="/es/themes/">temas de vista previa y exportación a PDF</a>.</li>
  <li>Entregar el PDF a alguien que no usa Markdown: <a href="/es/sharing-exported-pdfs/">compartir un PDF</a>.</li>
</ul>
""",
    }

    pages['view-markdown-on-mac'] = {
        "title": 'Cómo ver un archivo Markdown en Mac · MarsDawn',
        "description": 'Un archivo .md es texto plano con marcas de formato. Así puedes leerlo renderizado en Mac: como PDF con la herramienta de línea de comandos gratuita marsdawn desde hoy, y en la app MarsDawn, en el Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>Cómo ver un archivo Markdown en Mac.</h1>
  <p>Un archivo <code>.md</code> es texto plano. Los títulos, las palabras en negrita, las tablas y los diagramas están escritos como marcas: <code>#</code> para un título, <code>**</code> alrededor de la negrita, barras verticales para una tabla, un bloque de código <code>mermaid</code> para un diagrama. Si lo abres en un editor de texto plano, lees las marcas. Para leer la página como la pensó su autor, algo tiene que renderizarla.</p>
</section>
<h2>Hoy y gratis: conviértelo en PDF</h2>
<p>La herramienta de línea de comandos gratuita <code>marsdawn</code> renderiza un archivo Markdown como PDF, que cualquier Mac puede abrir. Las tablas, las fórmulas, los diagramas Mermaid y el código resaltado salen renderizados, y no necesita nada más instalado, ni siquiera la app MarsDawn.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> escribe <code>notes.pdf</code> junto al archivo Markdown, y <code>open</code> lo muestra en tu visor de PDF. Requiere macOS 15 o posterior. La guía paso a paso, con una página exportada real, está en <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</p>
<h2>Léelo en MarsDawn</h2>
<p>MarsDawn es un editor de Markdown para Mac, en el Mac App Store. Abre un archivo <code>.md</code> y lee la página renderizada junto al código fuente:</p>
<ul>
  <li>La vista previa se actualiza mientras escribes, y los dos paneles se desplazan juntos.</li>
  <li>Los diagramas de flujo y de secuencia de Mermaid se dibujan en la vista previa, y los bloques de código se resaltan.</li>
  <li>En el Finder, presiona la barra espaciadora sobre un archivo Markdown para verlo con Vista rápida, diagramas incluidos.</li>
  <li>Cuando quieras cambiar algo, el código fuente está ahí mismo. MarsDawn es un editor, no solo un visor.</li>
</ul>
<p>Si un agente de IA escribió el archivo, este es el ciclo para el que está hecho MarsDawn: el agente escribe, tú lo lees renderizado y el agente lo corrige. Consulta <a href="/es/">la página de inicio</a> y <a href="/es/cli/agents/">marsdawn para agentes</a> si quieres que un agente abra archivos por ti. Para saber por qué importa esa lectura y cómo revisar un plan, consulta <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a> y <a href="/es/reviewing-agent-plans/">Revisar el plan de un agente en cinco minutos</a>.</p>
<h2>Siguiente</h2>
<ul>
  <li>Todas las opciones de la herramienta de línea de comandos: <a href="/es/cli/">Línea de comandos</a>.</li>
  <li>Lo que MarsDawn no hace: <a href="/es/limits/">la lista</a>.</li>
  <li>Leer Markdown en VS Code, un navegador o Claude Desktop: <a href="/es/vs/markdown-preview-tools/">cómo se comparan</a>.</li>
</ul>
""",
    }

    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer vs. MarsDawn: un visor o un editor · MarsDawn',
        "description": 'MacMD Viewer muestra Markdown solo para lectura por 19,99 USD. MarsDawn edita y muestra la vista previa lado a lado: pruébalo gratis y luego paga 4,99 USD una sola vez en el Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer vs. MarsDawn.</h1>
  <p>Ambas son apps para Mac que sirven para leer Markdown renderizado. MacMD Viewer abre un archivo <code>.md</code> y muestra la página terminada; no permite editarla. MarsDawn pone un editor junto al mismo tipo de vista previa renderizada, para que escribas y revises en una sola ventana. Así se diferencian, función por función.</p>
</section>
<h2>Si solo necesitas leer, no editar</h2>
<p>Si tu trabajo consiste únicamente en leer Markdown que escribió otra persona y nunca necesitas tocar el código fuente, MacMD Viewer es una opción razonable: está hecho exactamente para eso, ya está disponible y funciona en versiones más antiguas de macOS. MarsDawn vale la pena cuando leer no es todo el trabajo, porque el Markdown de un agente suele volver para otra pasada.</p>
<h2>Qué hace cada app</h2>
<!--compare:macmd-features-->
<h2>Precio y forma de compra</h2>
<!--compare:macmd-buying-->
<h2>Pruébalo hoy, gratis</h2>
<p>MarsDawn está en el Mac App Store. La herramienta de línea de comandos gratuita <code>marsdawn</code> también renderiza cualquier archivo Markdown como PDF, con diagramas Mermaid y código resaltado, y no necesita nada más instalado:</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Siguiente</h2>
<ul>
  <li>La guía completa: <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</li>
  <li>Lo que MarsDawn no hace: <a href="/es/limits/">la lista</a>.</li>
  <li>Todas las opciones de la herramienta de línea de comandos: <a href="/es/cli/">Línea de comandos</a>.</li>
  <li>Comparado con leer Markdown en VS Code, un navegador o Claude Desktop: <a href="/es/vs/markdown-preview-tools/">cómo se comparan</a>.</li>
</ul>
""",
    }

    compare_tables['macmd-features'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Edición', 'Solo lectura, por diseño', 'Edita el código fuente, con la página renderizada al lado'],
            ['Temas de vista previa', '12 temas de documento', '4 temas, cada uno con una paleta clara y una oscura'],
            ['Diagramas y matemáticas', 'Mermaid y resaltado de código; su ficha no menciona matemáticas', 'Mermaid, resaltado de código y matemáticas con KaTeX'],
            ['Vista rápida en el Finder', 'Sí', 'Sí'],
            ['PDF e impresión', 'Sí', 'Sí'],
            ['Requisitos', 'macOS 14 (Sonoma) o posterior', 'macOS 26 (Tahoe) o posterior'],
            ['Idiomas de la interfaz', 'No se indica en sus propios materiales', '{langs}'],
        ],
    }
    compare_tables['macmd-buying'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Dónde se compra', 'Su propio sitio, Homebrew o Setapp; no en el Mac App Store', 'Solo en el Mac App Store'],
            ['Precio', '19,99 USD una sola vez, para una Mac; los paquetes para varias Mac cuestan más', 'Descarga gratuita y luego 4,99 USD una sola vez'],
            ['Probarlo primero', 'Sin prueba; garantía de reembolso de 14 días en compras directas', 'Una prueba gratuita de 14 días'],
            ['Reembolsos y actualizaciones', 'A través de su propio sitio', 'A través de Apple'],
            ['Cuenta necesaria', 'No', 'No'],
        ],
    }

    schema_notes = {
        "export": "éxito de export",
        "open": "éxito de open, marsdawn 0.5.1 y posterior, incluida una carpeta mostrada en la barra lateral",
        "open_v2": "éxito de open, marsdawn 0.3.0 a 0.5.0",
        "error": "error, ambos comandos, marsdawn 0.5.2 y posterior",
        "open_v1": "éxito de open, marsdawn 0.2.x, donde <code>opened</code> era una lista de rutas",
        "error_v1": "error, ambos comandos, marsdawn 0.5.1 y anterior",
    }

    pages['cli/agents'] = {
        "title": 'marsdawn para agentes: Markdown a PDF desde scripts · MarsDawn',
        "description": 'Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.',
        "body": f"""
<section class="intro">
  <h1>marsdawn para agentes</h1>
  <p>Una referencia para agentes de IA y scripts que llaman a la herramienta de línea de comandos <code>marsdawn</code>. Cada ejemplo de esta página se ejecutó con la herramienta compilada desde el código fuente actual.</p>
</section>

<div class="summary"><p><strong>Para convertir un archivo Markdown en PDF, ejecuta <code>marsdawn export notes.md --json</code> y lee un objeto JSON de stdout.</strong> Los diagramas Mermaid y el código resaltado se renderizan igual que en la app MarsDawn. <code>export</code> no necesita la app; <code>open</code>, sí.</p></div>

<h2>Qué hace</h2>
<ul>
  <li><code>export</code> renderiza un archivo Markdown como un PDF paginado, con el mismo exportador que la app MarsDawn. No se abre ninguna ventana.</li>
  <li><code>open</code> abre uno o varios archivos Markdown en la app MarsDawn para que una persona los revise; puede indicar la línea en la que debe abrirse cada archivo y mostrar una carpeta en la barra lateral de la ventana.</li>
</ul>

<h2>Qué no hace</h2>
<ul>
  <li>No lee Markdown desde stdin. Pasa una ruta de archivo.</li>
  <li>No escribe el PDF en stdout. El PDF siempre va a un archivo; stdout solo lleva el resultado.</li>
  <li>No reemplaza un archivo existente a menos que pases <code>--force</code>.</li>
  <li>No carga imágenes de la web a menos que pases <code>--allow-remote-images</code>, y en ese caso solo por https.</li>
  <li><code>open</code> no funciona si la app MarsDawn no está instalada; termina con el código 3. <code>export</code> no necesita la app. La app está en el <a href="{k.LISTING_URL}">Mac App Store</a>.</li>
  <li>MarsDawn 1.0 abre el archivo en la línea que indica <code>open</code>.</li>
  <li>Solo funciona en macOS.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Escribe <code>notes.pdf</code> junto a <code>notes.md</code>. Opciones:</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: dónde escribir el PDF. De forma predeterminada, la ruta de entrada con la extensión <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: la paleta clara del tema. De forma predeterminada, <code>$MARSDAWN_THEME</code> y, si no, <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: tamaño de papel. De forma predeterminada, <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: carga imágenes https de la web durante el renderizado.</li>
  <li><code>--force</code>: reemplaza el archivo de salida si existe.</li>
  <li><code>--json</code>: imprime un objeto JSON en stdout en lugar de texto.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Éxito, código de salida 0:</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>: ruta absoluta del PDF que se escribió.</li>
  <li><code>pages</code>: número de páginas.</li>
  <li><code>theme</code> y <code>paper</code>: los valores usados.</li>
  <li><code>diagramErrors</code>: un mensaje por cada diagrama Mermaid que no se pudo renderizar. El PDF se escribe de todos modos.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> indica la línea en la que abrir. Una columna después, como en <code>notes.md:120:8</code>, se ignora. Un argumento que nombra un archivo existente siempre es ese nombre de archivo completo, así que un archivo llamado <code>weird:12</code> se abre tal cual.</li>
  <li><code>--line &lt;n&gt;</code> indica la línea para un solo archivo, incluida una ruta que termina en dos puntos y dígitos. Necesita exactamente un archivo.</li>
  <li>Las líneas van de 1 a 999999999. Cualquier otro valor es un error de uso.</li>
  <li>Las líneas se agregaron en marsdawn 0.3.0. MarsDawn 1.0 abre el archivo en esa línea.</li>
  <li>Una carpeta como argumento se abre en la barra lateral de la ventana en lugar de como documento, así que <code>marsdawn open .</code> muestra la carpeta actual; <code>--folder &lt;path&gt;</code> hace lo mismo junto con archivos. La barra lateral de una ventana muestra una sola carpeta: indicar dos es un error de uso, igual que usar <code>--folder</code> dos veces, aunque sea para la misma carpeta; la misma carpeta repetida como argumento cuenta una vez. <code>--line</code> con una carpeta es un error de uso, porque una carpeta no tiene líneas. No existe <code>-a</code>: pasarlo es un error de uso que remite a <code>--folder</code>.</li>
  <li><code>--background</code> abre sin traer MarsDawn al frente, para un agente que abre archivos mientras la persona trabaja en otra cosa. El JSON es el mismo en ambos casos.</li>
  <li>Las carpetas y <code>--background</code> se agregaron en marsdawn 0.5.1.</li>
</ul>
<p>Éxito, código de salida 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>: un objeto por archivo, en el orden dado. <code>path</code> es la ruta absoluta del archivo; <code>line</code> solo aparece cuando se pidió una línea.</li>
  <li><code>app</code>: ruta de la app MarsDawn que los abrió.</li>
</ul>
<p>Con una carpeta (marsdawn 0.5.1 y posterior), código de salida 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code>: solo aparece cuando se dio una carpeta. <code>path</code> es su ruta absoluta. <code>requested</code> siempre es <code>true</code>: marsdawn le pidió a MarsDawn que mostrara la carpeta y no puede saber si la barra lateral la muestra, porque la app puede pedirle acceso a la persona primero. Infórmalo como solicitado, no como hecho.</li>
  <li><code>opened</code> está vacío cuando solo se dio una carpeta.</li>
</ul>
<p>marsdawn 0.2.x imprimía <code>opened</code> como una lista de rutas en texto. Revisa <code>marsdawn --version</code> si necesitas manejar ambos casos.</p>

<h2>Abrir archivos mientras Claude Code los edita</h2>
<p>Un <a href="https://code.claude.com/docs/en/hooks">hook de Claude Code</a> opcional: después de que Claude escribe o edita un archivo Markdown, lo abre en MarsDawn en segundo plano, una vez por archivo y por sesión. Está desactivado hasta que lo agregas, proyecto por proyecto, porque una ventana que no pediste se lleva tu atención. Ejecuta un comando de shell y no gasta tokens del modelo.</p>
<p>Necesita marsdawn 0.5.1 o posterior, por <code>--background</code>, y la app MarsDawn.</p>
<p>Guarda esto como <code>.claude/hooks/marsdawn-open.sh</code> en tu proyecto y hazlo ejecutable con <code>chmod +x</code>:</p>
<pre><code>#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2&gt;/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2&gt;/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || {{ [ -x /opt/homebrew/bin/marsdawn ] &amp;&amp; echo /opt/homebrew/bin/marsdawn; }}) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${{TMPDIR:-/tmp}}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2&gt;/dev/null &amp;&amp; exit 0
echo "$file" &gt;&gt; "$seen"

"$marsdawn" open --background "$file" &gt;/dev/null 2&gt;&amp;1 || true
exit 0</code></pre>
<p>Luego agrega el hook a <code>.claude/settings.json</code> en el proyecto, o a <code>.claude/settings.local.json</code> para que sea solo tuyo:</p>
<pre><code>{{
  "hooks": {{
    "PostToolUse": [
      {{
        "matcher": "Write|Edit",
        "hooks": [
          {{ "type": "command", "command": "\\"$CLAUDE_PROJECT_DIR\\"/.claude/hooks/marsdawn-open.sh" }}
        ]
      }}
    ]
  }}
}}</code></pre>
<ul>
  <li>Se ejecuta después de las herramientas Write y Edit de Claude. Los archivos que no terminan en <code>.md</code> o <code>.markdown</code> no se tocan.</li>
  <li>Cada archivo se abre una vez por sesión de Claude Code, sin importar cuántas veces Claude lo edite. La lista vive en <code>$TMPDIR/marsdawn-hook/</code>, un archivo por sesión, así que una sesión nueva vuelve a abrir el archivo.</li>
  <li><code>--background</code> evita que MarsDawn pase al frente: la ventana en la que trabajabas conserva el foco.</li>
  <li>Nunca le estorba a Claude. Cada ruta termina con 0, y si marsdawn o la app MarsDawn no están instalados, no pasa nada.</li>
  <li>Lee la entrada del hook con <code>/usr/bin/jq</code>, que viene con macOS 26, la versión que necesita la app MarsDawn.</li>
  <li>Para desactivarlo, quita la entrada del archivo de configuración.</li>
</ul>

<h2>Errores</h2>
<p>Con <code>--json</code>, un error imprime un objeto JSON en stdout y termina con su código:</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code>: la entrada no existe, es una carpeta o no es texto UTF-8; o una ruta de <code>--folder</code> no existe o no es una carpeta.</li>
  <li><code>3</code>, <code>app_not_installed</code>: MarsDawn no está instalado. Solo <code>open</code> devuelve este código.</li>
  <li><code>4</code>, <code>output_exists</code>: el archivo de salida existe. Pasa <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code>: la exportación en sí falló.</li>
  <li><code>6</code>, <code>app_cannot_open_folders</code>: esta versión de MarsDawn no puede mostrar una carpeta, así que no se abrió nada. Solo <code>open</code> devuelve este código.</li>
  <li><code>64</code>: error de uso, como una opción desconocida, un valor no válido, una línea fuera de rango, <code>--line</code> con más de un archivo o con una carpeta, más de una carpeta o <code>-a</code>. Este se imprime como texto en stderr, incluso con <code>--json</code>.</li>
</ul>

<h2>Esquemas JSON</h2>
<p>JSON Schema (draft 2020-12) para cada resultado de <code>--json</code>:</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>Variables de entorno</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>: el tema que usa <code>export</code> cuando no se pasa <code>--theme</code>. Un valor desconocido vuelve a <code>dawn</code> sin error.</li>
</ul>

<h2>Requisitos</h2>
<ul>
  <li>La herramienta funciona en macOS 15 o posterior. En chips de Apple, Homebrew instala un bottle precompilado y no se necesita nada más. Compilarla tú mismo, en una Mac con Intel o desde el código fuente, requiere Swift 6.2 o posterior, que viene con Xcode 26 o posterior.</li>
  <li>La app MarsDawn requiere macOS 26 o posterior.</li>
</ul>

<h2>Instalación</h2>
<p>Con Homebrew. En chips de Apple instala un bottle precompilado en segundos, sin necesidad de Xcode. En una Mac con Intel compila marsdawn desde el código fuente, lo que tarda unos minutos y requiere Xcode 26 o posterior.</p>
<pre><code>brew tap redtear1115/tap && brew install marsdawn
marsdawn --version</code></pre>
<p>O compílala desde <a href="{k.KIT_URL}">el código fuente</a>. La primera compilación descarga las dependencias y compila, lo que también tarda unos minutos.</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> imprime el número de versión, como <code>0.3.0</code>, y termina con el código 0.</p>

<h2>Siguiente</h2>
<ul>
  <li>Una skill de un solo archivo para agentes que leen instrucciones en lugar de usar una shell: <a href="/es/cli/skill/">la skill de marsdawn</a>.</li>
  <li>Un servidor MCP que envuelve este mismo <code>export</code>: <a href="/es/cli/mcp/">marsdawn-mcp</a>.</li>
  <li>Por qué este resultado JSON sale barato para el contexto del propio agente: <a href="/es/token-efficient-review/">revisión con pocos tokens</a>.</li>
</ul>
""",
    }

    pages['cli/skill'] = {
        "title": 'Una skill de agente de programación para pasar Markdown a PDF · MarsDawn',
        "description": 'Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.',
        "body": f"""
<section class="intro">
  <h1>Deja que tu agente te muestre lo que escribió y genere el PDF.</h1>
  <p>Esta skill es un archivo Markdown. Le enseña a un agente de programación a abrir en MarsDawn un documento que escribió para que lo revises, y a instalar <code>marsdawn</code>, comprobar que funciona, exportar un documento a PDF y leer el resultado.</p>
</section>
<div class="summary"><p><strong>Un archivo Markdown, en <code>~/.claude/skills/marsdawn/SKILL.md</code>.</strong> Con él, tu agente instala <code>marsdawn</code>, exporta a PDF y lee el resultado JSON, y aun así pregunta antes de ejecutar cualquier cosa.</p></div>
<h2>Instálala en Claude Code</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code la carga cuando una tarea pide un PDF, o cuando escribió o revisó un documento Markdown para que lo leas, y tú puedes ejecutarla con <code>/marsdawn</code>. Es <a href="/cli/skill/SKILL.md">un archivo corto</a>, así que léelo antes de instalarlo.</p>
<p>Otros agentes pueden usar el mismo archivo. Es Markdown simple, instrucciones y comandos, así que indícale la URL a tu agente o pega el contenido.</p>
<h2>Qué enseña</h2>
<ul>
  <li>Instalar <code>marsdawn</code> con Homebrew si falta y luego comprobarlo con <code>marsdawn --version</code> en lugar de suponer una versión.</li>
  <li>Exportar con <code>marsdawn export … --json</code> y leer el resultado: dónde quedó el PDF, cuántas páginas tiene y qué diagrama Mermaid no se pudo renderizar.</li>
  <li>Distinguir los errores por el código de salida: el archivo no existe, ya hay un PDF, la exportación falló, una opción no es válida.</li>
  <li>Abrir un documento que escribió con <code>marsdawn open file.md:line</code>, en su primer cambio, y solo una vez: los cambios posteriores aparecen solos en la ventana abierta.</li>
  <li>Si la app MarsDawn no está instalada, decirlo una vez y seguir, sin reintentar. Nunca usar <code>open</code> para generar un PDF.</li>
  <li>Con <code>--folder</code> (marsdawn 0.5.1 y posterior), informar la carpeta como solicitada, no como mostrada: la app decide y nada lo confirma.</li>
</ul>
<h2>Qué no hace</h2>
<ul>
  <li>No se da permiso a sí misma para ejecutar nada. Tu agente sigue preguntando antes de instalar <code>marsdawn</code> o ejecutarlo, como con cualquier otro comando.</li>
  <li>No envía tus documentos a ningún lado. <code>marsdawn</code> renderiza en tu Mac y omite las imágenes de la web a menos que pases <code>--allow-remote-images</code>.</li>
</ul>
<p>El contrato completo, cada campo y cada código, está en <a href="/es/cli/agents/">marsdawn para agentes</a>. Para un agente que llama a herramientas por MCP en lugar de leer un archivo de skill, también hay <a href="/es/cli/mcp/">un servidor MCP</a>.</p>
""",
    }

    pages['cli/mcp'] = {
        "title": 'Tres formas de llamar a marsdawn: CLI, archivo de skill, servidor MCP · MarsDawn',
        "description": 'marsdawn no tiene un modelo de IA propio, así que no importa qué agente escribió el Markdown. Llámalo desde la CLI, un archivo de skill o el servidor MCP marsdawn-mcp: los tres ejecutan la misma exportación.',
        "body": f"""
<section class="intro">
  <h1>Tres formas de llamar a marsdawn.</h1>
  <p>MarsDawn no tiene un modelo de IA propio: está hecho para revisar Markdown, no para escribirlo, así que no importa qué agente o modelo generó el archivo. Hay tres formas de que un agente o un script llame a <code>marsdawn</code>, y las tres terminan ejecutando el mismo <code>export</code>.</p>
</section>

<div class="summary"><p><strong>Elige la que admitan tus herramientas: la CLI gratuita <code>marsdawn</code>, un archivo de skill en Markdown simple o el servidor MCP <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>.</strong> Los tres llaman al mismo <code>marsdawn export</code> y devuelven el mismo resultado JSON.</p></div>

<h2>Cuál usar</h2>
<!--compare:mcp-choice-->

<h2>La CLI</h2>
<p><code>marsdawn export notes.md --json</code> lo puede llamar cualquier agente o script capaz de ejecutar un comando de shell, así que no depende de ningún modelo. Cada campo que devuelve está documentado en <a href="/es/cli/agents/">marsdawn para agentes</a>, la fuente de referencia del esquema JSON a la que remiten las otras dos opciones de abajo.</p>

<h2>El archivo de skill</h2>
<p>Para un agente que lee instrucciones en Markdown simple en lugar de llamar directamente a una shell (hoy, Claude Code), <a href="/es/cli/skill/">la skill de marsdawn</a> es un archivo que le enseña a instalar marsdawn, ejecutar <code>export</code> y leer el resultado. Es Markdown simple, así que otros agentes que cargan archivos de instrucciones pueden usar el mismo.</p>

<h2>El servidor MCP</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> es un repositorio aparte, público y con licencia Apache-2.0. Es un servidor MCP con dos herramientas, <code>export_markdown_to_pdf</code> y <code>open_in_marsdawn</code>, que envuelven <code>marsdawn export --json</code> y <code>marsdawn open --json</code>: apunta un cliente MCP hacia él y una llamada a una herramienta devuelve el mismo JSON que la CLI.</p>
<ul>
  <li><strong>Dónde obtenerlo:</strong> como MCP Bundle, <code>marsdawn.mcpb</code>, adjunto a <a href="https://github.com/redtear1115/marsdawn-mcp/releases">su release de GitHub</a>, o ejecutando el servidor desde el código fuente por stdio.</li>
  <li><strong>Registro:</strong> todavía no aparece en el MCP Registry (versión actual: 0.2.1). Revisa el estado actual en el repositorio antes de depender del descubrimiento por el registro.</li>
  <li><strong>Alojamiento:</strong> solo autoalojado. No existe un servicio de marsdawn-mcp alojado; el servidor se ejecuta en tu propia máquina, junto a marsdawn.</li>
  <li><strong>Requisitos:</strong> macOS, marsdawn 0.5.0 o posterior y Node.js 20 o posterior para ejecutar el servidor.</li>
</ul>

<h2>Limitado a las carpetas que permitas</h2>
<p>Las dos herramientas solo acceden a las carpetas que permitas: el ajuste <strong>Allowed folders</strong> de la extensión, que empieza vacío y sin valores predefinidos, o bien las raíces que ofrece tu cliente MCP. Si no hay ninguno de los dos, se rechaza cada llamada, y el mensaje de rechazo explica cómo solucionarlo. Cada ruta tiene que ser absoluta, y <code>export_markdown_to_pdf</code> solo escribe un archivo <code>.pdf</code>, nunca a través de un enlace simbólico.</p>
<p><strong>Seguridad:</strong> actualiza a <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>. Las versiones 0.1.0 y 0.2.0 permitían que una llamada escribiera un PDF en cualquier ruta en la que tu cuenta pudiera escribir; se corrigió como <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a>.</p>

<h2>La misma exportación, tres puertas</h2>
<p>Sea cual sea la vía que lo llame, el comportamiento de fondo no cambia: el mismo exportador, los mismos temas y tamaños de papel, los mismos <code>diagramErrors</code> cuando un diagrama Mermaid no se puede renderizar. Esta página no repite ese contrato; <a href="/es/cli/agents/">marsdawn para agentes</a> lo describe completo.</p>

<h2>Siguiente</h2>
<ul>
  <li>El esquema JSON completo y cada código de salida: <a href="/es/cli/agents/">marsdawn para agentes</a>.</li>
  <li>La skill de un solo archivo para Claude Code y agentes similares: <a href="/es/cli/skill/">la skill de marsdawn</a>.</li>
  <li>Por qué un resultado JSON compacto importa para el contexto de tu agente: <a href="/es/token-efficient-review/">revisión con pocos tokens</a>.</li>
</ul>
""",
    }

    pages['vs/markdown-preview-tools'] = {
        "title": 'Ver Markdown en otras herramientas o en MarsDawn · MarsDawn',
        "description": 'Cómo se compara MarsDawn con leer Markdown en la vista previa integrada de VS Code, una extensión del navegador o la vista previa de archivos de Claude Desktop: qué renderiza cada uno y qué hace falta para abrir un archivo.',
        "body": f"""
<section class="intro">
  <h1>Ver Markdown en otras herramientas, o en MarsDawn.</h1>
  <p>Si ya tienes abierto VS Code, un navegador o Claude Desktop, es razonable usarlos para echar un vistazo a un archivo Markdown. Esto es lo que cada uno renderiza de verdad, y lo que cuesta llegar ahí, comparado con abrir el mismo archivo en MarsDawn.</p>
</section>

<h2>De un vistazo</h2>
<!--compare:preview-tools-->

<h2>La vista previa integrada de VS Code</h2>
<p>Presiona <kbd>&#8984;&#8679;V</kbd> en VS Code y renderiza el archivo Markdown en un panel de vista previa integrado, gratis y sin instalar nada. Desde VS Code 1.121 (mayo de 2026), esa vista previa también renderiza diagramas Mermaid de forma nativa: Microsoft incorporó una extensión de Mermaid a VS Code, así que lo que antes necesitaba una extensión aparte ya no la necesita. Lo que no hace: es un panel de vista previa dentro de un editor, no un editor hecho para leer. El panel convive con un árbol de archivos, una terminal y cualquier otro panel que VS Code pueda mostrar, y VS Code en sí es una app de Electron que instalas como un entorno de desarrollo completo, no algo que abres para leer un archivo.</p>

<h2>Una extensión del navegador para archivos locales</h2>
<p>Ninguna extensión del navegador domina a la hora de leer un archivo <code>.md</code> local: Local Markdown Viewer, Markdown Viewer, MarkView y otras hacen más o menos lo mismo, y ninguna viene de forma predeterminada. Todas necesitan el mismo paso adicional antes de poder abrir algo: activar «Permitir el acceso a las URL de archivo» para esa extensión, porque los navegadores impiden de forma predeterminada que las extensiones lean páginas <code>file://</code>. Es un permiso que das una vez por extensión, y es fácil olvidar que lo diste, o por qué. Una vez activado, el archivo se renderiza en una pestaña del navegador, lo que significa tener un navegador completo en marcha para ver un archivo.</p>

<h2>La vista previa de archivos de Claude Desktop</h2>
<p>Claude Desktop muestra un archivo que ya está en un proyecto o en una conversación. Para lo que no está hecho es para explorar archivos cualesquiera del disco: lo que puedes ver es lo que la conversación ya contiene, no una carpeta de notas que tienes abierta junto a tu trabajo. La propia lista de Anthropic de <a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">los tipos de documentos que puedes subir</a> incluye PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON y XLSX: Markdown no está.</p>

<h2>Un motor de navegador para leer un archivo</h2>
<p>VS Code es una app de Electron: un Chromium y un entorno de Node.js integrados, no una app nativa para Mac. La vía de la extensión del navegador se ejecuta dentro de un navegador de verdad. En los dos casos, ver un archivo Markdown significa tener en marcha un motor de navegador completo. MarsDawn es una app nativa de AppKit: sin un navegador integrado, abre cualquier archivo local directamente, sin extensiones que instalar ni permisos que recordar.</p>

<h2>Siguiente</h2>
<ul>
  <li>Lo que MarsDawn tampoco hace: <a href="/es/limits/">la lista</a>.</li>
  <li>Convierte cualquier archivo Markdown en PDF hoy, gratis: <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</li>
  <li>Comparado con un visor nativo para Mac: <a href="/es/vs/macmd-viewer/">MacMD Viewer vs. MarsDawn</a>.</li>
</ul>
""",
    }

    pages['themes'] = {
        "title": 'Temas de vista previa y exportación a PDF en MarsDawn · MarsDawn',
        "description": 'Cuatro temas de vista previa, cada uno con una paleta clara y una oscura, y una sola exportación a PDF e impresión que respeta el que estés usando. Están previstos más temas importables y una galería para compartir los tuyos.',
        "body": f"""
<section class="intro">
  <h1>Ocho estilos, una exportación.</h1>
  <p>MarsDawn incluye cuatro temas de vista previa, Dawn, Classic, Modern y Vivid, cada uno con una paleta clara y una oscura: ocho combinaciones para leer un documento. Exporta a PDF o imprime, y la página sale con la que estabas leyendo.</p>
</section>

<div class="summary"><p><strong>Cuatro temas &#215; claro y oscuro = ocho formas de leer un documento, y una sola vía de exportación que respeta lo que elegiste.</strong> Están previstos más temas importables y una galería para compartir los tuyos; todavía no existen.</p></div>

<h2>Los cuatro temas</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Dawn</strong>, el predeterminado: el mismo papel cálido y el mismo acento Mars Rust con los que está hecho este sitio.</li>
  <li><strong>Classic</strong>: una paleta más sobria, de documento.</li>
  <li><strong>Modern</strong>: una paleta más fría y actual.</li>
  <li><strong>Vivid</strong>: una paleta más brillante y de mayor contraste.</li>
</ul>
<p>Cada uno tiene su propia variante clara y oscura, así que al cambiar el aspecto de tu Mac cambia también la paleta del tema, no solo la interfaz que la rodea.</p>

<h2>La exportación a PDF y la impresión usan el mismo tema</h2>
<p>Exporta a PDF o imprime, y la página usa la paleta clara de tu tema: los diagramas Mermaid se dibujan en ella, los bloques de código conservan el resaltado de sintaxis, y los saltos de página evitan separar un título de su sección o partir una tabla o un diagrama por la mitad. La <a href="/es/cli/">herramienta de línea de comandos marsdawn</a>, gratuita, usa el mismo exportador, así que un script o un agente genera el mismo PDF, en cualquiera de los cuatro temas, con <code>--theme</code>.</p>

<h2>Previsto: más temas y una galería</h2>
<p>Llegará más adelante, todavía no está disponible: más temas de vista previa importables y una galería en este sitio donde la gente pueda enviar los suyos. <code>/themes/v1/</code> ya está reservado para eso. Hasta entonces, MarsDawn tiene los cuatro temas integrados, y no puedes instalar otros.</p>

<h2>Siguiente</h2>
<ul>
  <li>La guía completa de exportación a PDF, desde la línea de comandos: <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</li>
  <li>Lo que MarsDawn todavía no hace: <a href="/es/limits/">la lista</a>.</li>
  <li>Entregar un PDF exportado a alguien que no usa Markdown: <a href="/es/sharing-exported-pdfs/">compartir un PDF</a>.</li>
</ul>
""",
    }

    compare_tables['mcp-choice'] = {
        'head': ['Si tu agente', 'Usa', 'Necesita'],
        'rows': [
            ['Puede ejecutar un comando de shell', '<a href="{root}cli/agents/">La CLI</a>', 'macOS 15 o posterior'],
            ['Carga archivos de instrucciones, como Claude Code', '<a href="{root}cli/skill/">El archivo de skill</a>', 'La CLI, que la skill instala'],
            ['Llama a herramientas por MCP', '<a href="{mcp}">marsdawn-mcp</a>', 'marsdawn-mcp 0.2.1 o posterior, marsdawn 0.5.0 o posterior y Node.js 20 o posterior'],
        ],
    }
    compare_tables['preview-tools'] = {
        'head': ['', 'Vista previa de VS Code', 'Extensión del navegador', 'Claude Desktop', 'MarsDawn'],
        'rows': [
            ['Abre un archivo Markdown del disco', 'Sí', 'Sí, después de permitir el acceso a archivos', 'No: Markdown no está en su lista de archivos admitidos', 'Sí'],
            ['Antes del primer archivo', 'Instalar VS Code, un entorno de desarrollo completo', 'Instalar una extensión y activar «Permitir el acceso a las URL de archivo»', 'No puede explorar archivos del disco', 'Instalar MarsDawn'],
            ['Hecho para', 'Escribir código; la vista previa es un panel entre muchos', 'Navegar por la web', 'Conversar con Claude', 'Leer y editar Markdown'],
            ['Dibuja la página con', 'Electron: un Chromium y Node.js integrados', 'Un navegador completo', 'La app Claude Desktop', 'Una app nativa de AppKit; WebKit dibuja la página'],
        ],
    }
    theme_shots = {
        '01-split': ('Dawn (predeterminado)', 'El tema Dawn en vista dividida: el código Markdown a la izquierda y la página renderizada a la derecha.'),
        '02-classic': ('Classic', 'El tema Classic, con la vista previa ocupando toda la ventana.'),
        '04-vivid': ('Vivid', 'El tema Vivid en vista dividida.'),
        '03-dark': ('Modo oscuro', 'MarsDawn en modo oscuro, en vista dividida.'),
    }
    theme_gallery_note = 'Modern todavía no aparece en las imágenes; la cuarta muestra el modo oscuro en su lugar.'

    pages['token-efficient-review'] = {
        "title": 'Revisar lo que genera MarsDawn sin gastar los tokens de tu agente · MarsDawn',
        "description": 'Una persona revisa la página renderizada en MarsDawn, y nunca se vuelve a leer en el contexto del agente. La llamada a la herramienta devuelve un resultado JSON compacto, no el contenido renderizado, así que llamarla también sale barato.',
        "body": f"""
<section class="intro">
  <h1>Revisa sin gastar los tokens de tu agente.</h1>
  <p>En este ciclo hay dos cosas distintas que salen baratas: lo que el agente recibe al llamar a la herramienta y lo que hace falta para confirmar que el resultado está bien.</p>
</section>

<div class="summary"><p><strong>La llamada a la herramienta devuelve un objeto JSON pequeño, no la página renderizada, y la página renderizada la revisa una persona en MarsDawn; nunca se vuelve a leer en el contexto del agente.</strong></p></div>

<h2>La llamada a la herramienta sale barata</h2>
<p>Llama a <code>marsdawn export</code>, desde la CLI, la skill o <a href="/es/cli/mcp/">el servidor MCP</a>, y lo que vuelve es <a href="/es/cli/agents/">un objeto JSON compacto</a>: <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> y <code>diagramErrors</code>. El esquema completo es <a href="/schemas/cli/export.v1.json">export.v1.json</a>. Nada de eso es el documento renderizado. Un PDF de 50 páginas con una docena de diagramas Mermaid devuelve los mismos pocos campos que una nota de una página.</p>

<h2>La revisión ocurre aparte</h2>
<p>Cuando el PDF ya existe, una persona lo abre, en MarsDawn o en cualquier visor de PDF, y lee los diagramas, las fórmulas y el diseño ya renderizados. El agente nunca necesita volver a leer ese resultado en su propia ventana de contexto para confirmar que está bien: la revisión ocurre en otra ventana, en otra pantalla, no en otra ronda de tokens gastados en describir cómo se ve un diagrama.</p>

<h2>Lo que esto evita</h2>
<ul>
  <li>Pegar de nuevo en la conversación Markdown renderizado, una captura de pantalla o su descripción, solo para que el agente confirme que la exportación funcionó.</li>
  <li>Un agente que tiene que reconstruir cómo se ve un diagrama Mermaid o una fórmula KaTeX renderizados, en lugar de una persona que simplemente lo mira.</li>
  <li>Una segunda llamada a la herramienta para obtener el contenido del PDF cuando la primera ya informó que todo salió bien.</li>
</ul>

<h2>Siguiente</h2>
<ul>
  <li>Las tres formas de llamar a marsdawn, CLI, archivo de skill y servidor MCP: <a href="/es/cli/mcp/">tres puertas de entrada</a>.</li>
  <li>Cada campo del resultado JSON: <a href="/es/cli/agents/">marsdawn para agentes</a>.</li>
  <li>Por qué una persona todavía tiene que leer lo que escribió un agente: <a href="/es/reviewing-ai-output/">por qué revisar</a>.</li>
  <li>El argumento completo para leer lo que entrega un agente, con una lista de verificación: <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a>.</li>
</ul>
""",
    }

    pages['sharing-exported-pdfs'] = {
        "title": 'Comparte lo que escribió un agente sin enseñar Markdown · MarsDawn',
        "description": 'Exporta a PDF el Markdown de un agente y entrégaselo a un colega que no lee Markdown y no va a instalar nada. Para abrirlo no hace falta sintaxis, ni app, ni cuenta.',
        "body": f"""
<section class="intro">
  <h1>Entrégales el PDF, no el Markdown.</h1>
  <p>Un agente termina un documento, tú lo revisas y lo corriges, y luego alguien fuera del equipo técnico también tiene que leerlo: un gerente, un cliente, alguien de otro equipo. No necesitan saber qué significa <code>##</code> ni una tabla con barras verticales. Exporta a PDF y entrégales eso.</p>
</section>

<div class="summary"><p><strong>Exporta el documento revisado a PDF y envía ese archivo.</strong> Se abre en cualquier lado, no requiere saber Markdown ni instalar nada, y se ve como lo viste en la vista previa, con diagramas, tablas y formato incluidos.</p></div>

<h2>Por qué no enviar simplemente el archivo .md</h2>
<p>Un archivo <code>.md</code> sin procesar, abierto en un editor de texto plano, muestra las marcas, no la página: <code>#</code> para un título, <code>**</code> alrededor de la negrita, un bloque delimitado para un diagrama Mermaid que no se dibuja. Alguien que no escribe Markdown no lee nada de eso como se pensó, y pedirle que primero instale un visor es mucho pedir para un solo documento.</p>

<h2>Por qué no una captura de pantalla</h2>
<p>Una captura congela una pantalla de un documento que puede tener varias páginas, no se puede buscar ni seleccionar, y se lee peor después de comprimirla y reenviarla unas cuantas veces. Un PDF conserva intactos el texto, los diagramas y los saltos de página, sin importar la extensión.</p>

<h2>Lo que te da un PDF</h2>
<ul>
  <li>Se abre con lo que la otra persona ya tiene, Vista Previa, un navegador, Acrobat, su teléfono, sin necesidad de una herramienta de Markdown.</li>
  <li>Los diagramas Mermaid aparecen dibujados, no como código; los bloques de código conservan el resaltado.</li>
  <li>Los saltos de página se eligen para que un título no quede solo al pie de una página y para que una tabla o un diagrama no se parta en dos.</li>
  <li>El mismo archivo, venga de la app MarsDawn o de la línea de comandos gratuita; la guía paso a paso está en <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</li>
</ul>

<h2>Siguiente</h2>
<ul>
  <li>Los temas y diseños de los que puede salir la exportación: <a href="/es/themes/">temas de vista previa y exportación a PDF</a>.</li>
  <li>Exportar desde un script o un agente en lugar de la app: <a href="/es/cli/agents/">marsdawn para agentes</a>.</li>
  <li>Por qué una persona tiene que leer el documento primero: <a href="/es/reviewing-ai-output/">por qué revisar</a>.</li>
  <li>Las entregas entre varios agentes son una fuente natural de PDF para compartir: <a href="/es/agent-design-patterns/">Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno</a>.</li>
</ul>
""",
    }

    pages['reviewing-ai-output'] = {
        "title": 'Por qué lo que genera la IA todavía necesita un lector humano · MarsDawn',
        "description": 'El Markdown escrito por una IA tiene que entenderlo una persona, no creerlo a simple vista. MarsDawn pone la página renderizada junto al código fuente y dibuja diagramas Mermaid y fórmulas KaTeX, para que la estructura se lea de un vistazo.',
        "body": f"""
<section class="intro">
  <h1>Un agente lo escribe. Tú todavía tienes que entenderlo.</h1>
  <p>Un agente de IA puede redactar rápido un plan, una especificación o unas notas. Lo que produce todavía tiene que entenderlo la persona que va a actuar en consecuencia, no creerlo solo porque se lee con fluidez.</p>
</section>

<div class="summary"><p><strong>MarsDawn está hecho para esa lectura: la página renderizada junto al código fuente, con los diagramas Mermaid y las fórmulas KaTeX dibujados en lugar de quedar como marcas, para que la estructura de un documento se lea de un vistazo.</strong></p></div>

<h2>Fluido no es lo mismo que correcto</h2>
<p>Al escribir sobre la programación asistida por IA, Simon Willison lo dijo así sobre el código en el que se va a seguir trabajando, no el que se tira: «la calidad y la comprensibilidad del código subyacente son cruciales» (<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>, 2025). Lo mismo vale para un documento: el borrador de un agente que se lee sin tropiezos puede equivocarse en la estructura, en los números o en la lógica, y la prosa fluida no avisa qué partes hay que revisar.</p>

<h2>Inferencia, no compilación</h2>
<p>Birgitta Böckeler, en un texto para Thoughtworks, marca la diferencia sin rodeos: «los LLM NO son compiladores, intérpretes, transpiladores ni ensambladores del lenguaje natural, son inferidores» (<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>). Un compilador acepta tu entrada o informa un error; un agente puede devolver algo que se ejecuta, o que se lee, sin ser correcto. Alguien todavía tiene que revisarlo.</p>

<h2>Lo que MarsDawn le da a ese lector</h2>
<ul>
  <li>La página renderizada junto al código fuente, que se actualiza cuando cambia cualquiera de los dos lados, para tener a la vista a la vez una afirmación del texto y la forma en que está estructurada.</li>
  <li>Diagramas Mermaid dibujados: un diagrama de flujo que un agente describió en texto se convierte en una forma que de verdad puedes seguir.</li>
  <li>Fórmulas KaTeX renderizadas, no una tira de barras invertidas: una fórmula se lee como fórmula.</li>
  <li>Nada se ejecuta por su cuenta. MarsDawn no califica, no resume ni marca nada del documento por ti; pone la estructura frente a ti para que tú lo hagas.</li>
</ul>

<h2>Siguiente</h2>
<ul>
  <li>Cómo esa revisión sale barata para el contexto del propio agente: <a href="/es/token-efficient-review/">revisión con pocos tokens</a>.</li>
  <li>Entregar el documento revisado a otra persona: <a href="/es/sharing-exported-pdfs/">compartir un PDF</a>.</li>
  <li>Por qué cuesta leerlo y cómo hacerlo: <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a>.</li>
  <li>Por qué los agentes muestran sus planes: <a href="/es/agent-transparency/">Anthropic dice que los agentes deben ser transparentes. ¿Quién lee lo que muestran?</a></li>
  <li>Qué es MarsDawn, en una página: <a href="/es/">la página de inicio</a>.</li>
</ul>
""",
    }

    pages['reading-agent-output'] = {
        "title": 'Leer lo que te devuelve tu agente · MarsDawn',
        "description": 'Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.',
        "body": f"""
<section class="intro">
  <h1>El trabajo de tu agente vuelve como un archivo Markdown.</h1>
  <p>Le pides a un agente de programación que planifique una migración, escriba una especificación o persiga un bug. Trabaja solo un rato y luego te entrega un archivo: <code>plan.md</code>, <code>SPEC.md</code>, un informe de avance, un resumen de investigación. Hasta donde puedes comprobar el trabajo, ese archivo es el trabajo.</p>
</section>

<div class="summary"><p><strong>Si el agente lo hizo bien, lo averiguas leyendo lo que te entrega. MarsDawn es una app para Mac hecha para esa lectura.</strong></p></div>

<h2>Qué dicen quienes construyen agentes</h2>
<p>Citado tal como se escribió; nuestra lectura viene después.</p>
<ul>
  <li>«Building Effective Agents», de Anthropic (Erik S. y Barry Zhang, diciembre de 2024), propone tres principios básicos para construir agentes. Uno es «Prioriza la transparencia mostrando explícitamente los pasos de planificación del agente». Está escrito para quienes construyen agentes. Desde tu lado, esa transparencia es el plan que terminas leyendo.</li>
  <li>El mismo artículo: «Luego, los agentes pueden hacer una pausa para recibir comentarios humanos en puntos de control o cuando encuentran obstáculos». Fíjate en el verbo: <em>pueden</em>.</li>
  <li>Chip Huyen, en «Agents» (enero de 2025), sobre por qué la planificación debe estar separada de la ejecución: «Sin supervisión, un agente puede ejecutar esos pasos durante horas, desperdiciando tiempo y dinero en llamadas a la API, antes de que te des cuenta de que no va a ninguna parte». También describe un fallo en el que «el agente está convencido de que completó una tarea cuando no es así». Si le pides que aloje a 50 personas en 30 habitaciones de hotel, ubica a 40 e insiste en que terminó.</li>
  <li>Andrew Ng, sobre el patrón de diseño de planificación en The Batch (abril de 2024): «Por un lado, la planificación es una capacidad muy poderosa; por otro, produce resultados menos predecibles». Es una observación sobre la previsibilidad, no un llamado a la revisión humana, y él espera que la planificación mejore rápido.</li>
</ul>
<p><strong>Nuestra conclusión, no la de ellos:</strong> si un agente expone su plan y se detiene en puntos de control, alguien lee ese plan en el punto de control, y casi siempre eres tú. Si un agente puede creer que terminó cuando no es así, su informe de «listo» también necesita un lector. Ninguno de estos autores menciona MarsDawn ni lo recomienda, ni tampoco ninguna otra herramienta de Markdown.</p>

<h2>Por qué cuesta más leerlo de lo que parece</h2>
<p>El archivo es largo, y la parte que importa rara vez está arriba. Tiene diagramas Mermaid y fórmulas que cuesta seguir como código fuente. Puede que el agente lo siga reescribiendo cuando vas por la mitad. Suele ser uno de varios archivos, a veces repartidos entre ramas o worktrees. Y cuando encuentras un problema, «la parte del caché se ve rara» deja al agente adivinando; «<code>docs/plan.md:42</code> borra la tabla vieja antes de que termine el backfill», no.</p>

<h2>Dónde ayuda MarsDawn</h2>
<ul>
  <li><strong>Archivos largos:</strong> la pestaña Esquema de la barra lateral (&#8963;&#8984;S) lista los títulos. Haz clic en uno y los dos paneles saltan ahí.</li>
  <li><strong>Diagramas y fórmulas:</strong> Mermaid y KaTeX se dibujan en la vista previa junto al código fuente (&#8984;2), y los dos paneles se desplazan juntos.</li>
  <li><strong>Reescrito mientras lees:</strong> cuando el agente reescribe el archivo, MarsDawn lo vuelve a cargar y conserva tu posición, siempre que no tengas cambios propios sin guardar.</li>
  <li><strong>Varios archivos:</strong> abre la carpeta del agente con Archivo &#9656; Abrir carpeta&#8230; (&#8679;&#8984;O). Los archivos nuevos aparecen en la pestaña Archivos en aproximadamente un segundo y, en un checkout de git, el encabezado indica la rama o el worktree.</li>
  <li><strong>Comentarios exactos:</strong> Edición &#9656; Copiar referencia (&#8997;&#8984;C) copia tu posición como <code>docs/plan.md:42</code>. Copiar para IA (&#8963;&#8997;&#8984;C) agrega el texto seleccionado debajo. Pega cualquiera de los dos en el chat con el agente.</li>
</ul>
<p>Dos más para el ciclo: un agente puede ejecutar <code>marsdawn open plan.md:42</code> para abrir el archivo en MarsDawn en la línea 42, la que quiere que veas primero, y un archivo revisado se exporta a PDF desde la app o con el comando gratuito <code>marsdawn export</code>.</p>
<p>MarsDawn no tiene ningún modelo de IA dentro. No resume el plan, no lo califica ni te dice qué está mal. Tú lees; la app mantiene legible un archivo largo que cambia y te deja señalar la línea exacta.</p>

<h2>Revisar el plan de un agente en cinco minutos</h2>
<p>Esto funciona en cualquier editor.</p>
<ol>
  <li>Lee solo los títulos. ¿El esquema coincide con lo que pediste? Una sección que falta suele significar trabajo que falta.</li>
  <li>Busca cada lugar que diga que algo está hecho, que pasa o que se verificó, y comprueba uno tú mismo: abre el archivo, ejecuta la prueba, cuenta las filas.</li>
  <li>Busca pasos que no se pueden deshacer: borrar datos, migraciones, force-push, cualquier cosa que envíe, pague o publique. Esos esperan tu sí explícito.</li>
  <li>Lee los diagramas renderizados y compara cada flecha con el texto.</li>
  <li>Haz una lista de los archivos y sistemas que toca el plan. Pregunta por todo lo que no pediste antes de que se ejecute.</li>
  <li>Escribe los comentarios como lugar, problema, solución: «<code>plan.md:88</code>: el backfill se ejecuta después del borrado. Intercambia los pasos 4 y 5». Un problema por línea.</li>
</ol>
<p>¿Poco tiempo? Haz el paso 2. Ahí es donde se descubre a un agente que cree que terminó. La versión larga, con un ejemplo completo: <a href="/es/reviewing-agent-plans/">Revisar el plan de un agente en cinco minutos</a>.</p>

<h2>Pruébalo</h2>
<p>MarsDawn está en el <a href="{k.LISTING_URL}">Mac App Store</a>. También existe la herramienta de línea de comandos gratuita <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Exporta Markdown a PDF sin la app, y <code>marsdawn open</code> le permite a tu agente abrir archivos en MarsDawn por ti.</p>
<p><a href="/es/cli/">Línea de comandos</a> &#183; <a href="/es/cli/agents/">marsdawn para agentes</a> &#183; Antes de comprar: <a href="/es/limits/">Lo que MarsDawn no hace</a></p>

<h2>Siguiente</h2>
<ul>
  <li>El argumento breve para leer lo que genera la IA: <a href="/es/reviewing-ai-output/">Por qué lo que genera la IA todavía necesita un lector humano</a>.</li>
  <li>Mantener pequeño el contexto del agente mientras revisas: <a href="/es/token-efficient-review/">revisión con pocos tokens</a>.</li>
  <li>Por qué los agentes muestran sus planes: <a href="/es/agent-transparency/">Anthropic dice que los agentes deben ser transparentes. ¿Quién lee lo que muestran?</a></li>
  <li>La lista de arriba, paso a paso con un ejemplo: <a href="/es/reviewing-agent-plans/">Revisar el plan de un agente en cinco minutos</a>.</li>
  <li>Qué documentos te entregan los distintos tipos de agentes: <a href="/es/agent-design-patterns/">Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno</a>.</li>
</ul>

<h2>Fuentes</h2>
<ul>
  <li>Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (citado de la versión publicada el 26/09/2026; el artículo ahora indica que buena parte de las herramientas que describe cambió desde diciembre de 2024).</li>
  <li>Chip Huyen, «Agents», 7 de enero de 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng, «Agentic Design Patterns Part 4, Planning», The Batch, 10 de abril de 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": 'Los agentes deben ser transparentes. ¿Quién lee lo que muestran? · MarsDawn',
        "description": 'La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.',
        "body": f"""
<section class="intro">
  <h1>Anthropic dice que los agentes deben ser transparentes. ¿Quién lee lo que muestran?</h1>
  <p>En diciembre de 2024, Anthropic publicó «Building Effective Agents», una guía para quienes construyen agentes de IA. Su resumen enumera tres principios, y uno de ellos es la transparencia. Este artículo trata del otro extremo de ese principio: cuando un agente muestra sus pasos, alguien tiene que leerlos.</p>
</section>

<div class="summary"><p><strong>La transparencia la pone el agente. La lectura la pones tú. Anthropic les pide a quienes construyen agentes que muestren los pasos de planificación; para la mayoría de las personas que manejan un agente de programación, esos pasos llegan como un archivo Markdown que alguien tiene que leer en el momento justo.</strong></p></div>

<h2>Qué dice la guía</h2>
<p>Erik S. y Barry Zhang resumen sus consejos así:</p>
<blockquote><p>«Al implementar agentes, intentamos seguir tres principios básicos: mantener la simplicidad en el diseño del agente. Priorizar la transparencia mostrando explícitamente los pasos de planificación del agente. Diseñar con cuidado la interfaz entre el agente y la computadora (ACI) mediante una documentación y unas pruebas exhaustivas de las herramientas».</p></blockquote>
<p>Son principios de diseño para quienes construyen agentes, no instrucciones para la persona que usa uno. El principio pide que se muestren los pasos. No dice quién los lee.</p>
<p>El mismo artículo describe lo que hace un agente una vez que tiene una tarea: «Una vez que la tarea está clara, los agentes planifican y operan de forma independiente, y posiblemente vuelven al humano para pedir más información o su criterio». Y: «Luego, los agentes pueden hacer una pausa para recibir comentarios humanos en puntos de control o cuando encuentran obstáculos». Fíjate en las palabras <em>posiblemente</em> y <em>pueden</em>. Los puntos de control se describen como algo que un agente puede tener, no algo que deba tener.</p>

<h2>La mayor parte de la verificación no la haces tú</h2>
<p>Es fácil exagerar esto, así que esto es lo que la guía pone primero en realidad. El agente se verifica a sí mismo contra el mundo: «Durante la ejecución, es crucial que los agentes obtengan en cada paso una “verdad de referencia” del entorno (como los resultados de llamadas a herramientas o de la ejecución de código) para evaluar su avance». En esa frase, la verdad de referencia son resultados de pruebas y salidas de herramientas. No una persona.</p>
<p>La guía también es directa sobre el riesgo: «La naturaleza autónoma de los agentes implica costos más altos y la posibilidad de errores que se acumulan». Su respuesta son pruebas exhaustivas en entornos aislados, con salvaguardas. No dice «lee con más cuidado».</p>
<p>Una persona sí aparece más adelante, en el apéndice sobre agentes de programación: «Sin embargo, aunque las pruebas automatizadas ayudan a verificar la funcionalidad, la revisión humana sigue siendo crucial para asegurar que las soluciones se ajusten a los requisitos más amplios del sistema». Esa frase habla de código. Pero el hueco que señala es conocido con cualquier agente: una prueba puede decirte que algo funciona, no que es lo que querías.</p>

<h2>Dónde terminan los pasos</h2>
<p><strong>De aquí en adelante, esta es nuestra lectura, no la de Anthropic.</strong></p>
<p>Si usas un agente de programación todos los días, sus pasos de planificación no suelen aparecer en un panel. Aparecen como archivos: <code>plan.md</code>, una lista de tareas con casillas, un archivo de avance que el agente no deja de reescribir, un resumen al final. La transparencia, desde tu lado, significa más cosas que leer.</p>
<p>Mostrar los pasos es la mitad que le toca al agente. La otra mitad es una persona que los lee cuando importa: antes de que se ejecute la migración, antes de fusionar la rama, antes de aceptar el «listo». Un agente que lo expone todo en un archivo de 600 líneas que nadie abre es transparente en el papel y no tiene supervisión en la práctica.</p>
<p>Harrison Chase planteó algo parecido en 2024, al escribir sobre cómo deberían funcionar los frameworks de agentes y no sobre documentos: «Vas a querer poder observar lo que pasa dentro, ya que es posible que los pasos exactos no se conozcan de antemano». Hablaba de herramientas para quienes construyen agentes. Si eres tú quien maneja el agente, el archivo simple que no deja de escribir suele ser la parte que puedes observar.</p>
<p>Ninguno de estos autores menciona MarsDawn, y ninguno lo recomienda, ni tampoco ninguna otra herramienta de Markdown.</p>

<h2>Por qué esa lectura cuesta más de lo que parece</h2>
<p>El archivo es largo, y lo que importa rara vez está arriba. El diagrama que explica el cambio es código Mermaid, no una imagen (cómo verlo dibujado se explica en <a href="/es/view-markdown-on-mac/">Cómo ver un archivo Markdown en Mac</a>). Puede que el agente reescriba el archivo cuando vas por la mitad. A menudo hay más de un archivo, a veces en distintas ramas o worktrees. Y cuando detectas un problema, «la parte del caché se ve rara» deja al agente adivinando. La versión larga está en <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a>.</p>

<h2>Dónde encaja MarsDawn y dónde no</h2>
<p>MarsDawn es una app para Mac hecha para esa lectura. No hace más transparente a un agente y no tiene ningún modelo de IA dentro: no va a resumir el plan ni a decirte si está bien. Lo que sí hace:</p>
<ul>
  <li><strong>Archivos largos:</strong> Visualización &#9656; Mostrar barra lateral (&#8963;&#8984;S) abre la pestaña Esquema, que lista los títulos. Haz clic en uno para saltar ahí.</li>
  <li><strong>Diagramas y fórmulas:</strong> el código fuente y la página renderizada quedan lado a lado (&#8984;2) y se desplazan juntos, con Mermaid y KaTeX dibujados. Si un diagrama tiene un error, la vista previa muestra su código con el error debajo.</li>
  <li><strong>Reescrito mientras lees:</strong> cuando el agente reescribe el archivo, MarsDawn lo vuelve a cargar y conserva tu posición, siempre que no tengas cambios propios sin guardar.</li>
  <li><strong>Varios archivos:</strong> abre la carpeta del agente con Archivo &#9656; Abrir carpeta&#8230; (&#8679;&#8984;O). Los archivos nuevos aparecen en la pestaña Archivos en aproximadamente un segundo y, en un checkout de git, el encabezado indica la rama o el worktree.</li>
  <li><strong>Señalar una línea:</strong> Edición &#9656; Copiar referencia (&#8997;&#8984;C) copia tu posición como <code>docs/plan.md:42</code>, y Copiar para IA (&#8963;&#8997;&#8984;C) agrega el texto seleccionado debajo, listo para pegar en el chat con el agente.</li>
</ul>
<p>La lectura la sigues haciendo tú. MarsDawn mantiene legible un archivo largo que cambia mientras la haces.</p>

<h2>Pruébalo</h2>
<p>MarsDawn está en el <a href="{k.LISTING_URL}">Mac App Store</a>. También existe la herramienta de línea de comandos gratuita <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Exporta Markdown a PDF sin la app.</p>
<p><a href="/es/cli/">Línea de comandos</a> &#183; Antes de comprar: <a href="/es/limits/">Lo que MarsDawn no hace</a></p>

<h2>Siguiente</h2>
<ul>
  <li>Por qué cuesta leer lo que entrega un agente, con una lista de verificación: <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a>.</li>
  <li>La lista, paso a paso con un ejemplo: <a href="/es/reviewing-agent-plans/">Revisar el plan de un agente en cinco minutos</a>.</li>
  <li>Qué documentos te entregan los distintos tipos de agentes: <a href="/es/agent-design-patterns/">Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno</a>.</li>
  <li>El argumento breve para leer lo que genera la IA: <a href="/es/reviewing-ai-output/">Por qué lo que genera la IA todavía necesita un lector humano</a>.</li>
</ul>

<h2>Fuentes</h2>
<ul>
  <li>Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (citado de la versión publicada el 26/09/2026; el artículo ahora indica que buena parte de las herramientas que describe cambió desde diciembre de 2024).</li>
  <li>Harrison Chase, «What is an agent?», LangChain, 28 de junio de 2024, copia archivada: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (la dirección original ahora muestra otro artículo, de 2026).</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": 'Revisar el plan de un agente en cinco minutos · MarsDawn',
        "description": 'Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.',
        "body": f"""
<section class="intro">
  <h1>Revisar el plan de un agente en cinco minutos</h1>
  <p>Tu agente escribió un plan y espera tu visto bueno. Tienes cinco minutos, no una hora. Esta es una forma de aprovecharlos que funciona en cualquier editor, incluso en uno de texto plano. MarsDawn ayuda con algunos pasos, y te diremos cuáles. No ayuda con el más importante.</p>
</section>

<div class="summary"><p><strong>No leas el plan de arriba abajo. Revisa su estructura, comprueba una afirmación, encuentra lo irreversible, mira los diagramas y el alcance, y escribe comentarios que el agente pueda aplicar. Seis pasos, unos cinco minutos.</strong></p></div>

<h2>Por qué importa antes de ejecutarlo</h2>
<p>Chip Huyen, al explicar por qué la planificación debe ir separada de la ejecución, pone el costo sin rodeos: «Sin supervisión, un agente puede ejecutar esos pasos durante horas, gastando tiempo y dinero en llamadas a la API, antes de que te des cuenta de que no lleva a ninguna parte». Lo que añadimos nosotros: un plan es el lugar más barato para detectar un error. Corregir una línea de <code>plan.md</code> cuesta una frase. Corregir lo que el agente hizo después cuesta una tarde.</p>

<h2>El ejemplo</h2>
<p>Le pediste a un agente que moviera los avatares de los usuarios a un almacenamiento de objetos sin romper los enlaces existentes. Te devuelve esto:</p>
<pre><code># Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. &#9989; done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.</code></pre>
<p>Se lee bien. También borraría todos los avatares antes de copiar uno solo.</p>

<h2>Los seis pasos</h2>
<p><strong>1. Lee solo los encabezados.</strong> <em>(un minuto aproximadamente)</em> ¿El plan coincide con lo que pediste? Si falta una sección, normalmente falta trabajo. Aquí: Goal, Steps, Status. Pediste que los enlaces existentes siguieran funcionando, y ningún encabezado habla de los enlaces antiguos ni de cómo deshacer el cambio. Ese es tu primer comentario.</p>
<p>En una terminal, <code>grep -n '^#' plan.md</code> muestra solo los encabezados, y la mayoría de los editores también pueden mostrar un esquema. En MarsDawn, la pestaña Esquema de la barra lateral (Visualización &#9656; Mostrar barra lateral, &#8963;&#8984;S) los enumera, y un clic te lleva a cada uno.</p>
<p><strong>2. Encuentra cada lugar que afirme que algo está hecho, que pasó o que se verificó, y comprueba uno tú mismo.</strong> <em>(un minuto aproximadamente)</em> Abre el archivo, ejecuta la prueba, cuenta las filas. Chip Huyen describe un fallo en el que «el agente está convencido de haber completado una tarea cuando no es así». En su ejemplo, a un agente se le pide alojar a 50 personas en 30 habitaciones de hotel, acomoda a 40 y dice que terminó.</p>
<pre><code>grep -n -i -E 'done|pass|verified|&#9989;' plan.md</code></pre>
<p>Aquí encuentra «&#9989; done» y «All tests pass.» ¿Qué pruebas? ¿Alguna toca los avatares? Ejecútalas, o pregunta. MarsDawn no puede hacer este paso por ti. Nadie más que tú puede.</p>
<p><strong>3. Busca los pasos que no se pueden deshacer.</strong> <em>(un minuto aproximadamente)</em> Borrar datos, migraciones, force-push, cualquier cosa que envíe, pague o publique. Esos esperan tu aprobación explícita. Chip Huyen describe la misma idea desde el lado del sistema: «Si un plan incluye operaciones riesgosas, como actualizar una base de datos o fusionar un cambio de código, el sistema puede pedir aprobación humana explícita antes de ejecutarlas, o dejar que las ejecuten personas». Aquí, el paso 4 borra los originales, y va antes del paso 5, la copia.</p>
<p><strong>4. Lee los diagramas renderizados y compara cada flecha con el texto.</strong> Un diagrama de flujo que dice «copiar &#8594; verificar &#8594; borrar» mientras los pasos dicen otra cosa es un hallazgo. Este plan no tiene diagramas, así que hoy te lo saltas. Cuando haya uno, mira la imagen, no el código Mermaid: muchos editores tienen vista previa, y <a href="/es/view-markdown-on-mac/">Cómo ver un archivo Markdown en la Mac</a> y <a href="/es/vs/markdown-preview-tools/">Ver Markdown en otros lugares</a> recorren las opciones. En MarsDawn, el diagrama renderizado está junto a su código (&#8984;2), y un diagrama roto muestra su código con el error debajo, lo que merece un comentario propio.</p>
<p><strong>5. Haz una lista de los archivos y sistemas que toca el plan, y pregunta por todo lo que no pediste.</strong> <em>(pasos 4 y 5 juntos, un minuto aproximadamente)</em> Aquí: la configuración de almacenamiento, las plantillas, una carpeta en el servidor, un bucket. ¿Quién puede leer el bucket? No dijiste que debiera ser público. Si abriste la carpeta de trabajo del agente en MarsDawn (Archivo &#9656; Abrir carpeta&#8230;, &#8679;&#8984;O), los archivos nuevos que escribe aparecen en la pestaña Archivos en un segundo aproximadamente, y el encabezado muestra la rama de git o el worktree, para que sepas qué copia de trabajo estás revisando.</p>
<p><strong>6. Escribe tus comentarios como lugar, problema y solución, un problema por línea.</strong> <em>(el último minuto)</em></p>
<pre><code>plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.</code></pre>
<p>Cualquier editor con números de línea sirve. En MarsDawn, Edición &#9656; Copiar referencia (&#8997;&#8984;C) copia tu posición como <code>plan.md:10</code>, y Copiar para IA (&#8963;&#8997;&#8984;C) añade debajo el texto seleccionado.</p>

<h2>Si tienes un minuto</h2>
<p>Haz el paso 2. Ahí es donde atrapas a un agente que cree que ya terminó.</p>

<h2>Cuando cinco minutos no bastan</h2>
<p>A veces no puedes saber si un paso es correcto, porque está fuera de lo que conoces. Jess Ou, en el artículo explicativo de LangChain sobre agentes de 2026, lo dice en dos frases: «No delegues un juicio que no puedes evaluar. Si tú no reconocerías una buena respuesta, el agente tampoco». Lo que concluimos nosotros: si no puedes juzgar un paso, eso no es motivo para aprobarlo más rápido. Es motivo para preguntarle a alguien que sí pueda.</p>

<h2>Qué hace MarsDawn aquí, y qué no</h2>
<p>MarsDawn no incluye ningún modelo de IA. No encontrará los problemas de este plan, y no hace ni el paso 2 ni el paso 3. Mantiene el archivo legible mientras trabajas: el esquema para el paso 1, los diagramas renderizados para el paso 4, la pestaña Archivos para el paso 5, las referencias de línea para el paso 6. Y si el agente revisa el plan mientras lo lees, MarsDawn lo recarga y conserva tu posición, siempre que no tengas cambios sin guardar.</p>
<p>Cuando el plan esté decidido, si alguien más necesita verlo, <a href="/es/sharing-exported-pdfs/">Compartir PDF exportados</a> y <a href="/es/markdown-to-pdf/">Markdown a PDF</a> explican cómo enviarlo en PDF.</p>

<h2>Pruébalo</h2>
<p>MarsDawn está en el <a href="{k.LISTING_URL}">Mac App Store</a>. También existe la herramienta de línea de comandos gratuita <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Exporta Markdown a PDF sin la app.</p>
<p><a href="/es/cli/">Línea de comandos</a> &#183; Antes de comprar, conviene saber: <a href="/es/limits/">Lo que MarsDawn no hace</a></p>

<h2>Para seguir leyendo</h2>
<ul>
  <li>Por qué lo que entrega un agente es difícil de leer: <a href="/es/reading-agent-output/">Leer lo que te entrega tu agente</a>.</li>
  <li>Por qué los agentes exponen sus planes: <a href="/es/agent-transparency/">Anthropic quiere agentes transparentes. ¿Quién lee lo que exponen?</a></li>
  <li>Los planes no son lo único que entregan los agentes: <a href="/es/agent-design-patterns/">Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno</a>.</li>
</ul>

<h2>Fuentes</h2>
<ul>
  <li>Chip Huyen, «Agents», 7 de enero de 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou, «What is an AI agent?», LangChain, 31 de julio de 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": 'Cuatro patrones de diseño de agentes y los documentos que te entregan · MarsDawn',
        "description": 'Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.',
        "body": f"""
<section class="intro">
  <h1>Cuatro patrones de diseño de agentes y los documentos que te entrega cada uno</h1>
  <p>En marzo de 2024, Andrew Ng describió en su boletín, The Batch, cuatro patrones de diseño para agentes de IA: reflexión, uso de herramientas, planificación y colaboración multiagente. Normalmente se explican desde el lado de quien construye agentes, como formas de obtener mejores resultados de un modelo. Este artículo mira desde el otro lado. Si usas un agente basado en uno de estos patrones, ¿qué llega a tu carpeta y qué deberías leer primero?</p>
</section>

<div class="summary"><p><strong>Los cuatro patrones son de Andrew Ng. Los documentos que suele entregarte cada uno, y qué revisar en ellos, son deducción nuestra. Él no escribe sobre ninguna de las dos cosas, y en esta serie no defiende la revisión humana.</strong></p></div>

<h2>Los cuatro patrones, en breve</h2>
<p>Ng los describe en «Agentic Design Patterns Part 1». En resumen: con la <strong>reflexión</strong>, el modelo revisa su propio trabajo y lo mejora. Con el <strong>uso de herramientas</strong>, puede llamar a herramientas como la búsqueda web o la ejecución de código. Con la <strong>planificación</strong>, elabora un plan de varios pasos y lo ejecuta. Con la <strong>colaboración multiagente</strong>, varios agentes se reparten el trabajo y lo discuten.</p>
<p>En la parte 1 muestra la mejora en un benchmark de programación, HumanEval, con resultados que su equipo reunió de varios grupos de investigación: «GPT-3.5 (zero-shot) acertaba el 48,1&#160;%. GPT-4 (zero-shot) lo hace mejor, con un 67,0&#160;%. Sin embargo, la mejora de GPT-3.5 a GPT-4 queda eclipsada al incorporar un flujo de trabajo agéntico iterativo. De hecho, dentro de un bucle de agente, GPT-3.5 alcanza hasta un 95,1&#160;%». Estas cifras corresponden a un solo benchmark de programación, y 95,1&#160;% es el mejor caso («hasta»). Muestran que los flujos de trabajo con agentes pueden mejorar el resultado. No dicen nada sobre quién lo comprueba.</p>
<p><strong>A partir de aquí, los documentos y las comprobaciones son nuestra lectura, no la de Ng.</strong> Además, los agentes reales mezclan patrones. Un agente de programación puede planificar, ejecutar herramientas y revisar su propio trabajo en una misma sesión, así que a menudo recibirás los cuatro tipos de archivo.</p>

<h2>1. Reflexión: un borrador que ya se revisó a sí mismo</h2>
<p>El artículo de Ng sobre la reflexión la plantea como automatizar los comentarios que, de otro modo, daría una persona: «¿Y si automatizamos el paso de los comentarios críticos, de modo que el modelo critique automáticamente su propia salida y mejore su respuesta?».</p>
<p><strong>Lo que suele entregarte:</strong> un documento revisado, a veces con una sección de autoevaluación o líneas como «casos límite revisados de nuevo».</p>
<p><strong>Qué revisar:</strong> el resultado frente a <em>tu</em> pedido, no frente a la autocrítica del agente. La autoevaluación puede equivocarse a su manera. Chip Huyen: «Un modo interesante de fallo de planificación se debe a errores en la reflexión. El agente está convencido de haber completado una tarea cuando no es así». Lilian Weng, en su blog Lil’Log en junio de 2023, entonces en OpenAI, sobre los modelos de esa época: «La falta de conocimiento experto puede impedir que los LLM conozcan sus defectos y, por lo tanto, que juzguen bien si los resultados de una tarea son correctos». (En el estudio que describía, la evaluación de resultados hecha por un LLM y la de expertos humanos no coincidían). Si dice «verificado», comprueba una cosa tú mismo.</p>

<h2>2. Uso de herramientas: un informe de lo que se ejecutó</h2>
<p><strong>Lo que suele entregarte:</strong> un resumen de lo que el agente ejecutó o buscó y de lo que obtuvo. «Ejecuté la suite de pruebas: todo pasa». Una tabla de resultados. Enlaces que encontró.</p>
<p>La guía de Anthropic presenta los resultados de las herramientas como la comprobación que el agente hace de sí mismo: «Durante la ejecución, es crucial que los agentes obtengan del entorno, en cada paso, una “verdad de referencia” (como los resultados de llamadas a herramientas o la ejecución de código) para evaluar su avance». Esa comprobación ocurre dentro del agente. Lo que te llega a ti es su relato de ella.</p>
<p><strong>Qué revisar:</strong> que cada afirmación remita a una salida que puedas ver. Compara una cifra del resumen con la salida real. Abre uno de los enlaces.</p>

<h2>3. Planificación: <code>plan.md</code></h2>
<p><strong>Lo que suele entregarte:</strong> un plan, una especificación, una lista de tareas que el agente va marcando.</p>
<p>Ng es franco sobre este patrón en la parte 4:</p>
<blockquote><p>«Por un lado, la planificación es una capacidad muy potente; por otro, produce resultados menos predecibles. En mi experiencia, aunque consigo que los patrones agénticos de reflexión y uso de herramientas funcionen de forma fiable y mejoren el rendimiento de mis aplicaciones, la planificación es una tecnología menos madura, y me cuesta predecir de antemano qué va a hacer».</p></blockquote>
<p>También es optimista: «Pero el campo sigue avanzando rápido, y estoy seguro de que las capacidades de planificación mejorarán pronto».</p>
<p><strong>Qué revisar:</strong> el plan antes de que se ejecute, con <a href="/es/reviewing-agent-plans/">la revisión de cinco minutos</a>: estructura, una afirmación, pasos irreversibles, diagramas, alcance. Si el agente reescribe el plan a mitad de camino, compáralo con la versión que aprobaste; si está en git, <code>git diff plan.md</code> muestra qué cambió. En MarsDawn, la pestaña Esquema muestra la estructura de un plan largo, y un plan reescrito se recarga sin que pierdas tu posición, siempre que no tengas cambios sin guardar.</p>

<h2>4. Colaboración multiagente: varios archivos, varios autores</h2>
<p><strong>Lo que suele entregarte:</strong> una especificación de un agente, notas de implementación de otro, una revisión de un tercero, y resúmenes que pasan de uno a otro. A veces cada uno trabaja en su propia rama o worktree.</p>
<p><strong>Qué revisar:</strong> los traspasos. Donde un agente resume el trabajo de otro, busca un requisito que no haya pasado. Busca dos archivos que se contradigan, y decide cuál manda antes de que alguien construya sobre el otro. En MarsDawn, abre la carpeta compartida con Archivo &#9656; Abrir carpeta&#8230; (&#8679;&#8984;O): los archivos nuevos aparecen en la pestaña Archivos en un segundo aproximadamente, a medida que los agentes los escriben, y en una copia de trabajo de git el encabezado muestra la rama o el worktree, para que dos ventanas con el mismo nombre de archivo en ramas distintas no parezcan iguales. Cuando el resultado tiene que llegar a personas que no leen Markdown, <a href="/es/sharing-exported-pdfs/">Compartir PDF exportados</a> cubre ese paso.</p>

<h2>De un vistazo</h2>
<table>
<thead><tr><th>Patrón (Ng)</th><th>Lo que suele entregarte (deducción nuestra)</th><th>Qué leer primero (sugerencia nuestra)</th></tr></thead>
<tbody>
<tr><td>Reflexión</td><td>Un borrador revisado, quizá con una autoevaluación</td><td>El resultado frente a tu pedido; comprueba un «verificado»</td></tr>
<tr><td>Uso de herramientas</td><td>Un informe de lo que se ejecutó y lo que obtuvo</td><td>Una afirmación rastreada hasta la salida real</td></tr>
<tr><td>Planificación</td><td><code>plan.md</code>, una especificación, una lista de tareas</td><td>La revisión de cinco minutos, antes de ejecutar</td></tr>
<tr><td>Colaboración multiagente</td><td>Varios archivos de varios agentes, quizá en varias ramas</td><td>Los traspasos, y qué archivo manda</td></tr>
</tbody>
</table>
<p>Ninguno de los autores citados aquí menciona MarsDawn ni lo recomienda, ni a ninguna otra herramienta de Markdown. MarsDawn no incluye ningún modelo de IA: no sabe qué modelo produjo un archivo, y no hará estas comprobaciones por ti. Mantiene los archivos legibles mientras tú las haces.</p>

<h2>Pruébalo</h2>
<p>MarsDawn está en el <a href="{k.LISTING_URL}">Mac App Store</a>. También existe la herramienta de línea de comandos gratuita <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Exporta Markdown a PDF sin la app: consulta <a href="/es/markdown-to-pdf/">Markdown a PDF</a>.</p>
<p><a href="/es/cli/">Línea de comandos</a> &#183; Antes de comprar, conviene saber: <a href="/es/limits/">Lo que MarsDawn no hace</a></p>

<h2>Para seguir leyendo</h2>
<ul>
  <li>Por qué lo que entrega un agente es difícil de leer, con una lista de comprobación: <a href="/es/reading-agent-output/">Leer lo que te entrega tu agente</a>.</li>
  <li>La comprobación del plan completa: <a href="/es/reviewing-agent-plans/">Revisar el plan de un agente en cinco minutos</a>.</li>
  <li>Lo que la transparencia te pide, y lo que no: <a href="/es/agent-transparency/">Anthropic quiere agentes transparentes. ¿Quién lee lo que exponen?</a></li>
</ul>

<h2>Fuentes</h2>
<ul>
  <li>Andrew Ng, «Agentic Design Patterns Part 1», The Batch, 20 de marzo de 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, «Agentic Design Patterns Part 2, Reflection», The Batch, 27 de marzo de 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng, «Agentic Design Patterns Part 4, Planning», The Batch, 10 de abril de 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen, «Agents», 7 de enero de 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng, «LLM Powered Autonomous Agents», Lil’Log, 23 de junio de 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S. y Barry Zhang, «Building Effective Agents», Anthropic, 19 de diciembre de 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (citado según la versión en línea del 26/09/2026).</li>
</ul>
""",
    }

    app_ui_languages = 'inglés, chino tradicional, chino simplificado, japonés, alemán, francés, español y coreano'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages, 'example_plan': example_plan,
    }
