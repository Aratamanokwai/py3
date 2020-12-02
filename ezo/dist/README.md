# EZO(EasyObjects)企劃

## ezsedの使ひ方

入力書類（クリップボード）を正字正假名遣に變換します。

### 導入の仕方

以下の電子書類を同じフォルダに置きます。

- ezsed.exe
- sed.lst
- scriipt.sed

ezsed.exeのショート・カットを作成します。

### 使用方法

1. テキストを選擇して複寫します(Ctrl-c)
2. ショート・カットをダブルクリックします。
3. 終了の傳言箱が表示されたら、OKボタンを押します。
4. 好きなエディタを起動します。
5. クリップボードのデータを貼付けます(Ctrl-v)

### 詳細説明

入力書類をストリーム・エディタで變換します。

```usage
> ezsed.exe [-?] [-e EXPRESSION] [-l LIST]
            [-i INPUT] [-o OUTPUT] [-V]
```

optional arguments:
  -?, --description     説明を表示
  -e EXPRESSION, --expression EXPRESSION
                        臺本
  -l LIST, --list LIST  臺本書類一覽（無指定なら、/sed.lst）
  -i INPUT, --input INPUT
                        入力書類（無指定ならクリップボード）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定ならクリップボード）
  -V, --version         履歴情報表示

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

- mkscript.exe
- table.xlsx

mkscript.exeのショート・カットを作成します。

### 使用方法

1. table.xlsxに資料を入力します。
2. ショート・カットをダブルクリックします。
3. 終了の傳言箱が表示されたら、OKボタンを押します。
4. added.sedが出力されます。

### 詳細説明

入力書類をストリーム・エディタで變換します。

```usage
> ezsed.exe [-?] [-i INPUT] [-o OUTPUT] [-V]
```

optional arguments:
  -?, --description     説明を表示
  -i INPUT, --input INPUT
                        入力書類（無指定なら./table.xlsx）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定なら./added.sed）
  -V, --version         履歴情報表示

#### 注意

發生した不具合は./msg_mkscript.logに記録されます。
