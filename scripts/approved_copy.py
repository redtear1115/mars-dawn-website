"""Owner-approved copy (en and zh-Hant), loaded programmatically from the vault drafts and never retyped.

Do not edit by hand: change the source and regenerate. Strings are the Markdown inside the sources' fenced
blocks (and, for table cells and bullets, the lines themselves); scripts/rich_pages.py turns them into HTML.

OPEN_MD and MERMAID: website #227, source
  <vault>/MarsDawn/協作/給擁有者/open-md-and-mermaid-copy-2026-10-15.md
  (owner-approved 2026-10-15, "all as recommended"). One declared edit, owner decision 7 (option b): the sentence(s)
  [' A diagram type that a newer Mermaid adds may show the error display instead.', '較新的 Mermaid 才加入的圖表類型，可能會顯示錯誤訊息。']
  were removed from MERMAID[...]["know"].
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
