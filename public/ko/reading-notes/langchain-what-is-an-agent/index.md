# Jess Ou의 평가 파이프라인, 그중 한 단계는 여전히 당신의 일

**2026년 7월 LangChain은 Harrison Chase의 2024년 «What is an agent?»가 있던 주소에 Jess Ou가 쓴 새 «What is an AI agent?»를 올렸습니다. 정의는 거의 그의 것과 한 글자 같습니다. 글의 대부분은 그의 글이 다루지 않았던 것, 에이전트를 자동으로 평가하는 파이프라인 전체에 관한 것입니다. 그 파이프라인이 아직 사람이 필요한 곳과 아닌 곳을 솔직히 말합니다.**

## 글이 주장하는 것

Ou의 정의는 Chase의 것과 가깝게 맞닿습니다.

> “An AI agent is a system that uses a large language model to decide the control flow of an application.”

Control flow는 다시, 다음에 어떤 단계가 도는지일 뿐입니다. 이어서 LangChain의 Agent Development Lifecycle — build, test, deploy, monitor — 과, 사람이 매번 실행을 읽지 않고도 에이전트 일을 검사하는 층위 접근을 설명합니다. 온라인 eval은 프로덕션 트레이스(실제 실행의 기록)를 샘플링해 회귀를 찾고, 오프라인 eval은 큐레이션된 데이터셋으로 배포 전 나쁜 변경을 잡으며, «LLM-as-a-judge»는 사람이 미리 정한 기준으로 실행 출력을 채점해 수동 검토가 못 미치는 규모를 감당합니다. 그 파이프라인에 사람이 남는 자리를 분명히 말합니다.

> “For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.”

파이프라인이 아무리 좋아져도 스케일되지 않는 판단에 대한 문장도 있습니다. «Do not outsource judgment you cannot evaluate. If you wouldn’t recognize a correct answer, neither will the agent.» `/reviewing-agent-plans/`가 이미 바로 그 문장 위에 세워져 있으므로 — 이 노트는 그 논의를 반복하지 않습니다. Ou는 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다. Chase의 이름도 부르지 않습니다. 두 글을 잇는 것은 LangChain이 2026년에 그의 2024년 글이 있던 주소에, 거의 같은 정의로 그녀의 글을 올렸다는 점 — 그녀가 아니라 우리가 하는 관찰입니다.

## 우리의 읽기이지 Ou의 것이 아님

Ou의 human-in-the-loop 줄은 특정 행동을 실행 전에 막는 일에 관한 것입니다 — write action을 승인 위해 멈추는 것, Chip Huyen의 read-only/write 구분이 다른 각도에서 가리키는 같은 아이디어 — 이지, 끝난 보고서를 나중에 읽는 일이 아닙니다. 자세히 읽으면 파이프라인의 대부분은 사람을 일상 검사에서 빼내도록 설계되어 있습니다. 넣도록이 아니라. 온라인·오프라인 eval과 LLM-as-a-judge는 팀이 모든 트레이스를 손으로 검토하지 않아도 되게 하려고 있습니다. 글에 대한 비판이 아닙니다 — 그것이 명시된 목표이고, 프로덕션 규모에서는 합리적입니다. 하지만 손으로 하는 검토 — 에이전트가 직접 건네는 계획이나 보고서를 읽는 일 — 은 바로 그 파이프라인이 줄이려 하지, 대체하려 하지 않는 종류의 확인입니다. 판단에 대한 그녀 자신의 문장은 그 축소에 바닥을 둡니다. 옳은 답과 틀린 답을 스스로 구별할 수 없는 곳에서는, 여전히 직접 읽어야 합니다.

## MarsDawn이 돕는 곳, 돕지 않는 곳

