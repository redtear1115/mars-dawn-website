"""French (fr) page copy for the MarsDawn site, tranche 2 (#164).

Same shape as scripts/copy_ja.py: build(k) returns the tables build_pages.py keeps per locale.
Translated from the en copy on main @ 6fe8435. Address: vous, as in the app. UI terms follow the
app's fr strings (release/1.1.0): Coup d’œil (Quick Look), Fichier, Présentation, Réglages,
Raccourcis, essai (trial), déverrouiller (unlock). U+00A0 before : ; ? ! and inside « ».
Built-in theme names stay English. Inline build_pages.py tables are returned under their own keys.
"""


def build(k) -> dict:
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn : un éditeur Markdown pour Mac, avec aperçu en direct',
        "description": 'Du Markdown pour les humains qui pilotent le travail des agents : un éditeur Mac natif avec aperçu en direct, diagrammes Mermaid et export PDF. Sur le Mac App Store.',
        "intro": """
<section class="intro hero">
  <p class="kicker">Des outils de pionnier pour ceux qui construisent</p>
  <h1><span>Prenez la carte.</span> <span>Lisez l’aube.</span></h1>
  <p>Du Markdown pour les humains qui pilotent le travail des agents.</p>
</section>
""",
        "body": """
<h2 class="loop-title">Lisez ce que votre agent a écrit.</h2>
<ol class="loop-steps">
  <li><strong>L’agent écrit.</strong> Votre agent de code ou votre assistant d’écriture rédige le Markdown : un README, une spécification, des notes.</li>
  <li><strong>Vous relisez dans MarsDawn.</strong> Ouvrez le fichier et lisez-le mis en forme, avec les diagrammes Mermaid et le code en couleur, à côté de la source.</li>
  <li><strong>L’agent corrige.</strong> Demandez des modifications. Ouvrez le fichier révisé et lisez-le de la même façon.</li>
</ol>
<p><a href="/fr/reading-agent-output/">Comment relire ce que votre agent vous rend</a>.</p>
""",
    }
    pages['yours'] = {
        "title": 'Un éditeur Markdown pour Mac sans compte ni cloud · MarsDawn',
        "description": 'MarsDawn n’a ni compte, ni synchronisation, ni cloud. Vos documents Markdown restent sur votre Mac, dans les fichiers et dossiers que vous choisissez.',
        "intro": """
<section class="intro">
  <h1>Vos textes restent sur votre Mac.</h1>
  <p>MarsDawn n’a ni compte, ni synchronisation, ni cloud. L’app ouvre un fichier, vous écrivez, et elle enregistre le fichier là où vous l’avez choisi.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<ul>
  <li>Il n’y a aucun compte à créer ni aucune connexion.</li>
  <li>Rien n’est synchronisé dans un cloud. Vos documents restent là où vous les enregistrez.</li>
  <li>Rien n’est suivi. MarsDawn ne collecte aucune donnée vous concernant, et son étiquette de confidentialité sur l’App Store indique « Aucune donnée collectée ».</li>
  <li>Les images web restent bloquées jusqu’à ce que vous choisissiez de les charger : ouvrir un document n’indique donc jamais à un serveur que vous le lisez. Quand vous les chargez, c’est uniquement en https.</li>
  <li>Les images locales s’affichent dans l’aperçu dès que vous autorisez l’accès à leur dossier.</li>
</ul>
<p>Les détails se trouvent dans la <a href="/fr/privacy/">politique de confidentialité</a>.</p>
""",
    }
    pages['pay-once'] = {
        "title": 'Essayez gratuitement, puis payez une fois · MarsDawn',
        "description": 'MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.',
        "intro": """
<section class="intro">
  <h1>Essayez tout. Puis payez une fois.</h1>
  <p>MarsDawn se télécharge gratuitement. Lancez l’essai de 14 jours et toutes les fonctionnalités sont disponibles ; pour continuer ensuite, un achat unique de 4,99 USD le déverrouille. Il n’y a ni abonnement ni compte.</p>
</section>
""",
        "body": """
<h2>Comment ça marche</h2>
<ol class="loop-steps">
  <li><strong>Téléchargez-le gratuitement.</strong> MarsDawn se télécharge gratuitement sur le Mac App Store.</li>
  <li><strong>Essayez tout pendant 14 jours.</strong> Lancez l’essai et tout MarsDawn fonctionne pendant 14 jours : tous les thèmes et toutes les dispositions, l’export PDF et l’impression, ainsi que les actions Siri et Raccourcis. Coup d’œil dans le Finder fonctionne avec ou sans essai.</li>
  <li><strong>Déverrouillez-le une fois.</strong> Pour continuer ensuite, déverrouillez-le une fois pour 4,99 USD. C’est un achat intégré, pas un abonnement : rien ne se renouvelle et rien ne vous sera facturé plus tard.</li>
</ol>
<ul>
  <li>L’essai ne vous coûte rien non plus. À la fin, rien n’est acheté, sauf si vous choisissez de déverrouiller.</li>
  <li>Il n’y a pas de compte. MarsDawn ne vous demande jamais d’en créer un.</li>
</ul>
<h2>Ce qui fonctionne, et quand</h2>
<!--compare:pay-once-states-->
<p>Avant que vous lanciez l’essai, MarsDawn affiche l’offre d’essai. La lancer ne coûte rien.</p>
<p>Les fichiers PDF ouverts dans MarsDawn sont verrouillés de la même façon à la fin de l’essai.</p>
<h2>Si vous ne déverrouillez pas</h2>
<ul>
  <li>Après 14 jours, et tant que vous ne l’avez pas déverrouillé, vous ne pouvez plus lire, modifier, exporter ni imprimer de documents dans MarsDawn. Un document s’ouvre toujours, mais son contenu est masqué.</li>
  <li>Vos fichiers ne changent pas. Ce sont des fichiers ordinaires sur votre Mac, et Coup d’œil dans le Finder continue de les afficher.</li>
  <li>L’<a href="/fr/cli/">outil en ligne de commande <code>marsdawn</code></a>, gratuit, continue de les exporter en PDF, avec ou sans essai.</li>
  <li>Si un document est ouvert dans MarsDawn à la fin de l’essai, le texte saisi n’est pas perdu : utilisez Fichier ▸ Enregistrer sous… pour le garder.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Exporter du Markdown en PDF sur Mac, diagrammes compris · MarsDawn',
        "description": 'Exportez du Markdown en PDF ou imprimez-le sur votre Mac, avec les diagrammes Mermaid et le code en couleur. Les sauts de page évitent de couper les blocs de code courts et les tableaux.',
        "intro": """
<section class="intro">
  <h1>Le PDF ressemble à la page que vous avez écrite.</h1>
  <p>Exportez en PDF ou imprimez, dans les couleurs claires de votre thème. Les diagrammes et le code en couleur sont conservés, et les sauts de page évitent de séparer ce qui va ensemble.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<ul>
  <li>Les diagrammes Mermaid sont dessinés dans le PDF.</li>
  <li>Les blocs de code gardent leur coloration syntaxique.</li>
  <li>Les sauts de page évitent de laisser un titre en bas de page ou de couper du code, des tableaux et des diagrammes.</li>
  <li>Quelle que soit la disposition. L’export fonctionne même quand seule la source est affichée.</li>
</ul>
<p>L’<a href="/fr/cli/">outil en ligne de commande marsdawn</a>, gratuit, utilise le même moteur d’export : un script ou un agent IA obtient le même PDF.</p>
""",
    }
    pages['native'] = {
        "title": 'Une app Markdown native pour Mac : onglets, Coup d’œil · MarsDawn',
        "description": 'Un éditeur Markdown qui est une vraie app Mac : fenêtres et onglets natifs, enregistrement automatique, historique des versions, Coup d’œil dans le Finder et un éditeur de texte qui se comporte comme sur Mac.',
        "intro": """
<section class="intro">
  <h1>Construit avec les pièces du Mac.</h1>
  <p>Les fenêtres, les onglets, les menus et l’éditeur de texte sont ceux du Mac. La page mise en forme est dessinée par WebKit, le moteur de Safari.</p>
</section>
""",
        "body": """
<h2>Concrètement</h2>
<h3>Édition</h3>
<ul>
  <li>Dispositions source, partagée et aperçu, à une touche l’une de l’autre (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>Les deux volets défilent ensemble : le paragraphe que vous modifiez reste visible.</li>
  <li>Coloration syntaxique Markdown dans l’éditeur, assortie à votre thème de l’aperçu.</li>
</ul>
<h3>Le reste du Mac</h3>
<ul>
  <li>Fenêtres et onglets natifs, enregistrement automatique et historique des versions.</li>
  <li>Coup d’œil : appuyez sur Espace sur un fichier Markdown dans le Finder pour un aperçu, diagrammes compris.</li>
  <li>Siri et Raccourcis : commencer un nouveau document à partir d’un modèle, ajouter une ligne à la boîte de réception de vos notes ou rouvrir un document récent.</li>
  <li>Anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'Ce que MarsDawn ne fait pas · MarsDawn',
        "description": 'Pas de synchronisation, pas d’app iPhone ou iPad, pas de plug-ins, pas de comptes. Quatre thèmes intégrés. À savoir avant d’acheter.',
        "intro": """
<section class="intro">
  <h1>Ce que MarsDawn ne fait pas.</h1>
  <p>Certaines choses sont absentes à dessein. Si vous avez besoin de l’une d’elles, mieux vaut le savoir maintenant qu’après l’achat.</p>
</section>
""",
        "body": """
<h2>Ce qui est laissé de côté</h2>
<h3>Appareils et personnes</h3>
<ul>
  <li><strong>Synchronisation :</strong> MarsDawn ne synchronise pas vos documents. Ils restent là où vous les enregistrez ; pour en utiliser un sur un autre Mac, gardez-le dans un dossier que vous synchronisez déjà.</li>
  <li><strong>iPhone et iPad :</strong> il n’existe pas d’app pour eux ; MarsDawn est fait pour le Mac.</li>
  <li><strong>Partage :</strong> il n’y a ni comptes ni édition partagée, car MarsDawn est conçu pour une personne, sur son propre Mac.</li>
  <li><strong>Système :</strong> MarsDawn nécessite macOS 26 ou version ultérieure.</li>
</ul>
<h3>Fichiers et fonctionnalités</h3>
<ul>
  <li><strong>Édition :</strong> vous écrivez le Markdown à gauche et lisez la page à droite ; la page elle-même n’est pas modifiable.</li>
  <li><strong>Formats :</strong> MarsDawn exporte en PDF et imprime, mais n’exporte pas de fichiers Word.</li>
  <li><strong>Autres fichiers :</strong> les fichiers texte brut et les PDF s’ouvrent en lecture seule.</li>
  <li><strong>Thèmes :</strong> l’app est livrée avec Dawn, Classic, Modern et Vivid, chacun en clair et en sombre, et vous ne pouvez pas encore en installer d’autres ; consultez <a href="/fr/themes/">thèmes de l’aperçu et export PDF</a> pour ce qui est prévu.</li>
  <li><strong>Plug-ins :</strong> MarsDawn n’a ni plug-ins ni extensions.</li>
</ul>
<h2>Après l’essai</h2>
<p>Si vous ne déverrouillez pas MarsDawn à la fin de l’essai de 14 jours, vous ne pouvez plus y lire, modifier, exporter ni imprimer de documents : ils s’ouvrent avec leur contenu masqué. Vos fichiers restent tels quels, Coup d’œil les affiche toujours, et l’outil en ligne de commande gratuit les exporte toujours. La <a href="/fr/pay-once/">page sur l’essai et le déverrouillage</a> présente les trois étapes côte à côte.</p>
""",
    }
    pages['changelog'] = {
        "title": 'Historique des versions · MarsDawn',
        "description": 'Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn.',
        "body": """
<section class="intro">
  <h1>Historique des versions</h1>
  <p>Ce qui a changé dans l’outil en ligne de commande gratuit marsdawn. Une version de MarsDawn du Mac App Store n’est mentionnée ici que lorsqu’elle a sa propre ligne. Les versions antérieures à 0.5.1 ne sont pas listées.</p>
</section>

<h2>marsdawn 0.6.3</h2>
<p>6 octobre 2026. MarsDawn est sur le Mac App Store.</p>
<ul>
  <li>Quand l’app n’est pas installée, <code>marsdawn open</code> renvoie vers MarsDawn sur le Mac App Store.</li>
  <li>Le README et la skill pour agents expliquent <code>marsdawn open .</code> et <code>--folder</code> : MarsDawn 1.0.0 affiche le dossier dans la barre latérale de la fenêtre.</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>26 septembre 2026. Corrections Mermaid, lignes des erreurs de diagramme et installation de la skill.</p>
<ul>
  <li>Dans un diagramme de séquence, le libellé d’un message qui croise les lignes de vie d’autres participants reste lisible, dans l’aperçu comme dans les PDF exportés.</li>
  <li><code>marsdawn export</code> gère les documents remplis de diagrammes Mermaid. Un document de 50 diagrammes, qui échouait auparavant avec le code 5, s’exporte désormais.</li>
  <li><code>marsdawn export --json</code> ajoute <code>diagramErrorDetails</code>, avec les numéros de ligne de chaque erreur de diagramme : où le diagramme commence dans votre document et, quand Mermaid en indique une, la ligne de l’erreur elle-même.</li>
  <li><code>marsdawn skill --install</code> installe la skill pour Claude Code dans <code>~/.claude/skills/marsdawn/SKILL.md</code>, ou dans un autre dossier avec <code>--dir</code>. Il laisse intact un fichier identique et ne remplace un fichier différent qu’avec <code>--force</code>. Sinon, il se termine avec le code 64 (<code>skill_differs</code>) sans rien modifier.</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>25 septembre 2026. État du dossier, erreurs Mermaid complètes et petites corrections.</p>
<ul>
  <li><code>marsdawn open --folder</code> peut indiquer ce qu’il est advenu du dossier. Avec une app qui répond, il attend jusqu’à <code>--wait</code> secondes (2 par défaut), et <code>--json</code> donne un état comme <code>attached</code> ou <code>needsUser</code>.</li>
  <li>Un diagramme Mermaid qui ne s’analyse pas affiche le message d’erreur complet de Mermaid au lieu de sa seule première ligne, avec le numéro de ligne compté depuis le début de votre document.</li>
  <li>La recherche de la fin d’un bloc front matter s’arrête après 1 000 lignes : un bloc non fermé n’entraîne plus le parcours du reste d’un long document.</li>
  <li>Une app peut donner au lien de retour d’une note de bas de page un libellé traduit pour l’export PDF et l’impression. Le libellé n’est pas imprimé sur la page, et <code>marsdawn export</code> garde le libellé anglais.</li>
  <li>La copie intégrée de highlight.js est désormais épinglée par version, source et SHA-256, comme KaTeX et Mermaid.</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>24 septembre 2026. Notes de bas de page, contraste et dossiers.</p>
<ul>
  <li>Les notes de bas de page s’affichent dans les PDF exportés : appels numérotés, avec les notes après le corps du texte.</li>
  <li>Chaque thème respecte le contraste WCAG AA, en clair comme en sombre. Classic est désormais en noir et blanc.</li>
  <li><code>marsdawn skill</code> affiche la skill pour agents qui correspond au marsdawn installé.</li>
  <li><code>marsdawn open</code> se termine avec le code 6 (<code>app_cannot_open_folders</code>) quand le MarsDawn trouvé ne peut pas afficher de dossier, au lieu d’annoncer un succès.</li>
  <li>Les espaces réservés dessinés dans les pages exportées existent aussi en allemand, français, espagnol et coréen.</li>
  <li>Un espace réservé d’image n’affiche plus le chemin absolu caché derrière un très long chemin relatif.</li>
  <li><code>MARSDAWN_APP_PATH</code> n’est utilisé que s’il pointe vers une app MarsDawn.</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>19 septembre 2026. Export PDF, et ouverture d’un fichier depuis la ligne de commande.</p>
<ul>
  <li>La couche de texte d’un PDF exporté est réparée pour le chinois, le japonais et le coréen.</li>
  <li><code>marsdawn open --background</code> ouvre un fichier sans faire passer MarsDawn au premier plan.</li>
  <li><code>marsdawn open</code> accepte un dossier, et MarsDawn l’affiche dans la barre latérale de la fenêtre (MarsDawn 1.0.0 et versions ultérieures).</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn : un outil en ligne de commande gratuit pour passer de Markdown à PDF · MarsDawn',
        "description": 'L’outil en ligne de commande gratuit marsdawn pour Mac : exportez du Markdown en PDF depuis un shell, un script ou un agent LLM, avec une sortie JSON. S’installe avec Homebrew.',
        "body": f"""
<section class="intro">
  <h1>Ligne de commande</h1>
  <p>L’outil en ligne de commande gratuit <code>marsdawn</code> : exportez du Markdown en PDF depuis un shell ou un agent LLM et, si l’app MarsDawn est installée, ouvrez-y des fichiers.</p>
</section>

<div class="summary"><p><strong>marsdawn est gratuit et distribué séparément du Mac App Store.</strong> Installez-le avec Homebrew : sur un Mac avec puce Apple, il arrive prêt à l’emploi. <code>export</code> fonctionne seul ; <code>open</code> nécessite l’app MarsDawn.</p></div>

<p>Vous appelez marsdawn depuis un agent IA ou un script ? Consultez <a href="/fr/cli/agents/">marsdawn pour les agents</a> pour la sortie JSON, ses schémas et tous les codes de sortie, ou <a href="/fr/cli/mcp/">le serveur MCP</a> si votre agent appelle plutôt des outils via MCP.</p>

<h2>Installation</h2>
<p>Avec <a href="https://brew.sh">Homebrew</a> :</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>Vous utilisez un agent de code ? <a href="/fr/cli/skill/">Ajoutez la skill marsdawn</a> : un seul fichier qui lui apprend à ouvrir ce qu’il a écrit dans MarsDawn pour que vous le relisiez, et à exporter des PDF.</p>
<p>Sur un Mac avec puce Apple, Homebrew installe une copie précompilée en quelques secondes, sans rien d’autre à installer. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure (Swift 6.2). L’outil fonctionne sous macOS 15 ou version ultérieure.</p>
<p>Vous pouvez aussi le compiler à partir des <a href="{k.KIT_URL}">sources</a> avec Swift Package Manager :</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Vérifiez votre version avec <code>marsdawn --version</code>.</p>

<h2>Commandes</h2>

<h3>marsdawn open</h3>
<p>Ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour les relire. L’app doit être installée : sans elle, <code>marsdawn open</code> se termine avec le code 3 et indique que MarsDawn n’est pas installé. <code>export</code> n’a pas besoin de l’app. L’app est disponible sur le <a href="{k.LISTING_URL}">Mac App Store</a>.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code> : demande à MarsDawn d’aller à cette ligne. Une colonne après, comme dans <code>notes.md:120:8</code>, est ignorée. Si un fichier portant le nom complet existe, l’argument désigne ce fichier.</li>
  <li><code>--line &lt;n&gt;</code> : la même chose pour un seul fichier, et le moyen de demander une ligne pour un chemin qui se termine lui-même par deux-points et des chiffres. Exige exactement un fichier.</li>
  <li>Les lignes vont de 1 à 999999999.</li>
  <li>MarsDawn 1.0 ouvre le fichier à cette ligne.</li>
  <li>Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre plutôt que comme un document : <code>marsdawn open .</code> affiche le dossier courant. <code>--folder &lt;path&gt;</code> fait de même en plus de fichiers. La barre latérale d’une fenêtre affiche un seul dossier, donc en nommer deux est une erreur d’utilisation.</li>
  <li><code>--background</code> : ouvrir sans faire passer MarsDawn au premier plan.</li>
  <li><code>--json</code> : afficher un résultat JSON au lieu de texte.</li>
</ul>
<p>Les lignes sont arrivées avec marsdawn 0.3.0, les dossiers et <code>--background</code> avec la 0.5.1.</p>

<h3>marsdawn export</h3>
<p>Convertit un fichier Markdown en PDF paginé, avec le même moteur d’export que celui de MarsDawn. Il n’a pas besoin de l’app MarsDawn. Les images relatives sont résolues par rapport au dossier du fichier d’entrée.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code> : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code> : la palette claire du thème de l’aperçu. Par défaut, <code>$MARSDAWN_THEME</code>, puis <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code> : format du papier. Par défaut, <code>a4</code>.</li>
  <li><code>--allow-remote-images</code> : charger les images web pendant le rendu. Désactivé par défaut.</li>
  <li><code>--force</code> : remplacer le fichier de sortie s’il existe déjà.</li>
  <li><code>--json</code> : afficher un résultat JSON au lieu de texte.</li>
</ul>

<h2>La variable $MARSDAWN_THEME</h2>
<p>Quand <code>--theme</code> n’est pas passé, <code>export</code> lit la variable d’environnement <code>$MARSDAWN_THEME</code>. Sa valeur doit être <code>dawn</code>, <code>classic</code>, <code>modern</code> ou <code>vivid</code> ; toute autre valeur revient à <code>dawn</code>. La CLI ne lit pas le réglage de thème de l’app, car lire le conteneur d’une autre app peut déclencher une demande d’autorisation de confidentialité de macOS.</p>

<h2>Écraser des fichiers</h2>
<p><code>export</code> refuse de remplacer un fichier de sortie existant, sauf si vous passez <code>--force</code>.</p>

<h2>Codes de sortie</h2>
<!--exit-table-->
<ul>
  <li><code>0</code> : succès.</li>
  <li><code>2</code> : entrée introuvable.</li>
  <li><code>3</code> : MarsDawn n’est pas installé (<code>open</code> uniquement).</li>
  <li><code>4</code> : la sortie existe déjà (passez <code>--force</code>).</li>
  <li><code>5</code> : échec de l’export.</li>
  <li><code>6</code> : ce MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert (<code>open</code> uniquement).</li>
  <li><code>64</code> : erreur d’utilisation, notamment une ligne hors limites, <code>--line</code> avec plus d’un fichier ou avec un dossier, ou plus d’un dossier.</li>
</ul>

<h2>Sortie --json</h2>
<p>En cas de succès, <code>marsdawn open --json</code> affiche <code>ok</code>, <code>opened</code> (une liste avec le <code>path</code> de chaque fichier, plus <code>line</code> quand une ligne a été demandée), <code>app</code> (le chemin de l’app) et, quand un dossier a été donné, <code>folder</code>. <code>marsdawn export --json</code> affiche <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> et <code>diagramErrors</code>. En cas d’échec, les deux affichent <code>ok</code>, <code>error</code> et <code>message</code>.</p>
""",
    }

    figures = {
        'index': {"alt": 'MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.', "callouts": []},
        'yours': {"alt": 'MarsDawn affiche un document avec le thème Classic, l’aperçu occupant toute la fenêtre.',
                  "callouts": ['Un fichier sur votre Mac, enregistré là où vous le choisissez.', 'La barre d’outils ne contient que des thèmes et des dispositions ; il n’y a rien à quoi se connecter.']},
        'pay-once': {"alt": 'MarsDawn avec le thème Vivid, la source Markdown à gauche et la page mise en forme à droite.',
                     "callouts": ['Coloration Markdown dans l’éditeur, incluse.', 'Tous les thèmes et toutes les dispositions sont inclus.', 'Diagrammes Mermaid, inclus.', 'Coloration du code, incluse.']},
        'pdf': {"alt": 'Un PDF exporté depuis MarsDawn, ouvert dans sa visionneuse PDF avec les vignettes des pages.',
                "callouts": ['Les diagrammes Mermaid, dessinés dans le PDF.', 'Le code garde sa coloration.']},
        'native': {"alt": 'MarsDawn en vue partagée : la source Markdown à gauche, la page mise en forme à droite.',
                   "callouts": ['Une fenêtre Mac native.', 'L’éditeur de texte du Mac, avec la coloration Markdown.', '⌘1 source, ⌘2 partagé, ⌘3 aperçu.', 'La page se met à jour pendant la saisie.']},
        'limits': {"alt": 'MarsDawn en mode sombre, la source Markdown à gauche et la page mise en forme à droite.',
                   "callouts": ['Un document par fenêtre, sur ce Mac.', 'C’est ici que vous écrivez le Markdown.', 'La barre d’outils contient les thèmes et les dispositions, et il n’y a pas de menu de plug-ins.', 'La page sert à lire, pas à modifier.']},
    }
    home = {
        "cta_cli": 'Installer la CLI gratuite',
        "cta_store": 'Voir sur le Mac App Store',
        "install_h": 'À faire dès maintenant',
        "install_lede": 'L’outil en ligne de commande gratuit <code>marsdawn</code> est disponible dès aujourd’hui. Installez-le avec Homebrew :',
        "install_caps": [
            '<code>marsdawn export</code> transforme un fichier Markdown en PDF, rendu comme l’aperçu de MarsDawn. Il n’a pas besoin de l’app.',
            '<code>marsdawn open</code> ouvre des fichiers dans l’app MarsDawn pour que vous les relisiez.',
            '<code>--json</code> donne aux scripts et aux agents des résultats qu’ils peuvent analyser.',
        ],
        "proof_h": 'L’app, telle qu’elle est',
    }
    compare_tables = {
        'pay-once-states': {
            "head": ['', 'Essai (jours 1 à 14)', 'Essai terminé, non déverrouillé', 'Déverrouillé'],
            "rows": [
                ['Ouvrir un document dans MarsDawn', 'Oui', 'S’ouvre, contenu masqué', 'Oui'],
                ['Lire et modifier dans MarsDawn (source, aperçu, Mermaid, formules)', 'Oui', 'Non', 'Oui'],
                ['Exporter en PDF et imprimer depuis MarsDawn', 'Oui', 'Non', 'Oui'],
                ['Garder le texte saisi avec Fichier ▸ Enregistrer sous…', 'Oui', 'Oui, dans une fenêtre ouverte à la fin de l’essai', 'Oui'],
                ['Actions Siri et Raccourcis', 'Oui', 'Non', 'Oui'],
                ['Coup d’œil dans le Finder, avec diagrammes Mermaid et formules', 'Oui', 'Oui, sans changement', 'Oui'],
                ['<code>marsdawn export</code> (outil en ligne de commande gratuit) : PDF avec diagrammes et formules', 'Oui', 'Oui, sans changement', 'Oui'],
                ['Vos fichiers sur le disque', 'Tels que vous les avez enregistrés', 'Tels que vous les avez enregistrés ; le verrouillage ne les modifie jamais', 'Tels que vous les avez enregistrés'],
            ],
        },
    }
    exit_table_head = ['Code', 'Signification', 'Que faire']
    exit_remedy = {
        "0": 'Avec <code>--json</code>, lire l’unique ligne JSON sur stdout',
        "2": 'Vérifier le chemin et le nom du fichier',
        "3": 'Installer l’app, ou utiliser <code>export</code>, qui n’en a pas besoin',
        "4": 'Passer <code>--force</code> pour le remplacer, ou <code>-o</code> pour écrire ailleurs',
        "5": 'Lire <code>message</code> dans le résultat JSON',
        "64": 'Corriger l’option ou la valeur ; cette erreur est du texte sur stderr, même avec <code>--json</code>',
    }
    # markdown-to-pdf shows /assets/cli/plan-fr.png, which does not exist yet. Before this ships,
    # export example_plan with marsdawn 0.5.0 the way EXAMPLE_PLAN's comment in build_pages.py
    # describes, or fall back to plan-en.png with EXAMPLE_PLAN['en'].
    example_plan = '# Plan : des exports plus rapides\n\nUn agent a rédigé ce plan. Vous le relisez, puis vous le transformez en PDF.\n\n## Étapes\n\n| Étape | Responsable | État |\n|-------|-------------|------|\n| Mesurer les pages lentes | Agent | Fait |\n| Mettre en cache les diagrammes rendus | Agent | En relecture |\n\nL\'objectif est $t < 2\\,\\text{s}$ pour un document de 50 pages :\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Brouillon --> Relecture --> Publication\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'

    pages['markdown-to-pdf'] = {
        "title": 'Markdown en PDF sur Mac, en ligne de commande · MarsDawn',
        "description": 'Convertissez du Markdown en PDF sur Mac avec l’outil en ligne de commande gratuit marsdawn. Installez-le avec Homebrew et lancez une seule commande : tableaux, maths, Mermaid et code.',
        "body": f"""
<section class="intro">
  <h1>Markdown en PDF sur Mac, en ligne de commande.</h1>
  <p>L’outil gratuit <code>marsdawn</code> transforme un fichier Markdown en PDF en une seule commande. Les tableaux, les formules, les diagrammes Mermaid et le code coloré sortent tels qu’on les lit dans la source, et rien d’autre n’est nécessaire, pas même l’app MarsDawn.</p>
</section>
<h2>L’installer</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Sur un Mac à puce Apple, Homebrew installe une copie précompilée en quelques secondes. Sur un Mac Intel, il compile à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure. L’outil fonctionne sous macOS 15 ou version ultérieure, et <code>marsdawn --version</code> affiche la version installée.</p>
<h2>Enregistrer un document</h2>
<p>Collez ceci dans un fichier nommé <code>plan.md</code> :</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>L’exporter</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>Il écrit <code>plan.pdf</code> à côté de la source et indique où il l’a placé :</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>Voici cette page, capturée lors d’une véritable exécution de <code>marsdawn</code> 0.5.0 :</p>
<p><img class="pdf-page" src="/assets/cli/plan-fr.png" alt="Le PDF exporté : le titre, un tableau d’étapes, une formule dans le texte et une formule centrée, un diagramme Brouillon, Relecture, Publication et une ligne de Swift colorée." width="989" height="930"></p>
<h2>Choisir un thème, un format de papier et un nom de fichier</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code> : dawn, classic, modern ou vivid, dans les couleurs claires du thème. Sans cette option, <code>export</code> utilise <code>$MARSDAWN_THEME</code>, sinon dawn.</li>
  <li><code>--paper</code> : a4 ou letter. La valeur par défaut est a4.</li>
  <li><code>-o</code> : où écrire le PDF, au lieu de le placer à côté de la source.</li>
  <li><code>--allow-remote-images</code> : charge les images du web pendant le rendu. Elles restent désactivées si vous ne le précisez pas.</li>
</ul>
<h2>Si ça ne fonctionne pas</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew compile <code>marsdawn</code> à partir des sources, comme sur un Mac Intel. Installez Xcode 26 ou version ultérieure depuis l’App Store, puis relancez l’installation.</li>
  <li><code>marsdawn: No such file: …</code> Le chemin ne mène pas à un fichier. Vérifiez le nom, ou lancez la commande depuis le dossier qui contient le fichier.</li>
  <li><code>… already exists. Pass --force to replace it.</code> Un PDF portant ce nom existe déjà. Ajoutez <code>--force</code> pour le remplacer, ou <code>-o</code> pour l’écrire ailleurs.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> Le thème ou le format de papier n’est pas reconnu. Les thèmes sont dawn, classic, modern et vivid ; le papier est a4 ou letter.</li>
</ul>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Toutes les options et le JSON produit : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Pour qu’un agent de code le fasse à votre place : <a href="/fr/cli/skill/">la compétence d’agent marsdawn</a>.</li>
  <li>Les quatre thèmes d’aperçu, et la direction que prend l’export PDF : <a href="/fr/themes/">thèmes d’aperçu et export PDF</a>.</li>
  <li>Remettre le PDF à quelqu’un qui n’utilise pas Markdown : <a href="/fr/sharing-exported-pdfs/">partager un PDF</a>.</li>
</ul>
""",
    }

    pages['view-markdown-on-mac'] = {
        "title": 'Comment afficher un fichier Markdown sur Mac · MarsDawn',
        "description": 'Un fichier .md est du texte brut avec des marques de mise en forme. Voici comment le lire rendu sur Mac : en PDF avec l’outil en ligne de commande gratuit marsdawn dès aujourd’hui, et dans l’app MarsDawn, sur le Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>Comment afficher un fichier Markdown sur Mac.</h1>
  <p>Un fichier <code>.md</code> est du texte brut. Les titres, les mots en gras, les tableaux et les diagrammes y sont écrits sous forme de marques : <code>#</code> pour un titre, <code>**</code> autour du gras, des barres verticales pour un tableau, un bloc de code <code>mermaid</code> pour un diagramme. Ouvrez-le dans un éditeur de texte brut et vous lisez les marques. Pour lire la page telle que l’auteur l’a voulue, il faut qu’un outil en fasse le rendu.</p>
</section>
<h2>Dès aujourd’hui, gratuitement : en faire un PDF</h2>
<p>L’outil en ligne de commande gratuit <code>marsdawn</code> fait le rendu d’un fichier Markdown en PDF, que n’importe quel Mac peut ouvrir. Les tableaux, les formules, les diagrammes Mermaid et le code coloré sont rendus, et rien d’autre n’est nécessaire, pas même l’app MarsDawn.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> écrit <code>notes.pdf</code> à côté du fichier Markdown, et <code>open</code> l’affiche dans votre lecteur PDF. macOS 15 ou version ultérieure est requis. Le pas-à-pas, avec une vraie page exportée, se trouve sur <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</p>
<h2>Le lire dans MarsDawn</h2>
<p>MarsDawn est un éditeur Markdown pour Mac, sur le Mac App Store. Ouvrez un fichier <code>.md</code> et lisez la page rendue à côté de la source :</p>
<ul>
  <li>L’aperçu se met à jour pendant la saisie, et les deux volets défilent ensemble.</li>
  <li>Les organigrammes et diagrammes de séquence Mermaid sont dessinés dans l’aperçu, et les blocs de code sont colorés.</li>
  <li>Dans le Finder, appuyez sur Espace sur un fichier Markdown pour un aperçu Coup d’œil, diagrammes compris.</li>
  <li>Quand vous voulez modifier quelque chose, la source est juste là. MarsDawn est un éditeur, pas seulement une visionneuse.</li>
</ul>
<p>Si un agent IA a rédigé le fichier, c’est la boucle pour laquelle MarsDawn est conçu : l’agent écrit, vous lisez le rendu, et il révise. Consultez <a href="/fr/">la page d’accueil</a>, ainsi que <a href="/fr/cli/agents/">marsdawn pour les agents</a> pour laisser un agent ouvrir des fichiers à votre place. Pour comprendre pourquoi cette lecture compte et comment relire un plan, consultez <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a> et <a href="/fr/reviewing-agent-plans/">Relire le plan d’un agent en cinq minutes</a>.</p>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Toutes les options de l’outil en ligne de commande : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Ce que MarsDawn ne fait pas : <a href="/fr/limits/">la liste</a>.</li>
  <li>Lire du Markdown plutôt dans VS Code, un navigateur ou Claude Desktop : <a href="/fr/vs/markdown-preview-tools/">la comparaison</a>.</li>
</ul>
""",
    }

    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer ou MarsDawn : une visionneuse ou un éditeur · MarsDawn',
        "description": 'MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer ou MarsDawn.</h1>
  <p>Ce sont deux apps Mac pour lire du Markdown rendu. MacMD Viewer ouvre un fichier <code>.md</code> et affiche la page finie ; il ne permet pas de la modifier. MarsDawn place un éditeur à côté du même type d’aperçu rendu, pour écrire et relire dans une seule fenêtre. Voici leurs différences, fonction par fonction.</p>
</section>
<h2>Si vous devez seulement lire, pas modifier</h2>
<p>Si votre travail consiste uniquement à lire du Markdown écrit par d’autres, sans jamais toucher à la source, MacMD Viewer est un choix raisonnable : il est conçu exactement pour cela, il est disponible dès maintenant et fonctionne sur des versions plus anciennes de macOS. MarsDawn vaut la peine dès que la lecture n’est pas tout le travail, car le Markdown d’un agent revient en général pour une nouvelle passe.</p>
<h2>Ce que fait chaque app</h2>
<!--compare:macmd-features-->
<h2>Prix et mode d’achat</h2>
<!--compare:macmd-buying-->
<h2>Essayez-le gratuitement dès aujourd’hui</h2>
<p>MarsDawn est sur le Mac App Store. L’outil en ligne de commande gratuit <code>marsdawn</code> fait aussi le rendu de n’importe quel fichier Markdown en PDF, avec les diagrammes Mermaid et le code coloré, et rien d’autre n’est nécessaire :</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Pour aller plus loin</h2>
<ul>
  <li>Le pas-à-pas complet : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Ce que MarsDawn ne fait pas : <a href="/fr/limits/">la liste</a>.</li>
  <li>Toutes les options de l’outil en ligne de commande : <a href="/fr/cli/">Ligne de commande</a>.</li>
  <li>Par rapport à la lecture du Markdown dans VS Code, un navigateur ou Claude Desktop : <a href="/fr/vs/markdown-preview-tools/">la comparaison</a>.</li>
</ul>
""",
    }

    compare_tables['macmd-features'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Modification', 'Lecture seule, par choix', 'Modifie la source, avec la page rendue à côté'],
            ['Thèmes d’aperçu', '12 thèmes de document', '4 thèmes, chacun avec une palette claire et une palette sombre'],
            ['Diagrammes et maths', 'Mermaid et coloration du code ; sa fiche ne mentionne pas les maths', 'Mermaid, coloration du code et maths KaTeX'],
            ['Coup d’œil dans le Finder', 'Oui', 'Oui'],
            ['PDF et impression', 'Oui', 'Oui'],
            ['Configuration requise', 'macOS 14 (Sonoma) ou version ultérieure', 'macOS 26 (Tahoe) ou version ultérieure'],
            ['Langues de l’interface', 'Non précisé dans ses propres documents', '{langs}'],
        ],
    }
    compare_tables['macmd-buying'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Où l’acheter', 'Son propre site, Homebrew ou Setapp ; pas le Mac App Store', 'Uniquement sur le Mac App Store'],
            ['Prix', '19,99 USD une seule fois, pour un Mac ; les packs multi-Mac coûtent plus cher', 'Téléchargement gratuit, puis 4,99 USD une seule fois'],
            ['L’essayer d’abord', 'Pas d’essai ; garantie de remboursement de 14 jours pour les achats directs', 'Un essai gratuit de 14 jours'],
            ['Remboursements et mises à jour', 'Via son propre site', 'Via Apple'],
            ['Compte requis', 'Non', 'Non'],
        ],
    }

    schema_notes = {
        "export": "succès de export",
        "open": "succès de open, marsdawn 0.5.1 et versions ultérieures, y compris un dossier affiché dans la barre latérale",
        "open_v2": "succès de open, marsdawn 0.3.0 à 0.5.0",
        "error": "échec, pour les deux commandes, marsdawn 0.5.2 et versions ultérieures",
        "open_v1": "succès de open, marsdawn 0.2.x, où <code>opened</code> était une liste de chemins",
        "error_v1": "échec, pour les deux commandes, marsdawn 0.5.1 et versions antérieures",
    }

    pages['cli/agents'] = {
        "title": 'marsdawn pour les agents : Markdown en PDF depuis des scripts · MarsDawn',
        "description": 'Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.',
        "body": f"""
<section class="intro">
  <h1>marsdawn pour les agents</h1>
  <p>Une référence pour les agents IA et les scripts qui appellent l’outil en ligne de commande <code>marsdawn</code>. Chaque exemple de cette page a été exécuté avec l’outil compilé à partir des sources actuelles.</p>
</section>

<div class="summary"><p><strong>Pour convertir un fichier Markdown en PDF, lancez <code>marsdawn export notes.md --json</code> et lisez un objet JSON sur stdout.</strong> Les diagrammes Mermaid et le code coloré sont rendus de la même façon que dans l’app MarsDawn. <code>export</code> n’a pas besoin de l’app ; <code>open</code>, si.</p></div>

<h2>Ce qu’il fait</h2>
<ul>
  <li><code>export</code> fait le rendu d’un fichier Markdown en un PDF paginé, avec le même moteur d’export que l’app MarsDawn. Aucune fenêtre ne s’ouvre.</li>
  <li><code>open</code> ouvre un ou plusieurs fichiers Markdown dans l’app MarsDawn pour qu’une personne les relise ; il peut indiquer la ligne à laquelle chaque fichier doit s’ouvrir et afficher un dossier dans la barre latérale de la fenêtre.</li>
</ul>

<h2>Ce qu’il ne fait pas</h2>
<ul>
  <li>Il ne lit pas le Markdown depuis stdin. Passez un chemin de fichier.</li>
  <li>Il n’écrit pas le PDF sur stdout. Le PDF va toujours dans un fichier ; stdout ne contient que le résultat.</li>
  <li>Il ne remplace pas un fichier existant, sauf si vous passez <code>--force</code>.</li>
  <li>Il ne charge pas d’images depuis le web, sauf si vous passez <code>--allow-remote-images</code>, et uniquement en https.</li>
  <li><code>open</code> ne fonctionne pas sans l’app MarsDawn installée ; il se termine avec le code 3. <code>export</code> n’a pas besoin de l’app. L’app est sur le <a href="{k.LISTING_URL}">Mac App Store</a>.</li>
  <li>MarsDawn 1.0 ouvre le fichier à la ligne indiquée par <code>open</code>.</li>
  <li>Il ne fonctionne que sous macOS.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Écrit <code>notes.pdf</code> à côté de <code>notes.md</code>. Options :</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code> : où écrire le PDF. Par défaut, le chemin d’entrée avec l’extension <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code> : la palette claire du thème. Par défaut <code>$MARSDAWN_THEME</code>, sinon <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code> : format du papier. Par défaut <code>a4</code>.</li>
  <li><code>--allow-remote-images</code> : charge les images https du web pendant le rendu.</li>
  <li><code>--force</code> : remplace le fichier de sortie s’il existe.</li>
  <li><code>--json</code> : affiche un objet JSON sur stdout au lieu de texte.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Succès, code de sortie 0 :</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code> : chemin absolu du PDF écrit.</li>
  <li><code>pages</code> : nombre de pages.</li>
  <li><code>theme</code> et <code>paper</code> : les valeurs utilisées.</li>
  <li><code>diagramErrors</code> : un message par diagramme Mermaid dont le rendu a échoué. Le PDF est tout de même écrit.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> indique la ligne à laquelle s’ouvrir. Une colonne après, comme dans <code>notes.md:120:8</code>, est ignorée. Un argument qui désigne un fichier existant est toujours ce nom de fichier entier : un fichier nommé <code>weird:12</code> s’ouvre donc tel quel.</li>
  <li><code>--line &lt;n&gt;</code> indique la ligne pour un seul fichier, y compris un chemin qui se termine lui-même par deux-points et des chiffres. Il faut exactement un fichier.</li>
  <li>Les lignes vont de 1 à 999999999. Toute autre valeur est une erreur d’utilisation.</li>
  <li>Les lignes ont été ajoutées dans marsdawn 0.3.0. MarsDawn 1.0 ouvre le fichier à cette ligne.</li>
  <li>Un dossier passé en argument s’ouvre dans la barre latérale de la fenêtre et non comme document : <code>marsdawn open .</code> affiche donc le dossier courant ; <code>--folder &lt;path&gt;</code> fait de même en plus des fichiers. La barre latérale d’une fenêtre affiche un seul dossier : en indiquer deux est une erreur d’utilisation, tout comme utiliser <code>--folder</code> deux fois, même pour le même dossier ; le même dossier redonné en argument compte une seule fois. <code>--line</code> avec un dossier est une erreur d’utilisation, puisqu’un dossier n’a pas de ligne. Il n’y a pas de <code>-a</code> : le passer est une erreur d’utilisation qui renvoie à <code>--folder</code>.</li>
  <li><code>--background</code> ouvre sans faire passer MarsDawn au premier plan, pour un agent qui ouvre des fichiers pendant que la personne travaille ailleurs. Le JSON est le même dans les deux cas.</li>
  <li>Les dossiers et <code>--background</code> ont été ajoutés dans marsdawn 0.5.1.</li>
</ul>
<p>Succès, code de sortie 0 :</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code> : un objet par fichier, dans l’ordre donné. <code>path</code> est le chemin absolu du fichier ; <code>line</code> n’apparaît que si une ligne a été demandée.</li>
  <li><code>app</code> : chemin de l’app MarsDawn qui les a ouverts.</li>
</ul>
<p>Avec un dossier (marsdawn 0.5.1 et versions ultérieures), code de sortie 0 :</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code> : présent seulement si un dossier a été donné. <code>path</code> est son chemin absolu. <code>requested</code> vaut toujours <code>true</code> : marsdawn a demandé à MarsDawn d’afficher le dossier, mais ne peut pas savoir si la barre latérale l’affiche, car l’app peut d’abord demander l’accès à la personne. Signalez-le comme demandé, pas comme fait.</li>
  <li><code>opened</code> est vide si seul un dossier a été donné.</li>
</ul>
<p>marsdawn 0.2.x affichait <code>opened</code> sous forme de liste de chemins. Vérifiez <code>marsdawn --version</code> si vous devez gérer les deux.</p>

<h2>Ouvrir les fichiers à mesure que Claude Code les modifie</h2>
<p>Un <a href="https://code.claude.com/docs/en/hooks">hook Claude Code</a> facultatif : après que Claude a écrit ou modifié un fichier Markdown, il ouvre ce fichier dans MarsDawn en arrière-plan, une fois par fichier et par session. Il est désactivé tant que vous ne l’ajoutez pas, projet par projet, car une fenêtre que vous n’avez pas demandée détourne l’attention. Il exécute une commande shell et ne coûte aucun token de modèle.</p>
<p>Il nécessite marsdawn 0.5.1 ou version ultérieure, pour <code>--background</code>, ainsi que l’app MarsDawn.</p>
<p>Enregistrez ceci sous <code>.claude/hooks/marsdawn-open.sh</code> dans votre projet, et rendez-le exécutable avec <code>chmod +x</code> :</p>
<pre><code>#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2&gt;/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2&gt;/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || {{ [ -x /opt/homebrew/bin/marsdawn ] &amp;&amp; echo /opt/homebrew/bin/marsdawn; }}) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${{TMPDIR:-/tmp}}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2&gt;/dev/null &amp;&amp; exit 0
echo "$file" &gt;&gt; "$seen"

"$marsdawn" open --background "$file" &gt;/dev/null 2&gt;&amp;1 || true
exit 0</code></pre>
<p>Ajoutez ensuite le hook à <code>.claude/settings.json</code> dans le projet, ou à <code>.claude/settings.local.json</code> pour le garder pour vous :</p>
<pre><code>{{
  "hooks": {{
    "PostToolUse": [
      {{
        "matcher": "Write|Edit",
        "hooks": [
          {{ "type": "command", "command": "\\"$CLAUDE_PROJECT_DIR\\"/.claude/hooks/marsdawn-open.sh" }}
        ]
      }}
    ]
  }}
}}</code></pre>
<ul>
  <li>Il s’exécute après les outils Write et Edit de Claude. Les fichiers qui ne se terminent pas par <code>.md</code> ou <code>.markdown</code> sont ignorés.</li>
  <li>Chaque fichier s’ouvre une fois par session Claude Code, quel que soit le nombre de modifications. La liste se trouve dans <code>$TMPDIR/marsdawn-hook/</code>, un fichier par session : une nouvelle session rouvre donc le fichier.</li>
  <li><code>--background</code> empêche MarsDawn de passer au premier plan : la fenêtre dans laquelle vous travailliez garde le focus.</li>
  <li>Il ne gêne jamais Claude. Chaque chemin se termine avec 0, et si marsdawn ou l’app MarsDawn n’est pas installé, rien ne se passe.</li>
  <li>Il lit l’entrée du hook avec <code>/usr/bin/jq</code>, fourni avec macOS 26, la version dont l’app MarsDawn a besoin.</li>
  <li>Pour le désactiver, supprimez l’entrée du fichier de réglages.</li>
</ul>

<h2>Échecs</h2>
<p>Avec <code>--json</code>, un échec affiche un objet JSON sur stdout et se termine avec son code :</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code> : l’entrée n’existe pas, est un dossier ou n’est pas du texte UTF-8 ; ou un chemin <code>--folder</code> n’existe pas ou n’est pas un dossier.</li>
  <li><code>3</code>, <code>app_not_installed</code> : MarsDawn n’est pas installé. Seul <code>open</code> renvoie ce code.</li>
  <li><code>4</code>, <code>output_exists</code> : le fichier de sortie existe. Passez <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code> : l’export lui-même a échoué.</li>
  <li><code>6</code>, <code>app_cannot_open_folders</code> : cette version de MarsDawn ne peut pas afficher de dossier, donc rien n’a été ouvert. Seul <code>open</code> renvoie ce code.</li>
  <li><code>64</code> : erreur d’utilisation, comme une option inconnue, une valeur non valide, une ligne hors limites, <code>--line</code> avec plus d’un fichier ou avec un dossier, plus d’un dossier, ou <code>-a</code>. Celle-ci s’affiche en texte sur stderr, même avec <code>--json</code>.</li>
</ul>

<h2>Schémas JSON</h2>
<p>JSON Schema (draft 2020-12) pour chaque résultat <code>--json</code> :</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>Variables d’environnement</h2>
<ul>
  <li><code>MARSDAWN_THEME</code> : le thème qu’utilise <code>export</code> quand <code>--theme</code> n’est pas passé. Une valeur inconnue revient à <code>dawn</code> sans erreur.</li>
</ul>

<h2>Configuration requise</h2>
<ul>
  <li>L’outil fonctionne sous macOS 15 ou version ultérieure. Sur puce Apple, Homebrew installe un bottle précompilé et rien d’autre n’est nécessaire. Le compiler vous-même, sur un Mac Intel ou à partir des sources, nécessite Swift 6.2 ou version ultérieure, fourni avec Xcode 26 ou version ultérieure.</li>
  <li>L’app MarsDawn nécessite macOS 26 ou version ultérieure.</li>
</ul>

<h2>Installation</h2>
<p>Avec Homebrew. Sur puce Apple, il installe un bottle précompilé en quelques secondes, sans Xcode. Sur un Mac Intel, il compile marsdawn à partir des sources, ce qui prend quelques minutes et nécessite Xcode 26 ou version ultérieure.</p>
<pre><code>brew tap redtear1115/tap && brew install marsdawn
marsdawn --version</code></pre>
<p>Ou compilez-le à partir <a href="{k.KIT_URL}">des sources</a>. La première compilation récupère les dépendances et compile, ce qui prend aussi quelques minutes.</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> affiche le numéro de version, par exemple <code>0.3.0</code>, et se termine avec le code 0.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Une compétence en un seul fichier pour les agents qui lisent des instructions plutôt qu’un shell : <a href="/fr/cli/skill/">la compétence marsdawn</a>.</li>
  <li>Un serveur MCP qui enveloppe ce même <code>export</code> : <a href="/fr/cli/mcp/">marsdawn-mcp</a>.</li>
  <li>Pourquoi ce résultat JSON reste économique pour le contexte de l’agent : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
</ul>
""",
    }

    pages['cli/skill'] = {
        "title": 'Une compétence d’agent de code pour convertir Markdown en PDF · MarsDawn',
        "description": 'Un fichier que votre agent de code charge pour ouvrir dans MarsDawn le Markdown qu’il a écrit, afin que vous le relisiez, et pour installer marsdawn, exporter du Markdown en PDF et lire le résultat JSON.',
        "body": f"""
<section class="intro">
  <h1>Laissez votre agent vous montrer ce qu’il a écrit, et produire le PDF.</h1>
  <p>Cette compétence tient en un fichier Markdown. Elle apprend à un agent de code à ouvrir dans MarsDawn un document qu’il a écrit pour que vous le relisiez, et à installer <code>marsdawn</code>, vérifier qu’il fonctionne, exporter un document en PDF et lire le résultat.</p>
</section>
<div class="summary"><p><strong>Un seul fichier Markdown, dans <code>~/.claude/skills/marsdawn/SKILL.md</code>.</strong> Avec lui, votre agent installe <code>marsdawn</code>, exporte en PDF et lit le résultat JSON, et il demande toujours avant d’exécuter quoi que ce soit.</p></div>
<h2>L’installer dans Claude Code</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code la charge quand une tâche demande un PDF, ou quand il a écrit ou révisé un document Markdown que vous allez lire, et vous pouvez la lancer vous-même avec <code>/marsdawn</code>. C’est <a href="/cli/skill/SKILL.md">un fichier court</a> : lisez-le avant de l’installer.</p>
<p>D’autres agents peuvent utiliser le même fichier. C’est du Markdown brut, des instructions et des commandes : indiquez l’URL à votre agent ou collez le contenu.</p>
<h2>Ce qu’elle enseigne</h2>
<ul>
  <li>Installer <code>marsdawn</code> avec Homebrew s’il manque, puis le vérifier avec <code>marsdawn --version</code> au lieu de supposer une version.</li>
  <li>Exporter avec <code>marsdawn export … --json</code> et lire le résultat : où est allé le PDF, combien de pages il compte, et quel diagramme Mermaid n’a pas pu être rendu.</li>
  <li>Distinguer les échecs par leur code de sortie : fichier introuvable, PDF déjà présent, export échoué, option incorrecte.</li>
  <li>Ouvrir un document qu’il a écrit avec <code>marsdawn open file.md:line</code>, sur sa première modification, et une seule fois : les modifications suivantes apparaissent d’elles-mêmes dans la fenêtre ouverte.</li>
  <li>Si l’app MarsDawn n’est pas installée, le dire une fois et continuer, sans réessayer. Ne jamais utiliser <code>open</code> pour produire un PDF.</li>
  <li>Avec <code>--folder</code> (marsdawn 0.5.1 et versions ultérieures), signaler le dossier comme demandé, pas comme affiché : c’est l’app qui décide, et rien ne le confirme.</li>
</ul>
<h2>Ce qu’elle ne fait pas</h2>
<ul>
  <li>Elle ne s’accorde pas elle-même la permission d’exécuter quoi que ce soit. Votre agent demande toujours avant d’installer <code>marsdawn</code> ou de le lancer, comme pour n’importe quelle autre commande.</li>
  <li>Elle n’envoie vos documents nulle part. <code>marsdawn</code> fait le rendu sur votre Mac et laisse de côté les images du web, sauf si vous passez <code>--allow-remote-images</code>.</li>
</ul>
<p>Le contrat complet, chaque champ et chaque code, se trouve dans <a href="/fr/cli/agents/">marsdawn pour les agents</a>. Pour un agent qui appelle des outils via MCP plutôt que de lire un fichier de compétence, il existe aussi <a href="/fr/cli/mcp/">un serveur MCP</a>.</p>
""",
    }

    pages['cli/mcp'] = {
        "title": 'Trois façons d’appeler marsdawn : CLI, fichier de compétence, serveur MCP · MarsDawn',
        "description": 'marsdawn n’a pas de modèle d’IA à lui : peu importe quel agent a écrit le Markdown. Appelez-le depuis la CLI, un fichier de compétence ou le serveur MCP marsdawn-mcp : tous trois lancent le même export.',
        "body": f"""
<section class="intro">
  <h1>Trois façons d’appeler marsdawn.</h1>
  <p>MarsDawn n’a pas de modèle d’IA à lui : il est conçu pour relire du Markdown, pas pour en écrire, donc peu importe quel agent ou quel modèle a produit le fichier. Un agent ou un script peut appeler <code>marsdawn</code> de trois façons, et toutes les trois finissent par lancer le même <code>export</code>.</p>
</section>

<div class="summary"><p><strong>Choisissez ce que vos outils prennent en charge : la CLI gratuite <code>marsdawn</code>, un fichier de compétence en Markdown brut, ou le serveur MCP <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>.</strong> Tous trois appellent le même <code>marsdawn export</code> et renvoient le même résultat JSON.</p></div>

<h2>Laquelle utiliser</h2>
<!--compare:mcp-choice-->

<h2>La CLI</h2>
<p><code>marsdawn export notes.md --json</code> peut être appelé par tout agent ou script capable de lancer une commande shell : il est indépendant du modèle par construction. Chaque champ qu’il renvoie est documenté dans <a href="/fr/cli/agents/">marsdawn pour les agents</a>, la référence pour le schéma JSON vers laquelle renvoient les deux autres options ci-dessous.</p>

<h2>Le fichier de compétence</h2>
<p>Pour un agent qui lit des instructions en Markdown brut au lieu d’appeler directement un shell (aujourd’hui, Claude Code), <a href="/fr/cli/skill/">la compétence marsdawn</a> est un fichier qui lui apprend à installer marsdawn, lancer <code>export</code> et lire le résultat. C’est du Markdown brut : d’autres agents qui chargent des fichiers d’instructions peuvent utiliser le même.</p>

<h2>Le serveur MCP</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> est un dépôt séparé, public, sous licence Apache-2.0. C’est un serveur MCP doté de deux outils, <code>export_markdown_to_pdf</code> et <code>open_in_marsdawn</code>, qui enveloppent <code>marsdawn export --json</code> et <code>marsdawn open --json</code> : pointez un client MCP vers lui, et un appel d’outil renvoie le même JSON que la CLI.</p>
<ul>
  <li><strong>Où l’obtenir :</strong> sous forme de MCP Bundle, <code>marsdawn.mcpb</code>, joint à <a href="https://github.com/redtear1115/marsdawn-mcp/releases">sa release GitHub</a>, ou en lançant le serveur depuis les sources via stdio.</li>
  <li><strong>Registre :</strong> pas encore référencé dans le MCP Registry (version actuelle : 0.2.1). Vérifiez l’état actuel dans le dépôt avant de compter sur la découverte via le registre.</li>
  <li><strong>Hébergement :</strong> auto-hébergé uniquement. Il n’existe pas de service marsdawn-mcp hébergé ; le serveur tourne sur votre propre machine, à côté de marsdawn.</li>
  <li><strong>Configuration requise :</strong> macOS, marsdawn 0.5.0 ou version ultérieure, et Node.js 20 ou version ultérieure pour lancer le serveur.</li>
</ul>

<h2>Limité aux dossiers que vous autorisez</h2>
<p>Les deux outils n’accèdent qu’aux dossiers que vous autorisez : le réglage <strong>Allowed folders</strong> de l’extension, vide au départ et sans valeur prédéfinie, ou à défaut les racines que propose votre client MCP. Si aucun des deux n’est défini, chaque appel est refusé, et le message de refus explique comment y remédier. Chaque chemin doit être absolu, et <code>export_markdown_to_pdf</code> n’écrit jamais qu’un fichier <code>.pdf</code>, jamais à travers un lien symbolique.</p>
<p><strong>Sécurité :</strong> passez à la version <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>. Avec 0.1.0 et 0.2.0, un appel pouvait écrire un PDF à n’importe quel emplacement accessible en écriture à votre compte ; corrigé sous la référence <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a>.</p>

<h2>Le même export, trois portes</h2>
<p>Quelle que soit la porte d’entrée, le comportement de fond ne change pas : le même moteur d’export, les mêmes thèmes et formats de papier, les mêmes <code>diagramErrors</code> quand un diagramme Mermaid ne peut pas être rendu. Cette page ne répète pas ce contrat ; <a href="/fr/cli/agents/">marsdawn pour les agents</a> le décrit en entier.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Le schéma JSON complet et chaque code de sortie : <a href="/fr/cli/agents/">marsdawn pour les agents</a>.</li>
  <li>La compétence en un seul fichier pour Claude Code et les agents similaires : <a href="/fr/cli/skill/">la compétence marsdawn</a>.</li>
  <li>Pourquoi un résultat JSON compact compte pour le contexte de votre agent : <a href="/fr/token-efficient-review/">une relecture économe en tokens</a>.</li>
</ul>
""",
    }

    pages['vs/markdown-preview-tools'] = {
        "title": 'Afficher du Markdown ailleurs ou dans MarsDawn · MarsDawn',
        "description": 'MarsDawn comparé à la lecture du Markdown dans l’aperçu intégré de VS Code, une extension de navigateur ou l’aperçu de fichiers de Claude Desktop : ce que chacun affiche, et ce qu’il faut pour ouvrir un fichier.',
        "body": f"""
<section class="intro">
  <h1>Afficher du Markdown ailleurs, ou dans MarsDawn.</h1>
  <p>Si VS Code, un navigateur ou Claude Desktop est déjà ouvert, il est logique de s’en servir pour jeter un œil à un fichier Markdown. Voici ce que chacun affiche réellement, et ce qu’il en coûte pour y arriver, comparé à l’ouverture du même fichier dans MarsDawn.</p>
</section>

<h2>En un coup d’œil</h2>
<!--compare:preview-tools-->

<h2>L’aperçu intégré de VS Code</h2>
<p>Appuyez sur <kbd>&#8984;&#8679;V</kbd> dans VS Code et il fait le rendu du fichier Markdown dans un volet d’aperçu intégré, gratuitement, sans rien installer. Depuis VS Code 1.121 (mai 2026), cet aperçu affiche aussi les diagrammes Mermaid nativement : Microsoft a intégré une extension Mermaid à VS Code lui-même, alors qu’il fallait auparavant une extension séparée. Ce qu’il ne fait pas : c’est un volet d’aperçu à l’intérieur d’un éditeur, pas un éditeur conçu pour la lecture. Le volet se trouve à côté d’une arborescence de fichiers, d’un terminal et de tous les autres panneaux que VS Code peut afficher, et VS Code lui-même est une app Electron qu’on installe comme un environnement de développement complet, pas quelque chose qu’on ouvre pour lire un fichier.</p>

<h2>Une extension de navigateur pour les fichiers locaux</h2>
<p>Aucune extension de navigateur ne s’impose pour lire un fichier <code>.md</code> local : Local Markdown Viewer, Markdown Viewer, MarkView et d’autres font à peu près la même chose, et aucune n’est installée par défaut. Toutes ont besoin de la même étape supplémentaire avant de pouvoir ouvrir quoi que ce soit : activer « Autoriser l’accès aux URL de fichier » pour l’extension, car les navigateurs empêchent par défaut les extensions de lire les pages <code>file://</code>. C’est une autorisation que l’on accorde une fois par extension, et on oublie facilement qu’on l’a fait, ou pourquoi. Une fois activée, le fichier s’affiche dans un onglet du navigateur : il faut donc faire tourner un navigateur complet pour regarder un fichier.</p>

<h2>L’aperçu de fichiers de Claude Desktop</h2>
<p>Claude Desktop affiche un fichier qui se trouve déjà dans un projet ou une conversation. Ce pour quoi il n’est pas conçu, c’est parcourir des fichiers quelconques sur le disque : vous pouvez regarder ce que la conversation contient déjà, pas un dossier de notes que vous gardez ouvert à côté de votre travail. La liste d’Anthropic <a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">des types de documents que l’on peut importer</a> comprend PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON et XLSX : Markdown n’y figure pas.</p>

<h2>Un moteur de navigateur pour lire un fichier</h2>
<p>VS Code est une app Electron : un Chromium et un environnement Node.js embarqués, pas une app Mac native. L’extension de navigateur, elle, tourne dans un vrai navigateur. Dans les deux cas, afficher un fichier Markdown suppose de faire tourner un moteur de navigateur complet. MarsDawn est une app AppKit native : pas de navigateur embarqué ; elle ouvre directement n’importe quel fichier local, sans extension à installer ni autorisation à retenir.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Ce que MarsDawn ne fait pas non plus : <a href="/fr/limits/">la liste</a>.</li>
  <li>Transformer n’importe quel fichier Markdown en PDF dès aujourd’hui, gratuitement : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Par rapport à une visionneuse Mac native : <a href="/fr/vs/macmd-viewer/">MacMD Viewer ou MarsDawn</a>.</li>
</ul>
""",
    }

    pages['themes'] = {
        "title": 'Thèmes d’aperçu et export PDF dans MarsDawn · MarsDawn',
        "description": 'Quatre thèmes d’aperçu, chacun avec une palette claire et une palette sombre, et un seul export PDF et impression qui suit celui que vous utilisez. D’autres thèmes importables et une galerie pour partager les vôtres sont prévus.',
        "body": f"""
<section class="intro">
  <h1>Huit apparences, un seul export.</h1>
  <p>MarsDawn propose quatre thèmes d’aperçu, Dawn, Classic, Modern et Vivid, chacun avec une palette claire et une palette sombre : huit combinaisons pour lire un document. Exportez en PDF ou imprimez, et la page sort dans celle que vous lisiez.</p>
</section>

<div class="summary"><p><strong>Quatre thèmes &#215; clair et sombre = huit façons de lire un document, et un seul chemin d’export qui suit votre choix.</strong> D’autres thèmes importables et une galerie pour partager les vôtres sont prévus, mais pas encore réalisés.</p></div>

<h2>Les quatre thèmes</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Dawn</strong>, le thème par défaut : le même papier chaleureux et le même accent Mars Rust que ce site.</li>
  <li><strong>Classic</strong> : une palette plus sobre, proche d’un document.</li>
  <li><strong>Modern</strong> : une palette plus froide et plus contemporaine.</li>
  <li><strong>Vivid</strong> : une palette plus lumineuse et plus contrastée.</li>
</ul>
<p>Chacun a sa propre variante claire et sombre : changer l’apparence de votre Mac change aussi la palette du thème, pas seulement l’interface autour.</p>

<h2>L’export PDF et l’impression utilisent le même thème</h2>
<p>Exportez en PDF ou imprimez, et la page utilise la palette claire de votre thème : les diagrammes Mermaid y sont dessinés, les blocs de code gardent leur coloration syntaxique, et les sauts de page évitent de séparer un titre de sa section ou de couper un tableau ou un diagramme en deux. L’<a href="/fr/cli/">outil en ligne de commande marsdawn</a>, gratuit, utilise le même moteur d’export : un script ou un agent produit donc le même PDF, dans n’importe lequel des quatre thèmes, avec <code>--theme</code>.</p>

<h2>Prévu : plus de thèmes, et une galerie</h2>
<p>À venir, pas encore disponible : d’autres thèmes d’aperçu importables, et une galerie sur ce site où chacun pourra proposer les siens. <code>/themes/v1/</code> est déjà réservé pour cela. D’ici là, MarsDawn dispose des quatre thèmes intégrés, et vous ne pouvez pas en installer d’autres.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Le pas-à-pas complet de l’export PDF, en ligne de commande : <a href="/fr/markdown-to-pdf/">Markdown en PDF</a>.</li>
  <li>Ce que MarsDawn ne fait pas encore : <a href="/fr/limits/">la liste</a>.</li>
  <li>Remettre un PDF exporté à quelqu’un qui n’utilise pas Markdown : <a href="/fr/sharing-exported-pdfs/">partager un PDF</a>.</li>
</ul>
""",
    }

    compare_tables['mcp-choice'] = {
        'head': ['Si votre agent', 'Utilisez', 'Prérequis'],
        'rows': [
            ['Peut lancer une commande shell', '<a href="{root}cli/agents/">La CLI</a>', 'macOS 15 ou version ultérieure'],
            ['Charge des fichiers d’instructions, comme Claude Code', '<a href="{root}cli/skill/">Le fichier de compétence</a>', 'La CLI, que la compétence installe'],
            ['Appelle des outils via MCP', '<a href="{mcp}">marsdawn-mcp</a>', 'marsdawn-mcp 0.2.1 ou version ultérieure, marsdawn 0.5.0 ou version ultérieure, et Node.js 20 ou version ultérieure'],
        ],
    }
    compare_tables['preview-tools'] = {
        'head': ['', 'Aperçu VS Code', 'Extension de navigateur', 'Claude Desktop', 'MarsDawn'],
        'rows': [
            ['Ouvre un fichier Markdown depuis le disque', 'Oui', 'Oui, une fois l’accès aux fichiers autorisé', 'Non : Markdown ne figure pas dans sa liste d’import', 'Oui'],
            ['Avant le premier fichier', 'Installer VS Code, un environnement de développement complet', 'Installer une extension, puis activer « Autoriser l’accès aux URL de fichier »', 'Il ne peut pas parcourir les fichiers du disque', 'Installer MarsDawn'],
            ['Conçu pour', 'Écrire du code ; l’aperçu est un volet parmi d’autres', 'Naviguer sur le web', 'Converser avec Claude', 'Lire et modifier du Markdown'],
            ['Dessine la page avec', 'Electron : un Chromium et Node.js embarqués', 'Un navigateur complet', 'L’app Claude Desktop', 'Une app AppKit native ; WebKit dessine la page'],
        ],
    }
    theme_shots = {
        '01-split': ('Dawn (par défaut)', 'Le thème Dawn en vue partagée : la source Markdown à gauche, la page rendue à droite.'),
        '02-classic': ('Classic', 'Le thème Classic, l’aperçu occupant toute la fenêtre.'),
        '04-vivid': ('Vivid', 'Le thème Vivid en vue partagée.'),
        '03-dark': ('Mode sombre', 'MarsDawn en mode sombre, en vue partagée.'),
    }
    theme_gallery_note = 'Modern n’est pas encore illustré ; la quatrième image montre le mode sombre à la place.'

    app_ui_languages = 'anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages, 'example_plan': example_plan,
    }
