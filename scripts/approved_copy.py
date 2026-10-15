"""Owner-approved copy (en and zh-Hant), loaded programmatically from the vault drafts and never retyped.

Do not edit by hand: change the source and regenerate. Strings are the Markdown inside the sources' fenced
blocks (and, for table cells and bullets, the lines themselves); scripts/rich_pages.py turns them into HTML.

OPEN_MD and MERMAID: website #227, source
  <vault>/MarsDawn/協作/給擁有者/open-md-and-mermaid-copy-2026-10-15.md
  (owner-approved 2026-10-15, "all as recommended"). One declared edit, owner decision 7 (option b): the sentence(s)
  [' A diagram type that a newer Mermaid adds may show the error display instead.', '較新的 Mermaid 才加入的圖表類型，可能會顯示錯誤訊息。']
  were removed from MERMAID[...]["know"].
VS_MACMD (and VS_SOURCES): /vs/macmd-viewer/, source
  <vault>/MarsDawn/協作/給擁有者/vs-macmd-viewer-copy-2026-10-15.md
  (owner-approved 2026-10-15; item 4 as orchi's option C and item 8 as option A). Tables, intro, "which one" and the FAQ
  are the source's; the source list is its source table (S1 to S10). Rows and headings the drafts do not have are
  added in build_pages.py (VS_MACMD_EXTRA).
FILM_THEMES: the second brand film's section on /features/ and /themes/ (heading and one-line caption), source
  <vault>/MarsDawn/協作/給擁有者/features-page-copy-2026-10-15.md, section 3.
SKILL_INSTALL, CLI_SKILL_LINE, AGENTS_SKILL_ITEM: website #231 (marsdawn skill --install on /cli/skill/, one line each on /cli/
  and /cli/agents/), source
  <vault>/MarsDawn/協作/給擁有者/cli-skill-install-copy-2026-10-15.md
  (owner-approved 2026-10-15, every 待你決定 item as recommended). HTML, as the source has it; {_SKILL_URL} is the skill's address.
"""

