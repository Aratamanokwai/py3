#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   s命令實裝
# Ver.0.2   y命令實裝
# Ver.0.3   --expression 選擇肢
# Ver.0.4   --fiile 選擇肢
# Ver.0.5   --display 選擇肢
# Ver.0.6   入力書類對應
# Ver.0.7   負具合記録對應
# Ver.0.8   MsgBoxで命令の説明表示
# Ver.0.9   --output 選擇肢
# Ver.1.0   公開
# Ver.1.1   録（ログ）の追加
# Ver.1.2   --input選擇肢
# Ver.1.3   内部函數名變更（_proc() -> _analyze_options()）
# Ver.1.4   臺本書類の一覽化（--list 選擇肢）
# Ver.1.5   正規表現對應
# Ver.1.6   一覽のコメント機能追加
# Ver.2.0   GUI化
# Ver.2.1   機能の部品化
# Ver.2.2   逆變換機能
# Ver.2.3   Sed處理の外部化
# Ver.2.4   「逆變換」ボタン追加
# Ver.2.5   蜷榊燕隶頑峩(coresed -> poorsed)
"""ストリーム・エディタ.

複寫板の資料をストリーム・エディタで變換します。

Samples:
    >>> sed = Sed('no melon, no lemon.')
    >>> sed.s_command('melon', 'lemon')
    >>> sed.get_data()
    'no lemon, no lemon.'
"""

import sys
import os
import re
import argparse
import doctest
import logging as log
import tkinter as tk
from tkinter import messagebox as mbox
try:
    import pyperclip as ppc
except ModuleNotFoundError:
    sys.exit('[!!] pyperclipモジュールの導入が必要です。')
# End of except ModuleNotFoundError:
try:
    import PySimpleGUI as psg
except ModuleNotFoundError:
    sys.exit('[!!] PySimpleGUIモジュールの導入が必要です。')
# End of except ModuleNotFoundError:
import ezo.poorsed as psed


# import pprint as pp         # For debug
# import ezo.deco as deco     # For debug

__prog__ = 'ezsed.py'
__description__ = '入力書類をストリーム・エディタで變換します。'
__epilog__ = '發生した不具合は./msg_ezsed.logに記録されます。'
__version__ = '2.4'
__usage__ = '''入力書類をストリーム・エディタで變換します。

「變換」ボタンを押すと複寫板の内容を變換します。

usage: ezsed.exe [-?] [-l LIST] [-V]

optional arguments:
  -?, --description     説明を表示
  -l LIST, --list LIST  臺本書類一覽（無指定なら、./sed.lst）
  -V, --version         履歴情報表示

#### 注意

- 發生した不具合は./msg_ezsed.logに記録されます。
'''

g_log = log.getLogger('file-logger')
TITLE = 'ezsed.exe'


# @deco.stopwatch
def run(scripts, data, rev=False, vbs=False):
    """Edit stream.

    ストリーム・エディタ處理の實行。.

    Args:
        scripts (list): 臺本の一覽
        data (str):     文字列
        rev (bool):     臺本を逆に實行
        vbs (bool):     詳細情報表示旌旗

    Returns:
        str:            變換された文字列

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合

    Samples:
        >>> data = 'no melon, no lemon.'
        >>> scripts = ['s/no/yes/g']
        >>> ppc.copy(data)
        >>> run(scripts, data)
        'yes melon, yes lemon.'
        >>> scripts = ['y/n/N/']
        >>> ppc.copy(data)
        >>> run(scripts, data)
        'No meloN, No lemoN.'
    """
    if not isinstance(data, str):
        g_log.error('[!!] run(): <data> must be a string.')
        raise TypeError('[!!] <data> must be a string.')
    if not isinstance(scripts, list):
        g_log.error('[!!] run(): <scripts> must be a list.')
        raise TypeError('[!!] <scripts> must be a list.')
    assert isinstance(rev, bool), '[!!] <rev> must be boolean.'
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    sed = psed.Sed(data, vbs, g_log)
    if rev:
        scripts.reverse()
    for script in scripts:
        script = script.rstrip()    # 改行符號を取除く。
        new_script = sed.del_comment(script)
        if new_script != '':
            lst = psed.analyze_script(new_script, vbs, g_log)
            if rev:
                fst = lst[2]
                scd = lst[1]
            else:
                fst = lst[1]
                scd = lst[2]
            # End of else:

            if len(lst) <= 0:
                continue
            if lst[0] == 's':
                # s命令の實行
                if lst[3] == 'g':
                    sed.s_command(fst, scd, cnt=0)
                else:   # if lst[3] != 'g':
                    sed.s_command(fst, scd, cnt=1)
                # End of else:
            elif lst[0] == 'y':
                # y命令の實行
                sed.y_command(sed.mk_dict(fst, scd))
            else:   # if lst[0] != 'y':
                msg = f'[!] Unsupported command: {lst}'
                g_log.warning(msg)
            # End of else:
        # End of if new_script != '':
    # End of for script in scripts:

    return sed.get_data()
