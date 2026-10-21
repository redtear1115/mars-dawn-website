# Mac에서 .md 파일을 여는 방법.

더블 클릭하면 열립니다. Mac이 텍스트 편집기로 파일을 열어 제목과 굵은 글씨 대신 `#`와 `**`가 보여도 파일에는 문제가 없습니다. `.md` 파일은 일반 텍스트이고, 그 편집기는 텍스트를 있는 그대로 보여 주는 것입니다. MarsDawn처럼 Markdown을 렌더링하는 앱으로 열고, 그 앱을 기본 앱으로 지정하면 모든 `.md` 파일이 그곳에서 열립니다.

`.md` 파일은 일반 텍스트입니다. 제목, 굵은 글씨, 표, 다이어그램은 기호로 적혀 있습니다. 제목은 `#`, 굵은 글씨는 `**`로 감싸고, 표는 세로 막대로, 다이어그램은 `mermaid` 코드 블록으로 씁니다. 일반 텍스트 편집기로 열면 이 기호들이 그대로 보입니다. 작성자가 의도한 대로 페이지를 읽으려면 무언가가 렌더링해 줘야 합니다.

## Mac에서 .md 파일 열기

1. **파일을 더블 클릭합니다.** Mac이 `.md` 파일에 지정한 앱에서 열립니다. Markdown 앱이 없으면 대개 일반 텍스트 편집기가 열려, 완성된 페이지 대신 기호가 보입니다.
2. **앱을 직접 고릅니다.** Control 키를 누른 채 파일을 클릭하고 “다음으로 열기”를 선택한 다음 앱을 고릅니다. 또는 “파일 ▸ 정보 가져오기”(⌘I)를 선택하고, “다음으로 열기:”에서 앱을 고른 뒤 “모두 변경…”을 클릭하면 같은 종류의 모든 파일이 그 앱에서 열립니다. MarsDawn은 `.md`, `.markdown`, `.mdown`, `.mkd`, `.mkdn` 파일을 열 수 있습니다.
3. **열지 않고 미리 봅니다.** Finder에서 파일을 선택하고 스페이스 바를 누릅니다. MarsDawn이 설치되어 있으면 훑어보기에 렌더링된 페이지가 표시되고, 다이어그램도 포함됩니다.

## MarsDawn에서 읽기

MarsDawn은 Mac용 Markdown 편집기입니다. Mac App Store에서 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다. macOS 26 이상이 필요합니다.

