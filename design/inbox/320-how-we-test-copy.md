# #320 How we test MarsDawn: en and zh-Hant draft

Issue: https://github.com/redtear1115/mars-dawn-website/issues/320
Outline: the issue's latest comment (Una's review, accepted as is), plus Ray's later decisions relayed by Paula (S11, S14).
Status: **proposal**. It goes live only after Ray approves.

## How to read this file

- The bodies below are HTML fragments in the same shape as the other evergreen articles in `scripts/build_pages.py` (`section.intro` → `div.summary` → `h2` sections → Next → Sources).
- **Every number has a source in an HTML comment** (`<!-- src: ... -->`), as #320's acceptance requires.
- **Placeholders**: `{{TBD:...}}`. kit #242's are filled in (merged as 85fe880, PR CI run 40285279080). One is left: the self-hosted MacBook Air run, which comes from kit #240. Don't publish while any are left: `grep -n 'TBD' design/inbox/320-how-we-test-copy.md`.
- Suggested slug: `/how-we-test/` (zh-Hant `/zh-hant/how-we-test/`). It needs to be added to `article_dates.py`'s `ARTICLE_SLUGS` and to the footer `ui` dict. Footer labels are at the end of this file.
- The app repo is private, so app facts are described in the text but not linked. Kit facts link to the public kit repo.

## Facts and sources

