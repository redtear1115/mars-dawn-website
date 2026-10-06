# Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?

2024년 12월 Anthropic은 AI 에이전트를 만드는 사람들을 위한 가이드 “Building Effective Agents”를 발표했습니다. 요약에는 세 가지 원칙이 나오고, 그중 하나가 투명성입니다. 이 글은 그 원칙의 반대편 끝에 관한 이야기입니다. 에이전트가 단계를 펼쳐 놓으면, 누군가는 그것을 읽어야 합니다.

**투명성은 에이전트가 하는 일이고, 읽기는 여러분이 하는 일입니다. Anthropic은 만드는 사람들에게 에이전트의 계획 단계를 보여 달라고 합니다. 코딩 에이전트를 부리는 대부분의 사람에게 그 단계는 누군가 적절한 순간에 읽어야 하는 Markdown 파일로 도착합니다.**

## 가이드가 말하는 것

Erik S.와 Barry Zhang은 조언을 이렇게 요약합니다.

> “에이전트를 구현할 때 우리는 세 가지 핵심 원칙을 따르려고 한다. 에이전트의 설계를 단순하게 유지하라. 에이전트의 계획 단계를 명시적으로 보여 줌으로써 투명성을 우선하라. 철저한 도구 문서화와 테스트를 통해 에이전트와 컴퓨터 사이의 인터페이스(ACI)를 신중하게 설계하라.”

이는 에이전트를 만드는 사람을 위한 설계 원칙이지, 에이전트를 쓰는 사람을 위한 지침이 아닙니다. 원칙은 단계를 보여 달라고 요구할 뿐, 누가 읽는지는 말하지 않습니다.

같은 글은 에이전트가 작업을 받은 뒤 하는 일을 이렇게 설명합니다. “작업이 명확해지면 에이전트는 독립적으로 계획하고 실행하며, 추가 정보나 판단이 필요할 경우 사람에게 돌아올 수도 있다.” 그리고 “그러면 에이전트는 체크포인트에서 또는 장애물을 만났을 때 사람의 피드백을 받기 위해 멈출 수 있다.” *수도 있다*와 *수 있다*라는 표현을 보세요. 체크포인트는 에이전트가 반드시 가져야 하는 것이 아니라 가질 수 있는 것으로 설명됩니다.

## 확인의 대부분은 여러분이 하지 않습니다

이 부분은 과장하기 쉬우니, 가이드가 실제로 무엇을 앞세우는지 보겠습니다. 에이전트는 바깥 세계에 비추어 스스로를 확인합니다. “실행 중에는 에이전트가 진행 상황을 평가하기 위해 각 단계에서 환경으로부터 ‘실측 정보(ground truth)’(도구 호출 결과나 코드 실행 결과 등)를 얻는 것이 매우 중요하다.” 이 문장에서 실측 정보란 테스트 결과와 도구 출력이지, 사람이 아닙니다.

가이드는 위험에 대해서도 직설적입니다. “에이전트의 자율적인 특성은 더 높은 비용과 오류가 누적될 가능성을 뜻한다.” 그에 대한 답은 샌드박스 환경에서의 광범위한 테스트와 안전장치입니다. “더 꼼꼼히 읽으라”고는 하지 않습니다.

사람은 뒤쪽, 코딩 에이전트에 관한 부록에서 등장합니다. “하지만 자동화된 테스트가 기능 검증을 돕는다 해도, 해결책이 더 넓은 시스템 요구 사항에 부합하는지 확인하려면 사람의 검토가 여전히 매우 중요하다.” 이 문장은 코드에 관한 것입니다. 하지만 이 문장이 가리키는 빈틈은 어떤 에이전트에서든 익숙합니다. 테스트는 무언가가 동작한다는 것을 알려 줄 수는 있어도, 그것이 여러분이 의도한 것인지는 알려 주지 못합니다.

## 단계는 어디로 가는가

**여기서부터는 Anthropic이 아니라 우리의 해석입니다.**

코딩 에이전트를 매일 쓴다면, 에이전트의 계획 단계는 대개 대시보드에 나타나지 않습니다. 파일로 나타납니다. `plan.md`, 체크박스가 달린 작업 목록, 에이전트가 계속 고쳐 쓰는 진행 파일, 마지막의 요약. 여러분 쪽에서 투명성이란 읽을 것이 늘어난다는 뜻입니다.

단계를 보여 주는 것은 에이전트의 몫입니다. 나머지 절반은 중요한 순간에 그것을 읽는 사람입니다. 마이그레이션이 실행되기 전, 브랜치가 병합되기 전, ‘완료’를 받아들이기 전. 아무도 열어 보지 않는 600줄짜리 파일에 모든 것을 펼쳐 놓는 에이전트는 서류상으로는 투명하지만 실제로는 감독받지 않는 셈입니다.

Harrison Chase도 2024년에 비슷한 이야기를 했습니다. 문서가 아니라 에이전트 프레임워크가 어떻게 동작해야 하는지에 관한 글이었습니다. “정확히 어떤 단계를 밟을지 미리 알 수 없을 수 있으므로, 내부에서 무슨 일이 일어나는지 관찰할 수 있기를 원하게 될 것이다.” 그는 에이전트를 만드는 사람을 위한 도구를 말하고 있었습니다. 에이전트를 부리는 사람이 여러분이라면, 에이전트가 계속 써 나가는 평범한 파일이 여러분이 지켜볼 수 있는 부분인 경우가 많습니다.