[Mac App Store에서 MarsDawn 무료로 다운로드](https://apps.apple.com/app/id6812925073)

`.md` 파일을 열고 원본 옆에서 렌더링된 페이지를 읽으세요.

- 입력하는 동안 미리보기가 업데이트되고, 두 패널이 함께 스크롤됩니다.
- [Mermaid](/ko/mermaid-preview-mac/) 순서도와 시퀀스 다이어그램이 미리보기에 그려지고, 코드 블록은 강조 표시됩니다.
- 무언가를 고치고 싶을 때 원본이 바로 옆에 있습니다. MarsDawn은 뷰어만이 아니라 편집기입니다.

AI 에이전트가 쓴 파일이라면, 이것이 바로 MarsDawn이 만들어진 이유인 반복 과정입니다. 에이전트가 쓰고, 여러분이 렌더링된 결과를 읽고, 에이전트가 고칩니다. [홈페이지](/ko/)를 참고하고, 에이전트가 대신 파일을 열게 하려면 [에이전트를 위한 marsdawn](/ko/cli/agents/)을 참고하세요. 이렇게 읽는 일이 왜 중요한지, 계획은 어떻게 검토하는지는 [에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)와 [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/)에서 확인하세요.

## 앱 없이: PDF로 바꾸기

무료 `marsdawn` 명령줄 도구는 Markdown 파일을 어떤 Mac에서든 열 수 있는 PDF로 렌더링합니다. 표, 수식, Mermaid 다이어그램, 강조 표시된 코드가 렌더링된 상태로 나오며, 다른 것은 아무것도 설치할 필요가 없습니다. MarsDawn 앱조차 필요 없습니다.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export`는 Markdown 파일 옆에 `notes.pdf`를 쓰고, `open`은 그 파일을 PDF 뷰어에서 보여 줍니다. macOS 15 이상이 필요합니다. 실제로 내보낸 페이지와 함께 보는 단계별 안내는 [Markdown을 PDF로](/ko/markdown-to-pdf/)에 있습니다.

## 자주 묻는 질문

### .md 파일이란?

`.md` 파일은 Markdown으로 쓴 일반 텍스트 파일입니다. Markdown은 간단한 문자로 텍스트에 표시를 하는 방법으로, `#`은 제목, `**`로 감싸면 굵은 글씨, 세로 막대는 표의 칸이 됩니다. `.markdown`, `.mdown`, `.mkd`, `.mkdn` 확장자도 같은 것을 뜻합니다. 개발자는 README와 문서에 쓰고, AI 에이전트도 계획과 보고서를 `.md` 파일로 돌려주는 경우가 많습니다.

### .md 파일이 # 와 ** 가 가득한 일반 텍스트로 열리는 이유는?

원래 일반 텍스트이고, 일반 텍스트 편집기는 그대로 보여 주기 때문입니다. 파일에는 아무 문제가 없습니다. 제목, 굵은 글씨, 표, 다이어그램을 보려면 Markdown을 렌더링하는 앱으로 여세요. MarsDawn에서는 렌더링된 페이지가 소스 옆에 있습니다.

### 열면 글자가 깨져 보이는 이유는?

글자가 깨지는 것은 대개 파일이 UTF-8이 아닌 다른 텍스트 인코딩으로 저장되어 있고, 파일을 연 앱이 인코딩을 잘못 추측했기 때문입니다. 해결책은 UTF-8 사본을 저장하는 것입니다. MarsDawn은 UTF-8이 아닌 일반 텍스트 파일을 읽기 전용으로 열고, 창 위쪽의 막대에 어떤 인코딩으로 읽었는지 표시하며, 그곳의 “UTF-8로 별도 저장…” 또는 “파일 ▸ 별도 저장…”(⌥⇧⌘S)으로 편집할 수 있는 UTF-8 사본을 만들 수 있게 합니다.

### .md 파일을 PDF로 바꿀 수 있나요?

네. MarsDawn에서 “파일 ▸ PDF로 내보내기…”(⌥⌘E) 또는 “파일 ▸ 프린트…”를 선택하면, 페이지가 나뉘고 다이어그램이 그려지며 코드는 강조 표시된 채로, 테마의 라이트 색상으로 출력됩니다. 앱이 없어도 무료 `marsdawn export` 명령줄 도구가 같은 PDF를 만듭니다: `marsdawn export notes.md`. [PDF 내보내기](/ko/pdf/)와 [Markdown을 PDF로](/ko/markdown-to-pdf/)를 참고하세요.

### AI 에이전트가 쓴 .md 파일도 열 수 있나요?

네, MarsDawn은 바로 그것을 위해 만들어졌습니다. 파일을 열고 렌더링된 페이지를 소스 옆에서 읽으세요. 에이전트가 고치면 다시 여세요. 에이전트가 `marsdawn open plan.md`를 실행해 MarsDawn에서 파일을 대신 열어 줄 수도 있습니다. [에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)를 참고하세요.

## 다음

- 명령줄 도구의 모든 옵션: [명령줄](/ko/cli/).
- MarsDawn이 하지 않는 일: [목록](/ko/limits/).
- VS Code, 브라우저, Claude Desktop에서 Markdown을 읽는 경우: [비교해 보기](/ko/vs/markdown-preview-tools/).
- Markdown 파일 속 다이어그램: [Mac에서 Mermaid 미리보기](/ko/mermaid-preview-mac/).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록을 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지이고, 갤러리에 더 있습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [Mac용 Markdown 뷰어 추천 (2026)](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 브라우저에서 테마를 직접 만들고, 커뮤니티 갤러리도 둘러보세요.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [에이전트와 함께 테마 만들기](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
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
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [日本語](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Français](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Español](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