| # | Fact | Source |
|---|---|---|
| S1 | The test failed on the MacBook Air: 0.1634 / 0.1648 / 0.1796, limit 0.16. It passed on the Mac mini. Same commit, macOS 26.6.2, Xcode 27.1. | kit #241 body; CI run 40271990387 |
| S2 | The pure-colour probe: sRGB (0.784, 0.278, 0.106) reads back as (0.822, 0.335, 0.179) on the mini and (0.782, 0.395, 0.221) on the Air. | kit #241 body |
| S3 | Independent verification of the fix: `best` 0.0 on both machines. The old path on the mini was off by up to 0.128. With the expected colours set to #0000FF, all 5 callouts fail. Note (#C8471B) and Caution (#B03C0C) are about 0.119 apart. | kit PR #242, comment of 2026-10-26 07:39 UTC |
| S4 | A full run on hosted macOS 15: debug about 32 min plus release about 25 min (run 40196953693). Moving macOS 26 to self-hosted MacBook Airs is expected to cut a normal PR from about 60 min to about 15–20. | kit PR #240 body (**not merged**; the 15–20 min figure is an estimate and is not used in the text) |
| S5 | The timeout went from 30 to 45, then 50, then 70 minutes. macos-15 hit the 50-minute limit twice in the release pass with every test passing (run 39231688388). | kit `.github/workflows/ci.yml` comments, main 8e93930, lines 27–34 |
| S6 | Kit CI matrix: macos-15 (the floor) and macos-26 (what the app ships on), debug and release passes. The PDF corpus runs in its own process. A release suite name that matches no test fails the job. | kit `ci.yml` lines 21–26, 85–129 |
| S7 | App CI: one self-hosted runner, `CODE_SIGNING_ALLOWED=NO`. python 3.9's unittest exits 0 having found no tests, so the job checks that the count is above 0, and guards.sh's summary must read "N passed, 0 failed" with N > 0. | app `.github/workflows/ci.yml` lines 78–108 (private) |
| S8 | That guards.sh check came out of an independent verification of #335 (finding P3). | app #341 (private) |
| S9 | `tools/test.sh --all`: signed and unsigned, each with the paywall off and on, so 4 combinations, run locally on a Mac and a MacBook Air (not in CI). **These are not debug/release × macOS 15/26; that matrix is the kit's CI (S6).** | app `tools/test.sh` lines 9, 24–26; #320 owner comment |
| S10 | kit #242 merged as 85fe880. Its PR CI run is all green. | https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080 |
| S11 | Vibe coding framing: Ray's decision, relayed by Paula on 2026-10-26: vibe coding isn't bad, but software depends on long-term maintenance and security, and people should be choosy about the software they pick. No names of people or products. | #320 / Ray |
| S12 | Red controls: the app's CI expects exactly 11. Each is a copy of the local cleanup script (`tools/cleanup-local.sh`) with one safety guard cut out, and the test suite must FAIL against every one; if a copy passes, CI fails. | app `ci.yml` (`expected 11 red controls caught`); `tools/test-cleanup-local.sh` lines 9–13, 685–713 (private) |
| S13 | PDF goldens: sample documents are exported and each page's text is compared with a recorded copy, per OS build (the `pdf-goldens` CI job). The corpus guards against export silently losing content, the page count changing, and export drifting from the preview. | kit `Tests/MarsDawnExportTests/PDFCorpusTests.swift` lines 10–13, 126–175; `record-pdf-goldens.yml` |
| S14 | Ray's decision, relayed by Paula on 2026-10-26: add back "deliberately break a test to check it catches the error" as a recommended habit, and lead into 「測試是一層一層的網子，有很多種目的，這種紅綠測試的意涵」. | #320 / Ray |
| S15 | Scenario review: UX copy and flows go through a scenario review (`needs-ux` → `replied-ux`) before copy and build; #320 itself went through one. | website #320 labels and comment of 2026-10-26 08:31 UTC |
| S16 | Large inputs. 2 MB of dense Markdown renders within 1.5 s; 5 MB (about a million nodes) falls back to plain source within 1.0 s (release budgets; debug allows 10×). The default byte cap is 16 MiB: one byte over is shown as source, unparsed. About 3 MB of one-line blocks (`- a`, `# a`; ~786,000 lines) is refused by the pre-scan's early stop and falls back as too complex (no timing assertion). There is **no** test aimed at line breaks as such; this is the closest. | kit main 85fe880: `Tests/MarsDawnKitTests/MarkdownParsingTests.swift` lines 375–394 (`largeDocuments`), 396–417; `Tests/MarsDawnKitTests/ByteCapTests.swift` lines 5–7, 73, 103; `Tests/MarsDawnKitTests/NodeBudgetTests.swift` line 218 (`realSizeBlockHeavyDocumentsStopEarly`) |
| S17 | Unclosed markers. 1 MiB of `:::` callout openers with no closers, and 65,536 openers then closers, must each render in under 2× the time of 1 MiB of plain text (+0.05 s). Callout nesting caps at 8. Doubling unmatched `<details>` openings may at most 2.5× the time (release). | kit `Tests/MarsDawnKitTests/CalloutSecurityTests.swift` lines 125–146, 156; `Tests/MarsDawnKitTests/DetailsGroupingCostTests.swift` lines 74–84 |
| S18 | Math (KaTeX in the preview). A bad expression shows an error instead of throwing; over 10,000 characters stays as source; at most 1,000 expressions per update; hostile TeX never becomes markup; `trust: false` gives no link or image. | kit `Tests/MarsDawnKitTests/PreviewMathPageTests.swift` lines 85, 98, 133, 160, 192; `Tests/MarsDawnKitTests/MathRenderingTests.swift` lines 383–387 |
| S19 | Hostile HTML. `script`/`noscript` are removed from the content and nothing runs; a copy with that filter reverted must fail (red control); inline handlers are blocked by the enforced CSP; `link`/`meta`/`base`/`iframe`/`object`/`embed` never reach the page. Remote content: the blocked list stops every request; with remote images allowed only the HTTPS image loads and plain HTTP never connects; preconnects are stopped too. | kit `Tests/MarsDawnKitTests/PreviewFilterAndCSPSecurityTests.swift` lines 43, 54, 96; `Tests/MarsDawnKitTests/PreviewDOMFilterTests.swift` lines 29–31, 98; `Tests/MarsDawnKitTests/ContentRuleBehaviorTests.swift` lines 84, 150, 245 |
| S20 | Hostile theme files are refused, and no message repeats a control character, a link, a mention or more than a capped slice of the input. Theme files over 16,384 bytes are refused unread. | kit `Tests/MarsDawnThemesTests/ThemeFixtureTests.swift` lines 108–123, 128, 145 |

---

## en

- **title**: `How we test MarsDawn: one test, two Macs · MarsDawn`
- **description** (about 150 characters): `A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.`

