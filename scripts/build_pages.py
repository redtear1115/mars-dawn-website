#!/usr/bin/env python3
"""Generates the MarsDawn privacy and support pages in public/ (en and zh-Hant).

UI labels quoted on each page must match the app's own strings in that language.
The app lives in another repository, so check them by hand when either side changes.

Static output, no build step at deploy time. Edit the copy here and rerun:
    python3 scripts/build_pages.py
"""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

SITE = Path(__file__).resolve().parent.parent / "public"
UPDATED = "2026-09-17"
EMAIL = "support@southern-light.dev"
BASE_URL = "https://marsdawn.southern-light.dev"

LOCALES = {
    "en": {"prefix": "", "html_lang": "en", "label": "English", "root": "/"},
    "zh-hant": {"prefix": "zh-hant/", "html_lang": "zh-Hant", "label": "繁體中文", "root": "/zh-hant/"},
}

# OG locale tokens (underscore-separated, per the Open Graph protocol).
OG_LOCALE = {"en": "en_US", "zh-hant": "zh_Hant_TW"}

UI = {
    "en": {
        "home": "MarsDawn", "privacy": "Privacy Policy", "support": "Support", "cli": "Command Line",
        "updated": f"Last updated {UPDATED}", "tagline": "A new dawn for Markdown.",
        "footer_store": "MarsDawn is available on the Mac App Store.",
    },
    "zh-hant": {
        "home": "MarsDawn", "privacy": "隱私權政策", "support": "支援", "cli": "命令列工具",
        "updated": f"最後更新：{UPDATED}", "tagline": "Markdown 的新黎明。",
        "footer_store": "MarsDawn 於 Mac App Store 販售。",
    },
}

