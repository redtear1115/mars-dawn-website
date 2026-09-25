# #110 copy: the marsdawn 0.5.3 changelog entry

Grok's copy for [mars-dawn-website#110](https://github.com/redtear1115/mars-dawn-website/issues/110). It is paste-ready HTML for `/changelog/`, in four locales, to go on PR #47's branch (`1001-go-live`). Each block goes between the `marsdawn 0.5.4` entry and the `marsdawn 0.5.2` entry:

- **en** (`scripts/build_pages.py`, `("en", "changelog")`): replace the `<!-- DRAFT (needs-copy, needs-i18n) … -->` comment and the draft `marsdawn 0.5.3` block under it.
- **zh-Hant** (`scripts/build_pages.py`, `("zh-hant", "changelog")`): replace the `<!-- DRAFT … -->` placeholder comment.
- **zh-Hans** (`scripts/copy_zh_hans.py`, `pages['changelog']`): replace the `<!-- DRAFT … -->` placeholder comment.
- **ja** (`scripts/copy_ja.py`, `pages['changelog']`): replace the `<!-- DRAFT … -->` placeholder comment.

Nothing changes in the 0.5.4 entry or in any version heading. Then rerun `python3 scripts/build_pages.py`.

Facts are from kit tag `0.5.3` (`bd728cf`, 2026-09-25): the README at that tag, and kit PRs #102, #106, #107, #108, #109, #110 and #105. UI terms come from the app's `Localizable.xcstrings` (app `main` at `0e022a5`).

## en

```html
<h2>marsdawn 0.5.3</h2>
<p>25 September 2026. Folder status, full Mermaid errors and smaller fixes.</p>
<ul>
  <li><code>marsdawn open --folder</code> can say what happened to the folder. With an app that reports back, it waits up to <code>--wait</code> seconds (2 by default), and <code>--json</code> gives a status such as <code>attached</code> or <code>needsUser</code>.</li>
  <li>A Mermaid diagram that doesn't parse shows Mermaid's whole error message instead of only its first line, with the line number counted from the top of your document.</li>
  <li>The search for the end of a front-matter block stops after 1,000 lines, so an unclosed block no longer means scanning the rest of a large document.</li>
  <li>An app can give the footnote back-link a translated label for PDF export and printing. The label isn't printed on the page, and <code>marsdawn export</code> keeps the English one.</li>
  <li>The bundled highlight.js is now pinned by version, source and SHA-256, like KaTeX and Mermaid.</li>
</ul>
```

## zh-Hant

```html
<h2>marsdawn 0.5.3</h2>
<p>2026 年 9 月 25 日。資料夾狀態、完整的 Mermaid 錯誤訊息，以及其他小修正。</p>
<ul>
  <li><code>marsdawn open --folder</code> 可以回報資料夾後來怎麼了。搭配會回報狀態的 app，它最多等待 <code>--wait</code> 秒（預設 2 秒），<code>--json</code> 會給出 <code>attached</code>、<code>needsUser</code> 等狀態。</li>
  <li>Mermaid 圖表無法解析時，會顯示 Mermaid 完整的錯誤訊息，不再只有第一行；行號也改成從文件開頭算起。</li>
  <li>尋找 front matter 區塊的結尾時，最多只找 1,000 行；沒有結尾的區塊，不再讓大型文件每次都被掃描到最後。</li>
  <li>app 可以為 PDF 輸出與列印，替註腳的返回連結提供翻譯後的標籤。這個標籤不會印在頁面上，<code>marsdawn export</code> 仍使用英文。</li>
  <li>內建的 highlight.js 現在和 KaTeX、Mermaid 一樣，記錄版本、來源與 SHA-256。</li>
</ul>
```

## zh-Hans

```html
<h2>marsdawn 0.5.3</h2>
<p>2026 年 9 月 25 日。文件夹状态、完整的 Mermaid 错误信息，以及其他小修复。</p>
<ul>
  <li><code>marsdawn open --folder</code> 可以报告文件夹最后的状态。配合会回报状态的 app，它最多等待 <code>--wait</code> 秒（默认 2 秒），<code>--json</code> 会给出 <code>attached</code>、<code>needsUser</code> 等状态。</li>
  <li>Mermaid 图表无法解析时，会显示 Mermaid 完整的错误信息，不再只有第一行；行号也改为从文稿开头算起。</li>
  <li>查找 front matter 区块的结尾时，最多只查找 1,000 行；未闭合的区块，不再让大型文稿每次都被扫描到最后。</li>
  <li>app 可以在导出 PDF 和打印时，为脚注的返回链接提供翻译后的标签。这个标签不会打印在页面上，<code>marsdawn export</code> 仍使用英文。</li>
  <li>内置的 highlight.js 现在和 KaTeX、Mermaid 一样，记录版本、来源与 SHA-256。</li>
</ul>
```

## ja

