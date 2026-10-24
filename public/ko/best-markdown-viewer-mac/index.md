# Mac용 Markdown 뷰어 추천 (2026)

어떤 Markdown 뷰어가 가장 좋은지는 무엇을 읽느냐에 달려 있습니다. 직접 쓴 메모라면 올인원 노트 앱으로 충분합니다. 다이어그램과 수식이 들어간 긴 문서나 AI 에이전트가 계속 다시 쓰는 파일이라면, 각 앱이 자동 새로 고침, Mermaid, PDF를 어떻게 다루는지 확인하세요. 아래 앱은 알파벳 순서이며, 각각 누구에게 맞는지, 솔직한 단점 하나, 가격을 적었습니다.

## MacDown 3000

원래의 MacDown은 더 이상 유지 관리되지 않습니다. MacDown 3000은 커뮤니티가 이어받은 버전으로, 무료 오픈 소스(MIT)이고 네이티브이며 Mermaid, MathJax, PDF 내보내기, 자동 새로 고침, 훑어보기를 지원합니다.

- 맞는 사람: 무료 네이티브 좌우 분할 보기를 원하는 사람.
- 단점: 명령줄에서 특정 줄로 여는 방법이 문서화되어 있지 않습니다.
- 가격: 무료.

## Marked

Marked 3은 다른 앱에서 쓴 Markdown을 보기 위한 미리보기 앱입니다. 파일이 바뀔 때마다 다시 불러오고, MathJax와 KaTeX를 지원하며, 페이지 번호가 붙은 PDF를 인쇄할 수 있습니다. Marked 2도 계속 판매 중입니다.

- 맞는 사람: 자신의 작성 도구를 유지하면서 깔끔한 미리보기와 인쇄를 원하는 작가.
- 단점: 훑어보기는 별도 앱인 Marked QL(USD 9.99)이 필요합니다.
- 가격: Marked 3은 무료 다운로드 후 월 USD 2.99, 연 USD 29.99 또는 평생 USD 69.99. Marked 2는 공식 사이트 USD 14.99, Mac App Store USD 13.99.

## MarkEdit

가볍고 무료인 네이티브 앱(웹 뷰에서 CodeMirror 사용)이며 훑어보기를 지원합니다.

- 맞는 사람: 빠르고 Mac다운 일반 텍스트 도구를 원하는 사람.
- 단점: Mermaid와 수식에는 공식 확장 프로그램이, PDF 내보내기에는 Pandoc이 필요합니다.
- 가격: 무료.

## MarsDawn

소스와 실시간 미리보기를 나란히 보여 주는 네이티브 Mac 앱으로, Mermaid와 KaTeX가 내장되어 있습니다. 에이전트가 파일을 저장하면 열린 윈도우가 그 변경을 한 번에 실행 취소할 수 있는 '디스크에서 업데이트'로 받아들입니다. `marsdawn open notes.md:120`으로 특정 줄을 열 수 있고, 에이전트용 스킬과 MCP 서버도 있습니다. 훑어보기는 체험 기간과 관계없이 작동합니다. 'AI용으로 복사'와 '참조 복사'로 텍스트를 에이전트에 넘길 수 있습니다. 직접 선택하지 않는 한 아무것도 Mac 밖으로 나가지 않습니다.

- 맞는 사람: AI 에이전트가 쓴 Markdown을 검토하는 사람.
- 단점: 내보낸 PDF에 페이지 번호가 없습니다.
- 가격: 무료 다운로드, 14일 체험 후 USD 4.99 한 번 결제. 계정 불필요. Mac App Store 전용.

## Obsidian

서로 링크된 Markdown 파일의 보관소(vault)를 중심으로 한 노트 앱으로, Mermaid, MathJax, PDF 내보내기, 자동 새로 고침을 지원합니다.

- 맞는 사람: 자신의 메모로 지식 베이스를 만드는 사람.
- 단점: Electron 앱이며, 파일이 보관소 안에 있을 때 가장 잘 작동합니다.
- 가격: 무료. Sync와 Publish는 유료.

## QLMarkdown

훑어보기 확장 프로그램입니다. Finder에서 .md 파일을 선택하고 스페이스 바를 누르면 됩니다. Mermaid와 MathJax는 선택 사항입니다.

- 맞는 사람: Finder에서 파일을 잠깐 보기만 하면 되는 사람.
- 단점: 읽거나 편집하는 앱이 아니며, PDF 내보내기도 문서화되어 있지 않습니다.
- 가격: 무료(GPL-3.0).

## Typora

미리보기가 곧 문서가 되는 위지윅 방식의 작성 도구로, Mermaid, MathJax, 머리글이나 바닥글에 페이지 번호를 넣는 PDF 내보내기를 지원합니다.

