# 和你的代理一起做主题

给制作 MarsDawn 预览主题的 AI 代理的参考。代理写出一个 `theme.json`，用 `marsdawn` 命令行工具检查并渲染，再把链接交给你。你在[打造一个主题](/zh-hans/themes/new/)页面用眼睛调整，然后投稿。下面的字段表直接读自 kit 的源代码，并有检查确保两者一致。

**写出一个 `theme.json`，反复运行 `marsdawn theme validate theme.json --require-complete --json` 直到退出代码为 0，用 `marsdawn theme preview` 分别渲染浅色与深色，再把链接交给用户。**主题只有参数，不含任何 CSS。

## 主题是什么

- **颜色**，浅色与深色各一组：基本色板，以及可选的语法与图表颜色。每个颜色都是 `#RRGGBB`。
- **字体设计**：`sans`、`serif` 或 `rounded`。
- **一组封闭的样式选项**：数字落在固定范围内，选择来自固定列表。样式选项里的颜色一律是像 `accent` 这样的色板角色，不能是颜色字面值。
- **显示字符串**：名称与摘要，以及可选的作者与许可证。

不在下面表格里的键是错误，同一个键写两次也是。文件最大 16,384 字节。

## 检查与渲染

在放有 `theme.json` 的文件夹里运行这些命令。需要 `marsdawn` 工具：见[给 AI 代理的 marsdawn 参考](/zh-hans/cli/agents/)。

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- 退出代码：0 表示有效，1 表示无效并列出规则 id，2 表示找不到文件，64 表示用法错误。`preview` 另外有 4（PNG 已存在，传入 `--force` 或换个文件名）和 5（渲染失败）。
- 加上 `--json` 时，无效的主题会把问题列在 `issues` 下，每一项都有 `rule` id、`path` 和 `message`。修正后再运行一次。
- `--require-complete` 是要发布的主题用的检查：它还要求两组色板都有 `syntax` 与 `diagram` 颜色。
- `css` 打印预览使用的 CSS，`preview` 把范例文档渲染成 PNG。两者都会先验证，所以无效的主题什么都不会渲染。
- 交出主题之前，先看过浅色与深色两张 PNG。

## 从内置主题开始

复制四个内置主题之一再修改。每一个都是完整且有效的文件：

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): 默认主题，也是下面的范例
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): 较素雅、像文档的色板
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): 较冷调、较现代的色板
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): 较明亮、对比较高的色板

### 范例：Dawn

这是 `dawn.json`，一个字节都没改。它唯一的样式选项是 `hr` 的一条细的强调色分隔线。

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

## 字段

下面每个对象都用同样的方式读取。`required` 表示这个键必须存在，没有列出的键都是错误。

类型：`string`、`integer`、`number`、`boolean`、`map`（语言标签对应文字）、`enum`（列出的值之一）、`role`（色板角色）和 `object`（连到它的表格）。类型后面的 `[]` 表示列表。

