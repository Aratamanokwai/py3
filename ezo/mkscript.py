#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   ハ行アワ行變換
# Ver.0.2   備考、置換、變換
# Ver.0.3   リファクタリング
# Ver.1.0   公開
"""標本算譜.

Tests:
    >>> __prog__ == 'mkscript.py'
    True
"""

import sys
import argparse
import doctest
import logging as log
import tkinter as tk
from tkinter import messagebox as mbox
try:
    import openpyxl as opx
except ModuleNotFoundError:
    sys.exit('[!!] 外部モジュール(openpyxl)の導入が必要です。')
# End of except ModuleNotFoundError:

__prog__ = 'mkscript.py'
__description__ = 'エクセル書類からSed臺本を作成します。'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.3'
__usage__ = '''
エクセル書類からSed臺本を作成します。

optional arguments:
  -?, --description     説明を表示
  -i INPUT, --input INPUT
                        入力書類（無指定なら./table.xlsx）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定なら./added.sed）
  -V, --version         履歴情報表示

#### 注意

發生した不具合は./msg_mkscript.logに記録されます。
'''

g_log = log.getLogger('file-logger')

TITLE = 'mkscript.exe'
F_NO = 0
F_TYPE = 1
F_OLD = 2
F_NEW0 = 3
F_NEW1 = 4
F_MEMO = 5


