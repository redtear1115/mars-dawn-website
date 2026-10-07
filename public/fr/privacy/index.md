# Politique de confidentialité

Comment MarsDawn, l’éditeur Markdown pour macOS, traite vos informations.

Dernière mise à jour : 2026-09-23

> **L’app MarsDawn ne collecte aucune donnée vous concernant.** Il n’y a ni compte, ni publicité, ni suivi. Vos documents et vos réglages restent sur votre Mac.

## Le site web

L’app et ce site web sont deux choses distinctes. L’app ne collecte rien. Une visite ne peut être enregistrée qu’ici, sur marsdawn.southern-light.dev.

Ce site utilise **Google Analytics 4**, chargé via **Google Tag Manager**. Pour chaque visiteur, la mesure d’audience est d’abord refusée : le mode Consentement (Consent Mode) de Google n’envoie qu’un ping sans cookie, sans cookie de mesure et sans identifiant persistant, jusqu’à ce que vous choisissiez *Accepter* dans le bandeau. Si vous choisissez *Refuser*, ou si vous ne faites aucun choix, rien ne change. Choisir *Refuser* après avoir accepté désactive immédiatement la mesure d’audience et supprime les cookies ci-dessous. Vous pouvez modifier votre choix à tout moment avec le lien « Réglages des cookies » en pied de chaque page. Ce choix est enregistré uniquement dans le stockage local de votre navigateur, jamais dans un cookie de notre part.

Une fois que vous avez accepté, Google Analytics dépose ses propres cookies (`_ga` et `_ga_<measurement id>`) et enregistre :

- **Pages vues et référent.** La page consultée et, lorsque le navigateur l’envoie, l’adresse de provenance.
- **Localisation approximative, appareil et navigateur.** Une localisation grossière déduite de votre adresse IP (au plus au niveau de la ville), votre type d’appareil, votre système d’exploitation et votre navigateur. Rien de tout cela n’est assez précis pour vous identifier.
- **Clics sortants et profondeur de défilement.** Les mesures améliorées de Google Analytics enregistrent les clics qui quittent le site, comme le lien vers le Mac App Store, ainsi que la distance que vous faites défiler sur une page.
- **Adresses IP.** Google Analytics 4 ne journalise ni ne stocke les adresses IP.
- **Ce qui n’est pas enregistré.** Aucun compte, puisque le site n’en a pas. Aucun document, et rien de ce que vous saisissez. Aucune publicité intersites, et aucun profil de vous. Les requêtes de l’app pour les fichiers de thème sous `/themes/` sont ignorées et ne sont pas transmises.
- **Conservation.** Google conserve ces données pendant 14 mois, puis les supprime.
- **Lieu de traitement.** Google Tag Manager et Google Analytics sont exploités par Google ; vos données peuvent être traitées aux États-Unis ainsi que dans d’autres pays où Google exerce ses activités.
- **L’hébergeur.** Cloudflare héberge le site et, comme tout hébergeur, voit votre adresse IP pendant qu’il répond à la requête. Ce journal appartient à l’hébergeur. Il ne s’agit pas de la mesure d’audience décrite ci-dessus.

## Ce qui reste sur votre Mac

- **Vos documents.** MarsDawn lit et écrit uniquement les fichiers et dossiers que vous ouvrez, enregistrez ou choisissez. L’app ne les envoie jamais nulle part.
- **Vos réglages.** L’apparence, le thème de l’aperçu, la disposition des fenêtres et la préférence pour les images sont stockés dans les préférences propres de l’app, sur votre Mac.
- **L’accès aux dossiers que vous autorisez.** Lorsque vous laissez MarsDawn afficher des images ou des fichiers de page provenant d’un dossier, ou que vous choisissez un dossier de notes, l’app conserve un signet macOS afin de pouvoir rouvrir ce dossier. Un dossier que vous ouvrez dans la barre latérale reste accessible en lecture et en écriture par MarsDawn jusqu’à ce que vous le supprimiez dans les Réglages, et pas seulement tant que sa fenêtre est ouverte. Vous pouvez supprimer des dossiers à tout moment dans MarsDawn › Réglages.