### `theme.json`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | 固定是 `1`。 |
| `id` | `string` | `required` | 1 到 32 个字符：小写字母与数字，以单一连字符连接成段，例如 `calm-green`。 |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`，例如 `1.0.0`。 |
| `name` | `map` | `required` | 语言标签对应文字。`en` 必填，其他键是像 `zh-Hant` 的语言标签。每段文字最多 48 个字符，不可含链接或换行。 |
| `summary` | `map` | `required` | 和 `name` 的形式相同，每段文字最多 120 个字符。 |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — 一个或两个，不可重复。它们决定主题必须达到多高的对比。 |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | SPDX 标识符，例如 `Apache-2.0`。投稿的主题以 Apache-2.0 发布。 |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `name` | `string` | `required` | 最多 64 个字符，不可含链接。 |
| `github` | `string` | `optional` | GitHub 账号。投稿时请填投稿者自己的账号。 |

### `light, dark`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `background` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `surface` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `text` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `muted` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `border` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `heading` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `accent` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `link` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `quote` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `syntax` | `object` | `optional` （发布时必填，用 `--require-complete` 检查） | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` （发布时必填，用 `--require-complete` 检查） | [`diagram`](#t-diagram-colors) |

### `syntax`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `string` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `comment` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `number` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `function` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `type` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |

### `diagram`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `node` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `nodeBorder` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `text` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `line` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `secondary` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `tertiary` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |
| `note` | `string` | `required` | `#` 加六个十六进制数字，例如 `#1C1C1C`。 |

### `style`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [范围](#t-numbers) |
| `lineHeight` | `number` | `optional` | [范围](#t-numbers) |
| `headingWeight` | `number` | `optional` | [范围](#t-numbers) |
| `radius` | `number` | `optional` | [范围](#t-numbers) |
| `maxWidth` | `number` | `optional` | [范围](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [色板角色](#roles) |
| `inlineCode` | `role` | `optional` | [色板角色](#roles) — 只能是 `text` 或语法角色：`keyword`、`string`、`comment`、`number`、`function` 或 `type`。 |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `size` | `number` | `optional` | [范围](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [范围](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [范围](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| 字段 | 类型 | 必填与否 | 值与备注 |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### 带 type 的选项

这些样式选项是带有 `type` 的对象。每个 `type` 只接受为它列出的字段，其他都不行。

| 选项 | type | 字段 | 必填与否 | 类型 |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [范围](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [范围](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` 两个或三个角色。 |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### 色板角色

色板角色是下列名称之一：

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### 数字

数字会先对齐到最接近的间隔倍数，再检查是否落在最小值与最大值之间，否则规则是 `number.range`。

| 字段 | 最小值 | 最大值 | 间隔 |
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

## 还会检查什么

- **对比。**预览画出的每一组颜色配对，例如 `background` 上的 `text`，文字要达到 4.5:1，线条与其他非文字要达到 3:1。你列出的场景会把部分颜色提高到 4.5:1。消息会指出是哪一组配对、它的比值和需要的比值。
- **字符串。**名称、摘要或作者名称若是空的、太长，或含有链接、控制字符、不可见或双向格式字符，都会被拒绝。
- **规则 id。**每个问题都带一个，例如 `contrast.pair`、`color.hex`、`number.range`、`id.pattern`、`schema.unknownKey` 或 `palette.incomplete`。按 id 与 `path` 的说明修正文件。

## 用链接交给人

[打造一个主题](/zh-hans/themes/new/)页面可以从链接打开主题，让人用眼睛调整。链接是该页的网址，接着 `#theme=`，再接文件字节的 base64url（不含补位）。文件最大 16,384 字节。下面这一行命令在 macOS 与 Linux 的 zsh 和 bash 都能生成链接：

```
printf 'https://marsdawn.southern-light.dev/zh-hans/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

主题跟在 `#` 后面，浏览器不会把它发送给网站，网站也不会把它发送到任何地方。链接确实会留在你的 shell 历史与浏览器历史里，你贴给谁，谁就能读到这个主题。

## 投稿

代理准备文件与链接，由人来投稿。两条路都会要求 Developer Certificate of Origin 与 Apache-2.0 许可声明，这个声明由人本人做出：代理不会替他勾选方框或签署。

- **Issue。**人打开链接，在“打造一个主题”页面点按 **Submit**，或是打开 [issue 表单](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml)，把 JSON 贴进 *Theme*。接着有工作流检查主题并回复。
- **Pull request。**只改 `themes/<id>/theme.json`，把 `author.github` 设为 pull request 作者的账号，每个 commit 都用 `git commit -s` 签署。规则在 [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md)。

投稿主题的作者名称、名称、摘要与 GitHub 账号会永久公开，所以请把 `author.name` 设成人愿意公开的名字。

## 已发布的主题

想看已发布的主题长什么样子，可以逛逛[主题图库](/zh-hans/themes/gallery/)。

## 其他页面

- [MarsDawn](https://marsdawn.southern-light.dev/zh-hans/index.md): 读懂、检查代理写的 Markdown 的 Mac 原生 app：分栏实时预览、Mermaid、KaTeX、快速查看、PDF 导出。可免费试用，之后一次 USD 4.99。
- [功能一览](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [你写的内容留在你的 Mac 上](https://marsdawn.southern-light.dev/zh-hans/yours/index.md): MarsDawn 不需要账户，没有同步，也没有云端。你的 Markdown 文稿留在你的 Mac 上，就在你选的文件和文件夹里。
- [免费试用，买一次就好](https://marsdawn.southern-light.dev/zh-hans/pay-once/index.md): MarsDawn 免费下载。先免费试用 14 天，之后花 USD 4.99 解锁一次就好。没有订阅，也不需要账户。
- [导出 PDF](https://marsdawn.southern-light.dev/zh-hans/pdf/index.md): 在 Mac 上把 Markdown 导出成 PDF 或打印，Mermaid 图表和代码高亮都会保留；分页会尽量不切开短的代码，超过一页的会接到下一页。
- [为 Mac 而做](https://marsdawn.southern-light.dev/zh-hans/native/index.md): 真正的 Mac app：原生窗口与标签页、自动保存、版本记录、在访达用快速查看预览 Markdown，文本编辑器的操作和 Mac 上其他 app 一致。
- [MarsDawn 做不到的事](https://marsdawn.southern-light.dev/zh-hans/limits/index.md): 没有同步、没有 iPhone 或 iPad 版、没有插件、不需要账户。内置四种主题，主题图库还有更多。购买前先知道。
- [支持](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [隐私政策](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [Mac 上怎么打开 md 文件](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [在 Mac 上预览 Mermaid](https://marsdawn.southern-light.dev/zh-hans/mermaid-preview-mac/index.md): 在 Mac 上预览 Mermaid 图表：源代码旁边实时画出来，快速查看和导出 PDF 也看得到。图表写错时，会显示错误信息和出错的那一行。
- [Markdown 快速查看](https://marsdawn.southern-light.dev/zh-hans/quicklook/index.md): MarsDawn 的快速查看让你在访达按空格键就能看到排版后的 Markdown，Mermaid 图表、KaTeX 数学公式和代码高亮都在。试用期结束后，快速查看照常可用。
- [Markdown 转 PDF](https://marsdawn.southern-light.dev/zh-hans/markdown-to-pdf/index.md): 免费的 Markdown 转 PDF 工具：在 Mac 上用 marsdawn 命令行，一个命令就把 Markdown 转成 PDF，表格、数学公式、Mermaid 图表和代码高亮都在。
- [MarsDawn 对比：VS Code 预览、Obsidian、QLMarkdown、LynxOffice](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [MacMD Viewer 对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [命令行工具](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM 代理把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [给 AI 代理的 marsdawn 参考](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI 代理与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [给代理的 skill](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的代理把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [MCP 服务器](https://marsdawn.southern-light.dev/zh-hans/cli/mcp/index.md): marsdawn 没有自己的 AI 模型，是哪个代理写出 Markdown 都无所谓。可以从 CLI、skill 文件，或 marsdawn-mcp 这个 MCP 服务器调用，三者最后都运行同一个 export。
- [节省 token 的审阅方式](https://marsdawn.southern-light.dev/zh-hans/token-efficient-review/index.md): 人在 MarsDawn 里读排版后的页面，不会被读回代理的 context。工具调用本身返回的也只是精简的 JSON，不是排版内容，调用本身就很便宜。
- [在别处看 Markdown，对比 MarsDawn](https://marsdawn.southern-light.dev/zh-hans/vs/markdown-preview-tools/index.md): MarsDawn 对比在 VS Code 内置预览、浏览器扩展，或 Claude Desktop 文件预览里看 Markdown：各自能排版出什么，打开一个文件要花多少功夫。
- [预览主题与 PDF 导出](https://marsdawn.southern-light.dev/zh-hans/themes/index.md): 四种主题，各有浅色与深色，一套导出对应你正在看的主题。在浏览器里打造自己的主题，也可以逛逛社区主题图库。
- [打造一个主题](https://marsdawn.southern-light.dev/zh-hans/themes/new/index.md): 挑选颜色和几个样式选项，实时看它们套用在范例文档上，再把主题送出成一个 GitHub issue。不用安装，也不用 git。
- [主题图库](https://marsdawn.southern-light.dev/zh-hans/themes/gallery/index.md): 浏览社区投稿的 MarsDawn 预览主题，按场景筛选，也可以举报有问题的主题。在浏览器里打造一个自己的主题，不用安装，也不用 git。
- [分享导出的 PDF](https://marsdawn.southern-light.dev/zh-hans/sharing-exported-pdfs/index.md): 把代理写的 Markdown 导出成 PDF，交给不写 Markdown、也不会安装任何东西的同事。不用懂语法，不用装 app，也不需要账号就能打开。
- [为什么 AI 写的东西还是需要人读过](https://marsdawn.southern-light.dev/zh-hans/reviewing-ai-output/index.md): AI 写的 Markdown 还是得由人来理解，不能因为读起来通顺就直接相信。MarsDawn 把排版后的页面和源代码并排，也把 Mermaid 图表与 KaTeX 数学式画出来，让结构一眼就看得懂。
- [读懂代理交回来的 Markdown](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI 代理把工作成果交成 Markdown：计划、规格、进度报告。做代理的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [代理的透明](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造代理的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [审代理计划](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): 代理交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [代理设计模式](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种代理设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [更新记录](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): 免费的 marsdawn 命令行工具改了什么。
- [编者的阅读笔记](https://marsdawn.southern-light.dev/zh-hans/reading-notes/index.md): 六篇短笔记，谈打造 AI 代理的人实际主张了什么——Anthropic、Chip Huyen、Lilian Weng、Harrison Chase、LangChain 与 Andrew Ng——以及这些主张对“要读代理交回来的东西”的人分别意味着什么。
- [阅读笔记：Anthropic](https://marsdawn.southern-light.dev/zh-hans/reading-notes/anthropic-building-effective-agents/index.md): Anthropic 在 2024 年 12 月发表的指南把 workflow 和代理分开来看，并描述了五种 workflow 模式，其中一种让另一次 LLM 调用来审查。这对落进你文件夹的东西来说，意味着什么。
- [阅读笔记：Chip Huyen](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把代理的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [阅读笔记：Lilian Weng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng 2023 年被广泛引用的整理，把 LLM 代理描述成大脑加上规划、记忆、工具使用。每个部件通常会留给你读什么，以及她点名的一个限制：计划遇到意外不太会调整。
- [阅读笔记：Harrison Chase](https://marsdawn.southern-light.dev/zh-hans/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase 2024 年对代理的定义，以及他自己的 agentic 光谱；他主张系统愈往自主那端走，就愈需要可观测性——从读那份文件的人的角度重新看一遍。
- [阅读笔记：LangChain（Jess Ou）](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测代理的流程。这套流程哪里还留给人，哪里不留。
- [阅读笔记：Andrew Ng](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [模板](https://marsdawn.southern-light.dev/zh-hans/templates/index.md): 给代理写、你来读的文档用的 Markdown 模板：规格文档、流程图和会议记录，每份都附一段给代理的提示词。
- [规格文档模板](https://marsdawn.southern-light.dev/zh-hans/templates/spec/index.md): Markdown 规格文档模板，包含需求、Mermaid 流程图和验收标准。代理来填，你在 MarsDawn 里审阅。
- [流程图模板](https://marsdawn.southern-light.dev/zh-hans/templates/flowchart/index.md): Markdown 的 Mermaid 流程图模板，图的下方把步骤写出来。在 Mac 上预览，也能导出成 PDF。
- [会议记录模板](https://marsdawn.southern-light.dev/zh-hans/templates/meeting-notes/index.md): Markdown 会议记录模板，列出决议和行动项，每项都有负责人。代理来写，你在 MarsDawn 里确认。
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
