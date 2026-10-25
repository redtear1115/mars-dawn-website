# Meilleur lecteur Markdown pour Mac (2026)

Le meilleur lecteur Markdown dépend de ce que vous lisez. Pour vos propres notes, une app de notes tout-en-un suffit. Pour de longs documents avec diagrammes et formules, ou des fichiers qu’un agent IA réécrit sans cesse, regardez comment chaque app gère le rechargement en direct, Mermaid et le PDF. Les apps sont classées par ordre alphabétique, chacune avec son public, un défaut honnête et son prix.

## MacDown 3000

Le MacDown d’origine n’est plus maintenu. MacDown 3000 en est la suite communautaire : gratuit et open source (MIT), natif, avec Mermaid, MathJax, export PDF, rechargement en direct et Coup d’œil.

- Pour : ceux qui veulent une vue scindée native et gratuite.
- Défaut : l’ouverture à une ligne précise depuis la ligne de commande n’est pas documentée.
- Prix : gratuit.

## Marked

Marked 3 est un outil d’aperçu pour le Markdown que vous écrivez dans une autre app. Il recharge dès que le fichier change, gère MathJax et KaTeX, et imprime des PDF paginés avec numéros de page. Marked 2 est toujours en vente.

- Pour : les auteurs qui gardent leur outil d’écriture et veulent un aperçu et une impression soignés.
- Défaut : Coup d’œil passe par une app séparée, Marked QL (9,99 USD).
- Prix : Marked 3 se télécharge gratuitement, puis 2,99 USD/mois, 29,99 USD/an ou 69,99 USD à vie. Marked 2 coûte 14,99 USD en direct, 13,99 USD sur le Mac App Store.

## MarkEdit

Une app native, légère et gratuite (CodeMirror dans une web view), avec Coup d’œil.

- Pour : ceux qui veulent un outil de texte brut rapide et bien intégré au Mac.
- Défaut : Mermaid et les maths demandent les extensions officielles, et l’export PDF passe par Pandoc.
- Prix : gratuit.

## MarsDawn

Une app Mac native qui affiche la source et un aperçu en direct côte à côte, avec Mermaid et KaTeX intégrés. Quand un agent enregistre le fichier, la fenêtre ouverte prend la modification comme une seule mise à jour depuis le disque, que vous pouvez annuler. `marsdawn open notes.md:120` ouvre un fichier à une ligne, et un skill ainsi qu’un serveur MCP sont fournis pour les agents. Coup d’œil fonctionne avec ou sans l’essai. « Copier pour l’IA » et « Copier la référence » transmettent du texte à un agent. Rien ne quitte votre Mac sans votre choix.

- Pour : ceux qui relisent le Markdown écrit par des agents IA.
- Défaut : l’export PDF n’a pas de numéros de page.
- Prix : téléchargement gratuit avec 14 jours d’essai, puis 4,99 USD une seule fois. Sans compte. Uniquement sur le Mac App Store.

## Obsidian

Une app de notes bâtie autour d’un coffre (vault) de fichiers Markdown liés, avec Mermaid, MathJax, export PDF et rechargement en direct.

- Pour : ceux qui construisent une base de connaissances à partir de leurs notes.
- Défaut : c’est une app Electron, et elle fonctionne mieux avec des fichiers rangés dans un coffre.
- Prix : gratuit. Sync et Publish sont payants.

## QLMarkdown

Une extension Coup d’œil : sélectionnez un fichier .md dans le Finder et appuyez sur Espace. Mermaid et MathJax sont à activer.

- Pour : ceux qui veulent seulement jeter un œil aux fichiers dans le Finder.
- Défaut : ce n’est pas une app pour lire ou modifier, et aucun export PDF n’est documenté.
- Prix : gratuit (GPL-3.0).

## Typora

Un outil d’écriture où l’aperçu est le document, avec Mermaid, MathJax et un export PDF avec numéros de page en en-tête ou en pied de page.

- Pour : ceux qui préfèrent écrire dans une vue de type WYSIWYG.
- Défaut : pas de source et d’aperçu côte à côte.
- Prix : 14,99 USD une seule fois, jusqu’à 3 appareils.

## Aperçu de VS Code

