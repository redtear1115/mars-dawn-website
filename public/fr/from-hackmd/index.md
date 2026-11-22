# Passer de HackMD à votre Mac

Vos notes sont déjà en Markdown, il n’y a rien à convertir. Choisissez une voie selon ce que vous déplacez. Les images demandent une étape à part : lisez cette section avant de supprimer quoi que ce soit sur HackMD.

Nous avons vérifié tout cela avec un compte HackMD gratuit en novembre 2026. HackMD peut évoluer, et nous n’avons testé ni les offres payantes ni les espaces d’équipe.

| Vous voulez | Votre voie |
|---|---|
| Déplacer toutes vos notes | Télécharger toutes les notes |
| Déplacer des notes déjà sur GitHub | Cloner le dépôt |
| Déplacer une ou deux notes | Télécharger une note |

## Télécharger toutes les notes

Les réglages de notes de HackMD proposent Download all notes, pour les espaces personnels et d’équipe. Vous obtenez un .zip avec un fichier .md par note, nommé d’après son titre.

- Les dossiers ne sont pas conservés. Toutes les notes arrivent au premier niveau.
- Les images ne sont pas incluses. Les fichiers .md y renvoient toujours par URL.
- L’option qui inclut le titre et les tags est activée par défaut et ajoute un bloc de front matter à chaque note. Désactivez-la pour obtenir chaque note telle qu’elle a été écrite.

Décompressez le fichier, puis choisissez Fichier ▸ Ouvrir un dossier… dans MarsDawn pour ouvrir ce dossier.

## Cloner le dépôt

La synchronisation GitHub de HackMD relie une note à un fichier. Une note que vous avez envoyée est donc déjà dans le dépôt. Clonez-le et ouvrez le dossier avec Fichier ▸ Ouvrir un dossier…. La barre latérale affiche le dépôt et sa branche.

Si vos notes ne sont pas encore sur GitHub, inutile de commencer pour ce déplacement. Chaque note doit être reliée séparément, et l’offre gratuite permet 20 envois par mois. Avec un compte personnel gratuit, nous n’avons trouvé aucun moyen d’envoyer tout un espace de travail d’un coup.

Après le déplacement, considérez le dépôt comme l’original. Un envoi depuis HackMD remplace ce qui se trouve sur GitHub, même si GitHub a un contenu plus récent, et il ne vous avertit pas.

## Télécharger une note

Le menu de la note la télécharge en .md ou en .html. Choisissez .md et ouvrez le fichier dans MarsDawn.

## Images

Les images que vous avez importées sur HackMD se trouvent à l’adresse `https://hackmd.io/_uploads/...`. Qui peut les voir dépend de l’autorisation de la note.

| Votre note est | Ce qui se passe sur votre Mac | Que faire |
|---|---|---|
| Publique | L’image se charge depuis HackMD | Cliquez sur Charger les images dans l’aperçu, ou activez Réglages ▸ Images ▸ Charger automatiquement les images distantes |
| Privée | L’image renvoie une erreur, car MarsDawn n’est pas connecté à HackMD | Enregistrez l’image depuis un navigateur connecté, placez-la à côté du fichier .md et modifiez le chemin. Ou rendez la note publique, si tout le monde peut la lire |

- **Les anciennes notes** peuvent utiliser des adresses `i.imgur.com`.
- **Supprimer une note supprime ses images.** Leurs adresses ne fonctionnent plus, alors déplacez d’abord les images.

Si MarsDawn n’atteint pas une image à côté de votre fichier, utilisez le bouton de l’aperçu pour lui donner accès au dossier.

## L’apparence de vos notes

La plupart de la syntaxe HackMD se lit de la même façon : `==surligné==`, `^exposant^`, `~indice~`, `[TOC]`, les tailles d’image comme `=300x200`, Mermaid et KaTeX. `{%youtube %}` s’affiche comme un lien. Pour garder chaque saut de ligne comme dans HackMD, activez Réglages ▸ Apparence ▸ Conserver les sauts de ligne simples.

Les blocs `:::` fonctionnent aussi. `:::info`, `:::success`, `:::warning` et `:::danger` apparaissent sous forme de blocs avec une barre colorée et un titre (Remarque, Conseil, Avertissement ou Danger par défaut). Si vous écrivez votre propre titre après le nom, c’est lui qui s’affiche. `:::spoiler` apparaît sous forme de bloc repliable qui s’ouvre d’un clic. Un bloc `:::` avec un autre nom, ou sans `:::` de fermeture, s’affiche tel que vous l’avez tapé.

Quelques éléments changent :

- `++inséré++` et les codes emoji comme `:sparkles:` s’affichent tels que vous les avez tapés.
- `{%hackmd id %}` n’est pas développé.
- Les icônes `<i class="fa ...">` n’apparaissent pas.

## Pour les scripts : hackmd-cli