OPEN_MD = {'en': {'title': 'How to open .md files on Mac · MarsDawn',
        'description': 'How to open a .md file on a Mac: double-click, set a default app, preview in Finder. '
                       'For .md files an AI agent wrote, read them rendered in MarsDawn.',
        'h1': 'How to open .md files on Mac.',
        'short': 'Double-click it. If your Mac opens it in a text editor and you see `#` and `**` instead of '
                 'headings and bold, the file is fine: a `.md` file is plain text, and that editor is '
                 'showing the text as it is. Open it in an app that renders Markdown, such as MarsDawn, and '
                 'make that app the default so every `.md` file opens there.',
        'steps_h2': 'Open a .md file on your Mac',
        'steps': '1. **Double-click the file.** It opens in the app your Mac has set for `.md` files. With '
                 'no Markdown app, that is often a plain text editor, which shows the marks instead of the '
                 'page.\n'
                 '2. **Pick the app yourself.** Control-click the file and choose Open With, then the app. '
                 'Or choose File ▸ Get Info (⌘I), pick an app under "Open with:", and click "Change All…" so '
                 'every file of this type opens there. MarsDawn opens `.md`, `.markdown`, `.mdown`, `.mkd` '
                 'and `.mkdn` files.\n'
                 '3. **Preview without opening it.** Select the file in Finder and press Space. With '
                 'MarsDawn installed, Quick Look shows the rendered page, diagrams included.',
        'read_mermaid': '- [Mermaid](/mermaid-preview-mac/) flowcharts and sequence diagrams are drawn in '
                        'the preview, and code blocks are highlighted.',
        'faq_h2': 'Questions',
        'faq': [['What is a .md file?',
                 'A `.md` file is a plain text file written in Markdown, a way of marking up text with '
                 'simple characters: `#` for a heading, `**` around bold, a pipe for a table cell. The '
                 'extensions `.markdown`, `.mdown`, `.mkd` and `.mkdn` mean the same thing. Developers use '
                 'it for READMEs and docs, and AI agents often hand back their plans and reports as `.md` '
                 'files.'],
                ['Why does my .md file open as plain text, with # and ** marks in it?',
                 'Because it is plain text, and a plain text editor shows it as it is. Nothing is wrong with '
                 'the file. To see headings, bold, tables and diagrams, open it in an app that renders '
                 'Markdown. In MarsDawn the rendered page sits next to the source.'],
                ['Why does it open with garbled characters?',
                 'Garbled characters usually mean the file was saved in a text encoding other than UTF-8, '
                 'and the app that opened it guessed wrong. The fix is to save a UTF-8 copy. MarsDawn opens '
                 "a plain text file that isn't UTF-8 read-only, names the encoding it read it as in a bar at "
                 'the top of the window, and offers Save As UTF-8… there, or File ▸ Save As… (⌥⇧⌘S), to '
                 'write a UTF-8 copy you can edit.'],
                ['Can I turn a .md file into a PDF?',
                 'Yes. In MarsDawn, choose File ▸ Export as PDF… (⌥⌘E) or File ▸ Print…; the pages are '
                 "paginated, with diagrams drawn in and code highlighted, in the theme's light colors. "
                 'Without the app, the free `marsdawn export` command-line tool makes the same PDF: '
                 '`marsdawn export notes.md`. See [PDF export](/pdf/) and [Markdown to '
                 'PDF](/markdown-to-pdf/).'],
                ['Can I open the .md files my AI agent wrote?',
                 'Yes, that is what MarsDawn is built for. Open the file and read the rendered page next to '
                 'its source; when the agent revises it, open it again. An agent can also run `marsdawn open '
                 'plan.md` to open the file in MarsDawn for you. See [Reading what your agent hands '
                 'back](/reading-agent-output/).']],
        'next_new': '- Diagrams in a Markdown file: [Mermaid preview on Mac](/mermaid-preview-mac/).'},
 'zh-hant': {'title': 'Mac 怎麼開 md 檔：雙擊、預設 App、快速查看 · MarsDawn',
             'description': 'Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn '
                            '打開，讀排好版的頁面。',
             'h1': 'Mac 怎麼開 md 檔。',
             'short': '雙擊就能打開。如果你的 Mac 用文字編輯器打開，看到的是 `#` 和 `**`，而不是標題和粗體，檔案沒有壞：`.md` '
                      '檔本來就是純文字，編輯器只是照原樣顯示。改用會排版 Markdown 的 app（例如 MarsDawn）打開，再把它設成預設 app，之後每個 `.md` '
                      '檔都會在那裡打開。',
             'steps_h2': '在 Mac 上打開 md 檔',
             'steps': '1. **雙擊檔案。** 檔案會用你的 Mac 為 `.md` 設定的 app 打開。如果沒有任何 Markdown '
                      'app，常常就是純文字編輯器，看到的是記號，不是排好的頁面。\n'
                      '2. **自己選 app。** 按住 Control 點檔案，選「打開檔案的應用程式」，再選 app。或者選「檔案 ▸ '
                      '取得資訊」（⌘I），在「打開檔案的應用程式：」選一個 app，再按「全部更改⋯」，以後這類檔案都會用它打開。MarsDawn 能打開 '
                      '`.md`、`.markdown`、`.mdown`、`.mkd` 和 `.mkdn`。\n'
                      '3. **不打開，直接預覽。** 在 Finder 選取檔案，按空白鍵。裝了 MarsDawn 的話，「快速查看」會顯示排版後的頁面，圖表也在。',
             'read_mermaid': '- [Mermaid](/zh-hant/mermaid-preview-mac/) 流程圖和循序圖直接畫在預覽裡，程式碼區塊也會上色。',
             'faq_h2': '常見問題',
             'faq': [['md 檔是什麼？',
                      '`.md` 檔是用 Markdown 寫成的純文字檔。Markdown 用簡單的字元標記文字：`#` 是標題，`**` '
                      '包住的是粗體，直線符號畫出表格。`.markdown`、`.mdown`、`.mkd`、`.mkdn` 是同樣的東西。開發者拿它寫 README 和文件，AI agent '
                      '也常把計畫和報告寫成 `.md` 檔交回來。'],
                     ['為什麼 md 檔打開是純文字，滿是 # 和 ** ？',
                      '因為它本來就是純文字，純文字編輯器只會照原樣顯示，檔案沒有壞。想看到標題、粗體、表格和圖表，要用會排版 Markdown 的 app 打開。在 MarsDawn '
                      '裡，排好的頁面就在原始碼旁邊。'],
                     ['為什麼打開是亂碼？',
                      '亂碼通常是因為檔案存成 UTF-8 以外的文字編碼，而打開它的 app 猜錯了。解法是另存一份 UTF-8 的副本。MarsDawn 打開不是 UTF-8 '
                      '的純文字檔時會以唯讀開啟，並在視窗上方的提示列寫出它當成哪種編碼來讀；那裡的「儲存為 UTF-8⋯」，或「檔案 ▸ 儲存為⋯」（⌥⇧⌘S），可以存出一份能編輯的 '
                      'UTF-8 副本。'],
                     ['md 檔可以轉成 PDF 嗎？',
                      '可以。在 MarsDawn 選「檔案 ▸ 輸出為 PDF⋯」（⌥⌘E）或「檔案 ▸ 列印⋯」，頁面會自動分頁，圖表畫進去，程式碼保留上色，使用主題的淺色配色。不裝 app '
                      '的話，免費的 `marsdawn export` 命令列工具能輸出同樣的 PDF：`marsdawn export notes.md`。請看[輸出 '
                      'PDF](/zh-hant/pdf/)和[Markdown 轉 PDF](/zh-hant/markdown-to-pdf/)。'],
                     ['AI agent 寫的 md 檔也能這樣打開嗎？',
                      '可以，MarsDawn 就是為這個做的。打開檔案，排好的頁面就在原始碼旁邊；agent 改好之後，再打開來讀一次。agent 也可以執行 `marsdawn open '
                      'plan.md`，在 MarsDawn 裡把檔案打開給你。請看[讀懂 agent 交回來的 '
                      'Markdown](/zh-hant/reading-agent-output/)。']],
             'next_new': '- Markdown 檔裡的圖表：[在 Mac 上預覽 Mermaid](/zh-hant/mermaid-preview-mac/)。'}}

