# 명령줄

무료 `marsdawn` 명령줄 도구입니다. 셸이나 LLM 에이전트에서 Markdown을 PDF로 내보내고, MarsDawn 앱이 설치되어 있으면 앱에서 파일을 열 수 있습니다.

**marsdawn은 무료이며 Mac App Store와 별도로 배포됩니다.** Homebrew로 설치하세요. Apple 실리콘 Mac에서는 바로 실행할 수 있는 상태로 설치됩니다. `export`는 단독으로 작동하고, `open`은 MarsDawn 앱이 필요합니다.

AI 에이전트나 스크립트에서 marsdawn을 호출하나요? JSON 출력과 스키마, 모든 종료 코드는 [에이전트를 위한 marsdawn](/ko/cli/agents/)에서, 에이전트가 MCP로 도구를 호출한다면 [MCP 서버](/ko/cli/mcp/)에서 확인하세요.

## 설치

[Homebrew](https://brew.sh)를 사용하는 경우:

```
brew tap redtear1115/tap && brew install marsdawn
```

코딩 에이전트를 쓰고 있나요? [marsdawn 스킬을 추가하세요](/ko/cli/skill/). 파일 하나로, 에이전트가 자기가 쓴 것을 MarsDawn에서 열어 검토를 받고 PDF로 내보내는 법을 익힙니다.

Apple 실리콘 Mac에서는 Homebrew가 미리 빌드된 버전을 몇 초 만에 설치하며, 따로 설치할 것이 없습니다. Intel Mac에서는 대신 소스에서 marsdawn을 빌드하므로 몇 분이 걸리고 Xcode 26 이상(Swift 6.2)이 필요합니다. 이 도구는 macOS 15 이상에서 실행됩니다.

또는 Swift Package Manager로 [소스](https://github.com/redtear1115/mars-dawn-kit)에서 빌드하세요.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

설치된 버전은 `marsdawn --version`으로 확인할 수 있습니다.

## 명령

### marsdawn open

Markdown 파일 하나 이상을 MarsDawn 앱에서 열어 검토할 수 있게 합니다. 앱이 설치되어 있어야 합니다. 앱이 없으면 `marsdawn open`은 코드 3으로 종료하며 MarsDawn이 설치되어 있지 않다고 알립니다. `export`는 앱이 필요 없습니다. 앱은 [Mac App Store](https://apps.apple.com/app/id6812925073)에 있습니다.

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .
```

- `path:line`: MarsDawn에 해당 줄로 이동하도록 요청합니다. `notes.md:120:8`처럼 뒤에 붙은 열 번호는 무시됩니다. 전체 이름 그대로의 파일이 있으면 인수는 그 파일을 가리킵니다.
- `--line <n>`: 파일 하나에 대해 같은 일을 하며, 경로 자체가 콜론과 숫자로 끝날 때 줄을 지정하는 방법입니다. 파일이 정확히 하나여야 합니다.
- 줄 번호는 1부터 999999999까지입니다.
- MarsDawn 1.0은 해당 줄에서 파일을 엽니다.
- 폴더를 인수로 주면 문서가 아니라 윈도우의 사이드바에 열립니다. `marsdawn open .`은 현재 폴더를 보여줍니다. `--folder <path>`는 파일과 함께 같은 일을 합니다. 윈도우의 사이드바는 폴더 하나만 보여주므로, 두 개를 지정하면 사용법 오류입니다.
- `--background`: MarsDawn을 앞으로 가져오지 않고 엽니다.
- `--json`: 텍스트 대신 JSON 결과를 출력합니다.

줄 지정은 marsdawn 0.3.0에서, 폴더와 `--background`는 0.5.1에서 추가되었습니다.

### marsdawn export

MarsDawn 자체의 PDF 내보내기와 같은 엔진으로 Markdown 파일을 페이지가 나뉜 PDF로 렌더링합니다. MarsDawn 앱은 필요 없습니다. 상대 경로의 이미지는 입력 파일이 있는 폴더를 기준으로 찾습니다.

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`: PDF를 쓸 위치입니다. 기본값은 입력 경로에 `.pdf` 확장자를 붙인 것입니다.
- `--theme <dawn|classic|modern|vivid>`: 미리보기 테마의 라이트 팔레트입니다. 기본값은 `$MARSDAWN_THEME`, 그다음 `dawn`입니다.
- `--paper <a4|letter>`: 용지 크기입니다. 기본값은 `a4`입니다.
- `--allow-remote-images`: 렌더링하는 동안 웹 이미지를 불러옵니다. 기본값은 꺼짐입니다.
- `--force`: 출력 파일이 이미 있으면 바꿉니다.
- `--json`: 텍스트 대신 JSON 결과를 출력합니다.

## $MARSDAWN_THEME 변수

`--theme`를 주지 않으면 `export`는 `$MARSDAWN_THEME` 환경 변수를 읽습니다. 값은 `dawn`, `classic`, `modern`, `vivid` 중 하나여야 하며, 그 밖의 값은 `dawn`으로 처리됩니다. 다른 앱의 컨테이너를 읽으면 macOS 개인정보 보호 확인 창이 뜰 수 있기 때문에, CLI는 앱 자체의 테마 설정을 읽지 않습니다.

## 파일 덮어쓰기

`export`는 `--force`를 주지 않는 한 기존 출력 파일을 바꾸지 않습니다.

## 종료 코드

| 코드 | 의미 | 해결 방법 |
|---|---|---|
| `0` | 성공. | `--json`을 줬다면 stdout의 JSON 한 줄을 읽으세요 |
| `2` | 입력을 찾을 수 없음. | 경로와 파일 이름을 확인하세요 |
| `3` | MarsDawn이 설치되어 있지 않음(`open`만 해당). | 앱을 설치하거나, 앱이 필요 없는 `export`를 쓰세요 |
| `4` | 출력 파일이 이미 있음(`--force`를 주세요). | `--force`로 바꾸거나, `-o`로 다른 곳에 쓰세요 |
| `5` | 내보내기 실패. | JSON 결과의 `message`를 읽으세요 |
| `6` | 이 MarsDawn은 폴더를 보여줄 수 없어 아무것도 열지 않았음(`open`만 해당). |  |
| `64` | 사용법 오류. 범위를 벗어난 줄 번호, 파일 둘 이상이나 폴더와 함께 쓴 `--line`, 폴더 둘 이상 등이 포함됩니다. | 옵션이나 값을 고치세요. 이 오류는 `--json`을 줘도 stderr에 텍스트로 나옵니다 |

## --json 출력

성공하면 `marsdawn open --json`은 `ok`, `opened`(각 파일의 `path`와, 줄을 요청한 경우 `line`이 담긴 목록), `app`(앱 경로), 그리고 폴더를 준 경우 `folder`를 출력합니다. `marsdawn export --json`은 `ok`, `output`, `pages`, `theme`, `paper`, `diagramErrors`를 출력합니다. 실패하면 둘 다 `ok`, `error`, `message`를 출력합니다.

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
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [Français](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [Español](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
