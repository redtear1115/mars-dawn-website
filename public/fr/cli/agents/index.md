# marsdawn pour les agents

Une référence pour les agents IA et les scripts qui appellent l’outil en ligne de commande `marsdawn`. Chaque exemple de cette page a été exécuté avec l’outil compilé à partir des sources actuelles.

**Pour convertir un fichier Markdown en PDF, lancez `marsdawn export notes.md --json` et lisez un objet JSON sur stdout.** Les diagrammes Mermaid et le code coloré sont rendus de la même façon que dans l’app MarsDawn. `export` n’a pas besoin de l’app ; `open`, si.

## Ce qu’il fait

- `export` fait le rendu d’un fichier Markdown en un PDF paginé, avec le même moteur d’export que l’app MarsDawn. Aucune fenêtre ne s’ouvre.
- `open` ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour qu’une personne les relise ; il peut indiquer la ligne à laquelle chaque fichier doit s’ouvrir et afficher un dossier dans la barre latérale de la fenêtre.

## Ce qu’il ne fait pas

- Il ne lit pas le Markdown depuis stdin. Passez un chemin de fichier.
- Il n’écrit pas le PDF sur stdout. Le PDF va toujours dans un fichier ; stdout ne contient que le résultat.
- Il ne remplace pas un fichier existant, sauf si vous passez `--force`.
- Il ne charge pas d’images depuis le web, sauf si vous passez `--allow-remote-images`, et uniquement en https.
- `open` ne fonctionne pas sans l’app MarsDawn installée ; il se termine avec le code 3. `export` n’a pas besoin de l’app. L’app est sur le [Mac App Store](https://apps.apple.com/app/id6812925073).
- MarsDawn 1.0 ouvre le fichier à la ligne indiquée par `open`.
- Il ne fonctionne que sous macOS.

## export

```
marsdawn export notes.md --json
```

Écrit `notes.pdf` à côté de `notes.md`. Options :

- `-o, --output <path>` : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension `.pdf`.
- `--theme <dawn|classic|modern|vivid>` : la palette claire du thème. Par défaut `$MARSDAWN_THEME`, sinon `dawn`.
- `--paper <a4|letter>` : format du papier. Par défaut `a4`.
- `--allow-remote-images` : charge les images https du web pendant le rendu.
- `--force` : remplace le fichier de sortie s’il existe.
- `--json` : affiche un objet JSON sur stdout au lieu de texte.

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

Succès, code de sortie 0 :

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output` : chemin absolu du PDF écrit.
- `pages` : nombre de pages.
- `theme` et `paper` : les valeurs utilisées.
- `diagramErrors` : un message par diagramme Mermaid dont le rendu a échoué. Le PDF est tout de même écrit.

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json
```

- `path:line` indique la ligne à laquelle s’ouvrir. Une colonne après, comme dans `notes.md:120:8`, est ignorée. Un argument qui désigne un fichier existant est toujours ce nom de fichier entier : un fichier nommé `weird:12` s’ouvre donc tel quel.
- `--line <n>` indique la ligne pour un seul fichier, y compris un chemin qui se termine lui-même par deux-points et des chiffres. Il faut exactement un fichier.
- Les lignes vont de 1 à 999999999. Toute autre valeur est une erreur d’utilisation.
- Les lignes ont été ajoutées dans marsdawn 0.3.0. MarsDawn 1.0 ouvre le fichier à cette ligne.
- Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre et non comme document : `marsdawn open .` affiche donc le dossier courant ; `--folder <path>` fait de même en plus des fichiers. La barre latérale d’une fenêtre affiche un seul dossier : en indiquer deux est une erreur d’utilisation, tout comme utiliser `--folder` deux fois, même pour le même dossier ; le même dossier redonné en argument compte une seule fois. `--line` avec un dossier est une erreur d’utilisation, puisqu’un dossier n’a pas de ligne. Il n’y a pas de `-a` : le passer est une erreur d’utilisation qui renvoie à `--folder`.
- `--background` ouvre sans faire passer MarsDawn au premier plan, pour un agent qui ouvre des fichiers pendant que la personne travaille ailleurs. Le JSON est le même dans les deux cas.
- Les dossiers et `--background` ont été ajoutés dans marsdawn 0.5.1.

Succès, code de sortie 0 :

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened` : un objet par fichier, dans l’ordre donné. `path` est le chemin absolu du fichier ; `line` n’apparaît que si une ligne a été demandée.
- `app` : chemin de l’app MarsDawn qui les a ouverts.

Avec un dossier (marsdawn 0.5.1 et versions ultérieures), code de sortie 0 :

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/project","requested":true},"ok":true,"opened":[{"path":"/path/to/project/notes.md"}]}
```

- `folder` : présent seulement si un dossier a été donné. `path` est son chemin absolu. `requested` vaut toujours `true` : marsdawn a demandé à MarsDawn d’afficher le dossier, mais ne peut pas savoir si la barre latérale l’affiche, car l’app peut d’abord demander l’accès à la personne. Signalez-le comme demandé, pas comme fait.
- `opened` est vide si seul un dossier a été donné.

marsdawn 0.2.x affichait `opened` sous forme de liste de chemins. Vérifiez `marsdawn --version` si vous devez gérer les deux.

## Ouvrir les fichiers à mesure que Claude Code les modifie

Un [hook Claude Code](https://code.claude.com/docs/en/hooks) facultatif : après que Claude a écrit ou modifié un fichier Markdown, il ouvre ce fichier dans MarsDawn en arrière-plan, une fois par fichier et par session. Il est désactivé tant que vous ne l’ajoutez pas, projet par projet, car une fenêtre que vous n’avez pas demandée détourne l’attention. Il exécute une commande shell et ne coûte aucun token de modèle.

Il nécessite marsdawn 0.5.1 ou version ultérieure, pour `--background`, ainsi que l’app MarsDawn.

Enregistrez ceci sous `.claude/hooks/marsdawn-open.sh` dans votre projet, et rendez-le exécutable avec `chmod +x` :

```
#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2>/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2>/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || { [ -x /opt/homebrew/bin/marsdawn ] && echo /opt/homebrew/bin/marsdawn; }) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${TMPDIR:-/tmp}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2>/dev/null && exit 0
echo "$file" >> "$seen"

"$marsdawn" open --background "$file" >/dev/null 2>&1 || true
exit 0
```

Ajoutez ensuite le hook à `.claude/settings.json` dans le projet, ou à `.claude/settings.local.json` pour le garder pour vous :

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/marsdawn-open.sh" }
        ]
      }
    ]
  }
}
```

- Il s’exécute après les outils Write et Edit de Claude. Les fichiers qui ne se terminent pas par `.md` ou `.markdown` sont ignorés.
- Chaque fichier s’ouvre une fois par session Claude Code, quel que soit le nombre de modifications. La liste se trouve dans `$TMPDIR/marsdawn-hook/`, un fichier par session : une nouvelle session rouvre donc le fichier.
- `--background` empêche MarsDawn de passer au premier plan : la fenêtre dans laquelle vous travailliez garde le focus.
- Il ne gêne jamais Claude. Chaque chemin se termine avec 0, et si marsdawn ou l’app MarsDawn n’est pas installé, rien ne se passe.
- Il lit l’entrée du hook avec `/usr/bin/jq`, fourni avec macOS 26, la version dont l’app MarsDawn a besoin.
- Pour le désactiver, supprimez l’entrée du fichier de réglages.

## Échecs

Avec `--json`, un échec affiche un objet JSON sur stdout et se termine avec son code :

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found` : l’entrée n’existe pas, est un dossier ou n’est pas du texte UTF-8 ; ou un chemin `--folder` n’existe pas ou n’est pas un dossier.
- `3`, `app_not_installed` : MarsDawn n’est pas installé. Seul `open` renvoie ce code.
- `4`, `output_exists` : le fichier de sortie existe. Passez `--force`.
- `5`, `export_failed` : l’export lui-même a échoué.
- `6`, `app_cannot_open_folders` : cette version de MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert. Seul `open` renvoie ce code.
- `64` : erreur d’utilisation, comme une option inconnue, une valeur non valide, une ligne hors limites, `--line` avec plus d’un fichier ou avec un dossier, plus d’un dossier, ou `-a`. Celle-ci s’affiche en texte sur stderr, même avec `--json`.