```html
<section class="intro">
  <h1>A test that passes on one Mac may not be testing what you think.</h1>
  <!-- src S11 -->
  <p>Vibe coding isn't a bad thing. Describing what you want and letting an agent build it is how a lot of software starts now, and MarsDawn is built with agents too. But software people rely on is judged by what comes after the first version: years of maintenance, and keeping it secure. An agent can change dozens of files in an evening. So who checks it didn't break anything? Here is one test that showed us how that checking goes wrong, and what we changed.</p>
</section>

<div class="summary"><p><strong>A test passed on a Mac mini and failed on a MacBook Air. The product was fine. The test had been reading colours through the screen's colour profile, and on the Mac mini it had been passing by luck. A second machine found a bug in the test, not in the code.</strong></p></div>

<h2>The test that failed on a MacBook Air</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>A full run of the export engine's tests on GitHub's macOS 15 runner takes close to an hour: about 32 minutes for the debug build and about 25 for the release build. To cut that down, we started moving the macOS 26 half onto a MacBook Air of our own (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>On its first run there, one test failed. It exports a PDF with callouts (Note, Tip, Warning) and checks that each one has a bar at its edge in the right colour, meaning a colour distance under 0.16. On the MacBook Air the distances were 0.1634, 0.1648 and 0.1796. On a Mac mini, with the same commit, macOS and Xcode, the test passed.</p>
<p>Our first guess was that the export had broken. It hadn't. Nothing was wrong with the PDF; what differed between the machines was how the test read it.</p>
<!-- src S1, S2: kit #241 -->
<p>The test turned each PDF page into an image and read the pixels, and macOS draws that image in the colour space of the main display. The Mac mini was connected to an ordinary external monitor; the MacBook Air was using its built-in screen. We filled an image with one orange and read it back: (0.784, 0.278, 0.106) came back as (0.822, 0.335, 0.179) on the Mac mini and (0.782, 0.395, 0.221) on the MacBook Air.</p>
<!-- src S3: kit #242 verification comment -->
<p>Here's the part that matters: on the Mac mini, the test hadn't been reading the right colours either. It was off by as much as 0.128, just inside the 0.16 limit. It passed because of the monitor, not because it measured the bar correctly.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>The fix (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) changes only the test: it draws the page into an image with a fixed sRGB colour space, so no screen is involved. Both machines now read the bar colours exactly: the best match is 0.0, on the MacBook Air's built-in screen as well as on the Mac mini. The pull request's CI passed (<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), and so did the full suite on the MacBook Air runner (run {{TBD:mba-run}}). Then we made it fail on purpose: with every expected colour set to blue, it went red for all five callouts.</p>
<p>It still has a known gap. Note and Caution use two oranges about 0.119 apart, inside the 0.16 limit, so if those two were swapped, the test would probably not notice. We've written that down rather than pretend the test is complete.</p>
<p>A test that can't fail protects nothing, and neither does one that fails for the wrong reason, like a screen's colour profile. Green on one machine tells you the test passed there, not that it measures what its name says.</p>

<h2>What red and green mean</h2>
<!-- src S14 -->
<p>Green means a test passed. That's only worth something if you've seen the same test go red when the thing it checks is actually wrong. So the order matters: break it on purpose, watch it turn red, put it back, watch it turn green. Then you know the test is looking at the right thing. If you've never seen it red, a green check might just mean the test isn't looking.</p>

<h2>Tests are layers of nets</h2>
<p>No single test catches everything. Each layer is a net with a different mesh, and a mistake that slips through one should land in the next:</p>
<ul>
  <!-- src S6 -->
  <li><strong>Unit tests</strong> in the export engine (the open-source <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, which also powers the <code>marsdawn</code> command): a piece of code that returns the wrong answer.</li>
  <!-- src S13 -->
  <li><strong>Reference PDFs:</strong> sample documents are exported and every page's text is compared with a recorded copy. This catches content that silently goes missing, or a page count that changes.</li>
  <!-- src S6, S9 -->
  <li><strong>Different systems and builds:</strong> the engine runs on macOS 15, the oldest version it supports, and macOS 26, the one the app ships on, each as a debug and a release build. The app's full suite runs in four combinations: signed and unsigned, each with the paywall off and on. This catches what breaks only on an older system, or only in the build customers actually get.</li>
  <!-- src S4, S1 -->
  <li><strong>Real hardware:</strong> besides GitHub's machines, tests run on Macs of our own, including the MacBook Air above. This catches what a server without a screen can't show.</li>
  <!-- src S12 -->
  <li><strong>Red controls:</strong> the app's CI keeps 11 deliberately broken copies of a cleanup script, each missing one safety check, and the tests must fail on every one. If one passes, the test is the thing that's broken.</li>
  <!-- src S3, S15 -->
  <li><strong>A second pair of eyes:</strong> a separate agent verifies each change, and a scenario review checks how people will really use a feature before it's built. This catches "done" that isn't, and code that works but in the wrong situation.</li>
  <li><strong>A person merges.</strong> No change reaches the main branch because an agent said it was done.</li>
</ul>

<h2>What we throw at it</h2>
<p>Those nets are only as good as what goes into them. A few of the inputs the engine's tests feed it, and what each test makes sure happens:</p>
<ul>
  <!-- src S16 -->
  <li><strong>Very large files.</strong> A 2 MB document renders in under a second and a half. A 5 MB one too complex to lay out still opens, as plain text, within a second. Anything over 16 MB is shown as text without being parsed at all.</li>
  <!-- src S16 -->
  <li><strong>Hundreds of thousands of lines.</strong> About 3 MB of one-word lines, close to 800,000 of them, is spotted as too much partway through reading and shown as plain text instead of tying the app up.</li>
  <!-- src S17 -->
  <li><strong>Markers that never close.</strong> A megabyte of section openers with no closers, or tens of thousands nested inside each other, must take no more than about twice as long as a megabyte of plain text. Nesting stops at eight levels.</li>
  <!-- src S18 -->
  <li><strong>Formulas.</strong> A broken formula shows an error where it sits instead of breaking the page. One over 10,000 characters stays as written, only the first 1,000 in a document are drawn at a time, and nothing in a formula can turn into a link, an image or page markup.</li>
  <!-- src S19 -->
  <li><strong>Hostile HTML inside Markdown.</strong> Scripts are removed and never run, and embedded frames are taken out before the page shows them. Remote images stay off unless you allow them, and even then only secure (HTTPS) ones load. One control copy has the script filter taken out, and the test must fail on it.</li>
  <!-- src S20 -->
  <li><strong>A hostile theme file.</strong> It's refused, and the error message never repeats hidden control characters or links from the file. Theme files over 16 KB aren't read at all.</li>
</ul>
<!-- src S5 -->
<p>None of this is free. The time limit for one engine run has gone from 30 minutes to 45, then 50, then 70, and macOS 15 once hit the 50-minute limit twice with every test passing.</p>

<h2>Four habits you can copy</h2>
<ol>
  <li><strong>Keep the agent that writes apart from the agent that checks.</strong> Give the checker the change and what "done" means, not the writer's explanation, and ask it to run the tests itself and say what it didn't check. For kit #242, the verifier ran the old test on the MacBook Air to watch it fail before passing the new one. It costs a second session's tokens, which is still cheaper than fixing a broken change later.</li>
  <li><strong>See every test fail once.</strong> Before you trust a green check, break the thing it guards (or ask the agent to) and make sure it goes red. Agents are good at writing tests that pass; that's exactly why you need to see them fail.</li>
  <li><strong>Run your tests in a second environment.</strong> No second Mac? A CI matrix with two OS versions, or a debug build and a release build, is a fine start. You're looking for tests that pass only by accident.</li>
  <!-- src S7, S8 -->
  <li><strong>Treat "no tests ran" as a failure.</strong> Python 3.9's <code>unittest</code> exits successfully when it finds no tests at all, so a typo in a path gives you a green check. Our CI reads the count and fails on zero, and checks that the summary says "0 failed", not just the exit code. An agent reporting "all tests pass" when none ran is one of the most common false finishes there is.</li>
</ol>

<h2>The short version</h2>
<!-- src S11 -->
<p>Whether an app was vibe coded matters less than whether anyone keeps testing and maintaining it. That's worth checking when you choose software: does it say how it's tested, and when was it last updated?</p>
<p>Let the agent be fast. Leave the checking to tests that measure the right thing, and to a person who reads the result.</p>

<h2>Next</h2>
<ul>
  <li>Why a person still has to read what an agent wrote: <a href="/reviewing-ai-output/">Why AI output still needs a human reader</a>.</li>
  <li>How to read the plans and reports an agent hands back: <a href="/reading-agent-output/">Reading what your agent hands back</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>The failing test and its cause: <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>The fix and its independent verification: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>Moving CI onto a MacBook Air, with run times: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>The export engine's CI, with the history of its time limit in the comments: <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>The app's repository is private; the app details above come from its CI workflow and test scripts.</li>
</ul>
```

