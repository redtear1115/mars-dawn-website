"""/roadmap/ (website #272), in every locale, from the owner-approved copy on the issue.

Sources (all on redtear1115/mars-dawn-website#272, none retyped by hand; this file holds them as Markdown):
- 6249083907 (2026-10-18)   en, zh-Hant and ja: title, meta and page, approved by the owner;
- 6361851869 (2026-10-23)   zh-Hans, ko, de, fr and es: title, meta and page (the standing consent covers them);
                            (a) "Last updated" and (b) "Plans can change" for all eight, (c) the home FAQ's third
                            question's link row, (e) /changelog/'s link back, and the footer name;
- 6363903472 (2026-10-23)   the feature names that follow the app 1.2.0 catalog (en, zh-Hant and ja lines replaced),
                            and /product-facts.md's "currently" (see build_pages.py);
- 6363973670 (2026-10-23)   the owner's approval of (a) to (e) in en, zh-Hant and ja, and the reminder that the
                            zh-Hant and ja "Released" links carry their locale's prefix.

Each page is its Markdown block: "# " is the h1, the paragraph after it the intro, "## " and "### " are headings,
"- " lines are lists. {date} in the "Last updated" line is LAST_UPDATED written as /changelog/ writes its dates.
The private app issue numbers the list was written from never appear on the page.
"""
from rich_pages import attr, md_blocks, md_inline
from xml.sax.saxutils import escape

LOCALES = ("en", "zh-hant", "zh-hans", "ja", "de", "fr", "es", "ko")

# The day the copy was last changed. Update it with each release, as the page says.
LAST_UPDATED = "2026-10-23"

# The page's h1 and its name in the footer (and in the sitemap-style lists that read UI["roadmap"]).
NAME = {'en': 'Roadmap',
 'zh-hant': '路線圖',
 'ja': 'ロードマップ',
 'zh-hans': '路线图',
 'ko': '로드맵',
 'de': 'Roadmap',
 'fr': 'Feuille de route',
 'es': 'Hoja de ruta'}

# (c) the link row under the home FAQ's third question ("Does MarsDawn work on iPhone or iPad?").
FAQ_MORE = {'en': 'More: [Roadmap](/roadmap/)',
 'zh-hant': '詳見：[路線圖](/zh-hant/roadmap/)',
 'ja': '詳しくは：[ロードマップ](/ja/roadmap/)',
 'zh-hans': '详见：[路线图](/zh-hans/roadmap/)',
 'ko': '자세히: [로드맵](/ko/roadmap/)',
 'de': 'Mehr dazu: [Roadmap](/de/roadmap/)',
 'fr': 'En savoir plus : [Feuille de route](/fr/roadmap/)',
 'es': 'Más información: [Hoja de ruta](/es/roadmap/)'}

# (e) the paragraph after /changelog/'s intro.
CHANGELOG_BACKLINK = {'en': "What's coming next is on the [roadmap](/roadmap/).",
 'zh-hant': '接下來要做的事列在[路線圖](/zh-hant/roadmap/)。',
 'ja': '今後の予定は[ロードマップ](/ja/roadmap/)にあります。',
 'zh-hans': '接下来要做的事列在[路线图](/zh-hans/roadmap/)。',
 'ko': '앞으로 나올 기능은 [로드맵](/ko/roadmap/)에 있습니다.',
 'de': 'Was als Nächstes kommt, steht in der [Roadmap](/de/roadmap/).',
 'fr': 'Ce qui arrive ensuite figure dans la [feuille de route](/fr/roadmap/).',
 'es': 'Lo que viene después está en la [hoja de ruta](/es/roadmap/).'}