## Schémas JSON

JSON Schema (draft 2020-12) pour chaque résultat `--json` :

- [export.v1.json](/schemas/cli/export.v1.json): succès de export
- [open.v3.json](/schemas/cli/open.v3.json): succès de open, marsdawn 0.5.1 et versions ultérieures, y compris un dossier affiché dans la barre latérale
- [error.v2.json](/schemas/cli/error.v2.json): échec, pour les deux commandes, marsdawn 0.5.2 et versions ultérieures
- [open.v2.json](/schemas/cli/open.v2.json): succès de open, marsdawn 0.3.0 à 0.5.0
- [open.v1.json](/schemas/cli/open.v1.json): succès de open, marsdawn 0.2.x, où `opened` était une liste de chemins
- [error.v1.json](/schemas/cli/error.v1.json): échec, pour les deux commandes, marsdawn 0.5.1 et versions antérieures

## Variables d’environnement

- `MARSDAWN_THEME` : le thème qu’utilise `export` quand `--theme` n’est pas passé. Une valeur inconnue revient à `dawn` sans erreur.

## Configuration requise

- L’outil fonctionne sous macOS 15 ou version ultérieure. Sur puce Apple, Homebrew installe un bottle précompilé et rien d’autre n’est nécessaire. Le compiler vous-même, sur un Mac Intel ou à partir des sources, nécessite Swift 6.2 ou version ultérieure, fourni avec Xcode 26 ou version ultérieure.
- L’app MarsDawn nécessite macOS 26 ou version ultérieure.

## Installation

Avec Homebrew. Sur puce Apple, il installe un bottle précompilé en quelques secondes, sans Xcode. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

Ou compilez-le à partir [des sources](https://github.com/redtear1115/mars-dawn-kit). La première compilation récupère les dépendances et compile, ce qui prend aussi quelques minutes.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` affiche le numéro de version, par exemple `0.3.0`, et se termine avec le code 0.

## Pour aller plus loin

- Une compétence en un seul fichier pour les agents qui lisent des instructions plutôt qu’un shell : [la compétence marsdawn](/fr/cli/skill/).
- Un serveur MCP qui enveloppe ce même `export` : [marsdawn-mcp](/fr/cli/mcp/).
- Pourquoi ce résultat JSON reste économique pour le contexte de l’agent : [une relecture économe en tokens](/fr/token-efficient-review/).

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
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
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
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Español](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
