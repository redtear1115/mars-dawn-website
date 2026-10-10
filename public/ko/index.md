만드는 사람을 위한 개척자의 도구

# 지도를 손에 쥐세요. 새벽을 읽으세요.

에이전트의 작업을 이끄는 사람을 위한 Markdown.

MarsDawn은 소스 옆 실시간 미리보기, Mermaid 다이어그램, KaTeX 수식, 훑어보기(Quick Look), PDF 내보내기를 갖춘 macOS 네이티브 Markdown 편집기로, 14일 동안 무료로 체험할 수 있고 잠금 해제는 한 번만 USD 4.99입니다.

이 페이지에는 앱의 시작 가이드 일부를 보여 주는, 직접 조작할 수 있는 MarsDawn 창이 있습니다. 팔레트 메뉴에서 화면 모드(시스템, 라이트, 다크)를 고르고, 라이트와 다크에 각각 네 가지 미리보기 테마(새벽, 클래식, 모던, 비비드) 중 하나를 지정할 수 있으며, 도구 막대에서는 세 가지 레이아웃(소스, 분할, 미리보기) 중 하나를 고를 수 있습니다.

## 에이전트가 쓴 글을 읽으세요.

1. **에이전트가 씁니다.** 코딩 에이전트나 글쓰기 도우미가 README, 명세서, 메모 같은 Markdown 초안을 작성합니다.
2. **MarsDawn에서 검토합니다.** 파일을 열고, Mermaid 다이어그램과 하이라이트된 코드까지 렌더링된 페이지를 소스 옆에 두고 읽으세요.
3. **에이전트가 고칩니다.** 수정을 요청하세요. 고친 파일을 열어 같은 방식으로 읽으면 됩니다.

[에이전트가 돌려준 결과를 검토하는 방법](/ko/reading-agent-output/).

## 지금 바로 해 보세요