COPY = {
    "en": {
        "title": 'Roadmap · MarsDawn',
        "description": "What's in progress and what's next for MarsDawn on Mac, iPhone and iPad, by version. No dates, and unscheduled ideas are marked.",
        "md": """# Roadmap

What we're building next, by version. There are no dates: a version ships when it's ready.

Last updated: {date}

Plans can change: an item may move to another version or be dropped.

## Released

Everything that has shipped is in the [changelog](/changelog/).

## In progress

### Mac 1.2.0
- A formatting bar above the source, plus a Format menu and keyboard shortcuts.
- Ask AI: send the selected text, with the file name, line numbers and your prompt, to Claude or ChatGPT.
- Copy as RTF, to paste the rendered document into Google Docs, Notion, Mail or Pages.
- New from Clipboard: paste Markdown, including AI output with escaped characters, and see it rendered.
- The Handbook layout for PDF export: body pages numbered from 1, "n / N" in the footer and a binding margin on the left.
- HackMD compatibility: its line-break setting and its syntax.
- Install the app, the marsdawn command-line tool or the agent skill, and MarsDawn helps you add the other two.

### iPhone and iPad (iOS 1.0)
- Read Markdown on iPhone and iPad with the same preview as on the Mac.

## Next

### Mac 1.2.1
- Open JSON and YAML, edit them, and see a live tree preview beside the source.
- Open a URL: read Markdown from a public link on GitHub, a Gist or a raw file.
- Callouts: GitHub alerts and HackMD `:::` blocks.
- Add Claude Code's Plans folder to the sidebar in one click, newest plan first.

### Mac 1.2.2
- After an agent changes a file, see which blocks changed.
- An image viewer for PNG, JPEG, GIF and WebP.

### iPad and unfolded iPhone Duo (iOS 1.1)
- Editing on the larger screen.

## Later (not scheduled)
- AI in the app: generate documents on your Mac with Apple's on-device Foundation Models. Not scheduled.
- True WYSIWYG editing. Not scheduled.
- Export to Word (.docx). Not scheduled.

Missing something you need? [Write to us](mailto:support@southern-light.dev?subject=Feature%20request) and tell us what you'd use it for.
""",
    },
    "zh-hant": {
        "title": '路線圖 · MarsDawn',
        "description": 'MarsDawn 在 Mac、iPhone 與 iPad 上正在做與接下來要做的功能，依版本列出。不寫日期，未排程的項目另外標明。',
        "md": """# 路線圖

依版本列出我們接下來要做的事。不寫日期：版本做好了才會推出。

最後更新：{date}

計畫可能會調整：項目可能移到別的版本，也可能取消。

## 已上線

已推出的內容都在[更新紀錄](/zh-hant/changelog/)裡。

## 進行中

### Mac 1.2.0
- 原始碼上方加入格式列，另有「格式」選單和快速鍵。
- Ask AI：把選取的文字連同檔名、行號和你的提示詞，送到 Claude 或 ChatGPT。
- 拷貝為 RTF：把算繪好的文件貼進 Google 文件、Notion、郵件或 Pages。
- 從剪貼板新增：貼上 Markdown，連 AI 輸出時被跳脫的字元也一樣，直接看算繪結果。
- PDF 輸出的「手冊」版面：內文頁碼從 1 起算、頁尾顯示「n / N」、左側留裝訂邊。
- 相容 HackMD：支援它的換行設定和語法。
- App、marsdawn 命令列工具、agent skill 裝了其中一個，MarsDawn 會帶你裝好另外兩個。

### iPhone 與 iPad（iOS 1.0）
- 在 iPhone 和 iPad 上讀 Markdown，預覽和 Mac 版一樣。

## 接下來

### Mac 1.2.1
- 開啟 JSON 和 YAML，可以編輯，旁邊是即時的樹狀預覽。
- 開啟網址：從 GitHub、Gist 或 raw 檔的公開連結讀 Markdown。
- 提示框：支援 GitHub alerts 和 HackMD 的 `:::` 區塊。
- 一鍵把 Claude Code 的 Plans 資料夾加進側邊欄，最新的計畫排在最上面。

### Mac 1.2.2
- agent 改了檔案之後，看得出哪些區塊變了。
- 圖片檢視器：開啟 PNG、JPEG、GIF、WebP。

### iPad 與展開的 iPhone Duo（iOS 1.1）
- 在大螢幕上編輯。

## 更遠以後（未排程）
- App 內 AI：在你的 Mac 上用 Apple 裝置端的 Foundation Models 產生文件。未排程。
- 真正的所見即所得編輯。未排程。
- 輸出 Word（.docx）。未排程。

想要的功能沒列出來？[寫信告訴我們](mailto:support@southern-light.dev?subject=Feature%20request)，也說說你會拿它來做什麼。
""",
    },
    "zh-hans": {
        "title": '路线图 · MarsDawn',
        "description": 'MarsDawn 在 Mac、iPhone 与 iPad 上正在做和接下来要做的功能，按版本列出。不写日期，未排期的项目另行标明。',
        "md": """# 路线图

按版本列出我们接下来要做的事。不写日期：版本做好了才会推出。

最后更新：{date}

计划可能会调整：项目可能移到别的版本，也可能取消。

## 已上线

已推出的内容都在[更新记录](/zh-hans/changelog/)里。

## 进行中

### Mac 1.2.0
- 源文本上方加入格式栏，另有“格式”菜单和快捷键。
- Ask AI：把选中的文字连同文件名、行号和你的提示词，发送到 Claude 或 ChatGPT。
- 拷贝为 RTF：把渲染好的文稿粘贴到 Google 文档、Notion、邮件或 Pages。
- 从剪贴板新建：粘贴 Markdown，连 AI 输出时被转义的字符也一样，直接看渲染结果。
- PDF 导出的“手册”版面：正文页码从 1 起算，页脚显示“n / N”，左侧留装订边。
- 兼容 HackMD：支持它的换行设置和语法。
- App、marsdawn 命令行工具、代理技能装了其中一个，MarsDawn 会带你装好另外两个。

### iPhone 与 iPad（iOS 1.0）
- 在 iPhone 和 iPad 上读 Markdown，预览和 Mac 版一样。

## 接下来

### Mac 1.2.1
- 打开 JSON 和 YAML，可以编辑，旁边是实时的树状预览。
- 打开网址：从 GitHub、Gist 或 raw 文件的公开链接读取 Markdown。
- 提示框：支持 GitHub alerts 和 HackMD 的 `:::` 区块。
- 一键把 Claude Code 的 Plans 文件夹加入边栏，最新的计划排在最上面。

### Mac 1.2.2
- 代理改了文件之后，看得出哪些区块变了。
- 图片查看器：打开 PNG、JPEG、GIF、WebP。

### iPad 与展开的 iPhone Duo（iOS 1.1）
- 在大屏幕上编辑。

## 更远以后（未排期）
- App 内 AI：在你的 Mac 上用 Apple 设备端的 Foundation Models 生成文稿。未排期。
- 真正的所见即所得编辑。未排期。
- 导出 Word（.docx）。未排期。

想要的功能没列出来？[写信告诉我们](mailto:support@southern-light.dev?subject=Feature%20request)，也说说你会用它来做什么。
""",
    },
    "ja": {
        "title": 'ロードマップ · MarsDawn',
        "description": 'Mac、iPhone、iPad 向け MarsDawn で開発中の機能と次に予定している機能を、バージョンごとにまとめました。日付は書かず、未定のものは明記しています。',
        "md": """# ロードマップ

これから作るものを、バージョンごとにまとめています。日付は書きません。準備ができたバージョンから公開します。

最終更新：{date}

計画は変わることがあります。項目が別のバージョンに移ったり、取りやめになったりすることもあります。

## 公開済み

これまでに公開した内容は[更新履歴](/ja/changelog/)にあります。

## 開発中

### Mac 1.2.0
- ソースの上にフォーマットバーを追加。「フォーマット」メニューとキーボードショートカットも用意します。
- Ask AI：選択したテキストを、ファイル名、行番号、プロンプトと一緒に Claude または ChatGPT に送ります。
- RTF としてコピー：レンダリングした文書を Google ドキュメント、Notion、メール、Pages に貼り付けられます。
- クリップボードから新規作成：Markdown を貼り付けるだけでレンダリング結果を表示します。AI の出力でエスケープされた文字にも対応します。
- PDF 書き出しの「ハンドブック」レイアウト：本文のページ番号は 1 から、フッタに「n / N」、左側に綴じしろを付けます。
- HackMD 互換：改行の設定と HackMD の記法に対応します。
- アプリ、marsdawn コマンドラインツール、エージェントスキルのどれかを入れると、残りの 2 つを入れる手順を案内します。

### iPhone と iPad（iOS 1.0）
- iPhone と iPad で、Mac と同じプレビューで Markdown を読めます。

## 今後の予定

### Mac 1.2.1
- JSON と YAML を開いて編集でき、横にリアルタイムのツリープレビューを表示します。
- URL を開く：GitHub、Gist、raw ファイルの公開リンクから Markdown を読み込みます。
- コールアウト：GitHub alerts と HackMD の `:::` ブロックに対応します。
- Claude Code の Plans フォルダをワンクリックでサイドバーに追加。新しいプランが一番上に並びます。

### Mac 1.2.2
- エージェントがファイルを変更したあと、どのブロックが変わったかがわかります。
- 画像ビューア：PNG、JPEG、GIF、WebP を開けます。

### iPad と開いた iPhone Duo（iOS 1.1）
- 大きな画面での編集。

## さらに先（未定）
- アプリ内 AI：Apple のオンデバイス Foundation Models を使い、Mac 上で文書を生成します。時期は未定です。
- 本格的な WYSIWYG 編集。時期は未定です。
- Word（.docx）への書き出し。時期は未定です。

欲しい機能が載っていませんか。[メールで教えてください](mailto:support@southern-light.dev?subject=Feature%20request)。何に使いたいかも書いてもらえると助かります。
""",
    },
    "de": {
        "title": 'Roadmap · MarsDawn',
        "description": 'Woran wir bei MarsDawn für Mac, iPhone und iPad arbeiten und was als Nächstes kommt, nach Version. Ohne Termine; Ideen ohne Zeitplan sind markiert.',
        "md": """# Roadmap

Woran wir als Nächstes arbeiten, nach Version. Es gibt keine Termine: Eine Version erscheint, wenn sie fertig ist.

Zuletzt aktualisiert: {date}

Pläne können sich ändern: Ein Punkt kann in eine andere Version wandern oder wegfallen.

## Erschienen

Alles, was bereits erschienen ist, steht im [Änderungsprotokoll](/de/changelog/).

## In Arbeit

### Mac 1.2.0
- Eine Formatleiste über dem Quelltext, dazu ein Menü „Format“ und Tastaturkurzbefehle.
- Ask AI: den markierten Text mit Dateiname, Zeilennummern und deinem Prompt an Claude oder ChatGPT senden.
- Als RTF kopieren, um das gerenderte Dokument in Google Docs, Notion, Mail oder Pages einzufügen.
- „Neu aus der Zwischenablage“: Markdown einfügen, auch KI-Ausgabe mit maskierten Zeichen, und es gerendert sehen.
- Das Layout „Handbuch“ für den PDF-Export: Seitenzahlen ab 1 im Hauptteil, „n / N“ in der Fußzeile und ein Bundsteg links.
- HackMD-Kompatibilität: seine Einstellung für Zeilenumbrüche und seine Syntax.
- Installiere die App, das Befehlszeilenprogramm marsdawn oder den Agent-Skill, und MarsDawn hilft dir, die anderen beiden hinzuzufügen.

### iPhone und iPad (iOS 1.0)
- Markdown auf iPhone und iPad lesen, mit derselben Vorschau wie auf dem Mac.

## Als Nächstes

### Mac 1.2.1
- JSON und YAML öffnen, bearbeiten und neben dem Quelltext eine Live-Baumvorschau sehen.
- URL öffnen: Markdown von einem öffentlichen Link auf GitHub, aus einem Gist oder einer Raw-Datei lesen.
- Callouts: GitHub-Alerts und HackMD-Blöcke mit `:::`.
- Den Plans-Ordner von Claude Code mit einem Klick zur Seitenleiste hinzufügen, den neuesten Plan zuerst.

### Mac 1.2.2
- Nachdem ein Agent eine Datei geändert hat, sehen, welche Blöcke sich geändert haben.
- Ein Bildbetrachter für PNG, JPEG, GIF und WebP.

### iPad und aufgeklapptes iPhone Duo (iOS 1.1)
- Bearbeiten auf dem größeren Bildschirm.

## Später (ohne Zeitplan)
- KI in der App: Dokumente auf deinem Mac mit Apples Foundation Models auf dem Gerät erzeugen. Ohne Zeitplan.
- Echtes WYSIWYG-Bearbeiten. Ohne Zeitplan.
- Export nach Word (.docx). Ohne Zeitplan.

Fehlt dir etwas? [Schreib uns](mailto:support@southern-light.dev?subject=Feature%20request) und erzähl, wofür du es nutzen würdest.
""",
    },
    "fr": {
        "title": 'Feuille de route · MarsDawn',
        "description": 'Ce qui est en cours et ce qui vient ensuite pour MarsDawn sur Mac, iPhone et iPad, version par version. Sans dates ; les idées non planifiées sont signalées.',
        "md": """# Feuille de route

Ce que nous préparons, version par version. Pas de dates : une version sort quand elle est prête.

Dernière mise à jour : {date}

Les plans peuvent changer : un élément peut passer à une autre version ou être abandonné.

## Disponible

Tout ce qui est déjà sorti figure dans l’[historique des versions](/fr/changelog/).

## En cours

### Mac 1.2.0
- Une barre de format au-dessus de la source, avec un menu Format et des raccourcis clavier.
- Ask AI : envoyer le texte sélectionné, avec le nom du fichier, les numéros de ligne et votre prompt, à Claude ou ChatGPT.
- Copier en RTF, pour coller le document mis en forme dans Google Docs, Notion, Mail ou Pages.
- Créer à partir du presse-papiers : collez du Markdown, y compris une sortie d’IA aux caractères échappés, et voyez le rendu.
- La mise en page « Guide » pour l’export PDF : pages du corps numérotées à partir de 1, « n / N » en pied de page et une marge de reliure à gauche.
- Compatibilité HackMD : son réglage des sauts de ligne et sa syntaxe.
- Installez l’app, l’outil en ligne de commande marsdawn ou le skill d’agent, et MarsDawn vous aide à ajouter les deux autres.

### iPhone et iPad (iOS 1.0)
- Lire du Markdown sur iPhone et iPad avec le même aperçu que sur Mac.

## Ensuite

### Mac 1.2.1
- Ouvrir du JSON et du YAML, les modifier et voir un aperçu en arborescence en direct à côté de la source.
- Ouvrir une URL : lire du Markdown depuis un lien public sur GitHub, un Gist ou un fichier brut.
- Encadrés : les alertes GitHub et les blocs `:::` de HackMD.
- Ajouter le dossier Plans de Claude Code à la barre latérale en un clic, le plan le plus récent en premier.

### Mac 1.2.2
- Après qu’un agent a modifié un fichier, voir quels blocs ont changé.
- Un visualiseur d’images pour PNG, JPEG, GIF et WebP.

### iPad et iPhone Duo déplié (iOS 1.1)
- Modifier sur le grand écran.

## Plus tard (non planifié)
- IA dans l’app : générer des documents sur votre Mac avec les Foundation Models d’Apple, sur l’appareil. Non planifié.
- Une vraie édition WYSIWYG. Non planifié.
- Export vers Word (.docx). Non planifié.

Il vous manque quelque chose ? [Écrivez-nous](mailto:support@southern-light.dev?subject=Feature%20request) et dites-nous à quoi cela vous servirait.
""",
    },
    "es": {
        "title": 'Hoja de ruta · MarsDawn',
        "description": 'Lo que está en marcha y lo que viene para MarsDawn en Mac, iPhone y iPad, por versión. Sin fechas; las ideas sin planificar están marcadas.',
        "md": """# Hoja de ruta

Lo que vamos a hacer a continuación, por versión. No hay fechas: una versión sale cuando está lista.

Última actualización: {date}

Los planes pueden cambiar: un elemento puede pasar a otra versión o descartarse.

## Publicado

Todo lo publicado está en el [historial de cambios](/es/changelog/).

## En desarrollo

### Mac 1.2.0
- Una barra de formato sobre el código fuente, con un menú Formato y atajos de teclado.
- Ask AI: envía el texto seleccionado, con el nombre del archivo, los números de línea y tu prompt, a Claude o ChatGPT.
- Copiar como RTF, para pegar el documento renderizado en Google Docs, Notion, Mail o Pages.
- Nuevo a partir del portapapeles: pega Markdown, incluida salida de IA con caracteres escapados, y míralo renderizado.
- El diseño «Guía» para exportar a PDF: páginas del cuerpo numeradas desde 1, «n / N» en el pie y un margen de encuadernación a la izquierda.
- Compatibilidad con HackMD: su ajuste de saltos de línea y su sintaxis.
- Instala la app, la herramienta de línea de comandos marsdawn o la skill de agente, y MarsDawn te ayuda a añadir las otras dos.

### iPhone y iPad (iOS 1.0)
- Lee Markdown en iPhone y iPad con la misma vista previa que en el Mac.

## A continuación

### Mac 1.2.1
- Abre JSON y YAML, edítalos y ve una vista previa en árbol en vivo junto al código fuente.
- Abrir una URL: lee Markdown desde un enlace público de GitHub, un Gist o un archivo raw.
- Avisos destacados: las alertas de GitHub y los bloques `:::` de HackMD.
- Añade la carpeta Plans de Claude Code a la barra lateral con un clic, con el plan más reciente arriba.

### Mac 1.2.2
- Después de que un agente cambie un archivo, ve qué bloques cambiaron.
- Un visor de imágenes para PNG, JPEG, GIF y WebP.

### iPad y iPhone Duo desplegado (iOS 1.1)
- Edición en la pantalla más grande.

## Más adelante (sin planificar)
- IA en la app: genera documentos en tu Mac con los Foundation Models de Apple en el dispositivo. Sin planificar.
- Edición WYSIWYG de verdad. Sin planificar.
- Exportar a Word (.docx). Sin planificar.

¿Te falta algo? [Escríbenos](mailto:support@southern-light.dev?subject=Feature%20request) y cuéntanos para qué lo usarías.
""",
    },
    "ko": {
        "title": '로드맵 · MarsDawn',
        "description": 'Mac, iPhone, iPad용 MarsDawn에서 개발 중인 기능과 다음에 나올 기능을 버전별로 정리했습니다. 날짜는 적지 않고, 일정이 없는 항목은 따로 표시합니다.',
        "md": """# 로드맵

다음에 만들 것을 버전별로 정리했습니다. 날짜는 적지 않습니다. 준비가 끝난 버전부터 내놓습니다.

마지막 업데이트: {date}

계획은 바뀔 수 있습니다. 항목이 다른 버전으로 옮겨지거나 취소될 수도 있습니다.

## 출시됨

지금까지 출시한 내용은 모두 [변경 내역](/ko/changelog/)에 있습니다.

## 개발 중

### Mac 1.2.0
- 소스 위에 포맷 막대를 추가하고, ‘포맷’ 메뉴와 키보드 단축키도 제공합니다.
- Ask AI: 선택한 텍스트를 파일 이름, 줄 번호, 프롬프트와 함께 Claude나 ChatGPT로 보냅니다.
- RTF로 복사: 렌더링한 문서를 Google 문서, Notion, 메일, Pages에 붙여 넣을 수 있습니다.
- 클립보드에서 신규: Markdown을 붙여 넣으면 바로 렌더링 결과를 볼 수 있습니다. AI 출력에서 이스케이프된 문자도 마찬가지입니다.
- PDF 내보내기의 ‘설명서’ 레이아웃: 본문 페이지 번호는 1부터 시작하고, 꼬리말에 ‘n / N’을 넣고, 왼쪽에 제본 여백을 둡니다.
- HackMD 호환: HackMD의 줄바꿈 설정과 문법을 지원합니다.
- 앱, marsdawn 명령줄 도구, 에이전트 스킬 중 하나를 설치하면 나머지 두 개도 설치하도록 MarsDawn이 안내합니다.

### iPhone 및 iPad (iOS 1.0)
- iPhone과 iPad에서 Mac과 같은 미리보기로 Markdown을 읽습니다.

## 다음 계획

### Mac 1.2.1
- JSON과 YAML을 열어 편집하고, 옆에서 실시간 트리 미리보기를 봅니다.
- URL 열기: GitHub, Gist, raw 파일의 공개 링크에서 Markdown을 읽습니다.
- 콜아웃: GitHub alerts와 HackMD의 `:::` 블록을 지원합니다.
- Claude Code의 Plans 폴더를 클릭 한 번으로 사이드바에 추가하고, 최신 계획을 맨 위에 둡니다.

### Mac 1.2.2
- 에이전트가 파일을 바꾼 뒤 어떤 블록이 바뀌었는지 보여 줍니다.
- 이미지 뷰어: PNG, JPEG, GIF, WebP를 엽니다.

### iPad 및 펼친 iPhone Duo (iOS 1.1)
- 큰 화면에서 편집.

## 나중에 (일정 없음)
- 앱 내 AI: Apple의 온디바이스 Foundation Models로 Mac에서 문서를 생성합니다. 일정 없음.
- 진정한 WYSIWYG 편집. 일정 없음.
- Word(.docx)로 내보내기. 일정 없음.

원하는 기능이 없나요? [메일로 알려 주세요](mailto:support@southern-light.dev?subject=Feature%20request). 어디에 쓰고 싶은지도 함께 적어 주세요.
""",
    },
}