def get_excel_data(xlsx, vbs=False):
    """Get the excel data.

    Args:
        xlsx (str):     Excel書類名
        vbs (bool):     詳細情報表示旌旗

    Returns:
        generator:      Excel書類の資料

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    """
    if not isinstance(xlsx, str):
        g_log.error('[!!] get_xlsx_data(): <xlsx> must be a string.')
        raise TypeError('[!!] <xlsx> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    wkb = opx.load_workbook(xlsx)
    wks = wkb.active

    # 二行目から資料を讀込む。
    rows = wks.iter_rows(min_row=2)
    return rows
# End of def get_excel_data(xlsx, vbs=False):


def _add_script(lst, script, memo):
    """Sed命令に備考を追加.

    Args:
        lst (list):     Sed命令一覽
        script (str):   Sed命令
        memo (str):     備考

    Returns:
        list:           Sed命令一覽

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    """
    if not isinstance(lst, list):
        g_log.error('[!!] run(): <lst> must be a list.')
        raise TypeError('[!!] <lst> must be a list.')
    if not isinstance(script, str):
        g_log.error('[!!] run(): <script> must be a string.')
        raise TypeError('[!!] <script> must be a string.')
    if not isinstance(memo, str):
        if memo != None:
            g_log.error('[!!] run(): <memo> must be a string.')
            raise TypeError('[!!] <memo> must be a string.')
        # End of if memo != None:
    # End of if not isinstance(memo, str):

    if memo:
        script += f'\t# {memo}'
    lst.append(script)
# End of def _add_script(lst, script, memo):


def h4toaw5(old, new, memo, vbs=False):
    """ハ行アワ行變換

    ハ行四段動詞をアワ行五段に變換するSed命令の一覽を返します。

    Args:
        old (str):      變換前文字列
        new (str):      變換後文字列
        memo (str)      備考
        vbs (bool):     詳細情報表示旌旗

    Returns:
        list:           Sed命令の一覽

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
    """
    if not isinstance(old, str):
        g_log.error('[!!] run(): <old> must be a string.')
        raise TypeError('[!!] <old> must be a string.')
    if not isinstance(new, str):
        g_log.error('[!!] run(): <new> must be a string.')
        raise TypeError('[!!] <new> must be a string.')
    if not isinstance(memo, str):
        if memo != None:
            print(f'{memo}')
            g_log.error('[!!] run(): <memo> must be a string.')
            raise TypeError('[!!] <memo> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    lst = []

    # ハ行四段動詞をアワ行四段に變換するSed命令の作成
    _add_script(lst, f's/{old}わ/{new}は/g', memo)
    _add_script(lst, f's/{old}い/{new}ひ/g', memo)
    _add_script(lst, f's/{old}う。/{new}ふ。/g', memo)
    _add_script(lst, f's/{old}うと/{new}ふと/g', memo)
    _add_script(lst, f's/{old}うに/{new}ふに/g', memo)
    _add_script(lst, f's/{old}うべ/{new}ふべ/g', memo)
    _add_script(lst, f's/{old}うこと/{new}ふこと/g', memo)
    _add_script(lst, f's/{old}え/{new}へ/g', memo)
    _add_script(lst, f's/{old}お/{new}は/g', memo)

    _add_script(lst, f's/{old}う/{new}【う|ふ】/g', memo)

    _add_script(lst, f's/{old}ふた/{new}うた/g', memo)
    _add_script(lst, f's/{old}ふて/{new}うて/g', memo)

    return lst
# End of def h4toaw5(old, new, memo, vbs=False):


def conv2sed(row, vbs=False):
    """Excel資料の變換.

    Excel資料を基にSed臺本を作成します。

    Args:
        row:            Excelの行資料
        vbs (bool):     詳細情報表示旌旗

    Returns:
        list:           Sed命令の一覽

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    """
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    res = None
    if row[F_NO].value:
        old = row[F_OLD].value
        memo = row[F_MEMO].value
        typ = row[F_TYPE].value
        if typ == '備考':
            # 備考作成
            msg = '# ' + row[F_OLD].value
            res = [msg]
        elif typ == '個別':
            # y命令作成
            new = row[F_NEW0].value
            msg = f'y/{old}/{new}/'
            if memo:
                msg += f'\t# {memo}'
            res = [msg]
        elif typ == '全體':
            # s命令作成
            new0 = row[F_NEW0].value
            new1 = row[F_NEW1].value
            if new1:
                msg = f's/{old}/[{new0}|{new1}]/g'
            else:
                msg = f's/{old}/{new0}/g'
            # End of else:
            if memo:
                msg += f'\t# {memo}'
            res = [msg]
        elif typ == 'ウフ':
            if row[F_NEW0].value:
                new = row[F_NEW0].value
            else:   # if not row[F_NEW0].value:
                new = old
            # End of else:
            res = h4toaw5(old, new, memo, vbs)
        else:
            if vbs:
                msg = f'_analyze_options(): [!] Unknown type: {typ}'
                g_log.warning(msg)
        # End of else:
    # End of if row[F_NO].value:

    return res
# End of def conv2sed(row, vbs=False):


def _analyze_options(args):
    """選擇肢の解析.

    詳細説明

    Args:
        args:           選擇肢情報

    Returns:
        bool:           處理結果

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    """
    # import pdb; pdb.set_trace()   # For debug
    output = args.output
    vbs = args.verbose

    # Excel資料取得
    rows = get_excel_data(args.input, vbs)

    # Excel資料のSed臺本への變換
    com_lst = []
    for row in rows:
        scripts = conv2sed(row, vbs)
        if scripts:
            com_lst += scripts
    # End o for row in rows:

    if args.stdout:
        # 標準出力
        for item in com_lst:
            print(item)
        # End of for item in com_lst:
    else:   # if not args.stdout:
        # 書類出力
        with open(output, mode='w', encoding='utf-8') as fpw:
            for item in com_lst:
                print(item, file=fpw)
            # End of for item in com_lst:
        # End of with open(args.output, mode='w', encoding='utf-8') as fpw:
    # End of else:
# End of def _analyze_options(args):


def main():
    """Do main function.

    Tests:
        >>> import mkscript

    Note:
        何かあれば。

    Todo:
        * 課題の項目
        * 課題の項目
    """
    parser = argparse.ArgumentParser(
        prog=__prog__,
        # usage='usage',
        description=__description__,
        epilog=__epilog__,
        add_help=True,
        )
    parser.add_argument('-?', '--description',
                        help='MsgBoxで説明表示',
                        action='store_true')
    parser.add_argument('-i', '--input',
                        default='table.xlsx',
                        help='入力書類')
    parser.add_argument('-o', '--output',
                        default='added.sed',
                        help='出力書類')
    parser.add_argument('-s', '--stdout',
                        help='變換結果を標準出力',
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help='詳細情報表示',
                        action='store_true')
    parser.add_argument('-t', '--test',
                        help='内部試驗',
                        action='store_true')
    parser.add_argument('-V', '--version',
                        help='履歴情報表示',
                        action='store_true')
    args = parser.parse_args()

    root = tk.Tk()
    root.withdraw()     # 小さなウィンドウを表示させない。

    if args.description:
        mbox.showinfo(TITLE, __usage__)
        sys.exit()

    if args.test:
        doctest.testmod(verbose=args.verbose)
        sys.exit()

    if args.version:
        mbox.showinfo(TITLE, f'Ver: {__version__}')
        sys.exit()

    if args.verbose:
        print(f'Program: {__prog__}')

    # 録の設定
    log.basicConfig(level=log.INFO)
    # log.basicConfig(level=log.DEBUG)
    handler = log.FileHandler(filename='msg_mkscript.log', encoding='utf-8')
    _fmt = '%(asctime)s %(levelname)-5.5s %(message)s'
    fmt = log.Formatter(_fmt)
    handler.setFormatter(fmt)
    g_log.addHandler(handler)

    _analyze_options(args)

    msg = '正常終了'
    if args.verbose:
        g_log.info('[*] ' + msg)
    mbox.showinfo(TITLE, msg)
# End of def main():


if __name__ == '__main__':
    main()
