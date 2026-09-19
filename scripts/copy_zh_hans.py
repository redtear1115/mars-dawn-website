"""Simplified Chinese (zh-Hans) copy for the MarsDawn site, translated from the zh-hant copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': '隱私權政策', 'support': '支援', 'cli': '命令列工具', 'agents': '給 AI agent 的 marsdawn 參考', 'using_cli': '使用 CLI', 'markdown-to-pdf': 'Markdown 轉 PDF', 'skill': '給 agent 的 skill', 'view-markdown-on-mac': '在 Mac 上看 Markdown', 'vs-macmd-viewer': 'MacMD Viewer 對比 MarsDawn', 'updated': f"最後更新：{k.UPDATED}", 'tagline': '讀 agent 寫的 Markdown。', 'footer_store': 'MarsDawn 即將在 Mac App Store 上架。', 'more': '其他頁面', 'yours': '你寫的內容留在你的 Mac 上', 'pay-once': '免費試用，買一次就好', 'pdf': '輸出 PDF', 'native': '為 Mac 而做', 'limits': 'MarsDawn 做不到的事'}
    store_chip = '即將在 Mac App Store 上架'
    schema_notes = {'export': 'export 成功', 'open': 'open 成功，marsdawn 0.3.0 以後', 'error': '兩個指令的失敗結果', 'open_v1': 'open 成功，marsdawn 0.2.x，當時 <code>opened</code> 是路徑清單'}
    example_plan = '# 計畫：讓輸出更快\n\n這份計畫由 agent 撰寫，你審閱後再把它轉成 PDF。\n\n## 步驟\n\n| 步驟 | 負責 | 狀態 |\n|------|------|------|\n| 找出慢的頁面 | Agent | 完成 |\n| 快取算好的圖表 | Agent | 審閱中 |\n\n目標是 50 頁的文件在 $t < 2\\,\\text{s}$ 內完成：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  草稿 --> 審閱 --> 發佈\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'yours': ('你寫的內容留在你的 Mac 上', '不需要帳號，沒有同步，也沒有雲端。'), 'pay-once': ('免費試用，買一次就好', '免費試用 14 天，之後 USD 4.99 買一次，沒有訂閱。'), 'pdf': ('輸出 PDF', '圖表、程式碼上色、經過安排的分頁。'), 'native': ('為 Mac 而做', '原生視窗、分頁、自動儲存、快速查看。'), 'limits': ('MarsDawn 做不到的事', '購買前先知道。')}
    trait_nav_heading = 'MarsDawn 是什麼樣的 app'
    figure_list_label = '這張截圖裡'
    figures = {
        'index': {
            "alt": 'MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。',
            "callouts": [],
        },
        'yours': {
            "alt": 'MarsDawn 以 Classic 主題顯示文件，預覽佔滿整個視窗。',
            "callouts": ['你 Mac 上的一個檔案，存在你選的地方。', '整條工具列只有主題和版面，沒有任何需要登入的地方。'],
        },
        'pay-once': {
            "alt": 'MarsDawn 使用 Vivid 主題，左邊是 Markdown 原始碼，右邊是排版後的頁面。',
            "callouts": ['編輯器的 Markdown 語法上色，包含在內。', '所有主題和版面都包含在內。', 'Mermaid 圖表，包含在內。', '程式碼上色，包含在內。'],
        },
        'pdf': {
            "alt": '用 MarsDawn 輸出的 PDF，在內建的 PDF 檢視器中開啟，旁邊有頁面縮圖。',
            "callouts": ['Mermaid 圖表直接畫進 PDF。', '程式碼保留語法上色。'],
        },
        'native': {
            "alt": 'MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。',
            "callouts": ['原生的 Mac 視窗。', 'Mac 原生的文字編輯器，附 Markdown 語法上色。', '⌘1 原始碼、⌘2 並排、⌘3 預覽。', '頁面會隨著打字更新。'],
        },
        'limits': {
            "alt": 'MarsDawn 的深色模式，左邊是 Markdown 原始碼，右邊是排版後的頁面。',
            "callouts": ['一個視窗一份文件，就在這台 Mac 上。', '你在這裡寫 Markdown。', '工具列只有主題和版面，沒有外掛選單。', '這一側用來閱讀，不能直接編輯。'],
        },
    }
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn：Mac 上的 Markdown 編輯器，即時預覽',
        "description": '原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">為 AI 工作流程而生</p>
  <h1>讓 agent 寫的 Markdown，被好好讀過一遍。</h1>
  <p>AI agent 寫 Markdown，你在 MarsDawn 裡讀，原始碼和排版後的頁面並排顯示，再把修改意見交回去。</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">整個循環</h2>
<ol class="loop-steps">
  <li><strong>Agent 動筆。</strong>你的程式碼助手或寫作 agent 先寫出 Markdown：README、規格文件，或一份筆記。</li>
  <li><strong>你在 MarsDawn 裡讀。</strong>打開檔案，看排版後的頁面，Mermaid 圖表和程式碼上色都在，旁邊就是原始碼。</li>
  <li><strong>Agent 修改。</strong>提出修改意見，agent 改好之後，再打開來讀一次。</li>
</ol>
<p>Agent 也能直接操作 MarsDawn：免費的 <a href="/zh-hans/cli/">marsdawn</a> 命令列工具能開啟檔案供你檢閱，也能輸出 PDF，並提供給腳本使用的 JSON 輸出。細節請看<a href="/zh-hans/cli/agents/">給 AI agent 的 marsdawn 參考</a>。</p>
""",
    }
    pages['yours'] = {
        "title": '不用帳號、不上雲端的 Mac Markdown 編輯器 · MarsDawn',
        "description": 'MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。',
        "intro": f"""
<section class="intro">
  <h1>你寫的內容，留在你的 Mac 上。</h1>
  <p>MarsDawn 不需要帳號，沒有同步，也沒有雲端。它打開檔案、讓你寫，再存回你選的位置。</p>
</section>
""",
        "body": f"""
<h2>這代表什麼</h2>
<ul>
  <li>不需要帳號，不用註冊，也不用登入。</li>
  <li>不會同步到雲端，文件存在哪裡就留在哪裡。</li>
  <li>不追蹤任何行為。MarsDawn 不收集任何關於你的資料，App Store 隱私權標示為「未收集資料」。</li>
  <li>網路圖片在你選擇載入之前一律不載入，打開文件不會讓任何伺服器知道你讀了它。選擇載入時，也只走 https。</li>
  <li>本機圖片在你授權資料夾存取後，就會顯示在預覽中。</li>
</ul>
<p>完整說明請看<a href="/zh-hans/privacy/">隱私權政策</a>。</p>
""",
    }
    pages['pay-once'] = {
        "title": '免費試用，買一次就好 · MarsDawn',
        "description": 'MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。',
        "intro": f"""
<section class="intro">
  <h1>先全部試用，再買一次。</h1>
  <p>MarsDawn 可以免費下載。開始 14 天試用後，所有功能都能使用；試用結束後想繼續使用，花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。</p>
</section>
""",
        "body": f"""
<h2>怎麼運作</h2>
<ul>
  <li>在 Mac App Store 免費下載 MarsDawn。</li>
  <li>開始試用後，14 天內所有功能都能使用：所有主題與版面、PDF 輸出與列印、快速查看，以及 Siri 和捷徑動作。</li>
  <li>試用結束後想繼續使用，花 USD 4.99 解鎖一次就好。這是 App 內購買，不是訂閱，不會自動續費，之後也不會再扣款。</li>
  <li>試用本身也不會扣款。試用結束時，除非你選擇解鎖，否則不會購買任何東西。</li>
  <li>不需要帳號，MarsDawn 從不要求你建立帳號。</li>
</ul>
<h2>如果沒有解鎖</h2>
<ul>
  <li>14 天後，在你解鎖之前，無法在 MarsDawn 中閱讀、編輯、輸出或列印文件。文件仍會開啟，但內容會被遮住。</li>
  <li>你的檔案不會有任何改變。它們就是你 Mac 上的一般檔案，在 Finder 中用「快速查看」依然看得到。</li>
  <li>免費的 <a href="/zh-hans/cli/"><code>marsdawn</code> 命令列工具</a>不受試用影響，依然能把它們匯出成 PDF。</li>
  <li>如果試用結束時有文件正開在 MarsDawn 裡，你輸入的文字不會遺失，可以用「檔案」▸「另存新檔⋯」保存。</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": '在 Mac 把 Markdown 輸出成 PDF，圖表也在 · MarsDawn',
        "description": '在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。',
        "intro": f"""
<section class="intro">
  <h1>PDF 看起來就是你寫的那一頁。</h1>
  <p>輸出成 PDF 或列印，使用主題的淺色配色。圖表和程式碼上色都會保留，分頁位置也經過安排。</p>
</section>
""",
        "body": f"""
<h2>這代表什麼</h2>
<ul>
  <li>Mermaid 圖表直接畫進 PDF。</li>
  <li>程式碼區塊保留語法上色。</li>
  <li>分頁時會盡量不讓標題落在頁尾，也不切開程式碼、表格和圖表。</li>
  <li>任何版面都能輸出，只顯示原始碼時也可以。</li>
</ul>
<p>免費的 <a href="/zh-hans/cli/">marsdawn 命令列工具</a>使用同一套輸出程式，所以腳本或 AI agent 也能得到一樣的 PDF。</p>
""",
    }
    pages['native'] = {
        "title": '原生的 Mac Markdown app：分頁、快速查看 · MarsDawn',
        "description": '真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。',
        "intro": f"""
<section class="intro">
  <h1>用 Mac 原生的元件做的。</h1>
  <p>視窗、分頁、選單和文字編輯器都是 Mac 原生的。排版後的頁面由 Safari 使用的 WebKit 引擎繪製。</p>
</section>
""",
        "body": f"""
<h2>這代表什麼</h2>
<ul>
  <li>原始碼、並排、預覽三種版面，一個快捷鍵切換（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>兩側同步捲動，正在編輯的段落一直在眼前。</li>
  <li>編輯器內建 Markdown 語法上色，顏色與預覽主題一致。</li>
  <li>原生視窗、分頁、自動儲存和版本記錄。</li>
  <li>快速查看：在 Finder 選取 Markdown 檔按空白鍵就能預覽，圖表也會顯示。</li>
  <li>Siri 和捷徑：用範本新增文件、在筆記收件匣加上一行，或重新打開最近的文件。</li>
  <li>支援{k.APP_UI_LANGUAGES}。</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'MarsDawn 做不到的事 · MarsDawn',
        "description": '沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。',
        "intro": f"""
<section class="intro">
  <h1>MarsDawn 做不到的事。</h1>
  <p>有些功能是刻意不做的。如果你需要其中一項，現在知道總比買了之後才發現好。</p>
</section>
""",
        "body": f"""
<h2>刻意不做的</h2>
<ul>
  <li><strong>同步：</strong>MarsDawn 不會同步文件，文件存在哪裡就留在哪裡；要在另一台 Mac 上使用，請放在你原本就會同步的資料夾。</li>
  <li><strong>iPhone 和 iPad：</strong>沒有這兩個平台的版本，MarsDawn 只給 Mac。</li>
  <li><strong>外掛：</strong>MarsDawn 沒有外掛或擴充功能。</li>
  <li><strong>分享：</strong>沒有帳號，也不能共同編輯，因為 MarsDawn 是給一個人在自己的 Mac 上用的。</li>
  <li><strong>編輯：</strong>你在左邊寫 Markdown，在右邊閱讀排版後的頁面；頁面本身不能直接編輯。</li>
  <li><strong>格式：</strong>MarsDawn 能輸出 PDF 和列印，不能輸出 Word 檔。</li>
  <li><strong>主題：</strong>內建 Dawn、Classic、Modern 和 Vivid，每種都有淺色與深色，無法安裝其他主題。</li>
  <li><strong>其他檔案：</strong>純文字檔和 PDF 以唯讀方式開啟。</li>
  <li><strong>試用結束後：</strong>如果 14 天試用結束後沒有解鎖，就無法在 MarsDawn 中閱讀和編輯文件：文件會開啟，但內容會被遮住。你的檔案維持原樣，「快速查看」依然看得到，免費的命令列工具也依然能匯出它們。</li>
  <li><strong>系統：</strong>MarsDawn 需要 macOS 26 以上。</li>
</ul>
""",
    }
    pages['support'] = {
        "title": '支援 · MarsDawn',
        "description": 'MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。',
        "body": f"""
<section class="intro">
  <h1>支援</h1>
  <p>macOS Markdown 編輯器 MarsDawn 的使用說明。</p>
</section>

<section class="contact">
  <h2>寫信給我們</h2>
  <a class="email" href="mailto:{k.EMAIL}?subject=MarsDawn%20support">{k.EMAIL}</a>
  <p>請附上你的 macOS 版本與 MarsDawn 版本（MarsDawn › 關於 MarsDawn）。如果畫面看起來不對，附上截圖或一份小的範例文件會很有幫助。</p>
</section>

<section class="faq">
  <h2>常見問題</h2>

  <h3>MarsDawn 需要什麼環境？</h3>
  <p>macOS 26 Tahoe 或更新版本的 Mac，Apple 晶片或 Intel 皆可。</p>

  <h3>怎麼切換編輯器與預覽？</h3>
  <p>按 <kbd>⌘1</kbd> 只看原始碼、<kbd>⌘2</kbd> 左右並排、<kbd>⌘3</kbd> 只看預覽。「顯示方式」選單和工具列也有相同選項。</p>

  <h3>文件裡的圖片沒有顯示。</h3>
  <ul>
    <li><strong>Mac 上的圖片：</strong>先儲存文件，再按預覽中的「授權資料夾存取⋯」，選擇圖片所在的資料夾。MarsDawn 會記住這個資料夾，你可以到 MarsDawn › 設定⋯ › 資料夾存取查看。</li>
    <li><strong>網路上的圖片：</strong>網路圖片在你按下預覽上方的「載入圖片」之前不會載入。想要一律載入，可在設定中開啟「自動載入網路圖片」。</li>
  </ul>

  <h3>怎麼加入圖片？</h3>
  <p>把圖片拖進編輯器，或直接貼上。文件需要先儲存：MarsDawn 會把圖片複製到文件旁的 <code>assets</code> 資料夾，並幫你寫好 Markdown 連結。</p>

  <h3>Mermaid 圖表顯示錯誤。</h3>
  <p>MarsDawn 會顯示圖表的原始碼，下方附上 Mermaid 錯誤訊息的第一行。請檢查訊息指出的那一行，例如箭頭後面缺了目標，或括號沒有閉合。</p>

  <h3>怎麼產生 PDF？</h3>
  <p>選擇「檔案 › 輸出為 PDF⋯」（<kbd>⌥⌘E</kbd>）。不論目前是哪種版面，PDF 都會使用預覽主題的淺色版本並自動分頁。「檔案 › 列印⋯」會印出相同的頁面。</p>

  <h3>怎麼搭配 Siri 或捷徑使用？</h3>
  <p>打開「捷徑」App 搜尋 MarsDawn，就能找到「新增 Markdown 文件」、「新增筆記到收件匣」與「打開最近的文件」。要新增筆記之前，請先到 MarsDawn › 設定⋯ › 筆記資料夾選擇資料夾，筆記會加到該資料夾的 <code>Inbox.md</code>。</p>

  <h3>設定在哪裡？</h3>
  <p>MarsDawn › 設定⋯（<kbd>⌘,</kbd>），包含外觀、圖片、筆記資料夾、資料夾存取與預覽主題。</p>

  <h3>怎麼申請退款？</h3>
  <p>購買由 Apple 處理，請到 <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> 申請退款。</p>
</section>
""",
    }
    pages['privacy'] = {
        "title": '隱私權政策 · MarsDawn',
        "description": 'MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。',
        "body": f"""
<section class="intro">
  <h1>隱私權政策</h1>
  <p>macOS 的 Markdown 編輯器 MarsDawn 如何處理你的資訊。</p>
  <p class="updated">最後更新：{k.PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn 不收集任何關於你的資料。</strong>沒有帳號、沒有分析、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。</p></div>

<h2>留在你 Mac 上的東西</h2>
<ul>
  <li><strong>你的文件。</strong>MarsDawn 只讀寫你打開、儲存或選擇的檔案與資料夾，App 不會把它們上傳到任何地方。</li>
  <li><strong>你的設定。</strong>外觀、預覽主題、視窗版面和圖片偏好，都存在 App 自己的偏好設定裡。</li>
  <li><strong>你授權的資料夾。</strong>當你讓 MarsDawn 顯示某個資料夾裡的圖片或網頁檔案，或選擇筆記資料夾時，App 會保存 macOS 書籤，以便之後再次開啟。你在側邊欄開啟的資料夾，MarsDawn 會保持可讀寫，直到你在設定中移除為止，而不只是在那個視窗開著的時候。你隨時可以到 MarsDawn › 設定⋯ 移除。</li>
</ul>

<h2>MarsDawn 什麼時候會連上網路</h2>
<p>MarsDawn 可以完全離線使用，只有在<strong>你自己選擇時</strong>，才會為引用網路內容的文件連網：</p>
<ul>
  <li><strong>Markdown 文件。</strong>網路圖片預設不載入，只有在你按下預覽中的「載入圖片」，或在設定中開啟「自動載入網路圖片」後才會載入。Markdown 文件引用的其他網路內容一律不載入。</li>
  <li><strong>HTML 文件。</strong>HTML 文件開啟時是靜態的：它的程式碼不會執行，也不會從網路載入任何東西。如果文件含有可以執行的程式碼，你可以針對這份文件選擇「顯示方式 › 執行這份文件」。之後它自己的程式碼會一直執行，直到你停止它、文件重新載入，或關閉視窗為止。這個選擇不會被記住，也不是一項設定。執行期間，這份文件可以透過網路傳送資料，並讀取它所在資料夾及其子資料夾中的圖片、樣式表、字型與媒體檔案。從網路下載的程式碼一律不會執行。</li>
</ul>
<p>MarsDawn 只透過 https 載入網路內容。http 位址一律不會載入，任何設定都無法開啟，MarsDawn 也不會自動改寫成 https。在 Markdown 文件中，預覽會以佔位圖示代替。</p>
<p>載入網路內容時，你的 Mac 會直接向存放內容的伺服器發出請求。和所有網路請求一樣，這些伺服器會看到你的 IP 位址與請求的內容。MarsDawn 的開發者不會收到任何這類資訊。</p>
<p>在預覽中點選的連結會用你的預設瀏覽器打開，適用該瀏覽器的隱私做法。音訊與影片不會自動播放。</p>

<h2>Siri、捷徑和 Spotlight</h2>
<p>MarsDawn 提供 Siri、捷徑 App 和 Spotlight 可用的動作，例如新增文件或加入筆記。使用時，你提供的文字會交給你 Mac 上的 MarsDawn，並只存到動作指定的位置（新文件，或你所選筆記資料夾中的 <code>Inbox.md</code>）。對 Siri 說的話由 Apple 依 <a href="https://www.apple.com/legal/privacy/">Apple 隱私權政策</a> 處理。</p>

<h2>輸出 PDF 和列印</h2>
<p>輸出 PDF 和列印都在你的 Mac 上完成。PDF 存在你選擇的位置，列印則透過 macOS 送到你選的印表機。</p>

<h2>marsdawn 命令列工具</h2>
<p>另外發佈、可自由選用的 <code>marsdawn</code> 命令列工具，同樣完全在你的 Mac 上執行：只讀取你指定的 Markdown 檔，並寫出你要求的 PDF。只有在加上 <code>--allow-remote-images</code> 時才會載入網路圖片。</p>

<h2>兒童</h2>
<p>MarsDawn 不向任何人收集資料，包括兒童。</p>

<h2>購買</h2>
<p>MarsDawn 將透過 Mac App Store 販售，付款會由 Apple 依其條款處理，開發者不會取得你的付款資訊。</p>

<h2>政策變更</h2>
<p>如果 MarsDawn 未來處理資料的方式有所改變，本頁會在該版本推出前更新，頁首的日期也會一併更改。</p>

<h2>聯絡我們</h2>
<p>隱私相關問題：<a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
""",
    }
    pages['view-markdown-on-mac'] = {
        "title": '在 Mac 上怎麼看 Markdown 檔案 · MarsDawn',
        "description": 'md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。',
        "body": f"""
<section class="intro">
  <h1>在 Mac 上，怎麼看 Markdown 檔案。</h1>
  <p><code>.md</code> 檔案是純文字。標題、粗體、表格和圖表，都是用記號寫成的：<code>#</code> 代表標題，<code>**</code> 包住粗體，直線符號畫出表格，<code>mermaid</code> 程式碼區塊則是一張圖。用純文字編輯器打開，看到的就是這些記號。想照作者的意思讀到排好的頁面，就需要有東西把它排版出來。</p>
</section>
<h2>現在就能用，而且免費：轉成 PDF</h2>
<p>免費的 <code>marsdawn</code> 命令列工具，能把 Markdown 檔案排版成 PDF，任何一台 Mac 都打得開。表格、數學式、Mermaid 圖表和程式碼上色都會排好，而且不需要安裝其他東西，連 MarsDawn app 都不用。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> 會在 Markdown 檔案旁邊寫出 <code>notes.pdf</code>，<code>open</code> 會用你的 PDF 檢視器打開它。這個工具需要 macOS 15 以上。完整步驟和一頁實際匯出的結果，請看<a href="/zh-hans/markdown-to-pdf/">Markdown 轉 PDF</a>。</p>
<h2>即將推出：在 MarsDawn 裡讀</h2>
<p>MarsDawn 是為 Mac 做的 Markdown 編輯器，即將在 Mac App Store 上架。打開 <code>.md</code> 檔案，排好的頁面就在原始碼旁邊：</p>
<ul>
  <li>預覽會隨著你打字即時更新，兩邊的窗格一起捲動。</li>
  <li>Mermaid 流程圖和循序圖直接畫在預覽裡，程式碼區塊也會上色。</li>
  <li>在 Finder 裡對 Markdown 檔案按空白鍵，就有「快速查看」預覽，圖表也在。</li>
  <li>想改的時候，原始碼就在旁邊。MarsDawn 是編輯器，不只是檢視器。</li>
</ul>
<p>如果這份檔案是 AI agent 寫的，這正是 MarsDawn 要支援的循環：agent 寫，你讀排好的頁面，agent 再修改。請看<a href="/zh-hans/">首頁</a>，想讓 agent 幫你開檔案，請看<a href="/zh-hans/cli/agents/">給 AI agent 的 marsdawn 參考</a>。</p>
<h2>接下來</h2>
<ul>
  <li>命令列工具的所有選項：<a href="/zh-hans/cli/">命令列工具</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hans/limits/">這份清單</a>。</li>
</ul>
""",
    }
    pages['markdown-to-pdf'] = {
        "title": 'Markdown 轉 PDF 工具：在 Mac 用命令列轉檔 · MarsDawn',
        "description": '免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。',
        "body": f"""
<section class="intro">
  <h1>Markdown 轉 PDF 工具：在 Mac 上用命令列轉檔。</h1>
  <p>免費的 <code>marsdawn</code> 工具只要一個指令，就能把 Markdown 檔案轉成 PDF。表格、數學式、Mermaid 圖表和程式碼上色，都會照原始檔的樣子呈現，而且不需要安裝其他東西，連 MarsDawn app 都不用。</p>
</section>
<h2>安裝</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上。這個工具需要 macOS 15 以上，<code>marsdawn --version</code> 會印出你裝到的版本。</p>
<h2>存一份文件</h2>
<p>把下面的內容貼進一個叫 <code>plan.md</code> 的檔案：</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>匯出</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>它會在原始檔旁邊寫出 <code>plan.pdf</code>，並印出存放的位置：</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>這是那一頁，擷取自 <code>marsdawn</code> 0.5.0 的實際執行結果：</p>
<p><img class="pdf-page" src="/assets/cli/plan-zh-hans.png" alt="匯出的 PDF：標題、步驟表格、行內與獨立的數學式、「草稿、審閱、發佈」流程圖，以及一行上色的 Swift 程式碼。" width="989" height="930"></p>
<h2>選主題、紙張大小和檔名</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>：dawn、classic、modern 或 vivid，使用主題的淺色配色。沒有指定時，<code>export</code> 會用 <code>$MARSDAWN_THEME</code>，再來才是 dawn。</li>
  <li><code>--paper</code>：a4 或 letter，預設是 a4。</li>
  <li><code>-o</code>：PDF 要寫到哪裡，而不是寫在原始檔旁邊。</li>
  <li><code>--allow-remote-images</code>：轉檔時載入網路上的圖片。沒加這個選項就不會載入。</li>
</ul>
<h2>如果沒有成功</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> 代表 Homebrew 正在從原始碼建置 <code>marsdawn</code>，這在 Intel Mac 上會發生。從 App Store 安裝 Xcode 26 以上，再重新安裝一次。</li>
  <li><code>marsdawn: No such file: …</code> 路徑沒有指到檔案。確認檔名，或在檔案所在的資料夾裡執行指令。</li>
  <li><code>… already exists. Pass --force to replace it.</code> 同名的 PDF 已經存在。加上 <code>--force</code> 覆蓋它，或用 <code>-o</code> 寫到別的地方。</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> 主題或紙張大小不是它認得的。主題有 dawn、classic、modern 和 vivid，紙張是 a4 或 letter。</li>
</ul>
<h2>接下來</h2>
<ul>
  <li>所有選項和它印出的 JSON：<a href="/zh-hans/cli/">命令列工具</a>。</li>
  <li>讓寫程式的 agent 幫你做這件事：<a href="/zh-hans/cli/skill/">marsdawn 的 agent skill</a>。</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer 對比 MarsDawn：檢視器與編輯器 · MarsDawn',
        "description": 'MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer 對比 MarsDawn。</h1>
  <p>兩者都是給 Mac 用的 app，都能把 Markdown 排版出來讀。MacMD Viewer 打開 <code>.md</code> 檔案，顯示排好版的頁面，但不能編輯它。MarsDawn 則是在同樣的預覽旁邊放了編輯器，讓你在同一個視窗裡寫和讀。以下逐項比較兩者的差異。</p>
</section>
<h2>如果你只需要讀，不需要編輯</h2>
<p>如果你的工作就是讀別人寫好的 Markdown，完全不用碰原始碼，MacMD Viewer 是合理的選擇：它就是為這件事做的，現在就能買，也能在比較舊的 macOS 上跑。當閱讀不是全部的工作時，MarsDawn 才值得，因為 agent 寫的 Markdown 通常還要再改一輪。</p>
<h2>各自能做什麼</h2>
<ul>
  <li><strong>編輯：</strong>MacMD Viewer 設計上就是唯讀。MarsDawn 邊編輯原始碼邊在旁邊排版，打字的同時就看得到改動。</li>
  <li><strong>預覽主題：</strong>MacMD Viewer 內建 12 種文件主題。MarsDawn 有四種：Dawn、Classic、Modern 和 Vivid，各有淺色與深色。</li>
  <li><strong>圖表與數學式：</strong>兩者都能畫出 Mermaid 圖表、也都有程式碼上色。MarsDawn 還能排版 KaTeX 數學式；MacMD Viewer 自己的介紹頁沒有提到數學式排版。</li>
  <li><strong>Finder 整合：</strong>兩者都有 Finder 的快速查看擴充功能，對 <code>.md</code> 檔案按空白鍵就能看到排好版的頁面。</li>
  <li><strong>PDF 與列印：</strong>兩者都能把排好版的頁面輸出或列印成 PDF。</li>
  <li><strong>系統需求：</strong>MacMD Viewer 需要 macOS 14（Sonoma）以上。MarsDawn 需要 macOS 26（Tahoe）以上。</li>
  <li><strong>語言：</strong>MarsDawn 的介面有{k.APP_UI_LANGUAGES}。MacMD Viewer 自己的資料沒有寫出介面語言，這頁就不比較這一項。</li>
</ul>
<h2>價格與購買方式</h2>
<ul>
  <li><strong>從哪裡買：</strong>MacMD Viewer 從自己的網站直接下載，也上架 Homebrew 和 Setapp，但不在 Mac App Store 上；MarsDawn 只在 Mac App Store 上架。</li>
  <li><strong>價格：</strong>MacMD Viewer 一台 Mac 一次 USD 19.99（三台的組合包和大量授權更貴）。MarsDawn 免費下載，之後以 USD 4.99 一次解鎖。</li>
  <li><strong>先試用：</strong>MacMD Viewer 沒有免費試用，直接購買改用 14 天內可退款的保證。MarsDawn 在你付費之前，先給你 14 天的試用。</li>
  <li><strong>退款與更新：</strong>MacMD Viewer 的退款和更新都在它自己的網站上處理。MarsDawn 透過 Apple 購買，退款和更新都走 Apple 的標準流程。</li>
  <li><strong>帳號：</strong>兩者都不需要帳號就能使用。</li>
</ul>
<h2>現在就能免費試試看</h2>
<p>MarsDawn 即將在 Mac App Store 上架，現在還沒開賣。在那之前，免費的 <code>marsdawn</code> 命令列工具今天就能把任何 Markdown 檔案轉成 PDF，Mermaid 圖表和程式碼上色都在，而且不需要安裝其他東西：</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>接下來</h2>
<ul>
  <li>完整步驟：<a href="/zh-hans/markdown-to-pdf/">Markdown 轉 PDF</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hans/limits/">這份清單</a>。</li>
  <li>命令列工具的所有選項：<a href="/zh-hans/cli/">命令列工具</a>。</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn：免費的 Markdown 轉 PDF 命令列工具 · MarsDawn',
        "description": '免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。',
        "body": f"""
<section class="intro">
  <h1>命令列工具</h1>
  <p>免費的 <code>marsdawn</code> 命令列工具：從終端機或 LLM agent 把 Markdown 匯出成 PDF；裝了 MarsDawn app 的話，也能用它開啟檔案。</p>
</section>

<div class="summary"><p><strong>marsdawn 免費、另外發佈，不透過 Mac App Store。</strong>用 Homebrew 安裝，在 Apple 晶片的 Mac 上裝好就能直接使用。<code>export</code> 可以單獨使用；<code>open</code> 需要 MarsDawn app。</p></div>

<p>要從 AI agent 或腳本呼叫 marsdawn？請看<a href="/zh-hans/cli/agents/">給 AI agent 的 marsdawn 參考</a>，裡面有 JSON 輸出、Schema 和所有離開代碼。</p>

<h2>安裝</h2>
<p>使用 <a href="https://brew.sh">Homebrew</a>：</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成，不需要另外安裝任何東西。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上（Swift 6.2）。這個工具需要 macOS 15 以上。</p>
<p>也可以從<a href="{k.KIT_URL}">原始碼</a>用 Swift Package Manager 建置：</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>用 <code>marsdawn --version</code> 查看安裝的版本。</p>

<h2>指令</h2>

<h3>marsdawn open</h3>
<p>在 MarsDawn app 中開啟一個或多個 Markdown 檔案，方便審閱。需要先安裝這個 app：沒有安裝時，<code>marsdawn open</code> 會以代碼 3 結束，並說明沒有安裝 MarsDawn。<code>export</code> 不需要這個 app。</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>：請 MarsDawn 定位到那一行。後面再接欄位，例如 <code>notes.md:120:8</code>，會被忽略。如果有檔案的完整名稱就是這個參數，則視為那個檔案。</li>
  <li><code>--line &lt;n&gt;</code>：同樣的功能，只用於單一檔案，也可以用在檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。</li>
  <li>行號範圍是 1 到 999999999。</li>
  <li>MarsDawn 1.0 會打開檔案，但還不會跳到指定的行。</li>
  <li><code>--json</code>：印出 JSON 結果，而不是文字。</li>
</ul>
<p>行號功能從 marsdawn 0.3.0 開始提供。</p>

<h3>marsdawn export</h3>
<p>把 Markdown 檔案輸出成分頁的 PDF，使用和 MarsDawn 輸出 PDF 相同的元件。不需要安裝 MarsDawn app。相對路徑的圖片，會以輸入檔案所在的資料夾為準。</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF 的輸出位置，預設是把輸入檔的副檔名換成 <code>.pdf</code>。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：預覽主題的淺色版本，預設讀取 <code>$MARSDAWN_THEME</code>，否則用 <code>dawn</code>。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：紙張大小，預設 <code>a4</code>。</li>
  <li><code>--allow-remote-images</code>：輸出時載入網路圖片，預設關閉。</li>
  <li><code>--force</code>：如果輸出檔已存在就直接覆蓋。</li>
  <li><code>--json</code>：印出 JSON 結果，而不是文字。</li>
</ul>

<h2>$MARSDAWN_THEME 環境變數</h2>
<p>沒有傳入 <code>--theme</code> 時，<code>export</code> 會讀取 <code>$MARSDAWN_THEME</code> 環境變數，值必須是 <code>dawn</code>、<code>classic</code>、<code>modern</code> 或 <code>vivid</code> 其中之一，其他值都會改用 <code>dawn</code>。這個工具不會讀取 App 本身的主題設定，因為讀取其他 App 的容器可能觸發 macOS 隱私權提示。</p>

<h2>覆蓋檔案的規則</h2>
<p><code>export</code> 預設不會覆蓋已存在的輸出檔，除非加上 <code>--force</code>。</p>

<h2>結束代碼</h2>
<ul>
  <li><code>0</code>：成功。</li>
  <li><code>2</code>：找不到輸入檔。</li>
  <li><code>3</code>：尚未安裝 MarsDawn（只有 <code>open</code> 會用到）。</li>
  <li><code>4</code>：輸出檔已存在（可加上 <code>--force</code>）。</li>
  <li><code>5</code>：輸出失敗。</li>
  <li><code>64</code>：使用方式錯誤，包括行號超出範圍，或 <code>--line</code> 搭配了多個檔案。</li>
</ul>

<h2>--json 輸出</h2>
<p>成功時，<code>marsdawn open --json</code> 會印出 <code>ok</code>、<code>opened</code>（每個檔案的 <code>path</code>，有指定行號時另含 <code>line</code>）與 <code>app</code>（App 路徑）；<code>marsdawn export --json</code> 會印出 <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code> 與 <code>diagramErrors</code>。失敗時兩者都會印出 <code>ok</code>、<code>error</code> 與 <code>message</code>。</p>
""",
    }
    pages['cli/agents'] = {
        "title": '給 AI agent 的 marsdawn 參考：用腳本轉 PDF · MarsDawn',
        "description": '給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。',
        "body": f"""
<section class="intro">
  <h1>給 AI agent 的 marsdawn 參考</h1>
  <p>給呼叫 <code>marsdawn</code> 命令列工具的 AI agent 與腳本參考。本頁每個範例都用目前原始碼建置的工具實際執行過。</p>
</section>

<div class="summary"><p><strong>要把 Markdown 檔轉成 PDF，執行 <code>marsdawn export notes.md --json</code>，再從 stdout 讀取一個 JSON 物件。</strong>Mermaid 圖表與程式碼上色的呈現方式和 MarsDawn app 相同。<code>export</code> 不需要 app，<code>open</code> 需要。</p></div>

<h2>能做什麼</h2>
<ul>
  <li><code>export</code>：用和 MarsDawn app 相同的匯出程式，把一個 Markdown 檔輸出成分頁的 PDF，不會開啟任何視窗。</li>
  <li><code>open</code>：在 MarsDawn app 中開啟一或多個 Markdown 檔，讓人檢閱，也可以指定每個檔案要定位的行。</li>
</ul>

<h2>不做什麼</h2>
<ul>
  <li>不從 stdin 讀取 Markdown，請傳入檔案路徑。</li>
  <li>不把 PDF 寫到 stdout。PDF 一律寫成檔案，stdout 只輸出結果。</li>
  <li>檔案已存在時不會覆寫，除非加上 <code>--force</code>。</li>
  <li>不載入網路圖片，除非加上 <code>--allow-remote-images</code>，而且只走 https。</li>
  <li>沒有安裝 MarsDawn 時，<code>open</code> 無法使用，會以代碼 3 結束。<code>export</code> 不需要 app。</li>
  <li>MarsDawn 1.0 還不會跳到 <code>open</code> 指定的行，會從檔案開頭顯示。</li>
  <li>只能在 macOS 上執行。</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>在 <code>notes.md</code> 旁寫出 <code>notes.pdf</code>。選項：</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>：PDF 的寫入位置。預設為輸入檔路徑，副檔名換成 <code>.pdf</code>。</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>：使用主題的淺色色盤。預設為 <code>$MARSDAWN_THEME</code>，其次是 <code>dawn</code>。</li>
  <li><code>--paper &lt;a4|letter&gt;</code>：紙張大小。預設為 <code>a4</code>。</li>
  <li><code>--allow-remote-images</code>：算繪時載入網路上的 https 圖片。</li>
  <li><code>--force</code>：輸出檔已存在時覆寫。</li>
  <li><code>--json</code>：在 stdout 輸出一個 JSON 物件，而不是文字。</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>成功，離開代碼 0：</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>：寫出的 PDF 的絕對路徑。</li>
  <li><code>pages</code>：頁數。</li>
  <li><code>theme</code> 與 <code>paper</code>：實際使用的值。</li>
  <li><code>diagramErrors</code>：每個算繪失敗的 Mermaid 圖表各一則訊息。PDF 仍會寫出。</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> 指定要定位的行。後面再接欄位，例如 <code>notes.md:120:8</code>，會被忽略。如果參數本身就是一個存在的檔名，就一律當成那個檔案，所以名為 <code>weird:12</code> 的檔案會照原名開啟。</li>
  <li><code>--line &lt;n&gt;</code> 為單一檔案指定行號，包括檔名本身以冒號加數字結尾的情況。只能搭配一個檔案。</li>
  <li>行號範圍是 1 到 999999999，超出範圍是用法錯誤。</li>
  <li>行號從 marsdawn 0.3.0 開始提供。MarsDawn 1.0 會打開檔案，但還不會跳到指定的行。</li>
</ul>
<p>成功，離開代碼 0：</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>：每個檔案一個物件，順序與傳入時相同。<code>path</code> 是檔案的絕對路徑；只有指定了行號時才有 <code>line</code>。</li>
  <li><code>app</code>：開啟它們的 MarsDawn app 路徑。</li>
</ul>
<p>marsdawn 0.2.x 的 <code>opened</code> 是路徑字串的清單。如果需要同時處理兩種格式，請先查看 <code>marsdawn --version</code>。</p>

<h2>失敗</h2>
<p>加上 <code>--json</code> 時，失敗會在 stdout 輸出一個 JSON 物件，並以對應的代碼結束：</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>，<code>input_not_found</code>：輸入檔不存在、是資料夾，或不是 UTF-8 文字。</li>
  <li><code>3</code>，<code>app_not_installed</code>：沒有安裝 MarsDawn。只有 <code>open</code> 會回傳這個代碼。</li>
  <li><code>4</code>，<code>output_exists</code>：輸出檔已存在，請加上 <code>--force</code>。</li>
  <li><code>5</code>，<code>export_failed</code>：匯出本身失敗。</li>
  <li><code>64</code>：用法錯誤，例如未知的選項、無效的值、行號超出範圍，或 <code>--line</code> 搭配了多個檔案。這種錯誤一律以文字輸出到 stderr，即使加了 <code>--json</code> 也一樣。</li>
</ul>

<h2>JSON Schema</h2>
<p>每種 <code>--json</code> 結果的 JSON Schema（draft 2020-12）：</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>環境變數</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>：沒有傳入 <code>--theme</code> 時，<code>export</code> 使用的主題。未知的值會直接改用 <code>dawn</code>，不會報錯。</li>
</ul>

<h2>系統需求</h2>
<ul>
  <li>這個工具需要 macOS 15 以上。在 Apple 晶片的 Mac 上，Homebrew 會安裝預先建置好的版本，不需要其他東西。自己建置時（在 Intel Mac 上，或從原始碼建置），需要 Swift 6.2 以上，也就是 Xcode 26 以上。</li>
  <li>MarsDawn app 需要 macOS 26 以上。</li>
</ul>

<h2>安裝</h2>
<p>使用 Homebrew。在 Apple 晶片的 Mac 上，會直接安裝預先建置好的版本，幾秒就完成，不需要 Xcode。在 Intel Mac 上則會從原始碼編譯 marsdawn，需要幾分鐘，也需要 Xcode 26 以上。</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>也可以從<a href="{k.KIT_URL}">原始碼</a>建置。第一次建置會下載相依套件並編譯，同樣需要幾分鐘。</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> 會印出版本號，例如 <code>0.3.0</code>，並以代碼 0 結束。</p>
""",
    }
    pages['cli/skill'] = {
        "title": '讓寫程式的 agent 把 Markdown 轉 PDF 的 skill · MarsDawn',
        "description": '一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。',
        "body": f"""
<section class="intro">
  <h1>讓 agent 幫你做出 PDF。</h1>
  <p>這個 skill 是一個 Markdown 檔案。它教寫程式的 agent 安裝 <code>marsdawn</code>、確認它能用、把文件匯出成 PDF 並讀懂結果，這樣寫出 Markdown 的 agent，也能把 PDF 交給你。</p>
</section>
<h2>在 Claude Code 中安裝</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>需要做出 PDF 時，Claude Code 會自動載入它，你也可以用 <code>/marsdawn</code> 自己執行。它只是<a href="/cli/skill/SKILL.md">一個簡短的檔案</a>，安裝前先讀一遍。</p>
<p>其他 agent 也能用同一個檔案。它是純 Markdown，只有說明和指令，讓你的 agent 讀這個網址，或直接貼給它就好。這個檔案是英文的。</p>
<h2>它教什麼</h2>
<ul>
  <li>如果沒有 <code>marsdawn</code>，就用 Homebrew 安裝，再用 <code>marsdawn --version</code> 確認版本，而不是假設某個版本。</li>
  <li>用 <code>marsdawn export … --json</code> 匯出，並讀懂結果：PDF 存到哪裡、有幾頁，以及有沒有 Mermaid 圖表沒畫出來。</li>
  <li>依結束代碼分辨失敗的原因：找不到檔案、PDF 已經存在、匯出失敗、選項錯誤。</li>
  <li>只有裝了 MarsDawn app 才用 <code>open</code>，而且絕不用它來做 PDF。</li>
</ul>
<h2>它不會做的事</h2>
<ul>
  <li>它不會自己取得執行任何東西的權限。你的 agent 在安裝或執行 <code>marsdawn</code> 之前，仍然會先問你，就像執行其他指令一樣。</li>
  <li>它不會把你的文件傳到任何地方。<code>marsdawn</code> 在你的 Mac 上產生 PDF，除非你加上 <code>--allow-remote-images</code>，否則不會載入網路上的圖片。</li>
</ul>
<p>完整的規格，每個欄位和每個代碼，都在<a href="/zh-hans/cli/agents/">給 AI agent 的 marsdawn 參考</a>裡。</p>
""",
    }
    return {
        'ui': ui,
        'store_chip': store_chip,
        'schema_notes': schema_notes,
        'example_plan': example_plan,
        'trait_link': trait_link,
        'trait_nav_heading': trait_nav_heading,
        'figure_list_label': figure_list_label,
        'figures': figures,
        'pages': pages,
    }