```html
<h2>marsdawn 0.5.3</h2>
<p>2026年9月25日。フォルダの状態、Mermaid エラーの全文、そのほかの修正。</p>
<ul>
  <li><code>marsdawn open --folder</code> が、フォルダがどうなったかを返せるようになりました。状態を返すアプリが相手なら、<code>--wait</code> の秒数（デフォルトは 2 秒）まで応答を待ち、<code>--json</code> に <code>attached</code> や <code>needsUser</code> などの状態が入ります。</li>
  <li>Mermaid の図を解析できないとき、最初の行だけでなく Mermaid のエラーメッセージ全文を表示します。行番号もファイルの先頭から数えた値になりました。</li>
  <li>フロントマターの終わりを探すのは 1,000 行までになりました。閉じていないブロックがあっても、大きなファイルを毎回最後まで調べることはありません。</li>
  <li>脚注の戻りリンクのラベルを、アプリが PDF の書き出しとプリント用に翻訳して渡せるようになりました。このラベルはページには印刷されず、<code>marsdawn export</code> では英語のままです。</li>
  <li>同梱の highlight.js を、KaTeX や Mermaid と同じく、バージョン、入手元、SHA-256 で記録するようになりました。</li>
</ul>
```

---

Nothing below this rule is page copy.

## Optional sixth line (held back)

The owner's list has a sixth item, kit #110 (#91): restoring the thread's I/O policy when the previous one can't be read. It is left out of the page because kit PR #110 itself says the failure "cannot be triggered on a real system" and "cannot be triggered from the app", so no reader can meet the bug or check the fix. If the owner wants it anyway, append this as the last `<li>` in each locale:

```html
<li>A safeguard for files kept only in iCloud: if the previous download setting can't be read, it's reset to the default afterwards, so later reads aren't left unable to download files.</li>
```

```html
<li>讀取只存在 iCloud 上、沒有下載到本機的檔案時，多了一層保護：如果讀不到先前的下載設定，事後會恢復成預設值，之後的讀取不會因此無法下載檔案。</li>
```

```html
<li>读取只存在 iCloud 中、未下载到本地的文件时，多了一层保护：如果读不到之前的下载设置，之后会恢复为默认值，后续读取不会因此无法下载文件。</li>
```

```html
<li>iCloud 上にだけあり、この Mac にダウンロードされていないファイルを読むときの安全策です。以前のダウンロード設定を読み取れなかった場合も、読み込み後にデフォルトに戻し、以降の読み込みでファイルをダウンロードできなくなることはありません。</li>
```

## English changes, draft → final

| Line | Draft | Final | Why |
|---|---|---|---|
| Summary | Folder status, clearer diagram errors, and export fixes. | Folder status, full Mermaid errors and smaller fixes. | Only the footnote label touches export; "export fixes" oversold it. No Oxford comma, like 0.5.2's "Footnotes, contrast and folders." |
| open --folder | …can report back what happened to the folder, with `--wait`: `attached`, `needsUser`, and more, from an app that opts in. | …can say what happened to the folder. With an app that reports back, it waits up to `--wait` seconds (2 by default), and `--json` gives a status… | `--wait` isn't needed to get a status: it defaults to 2 (kit README at 0.5.3, 0–30). The status is a field of the `--json` result. "Opts in" is now said plainly. |
| Mermaid | …shows the full message, mapped to the document's line, instead of only its first line. | …shows Mermaid's whole error message instead of only its first line, with the line number counted from the top of your document. | "Mapped to the document's line" is jargon. What changed (kit #106) is that Mermaid's own "line N" is rewritten from diagram-relative to document-relative. |
| Front matter | Scanning for an unclosed front-matter block stops after 1000 lines, instead of scanning the rest of a large document on every edit. | The search for the end of a front-matter block stops after 1,000 lines, so an unclosed block no longer means scanning… | "On every edit" describes the app's highlighter, not the CLI (kit #107: "Not wired into the app" yet). 1,000 gets a thousands separator. |
| Footnote label | Exported PDFs can carry a localized label for the footnote back-link. | An app can give the footnote back-link a translated label for PDF export and printing. The label isn't printed on the page, and `marsdawn export` keeps the English one. | It is a parameter for callers (`DocumentExporter`, kit #108). The CLI has no option for it, and the label is the link's `aria-label`, not visible text. The draft read as if every exported PDF changed. |
| highlight.js | The vendored highlight.js is now recorded by version, source and SHA-256, the way KaTeX and Mermaid already are. | The bundled highlight.js is now pinned by version, source and SHA-256, like KaTeX and Mermaid. | "Vendored" is contributor jargon; shorter. |
| iCloud | Reading a file iCloud has offloaded restores the thread's file-materialization policy correctly, even when the previous one couldn't be read. | (held back, see above) | Not reachable on a real system (kit PR #110). "Thread's file-materialization policy" isn't reader language. |

## Terms

- UI terms follow the app's `Localizable.xcstrings`: 資料夾／文件夹／フォルダ (`folder`), 預覽／预览／プレビュー, 輸出／导出／書き出し (`Export as PDF…`), 列印／打印／プリント (`Print…`), 文件／文稿 (`Document`).
- The zh-Hans entry says 导出, as the app does (`导出为 PDF…`). The zh-Hans 0.5.2 and 0.5.1 entries say 输出, so the page will mix the two until they're aligned.
- The ja entry says プリント, as the app does (`プリント…`), and ファイル rather than 書類 or 文書, to stay out of the site's 文書 vs the app's 書類 split.
- zh punctuation is full-width; code, flags, status values and version numbers stay ASCII.

Co-authored-by: Grok <grok@southern-light.dev>