- 맞는 사람: 완성된 모습에 가까운 화면에서 쓰고 싶은 사람.
- 단점: 소스와 미리보기를 나란히 보는 화면이 없습니다.
- 가격: USD 14.99 한 번 결제, 기기 3대까지.

## VS Code 미리보기

기본 Markdown 미리보기로, 1.121부터 Mermaid가 내장되어 있고 KaTeX를 지원합니다. `code -g file:line`으로 특정 줄을 열 수 있습니다.

- 맞는 사람: 이미 VS Code에서 일하는 개발자.
- 단점: Electron 앱이며, PDF 내보내기가 기본 제공되지 않습니다.
- 가격: 무료.

## 비교표

| 앱 | 가격 | Mermaid | 수식 | PDF | 자동 새로 고침 | CLI로 특정 줄 열기 | 훑어보기 | 구성 |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | 무료 | 지원 | MathJax | 지원 | 지원 | 문서화 안 됨 | 지원 | 네이티브 |
| Marked 3 | 월 USD 2.99부터 | 지원 | MathJax, KaTeX | 지원, 페이지 번호 | 지원 | 문서화 안 됨 | Marked QL, USD 9.99 | 네이티브 |
| MarkEdit | 무료 | 확장 프로그램 | KaTeX(확장 프로그램) | Pandoc | 문서화 안 됨 | 문서화 안 됨 | 지원 | 네이티브(웹 뷰) |
| MarsDawn | USD 4.99 한 번 | 지원 | KaTeX | 지원, 페이지 번호 없음 | 지원, 실행 취소 가능 | 지원 | 지원 | 네이티브 |
| Obsidian | 무료 | 지원 | MathJax | 지원 | 지원 | 문서화 안 됨 | 문서화 안 됨 | Electron |
| QLMarkdown | 무료 | 선택 사항 | MathJax(선택 사항) | 문서화 안 됨 | 해당 없음 | 해당 없음 | 그 자체 | 네이티브 |
| Typora | USD 14.99 한 번 | 지원 | MathJax | 지원, 페이지 번호 | 문서화 안 됨 | 문서화 안 됨 | 문서화 안 됨 | 네이티브 |
| VS Code | 무료 | 지원(1.121 이상) | KaTeX | 미지원 | 문서화 안 됨 | 지원 | 문서화 안 됨 | Electron |

## MarsDawn이 맞지 않는 사람

- PDF에 페이지 번호가 꼭 필요한 사람. Typora와 Marked 3은 넣을 수 있지만 MarsDawn은 넣을 수 없습니다.
- 서로 링크된 개인 메모 지식 베이스를 가꾸는 사람. Obsidian은 그 용도로 만들어졌습니다.
- VS Code를 떠나지 않는 사람. 기본 미리보기는 무료이고, VS Code는 Agents 윈도우에 실험적인 Markdown 보기를 추가하고 있습니다.
- Finder에서 미리보기만 하면 되는 사람. QLMarkdown은 무료입니다.

## 자주 묻는 질문

### Mermaid를 지원하는 무료 Mac Markdown 뷰어는?

MacDown 3000, Obsidian, VS Code(1.121 이상)에 내장되어 있습니다. QLMarkdown은 선택 사항으로, MarkEdit은 확장 프로그램으로 지원합니다.

### 페이지 번호가 붙은 PDF를 내보낼 수 있는 앱은?

Typora와 Marked 3입니다. MarsDawn의 PDF에는 페이지 번호가 없습니다.

### 명령줄에서 특정 줄로 파일을 열 수 있는 앱은?

MarsDawn(`marsdawn open notes.md:120`)과 VS Code(`code -g file:line`)입니다. 나머지는 문서화되어 있지 않습니다.

### Electron이 아닌 네이티브 Mac 앱은?

Obsidian과 VS Code를 제외한 모두입니다. MarkEdit은 네이티브 앱이며 편집 영역에 웹 뷰를 사용합니다.

[지금 다운로드하고 체험하기](https://apps.apple.com/app/id6812925073)

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록을 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 테마는 바꿀 수 있지만 사용자 지정 CSS는 없습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [테마](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크를 각각 갖춘 기본 미리보기 테마 네 가지와, Mac용 MarsDawn 설정에서 여는 엄선된 테마 갤러리. 훑어보기도 고른 테마를 씁니다.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [에이전트와 함께 테마 만들기](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 개발자가 검토한 MarsDawn 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만들 수 있습니다. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
- [로드맵](https://marsdawn.southern-light.dev/ko/roadmap/index.md): Mac, iPhone, iPad용 MarsDawn에서 개발 중인 기능과 다음에 나올 기능을 버전별로 정리했습니다. 날짜는 적지 않고, 일정이 없는 항목은 따로 표시합니다.
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
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