MarsDawn은 eval 파이프라인이 아니고 안에 AI 모델도 없습니다 — 트레이스를 채점하지도, LLM-as-a-judge를 돌리지도, 어떤 행동이 멈출 만큼 민감한지 정하지도 않습니다. 그 파이프라인이 아직 사람에게 넘기는 순간, 즉 직접 읽는 일을 위해 만들어졌습니다. 개요 탭(보기 ▸ 사이드바 보기, ⌃⌘S)이 긴 보고서의 제목을 나열하고, 소스와 렌더 미리보기가 나란히(⌘2) Mermaid와 KaTeX를 그리며, 편집 ▸ 참조 복사 (⌥⌘C)와 AI용으로 복사 (⌃⌥⌘C)가 한곳 확인을 에이전트가 움직일 수 있는 정확한 피드백으로 바꿉니다.

## 사용해 보기

MarsDawn은 Mac App Store에 있습니다. 무료 `marsdawn` 명령줄 도구는 오늘부터 쓸 수 있습니다:

```
brew install redtear1115/tap/marsdawn
```

앱 없이 Markdown을 PDF로 내보냅니다.

[명령줄](/ko/cli/) · 구입 전에: [MarsDawn이 하지 않는 일](/ko/limits/)

## 다음

- 그녀의 «outsource judgment» 줄에서 일부 나온 체크리스트 전체: [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/)
- 같은 정의가 2024년에 처음 적힌 곳: [Harrison Chase의 스펙트럼: agentic할수록 더 지켜보고 싶어진다](/ko/reading-notes/harrison-chase-what-is-an-agent/)
- 시리즈로 돌아가기: [편집자의 독서 노트](/ko/reading-notes/)

## 출처

- Jess Ou, “What is an AI agent?,” LangChain, July 31, 2026: [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent) (2026-09-26에 가져와 인용).

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
- [독서 노트: Chip Huyen](https://marsdawn.southern-light.dev/ko/reading-notes/chip-huyen-agents/index.md): Chip Huyen의 2025년 1월 에세이 «Agents»는 에이전트 행동을 read-only와 write로 나눕니다. 그 구분이 계획에서 승인 전에 더 자세히 볼 줄을 빠르게 짚는 방법이 되는 이유.
- [독서 노트: Lilian Weng](https://marsdawn.southern-light.dev/ko/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.
- [독서 노트: Harrison Chase](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
- [독서 노트: Andrew Ng](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰寫的〈What is an AI agent?〉，定義幾乎和 Harrison Chase 2024 年那篇一樣，並描述了一套自動評測 agent 的流程。這套流程哪裡還留給人，哪裡不留。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/langchain-what-is-an-agent/index.md): LangChain 2026 年由 Jess Ou 撰写的《What is an AI agent?》，定义几乎和 Harrison Chase 2024 年那篇一样，并描述了一套自动评测 agent 的流程。这套流程哪里还留给人，哪里不留。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/langchain-what-is-an-agent/index.md): LangChain が 2026 年に Jess Ou 名義で発表した「What is an AI agent?」は、Harrison Chase による 2024 年の定義とほぼ同一で、エージェントを自動評価する一連のパイプラインを説明している。そのパイプラインのどこがまだ人に委ねられ、どこがそうではないか。
- [Deutsch](https://marsdawn.southern-light.dev/de/reading-notes/langchain-what-is-an-agent/index.md): LangChains „What is an AI agent?“ von Jess Ou (2026) greift Harrison Chases Definition von 2024 auf und beschreibt eine Pipeline zur automatischen Bewertung von Agenten. Wo diese Pipeline noch einen Schritt an eine Person übergibt — und wo nicht.
- [Français](https://marsdawn.southern-light.dev/fr/reading-notes/langchain-what-is-an-agent/index.md): Le « What is an AI agent ? » de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.
- [Español](https://marsdawn.southern-light.dev/es/reading-notes/langchain-what-is-an-agent/index.md): El «What is an AI agent?» de LangChain de Jess Ou (2026) recoge la definición de 2024 de Harrison Chase y describe un pipeline para evaluar agentes automáticamente. Dónde ese pipeline todavía entrega un paso a una persona — y dónde no.