MERMAID = {'en': {'title': 'Mermaid preview on Mac, next to your Markdown · MarsDawn',
        'description': 'See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look '
                       'and PDF export. A broken diagram shows its error and the line.',
        'h1': 'Mermaid preview on Mac.',
        'intro': 'Mermaid lets you write a diagram as text inside a Markdown file. Most editors show you the '
                 'text. MarsDawn draws the diagram: in the preview next to the source, in Quick Look in '
                 'Finder, and in the PDF you export.',
        'example_h2': 'Write the diagram as text',
        'example': 'Put the diagram in a code block marked `mermaid`:',
        'code': '```mermaid\n'
                'flowchart LR\n'
                '    Write[Write Markdown] --> Preview[Live preview]\n'
                '    Preview --> Export{Share it?}\n'
                '    Export -- PDF --> PDF[File ▸ Export as PDF…]\n'
                '    Export -- Print --> Print[File ▸ Print…]\n'
                '```',
        'after': 'In MarsDawn that block becomes a flowchart: Write Markdown, then Live preview, then a '
                 'Share it? choice that leads to PDF or Print.',
        'where_h2': 'Where the diagram is drawn',
        'where': '- **In the preview.** Open the file and the diagram sits next to its source (⌘2). The page '
                 'updates as you type, and the two panes scroll together.\n'
                 '- **In Quick Look.** Select the file in Finder and press Space; diagrams are drawn there '
                 'too.\n'
                 '- **In the PDF.** File ▸ Export as PDF… and File ▸ Print… draw the diagram into the page. '
                 "Page breaks avoid cutting a diagram in half. The PDF uses the theme's light colors.\n"
                 '- **From the command line.** The free `marsdawn export` tool draws the same diagrams into '
                 'a PDF, and does not need the app. See [Command Line](/cli/).\n'
                 "- **In your theme.** The preview's Appearance setting applies to diagrams too, so a "
                 'diagram follows light or dark.',
        'error_h2': 'When the diagram has a mistake',
        'error': "If Mermaid can't draw a diagram, the preview shows the diagram's source with the full "
                 'error message underneath. When the error names a line, click the message and the editor '
                 'jumps to that line. `marsdawn export --json` reports failed diagrams in `diagramErrors`, '
                 "so a script or an agent can tell that a diagram didn't draw.",
        'know_h2': 'What to know',
        'know': "- You edit the Mermaid text. There is no visual diagram editor, and you can't drag boxes in "
                'the preview.\n'
                '- Which diagram types draw depends on the Mermaid version inside the app. MarsDawn 1.1.0 '
                "includes Mermaid 12.0.0. The kit's export tests render documents for flowcharts, sequence, "
                'class, state, entity-relationship, Gantt, pie, mindmap, journey, timeline and git graphs, '
                'among others.\n'
                "- MarsDawn has no AI model, so it doesn't write a diagram for you. The [flowchart "
                'template](/templates/flowchart/) has a prompt you can hand to your own agent.',
        'next_h2': 'Next',
        'next': '- Start from a diagram that already works: the [flowchart '
                'template](/templates/flowchart/).\n'
                '- Export it: [PDF export](/pdf/), or from a script, [Command Line](/cli/).\n'
                '- Not sure how to open the file? [How to open .md files on Mac](/view-markdown-on-mac/).',
        'try_h2': 'Try it on your Mac',
        'try': 'MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. '
               'No subscription, no account. It needs macOS 26 or later.\n'
               '\n'
               '[Download and try it free]({App Store 連結})'},
 'zh-hant': {'title': '在 Mac 上預覽 Mermaid 圖表，就在 Markdown 旁邊 · MarsDawn',
             'description': '在 Mac 上預覽 Mermaid 圖表：原始碼旁邊即時畫出來，快速查看和輸出 PDF 也看得到。圖表寫錯時，會顯示錯誤訊息和出錯的那一行。',
             'h1': '在 Mac 上預覽 Mermaid。',
             'intro': 'Mermaid 讓你用文字在 Markdown 檔案裡寫一張圖。多數編輯器只給你看那段文字。MarsDawn 會把圖畫出來：在原始碼旁邊的預覽、在 Finder '
                      '的快速查看，也在你輸出的 PDF 裡。',
             'example_h2': '用文字寫出圖',
             'example': '把圖放進標記為 `mermaid` 的程式碼區塊：',
             'code': '```mermaid\n'
                     'flowchart LR\n'
                     '    Write[寫 Markdown] --> Preview[即時預覽]\n'
                     '    Preview --> Export{要分享嗎？}\n'
                     '    Export -- PDF --> PDF[檔案 ▸ 輸出為 PDF⋯]\n'
                     '    Export -- 列印 --> Print[檔案 ▸ 列印⋯]\n'
                     '```',
             'after': '在 MarsDawn 裡，這個區塊會畫成一張流程圖：寫 Markdown，接著即時預覽，再到「要分享嗎？」這個選擇，分成輸出 PDF 和列印兩條路。',
             'where_h2': '圖會畫在哪裡',
             'where': '- **預覽裡。** 打開檔案，圖就在原始碼旁邊（⌘2）。頁面隨著打字更新，兩邊的窗格一起捲動。\n'
                      '- **快速查看裡。** 在 Finder 選取檔案按空白鍵，圖也會畫出來。\n'
                      '- **PDF 裡。** 「檔案 ▸ 輸出為 PDF⋯」和「檔案 ▸ 列印⋯」都會把圖畫進頁面，分頁時盡量不把一張圖切成兩半。PDF 使用主題的淺色配色。\n'
                      '- **命令列。** 免費的 `marsdawn export` 工具會把同樣的圖畫進 PDF，而且不需要 app。請看[命令列工具](/zh-hant/cli/)。\n'
                      '- **跟著外觀。** 預覽的外觀設定也會套用到圖表，所以圖會跟著淺色或深色。',
             'error_h2': '圖寫錯的時候',
             'error': 'Mermaid 畫不出一張圖時，預覽會顯示那張圖的原始碼，下方附上完整的錯誤訊息。如果錯誤訊息指出是哪一行，點一下訊息，編輯器就會跳到那一行。`marsdawn '
                      'export --json` 會在 `diagramErrors` 裡回報畫不出來的圖，所以腳本或 agent 知道有圖沒畫成。',
             'know_h2': '先知道的事',
             'know': '- 你編輯的是 Mermaid 文字。沒有視覺化的圖表編輯器，也不能在預覽裡拖動方塊。\n'
                     '- 哪些圖表類型畫得出來，取決於 app 裡內建的 Mermaid 版本。MarsDawn 1.1.0 內建 Mermaid 12.0.0。kit '
                     '的輸出測試會對流程圖、循序圖、類別圖、狀態圖、實體關聯圖、甘特圖、圓餅圖、心智圖、使用者旅程、時間軸、git 圖等類型各畫一份文件。\n'
                     '- MarsDawn 沒有 AI 模型，不會幫你寫圖。[流程圖範本](/zh-hant/templates/flowchart/)附有一段提示詞，可以交給你自己的 '
                     'agent。',
             'next_h2': '接下來',
             'next': '- 從一張已經能畫出來的圖開始：[流程圖範本](/zh-hant/templates/flowchart/)。\n'
                     '- 輸出：[輸出 PDF](/zh-hant/pdf/)；從腳本輸出，請看[命令列工具](/zh-hant/cli/)。\n'
                     '- 不確定怎麼打開檔案？請看[Mac 怎麼開 md 檔](/zh-hant/view-markdown-on-mac/)。',
             'try_h2': '在你的 Mac 上試試',
             'try': 'MarsDawn 可以免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。需要 macOS 26 以上。\n'
                    '\n'
                    '[立刻下載試用]({App Store 連結})'}}

