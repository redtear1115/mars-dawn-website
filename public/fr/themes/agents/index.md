# Créer un thème avec votre agent

Une référence pour un agent IA qui crée un thème d’aperçu MarsDawn. L’agent écrit un seul `theme.json`, le vérifie et le rend avec l’outil en ligne de commande `marsdawn`, puis vous remet un lien. Vous l’ajustez à l’œil sur la page [Créer un thème](/fr/themes/new/) et vous le soumettez. Les tableaux de champs ci-dessous sont lus dans le code source du kit, et une vérification les maintient identiques.

**Écrivez un `theme.json`, lancez `marsdawn theme validate theme.json --require-complete --json` jusqu’à obtenir le code de sortie 0, rendez-le avec `marsdawn theme preview` en clair et en sombre, puis donnez un lien à la personne.** Un thème n’est fait que de paramètres. Il ne contient jamais de CSS.

## Ce qu’est un thème

- **Des couleurs** pour le clair et pour le sombre : une palette de base, et des couleurs de syntaxe et de diagramme facultatives. Chacune est de la forme `#RRGGBB`.
- **Un style de police** : `sans`, `serif` ou `rounded`.
- **Un ensemble fermé d’options de style** : des nombres dans des plages fixes et des choix dans des listes fixes. Une couleur dans une option de style est toujours un rôle de palette comme `accent`, jamais une couleur littérale.
- **Des textes affichés** : un nom et un résumé, et éventuellement un auteur et une licence.

Une clé absente des tableaux ci-dessous est une erreur, tout comme une clé écrite deux fois. Le fichier fait au plus 16 384 octets.

## Vérifier et rendre

Lancez ces commandes dans le dossier qui contient `theme.json`. Elles demandent l’outil `marsdawn` : voir [marsdawn pour les agents](/fr/cli/agents/).

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- Codes de sortie : 0 valide, 1 invalide avec des identifiants de règle, 2 fichier introuvable, 64 erreur d’usage. `preview` ajoute 4 quand le PNG existe déjà (passez `--force` ou choisissez un autre nom) et 5 quand le rendu échoue.
- Avec `--json`, un thème invalide énumère ses problèmes sous `issues`, chacun avec un identifiant `rule`, un `path` et un `message`. Corrigez-les et relancez la commande.
- `--require-complete` est la vérification d’un thème destiné à être publié : elle exige aussi les couleurs `syntax` et `diagram` dans les deux palettes.
- `css` affiche le CSS que sert l’aperçu. `preview` rend un document d’exemple en PNG. Les deux valident d’abord : un thème invalide ne produit aucun rendu.
- Regardez le PNG clair et le PNG sombre avant de remettre le thème.

## Partir d’un thème intégré

Copiez l’un des quatre thèmes intégrés et modifiez-le. Chacun est un fichier complet et valide :

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): le thème par défaut, et l’exemple ci-dessous
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): une palette plus sobre, proche d’un document
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): une palette plus froide et plus contemporaine
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): une palette plus vive et plus contrastée

### Exemple : Dawn

Voici `dawn.json`, octet pour octet. Sa seule option de style est un fin filet de couleur d’accent pour `hr`.

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## Champs

Chaque objet ci-dessous est lu de la même façon. `required` signifie que la clé doit être présente, et une clé qui n’est pas listée est une erreur.

Types : `string`, `integer`, `number`, `boolean`, `map` (balise de langue vers texte), `enum` (l’une des valeurs listées), `role` (un rôle de palette) et `object` (le tableau vers lequel il renvoie). Un `[]` après un type signifie une liste.

