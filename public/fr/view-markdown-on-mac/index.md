# Comment ouvrir un fichier .md sur Mac.

Double-cliquez dessus. Si votre Mac l’ouvre dans un éditeur de texte et que vous voyez `#` et `**` au lieu de titres et de gras, le fichier n’a rien : un fichier `.md` est du texte brut, et cet éditeur affiche le texte tel quel. Ouvrez-le dans une app qui fait le rendu du Markdown, comme MarsDawn, et faites-en l’app par défaut pour que tous les fichiers `.md` s’y ouvrent.

Un fichier `.md` est du texte brut. Les titres, les mots en gras, les tableaux et les diagrammes y sont écrits sous forme de marques : `#` pour un titre, `**` autour du gras, des barres verticales pour un tableau, un bloc de code `mermaid` pour un diagramme. Ouvrez-le dans un éditeur de texte brut et vous lisez les marques. Pour lire la page telle que l’auteur l’a voulue, il faut qu’un outil en fasse le rendu.

## Ouvrir un fichier .md sur votre Mac

1. **Double-cliquez sur le fichier.** Il s’ouvre dans l’app que votre Mac a définie pour les fichiers `.md`. Sans app Markdown, c’est souvent un éditeur de texte brut, qui affiche les marques au lieu de la page.
2. **Choisissez l’app vous-même.** Faites un clic en maintenant la touche Contrôle enfoncée sur le fichier et choisissez « Ouvrir avec », puis l’app. Ou choisissez « Fichier ▸ Lire les informations » (⌘I), choisissez une app sous « Ouvrir avec : », puis cliquez sur « Tout modifier… » pour que tous les fichiers de ce type s’y ouvrent. MarsDawn ouvre les fichiers `.md`, `.markdown`, `.mdown`, `.mkd` et `.mkdn`.
3. **Afficher sans ouvrir.** Sélectionnez le fichier dans le Finder et appuyez sur la barre d’espace. Avec MarsDawn installé, Coup d’œil affiche la page rendue, diagrammes compris.

## Le lire dans MarsDawn

MarsDawn est un éditeur Markdown pour Mac. Il se télécharge gratuitement sur le Mac App Store : essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte. macOS 26 ou version ultérieure est requis.