VS_MACMD = {'en': {'title': 'MacMD Viewer vs. MarsDawn: a Markdown viewer or an editor · MarsDawn',
        'description': 'MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and '
                       'previews side by side: free for 14 days, then USD 4.99 once.',
        'h1': 'MacMD Viewer vs. MarsDawn.',
        'intro': ['Both are Mac apps for reading Markdown as a finished page. MacMD Viewer opens a `.md` '
                  'file and shows it; it is read-only by design and never saves changes to your file. '
                  'MarsDawn puts an editor next to the same kind of rendered preview, so you write and '
                  'review in one window. This page sets the two side by side, row by row, with a source for '
                  'every fact about MacMD Viewer, and says when MacMD Viewer is the better choice.',
                  "Checked against MacMD Viewer's own site and repository on 15 October 2026 (version 1.7.0, "
                  'released 10 October 2026). If something here is out of date, tell us at the address on '
                  'the [support page](/support/).'],
        'tables': [{'h2': 'What it is and what it does',
                    'rows': [['What it is',
                              'A viewer: "read-only and never saves changes to your source file" [S1, S9]',
                              'An editor with a live preview: Markdown on the left, the rendered page on the '
                              'right, in three layouts (source, split, preview)'],
                             ['Editing',
                              'No [S1, S7, S9]',
                              "Yes. The rendered page itself isn't editable; you edit the source beside it"],
                             ['Live preview',
                              'Renders the file; reloads when the file is saved by another editor [S9]',
                              'Updates as you type'],
                             ['Mermaid',
                              'Yes: flowcharts, sequence, state and Gantt diagrams, pie charts and more, '
                              'offline [S1, S3, S7]',
                              'Yes'],
                             ['Math',
                              'No: its README says it "does not render math (LaTeX/KaTeX)" [S7]',
                              'Yes, KaTeX'],
                             ['Code highlighting', 'Yes [S1, S9]', 'Yes'],
                             ['Themes',
                              '12 document themes [S1, S7]',
                              '4 built in (Dawn, Classic, Modern, Vivid), each with a light and a dark '
                              'palette, plus more in the theme gallery'],
                             ['Tabs', 'Yes, optional and off by default (since 1.6.0) [S5, S8]', 'Yes'],
                             ['PDF export',
                              'Yes, one continuous page, in the current theme, no watermark [S3, S9]',
                              "Yes, paginated pages in the theme's light palette; page breaks avoid "
                              'splitting short code blocks and tables'],
                             ['Print', 'Yes, through the macOS print dialog [S3, S9]', 'Yes'],
                             ['Quick Look in Finder',
                              'Yes, included; you enable it in System Settings; uses your theme [S4]',
                              'Yes, works with or without the trial; uses your theme'],
                             ['Command line',
                              'No standalone command-line tool is described. It has a `markdownviewer://` '
                              'URL scheme and a Claude Code plugin and hooks that open files in the viewer '
                              '[S6]',
                              'The free `marsdawn` tool: `marsdawn export` renders a PDF without the app, '
                              '`marsdawn open` opens a file at a line'],
                             ['Interface languages',
                              'Not stated in its own materials [S1, S3, S7]',
                              'English, Traditional Chinese, Simplified Chinese, Japanese, German, French, '
                              'Spanish and Korean'],
                             ['Requires',
                              'macOS 14 (Sonoma) or later; Apple Silicon and Intel [S1, S7]',
                              'macOS 26 (Tahoe) or later'],
                             ['Other platforms', 'Mac only [S1]', 'Mac only. No iPhone or iPad app']],
                    'head': ['', 'MacMD Viewer', 'MarsDawn']},
                   {'h2': 'Price and how you buy it',
                    'rows': [['Where you buy it',
                              'Its own site, Homebrew or Setapp; no Mac App Store listing [S2, S7]',
                              'The Mac App Store only'],
                             ['Price',
                              'USD 19.99 once, for one active Mac (movable to another Mac); Family Pack USD '
                              '39.99 for 3; 10 keys USD 129 [S2]',
                              'Free download, then USD 4.99 once'],
                             ['Trying it first',
                              'No trial or free tier; 14-day full refund on direct purchase [S2]',
                              '14-day free trial with everything on'],
                             ['Refunds', 'Through its own support, within 14 days [S2]', 'Through Apple'],
                             ['Updates',
                              'Updates within the current major version are free [S2]; the direct download '
                              'updates itself with Sparkle [S7]',
                              'Through the Mac App Store'],
                             ['Account needed', 'No [S2]', 'No'],
                             ['Subscription', 'No [S1, S2]', 'No']],
                    'head': ['', 'MacMD Viewer', 'MarsDawn']},
                   {'h2': 'What changes if you stop paying or trying',
                    'rows': [['After the trial or purchase window',
                              'No trial; keeps working once bought',
                              "If you don't unlock after 14 days, documents open with their content covered; "
                              'your files are untouched, Quick Look and the free `marsdawn` export keep '
                              'working']],
                    'head': ['', 'MacMD Viewer', 'MarsDawn']}],
        'pick': ['**Pick MacMD Viewer if** you only read Markdown and you want that to be guaranteed: it '
                 'never saves changes to your file [S1]. It also fits better if your Mac runs macOS 14 or '
                 "15, since MarsDawn needs macOS 26 [S1, S7]; if you would rather buy from a developer's own "
                 'site, Homebrew or Setapp than the Mac App Store [S2, S7]; if you want files an agent edits '
                 'to open in the viewer automatically, which it does through hooks for Claude Code, Cursor '
                 'and Windsurf [S6]; or if you want a single continuous-page PDF rather than paginated pages '
                 '[S9]. It has no trial, but it has a 14-day refund [S2].',
                 "**Pick MarsDawn if** the Markdown comes back for another pass. An agent's plan, README or "
                 'spec usually needs a fix, a reworded line or a new section, and in MarsDawn you do that in '
                 'the window where you are already reading. It also covers math (KaTeX), which MacMD Viewer '
                 "says it doesn't render [S7]; it ships in eight interface languages; it has a free "
                 '`marsdawn` command line that exports a PDF without the app; and its price is USD 4.99 '
                 'after a 14-day trial in which everything works.',
                 '**Either works if** you read Markdown on a recent Mac, want Mermaid diagrams drawn '
                 'properly and want Quick Look in Finder. Both do those.',
                 "**And you can use both.** They aren't exclusive: nothing stops you from keeping a "
                 'read-only viewer for what you only read and an editor for what you write.'],
        'faq': [['Does MacMD Viewer edit files?',
                 'No. It is read-only and, in its own words, never saves changes to your source file [S1, '
                 'S9]. It does have "Open in Text Editor" (since 1.7.0), which hands the file to another app '
                 '[S5].'],
                ['Is MacMD Viewer on the Mac App Store?',
                 "Its own pages list its site, Homebrew and Setapp, and don't mention the Mac App Store [S2, "
                 'S7]. MarsDawn is on the Mac App Store only.'],
                ['Can MarsDawn open the same files?',
                 'Yes. It opens `.md` files, and also plain text files and PDFs: text opens ready to edit as '
                 'UTF-8, and PDFs open in a viewer.'],
                ["What if I'm on macOS 14 or 15?",
                 'MacMD Viewer runs on macOS 14 or later [S1]. MarsDawn needs macOS 26 or later, and the '
                 'free `marsdawn` command-line tool can still export a PDF.'],
                ['Why is one USD 19.99 and the other USD 4.99?',
                 'They differ in what you get and how you pay. MacMD Viewer is a one-time purchase with a '
                 '14-day refund and no trial [S2]. MarsDawn is a free download with a 14-day trial, then a '
                 'one-time unlock. Neither is a subscription.']]},
 'zh-hant': {'title': 'MacMD Viewer 對比 MarsDawn：Markdown 檢視器還是編輯器 · MarsDawn',
             'description': 'MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 '
                            '解鎖一次。逐項比較，附來源。',
             'h1': 'MacMD Viewer 對比 MarsDawn。',
             'intro': ['兩者都是給 Mac 用的 app，都能把 Markdown 排版成完整的頁面來讀。MacMD Viewer 打開 `.md` '
                       '檔案並顯示出來；它設計上就是唯讀，不會儲存對檔案的任何更動。MarsDawn 則是在同樣的預覽旁邊放了編輯器，讓你在同一個視窗裡寫和讀。這一頁把兩者逐項並排，MacMD '
                       'Viewer 的每一項事實都附上來源，也會說明什麼情況下 MacMD Viewer 是比較好的選擇。',
                       '以上依 2026 年 10 月 15 日 MacMD Viewer 自己的網站和 repo 核對（版本 1.7.0，2026 年 10 月 10 '
                       '日發布）。如果有哪裡過時了，請照<a href="/zh-hant/support/">支援頁</a>上的聯絡方式告訴我們。'],
             'tables': [{'h2': '它是什麼、能做什麼',
                         'rows': [['是什麼',
                                   '檢視器：「唯讀，不會儲存對原始檔的更動」[S1, S9]',
                                   '有即時預覽的編輯器：左邊寫 Markdown，右邊看排版後的頁面，三種版面（原始碼、並排、預覽）'],
                                  ['編輯', '不能 [S1, S7, S9]', '可以。排版後的頁面本身不能直接編輯，要編輯旁邊的原始碼'],
                                  ['即時預覽', '顯示檔案；別的編輯器儲存檔案後會自動重新載入 [S9]', '打字時就更新'],
                                  ['Mermaid', '有：流程圖、循序圖、狀態圖、甘特圖、圓餅圖等，離線可用 [S1, S3, S7]', '有'],
                                  ['數學式', '沒有：它的 README 寫明「不顯示數學式（LaTeX／KaTeX）」[S7]', '有，KaTeX'],
                                  ['程式碼上色', '有 [S1, S9]', '有'],
                                  ['主題', '12 種文件主題 [S1, S7]', '內建 4 種（黎明、典雅、流行、活潑），各有淺色與深色，主題庫還有更多'],
                                  ['分頁', '有，選用，預設關閉（1.6.0 起）[S5, S8]', '有'],
                                  ['PDF 輸出',
                                   '有，單一連續頁面，用目前的主題，無浮水印 [S3, S9]',
                                   '有，分頁輸出，用主題的淺色配色；分頁時盡量不切開短的程式碼和表格'],
                                  ['列印', '有，走 macOS 的列印對話框 [S3, S9]', '有'],
                                  ['Finder 的快速查看', '有，已包含；要在系統設定裡啟用；使用你選的主題 [S4]', '有，不論有沒有試用都能用；使用你選的主題'],
                                  ['命令列',
                                   '沒有描述獨立的命令列工具。它有 `markdownviewer://` URL scheme，以及用來開啟檔案的 Claude Code 外掛和 '
                                   'hook [S6]',
                                   '免費的 `marsdawn` 工具：`marsdawn export` 不需要 app 就能輸出 PDF，`marsdawn open` '
                                   '能在指定行開啟檔案'],
                                  ['介面語言', '自己的資料沒有寫出 [S1, S3, S7]', '英文、繁體中文、簡體中文、日文、德文、法文、西班牙文和韓文'],
                                  ['系統需求',
                                   'macOS 14（Sonoma）以上；Apple 晶片與 Intel [S1, S7]',
                                   'macOS 26（Tahoe）以上'],
                                  ['其他平台', '只有 Mac [S1]', '只有 Mac，沒有 iPhone 或 iPad 版']],
                         'head': ['', 'MacMD Viewer', 'MarsDawn']},
                        {'h2': '價格與購買方式',
                         'rows': [['從哪裡買',
                                   '自己的網站、Homebrew 或 Setapp；沒有 Mac App Store 上架 [S2, S7]',
                                   '只在 Mac App Store'],
                                  ['價格',
                                   '一台使用中的 Mac 一次 USD 19.99（可以移到另一台 Mac）；Family Pack 3 把 USD 39.99；10 把 USD '
                                   '129 [S2]',
                                   '免費下載，之後一次 USD 4.99'],
                                  ['先試用', '沒有試用，也沒有免費版；直接購買 14 天內全額退款 [S2]', '14 天免費試用，所有功能都能用'],
                                  ['退款', '14 天內，透過它自己的支援信箱 [S2]', '透過 Apple'],
                                  ['更新', '同一主版本內的更新免費 [S2]；直接下載的版本用 Sparkle 自動更新 [S7]', '透過 Mac App Store'],
                                  ['需要帳號', '不用 [S2]', '不用'],
                                  ['訂閱', '沒有 [S1, S2]', '沒有']],
                         'head': ['', 'MacMD Viewer', 'MarsDawn']},
                        {'h2': '試用或購買之後',
                         'rows': [['狀態',
                                   '沒有試用；買了就一直能用',
                                   '14 天後沒有解鎖，文件仍會開啟但內容被遮住；檔案不會有任何改變，快速查看和免費的 `marsdawn` 輸出都照常']],
                         'head': ['', 'MacMD Viewer', 'MarsDawn']}],
             'pick': ['**選 MacMD Viewer，如果**你只讀 Markdown，而且希望「不會改到檔案」這件事是保證的：它不會儲存對檔案的任何更動 '
                      '[S1]。這些情況它也比較合適：你的 Mac 跑的是 macOS 14 或 15（MarsDawn 需要 macOS 26）[S1, '
                      'S7]；你比較想從開發者自己的網站、Homebrew 或 Setapp 買，而不是 Mac App Store [S2, S7]；你想讓 agent '
                      '改過的檔案自動在檢視器裡打開，它用 Claude Code、Cursor 和 Windsurf 的 hook 做到 [S6]；或者你想要單一連續頁面的 '
                      'PDF，而不是分頁的 PDF [S9]。它沒有試用，但有 14 天退款 [S2]。',
                      '**選 MarsDawn，如果** Markdown 讀完還要再改一輪。agent 寫的計畫、README 或規格，通常要修一個地方、改一句話或加一段，在 '
                      'MarsDawn 裡就在你正在讀的那個視窗裡改。它也支援數學式（KaTeX），MacMD Viewer 自己說不顯示 [S7]；介面有八種語言；有免費的 '
                      '`marsdawn` 命令列工具，不需要 app 就能輸出 PDF；價格是 14 天全功能試用後 USD 4.99。',
                      '**兩個都可以，如果**你在較新的 Mac 上讀 Markdown，想把 Mermaid 圖表畫好，也想在 Finder 用快速查看。兩者都做得到。',
                      '**也可以兩個都用。**兩者不互斥：只讀的檔案用唯讀檢視器，要寫的檔案用編輯器，並不衝突。'],
             'faq': [['MacMD Viewer 能編輯檔案嗎？',
                      '不能。它是唯讀的，照它自己的說法，不會儲存對原始檔的更動 [S1, S9]。它有「在文字編輯器中開啟」（1.7.0 起），是把檔案交給別的 app [S5]。'],
                     ['MacMD Viewer 在 Mac App Store 上嗎？',
                      '它自己的頁面列出的是官網、Homebrew 和 Setapp，沒有提到 Mac App Store [S2, S7]。MarsDawn 只在 Mac App '
                      'Store。'],
                     ['MarsDawn 能打開同樣的檔案嗎？', '可以。它打開 `.md` 檔案，也能打開純文字檔和 PDF：UTF-8 的文字檔可直接編輯，PDF 以檢視器開啟。'],
                     ['我的 Mac 是 macOS 14 或 15 呢？',
                      'MacMD Viewer 在 macOS 14 以上都能跑 [S1]。MarsDawn 需要 macOS 26 以上，不過免費的 `marsdawn` '
                      '命令列工具仍然可以輸出 PDF。'],
                     ['為什麼一個是 USD 19.99，一個是 USD 4.99？',
                      '兩者拿到的東西和付費方式不同。MacMD Viewer 是一次買斷，有 14 天退款，沒有試用 [S2]。MarsDawn 免費下載，有 14 '
                      '天試用，之後一次解鎖。兩者都不是訂閱。']]}}

