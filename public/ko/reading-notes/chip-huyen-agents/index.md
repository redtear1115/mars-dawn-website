# Chip Huyen의 read-only/write action 구분, 승인하기 전에 왜 중요한지

**Chip Huyen의 2025년 1월 에세이 «Agents»는 교과서적 정의에서 시작해 더 구체적인 데로 갑니다. 에이전트의 행동은 세상을 보기만 하는 것과 바꾸는 것으로 나뉩니다. 그 구분은 주어진 5분 안에서, 계획의 어떤 줄이 승인 전에 더 자세히 볼 가치가 있는지 정하는 좋은 방법입니다.**

## 글이 주장하는 것

Huyen은 담백하게 엽니다.

> “An agent is anything that can perceive its environment and act upon that environment.”

거기서 에이전트에 필요한 것을 쌓아 올립니다. 행동할 환경, 그리고 할 수 있는 일을 정하는 도구 집합 — «tool inventory». 환경을 지각만 하게 하는 행동(«read-only actions»)과 환경에 작용하게 하는 행동(«write actions»)을 구분합니다. 두 번째 종류의 위험에 대해서도 직설적입니다. «Write actions enable a system to do more»이지만 «the prospect of giving AI the ability to automatically alter our lives is frightening» — 그녀의 말로 «you shouldn’t allow an unreliable AI to initiate bank transfers.» 에이전트에서 가장 맞추기 어려운 부분에 대해서도 솔직합니다.

> “If you’ve ever been in any planning meeting, you know that planning is hard.”

Huyen은 이 에세이 어디에서도 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다. `/reviewing-agent-plans/`는 이미 같은 에세이에서 그녀 문장 셋을 인용합니다. 계획이 돌기 전에 감독을 건너뛰는 비용, 끝나지 않았는데 끝났다고 믿는 에이전트, 그리고 체크리스트 3단계 안의 «위험한 작업 앞에서 시스템 can ask for explicit human approval before executing»라는 줄. 이 노트는 그 인용을 반복하지 않습니다. 그 페이지를 아직 안 읽었다면 아래에 링크가 있습니다.

## 우리의 읽기이지 Huyen의 것이 아님

Huyen의 read-only/write 구분은 검토 조언으로 쓰인 것이 아닙니다 — 도구가 무엇을 하는지 분류하는 방식입니다. 하지만 그 체크리스트 3단계가 이미 천천히 보라고 하는, 위험한 작업 줄을 짚는 담백하고 범용적인 검사입니다. 파일 읽기, 검색 실행, 디렉터리 나열은 read-only이고, read-only 단계가 잘못되면 다시 돌리는 비용입니다. 데이터 삭제, force-push, 브랜치 병합, 메일 발송, 카드 결제는 write action이고 — 그녀가 말하듯 — write 단계가 잘못되면 무서운 쪽이며, 에이전트 보고서를 읽을 즈음에는 이미 벌어졌을 수 있습니다. 방에 모인 사람에게도 계획이 어렵다는 지적은, 형식이 감당할 수 있는 것보다 더 정밀한 계획을 기대하지 말라는 점검이 됩니다. 자신 있게 읽히는 계획이 곧 맞는 계획은 아닙니다.

## MarsDawn이 돕는 곳, 돕지 않는 곳

MarsDawn은 계획에서 read-only 단계와 write 단계를 구분하지 못합니다 — 텍스트가 라벨을 붙이지 않은 판단이고, 앱 안에는 의미를 읽는 기능이 없습니다. AI 모델도 없습니다. 위험한 줄을 대신 표시해 주지도, «계획은 어렵다» 검사를 돌리지도, 계획에 점수를 매기지도 않습니다. 하는 일은 당신이 그 판단을 하는 동안 파일을 읽기 쉽게 유지하는 것입니다. 개요 탭(보기 ▸ 사이드바 보기, ⌃⌘S)으로 줄마다 읽기 전에 계획의 형태를 훑을 수 있고, 소스와 렌더링된 페이지를 나란히(⌘2) 두어 단계 다이어그램이 날 Mermaid로 남지 않게 하며, 편집 ▸ 참조 복사 (⌥⌘C)는 자리를 `plan.md:10`으로 만들어, 잘못된 순서의 write action을 보는 순간 피드백으로 붙여 넣을 수 있게 합니다.

## 사용해 보기

MarsDawn은 Mac App Store에 있습니다. 무료 `marsdawn` 명령줄 도구는 오늘부터 쓸 수 있습니다:

```
brew install redtear1115/tap/marsdawn
```

앱 없이 Markdown을 PDF로 내보냅니다.

[명령줄](/ko/cli/) · 구입 전에: [MarsDawn이 하지 않는 일](/ko/limits/)

## 다음

- 같은 에세이에서 나온 6단계·5분 체크리스트 전체: [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/)
- 에이전트 출력이 일반적으로 왜 읽기 어려운지: [에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)
- 시리즈로 돌아가기: [편집자의 독서 노트](/ko/reading-notes/)

## 출처

- Chip Huyen, “Agents,” January 7, 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html) (2026-09-26에 가져와 인용).

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 Mermaid 다이어그램, KaTeX 수식, 강조된 코드까지 렌더링된 모습으로 읽을 수 있습니다. MarsDawn의 훑어보기는 체험 기간의 제한을 받지 않습니다.
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
- [독서 노트: Lilian Weng](https://marsdawn.southern-light.dev/ko/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.
- [독서 노트: Harrison Chase](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
- [독서 노트: LangChain(Jess Ou)](https://marsdawn.southern-light.dev/ko/reading-notes/langchain-what-is-an-agent/index.md): LangChain의 2026년 «What is an AI agent?»(Jess Ou)는 Harrison Chase의 2024년 정의를 이어받고, 에이전트를 자동으로 평가하는 파이프라인을 그립니다. 그 파이프라인이 아직 사람에게 넘기는 단계, 그리고 넘기지 않는 단계.
- [독서 노트: Andrew Ng](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章裡，把 agent 的動作分成 read-only 和 write action 兩種。這個分法為什麼是核準計畫前，快速拓出該多看一眼的那一行的好方法。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/chip-huyen-agents/index.md): Chip Huyen 在 2025 年 1 月的文章里，把 agent 的动作分成 read-only 和 write action 两种。这个分法为什么是核准计划前，快速抓出该多看一眼的那一行的好方法。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/chip-huyen-agents/index.md): Chip Huyen が 2025 年 1 月に書いたエッセイは、エージェントの行動を read-only と write action に分ける。承認する前の 5 分間で、計画のどの行を特に見るべきかを見分ける、手早い方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-notes/chip-huyen-agents/index.md): Chip Huyens Essay „Agents“ vom Januar 2025 teilt Aktionen von Agenten in read-only und write. Warum diese Aufteilung ein schneller Weg ist, in einem Plan die Zeile zu finden, die vor der Freigabe einen genaueren Blick verdient.
- [Français](https://marsdawn.southern-light.dev/fr/reading-notes/chip-huyen-agents/index.md): L’essai « Agents » de Chip Huyen de janvier 2025 partage les actions d’un agent en read-only et write. Pourquoi cette distinction est un moyen rapide de repérer, dans un plan, la ligne qui mérite un regard plus attentif avant d’approuver.
- [Español](https://marsdawn.southern-light.dev/es/reading-notes/chip-huyen-agents/index.md): El ensayo «Agents» de Chip Huyen de enero de 2025 reparte las acciones de un agente en read-only y write. Por qué esa división es una forma rápida de ver, en un plan, la línea que merece una mirada más atenta antes de aprobar.