[Télécharger MarsDawn gratuitement sur le Mac App Store](https://apps.apple.com/app/id6812925073)

Ouvrez un fichier `.md` et lisez la page rendue à côté de la source :

- L’aperçu se met à jour pendant la saisie, et les deux volets défilent ensemble.
- Les organigrammes et les diagrammes de séquence [Mermaid](/fr/mermaid-preview-mac/) sont dessinés dans l’aperçu, et les blocs de code sont colorés.
- Quand vous voulez modifier quelque chose, la source est juste là. MarsDawn est un éditeur, pas seulement une visionneuse.

Si un agent IA a rédigé le fichier, c’est la boucle pour laquelle MarsDawn est conçu : l’agent écrit, vous lisez le rendu, et il révise. Consultez [la page d’accueil](/fr/), ainsi que [marsdawn pour les agents](/fr/cli/agents/) pour laisser un agent ouvrir des fichiers à votre place. Pour comprendre pourquoi cette lecture compte et comment relire un plan, consultez [Lire ce que votre agent vous rend](/fr/reading-agent-output/) et [Relire le plan d’un agent en cinq minutes](/fr/reviewing-agent-plans/).

## Sans l’app : en faire un PDF

L’outil en ligne de commande gratuit `marsdawn` fait le rendu d’un fichier Markdown en PDF, que n’importe quel Mac peut ouvrir. Les tableaux, les formules, les diagrammes Mermaid et le code coloré sont rendus, et rien d’autre n’est nécessaire, pas même l’app MarsDawn.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

`export` écrit `notes.pdf` à côté du fichier Markdown, et `open` l’affiche dans votre lecteur PDF. macOS 15 ou version ultérieure est requis. Le pas-à-pas, avec une vraie page exportée, se trouve sur [Markdown en PDF](/fr/markdown-to-pdf/).

## Questions

### Qu’est-ce qu’un fichier .md ?

Un fichier `.md` est un fichier de texte brut écrit en Markdown, une façon de mettre en forme du texte avec des caractères simples : `#` pour un titre, `**` autour du gras, une barre verticale pour une cellule de tableau. Les extensions `.markdown`, `.mdown`, `.mkd` et `.mkdn` veulent dire la même chose. Les développeurs s’en servent pour les README et la documentation, et les agents IA rendent souvent leurs plans et leurs rapports sous forme de fichiers `.md`.

### Pourquoi mon fichier .md s’ouvre-t-il en texte brut, avec des # et des ** ?

Parce que c’est du texte brut, et qu’un éditeur de texte brut l’affiche tel quel. Le fichier n’a aucun problème. Pour voir les titres, le gras, les tableaux et les diagrammes, ouvrez-le dans une app qui fait le rendu du Markdown. Dans MarsDawn, la page rendue se trouve à côté de la source.

### Pourquoi s’ouvre-t-il avec des caractères illisibles ?

Des caractères illisibles signifient généralement que le fichier a été enregistré dans un encodage autre que l’UTF-8 et que l’app qui l’a ouvert s’est trompée. La solution est d’enregistrer une copie en UTF-8. MarsDawn ouvre en lecture seule un fichier de texte brut qui n’est pas en UTF-8, indique dans une barre en haut de la fenêtre l’encodage dans lequel il l’a lu, et propose là « Enregistrer en UTF-8… » ou « Fichier ▸ Enregistrer sous… » (⌥⇧⌘S) pour écrire une copie en UTF-8 que vous pouvez modifier.

### Puis-je transformer un fichier .md en PDF ?

Oui. Dans MarsDawn, choisissez « Fichier ▸ Exporter au format PDF… » (⌥⌘E) ou « Fichier ▸ Imprimer… » ; les pages sont paginées, les diagrammes sont dessinés et le code est coloré, dans les couleurs claires du thème. Sans l’app, l’outil en ligne de commande gratuit `marsdawn export` produit le même PDF : `marsdawn export notes.md`. Voir [Export PDF](/fr/pdf/) et [Markdown vers PDF](/fr/markdown-to-pdf/).

### Puis-je ouvrir les fichiers .md que mon agent IA a écrits ?

Oui, c’est pour cela que MarsDawn est conçu. Ouvrez le fichier et lisez la page rendue à côté de sa source ; quand l’agent le révise, ouvrez-le de nouveau. Un agent peut aussi exécuter `marsdawn open plan.md` pour ouvrir le fichier dans MarsDawn à votre place. Voir [Lire ce que votre agent vous rend](/fr/reading-agent-output/).

## Pour aller plus loin

- Toutes les options de l’outil en ligne de commande : [Ligne de commande](/fr/cli/).
- Ce que MarsDawn ne fait pas : [la liste](/fr/limits/).
- Lire du Markdown plutôt dans VS Code, un navigateur ou Claude Desktop : [la comparaison](/fr/vs/markdown-preview-tools/).
- Les diagrammes dans un fichier Markdown : [Aperçu Mermaid sur Mac](/fr/mermaid-preview-mac/).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés, d’autres dans la galerie. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Quick Look pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MarsDawn comparé : aperçu VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
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
- [English](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/view-markdown-on-mac/index.md): Mac 怎麼開 md 檔：雙擊、設成預設 App、在 Finder 用快速查看。AI agent 寫出來的 .md，也可以用 MarsDawn 打開，讀排好版的頁面。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/view-markdown-on-mac/index.md): Mac 上怎么打开 md 文件：双击、设为默认 App、在访达用快速查看。AI 代理写出来的 .md，也可以用 MarsDawn 打开，读排好版的页面。
- [日本語](https://marsdawn.southern-light.dev/ja/view-markdown-on-mac/index.md): Mac で .md ファイルを開く方法：ダブルクリック、標準のアプリの設定、Finder のクイックルック。AI エージェントが書いた .md は、MarsDawn でレンダリングして読めます。
- [Deutsch](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Español](https://marsdawn.southern-light.dev/es/view-markdown-on-mac/index.md): Cómo abrir un archivo .md en una Mac: doble clic, app predeterminada, Vista rápida en el Finder. Lee en MarsDawn, ya renderizados, los .md de un agente de IA.
- [한국어](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