L’aperçu Markdown intégré, avec Mermaid intégré depuis la 1.121 et KaTeX. `code -g file:line` ouvre un fichier à une ligne.

- Pour : les développeurs qui vivent déjà dans VS Code.
- Défaut : c’est une app Electron, sans export PDF intégré.
- Prix : gratuit.

## Comparatif

| App | Prix | Mermaid | Maths | PDF | Rechargement en direct | CLI à une ligne | Coup d’œil | Technologie |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | Gratuit | Oui | MathJax | Oui | Oui | Non documenté | Oui | Natif |
| Marked 3 | Dès 2,99 USD/mois | Oui | MathJax, KaTeX | Oui, numéros de page | Oui | Non documenté | Marked QL, 9,99 USD | Natif |
| MarkEdit | Gratuit | Extension | KaTeX (extension) | Pandoc | Non documenté | Non documenté | Oui | Natif (web view) |
| MarsDawn | 4,99 USD une fois | Oui | KaTeX | Oui, sans numéros de page | Oui, annulable | Oui | Oui | Natif |
| Obsidian | Gratuit | Oui | MathJax | Oui | Oui | Non documenté | Non documenté | Electron |
| QLMarkdown | Gratuit | À activer | MathJax (à activer) | Non documenté | Sans objet | Sans objet | C’en est une | Natif |
| Typora | 14,99 USD une fois | Oui | MathJax | Oui, numéros de page | Non documenté | Non documenté | Non documenté | Natif |
| VS Code | Gratuit | Oui (1.121+) | KaTeX | Non | Non documenté | Oui | Non documenté | Electron |

## À qui MarsDawn ne convient pas

- Il vous faut des numéros de page dans vos PDF. Typora et Marked 3 les ajoutent, MarsDawn non.
- Vous entretenez une base de connaissances de notes liées. Obsidian est fait pour cela.
- Vous ne quittez jamais VS Code. Son aperçu intégré est gratuit, et VS Code ajoute une vue Markdown expérimentale à sa fenêtre Agents.
- Vous voulez seulement un aperçu dans le Finder. QLMarkdown est gratuit.

## Questions fréquentes

### Quels lecteurs Markdown gratuits pour Mac gèrent Mermaid ?

MacDown 3000, Obsidian et VS Code (1.121 et ultérieur) l’intègrent. QLMarkdown le propose en option, MarkEdit via une extension.

### Lesquels exportent un PDF avec numéros de page ?

Typora et Marked 3. MarsDawn exporte le PDF sans numéros de page.

### Lesquels ouvrent un fichier à une ligne précise depuis la ligne de commande ?

MarsDawn (`marsdawn open notes.md:120`) et VS Code (`code -g file:line`). Pour les autres, ce n’est pas documenté.

### Lesquels sont des apps Mac natives plutôt qu’Electron ?

Toutes sauf Obsidian et VS Code. MarkEdit est natif, avec sa zone d’édition dans une web view.

[Télécharger et essayer](https://apps.apple.com/app/id6812925073)

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Lisez et relisez le Markdown de votre agent sur Mac : aperçu partagé en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Des thèmes, mais pas de CSS personnalisé. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Ouvrir un fichier .md sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Coup d’œil pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MarsDawn comparé : aperçu VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu intégrés, chacun clair et sombre, et une galerie vérifiée dans les réglages de MarsDawn pour Mac. Coup d’œil utilise votre thème.
- [Créer un thème](https://marsdawn.southern-light.dev/fr/themes/new/index.md): Choisissez des couleurs et quelques options de style, voyez-les appliquées en direct à un document d’exemple, et envoyez votre thème en issue GitHub. Pas d’installation, pas de git.
- [Créer un thème avec votre agent](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Galerie de thèmes](https://marsdawn.southern-light.dev/fr/themes/gallery/index.md): Parcourez les thèmes d’aperçu pour MarsDawn, chacun relu par le développeur, filtrez par scénario et signalez un problème. Créez le vôtre dans le navigateur.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Feuille de route](https://marsdawn.southern-light.dev/fr/roadmap/index.md): Ce qui est en cours et ce qui vient ensuite pour MarsDawn sur Mac, iPhone et iPad, version par version. Sans dates ; les idées non planifiées sont signalées.
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
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
