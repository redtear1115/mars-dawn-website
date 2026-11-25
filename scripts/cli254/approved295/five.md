## 結論

#295 的五語（zh-Hans、ko、de、fr、es）如下：schema 說明兩則，加上「Failures」的 `5`、`7`、`64` 三條。來源是已核准的 en（issuecomment-6305066768），用語沿用各語系 `/cli/agents/` 現有的「Failures」和 schema 清單。

**依據**：website `origin/main` 4f91f92，各語系 `public/<locale>/cli/agents/index.md:158–163、172`。

### 1. Schema 說明（`SCHEMA_NOTES`）

這裡的 `error_v3` 會取代我在 #254（issuecomment-6295975448）給這五語的版本。

| key | zh-Hans | ko | de | fr | es |
|---|---|---|---|---|---|
| `error_v4`（新） | 所有命令的失败结果，marsdawn 0.7.1 以后，包括以代码 64 输出 JSON 的用法错误 | 실패, 모든 명령 공통, marsdawn 0.7.1 이상, 코드 64로 JSON을 출력하는 사용법 오류 포함 | Fehler, alle Befehle, marsdawn 0.7.1 und neuer, einschließlich der Bedienungsfehler, die mit Code 64 JSON ausgeben | échec, pour toutes les commandes, marsdawn 0.7.1 et versions ultérieures, y compris les erreurs d’utilisation qui affichent du JSON avec le code 64 | error, todos los comandos, marsdawn 0.7.1 y posterior, incluidos los errores de uso que imprimen JSON con el código 64 |
| `error_v3`（改） | 所有命令的失败结果，marsdawn 0.7.1 以后，不含代码 64 的种类；已由 error.v4.json 取代 | 실패, 모든 명령 공통, marsdawn 0.7.1 이상, 코드 64 종류 제외, error.v4.json으로 대체됨 | Fehler, alle Befehle, marsdawn 0.7.1 und neuer, ohne die Arten mit Code 64; ersetzt durch error.v4.json | échec, pour toutes les commandes, marsdawn 0.7.1 et versions ultérieures, sans les types du code 64 ; remplacé par error.v4.json | error, todos los comandos, marsdawn 0.7.1 y posterior, sin los tipos del código 64; lo reemplaza error.v4.json |

### 2、3. `/cli/agents/`「Failures」

位置同 en：`5` 接在 `export_failed` 之後，`7` 接在 `6` 之後，`64` 取代原本那條。

**zh-Hans**
```md
- `5`，`input_too_large`：输入文件超过 16 MiB，所以没有写出任何文件。只有 `export` 会返回这个代码。
- `7`，`skill_install_failed`：`skill --install` 无法创建文件夹或写入文件。原有的 SKILL.md 保持不变。
- `64`：用法错误。大多数用法错误，例如未知的选项、无效的值、行号超出范围、`--line` 搭配了多个文件或文件夹、指定了多个文件夹，或使用了 `-a`，都以文本输出到 stderr，即使加了 `--json` 也一样。下面这几种有自己的 `error` 值，会和其他失败一样在 stdout 输出 JSON：
  - `wait_out_of_range`：`open --wait` 超出 0 到 30。
  - `skill_differs`、`skill_unsafe_symlink`、`skill_target_not_a_file`、`skill_unreadable`：`skill --install` 拒绝写入。
  - `output_folder_missing`、`output_symlink`、`output_not_a_file`：`theme preview` 拒绝 `-o` 指定的路径。
```

**ko**
```md
- `5`, `input_too_large`: 입력이 16 MiB를 넘어서 아무것도 저장하지 않았습니다. `export`만 이 코드를 반환합니다.
- `7`, `skill_install_failed`: `skill --install`이 폴더를 만들거나 파일을 쓰지 못했습니다. 기존 SKILL.md는 그대로 둡니다.
- `64`: 사용법 오류. 알 수 없는 옵션, 잘못된 값, 범위를 벗어난 줄, 파일 두 개 이상이나 폴더와 함께 쓴 `--line`, 폴더 두 개 이상, `-a` 등 대부분의 사용법 오류는 `--json`을 줘도 stderr에 텍스트로 출력됩니다. 다음 오류는 각자의 `error`가 있으며, 다른 실패와 마찬가지로 stdout에 JSON을 출력합니다.
  - `wait_out_of_range`: `open --wait`가 0~30을 벗어남.
  - `skill_differs`, `skill_unsafe_symlink`, `skill_target_not_a_file`, `skill_unreadable`: `skill --install`이 쓰기를 거부함.
  - `output_folder_missing`, `output_symlink`, `output_not_a_file`: `theme preview`가 `-o` 경로를 거부함.
```

