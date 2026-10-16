# MacMD Viewer ou MarsDawn.

Ce sont deux apps Mac pour lire du Markdown sous forme de page terminée. MacMD Viewer ouvre un fichier `.md` et l’affiche ; il est en lecture seule par conception et n’enregistre jamais de modifications dans votre fichier. MarsDawn place un éditeur à côté du même genre d’aperçu rendu, pour que vous écriviez et relisiez dans une seule fenêtre. Cette page met les deux côte à côte, ligne par ligne, avec une source pour chaque fait sur MacMD Viewer, et dit quand MacMD Viewer est le meilleur choix.

Vérifié sur le site et le dépôt de MacMD Viewer le 15 octobre 2026 (version 1.7.0, publiée le 10 octobre 2026). Si quelque chose ici est périmé, écrivez-nous à l’adresse de la [page d’assistance](/fr/support/).

## Ce que c’est et ce que ça fait

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Ce que c’est | Une visionneuse : « en lecture seule, n’enregistre jamais de modifications dans votre fichier source » [[S1](#s1), [S9](#s9)] | Un éditeur avec aperçu en direct : le Markdown à gauche, la page rendue à droite, avec trois présentations (source, partagé, aperçu) |
| Modification | Non [[S1](#s1), [S7](#s7), [S9](#s9)] | Oui. La page rendue elle-même n’est pas modifiable ; vous modifiez la source à côté |
| Aperçu en direct | Affiche le fichier ; se recharge quand un autre éditeur l’enregistre [[S9](#s9)] | Se met à jour pendant la saisie. Quand une autre app modifie le fichier, MarsDawn le recharge et garde votre position, tant que vous n’avez pas de modifications non enregistrées. |
| Mermaid | Oui : organigrammes, diagrammes de séquence et d’états, diagrammes de Gantt, camemberts et plus, hors ligne [[S1](#s1), [S3](#s3), [S7](#s7)] | Oui |
| Mathématiques | Non : son README dit qu’il « n’affiche pas les mathématiques (LaTeX/KaTeX) » [[S7](#s7)] | Oui, KaTeX |
| Coloration du code | Oui [[S1](#s1), [S9](#s9)] | Oui |
| Thèmes | 12 thèmes de document [[S1](#s1), [S7](#s7)] | 4 intégrés (Aube, Classique, Moderne, Vif), chacun avec une palette claire et une sombre, plus d’autres dans la galerie de thèmes |
| Onglets | Oui, facultatifs et désactivés par défaut (depuis 1.6.0) [[S5](#s5), [S8](#s8)] | Oui |
| Export PDF | Oui, une seule page continue, dans le thème actuel, sans filigrane [[S3](#s3), [S9](#s9)] | Oui, pages paginées dans la palette claire du thème ; les sauts de page évitent de couper les blocs de code courts et les tableaux |
| Impression | Oui, via la fenêtre d’impression de macOS [[S3](#s3), [S9](#s9)] | Oui |
| Coup d’œil dans le Finder | Oui, inclus ; vous l’activez dans Réglages Système ; utilise votre thème [[S4](#s4)] | Oui, fonctionne avec ou sans l’essai ; utilise votre thème |
| Mermaid et mathématiques dans Coup d’œil | Mermaid : oui [[S4](#s4)]. Mathématiques : non, il ne les affiche pas [[S7](#s7)] | Oui, les deux sont dessinés |
| Ligne de commande | Aucun outil en ligne de commande autonome n’est décrit. Il a un schéma d’URL `markdownviewer://` et un plug-in Claude Code avec des hooks qui ouvrent des fichiers dans la visionneuse [[S6](#s6)] | L’outil gratuit `marsdawn` : `marsdawn export` produit un PDF sans l’app, `marsdawn open` ouvre un fichier à une ligne donnée |
| Langues de l’interface | Non précisé dans ses propres documents [[S1](#s1), [S3](#s3), [S7](#s7)] | anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen |
| Configuration requise | macOS 14 (Sonoma) ou version ultérieure ; Apple silicon et Intel [[S1](#s1), [S7](#s7)] | macOS 26 (Tahoe) ou version ultérieure |
| Autres plateformes | Mac uniquement [[S1](#s1)] | Mac uniquement. Pas d’app pour iPhone ou iPad |

## Prix et mode d’achat

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Où l’acheter | Son propre site, Homebrew ou Setapp ; pas de fiche sur le Mac App Store [[S2](#s2), [S7](#s7)] | Uniquement sur le Mac App Store |
| Prix | 19,99 USD une seule fois, pour un Mac actif (transférable vers un autre Mac) ; Family Pack à 39,99 USD pour 3 ; 10 clés à 129 USD [[S2](#s2)] | Téléchargement gratuit, puis 4,99 USD une seule fois |
| L’essayer d’abord | Ni essai ni version gratuite ; remboursement intégral sous 14 jours pour un achat direct [[S2](#s2)] | Essai gratuit de 14 jours, avec toutes les fonctions |
| Remboursements | Via son propre support, sous 14 jours [[S2](#s2)] | Via Apple |
| Mises à jour | Les mises à jour de la version majeure en cours sont gratuites [[S2](#s2)] ; le téléchargement direct se met à jour avec Sparkle [[S7](#s7)] | Via le Mac App Store |
| Compte requis | Non [[S2](#s2)] | Non |
| Abonnement | Non [[S1](#s1), [S2](#s2)] | Non |

## Ce qui change quand vous cessez d’essayer ou de payer

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Ensuite | Pas d’essai ; une fois acheté, il continue de fonctionner | Si vous ne déverrouillez pas après 14 jours, les documents s’ouvrent avec leur contenu masqué ; vos fichiers ne sont pas touchés, Coup d’œil et l’export `marsdawn` gratuit continuent de fonctionner |

## Sources

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## Lequel choisir

**Choisissez MacMD Viewer si** vous ne faites que lire du Markdown et voulez la garantie que votre fichier ne sera jamais modifié : il n’enregistre jamais de modifications [[S1](#s1)]. Il convient aussi mieux si votre Mac tourne sous macOS 14 ou 15, puisque MarsDawn demande macOS 26 [[S1](#s1), [S7](#s7)] ; si vous préférez acheter sur le site d’un développeur, via Homebrew ou Setapp plutôt que sur le Mac App Store [[S2](#s2), [S7](#s7)] ; si vous voulez que les fichiers qu’un agent modifie s’ouvrent automatiquement dans la visionneuse, ce qu’il fait grâce à des hooks pour Claude Code, Cursor et Windsurf [[S6](#s6)] ; ou si vous voulez un PDF d’une seule page continue plutôt que de pages paginées [[S9](#s9)]. Il n’a pas d’essai, mais un remboursement sous 14 jours [[S2](#s2)].

**Choisissez MarsDawn si** le Markdown revient pour un nouveau passage. Le plan, le README ou la spécification d’un agent demande généralement une correction, une phrase reformulée ou une nouvelle section, et dans MarsDawn vous la faites dans la fenêtre où vous lisez déjà. Il couvre aussi les mathématiques (KaTeX), que MacMD Viewer dit ne pas afficher [[S7](#s7)] ; il est livré en huit langues d’interface ; il a un outil `marsdawn` en ligne de commande gratuit qui exporte un PDF sans l’app ; et son prix est de 4,99 USD après un essai de 14 jours où tout fonctionne.

**L’un ou l’autre convient si** vous lisez du Markdown sur un Mac récent, voulez des diagrammes Mermaid bien dessinés et voulez Coup d’œil dans le Finder. Les deux le font.

**Et vous pouvez utiliser les deux.** Ils ne s’excluent pas : rien ne vous empêche de garder une visionneuse en lecture seule pour ce que vous ne faites que lire et un éditeur pour ce que vous écrivez.

## Questions

### MacMD Viewer modifie-t-il les fichiers ?

Non. Il est en lecture seule et, selon ses propres termes, n’enregistre jamais de modifications dans votre fichier source [[S1](#s1), [S9](#s9)]. Il propose « Ouvrir dans l’éditeur de texte » (depuis 1.7.0), qui confie le fichier à une autre app [[S5](#s5)].

### MacMD Viewer est-il sur le Mac App Store ?

Ses propres pages citent son site, Homebrew et Setapp, et ne mentionnent pas le Mac App Store [[S2](#s2), [S7](#s7)]. MarsDawn est uniquement sur le Mac App Store.

### MarsDawn peut-il ouvrir les mêmes fichiers ?

Oui. Il ouvre les fichiers `.md`, ainsi que les fichiers de texte brut et les PDF : le texte s’ouvre prêt à être modifié en UTF-8, et les PDF s’ouvrent dans une visionneuse.

### Et si j’ai macOS 14 ou 15 ?

MacMD Viewer fonctionne sous macOS 14 ou version ultérieure [[S1](#s1)]. MarsDawn demande macOS 26 ou version ultérieure, et l’outil gratuit `marsdawn` en ligne de commande peut malgré tout exporter un PDF.

### Pourquoi l’un coûte-t-il 19,99 USD et l’autre 4,99 USD ?

Ils diffèrent par ce que vous obtenez et par la façon de payer. MacMD Viewer est un achat unique avec remboursement sous 14 jours et sans essai [[S2](#s2)]. MarsDawn est un téléchargement gratuit avec un essai de 14 jours, puis un déverrouillage unique. Aucun des deux n’est un abonnement.

## Essayez-le gratuitement dès aujourd’hui

MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit `marsdawn` fait aussi le rendu de n’importe quel fichier Markdown en PDF, avec les diagrammes Mermaid et le code coloré, et rien d’autre n’est nécessaire :

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## Pour aller plus loin

- Le pas-à-pas complet : [Markdown en PDF](/fr/markdown-to-pdf/).
- Ce que MarsDawn ne fait pas : [la liste](/fr/limits/).
- Toutes les options de l’outil en ligne de commande : [Ligne de commande](/fr/cli/).
- Par rapport à la lecture du Markdown dans VS Code, un navigateur ou Claude Desktop : [la comparaison](/fr/vs/markdown-preview-tools/).
- Tout ce que fait MarsDawn, sur une seule page : [Fonctionnalités](/fr/features/).

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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Deutsch](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD. Zeile für Zeile verglichen, mit Quellen.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita y muestra la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez. Comparación fila por fila, con fuentes.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
