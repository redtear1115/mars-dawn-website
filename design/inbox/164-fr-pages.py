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
        "description": 'MarsDawn se télécharge gratuitement. Essayez tout pendant 14 jours, puis déverrouillez-le une fois pour 4,99 USD. Sans abonnement, sans compte.',
        "intro": """
<section class="intro">
  <h1>Essayez tout. Puis payez une fois.</h1>
  <p>MarsDawn se télécharge gratuitement. Lancez l’essai de 14 jours et toutes les fonctionnalités sont disponibles ; pour continuer ensuite, un achat unique de 4,99 USD le déverrouille. Il n’y a ni abonnement ni compte.</p>
</section>
""",
        "body": """
<h2>Comment ça marche</h2>
<ol class="loop-steps">
  <li><strong>Téléchargez-le gratuitement.</strong> MarsDawn se télécharge gratuitement sur le Mac App Store.</li>
  <li><strong>Essayez tout pendant 14 jours.</strong> Lancez l’essai et tout MarsDawn fonctionne pendant 14 jours : tous les thèmes et toutes les dispositions, l’export PDF et l’impression, ainsi que les actions Siri et Raccourcis. Coup d’œil dans le Finder fonctionne avec ou sans essai.</li>
  <li><strong>Déverrouillez-le une fois.</strong> Pour continuer ensuite, déverrouillez-le une fois pour 4,99 USD. C’est un achat intégré, pas un abonnement : rien ne se renouvelle et rien ne vous sera facturé plus tard.</li>
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
    app_ui_languages = 'anglais, chinois traditionnel, chinois simplifié, japonais, allemand, français, espagnol et coréen'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages,
    }