## Quand MarsDawn utilise Internet

MarsDawn fonctionne entièrement hors ligne. L’app ne se connecte à Internet **que si vous le choisissez**, pour un document qui fait référence au web :

- **Documents Markdown.** Les images web sont bloquées par défaut. Elles ne se chargent qu’après un clic sur *Charger les images* dans l’aperçu, ou si vous activez *Charger automatiquement les images distantes* dans les Réglages. Rien d’autre de ce à quoi un document Markdown fait référence n’est chargé depuis le web.
- **Documents HTML.** Un document HTML s’ouvre de façon statique : son code ne s’exécute pas et rien n’est chargé depuis le web. Si un document contient du code exécutable, vous pouvez choisir *Présentation › Exécuter ce document* pour ce document. Son propre code s’exécute alors jusqu’à ce que vous l’arrêtiez, que le document se recharge ou que vous fermiez la fenêtre. Ce choix n’est jamais mémorisé, et ce n’est pas un réglage. Pendant l’exécution, le document peut envoyer des données sur le réseau, et lire les images, feuilles de style, polices et médias de son dossier et des dossiers qu’il contient. Le code téléchargé depuis le web ne s’exécute jamais.

MarsDawn charge le contenu web uniquement en https. Une adresse en http simple n’est jamais chargée, quel que soit le réglage, et MarsDawn ne la réécrit pas en https. Dans un document Markdown, l’aperçu affiche un espace réservé à sa place.

Lorsqu’un contenu web se charge, votre Mac le demande directement aux serveurs qui l’hébergent. Comme pour toute requête web, ces serveurs voient alors votre adresse IP et ce qui a été demandé. Le développeur de MarsDawn ne reçoit aucune de ces informations.

Les liens sur lesquels vous cliquez dans l’aperçu s’ouvrent dans votre navigateur web par défaut, selon les pratiques de confidentialité de ce navigateur. L’audio et la vidéo ne se lancent jamais d’eux-mêmes.

## Siri, Raccourcis et Spotlight

MarsDawn propose des actions pour Siri, l’app Raccourcis et Spotlight, comme créer un document ou ajouter une note. Lorsque vous les utilisez, le texte que vous fournissez est transmis à MarsDawn sur votre Mac et enregistré uniquement à l’endroit indiqué par l’action (un nouveau document, ou le fichier `Inbox.md` du dossier de notes que vous avez choisi). Ce que vous dictez à Siri est traité par Apple conformément à la [politique de confidentialité d’Apple](https://www.apple.com/legal/privacy/).

## Export et impression

L’export PDF et l’impression se font sur votre Mac. Le PDF est enregistré à l’endroit que vous choisissez. L’impression passe par macOS vers l’imprimante que vous sélectionnez.

## L’outil en ligne de commande marsdawn

L’outil en ligne de commande facultatif `marsdawn`, distribué séparément, s’exécute lui aussi entièrement sur votre Mac. Il lit le fichier Markdown que vous indiquez et écrit le PDF que vous demandez. Il ne charge les images web que si vous passez `--allow-remote-images`.

## Enfants

L’app MarsDawn ne collecte de données auprès de personne, y compris les enfants. Une visite enregistrée sur le site web n’est pas un compte, et elle ne sert pas à identifier qui que ce soit.

## Achats

MarsDawn est vendu sur le Mac App Store. Apple traite l’achat selon ses propres conditions, et le développeur ne reçoit jamais vos informations de paiement.

## Modifications de cette politique

Si MarsDawn venait à traiter les données différemment, cette page serait mise à jour avant la sortie de la version concernée, et la date en haut de page changerait.

## Contact

Questions relatives à la confidentialité : [support@southern-light.dev](mailto:support@southern-light.dev)

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Export PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Afficher du Markdown sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [Ligne de commande](https://marsdawn.southern-light.dev/fr/cli/index.md): L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.
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
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Deutsch](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Español](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [한국어](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