**de**
```md
- `5`, `input_too_large`: Die Eingabe ist größer als 16 MiB, also wurde nichts geschrieben. Nur `export` liefert das.
- `7`, `skill_install_failed`: `skill --install` konnte den Ordner nicht anlegen oder die Datei nicht schreiben. Eine vorhandene SKILL.md bleibt unverändert.
- `64`: Bedienungsfehler. Die meisten, etwa eine unbekannte Option, ein ungültiger Wert, eine Zeile außerhalb des Bereichs, `--line` mit mehr als einer Datei oder mit einem Ordner, mehr als ein Ordner oder `-a`, werden als Text auf stderr ausgegeben, auch mit `--json`. Diese haben ein eigenes `error` und geben wie jeder andere Fehler JSON auf stdout aus:
  - `wait_out_of_range`: `open --wait` außerhalb von 0 bis 30.
  - `skill_differs`, `skill_unsafe_symlink`, `skill_target_not_a_file`, `skill_unreadable`: `skill --install` hat das Schreiben verweigert.
  - `output_folder_missing`, `output_symlink`, `output_not_a_file`: `theme preview` hat den Pfad von `-o` abgelehnt.
```

**fr**
```md
- `5`, `input_too_large` : l’entrée dépasse 16 Mio, donc rien n’a été écrit. Seul `export` renvoie ce code.
- `7`, `skill_install_failed` : `skill --install` n’a pas pu créer le dossier ou écrire le fichier. Un SKILL.md existant reste tel quel.
- `64` : erreur d’utilisation. La plupart, comme une option inconnue, une valeur non valide, une ligne hors limites, `--line` avec plus d’un fichier ou avec un dossier, plus d’un dossier, ou `-a`, s’affichent en texte sur stderr, même avec `--json`. Celles-ci ont leur propre `error` et affichent du JSON sur stdout, comme tout autre échec :
  - `wait_out_of_range` : `open --wait` hors de 0 à 30.
  - `skill_differs`, `skill_unsafe_symlink`, `skill_target_not_a_file`, `skill_unreadable` : `skill --install` a refusé d’écrire.
  - `output_folder_missing`, `output_symlink`, `output_not_a_file` : `theme preview` a refusé le chemin de `-o`.
```

**es**
```md
- `5`, `input_too_large`: la entrada supera los 16 MiB, así que no se escribió nada. Solo `export` devuelve este código.
- `7`, `skill_install_failed`: `skill --install` no pudo crear la carpeta ni escribir el archivo. Un SKILL.md existente se deja como estaba.
- `64`: error de uso. La mayoría, como una opción desconocida, un valor no válido, una línea fuera de rango, `--line` con más de un archivo o con una carpeta, más de una carpeta o `-a`, se imprimen como texto en stderr, incluso con `--json`. Estos tienen su propio `error` e imprimen JSON en stdout, como cualquier otro error:
  - `wait_out_of_range`: `open --wait` fuera de 0 a 30.
  - `skill_differs`, `skill_unsafe_symlink`, `skill_target_not_a_file`, `skill_unreadable`: `skill --install` se negó a escribir.
  - `output_folder_missing`, `output_symlink`, `output_not_a_file`: `theme preview` rechazó la ruta de `-o`.
```

## 待確認

- fr 寫「16 Mio」，跟 fr 站上現有的寫法一致；其他語系用「16 MiB」。
- 如果 build 不支援子清單、改用單句版，我再補五語單句（依核准留言的安排）。

Co-authored-by: Grok <grok@southern-light.dev>