VS_SOURCES = [['S1', 'https://macmdviewer.com/'],
 ['S2', 'https://macmdviewer.com/pricing'],
 ['S3', 'https://macmdviewer.com/features'],
 ['S4', 'https://macmdviewer.com/quicklook'],
 ['S5', 'https://macmdviewer.com/changelog'],
 ['S6', 'https://macmdviewer.com/docs/integrations'],
 ['S7', 'https://github.com/macmdviewer/MacMDViewer'],
 ['S8', 'https://macmdviewer.com/press'],
 ['S9', 'https://macmdviewer.com/product-facts.md'],
 ['S10', 'https://github.com/macmdviewer/MacMDViewer/releases']]

FILM_THEMES = {'en': {'heading': 'After the page is printed',
        'caption': 'A meeting around printed pages, a pen in the margin, a paper record on file.'},
 'zh-hant': {'heading': '頁面印出來之後', 'caption': '大家圍著印出來的頁面開會，有人拿筆在頁邊寫字，紙本紀錄收進檔案。'}}

SKILL_INSTALL = {'en': '<h2>Install it in Claude Code</h2>\n'
       '<p>The <code>marsdawn</code> command-line tool writes the skill for you, and the file it writes '
       "matches the version of <code>marsdawn</code> you have installed. If you don't have "
       '<code>marsdawn</code> yet, install it with <a href="https://brew.sh">Homebrew</a>:</p>\n'
       '<pre><code>brew install redtear1115/tap/marsdawn</code></pre>\n'
       '<p>Then install the skill:</p>\n'
       '<pre><code>marsdawn skill --install</code></pre>\n'
       "<p>That writes <code>~/.claude/skills/marsdawn/SKILL.md</code>, creating the folder if it isn't "
       'there. Because the file comes from your copy of <code>marsdawn</code>, it never describes an option '
       "your copy doesn't have.</p>\n"
       '<p>Claude Code loads it when a task calls for a PDF, or when it has written or revised a Markdown '
       "document for you to read, and you can run it yourself as <code>/marsdawn</code>. It's <a "
       'href="/cli/skill/SKILL.md">one short file</a> if you\'d like to read it first.</p>\n'
       '<h2>After you upgrade marsdawn</h2>\n'
       '<p>Homebrew upgrades <code>marsdawn</code> but leaves the skill where it was, so it stays at the old '
       'version until you refresh it:</p>\n'
       '<pre><code>marsdawn skill --install --force</code></pre>\n'
       '<p><code>--force</code> replaces the existing <code>SKILL.md</code>, including any changes you made '
       'to it. Without <code>--force</code>, if a different <code>SKILL.md</code> is already there, '
       '<code>marsdawn</code> leaves it alone, tells you it differs and exits with code 64 '
       '(<code>skill_differs</code>). If the file is already the current one, nothing changes.</p>\n'
       '<h2>For other agents</h2>\n'
       '<p>Add <code>--dir</code> with the folder where your agent keeps its skills, and '
       '<code>marsdawn</code> writes <code>SKILL.md</code> there instead:</p>\n'
       '<pre><code>marsdawn skill --install --dir &lt;path&gt;</code></pre>\n'
       '<p>The file is plain Markdown, instructions and commands, so an agent that loads instruction files '
       'can use it as it is.</p>\n'
       '<h2>Without Homebrew or the command-line tool</h2>\n'
       "<p>If you can't install <code>marsdawn</code> first, download the file instead:</p>\n"
       '<pre><code>mkdir -p ~/.claude/skills/marsdawn\n'
       'curl -fsSL {_SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>\n'
       '<p>This fetches the latest skill from this site, which may be ahead of an older '
       '<code>marsdawn</code>. Once you have the tool, <code>marsdawn skill --install --force</code> '
       'replaces it with the one that matches. You can also point an agent at the URL, or paste the file '
       'in.</p>',
 'zh-hant': '<h2>在 Claude Code 中安裝</h2>\n'
            '<p>命令列工具 <code>marsdawn</code> 會幫你寫好這個 skill，寫進去的內容和你已安裝的 <code>marsdawn</code> 版本相符。如果還沒有 '
            '<code>marsdawn</code>，先用 <a href="https://brew.sh">Homebrew</a> 安裝：</p>\n'
            '<pre><code>brew install redtear1115/tap/marsdawn</code></pre>\n'
            '<p>然後安裝 skill：</p>\n'
            '<pre><code>marsdawn skill --install</code></pre>\n'
            '<p>這會把 skill 寫到 <code>~/.claude/skills/marsdawn/SKILL.md</code>，資料夾不存在時會一併建立。因為檔案是由你手上的 '
            '<code>marsdawn</code> 產生的，裡面不會出現你這個版本沒有的選項。</p>\n'
            '<p>需要做出 PDF，或寫好、改好一份要給你讀的 Markdown 文件時，Claude Code 會自動載入它，你也可以用 <code>/marsdawn</code> '
            '自己執行。想先看內容的話，它只是<a href="/cli/skill/SKILL.md">一個簡短的檔案</a>。</p>\n'
            '<h2>升級 marsdawn 之後</h2>\n'
            '<p>Homebrew 會升級 <code>marsdawn</code>，但不會動 skill，所以它會停在舊版本，要自己更新：</p>\n'
            '<pre><code>marsdawn skill --install --force</code></pre>\n'
            '<p><code>--force</code> 會取代現有的 <code>SKILL.md</code>，包括你自己改過的地方。不加 <code>--force</code> '
            '的話，如果那裡已經有內容不同的 <code>SKILL.md</code>，<code>marsdawn</code> 不會動它，會告訴你內容不同，並以代碼 '
            '64（<code>skill_differs</code>）結束。檔案已經是最新的，就什麼都不改。</p>\n'
            '<h2>給其他 agent</h2>\n'
            '<p>加上 <code>--dir</code>，指到你的 agent 放 skill 的資料夾，<code>marsdawn</code> 就會把 '
            '<code>SKILL.md</code> 寫到那裡：</p>\n'
            '<pre><code>marsdawn skill --install --dir &lt;path&gt;</code></pre>\n'
            '<p>這個檔案是純 Markdown，只有說明和指令，會讀指令檔的 agent 可以直接用。</p>\n'
            '<h2>沒有 Homebrew，或沒有命令列工具</h2>\n'
            '<p>如果沒辦法先安裝 <code>marsdawn</code>，就直接下載這個檔案：</p>\n'
            '<pre><code>mkdir -p ~/.claude/skills/marsdawn\n'
            'curl -fsSL {_SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>\n'
            '<p>這會從本站抓最新的 skill，可能比較舊的 <code>marsdawn</code> 還新。等你裝好命令列工具，再執行 <code>marsdawn skill --install '
            '--force</code>，就會換成和它相符的版本。你也可以讓 agent 讀這個網址，或直接貼給它。這個檔案是英文的。</p>'}

CLI_SKILL_LINE = {'en': '<p>Using a coding agent? Run <code>marsdawn skill --install</code> to add <a href="/cli/skill/">the '
       'marsdawn skill</a>: one file that teaches it to open what it wrote in MarsDawn for your review, and '
       'to export PDFs.</p>',
 'zh-hant': '<p>在用寫程式的 agent 嗎？執行 <code>marsdawn skill --install</code> 來加上 <a '
            'href="/zh-hant/cli/skill/">marsdawn skill</a>：一個檔案，教它把自己寫的文件在 MarsDawn 裡打開給你審閱，也能輸出 PDF。</p>'}

AGENTS_SKILL_ITEM = {'en': '<li>To have a coding agent do this for you, run <code>marsdawn skill --install</code> to add <a '
       'href="/cli/skill/">the marsdawn agent skill</a>.</li>',
 'zh-hant': '<li>讓寫程式的 agent 幫你做這件事：執行 <code>marsdawn skill --install</code> 來加上 <a '
            'href="/zh-hant/cli/skill/">marsdawn 的 agent skill</a>。</li>'}
