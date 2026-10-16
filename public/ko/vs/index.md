# Mac에서 Markdown 읽기: MarsDawn과 다른 방법

Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 [지원](/ko/support/) 페이지의 주소로 알려 주세요.

|  | MarsDawn | VS Code 미리보기 | Obsidian | QLMarkdown | LynxOffice |
|---|---|---|---|---|---|
| 로컬 .md 열기 | 가능, 원본 파일을 바로 편집 [app 1.1.1] | 가능, ⇧⌘V로 미리보기 [[V8](#v8)] | 공식 설명 없음 [[V21](#v21)] | 미리보기만: "for viewing Markdown files" [[V22](#v22)] | "Markdown opens rendered and saves back verbatim." [[V3](#v3)] |
| Mermaid | 기본 제공 [[V1](#v1)] | 기본 제공 [[V8](#v8)] | 기본 제공, 노트 문법 [[V16](#v16)] | 기본 제공, `mermaid` 블록 [[V22](#v22)] | "diagram blocks are not rendered" [[V3](#v3)] |
| 수식 | KaTeX, `$…$`와 `$$…$$` [[kit](#kit)] | KaTeX [[V8](#v8)] | MathJax [[V16](#v16)] | MathJax [[V22](#v22)] | "Footnotes, math, and diagram blocks are not rendered." [[V3](#v3)] |
| 에이전트의 계획 검토／줄로 이동 | `marsdawn open file:line`, 디스크에서 업데이트, 참조 복사 [/cli/, /features/] | Markdown diff 미리보기, 변경된 줄 강조 [[V8](#v8)]; `code -g file:line` [[V14](#v14)] | `obsidian://open`에 줄 번호 지정 없음 [[V20](#v20)] | 공식 설명 없음 | CLI와 MCP 서버 있음, 줄 이동은 설명 없음 [[V4](#v4), [V5](#v5)] |
| PDF: 페이지 나누기, 페이지 번호 | 짧은 코드 블록을 나누지 않는 페이지 나누기 [/pdf/], 페이지 번호 없음 [직접 확인] | 공식 설명 없음 [[V8](#v8)] | 용지 크기, 여백; 페이지 나누기와 번호는 설명 없음 [[V17](#v17)] | 공식 설명 없음 [[V22](#v22)] | PDF "including tables", 페이지 나누기와 번호는 설명 없음 [[V3](#v3)] |
| 가격 | 무료 다운로드, 잠금 해제 한 번 USD 4.99, 14일 체험 [[V1](#v1)] | 공식 설명 없음 [[V12](#v12), [V13](#v13)] | 개인: "Free without limits", 상업용 라이선스는 선택 [[V15](#v15)] | 무료, GPL-3.0 [[V22](#v22)] | "Free while in early release." [[V2](#v2)] |
| 시스템 요구 사항 | macOS 26.0 이상 [[V1](#v1)] | "the latest release and the two previous versions" [[V9](#v9)] | 공식 설명 없음 [[V18](#v18)] | macOS 12.0 이상 [[V23](#v23)] | macOS 13 이상 [[V2](#v2)] |
| 계정 필요 | 필요 없음 [/privacy/] | 공식 설명 없음 | "No sign-up required" [[V15](#v15)] | 공식 설명 없음 | 필요 없음 [[V2](#v2)] |

모든 칸은 2026년 10월 16일에 괄호 안의 출처로 확인했습니다(V 번호는 아래 목록, [직접 확인]은 marsdawn 0.6.4로 직접 내보낸 결과). 각 회사의 원문은 그대로 인용합니다. ‘공식 설명 없음’은 읽은 페이지에 언급이 없었다는 뜻이며, 기능이 없다는 뜻은 아닙니다. 표는 제품의 순위를 매기지 않습니다.

## 출처

- V1 · [Mac App Store](https://apps.apple.com/app/id6812925073)
- V2 · [https://lynxoffice.com/](https://lynxoffice.com/)
- V3 · [https://lynxoffice.com/markdown/](https://lynxoffice.com/markdown/)
- V4 · [https://lynxoffice.com/cli/](https://lynxoffice.com/cli/)
- V5 · [https://lynxoffice.com/mcp/](https://lynxoffice.com/mcp/)
- V6 · [https://lynxoffice.com/release-notes/](https://lynxoffice.com/release-notes/)
- V8 · [https://code.visualstudio.com/docs/languages/markdown](https://code.visualstudio.com/docs/languages/markdown)
- V9 · [https://code.visualstudio.com/docs/supporting/requirements](https://code.visualstudio.com/docs/supporting/requirements)
- V11 · [https://code.visualstudio.com/updates/v1_142](https://code.visualstudio.com/updates/v1_142)
- V12 · [https://code.visualstudio.com/license](https://code.visualstudio.com/license)
- V13 · [https://code.visualstudio.com/](https://code.visualstudio.com/)
- V14 · [https://code.visualstudio.com/docs/configure/command-line](https://code.visualstudio.com/docs/configure/command-line)
- V15 · [https://obsidian.md/pricing](https://obsidian.md/pricing)
- V16 · [https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax](https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax)
- V17 · [https://obsidian.md/help/pdf](https://obsidian.md/help/pdf)
- V18 · [https://obsidian.md/download](https://obsidian.md/download)
- V19 · [https://obsidian.md/changelog/](https://obsidian.md/changelog/)
- V20 · [https://obsidian.md/help/uri](https://obsidian.md/help/uri)
- V21 · [https://obsidian.md/help/Getting+started/Create+a+vault](https://obsidian.md/help/Getting+started/Create+a+vault)
- V22 · [https://github.com/sbarex/QLMarkdown](https://github.com/sbarex/QLMarkdown)
- V23 · [https://github.com/sbarex/QLMarkdown/releases](https://github.com/sbarex/QLMarkdown/releases)
- V24 · [https://api.github.com/repos/sbarex/QLMarkdown/releases](https://api.github.com/repos/sbarex/QLMarkdown/releases)
- kit · [https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7](https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7)

MarsDawn에 없는 것. macOS 26 이상이 필요합니다. iPhone이나 iPad 앱은 없으며, MarsDawn은 Mac 전용입니다. 공동 편집, 동기화, 계정이 없습니다. 미리보기는 직접 편집할 수 없고, 옆의 Markdown 소스를 편집합니다. Word로 내보내기와 플러그인이 없습니다. PDF에는 페이지 번호가 없습니다. diff 보기가 없습니다. 에이전트가 변경을 저장하면 열린 윈도우가 디스크에서 업데이트되고 한 번에 실행 취소할 수 있지만, 무엇이 바뀌었는지는 강조하지 않습니다. 14일 체험이 끝나면 잠금 해제할 때까지 문서 내용이 가려진 채로 열립니다.

## MarsDawn이 필요 없는 경우

- 늘 VS Code에서 일하고 미리보기 패널로 충분한 경우. Mermaid와 KaTeX를 렌더링하고, Markdown diff 미리보기가 있으며, code -g로 줄로 이동할 수 있습니다.
- Finder에서 스페이스 바 미리보기만 원하는 경우. QLMarkdown은 무료 Markdown 훑어보기 확장입니다.
- Mac의 macOS가 오래된 경우. QLMarkdown은 12.0 이상, LynxOffice는 13 이상이 필요합니다. 무료 marsdawn 도구는 macOS 15에서 동작하며 앱 없이 PDF를 내보냅니다.
- 서로 연결된 노트를 보관소(vault)에서 관리하는 경우. Obsidian이 바로 그런 앱입니다.
- iPhone이나 iPad 앱, 공동 편집, Word 내보내기가 필요한 경우.
- 에이전트에게 스프레드시트, Word, PDF를 다루게 하려는 경우. LynxOffice는 이를 위한 MCP 서버를 문서로 제공합니다.

- [MacMD Viewer와 MarsDawn](/ko/vs/macmd-viewer/): 읽기 전용 뷰어와 MarsDawn을 칸마다 비교하고, 어떤 경우에 무엇을 고를지 적었습니다.
- [Markdown 미리보기 도구](/ko/vs/markdown-preview-tools/): VS Code 미리보기, 브라우저 확장, Claude Desktop의 파일 미리보기.

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
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
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
- [English](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [Français](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [Español](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
