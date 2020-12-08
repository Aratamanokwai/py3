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

#### Sed命令と正規表現と

臺本では、Sed命令を指定できます。

##### y命令による単漢字の置換

y命令は一括して文字を置換へる事が出來ます。
これを利用して新字を舊字に置換へます。

```sed
y/閙閧闘/鬧鬨鬪/
```
##### s命令による熟語の變換

熟語の變換にはs命令を用ゐます。

```sed
s/英才/穎才/g
```
##### 正規表現による置換

sedで使用可能な正規表現は、プログラムによつて異ります。
ezsedで使用可能な正規表現には、以下のやうなものがあります。

- OR檢索

パイプ('|')でOR檢索をしてのパターン・マッチが可能です。
```sed
s/[障害|障碍]/障礙/g    # 障害も障碍も障礙に變換
```
- \番號對應

'\1'が'()'にマッチした部分に對應してゐます。
'()'が複數ある場合は、'\2', '\3'のやうにして使ひます。
```sed
s/m([0-9]{2})年/明治\1年/g # m29年 -> 明治29年
```

#### 臺本書類一覽(sed.lst)

臺本書類一覽(sed.lst)に、實行したい臺本書類名を書きます。
臺本書類名は複數指定可能です。
臺本は書かれた順に處理されます。

```sed.lst
script.sed
added.sed
```

#### 注意

- ezsedはsedの一部機能しかサポートしてゐません。
- 發生した不具合は./msg_ezsed.logに記録されます。

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

エクセル書類からSed臺本を作成します。

```usage
> mkscript.exe [-?] [-i INPUT] [-o OUTPUT] [-V]
```

optional arguments:
  -?, --description     説明を表示
  -i INPUT, --input INPUT
                        入力書類（無指定なら./table.xlsx）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定なら./added.sed）
  -V, --version         履歴情報表示

#### 注意

- 發生した不具合は./msg_mkscript.logに記録されます。