---

## zh-Hant

- **title**: `MarsDawn 怎麼測試：同一個測試，兩台 Mac · MarsDawn`
- **description**: `同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。`

```html
<section class="intro">
  <h1>在一台 Mac 上通過的測試，不一定在測你以為的東西。</h1>
  <!-- src S11 -->
  <p>vibe coding 不是壞事。把想要的東西說出來、讓 agent 做出來，現在很多軟體都是這樣起頭的，MarsDawn 也是用 agent 開發的。但要讓人長期依賴的軟體，看的是第一版之後的事：多年的維護，以及安全。agent 一個晚上就能改幾十個檔案，那誰來確認它沒改壞？下面是一個讓我們看清楚「檢查」會怎麼出錯的測試，以及我們改了什麼。</p>
</section>

<div class="summary"><p><strong>同一個測試，在 Mac mini 上通過，在 MacBook Air 上失敗。產品沒壞。是測試透過螢幕的色彩描述檔在讀顏色，它在 Mac mini 上通過只是運氣好。換一台機器，抓到的是測試的 bug，不是程式的 bug。</strong></p></div>

<h2>只在 MacBook Air 上失敗的測試</h2>
<!-- src S4: kit PR #240（未合併）、run 40196953693 -->
<p>輸出引擎的測試，在 GitHub 的 macOS 15 機器上完整跑一次將近一小時：debug 版約 32 分鐘，release 版約 25 分鐘。為了縮短時間，我們開始把 macOS 26 那一半移到自己的 MacBook Air 上跑（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>）。</p>
<!-- src S1: kit #241、run 40271990387 -->
<p>在那台機器上第一次跑，就有一個測試失敗。這個測試會輸出一份帶有提示框（Note、Tip、Warning）的 PDF，檢查每個提示框邊上的色條顏色對不對，也就是色差要小於 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。換到 Mac mini，同一個 commit、同樣的 macOS 和 Xcode，測試通過。</p>
<p>我們第一個懷疑是輸出壞了。結果不是：PDF 本身沒問題，兩台機器不一樣的，是測試讀它的方式。</p>
<!-- src S1, S2: kit #241 -->
<p>這個測試會把 PDF 每一頁畫成圖片再讀像素，而 macOS 畫這張圖時，用的是主螢幕的色彩空間。Mac mini 接的是一般的外接螢幕，MacBook Air 用的是內建螢幕。我們拿一張填滿同一種橘色的圖片讀回來：(0.784, 0.278, 0.106) 在 Mac mini 上讀成 (0.822, 0.335, 0.179)，在 MacBook Air 上讀成 (0.782, 0.395, 0.221)。</p>
<!-- src S3: kit #242 驗證留言 -->
<p>重點在這裡：在 Mac mini 上，測試讀到的顏色其實也不對，最多差了 0.128，只是剛好落在 0.16 的上限內。它會通過，靠的是那台螢幕，不是因為它真的量對了色條。</p>
<!-- src S3, S10；{{TBD:mba-run}}＝自架 MacBook Air 的 run，來自 kit #240 -->
<p>修正（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>）只改測試：把頁面畫進一張固定使用 sRGB 色彩空間的圖片，完全不經過螢幕。現在兩台機器都能準確讀出色條的顏色：不論是 MacBook Air 的內建螢幕還是 Mac mini，最接近的色差都是 0.0。這個 pull request 的 CI 全部通過（<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>），MacBook Air 機器上的完整測試也通過了（run {{TBD:mba-run}}）。接著我們故意讓它失敗：把每個預期顏色都改成藍色，五個提示框全部變紅。</p>
<p>它還有一個已知的漏洞：Note 和 Caution 用的兩種橘色只差約 0.119，在 0.16 的上限內，所以這兩個顏色如果對調，測試多半不會發現。我們把這件事記了下來，沒有假裝這個測試已經完整。</p>
<p>一個不會失敗的測試，什麼也保護不了；因為錯的理由而失敗的測試（例如螢幕的色彩描述檔）也一樣。一台機器上的綠燈，只代表測試在那台機器上通過，不代表它測的就是名字上寫的那件事。</p>

<h2>紅燈和綠燈代表什麼</h2>
<!-- src S14 -->
<p>綠燈代表測試通過。但只有在你看過同一個測試，在它檢查的東西真的出錯時亮紅燈，這個綠燈才有意義。所以順序很重要：先故意弄壞，看它變紅；再改回來，看它變綠。這樣你才知道測試盯著的是對的地方。如果從來沒看過它變紅，綠燈可能只代表測試根本沒在看。</p>

<h2>測試是一層一層的網子</h2>
<p>沒有一個測試能抓到所有問題。每一層都是一張網目不同的網，從這一層漏掉的錯，應該要被下一層接住：</p>
<ul>
  <!-- src S6 -->
  <li><strong>單元測試</strong>，在輸出引擎裡（開源的 <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>，<code>marsdawn</code> 指令也用它）：抓某一段程式算錯答案。</li>
  <!-- src S13 -->
  <li><strong>參考 PDF：</strong>把一組樣本文件輸出成 PDF，每一頁的文字都和事先記錄的版本比對。抓內容悄悄不見，或頁數突然改變。</li>
  <!-- src S6, S9 -->
  <li><strong>不同的系統和版本：</strong>引擎在 macOS 15（支援的最舊版本）和 macOS 26（App 實際出貨的版本）上都要跑，各跑 debug 和 release 兩種版本。App 的完整測試則跑四種組合：簽章與不簽章，各自再分付費牆開與關。抓只在舊系統上壞掉，或只在使用者實際拿到的版本裡壞掉的問題。</li>
  <!-- src S4, S1 -->
  <li><strong>真的硬體：</strong>除了 GitHub 的機器，測試也在我們自己的 Mac 上跑，包括上面那台 MacBook Air。抓沒有螢幕的伺服器看不出來的問題。</li>
  <!-- src S12 -->
  <li><strong>紅燈對照組：</strong>App 的 CI 固定放著 11 份故意弄壞的清理腳本，每份都拿掉一道安全檢查，測試碰到每一份都必須失敗。只要有一份通過，壞掉的就是測試本身。</li>
  <!-- src S3, S15 -->
  <li><strong>另一雙眼睛：</strong>每個改動都由另一個 agent 驗證；功能動工前，也會先做情境審查，看大家實際會怎麼用。抓「說做完了其實沒做完」，以及程式能跑、卻用錯了場合。</li>
  <li><strong>最後由人合併。</strong>沒有任何改動是因為 agent 說「做完了」就進到主分支。</li>
</ul>

<h2>我們丟給它的東西</h2>
<p>網子好不好，要看丟進去的是什麼。下面是引擎測試會餵給它的幾種輸入，以及每個測試確保會發生的事：</p>
<ul>
  <!-- src S16 -->
  <li><strong>超大的檔案。</strong>2 MB 的文件要在一秒半內顯示完。5 MB、複雜到排不了版的文件照樣打得開，一秒內以純文字顯示。超過 16 MB 的檔案完全不解析，直接以文字顯示。</li>
  <!-- src S16 -->
  <li><strong>幾十萬行。</strong>大約 3 MB、每行只有一個字的文件，將近 80 萬行，讀到一半就會被判定太多，改以純文字顯示，不會把 App 卡住。</li>
  <!-- src S17 -->
  <li><strong>永遠不關的標記。</strong>1 MB 只開不關的區塊標記，或幾萬層互相包住的區塊，花的時間不能超過同樣 1 MB 純文字的兩倍左右。巢狀最多到八層。</li>
  <!-- src S18 -->
  <li><strong>數學公式。</strong>寫錯的公式就在原處顯示錯誤，不會讓整頁壞掉。超過一萬個字元的公式保留原樣；一份文件一次最多畫前 1,000 個；公式裡的內容也不會變成連結、圖片或網頁標籤。</li>
  <!-- src S19 -->
  <li><strong>藏在 Markdown 裡的惡意 HTML。</strong>指令碼會被移除，絕不執行；內嵌的框架在頁面顯示前就被拿掉。遠端圖片預設不載入，就算你允許，也只載入安全連線（HTTPS）的圖片。另有一份拿掉指令碼過濾的對照版本，測試碰到它必須失敗。</li>
  <!-- src S20 -->
  <li><strong>惡意的主題檔。</strong>會被拒絕，錯誤訊息也不會重複檔案裡隱藏的控制字元或連結。超過 16 KB 的主題檔直接不讀。</li>
</ul>
<!-- src S5 -->
<p>這些都有代價。引擎單次執行的時間上限從 30 分鐘拉到 45、50，再到 70 分鐘；macOS 15 還曾在測試全部通過的情況下，兩次撞到 50 分鐘的上限。</p>

<h2>你也能照做的四個習慣</h2>
<ol>
  <li><strong>寫的 agent 和驗的 agent 分開。</strong>只給驗證的那個改動本身和「怎樣才算完成」，不要給寫的人的說明，請它自己跑測試，並列出沒驗到的地方。驗 kit #242 時，驗證的 agent 先在 MacBook Air 上跑舊測試、親眼看它失敗，才讓新測試過關。這要多花一個 session 的 token，但比起事後修一個壞掉的改動，還是便宜。</li>
  <li><strong>每個測試都要看它失敗一次。</strong>相信綠燈之前，先把它守著的東西弄壞（或請 agent 弄壞），確認它會變紅。agent 很會寫出會通過的測試，正因為這樣，你才需要看到它失敗。</li>
  <li><strong>測試至少在第二個環境跑一次。</strong>沒有第二台 Mac 也沒關係，CI 裡跑兩個 OS 版本，或 debug 和 release 各跑一次，就是不錯的起點。要找的是那些靠運氣才通過的測試。</li>
  <!-- src S7, S8 -->
  <li><strong>「一個測試都沒跑」要算失敗。</strong>Python 3.9 的 <code>unittest</code> 一個測試都沒找到時，還是會回報成功，所以路徑打錯一個字，你照樣拿到綠燈。我們的 CI 會讀測試數量，是 0 就失敗，也會檢查摘要寫的是「0 failed」，不只看結束代碼。agent 回報「測試全部通過」，其實一個都沒跑，是最常見的假完成之一。</li>
</ol>

<h2>一句話</h2>
<!-- src S11 -->
<p>一個 App 是不是 vibe coding 做的，沒那麼重要；重要的是有沒有人持續在測試、在維護。選軟體的時候值得看一眼：它有沒有說明自己怎麼測試？最近一次更新是什麼時候？</p>
<p>速度交給 agent，把關留給真的量對東西的測試，以及讀過結果的人。</p>

<h2>接下來</h2>
<ul>
  <li>為什麼 agent 寫的東西還是要有人讀過：<a href="/zh-hant/reviewing-ai-output/">為什麼 AI 寫的東西還是需要人讀過</a>。</li>
  <li>怎麼讀 agent 交回來的計畫和報告：<a href="/zh-hant/reading-agent-output/">讀懂 agent 交回來的 Markdown</a>。</li>
</ul>

<h2>資料來源</h2>
<ul>
  <li>失敗的測試和原因：<a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>。</li>
  <li>修正和獨立驗證：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>。</li>
  <li>把 CI 移到 MacBook Air，附執行時間：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>。</li>
  <li>輸出引擎的 CI，時間上限的調整歷史寫在註解裡：<a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>。</li>
  <li>App 的程式碼庫不公開；上面關於 App 的內容，來自它的 CI 設定和測試腳本。</li>
</ul>
```

---

## Footer label (`ui` dict, `how-we-test`)

| en | zh-Hant |
|---|---|
| How we test | 我們怎麼測試 |

The other six languages (zh-Hans, ja, ko, de, fr, es) come after en and zh-Hant are approved and the TBDs are filled in, so they aren't translated twice.

Co-authored-by: Grok <grok@southern-light.dev>