무료 `marsdawn` 명령줄 도구는 지금 바로 쓸 수 있습니다. Homebrew로 설치하세요.

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export`는 Markdown 파일을 MarsDawn의 미리보기처럼 렌더링된 PDF로 만듭니다. 앱은 필요 없습니다.
- `marsdawn open`은 검토할 수 있도록 MarsDawn 앱에서 파일을 엽니다.
- `--json`은 스크립트와 에이전트가 파싱할 수 있는 결과를 돌려줍니다.

[명령줄](/ko/cli/) · [에이전트를 위한 marsdawn](/ko/cli/agents/) · [에이전트 스킬](/ko/cli/skill/) · [MCP 서버](/ko/cli/mcp/)

## MarsDawn에서 기대할 수 있는 것

- [Mac 앱](/ko/native/): 네이티브 윈도우와 탭, 자동 저장, 훑어보기.
- [내 글은 내 Mac에](/ko/yours/): 계정도, 동기화도, 클라우드도 없습니다.
- [무료로 체험하고, 한 번만 구입](/ko/pay-once/): 14일 무료, 이후 USD 4.99 1회 구입. 구독이 아닙니다.

구입 전에 알아 둘 점. [MarsDawn이 하지 않는 일](/ko/limits/)

## 자주 묻는 질문

### MarsDawn은 무엇인가요?

MarsDawn은 Mac용 네이티브 Markdown 편집기입니다. 소스 옆에 실시간 미리보기를 보여 주고, Mermaid 다이어그램과 KaTeX 수식을 그리며, Finder의 훑어보기(Quick Look)로 Markdown 파일을 미리 볼 수 있고, PDF로 내보낼 수 있습니다.

### MarsDawn은 구독인가요?

아니요. MarsDawn은 무료로 다운로드할 수 있고, 14일 동안 모든 기능을 체험할 수 있습니다. 그 뒤에는 USD 4.99의 앱 내 구입 한 번으로 영구히 잠금 해제됩니다. 갱신되는 것은 없고, 계정도 없습니다.

### MarsDawn은 iPhone이나 iPad에서 쓸 수 있나요?

아니요. MarsDawn은 Mac 앱이며 macOS 26 이상이 필요합니다. iPhone용이나 iPad용 앱은 없습니다.

### Claude Code가 MarsDawn에서 파일을 열 수 있나요?

네. 무료 marsdawn 명령줄 도구에는 Markdown 파일을 MarsDawn에서 여는 open 명령이 있어서, Claude Code나 셸 명령을 실행할 수 있는 모든 에이전트가 호출할 수 있습니다. 선택적으로 켜는 Claude Code 훅은 Claude가 쓰거나 편집한 Markdown 파일을 열어 줍니다.

### 체험이 끝나도 훑어보기를 쓸 수 있나요?

네. 체험 중이든 아니든 Finder의 훑어보기는 Markdown 파일을 계속 보여 줍니다. 체험이 끝나고 잠금을 해제하기 전까지는 MarsDawn에서 연 문서의 내용이 가려집니다.

## 앱의 실제 모습

### [Mac 앱](/ko/native/)

![분할 보기의 MarsDawn: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

이 스크린샷의 내용:

1. 네이티브 Mac 윈도우.
2. Markdown 하이라이트가 더해진 Mac의 텍스트 편집기.
3. ⌘1 소스, ⌘2 분할, ⌘3 미리보기.
4. 입력하는 대로 페이지가 바뀝니다.

### [PDF 내보내기](/ko/pdf/)

![MarsDawn에서 내보낸 PDF를 페이지 축소판과 함께 PDF 뷰어로 연 모습.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

이 스크린샷의 내용:

1. Mermaid 다이어그램이 PDF 안에 그려집니다.
2. 코드는 하이라이트를 유지합니다.

## 더 보기

- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 브라우저에서 테마를 직접 만들고, 커뮤니티 갤러리도 둘러보세요.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
- [편집자의 독서 노트](https://marsdawn.southern-light.dev/ko/reading-notes/index.md): AI 에이전트를 만드는 사람들이 실제로 무엇을 주장하는지 살피는 짧은 노트 여섯 편 — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain, Andrew Ng — 그리고 각각이 그런 에이전트가 돌려준 것을 읽어야 하는 사람에게 무엇을 의미하는지.
- [독서 노트: Anthropic](https://marsdawn.southern-light.dev/ko/reading-notes/anthropic-building-effective-agents/index.md): 2024년 12월 Anthropic이 에이전트를 만드는 사람을 위해 낸 가이드는 workflow와 agent를 나누고, 그중 하나가 두 번째 LLM 호출로 첫 번째를 검토하는 다섯 가지 workflow 패턴을 설명합니다. 그게 폴더에 떨어지는 파일에 무엇을 뜻하는지.
- [독서 노트: Chip Huyen](https://marsdawn.southern-light.dev/ko/reading-notes/chip-huyen-agents/index.md): Chip Huyen의 2025년 1월 에세이 «Agents»는 에이전트 행동을 read-only와 write로 나눕니다. 그 구분이 계획에서 승인 전에 더 자세히 볼 줄을 빠르게 짚는 방법이 되는 이유.
- [독서 노트: Lilian Weng](https://marsdawn.southern-light.dev/ko/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.
- [독서 노트: Harrison Chase](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
- [독서 노트: LangChain(Jess Ou)](https://marsdawn.southern-light.dev/ko/reading-notes/langchain-what-is-an-agent/index.md): LangChain의 2026년 «What is an AI agent?»(Jess Ou)는 Harrison Chase의 2024년 정의를 이어받고, 에이전트를 자동으로 평가하는 파이프라인을 그립니다. 그 파이프라인이 아직 사람에게 넘기는 단계, 그리고 넘기지 않는 단계.
- [독서 노트: Andrew Ng](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/index.md): MarsDawn is a native Markdown editor for Mac with live split preview, Mermaid, KaTeX, Quick Look and PDF export. Free to try, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): MarsDawn 是 Mac 原生 Markdown 編輯器：即時分割預覽、Mermaid、KaTeX、快速查看、PDF 輸出。免費試用，之後一次 USD 4.99 解鎖。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): MarsDawn 是 Mac 原生 Markdown 编辑器：实时分栏预览、Mermaid、KaTeX、快速查看、PDF 导出。免费试用，之后一次 USD 4.99 解锁。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): MarsDawn は Mac 向けのネイティブ Markdown エディタです。ライブ分割プレビュー、Mermaid、KaTeX、クイックルック、PDF 書き出し。無料で試せて、USD 4.99 の買い切り。
- [Deutsch](https://marsdawn.southern-light.dev/de/index.md): MarsDawn ist ein nativer Markdown-Editor für Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Français](https://marsdawn.southern-light.dev/fr/index.md): MarsDawn est un éditeur Markdown natif pour Mac : aperçu en direct côte à côte, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): MarsDawn es un editor Markdown nativo para Mac: vista previa en vivo, Mermaid, KaTeX, Vista rápida, exportación PDF. Pruébalo gratis; luego, 4,99 USD una vez.
