# EZO(EasObjects)企劃

## ezsedの使ひ方

クリップボードの文書資料を正字正假名遣に變換します。

### 導入の仕方

以下の電子書類を同じフォルダに置きます。

- ezsed.py
- sed.lst
- scriipt.sed

コマンド・プロンプトでPython3が使用できる必要があります。
installerでPthonを導入すれば、PATHは自動的に切られる筈です。

### 使用方法

1. テキストを選擇して複寫します(Ctrl-c)
2. コマンド・プロンプトでezsed.pyを實行します。
```コマンド・プロンプト
> cd \bin   ← ezsed.pyのあるディレクトリに移動。
> python ezsed.py
```
3. 好きなエディタを起動します。
4. クリップボードのデータを貼付けます(Ctrl-v)

#### 臺本書類一覽(sed.lst)

臺本書類一覽(sed.lst)に、實行したい臺本書類名を書きます。
臺本書類名は複數指定可能です。
臺本は書かれた順に處理されます。

```sed.lst
script.sed
added.sed
```

### 詳細説明

入力書類をストリーム・エディタで變換します。

```usage
> ezsed.exe [-h] [-?] [-e EXPRESSION] [-l LIST]
            [-i INPUT] [-o OUTPUT] [-V]
            [-s] [-v] [-t]
```

optional arguments:
  -h, --help            説明を表示
  -?, --description     傳言箱で説明を表示
  -e EXPRESSION, --expression EXPRESSION
                        臺本(Sed)
  -l LIST, --list LIST  臺本書類一覽（無指定なら、/sed.lst）
  -i INPUT, --input INPUT
                        入力書類（無指定ならクリップボード）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定ならクリップボード）
  -V, --version         履歴情報表示
  -s, --stdout          處理結果を標準出力
  -t, --test            内部試驗
  -v, --verbose         詳細情報表示

#### 臺本書類一覽(sed.lst)

臺本書類一覽(sed.lst)に、實行したい臺本書類名を書きます。
臺本書類名は複數指定可能です。
臺本は書かれた順に處理されます。

```sed.lst
script.sed
added.sed
```

#### 注意

發生した不具合は./msg_ezsed.logに記録されます。

## mkscriptの使ひ方

Excel書類に本づいてSed用の臺本を作成します。

### 導入の仕方

以下の電子書類を同じフォルダに置きます。

- mkscript.py
- table.xlsx

### 使用方法

1. table.xlsxに資料を入力します。
2. コマンド・プロンプトでmkscript.pyを實行します。
```コマンド・プロンプト
> cd \bin   ← mkscript.pyのあるディレクトリに移動。
> python mkscript.py
```
3. added.sedが出力されます。

### 詳細説明

エクセル書類からSed臺本を作成します。

```usage
> mkscript.exe [-h] [-?] [-i INPUT] [-o OUTPUT] [-V]
            [-s] [-v] [-t]
```

optional arguments:
  -h, --help            説明を表示
  -?, --description     説明を表示
  -i INPUT, --input INPUT
                        入力書類（無指定なら./table.xlsx）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定なら./added.sed）
  -V, --version         履歴情報表示
  -s, --stdout          處理結果を標準出力
  -t, --test            内部試驗
  -v, --verbose         詳細情報表示

#### 注意

- 發生した不具合は./msg_mkscript.logに記録されます。
