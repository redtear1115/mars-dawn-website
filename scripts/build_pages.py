#!/usr/bin/env python3
"""Generates the MarsDawn site in public/, in four languages: en, zh-Hant, zh-Hans and ja.

The en and zh-Hant copy is in this file. The zh-Hans and ja copy, translated from it, is in
copy_zh_hans.py and copy_ja.py, one module per language, merged in below.

UI labels quoted on each page must match the app's own strings in that language.
The app lives in another repository, so check them by hand when either side changes.

Static output, no build step at deploy time. Edit the copy here and rerun:
    python3 scripts/build_pages.py
"""
import json
import re
import sys
from types import SimpleNamespace
from html.parser import HTMLParser
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

SITE = Path(__file__).resolve().parent.parent / "public"
UPDATED = "2026-09-17"
# The privacy page has its own date: it changes when the policy does, not when other pages do.
PRIVACY_UPDATED = "2026-09-19"
EMAIL = "support@southern-light.dev"
BASE_URL = "https://marsdawn.southern-light.dev"

# The open-source kit and its free CLI. Pulled out as constants (instead of
# repeating the literal strings) so the CLI pages and product-facts.md, which
# both state these facts, can't drift apart from each other.
KIT_URL = "https://github.com/redtear1115/mars-dawn-kit"
KIT_LICENSE = "Apache-2.0"
BREW_TAP_INSTALL = "brew tap redtear1115/tap && brew install marsdawn"

LOCALES = {
    "en": {"prefix": "", "html_lang": "en", "label": "English", "root": "/"},
    "zh-hant": {"prefix": "zh-hant/", "html_lang": "zh-Hant", "label": "繁體中文", "root": "/zh-hant/"},
    "zh-hans": {"prefix": "zh-hans/", "html_lang": "zh-Hans", "label": "简体中文", "root": "/zh-hans/"},
    "ja": {"prefix": "ja/", "html_lang": "ja", "label": "日本語", "root": "/ja/"},
}

# OG locale tokens (underscore-separated, per the Open Graph protocol).
# zh_CN is the standard token for Simplified Chinese; it names a language, not a storefront.
OG_LOCALE = {"en": "en_US", "zh-hant": "zh_TW", "zh-hans": "zh_CN", "ja": "ja_JP"}

# Languages that use full-width punctuation in generated text (e.g. a list label's colon).
FULL_WIDTH = {"zh-hant", "zh-hans", "ja"}

# The app's interface languages, as /native/ and /vs/macmd-viewer/ state them. One place so the
# sentence changes in every language at once. Four languages from the 1.0 launch (app #104), approved
# for the site by the owner on 2026-09-20 (website #41). It's true only once that build ships, which
# is why this goes live with the launch deploy.
APP_UI_LANGUAGES = {
    "en": "English, Traditional Chinese, Simplified Chinese and Japanese",
    "zh-hant": "英文、繁體中文、簡體中文和日文",
    "zh-hans": "英文、繁体中文、简体中文和日文",
    "ja": "英語、繁体字中国語、簡体字中国語、日本語",
}

UI = {
    "en": {
        "home": "MarsDawn", "privacy": "Privacy Policy", "support": "Support", "cli": "Command Line",
        "agents": "marsdawn for agents", "using_cli": "Using the CLI",
        "markdown-to-pdf": "Markdown to PDF", "skill": "Agent skill",
        "view-markdown-on-mac": "View Markdown on a Mac",
        "vs-macmd-viewer": "MacMD Viewer vs. MarsDawn",
        "updated": f"Last updated {UPDATED}", "tagline": "Read what your agent wrote.",
        "footer_store": "MarsDawn is coming soon to the Mac App Store.",
        "more": "More",
        "yours": "Your writing stays on your Mac", "pay-once": "Try free, pay once", "pdf": "PDF export",
        "native": "A Mac app", "limits": "What MarsDawn doesn't do",
    },
    "zh-hant": {
        "home": "MarsDawn", "privacy": "隱私權政策", "support": "支援", "cli": "命令列工具",
        "agents": "給 AI agent 的 marsdawn 參考", "using_cli": "使用 CLI",
        "markdown-to-pdf": "Markdown 轉 PDF", "skill": "給 agent 的 skill",
        "view-markdown-on-mac": "在 Mac 上看 Markdown",
        "vs-macmd-viewer": "MacMD Viewer 對比 MarsDawn",
        "updated": f"最後更新：{UPDATED}", "tagline": "讀 agent 寫的 Markdown。",
        "footer_store": "MarsDawn 即將在 Mac App Store 上架。",
        "more": "其他頁面",
        "yours": "你寫的內容留在你的 Mac 上", "pay-once": "免費試用，買一次就好", "pdf": "輸出 PDF",
        "native": "為 Mac 而做", "limits": "MarsDawn 做不到的事",
    },
}

# The homepage hero: one dawn scene, not a banner. Inline SVG (same-origin, no
# script), colored entirely through CSS custom properties (site.css) so light
# and dark mode are each designed. A four-stop sky carries real tonal steps
# from deep night down to the warm limb; a wide radial glow sits at the
# horizon; the planet's mass has its own rim-to-deep gradient so it reads as
# a body, not a flat line. preserveAspectRatio keeps the horizon anchored to
# the bottom of the scene (xMidYMax slice) across every hero height.
#
# The scene is split into stacked layers, each its own <svg> with the same
# viewBox, so the one-time sunrise in site.css (the glow rising, a night veil
# lifting, the stars going out, the limb catching light from the centre) only
# moves whole layers with opacity, transform and clip-path, and never repaints
# the sky. With no animation, or reduced motion, every layer rests on the
# final frame: veil and stars at zero, glow and limb in place.
DAWN_VIEWBOX = 'viewBox="0 0 1200 900" preserveAspectRatio="xMidYMax slice" focusable="false"'


def _dawn_stars() -> str:
    """Three tiers of faint stars in the upper sky, from a fixed seed so the page
    regenerates byte for byte. They keep clear of the headline's column."""
    seed = 20260919
    tiers = {"a": [], "b": [], "c": []}
    placed = 0
    while placed < 36:
        seed = (seed * 1103515245 + 12345) % 2**31
        x = seed % 1200
        seed = (seed * 1103515245 + 12345) % 2**31
        y = 14 + seed % 330
        if 300 < x < 900 and y > 70:
            continue
        seed = (seed * 1103515245 + 12345) % 2**31
        tier = "aaaaabbbcc"[seed % 10]
        r = {"a": 1.1, "b": 1.4, "c": 1.8}[tier]
        tiers[tier].append(f'<circle cx="{x}" cy="{y}" r="{r}"></circle>')
        placed += 1
    return "\n".join(
        f'  <svg class="dawn-layer dawn-stars stars-{tier}" {DAWN_VIEWBOX}>{"".join(dots)}</svg>'
        for tier, dots in tiers.items()
    )


DAWN_HERO_SVG = f"""<div class="dawn-wrap" aria-hidden="true">
  <svg class="dawn-layer" {DAWN_VIEWBOX}>
    <defs>
      <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
        <stop class="stop-sky-1" offset="0%"></stop>
        <stop class="stop-sky-2" offset="42%"></stop>
        <stop class="stop-sky-3" offset="76%"></stop>
        <stop class="stop-sky-4" offset="100%"></stop>
      </linearGradient>
    </defs>
    <rect width="1200" height="900" fill="url(#skyGrad)"></rect>
  </svg>
  <svg class="dawn-layer dawn-glow" {DAWN_VIEWBOX}>
    <defs>
      <radialGradient id="glowGrad" cx="50%" cy="63%" r="75%">
        <stop class="stop-glow" offset="0%"></stop>
        <stop class="stop-glow-mid" offset="42%"></stop>
        <stop class="stop-glow-fade" offset="100%"></stop>
      </radialGradient>
    </defs>
    <ellipse cx="600" cy="560" rx="1000" ry="430" fill="url(#glowGrad)"></ellipse>
  </svg>
  <svg class="dawn-layer" {DAWN_VIEWBOX}>
    <defs>
      <linearGradient id="planetGrad" x1="0" y1="0" x2="0" y2="1">
        <stop class="stop-planet-rim" offset="0%"></stop>
        <stop class="stop-planet-deep" offset="26%"></stop>
      </linearGradient>
    </defs>
    <path d="M -40 560 Q 600 428 1240 560 L 1240 920 L -40 920 Z" fill="url(#planetGrad)"></path>
  </svg>
  <div class="dawn-layer night-veil"></div>
{_dawn_stars()}
  <svg class="dawn-layer dawn-limb" {DAWN_VIEWBOX}>
    <defs>
      <linearGradient id="limbGrad" x1="0" y1="0" x2="1" y2="0">
        <stop class="stop-limb-fade" offset="0%"></stop>
        <stop class="stop-limb" offset="50%"></stop>
        <stop class="stop-limb-fade" offset="100%"></stop>
      </linearGradient>
    </defs>
    <path class="limb-line" d="M -40 560 Q 600 428 1240 560" fill="none" stroke="url(#limbGrad)" stroke-width="5"></path>
  </svg>
</div>"""