이 저자들 중 누구도 MarsDawn을 언급하지 않으며, MarsDawn이나 다른 Markdown 도구를 추천하지도 않습니다.

## 그 읽기가 보기보다 어려운 이유

파일은 길고, 중요한 내용은 위쪽에 있는 경우가 드뭅니다. 변경 사항을 설명하는 다이어그램은 그림이 아니라 Mermaid 소스입니다(그려진 모습을 보는 방법은 [Mac에서 Markdown 파일을 보는 방법](/ko/view-markdown-on-mac/)에 있습니다). 여러분이 절반쯤 읽는 동안 에이전트가 파일을 고쳐 쓸 수도 있습니다. 파일이 하나가 아닌 경우가 많고, 때로는 서로 다른 브랜치나 워크트리에 있습니다. 그리고 문제를 발견해도 “캐시 부분이 좀 이상해”라고 하면 에이전트는 짐작할 수밖에 없습니다. 더 자세한 내용은 [에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/)에 있습니다.

## MarsDawn이 맞는 곳과 맞지 않는 곳

MarsDawn은 이 읽기를 위한 Mac 앱입니다. 에이전트를 더 투명하게 만들지는 않으며, 안에 AI 모델도 없습니다. 계획을 요약하거나 맞는지 알려 주지 않습니다. 하는 일은 다음과 같습니다.

- **긴 파일:** 보기 ▸ 사이드바 보기(⌃⌘S)를 선택하면 제목이 나열된 개요 탭이 열립니다. 하나를 클릭하면 그곳으로 이동합니다.
- **다이어그램과 수식:** 소스와 렌더링된 페이지가 나란히 놓이고(⌘2) 함께 스크롤되며, Mermaid와 KaTeX가 그려집니다. 다이어그램에 오류가 있으면 미리보기에 소스와 그 아래 오류가 표시됩니다.
- **읽는 동안 고쳐 쓰일 때:** 에이전트가 파일을 고쳐 쓰면 MarsDawn이 다시 불러오고 읽던 위치를 유지합니다. 여러분이 저장하지 않은 편집이 없는 한 그렇습니다.
- **여러 파일:** 파일 ▸ 폴더 열기…(⇧⌘O)로 에이전트의 폴더를 여세요. 새 파일은 약 1초 안에 파일 탭에 나타나고, git 체크아웃이라면 헤더에 브랜치나 워크트리 이름이 표시됩니다.
- **줄 가리키기:** 편집 ▸ 참조 복사(⌥⌘C)는 현재 위치를 `docs/plan.md:42` 형식으로 복사하고, AI용으로 복사(⌃⌥⌘C)는 그 아래에 선택한 텍스트를 덧붙여 에이전트와의 채팅에 바로 붙여 넣을 수 있게 합니다.

읽는 것은 여전히 여러분입니다. MarsDawn은 그동안 길고 계속 바뀌는 파일을 읽기 좋게 유지합니다.

## 사용해 보기

MarsDawn은 [Mac App Store](https://apps.apple.com/app/id6812925073)에 있습니다. 무료 `marsdawn` 명령줄 도구도 있습니다.

```
brew install redtear1115/tap/marsdawn
```

앱 없이 Markdown을 PDF로 내보냅니다.

[명령줄](/ko/cli/) · 구입 전에 알아 두세요: [MarsDawn이 하지 않는 일](/ko/limits/)

## 다음

- 에이전트의 결과물이 읽기 어려운 이유와 체크리스트: [에이전트가 돌려준 결과 읽기](/ko/reading-agent-output/).
- 체크리스트를 예시와 함께 단계별로: [에이전트의 계획을 5분 만에 검토하기](/ko/reviewing-agent-plans/).
- 여러 종류의 에이전트가 건네는 문서: [네 가지 에이전트 설계 패턴과 각각이 건네는 문서](/ko/agent-design-patterns/).
- AI의 결과물을 왜 읽어야 하는지 짧게: [AI의 결과물에 여전히 사람 독자가 필요한 이유](/ko/reviewing-ai-output/).

## 출처

- Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (2026-09-26 기준 온라인 버전에서 인용. 현재 이 글에는 설명된 도구 중 상당수가 2024년 12월 이후 바뀌었다는 안내가 붙어 있습니다.)
- Harrison Chase, “What is an agent?”, LangChain, 2024년 6월 28일, 보관된 사본: [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (원래 주소에는 현재 2026년의 다른 글이 있습니다.)

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트의 작업을 이끄는 사람을 위한 Markdown. 실시간 미리보기, Mermaid 다이어그램, PDF 내보내기를 갖춘 Mac 네이티브 편집기입니다. Mac App Store에서 구입할 수 있습니다.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 가져올 수 있는 테마를 더 늘리고, 직접 만든 테마를 공유하는 갤러리도 계획하고 있습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [Deutsch](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Français](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Español](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
