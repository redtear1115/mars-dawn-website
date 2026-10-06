# Assistance

De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.

## Écrivez-nous

[support@southern-light.dev](mailto:support@southern-light.dev?subject=MarsDawn%20support)

Merci d’indiquer votre version de macOS et votre version de MarsDawn (MarsDawn › À propos de MarsDawn). Si quelque chose semble anormal, une capture d’écran ou un petit document d’exemple aide beaucoup.

## Questions fréquentes

### De quoi ai-je besoin pour utiliser MarsDawn ?

Un Mac avec macOS 26 Tahoe ou version ultérieure, équipé d’une puce Apple ou d’un processeur Intel.

### Comment passer de l’éditeur à l’aperçu ?

Appuyez sur `⌘1` pour la source uniquement, `⌘2` pour les deux côte à côte et `⌘3` pour l’aperçu uniquement. Les mêmes options se trouvent dans le menu Présentation et dans la barre d’outils.

### Une image de mon document ne s’affiche pas.

- **Image sur votre Mac :** enregistrez d’abord le document, puis cliquez sur *Autoriser l’accès au dossier…* dans l’aperçu et choisissez le dossier qui contient l’image. MarsDawn mémorise le dossier. Vous pouvez revoir les dossiers autorisés dans MarsDawn › Réglages › Accès aux dossiers.
- **Image provenant du web :** les images web sont bloquées jusqu’à ce que vous cliquiez sur *Charger les images* en haut de l’aperçu. Pour toujours les charger, activez *Charger automatiquement les images distantes* dans les Réglages.

### Comment ajouter une image ?

Faites-la glisser dans l’éditeur, ou collez-la. Le document doit d’abord être enregistré : MarsDawn copie l’image dans un dossier `assets` à côté du document et écrit le lien Markdown pour vous.

### Un diagramme Mermaid affiche une erreur.

MarsDawn affiche la source du diagramme, avec en dessous la première ligne du message d’erreur de Mermaid. Vérifiez la ligne indiquée, par exemple une flèche suivie de rien ou une parenthèse non fermée.

### Comment créer un PDF ?

Choisissez Fichier › Exporter au format PDF… (`⌥⌘E`). Le PDF utilise la version claire de votre thème de l’aperçu et est découpé en pages, quelle que soit la disposition dans laquelle vous êtes. Fichier › Imprimer… imprime les mêmes pages.

### Comment utiliser MarsDawn avec Siri ou Raccourcis ?

Ouvrez l’app Raccourcis et recherchez MarsDawn pour trouver *Nouveau document Markdown*, *Ajouter une note à la boîte de réception* et *Ouvrir un document récent*. Avant d’ajouter des notes, choisissez un dossier de notes dans MarsDawn › Réglages › Dossier de notes. Les notes sont ajoutées au fichier `Inbox.md` de ce dossier.

### Où sont mes réglages ?

MarsDawn › Réglages (`⌘,`) regroupe l’apparence, les images, le dossier de notes, l’accès aux dossiers et le thème de l’aperçu.

### Comment obtenir un remboursement ?

Les achats sont gérés par Apple. Demandez un remboursement sur [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
- [marsdawn pour les agents](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Skill pour agents](https://marsdawn.southern-light.dev/fr/cli/skill/index.md): Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.
- [Serveur MCP](https://marsdawn.southern-light.dev/fr/cli/mcp/index.md): marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.
- [Relire en économisant les tokens](https://marsdawn.southern-light.dev/fr/token-efficient-review/index.md): Une personne relit la page rendue dans MarsDawn ; elle n’est jamais relue dans le contexte de l’agent. L’appel d’outil renvoie un résultat JSON compact, pas le contenu rendu : l’appeler coûte donc peu aussi.
- [Afficher du Markdown ailleurs vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/markdown-preview-tools/index.md): MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.
- [Thèmes de l’aperçu et export PDF](https://marsdawn.southern-light.dev/fr/themes/index.md): Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. D’autres thèmes importables et une galerie pour partager les vôtres sont prévus.
- [Partager les PDF exportés](https://marsdawn.southern-light.dev/fr/sharing-exported-pdfs/index.md): Exportez le Markdown d’un agent en PDF et remettez-le à un collègue qui ne lit pas le Markdown et n’installera rien. Aucune syntaxe, aucune app et aucun compte nécessaires pour l’ouvrir.
- [Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain](https://marsdawn.southern-light.dev/fr/reviewing-ai-output/index.md): Le Markdown écrit par une IA doit être compris par une personne, pas cru sur parole. MarsDawn place la page rendue à côté de la source et dessine les diagrammes Mermaid et les formules KaTeX, pour que la structure se lise d’un coup d’œil.
- [Lire ce que votre agent vous rend](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Transparence des agents](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Relire le plan d’un agent](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Patrons de conception d’agents](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Historique des versions](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.
- [Modèles](https://marsdawn.southern-light.dev/fr/templates/index.md): Des modèles Markdown pour les documents qu’un agent rédige et que vous lisez : une spécification, un organigramme et un compte rendu de réunion, chacun avec un prompt pour votre agent.
- [Modèle de spécification](https://marsdawn.southern-light.dev/fr/templates/spec/index.md): Un modèle de spécification en Markdown avec exigences, diagramme de flux Mermaid et critères d’acceptation. Votre agent le remplit ; vous le relisez dans MarsDawn.
- [Modèle d’organigramme](https://marsdawn.southern-light.dev/fr/templates/flowchart/index.md): Un modèle d’organigramme Mermaid en Markdown, avec les étapes écrites en dessous. Prévisualisez-le sur Mac et exportez-le en PDF.
- [Modèle de compte rendu](https://marsdawn.southern-light.dev/fr/templates/meeting-notes/index.md): Un modèle de compte rendu de réunion en Markdown, avec les décisions et les actions, chacune avec un responsable. Votre agent le rédige ; vous le vérifiez dans MarsDawn.
- [English](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/support/index.md): MarsDawn（macOS Markdown 編輯器）的使用說明與聯絡方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/support/index.md): MarsDawn（macOS Markdown 编辑器）的使用说明与联系方式。
- [日本語](https://marsdawn.southern-light.dev/ja/support/index.md): macOS 向け Markdown エディタ MarsDawn のヘルプ。
- [Deutsch](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Español](https://marsdawn.southern-light.dev/es/support/index.md): Ayuda con MarsDawn, el editor de Markdown para macOS.
- [한국어](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