### `theme.json`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | Toujours `1`. |
| `id` | `string` | `required` | De 1 à 32 caractères : lettres minuscules et chiffres, en blocs reliés par des tirets simples, par exemple `calm-green`. |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`, par exemple `1.0.0`. |
| `name` | `map` | `required` | Balise de langue vers texte. `en` est obligatoire ; les autres clés sont des balises de langue comme `zh-Hant`. Chaque texte compte au plus 48 caractères, sans lien ni saut de ligne. |
| `summary` | `map` | `required` | Même forme que `name`, au plus 120 caractères par texte. |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — Un ou deux, sans répétition. Ils fixent le contraste que le thème doit atteindre. |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | Un identifiant SPDX, par exemple `Apache-2.0`. Les thèmes soumis sont publiés sous Apache-2.0. |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `name` | `string` | `required` | Au plus 64 caractères, sans lien. |
| `github` | `string` | `optional` | Un identifiant GitHub. Pour une soumission, indiquez celui de la personne qui soumet. |

### `light, dark`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `background` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `surface` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `text` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `muted` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `border` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `heading` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `accent` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `link` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `quote` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `syntax` | `object` | `optional` (requis pour publier, avec `--require-complete`) | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` (requis pour publier, avec `--require-complete`) | [`diagram`](#t-diagram-colors) |

### `syntax`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `string` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `comment` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `number` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `function` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `type` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |

### `diagram`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `node` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `nodeBorder` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `text` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `line` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `secondary` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `tertiary` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |
| `note` | `string` | `required` | `#` suivi de six chiffres hexadécimaux, par exemple `#1C1C1C`. |

### `style`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [plage](#t-numbers) |
| `lineHeight` | `number` | `optional` | [plage](#t-numbers) |
| `headingWeight` | `number` | `optional` | [plage](#t-numbers) |
| `radius` | `number` | `optional` | [plage](#t-numbers) |
| `maxWidth` | `number` | `optional` | [plage](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [un rôle de palette](#roles) |
| `inlineCode` | `role` | `optional` | [un rôle de palette](#roles) — Seulement `text` ou un rôle de syntaxe : `keyword`, `string`, `comment`, `number`, `function` ou `type`. |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `size` | `number` | `optional` | [plage](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [plage](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [plage](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| Champ | Type | Présence | Valeurs et remarques |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### Options à type

Ces options de style sont des objets avec un `type`. Chaque `type` accepte les champs listés pour lui, et aucun autre.

| Option | type | Champ | Présence | Type |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [plage](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [plage](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` Deux ou trois rôles. |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### Rôles de palette

Un rôle de palette est l’un de ces noms :

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### Nombres

Un nombre est arrondi au multiple le plus proche de son pas, puis doit se trouver entre le min et le max. Sinon la règle est `number.range`.

| Champ | Min | Max | Pas |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## Ce qui est vérifié d’autre

- **Contraste.** Chaque paire de couleurs que dessine l’aperçu, comme `text` sur `background`, doit atteindre 4,5:1 pour le texte et 3:1 pour les traits et le reste du non-texte. Les scénarios que vous indiquez portent certaines couleurs à 4,5:1. Le message nomme la paire, son rapport et celui qu’il faut.
- **Textes.** Un nom, un résumé ou un nom d’auteur vide, trop long, ou contenant un lien, un caractère de contrôle ou un caractère de format invisible ou bidirectionnel est refusé.
- **Identifiants de règle.** Chaque problème en porte un, par exemple `contrast.pair`, `color.hex`, `number.range`, `id.pattern`, `schema.unknownKey` ou `palette.incomplete`. Corrigez le fichier d’après ce que disent l’identifiant et le `path`.

## Le remettre sous forme de lien

La page [Créer un thème](/fr/themes/new/) ouvre un thème à partir d’un lien, pour que la personne puisse l’ajuster à l’œil. Le lien est l’adresse de la page, puis `#theme=`, puis les octets du fichier en base64url sans remplissage. Le fichier fait au plus 16 384 octets. Cette seule ligne construit le lien sous zsh et sous bash, sur macOS et sur Linux :

```
printf 'https://marsdawn.southern-light.dev/fr/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

Le thème voyage après un `#`, que le navigateur n’envoie pas au site, et le site ne le transmet nulle part. Le lien reste toutefois dans l’historique de votre shell et du navigateur, et toute personne à qui vous le collez peut lire le thème.

## Le soumettre

L’agent prépare le fichier et le lien. La personne soumet. Les deux voies demandent le Developer Certificate of Origin et la publication sous Apache-2.0, et c’est la personne qui fait cette attestation : l’agent ne coche pas la case et ne signe pas à sa place.

- **Issue.** La personne ouvre le lien et appuie sur **Submit** dans la page « Créer un thème », ou ouvre le [formulaire d’issue](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml) et colle le JSON dans *Theme*. Un workflow vérifie le thème et répond.
- **Pull request.** Ne modifiez que `themes/<id>/theme.json`, mettez dans `author.github` l’identifiant de l’auteur de la pull request et signez chaque commit avec `git commit -s`. Les règles sont dans [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md).

Le nom d’auteur, le nom, le résumé et l’identifiant GitHub d’un thème soumis deviennent publics de façon permanente : mettez dans `author.name` un nom que la personne accepte de publier.

## Thèmes publiés

Pour voir à quoi ressemblent les thèmes publiés, parcourez la [galerie de thèmes](/fr/themes/gallery/).

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
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI agent 的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
