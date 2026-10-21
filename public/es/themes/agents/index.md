# Crea un tema con tu agente

Oferta de Black Friday: la compra única que desbloquea la app está a mitad de precio, 2,49 USD en lugar de 4,99 USD, hasta el 30 de noviembre. Vuelve a 4,99 USD el 1 de diciembre. <!-- sale-line -->

Una referencia para un agente de IA que crea un tema de vista previa de MarsDawn. El agente escribe un único `theme.json`, lo comprueba y lo renderiza con la herramienta de línea de comandos `marsdawn` y te da un enlace. Tú lo afinas a ojo en la página [Crear un tema](/es/themes/new/) y lo envías. Las tablas de campos de abajo se leen del código fuente del kit, y una comprobación las mantiene iguales.

**Escribe un `theme.json`, ejecuta `marsdawn theme validate theme.json --require-complete --json` hasta que termine con código 0, renderízalo con `marsdawn theme preview` en claro y en oscuro y después dale un enlace a la persona.** Un tema son solo parámetros. Nunca contiene CSS.

## Qué es un tema

- **Colores** para claro y para oscuro: una paleta base y, opcionalmente, colores de sintaxis y de diagramas. Cada uno es `#RRGGBB`.
- **Un diseño de fuente**: `sans`, `serif` o `rounded`.
- **Un conjunto cerrado de opciones de estilo**: números dentro de rangos fijos y elecciones de listas fijas. Un color en una opción de estilo es siempre un rol de la paleta, como `accent`, nunca un color literal.
- **Textos visibles**: un nombre y un resumen y, opcionalmente, un autor y una licencia.

Una clave que no está en las tablas de abajo es un error, y también lo es una clave escrita dos veces. El archivo pesa como máximo 16 384 bytes.

## Comprobar y renderizar

Ejecuta estos comandos en la carpeta que contiene `theme.json`. Necesitan la herramienta `marsdawn`: consulta [marsdawn para agentes](/es/cli/agents/).

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- Códigos de salida: 0 válido, 1 inválido con identificadores de regla, 2 archivo no encontrado, 64 error de uso. `preview` añade 4 cuando el PNG ya existe (pasa `--force` o elige otro nombre) y 5 cuando falla el renderizado.
- Con `--json`, un tema inválido lista sus problemas en `issues`, cada uno con un identificador `rule`, un `path` y un `message`. Corrígelos y vuelve a ejecutarlo.
- `--require-complete` es la comprobación para un tema que se va a publicar: exige además los colores `syntax` y `diagram` en las dos paletas.
- `css` imprime el CSS que sirve la vista previa. `preview` renderiza un documento de ejemplo en un PNG. Ambos validan primero, así que un tema inválido no se renderiza.
- Mira el PNG claro y el oscuro antes de entregar el tema.

## Partir de un tema integrado

Copia uno de los cuatro temas integrados y cámbialo. Cada uno es un archivo completo y válido:

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): el predeterminado y el ejemplo de abajo
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): una paleta más sobria, parecida a la de un documento
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): una paleta más fría y más actual
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): una paleta más viva y de más contraste

### Ejemplo: Dawn

Este es `dawn.json`, byte por byte. Su única opción de estilo es una línea fina del color de acento para `hr`.

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## Campos

Cada objeto de abajo se lee de la misma manera. `required` significa que la clave debe estar presente, y una clave que no figura en la lista es un error.

Tipos: `string`, `integer`, `number`, `boolean`, `map` (etiqueta de idioma a texto), `enum` (uno de los valores listados), `role` (un rol de la paleta) y `object` (la tabla a la que enlaza). Un `[]` después de un tipo significa una lista.