PAGES = {
    ("en", "index"): {
        "title": "MarsDawn: a Markdown editor for Mac, with live preview",
        "description": "A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.",
        "intro": """
<section class="intro hero">
  <p class="kicker">Built for the AI workflow</p>
  <h1>Where an agent's Markdown gets a careful read.</h1>
  <p>An AI agent writes the Markdown. You review it in MarsDawn, source and rendered page side by side, then send it back for changes.</p>
</section>
""",
        "body": """
<h2 class="loop-title">The loop</h2>
<ol class="loop-steps">
  <li><strong>The agent writes.</strong> Your coding agent or writing assistant drafts the Markdown: a README, a spec, a set of notes.</li>
  <li><strong>You review in MarsDawn.</strong> Open the file and read it rendered, with Mermaid diagrams and highlighted code, next to the source.</li>
  <li><strong>The agent revises.</strong> Ask for changes. Open the revised file and read it the same way.</li>
</ol>
<p>Agents can drive MarsDawn directly: the free <a href="/cli/">marsdawn</a> command-line tool opens a file for review or exports a PDF, with JSON output built for scripts. See <a href="/cli/agents/">marsdawn for agents</a> for the details.</p>
""",
    },
    ("zh-hant", "index"): {
        "title": "MarsDawn：Mac 上的 Markdown 編輯器，即時預覽",
        "description": "原生的 Mac Markdown 編輯器，有即時預覽、Mermaid 圖表和 PDF 輸出，為讀 AI agent 寫的 Markdown 而做。即將在 Mac App Store 上架。",
        "intro": """
<section class="intro hero">
  <p class="kicker">為 AI 工作流程而生</p>
  <h1>讓 agent 寫的 Markdown，被好好讀過一遍。</h1>
  <p>AI agent 寫 Markdown，你在 MarsDawn 裡讀，原始碼和排版後的頁面並排顯示，再把修改意見交回去。</p>
</section>
""",
        "body": """
<h2 class="loop-title">整個循環</h2>
<ol class="loop-steps">
  <li><strong>Agent 動筆。</strong>你的程式碼助手或寫作 agent 先寫出 Markdown：README、規格文件，或一份筆記。</li>
  <li><strong>你在 MarsDawn 裡讀。</strong>打開檔案，看排版後的頁面，Mermaid 圖表和程式碼上色都在，旁邊就是原始碼。</li>
  <li><strong>Agent 修改。</strong>提出修改意見，agent 改好之後，再打開來讀一次。</li>
</ol>
<p>Agent 也能直接操作 MarsDawn：免費的 <a href="/zh-hant/cli/">marsdawn</a> 命令列工具能開啟檔案供你檢閱，也能輸出 PDF，並提供給腳本使用的 JSON 輸出。細節請看<a href="/zh-hant/cli/agents/">給 AI agent 的 marsdawn 參考</a>。</p>
""",
    },
    ("en", "privacy"): {
        "title": "Privacy Policy · MarsDawn",
        "description": "MarsDawn does not collect personal data. Your documents and settings stay on your Mac.",
        "body": f"""
<section class="intro">
  <h1>Privacy Policy</h1>
  <p>How MarsDawn, the Markdown editor for macOS, handles your information.</p>
  <p class="updated">Last updated {PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn does not collect any data about you.</strong> There is no account, no analytics, no advertising and no tracking. Your documents and settings stay on your Mac.</p></div>

<h2>What stays on your Mac</h2>
<ul>
  <li><strong>Your documents.</strong> MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.</li>
  <li><strong>Your settings.</strong> Appearance, preview theme, window layout and the image preference are stored in the app's own preferences on your Mac.</li>
  <li><strong>Folder access you grant.</strong> When you let MarsDawn show images or page files from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. A folder you open in the sidebar stays readable and writable by MarsDawn until you remove it in Settings, not just while its window is open. You can remove folders at any time in MarsDawn › Settings.</li>
</ul>

<h2>When MarsDawn uses the internet</h2>
<p>MarsDawn works fully offline. It connects to the internet only <strong>when you choose to</strong>, for a document that refers to the web:</p>
<ul>
  <li><strong>Markdown documents.</strong> Web images are blocked by default. They load only after you click <em>Load Images</em> in the preview, or if you turn on <em>Load remote images automatically</em> in Settings. Nothing else a Markdown document refers to is loaded from the web.</li>
  <li><strong>HTML documents.</strong> An HTML document opens static: its code doesn't run and nothing is loaded from the web. If a document contains code that could run, you can choose <em>View › Run This Document</em> for that document. Its own code then runs until you stop it, the document reloads or you close the window. That choice is never remembered, and it isn't a setting. While it runs, the document can send data over the network, and read images, style sheets, fonts and media in its folder and the folders inside it. Code downloaded from the web never runs.</li>
</ul>
<p>MarsDawn loads web content over https only. A plain http address is never loaded, in any setting, and MarsDawn does not rewrite it to https. In a Markdown document, the preview shows a placeholder in its place.</p>
<p>When web content loads, your Mac requests it directly from the servers that host it. Like any web request, this lets those servers see your IP address and what was requested. MarsDawn's developer receives none of this information.</p>
<p>Links you click in the preview open in your default web browser, under that browser's own privacy practices. Audio and video never play by themselves.</p>

<h2>Siri, Shortcuts and Spotlight</h2>
<p>MarsDawn offers actions for Siri, the Shortcuts app and Spotlight, such as creating a document or adding a note. When you use them, the text you provide is passed to MarsDawn on your Mac and saved only where the action says (a new document, or the <code>Inbox.md</code> file in the notes folder you chose). Speech you dictate to Siri is handled by Apple under <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

<h2>Exporting and printing</h2>
<p>PDF export and printing happen on your Mac. The PDF is saved where you choose. Printing goes through macOS to the printer you pick.</p>

<h2>The marsdawn command-line tool</h2>
<p>The optional <code>marsdawn</code> command-line tool, distributed separately, also runs entirely on your Mac. It reads the Markdown file you name and writes the PDF you ask for. It loads web images only when you pass <code>--allow-remote-images</code>.</p>

<h2>Children</h2>
<p>MarsDawn does not collect data from anyone, including children.</p>

<h2>Purchases</h2>
<p>MarsDawn will be sold through the Mac App Store. Apple will process the purchase under its own terms, and the developer never receives your payment details.</p>

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
  <p class="updated">最後更新：{PRIVACY_UPDATED}</p>
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
        "title": "marsdawn: a free Markdown to PDF command-line tool · MarsDawn",
        "description": "The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.",
        "body": f"""
<section class="intro">
  <h1>Command Line</h1>
  <p>The free <code>marsdawn</code> command-line tool: export Markdown to PDF from a shell or an LLM agent, and, with the MarsDawn app installed, open files in it.</p>
</section>

<div class="summary"><p><strong>marsdawn is free and distributed separately from the Mac App Store.</strong> Install it with Homebrew: on an Apple silicon Mac it arrives ready to run. <code>export</code> works on its own; <code>open</code> needs the MarsDawn app.</p></div>

<p>Calling marsdawn from an AI agent or a script? See <a href="/cli/agents/">marsdawn for agents</a> for the JSON output, its schemas and every exit code.</p>

<h2>Install</h2>
<p>With <a href="https://brew.sh">Homebrew</a>:</p>
<pre><code>{BREW_TAP_INSTALL}</code></pre>
<p>On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds, with nothing else to install. On an Intel Mac it builds marsdawn from source instead, which takes a few minutes and needs Xcode 26 or later (Swift 6.2). The tool runs on macOS 15 or later.</p>
<p>Or build it from <a href="{KIT_URL}">the source</a> with Swift Package Manager:</p>
<pre><code>git clone {KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Check which version you have with <code>marsdawn --version</code>.</p>

<h2>Commands</h2>

<h3>marsdawn open</h3>
<p>Opens one or more Markdown files in the MarsDawn app for review. It needs the app installed: without it, <code>marsdawn open</code> exits with code 3 and says MarsDawn isn't installed. <code>export</code> doesn't need the app.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>: asks MarsDawn to land on that line. A column after it, as in <code>notes.md:120:8</code>, is ignored. If a file with the whole name exists, the argument is that file.</li>
  <li><code>--line &lt;n&gt;</code>: the same for a single file, and the way to ask for a line on a path that itself ends in a colon and digits. Needs exactly one file.</li>
  <li>Lines run from 1 to 999999999.</li>
  <li>MarsDawn 1.0 opens the file but doesn't jump to the line yet.</li>
  <li><code>--json</code>: print a JSON result instead of text.</li>
</ul>
<p>Lines were added in marsdawn 0.3.0.</p>

<h3>marsdawn export</h3>
<p>Renders a Markdown file to a paginated PDF, with the same exporter MarsDawn's own PDF export uses. It doesn't need the MarsDawn app. Relative images resolve against the input file's folder.</p>
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
  <li><code>3</code>: MarsDawn is not installed (<code>open</code> only).</li>
  <li><code>4</code>: output exists (pass <code>--force</code>).</li>
  <li><code>5</code>: export failed.</li>
  <li><code>64</code>: usage error, including a line out of range or <code>--line</code> with more than one file.</li>
</ul>

<h2>--json output</h2>
<p>On success, <code>marsdawn open --json</code> prints <code>ok</code>, <code>opened</code> (a list with each file's <code>path</code>, plus <code>line</code> when one was asked for) and <code>app</code> (the app path). <code>marsdawn export --json</code> prints <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> and <code>diagramErrors</code>. On failure, both print <code>ok</code>, <code>error</code> and <code>message</code>.</p>
""",
    },
    ("zh-hant", "cli"): {
        "title": "marsdawn：免費的 Markdown 轉 PDF 命令列工具 · MarsDawn",
        "description": "免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。",
        "body": f"""
<section class="intro">
  <h1>命令列工具</h1>
  <p>免費的 <code>marsdawn</code> 命令列工具：從終端機或 LLM agent 把 Markdown 匯出成 PDF；裝了 MarsDawn app 的話，也能用它開啟檔案。</p>
</section>

<div class="summary"><p><strong>marsdawn 免費、另外發佈，不透過 Mac App Store。</strong>用 Homebrew 安裝，在 Apple 晶片的 Mac 上裝好就能直接使用。<code>export</code> 可以單獨使用；<code>open</code> 需要 MarsDawn app。</p></div>

<p>要從 AI agent 或腳本呼叫 marsdawn？請看<a href="/zh-hant/cli/agents/">給 AI agent 的 marsdawn 參考</a>，裡面有 JSON 輸出、Schema 和所有離開代碼。</p>

<h2>安裝</h2>
<p>使用 <a href="https://brew.sh">Homebrew</a>：</p>
<pre><code>{BREW_TAP_INSTALL}</code></pre>
<p>在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成，不需要另外安裝任何東西。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上（Swift 6.2）。這個工具需要 macOS 15 以上。</p>
<p>也可以從<a href="{KIT_URL}">原始碼</a>用 Swift Package Manager 建置：</p>
<pre><code>git clone {KIT_URL}.git
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
    },
}


# The agent reference. Every fact and every example is taken from
# redtear1115/mars-dawn-kit @ tag 0.3.0 (Sources/marsdawn/Commands.swift,
# Sources/marsdawn/main.swift, Sources/MarsDawnKit/RevealRequest.swift, Package.swift),
# and every example was run against a release build of that tag before publishing.
# The install command is the redtear1115/homebrew-tap formula: a prebuilt bottle on Apple silicon,
# a source build (Xcode 26) on Intel.
# Published schemas are never removed or edited: open.v1.json stays, byte for byte, for marsdawn 0.2.x, whose
# `opened` was a list of paths; 0.3.0 reports {path, line} objects (open.v2.json).
SCHEMA_BASE = "/schemas/cli/"
SCHEMA_FILES = {
    "export": "export.v1.json",
    "open": "open.v2.json",
    "error": "error.v1.json",
    "open_v1": "open.v1.json",
}

THEME_IDS = ["dawn", "classic", "modern", "vivid"]
PAPER_SIZES = ["a4", "letter"]
ERROR_KINDS = ["input_not_found", "app_not_installed", "output_exists", "export_failed"]


def schema_url(kind: str) -> str:
    return BASE_URL + SCHEMA_BASE + SCHEMA_FILES[kind]


SCHEMAS = {
    "export": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_url("export"),
        "title": "marsdawn export --json: success",
        "description": "Printed on stdout as one line when `marsdawn export --json` succeeds (exit code 0).",
        "type": "object",
        "required": ["ok", "output", "pages", "theme", "paper", "diagramErrors"],
        "additionalProperties": False,
        "properties": {
            "ok": {"const": True},
            "output": {"type": "string", "description": "Absolute path of the PDF that was written."},
            "pages": {"type": "integer", "minimum": 0, "description": "Number of pages in the PDF."},
            "theme": {"enum": THEME_IDS, "description": "Theme used for the export."},
            "paper": {"enum": PAPER_SIZES, "description": "Paper size used for the export."},
            "diagramErrors": {
                "type": "array",
                "items": {"type": "string"},
                "description": "One message per Mermaid diagram that failed to render. The PDF is still written.",
            },
        },
    },
    "open": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_url("open"),
        "title": "marsdawn open --json: success",
        "description": "Printed on stdout as one line when `marsdawn open --json` succeeds (exit code 0). marsdawn 0.3.0 and later.",
        "type": "object",
        "required": ["ok", "opened", "app"],
        "additionalProperties": False,
        "properties": {
            "ok": {"const": True},
            "opened": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": ["path"],
                    "additionalProperties": False,
                    "properties": {
                        "path": {"type": "string", "description": "Absolute path of the file that was opened."},
                        "line": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 999999999,
                            "description": "The line MarsDawn was asked to land on. Present only when one was asked for.",
                        },
                    },
                },
                "description": "The files that were opened, in the order given.",
            },
            "app": {"type": "string", "description": "Path of the MarsDawn app that opened them."},
        },
    },
    "open_v1": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_url("open_v1"),
        "title": "marsdawn open --json: success",
        "description": "Printed on stdout as one line when `marsdawn open --json` succeeds (exit code 0).",
        "type": "object",
        "required": ["ok", "opened", "app"],
        "additionalProperties": False,
        "properties": {
            "ok": {"const": True},
            "opened": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
                "description": "Absolute paths of the files that were opened.",
            },
            "app": {"type": "string", "description": "Path of the MarsDawn app that opened them."},
        },
    },
    "error": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_url("error"),
        "title": "marsdawn --json: failure",
        "description": "Printed on stdout as one line when a command run with --json fails with exit code 2, 3, 4 or 5. Usage errors (exit code 64) are printed as text on stderr instead.",
        "type": "object",
        "required": ["ok", "error", "message"],
        "additionalProperties": False,
        "properties": {
            "ok": {"const": False},
            "error": {"enum": ERROR_KINDS, "description": "Machine-readable failure kind."},
            "message": {"type": "string", "description": "Human-readable explanation."},
        },
    },
}


