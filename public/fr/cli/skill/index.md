# Laissez votre agent vous montrer ce qu’il a écrit, et produire le PDF.

Cette compétence tient en un fichier Markdown. Elle apprend à un agent de code à ouvrir dans MarsDawn un document qu’il a écrit pour que vous le relisiez, et à installer `marsdawn`, vérifier qu’il fonctionne, exporter un document en PDF et lire le résultat.

**Un seul fichier Markdown, dans `~/.claude/skills/marsdawn/SKILL.md`.** Avec lui, votre agent installe `marsdawn`, exporte en PDF et lit le résultat JSON, et il demande toujours avant d’exécuter quoi que ce soit.

## L’installer dans Claude Code

L’outil en ligne de commande `marsdawn` écrit la skill pour vous, et le fichier qu’il écrit correspond à la version de `marsdawn` que vous avez installée. Si vous n’avez pas encore `marsdawn`, installez-le avec [Homebrew](https://brew.sh) :

```
brew install redtear1115/tap/marsdawn
```

Installez ensuite la skill :

```
marsdawn skill --install
```

Cela écrit `~/.claude/skills/marsdawn/SKILL.md`, en créant le dossier s’il n’existe pas. Comme le fichier vient de votre copie de `marsdawn`, il ne décrit jamais une option que votre copie n’a pas.

Claude Code la charge quand une tâche demande un PDF, ou quand il a écrit ou révisé un document Markdown que vous allez lire, et vous pouvez la lancer vous-même avec `/marsdawn`. Si vous voulez la lire d’abord, c’est [un fichier court](/cli/skill/SKILL.md).

## Après une mise à jour de marsdawn

Homebrew met à jour `marsdawn` mais laisse la skill où elle était, elle reste donc à l’ancienne version tant que vous ne la rafraîchissez pas :

```
marsdawn skill --install --force
```

`--force` remplace le `SKILL.md` existant, y compris les modifications que vous y avez faites. Sans `--force`, si un `SKILL.md` différent est déjà là, `marsdawn` n’y touche pas, vous dit qu’il diffère et se termine avec le code 64 (`skill_differs`). Si le fichier est déjà le bon, rien ne change.

## Pour d’autres agents

Ajoutez `--dir` avec le dossier où votre agent range ses skills, et `marsdawn` y écrit `SKILL.md` à la place :

```
marsdawn skill --install --dir <path>
```

Le fichier est du Markdown brut, des instructions et des commandes : un agent qui charge des fichiers d’instructions peut l’utiliser tel quel.

## Sans Homebrew ni l’outil en ligne de commande

Si vous ne pouvez pas installer `marsdawn` d’abord, téléchargez plutôt le fichier :

```
mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md
```

Cela récupère la dernière skill de ce site, qui peut être en avance sur un `marsdawn` plus ancien. Une fois l’outil installé, `marsdawn skill --install --force` la remplace par celle qui correspond. Vous pouvez aussi indiquer l’URL à un agent, ou coller le fichier.

## Ce qu’elle enseigne

- Installer `marsdawn` avec Homebrew s’il manque, puis le vérifier avec `marsdawn --version` au lieu de supposer une version.
- Exporter avec `marsdawn export … --json` et lire le résultat : où est allé le PDF, combien de pages il compte, et quel diagramme Mermaid n’a pas pu être rendu.
- Distinguer les échecs par leur code de sortie : fichier introuvable, PDF déjà présent, export échoué, option incorrecte.
- Ouvrir un document qu’il a écrit avec `marsdawn open file.md:line`, sur sa première modification, et une seule fois : les modifications suivantes apparaissent d’elles-mêmes dans la fenêtre ouverte.
- Si l’app MarsDawn n’est pas installée, le dire une fois et continuer, sans réessayer. Ne jamais utiliser `open` pour produire un PDF.
- Avec `--folder` (marsdawn 0.5.1 et versions ultérieures), signaler le dossier comme demandé, pas comme affiché : c’est l’app qui décide, et rien ne le confirme.

## Ce qu’elle ne fait pas

- Elle ne s’accorde pas elle-même la permission d’exécuter quoi que ce soit. Votre agent demande toujours avant d’installer `marsdawn` ou de le lancer, comme pour n’importe quelle autre commande.
- Elle n’envoie vos documents nulle part. `marsdawn` fait le rendu sur votre Mac et laisse de côté les images du web, sauf si vous passez `--allow-remote-images`.

Le contrat complet, chaque champ et chaque code, se trouve dans [marsdawn pour les agents](/fr/cli/agents/). Pour un agent qui appelle des outils via MCP plutôt que de lire un fichier de compétence, il existe aussi [un serveur MCP](/fr/cli/mcp/).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Ouvrir un fichier .md sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Comment ouvrir un fichier .md sur Mac : double-clic, app par défaut, coup d’œil dans le Finder. Pour les .md écrits par un agent IA, lisez-les rendus dans MarsDawn.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Voyez les diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte : 14 jours gratuits, puis 4,99 USD une seule fois. Comparaison ligne par ligne, avec sources.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. Créez votre propre thème dans le navigateur, et parcourez la galerie communautaire.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Créer un thème avec votre agent](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
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
- [English](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/skill/index.md): 一個檔案，讓寫程式的 agent 把自己寫的 Markdown 在 MarsDawn 裡打開給你審閱，也學會安裝 marsdawn、把 Markdown 匯出成 PDF，並讀懂 JSON 結果。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/skill/index.md): 一个文件，让写程序的 agent 把自己写的 Markdown 在 MarsDawn 里打开给你审阅，也学会安装 marsdawn、把 Markdown 导出成 PDF，并读懂 JSON 结果。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/skill/index.md): コーディングエージェントが読み込む1つのファイルです。自分が書いた Markdown を MarsDawn で開いてあなたに確認してもらう方法と、marsdawn のインストール、Markdown の PDF への書き出し、JSON の結果の読み取りを教えます。
- [Deutsch](https://marsdawn.southern-light.dev/de/cli/skill/index.md): Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.
- [Español](https://marsdawn.southern-light.dev/es/cli/skill/index.md): Un archivo que tu agente de programación carga para abrir en MarsDawn el Markdown que escribió, para que lo revises, y para instalar marsdawn, exportar Markdown a PDF y leer el resultado JSON.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
