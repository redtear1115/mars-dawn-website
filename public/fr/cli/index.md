# Ligne de commande

L’outil en ligne de commande gratuit `marsdawn` : exportez du Markdown en PDF depuis un shell ou un agent LLM et, si l’app MarsDawn est installée, ouvrez-y des fichiers.

**marsdawn est gratuit et distribué séparément du Mac App Store.** Installez-le avec Homebrew : sur un Mac avec puce Apple, il arrive prêt à l’emploi. `export` fonctionne seul ; `open` nécessite l’app MarsDawn.

Vous appelez marsdawn depuis un agent IA ou un script ? Consultez [marsdawn pour les agents](/fr/cli/agents/) pour la sortie JSON, ses schémas et tous les codes de sortie, ou [le serveur MCP](/fr/cli/mcp/) si votre agent appelle plutôt des outils via MCP.

## Installation

Avec [Homebrew](https://brew.sh) :

```
brew tap redtear1115/tap && brew install marsdawn
```

Vous utilisez un agent de code ? [Ajoutez la skill marsdawn](/fr/cli/skill/) : un seul fichier qui lui apprend à ouvrir ce qu’il a écrit dans MarsDawn pour que vous le relisiez, et à exporter des PDF.

Sur un Mac avec puce Apple, Homebrew installe une copie précompilée en quelques secondes, sans rien d’autre à installer. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure (Swift 6.2). L’outil fonctionne sous macOS 15 ou version ultérieure.

Vous pouvez aussi le compiler à partir des [sources](https://github.com/redtear1115/mars-dawn-kit) avec Swift Package Manager :

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
```

Vérifiez votre version avec `marsdawn --version`.

## Commandes

### marsdawn open

Ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour les relire. L’app doit être installée : sans elle, `marsdawn open` se termine avec le code 3 et indique que MarsDawn n’est pas installé. `export` n’a pas besoin de l’app. L’app est disponible sur le [Mac App Store](https://apps.apple.com/app/id6812925073).

```
marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .
```

- `path:line` : demande à MarsDawn d’aller à cette ligne. Une colonne après, comme dans `notes.md:120:8`, est ignorée. Si un fichier portant le nom complet existe, l’argument désigne ce fichier.
- `--line <n>` : la même chose pour un seul fichier, et le moyen de demander une ligne pour un chemin qui se termine lui-même par deux-points et des chiffres. Exige exactement un fichier.
- Les lignes vont de 1 à 999999999.
- MarsDawn 1.0 ouvre le fichier à cette ligne.
- Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre plutôt que comme un document : `marsdawn open .` affiche le dossier courant. `--folder <path>` fait de même en plus de fichiers. La barre latérale d’une fenêtre affiche un seul dossier, donc en nommer deux est une erreur d’utilisation.
- `--background` : ouvrir sans faire passer MarsDawn au premier plan.
- `--json` : afficher un résultat JSON au lieu de texte.

Les lignes sont arrivées avec marsdawn 0.3.0, les dossiers et `--background` avec la 0.5.1.

### marsdawn export

Convertit un fichier Markdown en PDF paginé, avec le même moteur d’export que celui de MarsDawn. Il n’a pas besoin de l’app MarsDawn. Les images relatives sont résolues par rapport au dossier du fichier d’entrée.

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>` : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension `.pdf`.
- `--theme <dawn|classic|modern|vivid>` : la palette claire du thème de l’aperçu. Par défaut, `$MARSDAWN_THEME`, puis `dawn`.
- `--paper <a4|letter>` : format du papier. Par défaut, `a4`.
- `--allow-remote-images` : charger les images web pendant le rendu. Désactivé par défaut.
- `--force` : remplacer le fichier de sortie s’il existe déjà.
- `--json` : afficher un résultat JSON au lieu de texte.

## La variable $MARSDAWN_THEME

Quand `--theme` n’est pas passé, `export` lit la variable d’environnement `$MARSDAWN_THEME`. Sa valeur doit être `dawn`, `classic`, `modern` ou `vivid` ; toute autre valeur revient à `dawn`. La CLI ne lit pas le réglage de thème de l’app, car lire le conteneur d’une autre app peut déclencher une demande d’autorisation de confidentialité de macOS.

## Écraser des fichiers

`export` refuse de remplacer un fichier de sortie existant, sauf si vous passez `--force`.

## Codes de sortie

| Code | Signification | Que faire |
|---|---|---|
| `0` | succès. | Avec `--json`, lire l’unique ligne JSON sur stdout |
| `2` | entrée introuvable. | Vérifier le chemin et le nom du fichier |
| `3` | MarsDawn n’est pas installé (`open` uniquement). | Installer l’app, ou utiliser `export`, qui n’en a pas besoin |
| `4` | la sortie existe déjà (passez `--force`). | Passer `--force` pour le remplacer, ou `-o` pour écrire ailleurs |
| `5` | échec de l’export. | Lire `message` dans le résultat JSON |
| `6` | ce MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert (`open` uniquement). |  |
| `64` | erreur d’utilisation, notamment une ligne hors limites, `--line` avec plus d’un fichier ou avec un dossier, ou plus d’un dossier. | Corriger l’option ou la valeur ; cette erreur est du texte sur stderr, même avec `--json` |

## Sortie --json

En cas de succès, `marsdawn open --json` affiche `ok`, `opened` (une liste avec le `path` de chaque fichier, plus `line` quand une ligne a été demandée), `app` (le chemin de l’app) et, quand un dossier a été donné, `folder`. `marsdawn export --json` affiche `ok`, `output`, `pages`, `theme`, `paper` et `diagramErrors`. En cas d’échec, les deux affichent `ok`, `error` et `message`.

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu proposés par la communauté pour MarsDawn, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur, sans installation ni git.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [Notes de lecture de la rédaction](https://marsdawn.southern-light.dev/fr/reading-notes/index.md): Six courtes notes sur ce que les gens qui construisent des agents IA avancent réellement — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain et Andrew Ng — et ce que cela signifie pour la personne qui doit lire ce qu’un tel agent rend.
- [Notes de lecture : Anthropic](https://marsdawn.southern-light.dev/fr/reading-notes/anthropic-building-effective-agents/index.md): Le guide d’Anthropic de décembre 2024 pour qui construit des agents sépare workflows et agents et décrit cinq patrons de workflow, dont un où un second appel LLM relit le premier. Ce que cela signifie pour ce qui atterrit dans votre dossier.
- [Notes de lecture : Chip Huyen](https://marsdawn.southern-light.dev/fr/reading-notes/chip-huyen-agents/index.md): L’essai « Agents » de Chip Huyen de janvier 2025 partage les actions d’un agent en read-only et write. Pourquoi cette distinction est un moyen rapide de repérer, dans un plan, la ligne qui mérite un regard plus attentif avant d’approuver.
- [Notes de lecture : Lilian Weng](https://marsdawn.southern-light.dev/fr/reading-notes/lilian-weng-llm-agents/index.md): L’enquête très citée de Lilian Weng en 2023 décrit un agent LLM comme un cerveau plus planification, mémoire et usage d’outils. Ce que chaque partie tend à vous laisser à lire, et la limite qu’elle nomme dans les plans qui ne s’ajustent pas aux surprises.
- [Notes de lecture : Harrison Chase](https://marsdawn.southern-light.dev/fr/reading-notes/harrison-chase-what-is-an-agent/index.md): La définition d’un agent de Harrison Chase en 2024 et son spectre de comportement agentic, et son plaidoyer pour l’observabilité à mesure qu’un système avance dessus — lu du côté de qui lit le fichier qu’il rend.
- [Notes de lecture : LangChain (Jess Ou)](https://marsdawn.southern-light.dev/fr/reading-notes/langchain-what-is-an-agent/index.md): Le « What is an AI agent ? » de LangChain par Jess Ou (2026) reprend la définition 2024 de Harrison Chase et décrit un pipeline pour évaluer les agents automatiquement. Où ce pipeline confie encore une étape à une personne — et où non.
- [Notes de lecture : Andrew Ng](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/index.md): 免費的 marsdawn 命令列工具：在 Mac 上從終端機、腳本或 LLM agent 把 Markdown 匯出成 PDF，並提供 JSON 輸出。用 Homebrew 安裝。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/index.md): 免费的 marsdawn 命令行工具：在 Mac 上从终端、脚本或 LLM agent 把 Markdown 导出成 PDF，并提供 JSON 输出。用 Homebrew 安装。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/index.md): 無料の marsdawn コマンドラインツールで、Mac のシェル、スクリプト、LLM エージェントから Markdown を PDF に書き出せます。JSON 出力にも対応。Homebrew でインストール。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [Español](https://marsdawn.southern-light.dev/es/cli/index.md): La herramienta de línea de comandos gratuita marsdawn para Mac: exporta Markdown a PDF desde una shell, un script o un agente LLM, con salida JSON. Se instala con Homebrew.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