`hackmd-cli` n’a pas de commande qui exporte tout d’un coup. Il exporte une note et l’affiche : il faut donc lister vos notes, puis les parcourir en boucle. Il vous faut Node.js, `jq` et un jeton API créé dans vos réglages HackMD. Si vous n’avez pas besoin de script, Download all notes est plus simple.

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<votre jeton>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **Les dossiers ne suivent pas.** La liste des notes n’indique pas leur dossier, donc tous les fichiers arrivent au même endroit.
- **Les images restent des liens `hackmd.io`.** Traitez-les comme dans la section Images ci-dessus.
- **Les noms de fichier sont les ID des notes,** pas leurs titres.
- **L’offre gratuite permet 400 appels API tous les 30 jours.** La liste utilise un appel, puis chaque note un de plus.

Nous n’avons essayé cela que sur un compte avec peu de notes, nous ne savons donc pas ce que donne une très longue liste. Supprimez le jeton dans vos réglages HackMD quand vous avez terminé.

## Écrire ensemble

MarsDawn n’a pas d’édition partagée. Si vous devez écrire ensemble en direct, gardez HackMD. Si votre équipe garde ses documents dans git, chacun peut ouvrir le même dépôt dans son propre MarsDawn, et vous finissez le document ensemble. Voir Relire des documents en équipe avec git.

## Questions

### Puis-je télécharger toutes mes notes HackMD d’un coup ?

Oui. Download all notes vous donne un .zip de fichiers .md. Il ne conserve pas les dossiers et n’inclut pas les images.

### Pourquoi mes images manquent-elles dans MarsDawn ?

MarsDawn retient les images du web jusqu’à ce que vous cliquiez sur Charger les images. Si la note est privée, l’image ne peut pas se charger : enregistrez-la à côté de votre fichier.

### Dois-je quitter HackMD ?

Non. HackMD reste le meilleur choix pour écrire ensemble. MarsDawn sert à lire et à relire sur votre Mac.

## Plus

- [MarsDawn](https://marsdawn.southern-light.dev/fr/index.md): Relisez le Markdown, JSON et YAML de votre agent sur Mac : aperçu en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Fonctionnalités](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Mac natif pour Markdown, JSON et YAML : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions et dossiers papier.
- [Vos textes restent sur votre Mac](https://marsdawn.southern-light.dev/fr/yours/index.md): MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.
- [Essai gratuit, achat unique](https://marsdawn.southern-light.dev/fr/pay-once/index.md): MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.
- [Imprimer et PDF](https://marsdawn.southern-light.dev/fr/pdf/index.md): Prévisualisez votre Markdown, puis imprimez-le ou enregistrez-le en PDF sur Mac, en disposition Document, Guide ou Polycopié, avec diagrammes et code coloré.
- [Une app Mac](https://marsdawn.southern-light.dev/fr/native/index.md): Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.
- [Ce que MarsDawn ne fait pas](https://marsdawn.southern-light.dev/fr/limits/index.md): Pas de synchronisation, pas de modification sur iPhone ou iPad, pas de plug-ins, pas de comptes. Des thèmes, mais pas de CSS personnalisé. À savoir avant d’acheter.
- [Assistance](https://marsdawn.southern-light.dev/fr/support/index.md): De l’aide pour MarsDawn, l’éditeur Markdown pour macOS.
- [Politique de confidentialité](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Ouvrir un fichier .md sur Mac](https://marsdawn.southern-light.dev/fr/view-markdown-on-mac/index.md): Ouvrir un fichier .md sur Mac : double-clic, app par défaut, Coup d’œil dans le Finder. Les .md écrits par un agent IA se lisent mis en forme dans MarsDawn.
- [Aperçu Mermaid sur Mac](https://marsdawn.southern-light.dev/fr/mermaid-preview-mac/index.md): Diagrammes Mermaid dessinés à côté de votre Markdown sur Mac : aperçu en direct, Coup d’œil et export PDF. Un diagramme erroné affiche l’erreur et la ligne.
- [Coup d’œil pour Markdown](https://marsdawn.southern-light.dev/fr/quicklook/index.md): Avec MarsDawn, Coup d’œil affiche le Markdown mis en forme dans le Finder avec Espace : Mermaid, KaTeX, code coloré. Il fonctionne toujours après l’essai.
- [Copier pour l’IA](https://marsdawn.southern-light.dev/fr/copy-for-ai/index.md): Copiez le texte sélectionné avec son chemin de fichier et ses numéros de ligne, puis collez-le dans Claude Code ou tout autre agent. Sur votre Mac, sans IDE ni plug-in.
- [Markdown vers PDF](https://marsdawn.southern-light.dev/fr/markdown-to-pdf/index.md): Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.
- [MarsDawn comparé : aperçu VS Code, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026, sauf la cellule PDF de MarsDawn, mise à jour le 7 novembre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [MacMD Viewer vs MarsDawn](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Meilleur lecteur Markdown pour Mac (2026)](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
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
- [English](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Deutsch](https://marsdawn.southern-light.dev/de/from-hackmd/index.md): Lade deine HackMD-Notizen als .md herunter und lies sie in MarsDawn auf dem Mac. Alle Notizen herunterladen, ein GitHub-Repository nutzen und Bilder retten.
- [Español](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
- [한국어](https://marsdawn.southern-light.dev/ko/from-hackmd/index.md): HackMD 노트를 .md로 내려받아 Mac의 MarsDawn에서 읽는 방법입니다. 모든 노트 다운로드, GitHub 저장소에서 옮기기, 이미지 처리 방법을 정리했습니다.