# End of def run(scripts, data, rev=False, vbs=False):


def _analyze_options(args, win):
    """選擇肢への對應.

    Args:
        args (argparse.Namespace):      處理の選擇肢情報

    Raises:
        AssertionError: 不具合
    """
    assert isinstance(args, argparse.Namespace), '[!!] args error.'

    # 臺本の讀込
    if args.list:
        scripts = psed.get_scripts(args.list, args.verbose, g_log)
    else:
        msg = '[!!] 臺本書類一覽を指定して下さい。'
        mbox.showerror(TITLE, msg)
        g_log.error(msg)
        sys.exit(msg)
    # End of else:

    # 出來事の繰返し
    loop = True
    while True:
        event, _ = win.read()
        if event == psg.WIN_CLOSED:
            break
        elif event == '終了':
            break
        elif event == '變換':
            flg = False
        elif event == '逆變換':
            flg = True
        # End of elif event == '逆變換':

        # 複寫板の資料讀込み
        data = ppc.paste()

        # 結果出力の指定
        result = run(scripts, data, flg, args.verbose)
        if args.stdout:
            # 結果を標準出力する。
            print(result)
            print('\n\n\n\n\n')
        # End of if args.stdout:
        # 結果を複寫板に出力する。
        ppc.copy(result)
        mbox.showinfo(TITLE, '變換完了')
    # End of while True:

    win.close()
# End of def _analyze_options(args):


# @deco.stopwatch
def main():
    """Do main function.

    選擇肢に本づいて文字列を變換します。

    Tests:
        >>> import ezsed

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
    parser.add_argument('-l', '--list',
                        default='./sed.lst',
                        help='臺本書類一覽（無指定なら、./sed.lst）')
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

    # 録の設定
    log.basicConfig(level=log.INFO)
    # log.basicConfig(level=log.DEBUG)
    handler = log.FileHandler(filename='msg_ezsed.log', encoding='utf-8')
    _fmt = '%(asctime)s %(levelname)-5.5s %(message)s'
    fmt = log.Formatter(_fmt)
    handler.setFormatter(fmt)
    g_log.addHandler(handler)

    root = tk.Tk()
    root.withdraw()     # 小さなウィンドウを表示させない。

    psg.theme('DarkAmber')   # 設計主題の設定

    # 窗に配置する部品
    layout = [[psg.Text('複寫板（クリップボード）に複寫して變換')],
              [psg.Button('變換'),
               psg.Button('逆變換'),
               psg.Button('終了')]]

    # 窗の生成
    window = psg.Window('EzSed', layout)

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
        msg = f'Program: {__prog__}'
        g_log.info(msg)
        msg = f'      LIST: {args.list}'
        g_log.info(msg)

    _analyze_options(args, window)

    msg = '[*] 正常終了'
    if args.verbose:
        g_log.info(msg)
# End of def main():


if __name__ == '__main__':
    main()
