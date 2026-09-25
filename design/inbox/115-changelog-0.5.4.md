# marsdawn 0.5.4 changelog entry, four languages (#115)

Where it goes: a new entry between `marsdawn 0.6.0` and `marsdawn 0.5.3` on `/changelog/`, in all four languages. The 0.6.0 and 0.5.3 entries and every heading stay as they are.

| Language | File | Insert right before |
|---|---|---|
| en | `scripts/build_pages.py` | the English `<h2>marsdawn 0.5.3</h2>` (line 2052 on `1001-go-live` e74db26) |
| zh-Hant | `scripts/build_pages.py` | the zh-Hant `<h2>marsdawn 0.5.3</h2>` (line 2099) |
| zh-Hans | `scripts/copy_zh_hans.py` | `<h2>marsdawn 0.5.3</h2>` (line 901) |
| ja | `scripts/copy_ja.py` | `<h2>marsdawn 0.5.3</h2>` (line 909) |

Then `python3 scripts/build_pages.py` regenerates `public/**/changelog/` and `llms-full.txt`.

Sources (kit `redtear1115/mars-dawn-kit`):

- Sequence-diagram labels: #112 / PR #116, merged
- 50-diagram export: #113 / PR #117, merged
- `diagramErrorDetails`: #114 / PR #118, merged
- `skill --install`: #120 / PR #121. PR #121 is still open (head 711248b), and the owner has put it in 0.5.4.

All of these are listed under the kit milestone "0.5.4 before launch".

The date is a placeholder, set to the milestone's due date (30 September). Change it to the day 0.5.4 is actually tagged.

Terms follow the app and Apple:

- zh-Hans: 导出, 文稿
- zh-Hant: 輸出, 文件
- ja: 書き出し, ファイル

## en

```html
<h2>marsdawn 0.5.4</h2>
<p>30 September 2026. Mermaid fixes, diagram error lines and installing the skill.</p>
<ul>
  <li>In a sequence diagram, a message label that crosses other participants' lifelines stays readable, in the preview and in exported PDFs.</li>
  <li><code>marsdawn export</code> copes with documents full of Mermaid diagrams. One with 50 diagrams, which used to fail with exit 5, now exports.</li>
  <li><code>marsdawn export --json</code> adds <code>diagramErrorDetails</code>, with line numbers for each diagram error: where the diagram starts in your document and, when Mermaid names one, the line of the error itself.</li>
  <li><code>marsdawn skill --install</code> installs the agent skill for Claude Code at <code>~/.claude/skills/marsdawn/SKILL.md</code>, or in another folder with <code>--dir</code>. It leaves an identical file alone and replaces a different one only with <code>--force</code>. Otherwise it exits 64 (<code>skill_differs</code>) and changes nothing.</li>
</ul>
```

## zh-Hant

```html
<h2>marsdawn 0.5.4</h2>
<p>2026 年 9 月 30 日。Mermaid 修正、圖表錯誤的行號，以及安裝 skill。</p>
<ul>
  <li>循序圖中，訊息標籤跨過其他參與者的生命線時，文字仍清楚可讀；預覽和輸出的 PDF 都一樣。</li>
  <li><code>marsdawn export</code> 能處理含有大量 Mermaid 圖表的文件。一份有 50 張圖表、原本會以代碼 5 結束的文件，現在可以順利輸出。</li>
  <li><code>marsdawn export --json</code> 新增 <code>diagramErrorDetails</code>，用行號標出每個圖表錯誤：圖表在文件中從第幾行開始；Mermaid 指出行號時，也列出錯誤本身所在的行。</li>
  <li><code>marsdawn skill --install</code> 會把 agent skill 安裝到 <code>~/.claude/skills/marsdawn/SKILL.md</code>，供 Claude Code 使用；加上 <code>--dir</code> 可以改裝到其他資料夾。已有相同的檔案時不會動它；內容不同時，只有加上 <code>--force</code> 才會取代，否則以代碼 64（<code>skill_differs</code>）結束，不做任何更動。</li>
</ul>
```

## zh-Hans

```html
<h2>marsdawn 0.5.4</h2>
<p>2026 年 9 月 30 日。Mermaid 修复、图表错误的行号，以及安装 skill。</p>
<ul>
  <li>时序图中，消息标签跨过其他参与者的生命线时，文字仍清晰可读；预览和导出的 PDF 都是如此。</li>
  <li><code>marsdawn export</code> 能处理包含大量 Mermaid 图表的文稿。一份有 50 张图表、以前会以代码 5 结束的文稿，现在可以顺利导出。</li>
  <li><code>marsdawn export --json</code> 新增 <code>diagramErrorDetails</code>，用行号标出每个图表错误：图表在文稿中从第几行开始；Mermaid 指出行号时，也给出错误本身所在的行。</li>
  <li><code>marsdawn skill --install</code> 会把 agent skill 安装到 <code>~/.claude/skills/marsdawn/SKILL.md</code>，供 Claude Code 使用；加上 <code>--dir</code> 可以改装到其他文件夹。已有相同的文件时不会改动它；内容不同时，只有加上 <code>--force</code> 才会替换，否则以代码 64（<code>skill_differs</code>）结束，不做任何改动。</li>
</ul>
```

## ja

```html
<h2>marsdawn 0.5.4</h2>
<p>2026年9月30日。Mermaid の修正、図のエラーの行番号、スキルのインストール。</p>
<ul>
  <li>シーケンス図で、メッセージのラベルがほかの参加者のライフラインをまたいでも、文字が読みやすいままです。プレビューでも、書き出した PDF でも同じです。</li>
  <li><code>marsdawn export</code> が、Mermaid の図をたくさん含むファイルを書き出せるようになりました。図が 50 個あり、これまでコード 5 で終了していたファイルも書き出せます。</li>
  <li><code>marsdawn export --json</code> に <code>diagramErrorDetails</code> が加わりました。図のエラーごとに、その図がファイルの何行目から始まるかと、Mermaid が行を示している場合はエラーそのものの行を、行番号で返します。</li>
  <li><code>marsdawn skill --install</code> は、Claude Code 用のエージェントスキルを <code>~/.claude/skills/marsdawn/SKILL.md</code> にインストールします。<code>--dir</code> でほかのフォルダも指定できます。同じ内容のファイルがあればそのままにし、内容が違うファイルは <code>--force</code> を付けたときだけ置き換えます。付けないときはコード 64（<code>skill_differs</code>）で終了し、何も変更しません。</li>
</ul>
```