### `theme.json`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | Siempre `1`. |
| `id` | `string` | `required` | De 1 a 32 caracteres: letras minúsculas y dígitos, en tramos unidos por guiones simples, como `calm-green`. |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`, como `1.0.0`. |
| `name` | `map` | `required` | Etiqueta de idioma a texto. `en` es obligatoria; las demás claves son etiquetas de idioma como `zh-Hant`. Cada texto tiene como máximo 48 caracteres, sin enlaces ni saltos de línea. |
| `summary` | `map` | `required` | La misma forma que `name`, con un máximo de 120 caracteres por texto. |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — Uno o dos, sin repetir. Fijan cuánto contraste debe alcanzar el tema. |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | Un identificador SPDX, como `Apache-2.0`. Los temas enviados se publican bajo Apache-2.0. |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `name` | `string` | `required` | Como máximo 64 caracteres, sin enlaces. |
| `github` | `string` | `optional` | Un usuario de GitHub. En un envío, pon el de quien lo envía. |

### `light, dark`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `background` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `surface` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `text` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `muted` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `border` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `heading` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `accent` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `link` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `quote` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `syntax` | `object` | `optional` (obligatorio para publicar, con `--require-complete`) | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` (obligatorio para publicar, con `--require-complete`) | [`diagram`](#t-diagram-colors) |

### `syntax`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `string` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `comment` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `number` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `function` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `type` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |

### `diagram`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `node` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `nodeBorder` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `text` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `line` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `secondary` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `tertiary` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |
| `note` | `string` | `required` | `#` y seis dígitos hexadecimales, como `#1C1C1C`. |

### `style`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [rango](#t-numbers) |
| `lineHeight` | `number` | `optional` | [rango](#t-numbers) |
| `headingWeight` | `number` | `optional` | [rango](#t-numbers) |
| `radius` | `number` | `optional` | [rango](#t-numbers) |
| `maxWidth` | `number` | `optional` | [rango](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [un rol de la paleta](#roles) |
| `inlineCode` | `role` | `optional` | [un rol de la paleta](#roles) — Solo `text` o un rol de sintaxis: `keyword`, `string`, `comment`, `number`, `function` o `type`. |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `size` | `number` | `optional` | [rango](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [rango](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [rango](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| Campo | Tipo | Presencia | Valores y notas |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### Opciones con un tipo

Estas opciones de estilo son objetos con un `type`. Cada `type` admite los campos listados para él y ningún otro.

| Opción | type | Campo | Presencia | Tipo |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [rango](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [rango](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` Dos o tres roles. |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### Roles de la paleta

Un rol de la paleta es uno de estos nombres:

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### Números

Un número se ajusta al múltiplo más cercano de su paso y después debe estar entre el mínimo y el máximo. Si no, la regla es `number.range`.

| Campo | Mín. | Máx. | Paso |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## Qué más se comprueba

- **Contraste.** Cada par de colores que dibuja la vista previa, como `text` sobre `background`, debe alcanzar 4,5:1 para el texto y 3:1 para las líneas y lo demás que no es texto. Los escenarios que indicas suben algunos colores a 4,5:1. El mensaje nombra el par, su proporción y la que necesita.
- **Textos.** Se rechaza un nombre, un resumen o un nombre de autor que esté vacío, sea demasiado largo o contenga un enlace, un carácter de control o un carácter de formato invisible o bidireccional.
- **Identificadores de regla.** Cada problema lleva uno, como `contrast.pair`, `color.hex`, `number.range`, `id.pattern`, `schema.unknownKey` o `palette.incomplete`. Corrige el archivo según lo que dicen el identificador y el `path`.

## Entrégalo como un enlace

La página [Crear un tema](/es/themes/new/) abre un tema desde un enlace, para que la persona pueda afinarlo a ojo. El enlace es la dirección de esa página, luego `#theme=` y luego los bytes del archivo en base64url sin relleno. El archivo puede pesar como máximo 16 384 bytes. Esta única línea construye el enlace en zsh y en bash, en macOS y en Linux:

```
printf 'https://marsdawn.southern-light.dev/es/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

El tema viaja detrás de un `#`, que el navegador no envía al sitio, y el sitio no lo envía a ninguna parte. Eso sí, el enlace queda en el historial de tu shell y en el del navegador, y cualquiera a quien se lo pegues puede leer el tema.

## Envíalo

El agente prepara el archivo y el enlace. La persona lo envía. Las dos vías piden el Developer Certificate of Origin y la publicación bajo Apache-2.0, y esa certificación la hace la persona: el agente no marca la casilla ni firma por ella.

- **Issue.** La persona abre el enlace y pulsa **Submit** en la página «Crear un tema», o abre el [formulario de issue](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml) y pega el JSON en *Theme*. Un workflow comprueba el tema y responde.
- **Pull request.** Cambia solo `themes/<id>/theme.json`, pon en `author.github` el usuario del autor de la pull request y firma cada commit con `git commit -s`. Las reglas están en [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md).

El nombre del autor, el nombre, el resumen y el usuario de GitHub de un tema enviado pasan a ser públicos de forma permanente, así que pon en `author.name` un nombre que la persona esté contenta de publicar.

## Temas publicados

Para ver cómo son los temas publicados, explora la [galería de temas](/es/themes/gallery/).

## Más

- [MarsDawn](https://marsdawn.southern-light.dev/es/index.md): Lee y revisa el Markdown de tu agente en tu Mac: vista previa dividida en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 2,49 USD una vez.
- [Funciones](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [Lo que escribes se queda en tu Mac](https://marsdawn.southern-light.dev/es/yours/index.md): MarsDawn no tiene cuenta, ni sincronización, ni nube. Tus documentos Markdown se quedan en tu Mac, en los archivos y carpetas que elijas.
- [Pruébalo gratis, paga una vez](https://marsdawn.southern-light.dev/es/pay-once/index.md): MarsDawn se descarga gratis. Prueba todo durante 14 días y desbloquéalo una sola vez por 2,49 USD. Sin suscripción y sin cuenta.
- [Exportación a PDF](https://marsdawn.southern-light.dev/es/pdf/index.md): Exporta Markdown como PDF o imprímelo en tu Mac, con diagramas Mermaid y código resaltado. Los saltos de página evitan partir bloques de código cortos.
- [Una app para Mac](https://marsdawn.southern-light.dev/es/native/index.md): Un editor de Markdown que es una app de Mac de verdad: ventanas y pestañas nativas, guardado automático, historial de versiones, Vista rápida en el Finder y un editor de texto que se comporta como en la Mac.
- [Lo que MarsDawn no hace](https://marsdawn.southern-light.dev/es/limits/index.md): Sin sincronización, sin app para iPhone o iPad, sin plugins, sin cuentas. Cuatro temas integrados y más en la galería. Lo que conviene saber antes de comprar.
- [Soporte](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [Política de privacidad](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [Cómo abrir archivos .md en Mac](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [Vista previa de Mermaid en Mac](https://marsdawn.southern-light.dev/es/mermaid-preview-mac/index.md): Diagramas Mermaid junto a tu Markdown en una Mac: vista previa en vivo, Vista rápida y exportación a PDF. Un diagrama con errores muestra el error y la línea.
- [Vista rápida para Markdown](https://marsdawn.southern-light.dev/es/quicklook/index.md): Con MarsDawn, Vista rápida renderiza Markdown en el Finder con la barra espaciadora: Mermaid, KaTeX y código resaltado. Sigue funcionando tras la prueba.
- [De Markdown a PDF](https://marsdawn.southern-light.dev/es/markdown-to-pdf/index.md): Convierte Markdown a PDF en Mac con la herramienta de línea de comandos gratuita marsdawn. Instálala con Homebrew y ejecuta un solo comando: tablas, matemáticas, Mermaid y código.
- [MarsDawn comparado: vista previa de VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [MacMD Viewer frente a MarsDawn](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 2,49 USD una sola vez.
- [El mejor visor de Markdown para Mac (2026)](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
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
- [Historial de cambios](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
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
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