def page(locale: str, date: str) -> dict:
    """{title, description, body} for /roadmap/ in one locale; the body is the Markdown above as HTML.
    `date` is LAST_UPDATED as /changelog/ writes it in this locale."""
    copy = COPY[locale]
    h1, intro, rest = copy["md"].replace("{date}", date).split("\n\n", 2)
    parts = [f'<section class="intro">\n  <h1>{escape(h1[2:])}</h1>\n  <p>{md_inline(intro)}</p>\n</section>']
    for chunk in rest.strip().split("\n\n"):
        for level, text in _split_headings(chunk):
            parts.append(f"<h{level}>{md_inline(text)}</h{level}>" if level else md_blocks(text))
    return {"title": attr(copy["title"]), "description": attr(copy["description"]), "body": "\n" + "\n".join(parts) + "\n"}


def _split_headings(chunk: str):
    """(level, text) for each heading line and (0, text) for the lines between them."""
    out, rest = [], []
    for line in chunk.split("\n"):
        level = len(line) - len(line.lstrip("#")) if line.startswith("#") else 0
        if level:
            if rest:
                out.append((0, "\n".join(rest)))
                rest = []
            out.append((level, line[level + 1:]))
        else:
            rest.append(line)
    if rest:
        out.append((0, "\n".join(rest)))
    return out