SCHEMA_NOTES = {
    "en": {
        "export": "export success",
        "open": "open success, marsdawn 0.3.0 and later",
        "error": "failure, both commands",
        "open_v1": "open success, marsdawn 0.2.x, where <code>opened</code> was a list of paths",
    },
    "zh-hant": {
        "export": "export 成功",
        "open": "open 成功，marsdawn 0.3.0 以後",
        "error": "兩個指令的失敗結果",
        "open_v1": "open 成功，marsdawn 0.2.x，當時 <code>opened</code> 是路徑清單",
    },
}


def schema_links(locale: str) -> str:
    return schema_links_from(SCHEMA_NOTES[locale])


def schema_links_from(notes: dict) -> str:
    return "\n".join(
        f'  <li><a href="{SCHEMA_BASE}{SCHEMA_FILES[kind]}">{SCHEMA_FILES[kind]}</a>: {notes[kind]}</li>'
        for kind in ("export", "open", "error", "open_v1")
    )


AGENT_PAGES = {
    ("en", "cli/agents"): {
        "title": "marsdawn for agents: Markdown to PDF from scripts · MarsDawn",
        "description": "A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.",
        "body": f"""
<section class="intro">
  <h1>marsdawn for agents</h1>
  <p>A reference for AI agents and scripts that call the <code>marsdawn</code> command-line tool. Every example on this page was run against the tool built from the current source.</p>
</section>

<div class="summary"><p><strong>To turn a Markdown file into a PDF, run <code>marsdawn export notes.md --json</code> and read one JSON object from stdout.</strong> Mermaid diagrams and highlighted code are rendered the same way as in the MarsDawn app. <code>export</code> doesn't need the app; <code>open</code> does.</p></div>

<h2>What it does</h2>
<ul>
  <li><code>export</code> renders one Markdown file to a paginated PDF with the same exporter as the MarsDawn app. No window opens.</li>
  <li><code>open</code> opens one or more Markdown files in the MarsDawn app, so a person can review them, and can name the line each file should land on.</li>
</ul>

<h2>What it does not do</h2>
<ul>
  <li>It doesn't read Markdown from stdin. Pass a file path.</li>
  <li>It doesn't write the PDF to stdout. The PDF always goes to a file; stdout carries only the result.</li>
  <li>It doesn't replace an existing file unless you pass <code>--force</code>.</li>
  <li>It doesn't load images from the web unless you pass <code>--allow-remote-images</code>, and then only over https.</li>
  <li><code>open</code> doesn't work without the MarsDawn app installed; it exits with code 3. <code>export</code> doesn't need the app.</li>
  <li>MarsDawn 1.0 doesn't jump to the line <code>open</code> names yet. It opens the file at the top.</li>
  <li>It runs on macOS only.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Writes <code>notes.pdf</code> next to <code>notes.md</code>. Options:</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: where to write the PDF. Defaults to the input path with a <code>.pdf</code> extension.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: the theme's light palette. Defaults to <code>$MARSDAWN_THEME</code>, then <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: paper size. Defaults to <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: load https images from the web while rendering.</li>
  <li><code>--force</code>: replace the output file if it exists.</li>
  <li><code>--json</code>: print one JSON object on stdout instead of text.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Success, exit code 0:</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>: absolute path of the PDF that was written.</li>
  <li><code>pages</code>: number of pages.</li>
  <li><code>theme</code> and <code>paper</code>: the values used.</li>
  <li><code>diagramErrors</code>: one message per Mermaid diagram that failed to render. The PDF is still written.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> names the line to land on. A column after it, as in <code>notes.md:120:8</code>, is ignored. An argument that names a file which exists is always that whole filename, so a file called <code>weird:12</code> opens as itself.</li>
  <li><code>--line &lt;n&gt;</code> names the line for a single file, including a path that itself ends in a colon and digits. It needs exactly one file.</li>
  <li>Lines run from 1 to 999999999. Anything else is a usage error.</li>
  <li>Lines were added in marsdawn 0.3.0. MarsDawn 1.0 opens the file but doesn't jump to the line yet.</li>
</ul>
<p>Success, exit code 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>: one object per file, in the order given. <code>path</code> is the file's absolute path; <code>line</code> appears only when a line was asked for.</li>
  <li><code>app</code>: path of the MarsDawn app that opened them.</li>
</ul>
<p>marsdawn 0.2.x printed <code>opened</code> as a list of path strings. Check <code>marsdawn --version</code> if you need to handle both.</p>

<h2>Failures</h2>
<p>With <code>--json</code>, a failure prints one JSON object on stdout and exits with its code:</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code>: the input doesn't exist, is a folder, or isn't UTF-8 text.</li>
  <li><code>3</code>, <code>app_not_installed</code>: MarsDawn isn't installed. Only <code>open</code> returns this.</li>
  <li><code>4</code>, <code>output_exists</code>: the output file exists. Pass <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code>: the export itself failed.</li>
  <li><code>64</code>: usage error, such as an unknown option, an invalid value, a line out of range or <code>--line</code> with more than one file. This one is printed as text on stderr, even with <code>--json</code>.</li>
</ul>

<h2>JSON Schemas</h2>
<p>JSON Schema (draft 2020-12) for every <code>--json</code> result:</p>
<ul>
{schema_links("en")}
</ul>

<h2>Environment variables</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>: the theme <code>export</code> uses when <code>--theme</code> isn't passed. An unknown value falls back to <code>dawn</code> without an error.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>The tool runs on macOS 15 or later. On Apple silicon, Homebrew installs a prebuilt bottle and nothing else is needed. Building it yourself, on an Intel Mac or from the source, needs Swift 6.2 or later, which comes with Xcode 26 or later.</li>
  <li>The MarsDawn app needs macOS 26 or later.</li>
</ul>

<h2>Install</h2>
<p>With Homebrew. On Apple silicon it pours a prebuilt bottle in seconds, with no Xcode needed. On an Intel Mac it compiles marsdawn from source, which takes a few minutes and needs Xcode 26 or later.</p>
<pre><code>{BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>Or build it from <a href="{KIT_URL}">the source</a>. The first build fetches dependencies and compiles, which also takes a few minutes.</p>
<pre><code>git clone {KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> prints the version number, such as <code>0.3.0</code>, and exits with code 0.</p>
""",
    },
    ("zh-hant", "cli/agents"): {
        "title": "給 AI agent 的 marsdawn 參考：用腳本轉 PDF · MarsDawn",
        "description": "給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。",
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
{schema_links("zh-hant")}
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
<pre><code>{BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>也可以從<a href="{KIT_URL}">原始碼</a>建置。第一次建置會下載相依套件並編譯，同樣需要幾分鐘。</p>
<pre><code>git clone {KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> 會印出版本號，例如 <code>0.3.0</code>，並以代碼 0 結束。</p>
""",
    },
}


# --- Trait pages (M1) ---------------------------------------------------------
# Five pages, one trait each, each proven by pointing at the real 1.0 app.
# Every claim matches the App Store listing (app repo docs/app-store-listing.md)
# or the privacy page. No competitor is named and no review is quoted.
# Screenshots are the app's own store screenshots (app repo
# docs/store-assets/screenshots), unmodified apart from resizing.
# The example on /markdown-to-pdf/, exactly as it was exported to make the page's images
# (/assets/cli/plan-en.png, plan-zh.png): `marsdawn export` 0.5.0, page 1 rendered with sips and
# cropped from the top to 930px. Change a document here and those images are out of date.
EXAMPLE_PLAN = {
    "en": '# Plan: faster exports\n\nAn agent wrote this plan. You review it, then turn it into a PDF.\n\n## Steps\n\n| Step | Owner | Status |\n|------|-------|--------|\n| Measure the slow pages | Agent | Done |\n| Cache rendered diagrams | Agent | In review |\n\nThe target is $t < 2\\,\\text{s}$ for a 50-page document:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Draft --> Review --> Ship\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n',
    "zh-hant": '# 計畫：讓輸出更快\n\n這份計畫由 agent 撰寫，你審閱後再把它轉成 PDF。\n\n## 步驟\n\n| 步驟 | 負責 | 狀態 |\n|------|------|------|\n| 找出慢的頁面 | Agent | 完成 |\n| 快取算好的圖表 | Agent | 審閱中 |\n\n目標是 50 頁的文件在 $t < 2\\,\\text{s}$ 內完成：\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  草稿 --> 審閱 --> 發佈\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n',
}

# Exit codes, one source for the skill (and anything else that lists them). The kinds must be
# ERROR_KINDS, in the same order, or the build stops.
EXIT_CODES = [
    (0, None, "Success. With --json, stdout is one JSON line."),
    (2, "input_not_found", "The input file isn't there."),
    (3, "app_not_installed", "MarsDawn isn't installed. Only `open` returns this."),
    (4, "output_exists", "The PDF already exists. Pass --force to replace it, or -o to write elsewhere."),
    (5, "export_failed", "Rendering failed."),
    (64, None, "Usage error: a bad option or value. Printed as text on stderr, never as JSON."),
]
assert [kind for _, kind, _ in EXIT_CODES if kind] == ERROR_KINDS, "EXIT_CODES and ERROR_KINDS disagree"


_PLAN_HTML = {locale: xml_escape(text) for locale, text in EXAMPLE_PLAN.items()}
_INSTALL = "brew install redtear1115/tap/marsdawn"
_SKILL_URL = f"{BASE_URL}/cli/skill/SKILL.md"

# DRAFT COPY for the owner: the two kit landing pages (see the app repo's docs/plan-kit-reach.md).
START_PAGES = {
    ("en", "markdown-to-pdf"): {
        "title": "Markdown to PDF on a Mac, from the command line · MarsDawn",
        "description": "Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.",
        "body": f"""
<section class="intro">
  <h1>Markdown to PDF on a Mac, from the command line.</h1>
  <p>The free <code>marsdawn</code> tool turns a Markdown file into a PDF with one command. Tables, math, Mermaid diagrams and highlighted code come out the way they read in the source, and it needs nothing else installed, not even the MarsDawn app.</p>
</section>
<h2>Install it</h2>
<pre><code>{_INSTALL}
marsdawn --version</code></pre>
<p>On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds. On an Intel Mac it builds from source instead, which takes a few minutes and needs Xcode 26 or later. It runs on macOS 15 or later, and <code>marsdawn --version</code> prints the version you got.</p>
<h2>Save a document</h2>
<p>Paste this into a file named <code>plan.md</code>:</p>
<pre><code>{_PLAN_HTML["en"]}</code></pre>
<h2>Export it</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>It writes <code>plan.pdf</code> next to the source and prints where it went:</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>This is that page, captured from a real run of <code>marsdawn</code> 0.5.0:</p>
<p><img class="pdf-page" src="/assets/cli/plan-en.png" alt="The exported PDF: the heading, a table of steps, an inline and a displayed formula, a Draft, Review, Ship diagram, and a highlighted line of Swift." width="989" height="930"></p>
<h2>Choose a theme, paper size and file name</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>: dawn, classic, modern or vivid, in the theme's light colors. Without it, <code>export</code> uses <code>$MARSDAWN_THEME</code>, then dawn.</li>
  <li><code>--paper</code>: a4 or letter. The default is a4.</li>
  <li><code>-o</code>: where to write the PDF, instead of next to the source.</li>
  <li><code>--allow-remote-images</code>: load images from the web while rendering. They stay off unless you pass it.</li>
</ul>
<h2>If it doesn't work</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew is building <code>marsdawn</code> from source, as it does on an Intel Mac. Install Xcode 26 or later from the App Store, then run the install again.</li>
  <li><code>marsdawn: No such file: …</code> The path doesn't point at a file. Check the name, or run the command from the folder the file is in.</li>
  <li><code>… already exists. Pass --force to replace it.</code> A PDF with that name is already there. Add <code>--force</code> to replace it, or <code>-o</code> to write it somewhere else.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> The theme or paper size isn't one it knows. The themes are dawn, classic, modern and vivid; the paper is a4 or letter.</li>
</ul>
<h2>Next</h2>
<ul>
  <li>Every option and the JSON it prints: <a href="/cli/">Command Line</a>.</li>
  <li>To have a coding agent do this for you: <a href="/cli/skill/">the marsdawn agent skill</a>.</li>
</ul>
""",
    },
    ("en", "view-markdown-on-mac"): {
        "title": "How to view a Markdown file on a Mac · MarsDawn",
        "description": "A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.",
        "body": f"""
<section class="intro">
  <h1>How to view a Markdown file on a Mac.</h1>
  <p>A <code>.md</code> file is plain text. The headings, bold words, tables and diagrams are written as marks: <code>#</code> for a heading, <code>**</code> around bold, pipes for a table, a <code>mermaid</code> code block for a diagram. Open it in a plain text editor and you read the marks. To read the page the way its author meant, something has to render it.</p>
</section>
<h2>Today, for free: turn it into a PDF</h2>
<p>The free <code>marsdawn</code> command-line tool renders a Markdown file to a PDF, which any Mac can open. Tables, math, Mermaid diagrams and highlighted code come out rendered, and it needs nothing else installed, not even the MarsDawn app.</p>
<pre><code>{BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> writes <code>notes.pdf</code> next to the Markdown file, and <code>open</code> shows it in your PDF viewer. It needs macOS 15 or later. The walk-through, with a real exported page, is on <a href="/markdown-to-pdf/">Markdown to PDF</a>.</p>
<h2>Coming soon: read it in MarsDawn</h2>
<p>MarsDawn is a Markdown editor for the Mac, coming soon to the Mac App Store. Open a <code>.md</code> file and read the rendered page next to the source:</p>
<ul>
  <li>The preview updates as you type, and the two panes scroll together.</li>
  <li>Mermaid flowcharts and sequence diagrams are drawn in the preview, and code blocks are highlighted.</li>
  <li>In Finder, press Space on a Markdown file for a Quick Look preview, diagrams included.</li>
  <li>When you want to change something, the source is right there. MarsDawn is an editor, not only a viewer.</li>
</ul>
<p>If an AI agent wrote the file, this is the loop MarsDawn is built for: the agent writes, you read it rendered, and it revises. See <a href="/">the home page</a>, and <a href="/cli/agents/">marsdawn for agents</a> for letting an agent open files for you.</p>
<h2>Next</h2>
<ul>
  <li>Every option of the command-line tool: <a href="/cli/">Command Line</a>.</li>
  <li>What MarsDawn doesn't do: <a href="/limits/">the list</a>.</li>
</ul>
""",
    },
    ("zh-hant", "view-markdown-on-mac"): {
        "title": "在 Mac 上怎麼看 Markdown 檔案 · MarsDawn",
        "description": "md 檔案是加上格式記號的純文字。這頁說明怎麼在 Mac 上看到排版後的樣子：現在可以用免費的 marsdawn 命令列工具轉成 PDF，之後可以用即將在 Mac App Store 上架的 MarsDawn app。",
        "body": f"""
<section class="intro">
  <h1>在 Mac 上，怎麼看 Markdown 檔案。</h1>
  <p><code>.md</code> 檔案是純文字。標題、粗體、表格和圖表，都是用記號寫成的：<code>#</code> 代表標題，<code>**</code> 包住粗體，直線符號畫出表格，<code>mermaid</code> 程式碼區塊則是一張圖。用純文字編輯器打開，看到的就是這些記號。想照作者的意思讀到排好的頁面，就需要有東西把它排版出來。</p>
</section>
<h2>現在就能用，而且免費：轉成 PDF</h2>
<p>免費的 <code>marsdawn</code> 命令列工具，能把 Markdown 檔案排版成 PDF，任何一台 Mac 都打得開。表格、數學式、Mermaid 圖表和程式碼上色都會排好，而且不需要安裝其他東西，連 MarsDawn app 都不用。</p>
<pre><code>{BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> 會在 Markdown 檔案旁邊寫出 <code>notes.pdf</code>，<code>open</code> 會用你的 PDF 檢視器打開它。這個工具需要 macOS 15 以上。完整步驟和一頁實際匯出的結果，請看<a href="/zh-hant/markdown-to-pdf/">Markdown 轉 PDF</a>。</p>
<h2>即將推出：在 MarsDawn 裡讀</h2>
<p>MarsDawn 是為 Mac 做的 Markdown 編輯器，即將在 Mac App Store 上架。打開 <code>.md</code> 檔案，排好的頁面就在原始碼旁邊：</p>
<ul>
  <li>預覽會隨著你打字即時更新，兩邊的窗格一起捲動。</li>
  <li>Mermaid 流程圖和循序圖直接畫在預覽裡，程式碼區塊也會上色。</li>
  <li>在 Finder 裡對 Markdown 檔案按空白鍵，就有「快速查看」預覽，圖表也在。</li>
  <li>想改的時候，原始碼就在旁邊。MarsDawn 是編輯器，不只是檢視器。</li>
</ul>
<p>如果這份檔案是 AI agent 寫的，這正是 MarsDawn 要支援的循環：agent 寫，你讀排好的頁面，agent 再修改。請看<a href="/zh-hant/">首頁</a>，想讓 agent 幫你開檔案，請看<a href="/zh-hant/cli/agents/">給 AI agent 的 marsdawn 參考</a>。</p>
<h2>接下來</h2>
<ul>
  <li>命令列工具的所有選項：<a href="/zh-hant/cli/">命令列工具</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hant/limits/">這份清單</a>。</li>
</ul>
""",
    },
    ("zh-hant", "markdown-to-pdf"): {
        "title": "Markdown 轉 PDF 工具：在 Mac 用命令列轉檔 · MarsDawn",
        "description": "免費的 Markdown 轉 PDF 工具：在 Mac 上用 marsdawn 命令列，一個指令就把 Markdown 轉成 PDF，表格、數學式、Mermaid 圖表和程式碼上色都在。",
        "body": f"""
<section class="intro">
  <h1>Markdown 轉 PDF 工具：在 Mac 上用命令列轉檔。</h1>
  <p>免費的 <code>marsdawn</code> 工具只要一個指令，就能把 Markdown 檔案轉成 PDF。表格、數學式、Mermaid 圖表和程式碼上色，都會照原始檔的樣子呈現，而且不需要安裝其他東西，連 MarsDawn app 都不用。</p>
</section>
<h2>安裝</h2>
<pre><code>{_INSTALL}
marsdawn --version</code></pre>
<p>在 Apple 晶片的 Mac 上，Homebrew 會直接安裝預先建置好的版本，幾秒就完成。在 Intel Mac 上則會從原始碼建置，需要幾分鐘，也需要 Xcode 26 以上。這個工具需要 macOS 15 以上，<code>marsdawn --version</code> 會印出你裝到的版本。</p>
<h2>存一份文件</h2>
<p>把下面的內容貼進一個叫 <code>plan.md</code> 的檔案：</p>
<pre><code>{_PLAN_HTML["zh-hant"]}</code></pre>
<h2>匯出</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>它會在原始檔旁邊寫出 <code>plan.pdf</code>，並印出存放的位置：</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>這是那一頁，擷取自 <code>marsdawn</code> 0.5.0 的實際執行結果：</p>
<p><img class="pdf-page" src="/assets/cli/plan-zh.png" alt="匯出的 PDF：標題、步驟表格、行內與獨立的數學式、「草稿、審閱、發佈」流程圖，以及一行上色的 Swift 程式碼。" width="989" height="930"></p>
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
  <li>所有選項和它印出的 JSON：<a href="/zh-hant/cli/">命令列工具</a>。</li>
  <li>讓寫程式的 agent 幫你做這件事：<a href="/zh-hant/cli/skill/">marsdawn 的 agent skill</a>。</li>
</ul>
""",
    },
    ("en", "vs/macmd-viewer"): {
        "title": "MacMD Viewer vs. MarsDawn: a viewer or an editor · MarsDawn",
        "description": "MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.",
        "body": """
<section class="intro">
  <h1>MacMD Viewer vs. MarsDawn.</h1>
  <p>Both are Mac apps for reading Markdown rendered. MacMD Viewer opens a <code>.md</code> file and shows the finished page; it doesn't edit it. MarsDawn puts an editor next to the same kind of rendered preview, so you write and review in one window. Here's how they differ, feature by feature.</p>
</section>
<h2>If you only need to read, not edit</h2>
<p>If your job is strictly reading Markdown someone else wrote, and you never need to touch the source, MacMD Viewer is a reasonable fit: it's built for exactly that, is available now and works down to an older macOS. MarsDawn is worth it once reading isn't the whole job, because an agent's Markdown usually comes back for another pass.</p>
<h2>What each app does</h2>
<ul>
  <li><strong>Editing:</strong> MacMD Viewer is read-only by design. MarsDawn edits the source and renders it side by side, so a change shows up as you type.</li>
  <li><strong>Preview themes:</strong> MacMD Viewer ships 12 document themes. MarsDawn ships four, Dawn, Classic, Modern and Vivid, each with a light and a dark palette.</li>
  <li><strong>Diagrams and math:</strong> both render Mermaid diagrams and highlight code. MarsDawn also renders KaTeX math; MacMD Viewer's own listing doesn't mention math rendering.</li>
  <li><strong>Finder integration:</strong> both add a Quick Look extension, so pressing Space on a <code>.md</code> file in Finder shows the rendered page.</li>
  <li><strong>PDF and print:</strong> both export or print a PDF of the rendered page.</li>
  <li><strong>System requirements:</strong> MacMD Viewer needs macOS 14 (Sonoma) or later. MarsDawn needs macOS 26 (Tahoe) or later.</li>
  <li><strong>Languages:</strong> MarsDawn's interface ships in {langs}. MacMD Viewer's own materials don't state a UI language, so this page doesn't compare that.</li>
</ul>
<h2>Pricing and how you buy it</h2>
<ul>
  <li><strong>Where you buy it:</strong> MacMD Viewer is a direct download from its own site, also on Homebrew and Setapp; it isn't on the Mac App Store. MarsDawn is Mac App Store only.</li>
  <li><strong>Price:</strong> MacMD Viewer is USD 19.99 once for one Mac (a 3-Mac pack and volume packs cost more). MarsDawn is a free download, then a USD 4.99 one-time unlock.</li>
  <li><strong>Trying it first:</strong> MacMD Viewer has no free trial; direct purchases carry a 14-day money-back guarantee instead. MarsDawn gives you a 14-day trial before you pay anything.</li>
  <li><strong>Refunds and updates:</strong> MacMD Viewer's refunds and updates run through its own site. MarsDawn's purchase goes through Apple, so refunds and updates use Apple's standard process.</li>
  <li><strong>Accounts:</strong> neither app needs an account to use.</li>
</ul>
<h2>Try it today, free</h2>
<p>MarsDawn is coming soon to the Mac App Store, not on sale yet. Until then, the free <code>marsdawn</code> command-line tool renders any Markdown file to a PDF today, with Mermaid diagrams and highlighted code, and needs nothing else installed:</p>
<pre><code>{brew}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Next</h2>
<ul>
  <li>The full walk-through: <a href="/markdown-to-pdf/">Markdown to PDF</a>.</li>
  <li>What MarsDawn doesn't do: <a href="/limits/">the list</a>.</li>
  <li>Every option of the command-line tool: <a href="/cli/">Command Line</a>.</li>
</ul>
""".format(brew=BREW_TAP_INSTALL, langs=APP_UI_LANGUAGES["en"]),
    },
    ("zh-hant", "vs/macmd-viewer"): {
        "title": "MacMD Viewer 對比 MarsDawn：檢視器與編輯器 · MarsDawn",
        "description": "MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。",
        "body": """
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
  <li><strong>語言：</strong>MarsDawn 的介面有{langs}。MacMD Viewer 自己的資料沒有寫出介面語言，這頁就不比較這一項。</li>
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
<pre><code>{brew}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>接下來</h2>
<ul>
  <li>完整步驟：<a href="/zh-hant/markdown-to-pdf/">Markdown 轉 PDF</a>。</li>
  <li>MarsDawn 做不到的事：<a href="/zh-hant/limits/">這份清單</a>。</li>
  <li>命令列工具的所有選項：<a href="/zh-hant/cli/">命令列工具</a>。</li>
</ul>
""".format(brew=BREW_TAP_INSTALL, langs=APP_UI_LANGUAGES["zh-hant"]),
    },
}

SKILL_PAGES = {
    ("en", "cli/skill"): {
        "title": "A coding-agent skill for Markdown to PDF · MarsDawn",
        "description": "One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.",
        "body": f"""
<section class="intro">
  <h1>Let your agent make the PDF.</h1>
  <p>This skill is one Markdown file. It teaches a coding agent to install <code>marsdawn</code>, check that it works, export a document to PDF and read the result, so the agent that wrote the Markdown can hand you the PDF as well.</p>
</section>
<h2>Install it in Claude Code</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {_SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code loads it when a task calls for a PDF, and you can run it yourself as <code>/marsdawn</code>. It's <a href="/cli/skill/SKILL.md">one short file</a>, so read it before you install it.</p>
<p>Other agents can use the same file. It's plain Markdown, instructions and commands, so point yours at the URL or paste it in.</p>
<h2>What it teaches</h2>
<ul>
  <li>Install <code>marsdawn</code> with Homebrew if it's missing, then check it with <code>marsdawn --version</code> instead of assuming a version.</li>
  <li>Export with <code>marsdawn export … --json</code>, and read the result: where the PDF went, how many pages it has, and any Mermaid diagram that didn't render.</li>
  <li>Tell the failures apart by exit code: no such file, a PDF already there, a failed export, a bad option.</li>
  <li>Use <code>open</code> only when the MarsDawn app is installed, and never to make a PDF.</li>
</ul>
<h2>What it doesn't do</h2>
<ul>
  <li>It doesn't give itself permission to run anything. Your agent still asks before it installs <code>marsdawn</code> or runs it, as it would for any other command.</li>
  <li>It doesn't send your documents anywhere. <code>marsdawn</code> renders on your Mac, and it leaves out images from the web unless you pass <code>--allow-remote-images</code>.</li>
</ul>
<p>The whole contract, every field and every code, is in <a href="/cli/agents/">marsdawn for agents</a>.</p>
""",
    },
    ("zh-hant", "cli/skill"): {
        "title": "讓寫程式的 agent 把 Markdown 轉 PDF 的 skill · MarsDawn",
        "description": "一個檔案，讓寫程式的 agent 學會安裝 marsdawn、確認它能用、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。",
        "body": f"""
<section class="intro">
  <h1>讓 agent 幫你做出 PDF。</h1>
  <p>這個 skill 是一個 Markdown 檔案。它教寫程式的 agent 安裝 <code>marsdawn</code>、確認它能用、把文件匯出成 PDF 並讀懂結果，這樣寫出 Markdown 的 agent，也能把 PDF 交給你。</p>
</section>
<h2>在 Claude Code 中安裝</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {_SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
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
<p>完整的規格，每個欄位和每個代碼，都在<a href="/zh-hant/cli/agents/">給 AI agent 的 marsdawn 參考</a>裡。</p>
""",
    },
}


def build_skill_md() -> str:
    """The agent skill, built from the same constants as /cli/agents/ so the two can't drift.

    No `allowed-tools`: a skill someone downloads shouldn't pre-approve shell commands for itself.
    No version number: the agent checks `marsdawn --version` against what it installed instead.
    """
    success = SCHEMAS["export"]["properties"]
    fields = "\n".join(f"- `{name}`: {spec['description'] if 'description' in spec else 'always true'}"
                       for name, spec in success.items())
    codes = "\n".join(f"| {code} | {f'`{kind}`' if kind else '—'} | {meaning} |"
                      for code, kind, meaning in EXIT_CODES)
    return f"""---
name: marsdawn
description: Export Markdown to PDF with the marsdawn command-line tool on macOS, and read its JSON result. Use when asked to turn a Markdown file into a PDF, or to render Markdown with tables, math, Mermaid diagrams or highlighted code into a PDF.
---

# marsdawn

`marsdawn export` renders a Markdown file to PDF on macOS 15 or later. It needs nothing else
installed, not even the MarsDawn app.

## Install and check

```sh
command -v marsdawn || {_INSTALL}
marsdawn --version
```

Use the version it prints. Don't assume one. On Apple silicon Homebrew pours a prebuilt bottle;
on an Intel Mac it builds from source and needs Xcode 26 or later. If the install stops with
"A full installation of Xcode.app 26.0 is required", say so rather than retrying.

## Export

```sh
marsdawn export input.md --json
```

Options: `-o out.pdf` (default: beside the input), `--theme {"|".join(THEME_IDS)}`,
`--paper {"|".join(PAPER_SIZES)}`, `--force` to replace an existing PDF, and
`--allow-remote-images` to load web images, which are left out by default.

On success it exits 0 and prints one JSON line:

{fields}

If `diagramErrors` isn't empty, the PDF was still written: tell the user which diagrams failed.

## Exit codes

On failure with `--json` it prints `{{"ok": false, "error": <kind>, "message": ...}}`.

| Code | `error` | Meaning |
|---|---|---|
{codes}

## open

`marsdawn open file.md` opens a file in the MarsDawn app for review. It needs the app; without
it, it exits 3. Never use it to make a PDF: that's `export`.

## Full contract

Every field, schema and code: {BASE_URL}/cli/agents/
"""


TRAIT_ORDER = ["yours", "pay-once", "pdf", "native", "limits"]

STORE_CHIP = {
    "en": "Coming soon to the Mac App Store",
    "zh-hant": "即將在 Mac App Store 上架",
}

# Callouts: (x %, y %) of the marker on the original 1440x900 store screenshot,
# which side's gutter the label sits in, and the label in each language. The
# published image is cropped to the app window (CROPS), and the positions are
# converted to the cropped frame when annotations.css is written.
CROPS = {
    "01-split": (130, 24, 1180, 844),
    "02-classic": (130, 24, 1180, 844),
    "03-dark": (130, 24, 1180, 844),
    "04-vivid": (130, 24, 1180, 844),
    "05-pdf": (230, 66, 980, 760),
}
SMALL_WIDTH = 800


def cropped_position(image: str, x: float, y: float) -> tuple:
    ox, oy, w, h = CROPS[image]
    return round((x * 14.4 - ox) / w * 100, 2), round((y * 9.0 - oy) / h * 100, 2)
FIGURES = {
    "index": {
        "image": "01-split",
        "alt": {
            "en": "MarsDawn in split view: the Markdown source on the left, the rendered page on the right.",
            "zh-hant": "MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。",
        },
        "callouts": [],
    },
    "yours": {
        "image": "02-classic",
        "alt": {
            "en": "MarsDawn showing a document in the Classic theme, with the preview filling the window.",
            "zh-hant": "MarsDawn 以 Classic 主題顯示文件，預覽佔滿整個視窗。",
        },
        "callouts": [
            (16.53, 7.0, "l", {"en": "A file on your Mac, saved where you choose.", "zh-hant": "你 Mac 上的一個檔案，存在你選的地方。"}),
            (88.89, 5.56, "r", {"en": "The whole toolbar is themes and layouts; there is nothing to sign in to.", "zh-hant": "整條工具列只有主題和版面，沒有任何需要登入的地方。"}),
        ],
    },
    "pay-once": {
        "image": "04-vivid",
        "alt": {
            "en": "MarsDawn in the Vivid theme, with Markdown source on the left and the rendered page on the right.",
            "zh-hant": "MarsDawn 使用 Vivid 主題，左邊是 Markdown 原始碼，右邊是排版後的頁面。",
        },
        "callouts": [
            (10.07, 26.22, "l", {"en": "Markdown highlighting in the editor, included.", "zh-hant": "編輯器的 Markdown 語法上色，包含在內。"}),
            (88.89, 5.56, "r", {"en": "Every theme and every layout is included.", "zh-hant": "所有主題和版面都包含在內。"}),
            (88.54, 38.89, "r", {"en": "Mermaid diagrams, included.", "zh-hant": "Mermaid 圖表，包含在內。"}),
            (87.5, 66.67, "r", {"en": "Code highlighting, included.", "zh-hant": "程式碼上色，包含在內。"}),
        ],
    },
    "pdf": {
        "image": "05-pdf",
        "alt": {
            "en": "A PDF exported from MarsDawn, open in its PDF viewer with page thumbnails.",
            "zh-hant": "用 MarsDawn 輸出的 PDF，在內建的 PDF 檢視器中開啟，旁邊有頁面縮圖。",
        },
        "callouts": [
            (80.56, 57.89, "r", {"en": "Mermaid diagrams, drawn into the PDF.", "zh-hant": "Mermaid 圖表直接畫進 PDF。"}),
            (78.47, 84.44, "r", {"en": "Code keeps its highlighting.", "zh-hant": "程式碼保留語法上色。"}),
        ],
    },
    "native": {
        "image": "01-split",
        "alt": {
            "en": "MarsDawn in split view: the Markdown source on the left, the rendered page on the right.",
            "zh-hant": "MarsDawn 的並排版面：左邊是 Markdown 原始碼，右邊是排版後的頁面。",
        },
        "callouts": [
            (16.53, 7.33, "l", {"en": "A native Mac window.", "zh-hant": "原生的 Mac 視窗。"}),
            (10.07, 24.22, "l", {"en": "The Mac's text editor, with Markdown highlighting.", "zh-hant": "Mac 原生的文字編輯器，附 Markdown 語法上色。"}),
            (88.89, 5.56, "r", {"en": "⌘1 source, ⌘2 split, ⌘3 preview.", "zh-hant": "⌘1 原始碼、⌘2 並排、⌘3 預覽。"}),
            (69.44, 13.78, "r", {"en": "The page updates as you type.", "zh-hant": "頁面會隨著打字更新。"}),
        ],
    },
    "limits": {
        "image": "03-dark",
        "alt": {
            "en": "MarsDawn in dark mode, with Markdown source on the left and the rendered page on the right.",
            "zh-hant": "MarsDawn 的深色模式，左邊是 Markdown 原始碼，右邊是排版後的頁面。",
        },
        "callouts": [
            (16.53, 7.0, "l", {"en": "One document per window, on this Mac.", "zh-hant": "一個視窗一份文件，就在這台 Mac 上。"}),
            (10.07, 14.0, "l", {"en": "You write Markdown here.", "zh-hant": "你在這裡寫 Markdown。"}),
            (88.89, 5.56, "r", {"en": "The toolbar holds themes and layouts, and there is no plugins menu.", "zh-hant": "工具列只有主題和版面，沒有外掛選單。"}),
            (70.14, 13.78, "r", {"en": "The page is for reading, not editing.", "zh-hant": "這一側用來閱讀，不能直接編輯。"}),
        ],
    },
}


def _trait_page(title, description, intro, body):
    return {"title": title, "description": description, "intro": intro, "body": body}


TRAIT_PAGES = {
    ("en", "yours"): _trait_page(
        "A Mac Markdown editor with no account and no cloud · MarsDawn",
        "MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.",
        """
<section class="intro">
  <h1>Your writing stays on your Mac.</h1>
  <p>MarsDawn has no account, no sync and no cloud. It opens a file, you write, and it saves the file where you chose.</p>
</section>
""",
        """
<h2>What that means</h2>
<ul>
  <li>There is no account to sign up for or sign in to.</li>
  <li>Nothing syncs to a cloud. Your documents stay where you save them.</li>
  <li>Nothing is tracked. MarsDawn does not collect any data about you, and its App Store privacy label is "Data Not Collected".</li>
  <li>Web images stay blocked until you choose to load them, so opening a document never tells a server you read it. When you do load them, they load over https only.</li>
  <li>Local images show in the preview once you grant access to their folder.</li>
</ul>
<p>The details are in the <a href="/privacy/">privacy policy</a>.</p>
""",
    ),
    ("zh-hant", "yours"): _trait_page(
        "不用帳號、不上雲端的 Mac Markdown 編輯器 · MarsDawn",
        "MarsDawn 不需要帳號，沒有同步，也沒有雲端。你的 Markdown 文件留在你的 Mac 上，就在你選的檔案和資料夾裡。",
        """
<section class="intro">
  <h1>你寫的內容，留在你的 Mac 上。</h1>
  <p>MarsDawn 不需要帳號，沒有同步，也沒有雲端。它打開檔案、讓你寫，再存回你選的位置。</p>
</section>
""",
        """
<h2>這代表什麼</h2>
<ul>
  <li>不需要帳號，不用註冊，也不用登入。</li>
  <li>不會同步到雲端，文件存在哪裡就留在哪裡。</li>
  <li>不追蹤任何行為。MarsDawn 不收集任何關於你的資料，App Store 隱私權標示為「未收集資料」。</li>
  <li>網路圖片在你選擇載入之前一律不載入，打開文件不會讓任何伺服器知道你讀了它。選擇載入時，也只走 https。</li>
  <li>本機圖片在你授權資料夾存取後，就會顯示在預覽中。</li>
</ul>
<p>完整說明請看<a href="/zh-hant/privacy/">隱私權政策</a>。</p>
""",
    ),
    ("en", "pay-once"): _trait_page(
        "Try it free, then pay once · MarsDawn",
        "MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.",
        """
<section class="intro">
  <h1>Try all of it. Then pay once.</h1>
  <p>MarsDawn is a free download. Start the 14-day trial and every feature works; to keep using it after that, one purchase of USD 4.99 unlocks it. There is no subscription and no account.</p>
</section>
""",
        """
<h2>How it works</h2>
<ul>
  <li>MarsDawn is free to download from the Mac App Store.</li>
  <li>Start the trial and everything works for 14 days: every theme and layout, PDF export and printing, Quick Look, and the Siri and Shortcuts actions.</li>
  <li>To keep using it after that, unlock it once for USD 4.99. It's an in-app purchase, not a subscription, so nothing renews and nothing charges you later.</li>
  <li>The trial doesn't charge you either. When it ends, nothing is bought unless you choose to unlock.</li>
  <li>There is no account. MarsDawn never asks you to create one.</li>
</ul>
<h2>If you don't unlock</h2>
<ul>
  <li>After 14 days, until you unlock it, you can't read, edit, export or print documents in MarsDawn. A document still opens, but its content is covered.</li>
  <li>Your files don't change. They're ordinary files on your Mac, and Quick Look in Finder keeps showing them.</li>
  <li>The free <a href="/cli/"><code>marsdawn</code> command-line tool</a> keeps exporting them to PDF, trial or not.</li>
  <li>If a document is open in MarsDawn when the trial ends, the text you typed isn't lost: use File ▸ Save As… to keep it.</li>
</ul>
""",
    ),
    ("zh-hant", "pay-once"): _trait_page(
        "免費試用，買一次就好 · MarsDawn",
        "MarsDawn 免費下載。先免費試用 14 天，之後花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。",
        """
<section class="intro">
  <h1>先全部試用，再買一次。</h1>
  <p>MarsDawn 可以免費下載。開始 14 天試用後，所有功能都能使用；試用結束後想繼續使用，花 USD 4.99 解鎖一次就好。沒有訂閱，也不需要帳號。</p>
</section>
""",
        """
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
  <li>免費的 <a href="/zh-hant/cli/"><code>marsdawn</code> 命令列工具</a>不受試用影響，依然能把它們匯出成 PDF。</li>
  <li>如果試用結束時有文件正開在 MarsDawn 裡，你輸入的文字不會遺失，可以用「檔案」▸「另存新檔⋯」保存。</li>
</ul>
""",
    ),
    ("en", "pdf"): _trait_page(
        "Export Markdown to PDF on a Mac, diagrams included · MarsDawn",
        "Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.",
        """
<section class="intro">
  <h1>The PDF looks like the page you wrote.</h1>
  <p>Export as PDF or print, in your theme's light colors. Diagrams and highlighted code come through, and page breaks avoid splitting what belongs together.</p>
</section>
""",
        """
<h2>What that means</h2>
<ul>
  <li>Mermaid diagrams are drawn into the PDF.</li>
  <li>Code blocks keep their syntax highlighting.</li>
  <li>Page breaks avoid leaving a heading at the bottom of a page or splitting code, tables and diagrams.</li>
  <li>Any layout. Export works even while only the source is showing.</li>
</ul>
<p>The free <a href="/cli/">marsdawn command-line tool</a> uses the same exporter, so a script or an AI agent gets the same PDF.</p>
""",
    ),
    ("zh-hant", "pdf"): _trait_page(
        "在 Mac 把 Markdown 輸出成 PDF，圖表也在 · MarsDawn",
        "在 Mac 上把 Markdown 輸出成 PDF 或列印，Mermaid 圖表和程式碼上色都會保留；分頁會盡量不切開短的程式碼和表格，超過一頁的會接到下一頁。",
        """
<section class="intro">
  <h1>PDF 看起來就是你寫的那一頁。</h1>
  <p>輸出成 PDF 或列印，使用主題的淺色配色。圖表和程式碼上色都會保留，分頁位置也經過安排。</p>
</section>
""",
        """
<h2>這代表什麼</h2>
<ul>
  <li>Mermaid 圖表直接畫進 PDF。</li>
  <li>程式碼區塊保留語法上色。</li>
  <li>分頁時會盡量不讓標題落在頁尾，也不切開程式碼、表格和圖表。</li>
  <li>任何版面都能輸出，只顯示原始碼時也可以。</li>
</ul>
<p>免費的 <a href="/zh-hant/cli/">marsdawn 命令列工具</a>使用同一套輸出程式，所以腳本或 AI agent 也能得到一樣的 PDF。</p>
""",
    ),
    ("en", "native"): _trait_page(
        "A native Markdown app for Mac: tabs, Quick Look · MarsDawn",
        "A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.",
        """
<section class="intro">
  <h1>Built out of the Mac's own parts.</h1>
  <p>The windows, tabs, menus and text editor are the Mac's own. The rendered page is drawn by WebKit, the engine behind Safari.</p>
</section>
""",
        f"""
<h2>What that means</h2>
<ul>
  <li>Source, split and preview layouts, one keystroke apart (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>The two panes scroll together, so the paragraph you are editing stays in view.</li>
  <li>Markdown syntax highlighting in the editor, matched to your preview theme.</li>
  <li>Native windows, tabs, autosave and version history.</li>
  <li>Quick Look: press Space on a Markdown file in Finder for a preview, diagrams included.</li>
  <li>Siri and Shortcuts: start a new document from a template, add a line to your notes inbox, or reopen a recent document.</li>
  <li>{APP_UI_LANGUAGES["en"]}.</li>
</ul>
""",
    ),
    ("zh-hant", "native"): _trait_page(
        "原生的 Mac Markdown app：分頁、快速查看 · MarsDawn",
        "真正的 Mac app：原生視窗與分頁、自動儲存、版本記錄、在 Finder 用快速查看預覽 Markdown，文字編輯器的操作和 Mac 上其他 app 一致。",
        """
<section class="intro">
  <h1>用 Mac 原生的元件做的。</h1>
  <p>視窗、分頁、選單和文字編輯器都是 Mac 原生的。排版後的頁面由 Safari 使用的 WebKit 引擎繪製。</p>
</section>
""",
        f"""
<h2>這代表什麼</h2>
<ul>
  <li>原始碼、並排、預覽三種版面，一個快捷鍵切換（<kbd>⌘1</kbd>、<kbd>⌘2</kbd>、<kbd>⌘3</kbd>）。</li>
  <li>兩側同步捲動，正在編輯的段落一直在眼前。</li>
  <li>編輯器內建 Markdown 語法上色，顏色與預覽主題一致。</li>
  <li>原生視窗、分頁、自動儲存和版本記錄。</li>
  <li>快速查看：在 Finder 選取 Markdown 檔按空白鍵就能預覽，圖表也會顯示。</li>
  <li>Siri 和捷徑：用範本新增文件、在筆記收件匣加上一行，或重新打開最近的文件。</li>
  <li>支援{APP_UI_LANGUAGES["zh-hant"]}。</li>
</ul>
""",
    ),
    ("en", "limits"): _trait_page(
        "What MarsDawn doesn't do · MarsDawn",
        "No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.",
        """
<section class="intro">
  <h1>What MarsDawn doesn't do.</h1>
  <p>Some things are left out on purpose. If you need one of them, it's better to know now than after you buy.</p>
</section>
""",
        """
<h2>Left out</h2>
<ul>
  <li><strong>Sync:</strong> MarsDawn doesn't sync your documents. They stay where you save them, so to use one on another Mac, keep it in a folder you already sync.</li>
  <li><strong>iPhone and iPad:</strong> there is no app for them; MarsDawn is for the Mac.</li>
  <li><strong>Plugins:</strong> MarsDawn has no plugins or extensions.</li>
  <li><strong>Sharing:</strong> there are no accounts and no shared editing, because MarsDawn is for one person on their own Mac.</li>
  <li><strong>Editing:</strong> you write Markdown on the left and read the page on the right; the page itself can't be edited.</li>
  <li><strong>Formats:</strong> MarsDawn exports PDF and prints, and doesn't export Word files.</li>
  <li><strong>Themes:</strong> it comes with Dawn, Classic, Modern and Vivid, each in light and dark, and you can't install others.</li>
  <li><strong>Other files:</strong> plain text files and PDFs open read-only.</li>
  <li><strong>After the trial:</strong> if you don't unlock MarsDawn once the 14-day trial ends, you can't read or edit documents in it: they open with their content covered. Your files stay as they are, Quick Look still shows them, and the free command-line tool still exports them.</li>
  <li><strong>System:</strong> MarsDawn needs macOS 26 or later.</li>
</ul>
""",
    ),
    ("zh-hant", "limits"): _trait_page(
        "MarsDawn 做不到的事 · MarsDawn",
        "沒有同步、沒有 iPhone 或 iPad 版、沒有外掛、不需要帳號，內建四種主題。購買前先知道。",
        """
<section class="intro">
  <h1>MarsDawn 做不到的事。</h1>
  <p>有些功能是刻意不做的。如果你需要其中一項，現在知道總比買了之後才發現好。</p>
</section>
""",
        """
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
    ),
}

TRAIT_LINK = {
    "en": {
        "yours": ("Your writing stays on your Mac", "No account, no sync, no cloud."),
        "pay-once": ("Try free, pay once", "Free for 14 days, then USD 4.99 once. No subscription."),
        "pdf": ("PDF export", "Diagrams, highlighted code, careful page breaks."),
        "native": ("A Mac app", "Native windows, tabs, autosave, Quick Look."),
        "limits": ("What MarsDawn doesn't do", "Know before you buy."),
    },
    "zh-hant": {
        "yours": ("你寫的內容留在你的 Mac 上", "不需要帳號，沒有同步，也沒有雲端。"),
        "pay-once": ("免費試用，買一次就好", "免費試用 14 天，之後 USD 4.99 買一次，沒有訂閱。"),
        "pdf": ("輸出 PDF", "圖表、程式碼上色、經過安排的分頁。"),
        "native": ("為 Mac 而做", "原生視窗、分頁、自動儲存、快速查看。"),
        "limits": ("MarsDawn 做不到的事", "購買前先知道。"),
    },
}
TRAIT_NAV_HEADING = {"en": "What to expect from MarsDawn", "zh-hant": "MarsDawn 是什麼樣的 app"}
FIGURE_LIST_LABEL = {"en": "In this screenshot", "zh-hant": "這張截圖裡"}


# --- Simplified Chinese and Japanese -------------------------------------------
# Each module's build(k) returns the same tables as above, for its one locale, translated from the
# en and zh-hant copy. k carries the shared constants, so a URL, address or command is written once.
# UI labels quoted in them follow the app's own zh-Hans and ja strings.
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True  # no scripts/__pycache__: CI fails on any untracked file after a build
import copy_ja  # noqa: E402
import copy_zh_hans  # noqa: E402

EXTRA_PAGES = {}


def _merge_locale(locale: str, module) -> None:
    k = SimpleNamespace(
        EMAIL=EMAIL, UPDATED=UPDATED, PRIVACY_UPDATED=PRIVACY_UPDATED, BASE_URL=BASE_URL,
        KIT_URL=KIT_URL, BREW_TAP_INSTALL=BREW_TAP_INSTALL, INSTALL=_INSTALL, SKILL_URL=_SKILL_URL,
        APP_UI_LANGUAGES=APP_UI_LANGUAGES[locale], schema_links_from=schema_links_from, xml_escape=xml_escape,
    )
    t = module.build(k)
    assert set(t["ui"]) == set(UI["en"]), f"{locale}: UI keys differ from en"
    UI[locale] = t["ui"]
    STORE_CHIP[locale] = t["store_chip"]
    assert set(t["schema_notes"]) == set(SCHEMA_NOTES["en"]), f"{locale}: schema notes differ from en"
    SCHEMA_NOTES[locale] = t["schema_notes"]
    EXAMPLE_PLAN[locale] = t["example_plan"]
    _PLAN_HTML[locale] = xml_escape(t["example_plan"])
    assert set(t["trait_link"]) == set(TRAIT_ORDER), f"{locale}: trait links differ from TRAIT_ORDER"
    TRAIT_LINK[locale] = t["trait_link"]
    TRAIT_NAV_HEADING[locale] = t["trait_nav_heading"]
    FIGURE_LIST_LABEL[locale] = t["figure_list_label"]
    assert set(t["figures"]) == set(FIGURES), f"{locale}: figures differ"
    for slug, fig in FIGURES.items():
        text = t["figures"][slug]
        fig["alt"][locale] = text["alt"]
        assert len(text["callouts"]) == len(fig["callouts"]), f"{locale}/{slug}: callout count differs"
        for (_, _, _, label), translated in zip(fig["callouts"], text["callouts"]):
            label[locale] = translated
    assert t["pages"] and set(t["pages"]) <= set(PAGE_ORDER), f"{locale}: unknown pages"
    for slug, page in t["pages"].items():
        assert ("intro" in page) == ("intro" in all_pages_en()[slug]), f"{locale}/{slug}: intro shape differs"
        EXTRA_PAGES[(locale, slug)] = page


def all_pages_en() -> dict:
    return {slug: page for (locale, slug), page in _base_pages().items() if locale == "en"}


def trait_nav_html(locale: str, current: str) -> str:
    items = "\n".join(
        f'  <li><a href="{page_path(locale, slug)}">{TRAIT_LINK[locale][slug][0]}</a>'
        f'<span>{TRAIT_LINK[locale][slug][1]}</span></li>'
        for slug in TRAIT_ORDER
        if slug != current
    )
    return f'<nav class="traits" aria-label="{TRAIT_NAV_HEADING[locale]}">\n<h2>{TRAIT_NAV_HEADING[locale]}</h2>\n<ul>\n{items}\n</ul>\n</nav>'


def figure_html(locale: str, slug: str) -> str:
    # The homepage hero shot spans min(76rem, 100vw - 48px); trait shots sit
    # inside 12rem gutters, so about 50rem.
    sizes = ("(min-width: 1264px) 76rem, (min-width: 736px) calc(100vw - 48px), calc(100vw - 32px)"
             if slug == "index" else "(min-width: 1100px) 50rem, calc(100vw - 32px)")
    fig = FIGURES[slug]
    img = fig["image"]
    _, _, width, height = CROPS[img]
    markers = []
    lines = []
    legend = []
    for index, (_, y, side, label) in enumerate(fig["callouts"], start=1):
        cls = f"co-{slug}-{index}"
        edge = " tb" if y < 9 else ""
        markers.append(f'<span class="marker {side}{edge} {cls}" aria-hidden="true">{index}</span>')
        lines.append(f'<span class="leader {side} {cls}" aria-hidden="true"><span>{label[locale]}</span></span>')
        legend.append(f"<li>{label[locale]}</li>")
    figcaption = ""
    if legend:
        figcaption = f"""
  <figcaption>
    <span class="figure-label">{FIGURE_LIST_LABEL[locale]}</span>
    <ol>{''.join(legend)}</ol>
  </figcaption>"""
    return f"""<figure class="shot">
  <div class="shot-frame"><div class="shot-canvas">
    <img src="/assets/screens/{img}-{width}.png" srcset="/assets/screens/{img}-{SMALL_WIDTH}.png {SMALL_WIDTH}w, /assets/screens/{img}-{width}.png {width}w" sizes="{sizes}" width="{width}" height="{height}" alt="{fig['alt'][locale]}">
    {''.join(markers)}
    {''.join(lines)}
  </div></div>{figcaption}
</figure>"""


def figure_markdown(locale: str, slug: str) -> str:
    fig = FIGURES[slug]
    image = fig["image"]
    width = CROPS[image][2]
    src = abs_url(f"/assets/screens/{image}-{width}.png")
    lines = [f"![{fig['alt'][locale]}]({src})"]
    if fig["callouts"]:
        colon = "：" if locale in FULL_WIDTH else ":"
        lines += ["", f"{FIGURE_LIST_LABEL[locale]}{colon}", ""]
        lines += [f"{i}. {label[locale]}" for i, (_, _, _, label) in enumerate(fig["callouts"], start=1)]
    return "\n".join(lines)


def annotations_css() -> str:
    rules = [
        "/* Generated by scripts/build_pages.py: callout positions for the annotated",
        "   screenshots, kept out of inline styles so the CSP stays strict. */",
    ]
    for slug in TRAIT_ORDER:
        image = FIGURES[slug]["image"]
        for index, (x, y, _, _) in enumerate(FIGURES[slug]["callouts"], start=1):
            cx, cy = cropped_position(image, x, y)
            rules.append(f".co-{slug}-{index} {{ --x: {cx}%; --y: {cy}%; }}")
    return "\n".join(rules) + "\n"


def page_markdown(pages: dict, locale: str, slug: str) -> str:
    page = pages[(locale, slug)]
    if "intro" not in page:
        return html_to_markdown(page["body"])
    return "\n\n".join([
        html_to_markdown(page["intro"]).rstrip(),
        figure_markdown(locale, slug),
        html_to_markdown(page["body"]).rstrip(),
    ])

PAGE_ORDER = ["index", "yours", "pay-once", "pdf", "native", "limits", "support", "privacy", "view-markdown-on-mac", "markdown-to-pdf", "vs/macmd-viewer", "cli", "cli/agents", "cli/skill"]
SLUG_TO_UI_KEY = {"index": "home", "support": "support", "privacy": "privacy", "cli": "cli", "cli/agents": "agents",
                  "markdown-to-pdf": "markdown-to-pdf", "view-markdown-on-mac": "view-markdown-on-mac", "cli/skill": "skill",
                  "yours": "yours", "pay-once": "pay-once", "pdf": "pdf", "native": "native", "limits": "limits",
                  "vs/macmd-viewer": "vs-macmd-viewer"}


def _base_pages() -> dict:
    merged = dict(PAGES)
    merged.update(CLI_PAGES)
    merged.update(AGENT_PAGES)
    merged.update(START_PAGES)
    merged.update(SKILL_PAGES)
    merged.update(TRAIT_PAGES)
    return merged


def all_pages() -> dict:
    merged = _base_pages()
    merged.update(EXTRA_PAGES)
    return merged


# A locale can have only some of the pages (zh-Hans and ja start with the privacy policy and support,
# which the App Store listings link to). Nothing may link to a page that doesn't exist: the language
# switch and hreflang list only the locales that have the page, the footer only the locale's own pages,
# and a locale without a home page takes its brand link from HOME_FALLBACK.
HOME_FALLBACK = {"zh-hans": "zh-hant", "ja": "en"}


def has_page(locale: str, slug: str) -> bool:
    return (locale, slug) in all_pages()


def locales_with(slug: str) -> list:
    return [locale for locale in LOCALES if has_page(locale, slug)]


def home_path(locale: str) -> str:
    return LOCALES[locale if has_page(locale, "index") else HOME_FALLBACK[locale]]["root"]


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
# Elements with no closing tag. Pushing one onto the stack would nest the rest of the page inside it.
_VOID_TAGS = {"img", "br"}


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
        if tag not in _VOID_TAGS:
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
        elif tag == "img":
            parts.append(f"![{child.attrs.get('alt', '')}]({child.attrs.get('src', '')})")
        else:
            raise MarkdownConversionError(f"unsupported inline tag <{tag}>")
    return "".join(parts)


def _longest_backtick_run(text: str) -> int:
    return max((len(run) for run in re.findall(r"`+", text)), default=0)


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
    if tag in ("ul", "ol"):
        items = []
        for child in node.children:
            if isinstance(child, str):
                if child.strip():
                    raise MarkdownConversionError(f"unexpected text directly inside <{tag}>")
                continue
            if child.tag != "li":
                raise MarkdownConversionError(f"unsupported child <{child.tag}> of <{tag}>")
            bullet = f"{len(items) + 1}." if tag == "ol" else "-"
            items.append(f"{bullet} " + _render_inline(child.children).strip())
        return "\n".join(items) + "\n\n"
    if tag == "pre":
        text = _pre_text(node)
        fence = "`" * max(3, _longest_backtick_run(text) + 1)
        return f"{fence}\n{text}\n{fence}\n\n"
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
        for other in locales_with(slug)
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{LOCALES[other]["html_lang"]}" href="{abs_url(page_path(other, slug))}">'
        for other in locales_with(slug)
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
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "url": canonical_url,
        }
        jsonld = f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>\n'
    has_intro = "intro" in page
    is_trait_page = slug in TRAIT_ORDER
    extra_css = '<link rel="stylesheet" href="/assets/annotations.css">\n' if is_trait_page else ""
    chip = f'<span class="store-chip">{STORE_CHIP[locale]}</span>\n  ' if is_trait_page else ""
    if slug == "index":
        hero_html = (
            '<section class="hero-scene">\n'
            f"{DAWN_HERO_SVG}\n"
            '<div class="hero-inner">\n'
            f'<div class="hero-copy">\n{page["intro"].strip()}\n</div>\n'
            f'<div class="hero-shot">\n{figure_html(locale, slug)}\n</div>\n'
            "</div>\n"
            "</section>"
        )
        closing_html = (
            '<section class="dawn-close">\n'
            f'<p><strong>{ui["tagline"]}</strong> {ui["footer_store"]}</p>\n'
            "</section>"
        )
        main_html = "\n".join([hero_html, page["body"].strip(), trait_nav_html(locale, ""), closing_html])
    elif has_intro:
        main_html = "\n".join([page["intro"].strip(), figure_html(locale, slug), page["body"].strip(), trait_nav_html(locale, slug)])
    else:
        main_html = page["body"].strip()
    footer_links = "".join(
        f'  <a href="{page_path(locale, target)}">{ui[target]}</a>\n'
        for target in ("support", "privacy", "cli")
        if has_page(locale, target)
    )
    if slug == "index":
        footer_html = f'<footer class="footer footer-home">\n{footer_links}</footer>'
    else:
        footer_html = (
            f'<footer class="footer">\n  <span>{ui["tagline"]}</span>\n{footer_links}'
            f'  <span>{ui["footer_store"]}</span>\n</footer>'
        )
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
{extra_css}{alternates}
{seo}
{jsonld}</head>
<body>
<div class="page">
<header class="masthead">
  <a class="brand" href="{home_path(locale)}">
    <img src="/assets/icon-192.png" alt="" width="40" height="40">
    <strong>MarsDawn</strong>
  </a>
  {chip}<nav class="lang" aria-label="Language">{switch}</nav>
</header>
<main>
{main_html}
</main>
{footer_html}
</div>
</body>
</html>
"""


# robots.txt: exactly these directives (Cloudflare prepends its own managed block).
# AI crawlers allowed by name. robots.txt semantics (RFC 9309): a named group
# replaces `*` for that bot entirely, so `User-agent: *` alone would not cover
# these, and its `Content-Signal` line would not apply to them either. All 7
# go in ONE group (repeated User-agent lines sharing the rules that follow),
# so that group's `Allow: /` and `Content-Signal` both apply to every one of
# them, matching what the `*` group gives everyone else — one place to edit,
# rather than repeating Content-Signal per bot.
AI_CRAWLERS = [
    "GPTBot", "ChatGPT-User", "OAI-SearchBot",
    "ClaudeBot", "Claude-User", "Claude-SearchBot",
    "PerplexityBot",
]

_AI_CRAWLER_USER_AGENTS = "\n".join(f"User-agent: {bot}" for bot in AI_CRAWLERS)

ROBOTS_TXT = f"""# robots.txt for marsdawn.southern-light.dev
User-agent: *
Allow: /
Content-Signal: search=yes, ai-input=yes, ai-train=yes

# One group, seven user agents: a named group replaces `*` for that bot, so
# each of these needs its own explicit Allow and Content-Signal rather than
# relying on the default group above.
{_AI_CRAWLER_USER_AGENTS}
Allow: /
Content-Signal: search=yes, ai-input=yes, ai-train=yes

Sitemap: {BASE_URL}/sitemap.xml
"""

# Stable URL for the machine-readable product facts page (plain Markdown,
# built once from the same constants as the rest of the site). Listed in
# llms.txt and the sitemap so crawlers find it.
PRODUCT_FACTS_PATH = "/product-facts.md"


def build_product_facts(pages: dict) -> str:
    """product-facts.md: what MarsDawn is, requirements, the open-source kit,
    and entity disambiguation, for AI assistants and search crawlers.

    Built from the same constants (KIT_URL, KIT_LICENSE, BREW_TAP_INSTALL,
    BASE_URL) and the same home-page description as the rest of the site, so
    this can't drift from them. The two macOS version numbers below are not
    behind a shared constant with the support and CLI pages' prose (each
    states them in a different sentence shape); they're checked by hand
    against those pages, the same way the README already asks UI labels to
    be checked by hand against the app.
    """
    home_en = pages[("en", "index")]
    return f"""# MarsDawn — Product Facts

Machine-readable facts about MarsDawn, for AI assistants and search crawlers.
Source: {BASE_URL}{PRODUCT_FACTS_PATH}

## What MarsDawn is

{home_en['description']}

## Requirements

- The MarsDawn app: macOS 26 (Tahoe) or later, Apple silicon or Intel.
- The `marsdawn` command-line tool: macOS 15 or later to run; building it from source needs Swift 6.2 (Xcode 26) or later.

## Free and open source, available today

- [mars-dawn-kit]({KIT_URL}) is free and open source, licensed {KIT_LICENSE}.
- The free `marsdawn` command-line tool is built from that kit and distributed separately from the Mac App Store: `{BREW_TAP_INSTALL}`.
- Both the kit and the CLI exist today and can be installed now, independent of the MarsDawn app's own release status.

## Entity disambiguation

MarsDawn **is**:

- a native AppKit Markdown editor for the Mac, with live preview.

MarsDawn is **not**:

- **not Electron.** It is a native AppKit application, not a web page in a bundled browser.
- **not a web app.** It runs locally as a macOS app; there is no server and no browser tab.
- **not read-only.** It is a full Markdown editor: you write and edit the source, not just view rendered output.
- **not a subscription.** It is a free download with a 14-day trial, then a USD 4.99 one-time in-app purchase to unlock it.
- **not cross-platform.** It is macOS only; there is no Windows, Linux, iOS or Android build.
- **not an AI product.** The app itself contains no AI. It is built for reviewing Markdown that an AI agent writes, and does not include an AI model of its own.

## More

- Full docs: {BASE_URL}/llms.txt and {BASE_URL}/llms-full.txt
- CLI reference for agents: {abs_url(md_path("en", "cli/agents"))}
"""


def build_sitemap(pages: dict, extra_urls: list = None) -> str:
    entries = []
    for slug in PAGE_ORDER:
        for locale in LOCALES:
            if (locale, slug) not in pages:
                continue
            loc = xml_escape(abs_url(page_path(locale, slug)))
            alt_links = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{LOCALES[other]["html_lang"]}" href="{xml_escape(abs_url(page_path(other, slug)))}"/>'
                for other in locales_with(slug)
            )
            alt_links += (
                f'\n    <xhtml:link rel="alternate" hreflang="x-default"'
                f' href="{xml_escape(abs_url(page_path("en", slug)))}"/>'
            )
            entries.append(f"  <url>\n    <loc>{loc}</loc>\n{alt_links}\n  </url>")
    for url in extra_urls or []:
        entries.append(f"  <url>\n    <loc>{xml_escape(url)}</loc>\n  </url>")
    body = "\n".join(entries)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def build_twin(pages: dict, locale: str, slug: str) -> str:
    """The page body as Markdown, plus links to the site's other pages.

    The body alone would leave an agent on a twin with no way to the rest of the
    site, because the HTML header and footer links aren't part of it.
    """
    body = page_markdown(pages, locale, slug)
    others = [other for other in PAGE_ORDER if other != slug and (locale, other) in pages]
    lines = [body.rstrip(), "", f"## {UI[locale]['more']}", ""]
    for other in others:
        page = pages[(locale, other)]
        lines.append(f"- [{UI[locale][SLUG_TO_UI_KEY[other]]}]({abs_url(md_path(locale, other))}): {page['description']}")
    for other_locale in locales_with(slug):
        if other_locale == locale:
            continue
        lines.append(f"- [{LOCALES[other_locale]['label']}]({abs_url(md_path(other_locale, slug))}): "
                     f"{pages[(other_locale, slug)]['description']}")
    return "\n".join(lines).rstrip() + "\n"


def build_llms_txt(pages: dict) -> str:
    home_en = pages[("en", "index")]
    lines = ["# MarsDawn", "", f"> {home_en['description']}", ""]
    for locale in LOCALES:
        heading = "Docs" if locale == "en" else LOCALES[locale]["label"]
        lines.append(f"## {heading}")
        for slug in PAGE_ORDER:
            if (locale, slug) not in pages:
                continue
            page = pages[(locale, slug)]
            label = UI[locale][SLUG_TO_UI_KEY[slug]]
            url = abs_url(md_path(locale, slug))
            lines.append(f"- [{label}]({url}): {page['description']}")
        lines.append("")
    lines.append(f"## {UI['en']['using_cli']}")
    lines.append(
        f"- [{UI['en']['agents']}]({abs_url(md_path('en', 'cli/agents'))}): commands, JSON output, "
        "exit codes and requirements, with examples that were run before publishing"
    )
    for kind in ("export", "open", "error", "open_v1"):
        note = SCHEMA_NOTES["en"][kind].replace("<code>", "`").replace("</code>", "`")
        lines.append(f"- [{SCHEMA_FILES[kind]}]({schema_url(kind)}): JSON Schema for the --json result, {note}")
    lines.append("")
    lines.append("## Product facts")
    lines.append(
        f"- [product-facts.md]({BASE_URL}{PRODUCT_FACTS_PATH}): what MarsDawn is, requirements, "
        "and entity disambiguation (not Electron, not a web app, not read-only, not a subscription, "
        "not cross-platform, not an AI product)"
    )
    lines.append("")
    lines.append(
        f"Open source: [mars-dawn-kit]({KIT_URL}) is free and {KIT_LICENSE}, and the free `marsdawn` "
        "command-line tool is built from it."
    )
    lines.append(f"Install: `{BREW_TAP_INSTALL}` (a prebuilt bottle on Apple silicon, "
                 "no Xcode needed; on Intel it builds from source with Xcode 26; macOS 15 or later). "
                 "`export` works without the MarsDawn app; `open` needs it.")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_llms_full(pages: dict) -> str:
    sections = []
    for locale in LOCALES:
        for slug in PAGE_ORDER:
            if (locale, slug) not in pages:
                continue
            page = pages[(locale, slug)]
            label = UI[locale][SLUG_TO_UI_KEY[slug]]
            url = abs_url(page_path(locale, slug))
            body_md = page_markdown(pages, locale, slug)
            sections.append(f"## {label}\n\nSource: {url}\n\n{body_md}")
    return "# MarsDawn — full content\n\n" + "\n---\n\n".join(sections)


for _locale, _module in (("zh-hans", copy_zh_hans), ("ja", copy_ja)):
    _merge_locale(_locale, _module)


def main() -> None:
    pages = all_pages()
    for (locale, slug), page in pages.items():
        folder = SITE / LOCALES[locale]["prefix"] / ("" if slug == "index" else slug)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(render(locale, slug, page), encoding="utf-8")
        print(folder / "index.html")
        (folder / "index.md").write_text(build_twin(pages, locale, slug), encoding="utf-8")
        print(folder / "index.md")

    (SITE / "llms.txt").write_text(build_llms_txt(pages), encoding="utf-8")
    print(SITE / "llms.txt")
    (SITE / "llms-full.txt").write_text(build_llms_full(pages), encoding="utf-8")
    print(SITE / "llms-full.txt")
    (SITE / "assets" / "annotations.css").write_text(annotations_css(), encoding="utf-8")
    print(SITE / "assets" / "annotations.css")
    (SITE / "robots.txt").write_text(ROBOTS_TXT, encoding="utf-8")
    print(SITE / "robots.txt")
    product_facts_path = SITE / PRODUCT_FACTS_PATH.lstrip("/")
    product_facts_path.write_text(build_product_facts(pages), encoding="utf-8")
    print(product_facts_path)
    (SITE / "sitemap.xml").write_text(
        build_sitemap(pages, extra_urls=[BASE_URL + PRODUCT_FACTS_PATH]), encoding="utf-8"
    )
    skill = SITE / "cli" / "skill" / "SKILL.md"
    skill.parent.mkdir(parents=True, exist_ok=True)
    skill.write_text(build_skill_md(), encoding="utf-8")
    print(skill)
    print(SITE / "sitemap.xml")
    schema_dir = SITE / SCHEMA_BASE.strip("/")
    schema_dir.mkdir(parents=True, exist_ok=True)
    for kind, schema in SCHEMAS.items():
        target = schema_dir / SCHEMA_FILES[kind]
        target.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(target)


if __name__ == "__main__":
    main()
