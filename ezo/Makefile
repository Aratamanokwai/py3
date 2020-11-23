# Mskeiile
#
# 履歴情報：
# Ver.0.1	ezsed.pyのコンパイル

all: dist/ezsed.exe

clean:
	rm -f errmsg.log ezsed.spec ooo

dist/ezsed.exe: ezsed.py
	pyinstaller ezsed.py --onefile --noconsol
