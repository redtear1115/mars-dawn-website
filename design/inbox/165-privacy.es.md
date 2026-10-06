# Política de privacidad

Cómo trata tu información MarsDawn, el editor de Markdown para macOS.

Última actualización: 2026-09-23

> **La app MarsDawn no recopila ningún dato sobre ti.** No hay cuenta, ni publicidad, ni seguimiento. Tus documentos y tus ajustes se quedan en tu Mac.

## El sitio web

La app y este sitio web son dos cosas distintas. La app no recopila nada. Una visita solo puede registrarse aquí, en marsdawn.southern-light.dev.

Este sitio usa **Google Analytics 4**, cargado mediante **Google Tag Manager**. Todos los visitantes empiezan con la analítica denegada: el modo de consentimiento (Consent Mode) de Google solo envía un ping sin cookies, sin cookie de analítica y sin identificador persistente, hasta que eliges *Aceptar* en el aviso. Si eliges *Rechazar*, o no eliges nada, todo sigue así; y si eliges *Rechazar* después de haber aceptado, la analítica se desactiva de inmediato y se eliminan las cookies que se indican abajo. Puedes cambiar tu elección en cualquier momento con el enlace «Ajustes de cookies» del pie de cada página. La elección en sí se guarda solo en el almacenamiento local de tu navegador, nunca en una cookie nuestra.

Una vez que aceptas, Google Analytics instala sus propias cookies (`_ga` y `_ga_<measurement id>`) y registra:

- **Páginas vistas y referente.** Qué página se vio y, cuando el navegador la envía, la dirección de procedencia.
- **Ubicación aproximada, dispositivo y navegador.** Una ubicación aproximada derivada de tu dirección IP (como mucho, a nivel de ciudad), tu tipo de dispositivo, tu sistema operativo y tu navegador. Nada de ello es lo bastante preciso para identificarte.
- **Clics salientes y profundidad de desplazamiento.** La medición mejorada de Google Analytics registra los clics que salen del sitio, como el enlace al Mac App Store, y hasta dónde te desplazas en una página.
- **Direcciones IP.** Google Analytics 4 no registra ni almacena direcciones IP.
- **Lo que no se registra.** Ninguna cuenta, porque el sitio no tiene. Ningún documento, ni nada de lo que escribes. Ninguna publicidad entre sitios, ni ningún perfil tuyo. Las solicitudes que hace la app de archivos de tema en `/themes/` se omiten y no se reenvían.
- **Conservación.** Google conserva estos datos durante 14 meses y después los elimina.
- **Dónde se tratan.** Google Tag Manager y Google Analytics los opera Google; tus datos pueden tratarse en Estados Unidos y en otros países donde Google opera.
- **El proveedor de alojamiento.** Cloudflare aloja el sitio y, como cualquier proveedor de alojamiento, ve tu dirección IP mientras responde a la solicitud. Ese registro pertenece al proveedor. No es la analítica descrita arriba.

## Lo que se queda en tu Mac

- **Tus documentos.** MarsDawn solo lee y escribe los archivos y carpetas que abres, guardas o eliges. La app nunca los sube a ningún sitio.
- **Tus ajustes.** El aspecto, el tema de la vista previa, la disposición de las ventanas y la preferencia de imágenes se guardan en las preferencias propias de la app, en tu Mac.
- **El acceso a carpetas que concedes.** Cuando dejas que MarsDawn muestre imágenes o archivos de página de una carpeta, o eliges una carpeta de notas, la app guarda un marcador de macOS para poder volver a abrir esa carpeta. Una carpeta que abres en la barra lateral sigue siendo legible y modificable por MarsDawn hasta que la eliminas en Ajustes, no solo mientras su ventana está abierta. Puedes eliminar carpetas en cualquier momento en MarsDawn › Ajustes.

## Cuándo usa MarsDawn internet

MarsDawn funciona totalmente sin conexión. Solo se conecta a internet **cuando tú lo eliges**, para un documento que hace referencia a la web:

- **Documentos Markdown.** Las imágenes web están bloqueadas por omisión. Solo se cargan después de que hagas clic en *Cargar imágenes* en la vista previa, o si activas *Cargar imágenes remotas automáticamente* en Ajustes. Nada más de lo que menciona un documento Markdown se carga desde la web.
- **Documentos HTML.** Un documento HTML se abre de forma estática: su código no se ejecuta y no se carga nada desde la web. Si un documento contiene código que podría ejecutarse, puedes elegir *Visualización › Ejecutar este documento* para ese documento. Su propio código se ejecuta entonces hasta que lo detengas, el documento se vuelva a cargar o cierres la ventana. Esa elección nunca se recuerda y no es un ajuste. Mientras se ejecuta, el documento puede enviar datos por la red y leer imágenes, hojas de estilo, tipos de letra y archivos multimedia de su carpeta y de las carpetas que contiene. El código descargado de la web nunca se ejecuta.

MarsDawn carga contenido web solo por https. Una dirección http simple nunca se carga, con ningún ajuste, y MarsDawn no la reescribe a https. En un documento Markdown, la vista previa muestra un marcador de posición en su lugar.

Cuando se carga contenido web, tu Mac lo solicita directamente a los servidores que lo alojan. Como en cualquier solicitud web, esos servidores pueden ver así tu dirección IP y lo que se solicitó. El desarrollador de MarsDawn no recibe nada de esta información.

Los enlaces en los que haces clic en la vista previa se abren en tu navegador web predeterminado, según las prácticas de privacidad de ese navegador. El audio y el vídeo nunca se reproducen solos.

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
