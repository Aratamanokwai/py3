# EZO(EasyObjects)企劃

## ezsedの使ひ方



入力書類（クリップボード）を正字正假名遣に變換します。



### 導入の仕方

以下の電子書類を同じフォルダに置きます。

- ezsed.exe
- scriipt.sed

ezsed.exeのショート・カットを作成します。

### 使用方法

1. テキストを選擇して複寫します(Ctrl-c)
2. ショート・カットをダブルクリックします。
3. 好きなエディタを起動します。
4. クリップボードのデータを貼付けます(Ctrl-v)

### 詳細説明

入力書類をストリーム・エディタで變換します。

```usage
> ezsed.exe [-?] [-e EXPRESSION] [-f FILE] [-s] [INPUT]
```

positional arguments:
  INPUT                 入力書類（無指定ならクリップボード）

optional arguments:
  -?, --description     説明を表示
  -e EXPRESSION, --expression EXPRESSION
                        臺本
  -f FILE, --file FILE  臺本書類（無指定なら./script.sed）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定ならクリップボード）
  -V, --version         履歴情報表示



#### 注意

發生した不具合は./msg_ezsed.logに記録されます。