PAGES = {
    ("en", "index"): {
        "title": "MarsDawn",
        "description": "MarsDawn is a native Markdown editor for the Mac with live preview, Mermaid diagrams and PDF export.",
        "body": f"""
<section class="intro">
  <h1>MarsDawn</h1>
  <p>A native Markdown editor for the Mac. Write on the left, read on the right, with Mermaid diagrams, four preview themes and PDF export.</p>
</section>
<ul class="links">
  <li><a href="/support/">Support and questions</a></li>
  <li><a href="/privacy/">Privacy Policy</a></li>
</ul>
""",
    },
    ("zh-hant", "index"): {
        "title": "MarsDawn",
        "description": "MarsDawn 是原生的 Mac Markdown 編輯器，支援即時預覽和 Mermaid 圖表，也能輸出 PDF。",
        "body": f"""
<section class="intro">
  <h1>MarsDawn</h1>
  <p>原生的 Mac Markdown 編輯器。左邊寫，右邊看排版後的頁面，支援 Mermaid 圖表和四種預覽主題，也能輸出 PDF。</p>
</section>
<ul class="links">
  <li><a href="/zh-hant/support/">支援與常見問題</a></li>
  <li><a href="/zh-hant/privacy/">隱私權政策</a></li>
</ul>
""",
    },
    ("en", "privacy"): {
        "title": "Privacy Policy · MarsDawn",
        "description": "MarsDawn does not collect personal data. Your documents and settings stay on your Mac.",
        "body": f"""
<section class="intro">
  <h1>Privacy Policy</h1>
  <p>How MarsDawn, the Markdown editor for macOS, handles your information.</p>
  <p class="updated">Last updated {UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn does not collect any data about you.</strong> There is no account, no analytics, no advertising and no tracking. Your documents and settings stay on your Mac.</p></div>

<h2>What stays on your Mac</h2>
<ul>
  <li><strong>Your documents.</strong> MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.</li>
  <li><strong>Your settings.</strong> Appearance, preview theme, window layout and the image preference are stored in the app's own preferences on your Mac.</li>
  <li><strong>Folder access you grant.</strong> When you let MarsDawn show images from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. You can remove folders at any time in MarsDawn › Settings.</li>
</ul>

<h2>When MarsDawn uses the internet</h2>
<p>MarsDawn works fully offline. It connects to the internet in one situation only: <strong>when you choose to load images from the web</strong> that a document refers to. Web images are blocked by default. They load only after you click <em>Load Images</em> in the preview, or if you turn on <em>Load remote images automatically</em> in Settings.</p>
<p>When web images load, your Mac requests them directly from the servers that host them. Like any web request, this lets those servers see your IP address and that the image was requested. MarsDawn's developer receives none of this information.</p>
<p>Links you click in the preview open in your default web browser, under that browser's own privacy practices.</p>

<h2>Siri, Shortcuts and Spotlight</h2>
<p>MarsDawn offers actions for Siri, the Shortcuts app and Spotlight, such as creating a document or adding a note. When you use them, the text you provide is passed to MarsDawn on your Mac and saved only where the action says (a new document, or the <code>Inbox.md</code> file in the notes folder you chose). Speech you dictate to Siri is handled by Apple under <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

<h2>Exporting and printing</h2>
<p>PDF export and printing happen on your Mac. The PDF is saved where you choose. Printing goes through macOS to the printer you pick.</p>

<h2>The marsdawn command-line tool</h2>
<p>The optional <code>marsdawn</code> command-line tool, distributed separately, also runs entirely on your Mac. It reads the Markdown file you name and writes the PDF you ask for. It loads web images only when you pass <code>--allow-remote-images</code>.</p>

<h2>Children</h2>
<p>MarsDawn does not collect data from anyone, including children.</p>

<h2>Purchases</h2>
<p>MarsDawn is sold through the Mac App Store. Apple processes the purchase under its own terms, and the developer does not receive your payment details.</p>

<h2>Changes to this policy</h2>
<p>If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
    },
    ("zh-hant", "privacy"): {
        "title": "隱私權政策 · MarsDawn",
        "description": "MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。",
        "body": f"""
<section class="intro">
  <h1>隱私權政策</h1>
  <p>macOS 的 Markdown 編輯器 MarsDawn 如何處理你的資訊。</p>
  <p class="updated">最後更新：{UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn 不收集任何關於你的資料。</strong>沒有帳號、沒有分析、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。</p></div>

<h2>留在你 Mac 上的東西</h2>
<ul>
  <li><strong>你的文件。</strong>MarsDawn 只讀寫你打開、儲存或選擇的檔案與資料夾，App 不會把它們上傳到任何地方。</li>
  <li><strong>你的設定。</strong>外觀、預覽主題、視窗版面和圖片偏好，都存在 App 自己的偏好設定裡。</li>
  <li><strong>你授權的資料夾。</strong>當你讓 MarsDawn 顯示某個資料夾裡的圖片，或選擇筆記資料夾時，App 會保存 macOS 書籤，以便之後再次開啟。你隨時可以到 MarsDawn › 設定⋯ 移除。</li>
</ul>

<h2>MarsDawn 什麼時候會連上網路</h2>
<p>MarsDawn 可以完全離線使用，只有一種情況會連網：<strong>你選擇載入文件裡引用的網路圖片</strong>。網路圖片預設不載入，只有在你按下預覽中的「載入圖片」，或在設定中開啟「自動載入網路圖片」後才會載入。</p>
<p>載入網路圖片時，你的 Mac 會直接向存放圖片的伺服器發出請求。和所有網路請求一樣，這些伺服器會看到你的 IP 位址與這次請求。MarsDawn 的開發者不會收到任何這類資訊。</p>
<p>在預覽中點選的連結會用你的預設瀏覽器打開，適用該瀏覽器的隱私做法。</p>

<h2>Siri、捷徑和 Spotlight</h2>
<p>MarsDawn 提供 Siri、捷徑 App 和 Spotlight 可用的動作，例如新增文件或加入筆記。使用時，你提供的文字會交給你 Mac 上的 MarsDawn，並只存到動作指定的位置（新文件，或你所選筆記資料夾中的 <code>Inbox.md</code>）。對 Siri 說的話由 Apple 依<a href="https://www.apple.com/legal/privacy/">Apple 隱私權政策</a>處理。</p>

<h2>輸出 PDF 和列印</h2>
<p>輸出 PDF 和列印都在你的 Mac 上完成。PDF 存在你選擇的位置，列印則透過 macOS 送到你選的印表機。</p>

<h2>marsdawn 命令列工具</h2>
<p>另外發佈、可自由選用的 <code>marsdawn</code> 命令列工具，同樣完全在你的 Mac 上執行：只讀取你指定的 Markdown 檔，並寫出你要求的 PDF。只有在加上 <code>--allow-remote-images</code> 時才會載入網路圖片。</p>

<h2>兒童</h2>
<p>MarsDawn 不向任何人收集資料，包括兒童。</p>

<h2>購買</h2>
<p>MarsDawn 透過 Mac App Store 販售，付款由 Apple 依其條款處理，開發者不會取得你的付款資訊。</p>

<h2>政策變更</h2>
<p>如果 MarsDawn 未來處理資料的方式有所改變，本頁會在該版本推出前更新，頁首的日期也會一併更改。</p>

<h2>聯絡我們</h2>
<p>隱私相關問題：<a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
    },
    ("en", "support"): {
        "title": "Support · MarsDawn",
        "description": "Get help with MarsDawn, the Markdown editor for macOS.",
        "body": f"""
<section class="intro">
  <h1>Support</h1>
  <p>Help with MarsDawn, the Markdown editor for macOS.</p>
</section>

<section class="contact">
  <h2>Write to us</h2>
  <a class="email" href="mailto:{EMAIL}?subject=MarsDawn%20support">{EMAIL}</a>
  <p>Please include your macOS version and your MarsDawn version (MarsDawn › About MarsDawn). If something looks wrong, a screenshot or a small sample document helps a lot.</p>
</section>

<section class="faq">
  <h2>Common questions</h2>

  <h3>What do I need to run MarsDawn?</h3>
  <p>A Mac with macOS 26 Tahoe or later, on Apple silicon or Intel.</p>

  <h3>How do I switch between the editor and the preview?</h3>
  <p>Press <kbd>⌘1</kbd> for the source only, <kbd>⌘2</kbd> for side by side, and <kbd>⌘3</kbd> for the preview only. The same choices are in the View menu and the toolbar.</p>

  <h3>An image in my document doesn't show.</h3>
  <ul>
    <li><strong>Image on your Mac:</strong> save the document first, then click <em>Grant Folder Access…</em> in the preview and choose the folder that holds the image. MarsDawn remembers the folder. You can review granted folders in MarsDawn › Settings › Folder Access.</li>
    <li><strong>Image from the web:</strong> web images are blocked until you click <em>Load Images</em> at the top of the preview. To always load them, turn on <em>Load remote images automatically</em> in Settings.</li>
  </ul>

  <h3>How do I add an image?</h3>
  <p>Drag it into the editor, or paste it. The document must be saved first: MarsDawn copies the image into an <code>assets</code> folder next to the document and writes the Markdown link for you.</p>

  <h3>A Mermaid diagram shows an error.</h3>
  <p>MarsDawn shows the diagram's source with the first line of Mermaid's error message underneath. Check the line it names, for example for an arrow with nothing after it or a bracket that isn't closed.</p>

  <h3>How do I make a PDF?</h3>
  <p>Choose File › Export as PDF… (<kbd>⌥⌘E</kbd>). The PDF uses the light version of your preview theme and is split into pages, whichever layout you are in. File › Print… prints the same pages.</p>

  <h3>How do I use MarsDawn with Siri or Shortcuts?</h3>
  <p>Open the Shortcuts app and search for MarsDawn to find <em>New Markdown Document</em>, <em>Add Note to Inbox</em> and <em>Open Recent Document</em>. Before adding notes, choose a notes folder in MarsDawn › Settings › Notes Folder. Notes are added to <code>Inbox.md</code> in that folder.</p>

  <h3>Where are my settings?</h3>
  <p>MarsDawn › Settings (<kbd>⌘,</kbd>) has appearance, images, the notes folder, folder access and the preview theme.</p>

  <h3>How do I get a refund?</h3>
  <p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
</section>
""",
    },
    ("zh-hant", "support"): {
        "title": "支援 · MarsDawn",
        "description": "MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。",
        "body": f"""
<section class="intro">
  <h1>支援</h1>
  <p>macOS Markdown 編輯器 MarsDawn 的使用說明。</p>
</section>

<section class="contact">
  <h2>寫信給我們</h2>
  <a class="email" href="mailto:{EMAIL}?subject=MarsDawn%20support">{EMAIL}</a>
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
    },
}


# The CLI page, kept separate from PAGES per the edit boundary for this slice.
# Facts are taken from redtear1115/mars-dawn-kit @ origin/main
# (Sources/marsdawn/Commands.swift, Sources/marsdawn/main.swift, README.md).
CLI_PAGES = {
    ("en", "cli"): {
        "title": "Command Line · MarsDawn",
        "description": "The free marsdawn command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.",
        "body": f"""
<section class="intro">
  <h1>Command Line</h1>
  <p>The free <code>marsdawn</code> command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.</p>
</section>

<div class="summary"><p><strong>marsdawn is free and distributed separately from the Mac App Store.</strong> Homebrew isn't published yet, so build it from source with Swift Package Manager. Both commands need the MarsDawn app installed.</p></div>

<h2>Install</h2>
<p>Clone <a href="https://github.com/redtear1115/mars-dawn-kit">the source</a> and run it with Swift Package Manager:</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift run marsdawn open notes.md</code></pre>

<h2>Commands</h2>

<h3>marsdawn open</h3>
<p>Opens one or more Markdown files in MarsDawn for review. Needs MarsDawn installed.</p>
<pre><code>marsdawn open notes.md</code></pre>
<ul>
  <li><code>--json</code>: print a JSON result instead of text.</li>
</ul>

<h3>marsdawn export</h3>
<p>Renders a Markdown file to a paginated PDF, with the same exporter MarsDawn's own PDF export uses. Also needs MarsDawn installed. Relative images resolve against the input file's folder.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: where to write the PDF. Defaults to the input path with a <code>.pdf</code> extension.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: the preview theme's light palette. Defaults to <code>$MARSDAWN_THEME</code>, then <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: paper size. Defaults to <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: load images from the web while rendering. Off by default.</li>
  <li><code>--force</code>: replace the output file if it already exists.</li>
  <li><code>--json</code>: print a JSON result instead of text.</li>
</ul>

<h2>The $MARSDAWN_THEME variable</h2>
<p>When <code>--theme</code> isn't passed, <code>export</code> reads the <code>$MARSDAWN_THEME</code> environment variable. Its value must be one of <code>dawn</code>, <code>classic</code>, <code>modern</code> or <code>vivid</code>; anything else falls back to <code>dawn</code>. The CLI doesn't read the app's own theme setting, because reading another app's container can trigger a macOS privacy prompt.</p>

<h2>Overwriting files</h2>
<p><code>export</code> refuses to replace an existing output file unless you pass <code>--force</code>.</p>

<h2>Exit codes</h2>
<ul>
  <li><code>0</code>: success.</li>
  <li><code>2</code>: input not found.</li>
  <li><code>3</code>: MarsDawn is not installed.</li>
  <li><code>4</code>: output exists (pass <code>--force</code>).</li>
  <li><code>5</code>: export failed.</li>
  <li><code>64</code>: usage error.</li>
</ul>

<h2>--json output</h2>
<p>On success, <code>marsdawn open --json</code> prints <code>ok</code>, <code>opened</code> (the file paths) and <code>app</code> (the app path). <code>marsdawn export --json</code> prints <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> and <code>diagramErrors</code>. On failure, both print <code>ok</code>, <code>error</code> and <code>message</code>.</p>

<h2>MarsDawn must be installed</h2>
<p>Both <code>open</code> and <code>export</code> need the MarsDawn app installed from the Mac App Store; <code>export</code> renders through the same code the app uses, but still checks that the app is present first.</p>
""",
    },
    ("zh-hant", "cli"): {
        "title": "命令列工具 · MarsDawn",
        "description": "免費的 marsdawn 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。",
        "body": f"""
<section class="intro">
  <h1>命令列工具</h1>
  <p>免費的 <code>marsdawn</code> 命令列工具：在 MarsDawn 中開啟 Markdown 檔案，或從終端機、LLM agent 匯出成 PDF。</p>
</section>

<div class="summary"><p><strong>marsdawn 免費、另外發佈，不透過 Mac App Store。</strong>目前尚未發佈到 Homebrew，需要用 Swift Package Manager 自行建置。兩個指令都需要先安裝 MarsDawn。</p></div>

<h2>安裝</h2>
<p>下載<a href="https://github.com/redtear1115/mars-dawn-kit">原始碼</a>，並用 Swift Package Manager 執行：</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift run marsdawn open notes.md</code></pre>

<h2>指令</h2>

<h3>marsdawn open</h3>
<p>在 MarsDawn 中開啟一個或多個 Markdown 檔案，方便審閱。需要先安裝 MarsDawn。</p>
<pre><code>marsdawn open notes.md</code></pre>
<ul>
  <li><code>--json</code>：印出 JSON 結果，而不是文字。</li>
</ul>

<h3>marsdawn export</h3>
<p>把 Markdown 檔案輸出成分頁的 PDF，使用和 MarsDawn 輸出 PDF 相同的元件。同樣需要先安裝 MarsDawn。相對路徑的圖片，會以輸入檔案所在的資料夾為準。</p>
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
  <li><code>3</code>：尚未安裝 MarsDawn。</li>
  <li><code>4</code>：輸出檔已存在（可加上 <code>--force</code>）。</li>
  <li><code>5</code>：輸出失敗。</li>
  <li><code>64</code>：使用方式錯誤。</li>
</ul>

<h2>--json 輸出</h2>
<p>成功時，<code>marsdawn open --json</code> 會印出 <code>ok</code>、<code>opened</code>（檔案路徑）與 <code>app</code>（App 路徑）；<code>marsdawn export --json</code> 會印出 <code>ok</code>、<code>output</code>、<code>pages</code>、<code>theme</code>、<code>paper</code> 與 <code>diagramErrors</code>。失敗時兩者都會印出 <code>ok</code>、<code>error</code> 與 <code>message</code>。</p>

<h2>需要先安裝 MarsDawn</h2>
<p><code>open</code> 和 <code>export</code> 都需要先從 Mac App Store 安裝 MarsDawn；<code>export</code> 雖然使用和 App 相同的元件，仍會先檢查 App 是否已安裝。</p>
""",
    },
}

PAGE_ORDER = ["index", "support", "privacy", "cli"]
SLUG_TO_UI_KEY = {"index": "home", "support": "support", "privacy": "privacy", "cli": "cli"}


def all_pages() -> dict:
    merged = dict(PAGES)
    merged.update(CLI_PAGES)
    return merged


def page_path(locale: str, slug: str) -> str:
    base = LOCALES[locale]["root"]
    return base if slug == "index" else f"{base}{slug}/"


def md_path(locale: str, slug: str) -> str:
    return page_path(locale, slug) + "index.md"


def abs_url(path: str) -> str:
    return BASE_URL + path


# --- A small, strict HTML-to-Markdown converter -----------------------------
# Handles exactly the tags used in page bodies (PAGES and CLI_PAGES) and
# raises MarkdownConversionError on anything else, rather than dropping it.

class MarkdownConversionError(Exception):
    """Raised when the converter meets an HTML tag it doesn't know how to render."""


_TRANSPARENT_TAGS = {"section", "div"}


class _Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag: str, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.children = []  # list[_Node | str]


class _TreeBuilder(HTMLParser):
    """Builds a tiny tree so tags nest correctly, tolerant of the whitespace
    formatting used in the page body literals."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = _Node("#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = _Node(tag, attrs)
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(_Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        raise MarkdownConversionError(f"unmatched closing tag </{tag}>")

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def _collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def _render_inline(children) -> str:
    parts = []
    for child in children:
        if isinstance(child, str):
            parts.append(_collapse(child))
            continue
        tag = child.tag
        if tag == "strong":
            parts.append("**" + _render_inline(child.children).strip() + "**")
        elif tag == "em":
            parts.append("*" + _render_inline(child.children).strip() + "*")
        elif tag in ("code", "kbd"):
            parts.append("`" + _render_inline(child.children).strip() + "`")
        elif tag == "a":
            href = child.attrs.get("href", "")
            label = _render_inline(child.children).strip()
            parts.append(f"[{label}]({href})")
        else:
            raise MarkdownConversionError(f"unsupported inline tag <{tag}>")
    return "".join(parts)


def _pre_text(node: _Node) -> str:
    parts = []

    def walk(n: _Node):
        for child in n.children:
            if isinstance(child, str):
                parts.append(child)
            elif child.tag == "code":
                walk(child)
            else:
                raise MarkdownConversionError(f"unsupported tag <{child.tag}> inside <pre>")

    walk(node)
    return "".join(parts).strip("\n")


def _render_block(node: _Node) -> str:
    tag = node.tag
    if tag in _TRANSPARENT_TAGS:
        return _render_children(node.children)
    if tag in ("h1", "h2", "h3"):
        return "#" * int(tag[1]) + " " + _render_inline(node.children).strip() + "\n\n"
    if tag == "p":
        text = _render_inline(node.children).strip()
        return (text + "\n\n") if text else ""
    if tag == "ul":
        items = []
        for child in node.children:
            if isinstance(child, str):
                if child.strip():
                    raise MarkdownConversionError("unexpected text directly inside <ul>")
                continue
            if child.tag != "li":
                raise MarkdownConversionError(f"unsupported child <{child.tag}> of <ul>")
            items.append("- " + _render_inline(child.children).strip())
        return "\n".join(items) + "\n\n"
    if tag == "pre":
        return "```\n" + _pre_text(node) + "\n```\n\n"
    if tag in ("strong", "em", "code", "kbd", "a"):
        # An inline element used directly as a block child (e.g. the support
        # page's standalone <a class="email">). Render it as its own paragraph.
        text = _render_inline([node]).strip()
        return (text + "\n\n") if text else ""
    raise MarkdownConversionError(f"unsupported tag <{tag}>")


def _render_children(children) -> str:
    out = []
    for child in children:
        if isinstance(child, str):
            if child.strip():
                raise MarkdownConversionError("unexpected text outside a block element")
            continue
        out.append(_render_block(child))
    return "".join(out)


def html_to_markdown(fragment: str) -> str:
    builder = _TreeBuilder()
    builder.feed(fragment)
    builder.close()
    return _render_children(builder.root.children).strip() + "\n"


def render(locale: str, slug: str, page: dict) -> str:
    ui = UI[locale]
    lang = LOCALES[locale]["html_lang"]
    switch = " · ".join(
        f'<a href="{page_path(other, slug)}" hreflang="{LOCALES[other]["html_lang"]}"'
        + (' aria-current="true"' if other == locale else "")
        + f' lang="{LOCALES[other]["html_lang"]}">{LOCALES[other]["label"]}</a>'
        for other in LOCALES
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{LOCALES[other]["html_lang"]}" href="{abs_url(page_path(other, slug))}">'
        for other in LOCALES
    )
    alternates += f'\n<link rel="alternate" hreflang="x-default" href="{abs_url(page_path("en", slug))}">'
    canonical_url = abs_url(page_path(locale, slug))
    seo = f"""<link rel="canonical" href="{canonical_url}">
<link rel="alternate" type="text/markdown" href="{md_path(locale, slug)}">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["description"]}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{abs_url("/assets/icon-192.png")}">
<meta property="og:locale" content="{OG_LOCALE[locale]}">
<meta name="twitter:card" content="summary">"""
    jsonld = ""
    if slug == "index":
        data = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "MarsDawn",
            "description": page["description"],
            "applicationCategory": "DeveloperApplication",
            "operatingSystem": "macOS 26 or later",
            "offers": {"@type": "Offer", "price": "4.99", "priceCurrency": "USD"},
            "url": canonical_url,
        }
        jsonld = f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>\n'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{page["description"]}">
<meta name="color-scheme" content="light dark">
<link rel="icon" type="image/png" href="/assets/favicon-64.png">
<link rel="stylesheet" href="/assets/site.css">
{alternates}
{seo}
{jsonld}</head>
<body>
<div class="page">
<header class="masthead">
  <a class="brand" href="{LOCALES[locale]["root"]}">
    <img src="/assets/icon-192.png" alt="" width="40" height="40">
    <strong>MarsDawn</strong>
  </a>
  <nav class="lang" aria-label="Language">{switch}</nav>
</header>
<main>
{page["body"].strip()}
</main>
<footer class="footer">
  <span>{ui["tagline"]}</span>
  <a href="{page_path(locale, "support")}">{ui["support"]}</a>
  <a href="{page_path(locale, "privacy")}">{ui["privacy"]}</a>
  <a href="{page_path(locale, "cli")}">{ui["cli"]}</a>
  <span>{ui["footer_store"]}</span>
</footer>
</div>
</body>
</html>
"""


# robots.txt: exactly these directives (Cloudflare prepends its own managed block).
ROBOTS_TXT = f"""# robots.txt for marsdawn.southern-light.dev
User-agent: *
Allow: /
Content-Signal: search=yes, ai-input=yes, ai-train=yes
Sitemap: {BASE_URL}/sitemap.xml
"""


def build_sitemap(pages: dict) -> str:
    entries = []
    for slug in PAGE_ORDER:
        for locale in LOCALES:
            if (locale, slug) not in pages:
                continue
            loc = xml_escape(abs_url(page_path(locale, slug)))
            alt_links = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{LOCALES[other]["html_lang"]}" href="{xml_escape(abs_url(page_path(other, slug)))}"/>'
                for other in LOCALES
            )
            alt_links += (
                f'\n    <xhtml:link rel="alternate" hreflang="x-default"'
                f' href="{xml_escape(abs_url(page_path("en", slug)))}"/>'
            )
            entries.append(f"  <url>\n    <loc>{loc}</loc>\n{alt_links}\n  </url>")
    body = "\n".join(entries)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def build_llms_txt(pages: dict) -> str:
    home_en = pages[("en", "index")]
    lines = ["# MarsDawn", "", f"> {home_en['description']}", ""]
    for locale, heading in (("en", "Docs"), ("zh-hant", "繁體中文")):
        lines.append(f"## {heading}")
        for slug in PAGE_ORDER:
            page = pages[(locale, slug)]
            label = UI[locale][SLUG_TO_UI_KEY[slug]]
            url = abs_url(md_path(locale, slug))
            lines.append(f"- [{label}]({url}): {page['description']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_llms_full(pages: dict) -> str:
    sections = []
    for locale, heading in (("en", "English"), ("zh-hant", "繁體中文")):
        for slug in PAGE_ORDER:
            page = pages[(locale, slug)]
            label = UI[locale][SLUG_TO_UI_KEY[slug]]
            url = abs_url(page_path(locale, slug))
            body_md = html_to_markdown(page["body"])
            sections.append(f"## {label}\n\nSource: {url}\n\n{body_md}")
    return "# MarsDawn — full content\n\n" + "\n---\n\n".join(sections)


def main() -> None:
    pages = all_pages()
    for (locale, slug), page in pages.items():
        folder = SITE / LOCALES[locale]["prefix"] / ("" if slug == "index" else slug)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(render(locale, slug, page), encoding="utf-8")
        print(folder / "index.html")
        (folder / "index.md").write_text(html_to_markdown(page["body"]), encoding="utf-8")
        print(folder / "index.md")

    (SITE / "llms.txt").write_text(build_llms_txt(pages), encoding="utf-8")
    print(SITE / "llms.txt")
    (SITE / "llms-full.txt").write_text(build_llms_full(pages), encoding="utf-8")
    print(SITE / "llms-full.txt")
    (SITE / "robots.txt").write_text(ROBOTS_TXT, encoding="utf-8")
    print(SITE / "robots.txt")
    (SITE / "sitemap.xml").write_text(build_sitemap(pages), encoding="utf-8")
    print(SITE / "sitemap.xml")


if __name__ == "__main__":
    main()
