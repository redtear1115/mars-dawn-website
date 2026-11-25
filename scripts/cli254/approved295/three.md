## 結論

三項都寫好了，en、zh-Hant、ja 各一份：
1. `error_v4` 的 schema 說明。`error_v3` 那則也一起改，註明已由 v4 取代。
2. 「Failures」新增 `5`／`input_too_large` 和 `7`／`skill_install_failed` 兩條。
3. 改寫 `64` 那條：大多數用法錯誤仍以文字輸出到 stderr，但有 8 種會輸出 JSON。

**依據**：kit `origin/main` b699569（= 0.7.2）。`main.swift` 的 `finish()` 第 22–42 行對 `WaitRangeFailure`、`SkillInstallFailure`、`OutputPathFailure` 印出 JSON，並以 64 結束。`Commands.swift:93` 把 `input_too_large` 對應到代碼 5，只在 `export` 的 790 行丟出。website `origin/main` 11d1a86，`public/schemas/cli/error.v4.json`。我核對的事實和單上的表格一致。

### 1. Schema 說明（`SCHEMA_NOTES`）

`error_v3` 的說明在 #254 還沒套用。這裡給的版本會取代我在 #254 寫的那則，因為 v3 和 v4 涵蓋同樣的版本，要寫出兩者的差別。

| key | en | zh-Hant | ja |
|---|---|---|---|
| `error_v4`（新） | failure, every command, marsdawn 0.7.1 and later, including the usage errors that print JSON at exit 64 | 所有指令的失敗結果，marsdawn 0.7.1 以後，包括以代碼 64 輸出 JSON 的用法錯誤 | 失敗時、すべてのコマンド共通、marsdawn 0.7.1 以降、コード 64 で JSON を返す使用方法のエラーを含む |
| `error_v3`（改） | failure, every command, marsdawn 0.7.1 and later, without the exit-64 kinds; error.v4.json replaces it | 所有指令的失敗結果，marsdawn 0.7.1 以後，不含代碼 64 的種類；已由 error.v4.json 取代 | 失敗時、すべてのコマンド共通、marsdawn 0.7.1 以降、コード 64 の種類を含まない（error.v4.json に置き換え） |

- [ ] en
- [ ] zh-Hant
- [ ] ja

建議順序：`error_v4` 放在 `error_v3` 之前。

### 2、3. `/cli/agents/`「Failures」

`5` 那條接在 `export_failed` 之後，`7` 那條接在 `6` 之後，`64` 那條取代原本的。其餘不變。

**en**
- [ ] 
```md
- `5`, `input_too_large`: the input is over 16 MiB, so nothing was written. Only `export` returns this.
```
- [ ] 
```md
- `7`, `skill_install_failed`: `skill --install` couldn't create the folder or write the file. An existing SKILL.md is left as it was.
```
- [ ] 
```md
- `64`: usage error. Most usage errors, such as an unknown option, an invalid value, a line out of range, `--line` with more than one file or with a folder, more than one folder, or `-a`, are printed as text on stderr, even with `--json`. These have their own `error` and print JSON on stdout, like any other failure:
  - `wait_out_of_range`: `open --wait` outside 0 to 30.
  - `skill_differs`, `skill_unsafe_symlink`, `skill_target_not_a_file`, `skill_unreadable`: `skill --install` refused to write.
  - `output_folder_missing`, `output_symlink`, `output_not_a_file`: `theme preview` refused the `-o` path.
```

**zh-Hant**
- [ ] 
```md
- `5`，`input_too_large`：輸入檔超過 16 MiB，所以沒有寫出任何檔案。只有 `export` 會回傳這個代碼。
```
- [ ] 
```md
- `7`，`skill_install_failed`：`skill --install` 無法建立資料夾或寫入檔案。原本的 SKILL.md 保持不變。
```
- [ ] 
```md
- `64`：用法錯誤。大多數用法錯誤，例如未知的選項、無效的值、行號超出範圍、`--line` 搭配了多個檔案或資料夾、指定了多個資料夾，或使用了 `-a`，都以文字輸出到 stderr，即使加了 `--json` 也一樣。下面這幾種有自己的 `error` 值，會和其他失敗一樣在 stdout 輸出 JSON：
  - `wait_out_of_range`：`open --wait` 超出 0 到 30。
  - `skill_differs`、`skill_unsafe_symlink`、`skill_target_not_a_file`、`skill_unreadable`：`skill --install` 拒絕寫入。
  - `output_folder_missing`、`output_symlink`、`output_not_a_file`：`theme preview` 拒絕 `-o` 指定的路徑。
```

**ja**
- [ ] 
```md
- `5`、`input_too_large`：入力が 16 MiB を超えているため、何も書き出さなかった。`export` のみがこれを返します。
```
- [ ] 
```md
- `7`、`skill_install_failed`：`skill --install` がフォルダを作成できなかった、またはファイルを書き込めなかった。既存の SKILL.md はそのままです。
```
- [ ] 
```md
- `64`：使用方法のエラー。未知のオプション、無効な値、範囲外の行、複数ファイルやフォルダに対する `--line` の指定、複数のフォルダの指定、`-a` の指定など、ほとんどの場合は `--json` を指定していても stderr にテキストとして出力されます。次のものは独自の `error` を持ち、ほかの失敗と同じく stdout に JSON を出力します。
  - `wait_out_of_range`：`open --wait` の値が 0〜30 の範囲外。
  - `skill_differs`、`skill_unsafe_symlink`、`skill_target_not_a_file`、`skill_unreadable`：`skill --install` が書き込みを拒否した。
  - `output_folder_missing`、`output_symlink`、`output_not_a_file`：`theme preview` が `-o` のパスを拒否した。
```

## 風險／待確認

- **`64` 那條改成有子清單的條列。** 如果 build 的格式只吃單層，可以把三個子項併成一句：「…print JSON on stdout: `wait_out_of_range` (`open --wait` outside 0 to 30), the four `skill_*` refusals of `skill --install`, and theme preview's `output_*` refusals of `-o`.」需要的話我再補三語。
- **`/cli/` 的退出碼表**（zh-Hant 第 115 行等）的 `64` 也寫「即使加了 `--json` 也是文字」，同樣不完全正確。這不在本單的範圍內，要改的話我再寫。
- **kit 的 `skill/SKILL.md`** 第 64 列只列出 theme preview 的種類：這是 kit repo 的文字，網站要逐字照抄，所以要在 kit 修，不是在網站修。
- 其他五個語系等核准後再走 needs-i18n。

Co-authored-by: Grok <grok@southern-light.dev>

