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
"""ストリーム・エディタ.

クリップボードの資料をストリーム・エディタで變換します。

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

# import pprint as pp         # For debug
# import ezo.deco as deco     # For debug

__prog__ = 'ezsed.py'
__description__ = '入力書類をストリーム・エディタで變換します。'
__epilog__ = '發生した不具合は./msg_ezsed.logに記録されます。'
__version__ = '1.6'
__usage__ = '''
入力書類をストリーム・エディタで變換します。

usage: ezsed.exe [-?] [-e EXPRESSION] [-f FILE] [-s]
                    [-i INPUT] [-o OUTPUT]

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

#### 注意

發生した不具合は./msg_ezsed.logに記録されます。
'''

g_log = log.getLogger('file-logger')
TITLE = 'ezsed.exe'


class Sed:
    """Sed.

    ストリーム・エディタ

    Attributes:
        data (str):     文

    Samples:
        >>> Sed.factory('This is a pen.')
        class Sed.
    """

    def __init__(self, data, vbs=False):
        """Iniitialize Sed.

        Args:
            data (str):     文
            vbs (bool):     詳細情報表示旌旗

        Raises:
            TypeError:      引數の型の不具合
            ValueError:     引數の値の不具合
            AssertionError: 不具合

        Note:
            實體作成時は工房を使用して下さい。
        """
        if not isinstance(data, str):
            g_log.error('[!!] Sed.__init__(): <data> must be a string.')
            raise TypeError('[!!] <data> must be a string.')
        assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

        self._data = data
        self._vbs = vbs
    # End of def __init__(self, data, vbs=False):

    @classmethod
    def factory(cls, data, vbs=False):
        """Sed Factory.

        ストリーム・エディタ工房

        Args:
            data (str):     文
            vbs (bool):     詳細情報表示旌旗

        Samples:
            >>> sed = Sed.factory('green')
            >>> sed.get_data()
            'green'
        """
        return cls(data, vbs)
    # End of def factory(cls, data, vbs=False):

    def get_data(self):
        """Ged the data.

        文を取得する。

        Returns:
            str:        文

        Samples:
            >>> sed = Sed.factory('green')
            >>> sed.get_data()
            'green'
        """
        return self._data
    # End of def get_data(self):

    @staticmethod
    def del_comment(script):
        """Delete comment.

        臺本からコメントを取除きます。

        Args:
            script (str):   臺本

        Returns:
            str:            コメントを取り除いた臺本。

        Raises:
            AssertionError: 不具合
        """
        assert isinstance(script, str), '[!!] <script> must be a string.'

        script = script.strip()
        if len(script) <= 0:
            script = ''
        elif script[0] == '#':
            script = ''
        return script
    # End of def del_comment(script):

    @staticmethod
    def mk_dict(keys, vals):
        """Make the dictionary.

        y命令に使用する辭書を作成します。

        Args:
            keys (str):     鍵となる文字列("abc")
            vals (str):     値となる文字列("ABC")

        Returns:
            dict:           辭書({'a': 'A', 'b': 'B', 'c': 'C'})

        Raises:
            TypeError:      引數の型の不具合
            ValueError:     引數の値の不具合
            AssertionError: 不具合

        Samples:
            >>> sed = Sed.factory('green')
            >>> sed.mk_dict('ab', 'AB')
            {'a': 'A', 'b': 'B'}
            >>> Sed.mk_dict('cd', 'CD')
            {'c': 'C', 'd': 'D'}
        """
        if not isinstance(keys, str):
            g_log.error('[!!] Sed.mk_dict(): <keys> must be a string.')
            raise TypeError('[!!] <keys> must be a string.')
        if not isinstance(vals, str):
            g_log.error('[!!] Sed.mk_dict(): <vals> must be a string.')
            raise TypeError('[!!] <vals> must be a string.')
        if len(vals) < len(keys):
            g_log.error('[!!] Sed.mk_dict(): <keys> are too many.')
            raise ValueError('[!!] <keys> are too many.')
        if len(keys) == 0:
            g_log.error('[!!] Sed.mk_dict(): <keys> are not empty.')
            raise ValueError('[!!] <keys> must be not empty.')

        # 辭書作成
        dic = {}
        for idx, key in enumerate(keys):
            dic[key] = vals[idx]
        return dic
    # End of def mk_dict(keys, vals):

    def y_command(self, dic):
        """Command y.

        文を辭書に本づいて變換します。

        Args:
            dic (dict):     變換辭書

        Raises:
            TypeError:      引數の型の不具合
            ValueError:     引數の値の不具合
            AssertionError: 不具合

        Note:
            辭書はmk_dict()で作成出來ます。

        Samples:
            >>> sed = Sed('no melon no lemon.')
            >>> sed.y_command({'n': 'N', 'm': 'M'})
            >>> sed.get_data()
            'No MeloN No leMoN.'
        """
        if not isinstance(dic, dict):
            g_log.error('[!!] Sed.y_command(): <dic> must be a dictionary.')
            raise TypeError('[!!] <dic> must be a dictionary.')
        if len(dic) <= 0:
            g_log.error('[!!] Sed.y_command(): <dic> are not empty.')
            raise ValueError('[!!] <dic> must be not empty.')

        self._data = self._data.translate(str.maketrans(dic))
    # End of def y_command(self, dic):

    def s_command(self, oldstr, newstr, cnt=0):
        """Command s.

        文のoldstrをnewstrに置換します。

        Args:
            oldstr (str):   置換前の文字型
            newstr (str):   置換後の文字型
            cnt (int):      置換回數（０の場合は全て置換）

        Raises:
            TypeError:      引數の型の不具合
            ValueError:     引數の値の不具合
            AssertionError: 不具合

        Samples:
            >>> sed = Sed('no melon no lemon.')
            >>> sed.s_command('no', 'yes')
            >>> sed.get_data()
            'yes melon yes lemon.'
            >>> sed.s_command('yes', 'none', 1)
            >>> sed.get_data()
            'none melon yes lemon.'
        """
        if not isinstance(oldstr, str):
            g_log.error('[!!] Sed.s_command(): <oldstr> must be a string.')
            raise TypeError('[!!] <oldstr> must be a string.')
        if not isinstance(newstr, str):
            g_log.error('[!!] Sed.s_command(): <newstr> must be a string.')
            raise TypeError('[!!] <newstr> must be a string.')
        if not isinstance(cnt, int):
            g_log.error('[!!] Sed.s_command(): <cnt> must be an integer.')
            raise TypeError('[!!] <cnt> must be an integer.')
        if cnt < 0:
            g_log.error('[!!] Sed.s_command(): <cnt> must be not negative.')
            raise ValueError('[!!] <cnt> must be not negative.')

        val = re.compile(oldstr)
        self._data = val.sub(newstr, self._data, cnt)
    # End of def s_command(self, oldstr, newstr, cnt=0):

    def __repr__(self):
        """Show representation.

        Sanples:
            >>> sed = Sed.factory('This is a pen.')
            >>> repr(sed)
            'class Sed.'
        """
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class Sed:


def analyze_script(script, vbs=False):
    """臺本解析.

    Args:
        script (str):   スクリブト
        vbs (bool):     詳細情報表示旌旗

    Returns:
        list:           '/'で分割された文字列の一覽

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合

    Samples:
        >>> analyze_script('y/nm/NM/')
        ['y', 'nm', 'NM', '']
        >>> analyze_script('y/nm/NM/g')
        ['y', 'nm', 'NM', 'g']
        >>> analyze_script('s/nm/NM/')
        ['s', 'nm', 'NM', '']
    """
    if not isinstance(script, str):
        g_log.error('[!!] analyze_script(): <script> must be a string.')
        raise TypeError('[!!] <script> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    newscript = Sed.del_comment(script)
    if len(newscript) <= 0:
        msg = '[!!] analyze_script(): empty script: {script}'
        g_log.debug(msg)
        return []
    script_list = newscript.split('/')
    return script_list
# End of def analyze_script(script, vbs=False):


# @deco.stopwatch
def run(scripts, data, vbs=False):
    """Edit stream.

    ストリーム・エディタ處理の實行。.

    Args:
        scripts (list): 臺本の一覽
        data (str):     文字列
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
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    sed = Sed(data, vbs)
    for script in scripts:
        script = script.rstrip()    # 改行符號を取除く。
        new_script = sed.del_comment(script)
        if new_script != '':
            lst = analyze_script(new_script, vbs)
            if len(lst) <= 0:
                continue
            if lst[0] == 's':
                # s命令の實行
                if lst[3] == 'g':
                    sed.s_command(lst[1], lst[2], cnt=0)
                else:   # if lst[3] != 'g':
                    sed.s_command(lst[1], lst[2], cnt=1)
                # End of else:
            elif lst[0] == 'y':
                # y命令の實行
                sed.y_command(sed.mk_dict(lst[1], lst[2]))
            else:   # if lst[0] != 'y':
                msg = f'[!] Unsupported command: {lst}'
                if vbs:
                    g_log.warning(msg)
            # End of else:
        # End of if new_script != '':
    # End of for script in scripts:

    return sed.get_data()
# End of def run(scripts, data, vbs=False):


def _analyze_options(args):
    """選擇肢への對應.

    Args:
        args (argparse.Namespace):      處理の選擇肢情報

    Raises:
        AssertionError: 不具合
    """
    assert isinstance(args, argparse.Namespace), '[!!] args error.'

    # 臺本の讀込
    if args.expression:
        scripts = [args.expression]
    elif args.list:
        scripts = []
        if not os.path.isfile(args.list):
            # 臺本書類一覽が無い場合
            msg = f'[!!] 臺本書類一覽がありません: {args.list}'
            mbox.showerror(TITLE, msg)
            g_log.error(msg)
            sys.exit(1)
        with open(args.list, mode='r', encoding='utf-8') as fpr:
            # 臺本書類一覽の讀込み
            scriptlist = fpr.readlines()

        for scriptfile in scriptlist:
            # 臺本書類毎の處理
            if scriptfile[0] == '#':
                # コメントを讀み飛ばす。
                continue
            scriptfile = scriptfile.rstrip()
            if not os.path.isfile(scriptfile):
                msg = f'[!!] 臺本書類がありません: {scriptfile}'
                mbox.showerror(TITLE, msg)
                g_log.error(msg)
                sys.exit(1)
            # End of if not os.path.isfile(scriptfile):

            with open(scriptfile, mode='r', encoding='utf-8') as fpr:
                # 臺本書類の讀込み
                scripts += fpr.readlines()
        # End of for scriptfile in scriptlist:
    # End of elif args.list:

    # 資料の取得
    if args.input:
        if not os.path.isfile(args.input):
            msg = f'[!!] 入力書類がありません: {args.input}'
            mbox.showerror(TITLE, msg)
            g_log.error(msg)
            sys.exit(1)
        with open(args.input, mode='r', encoding='utf-8') as fpr:
            # 入力書類の資料讀込み
            data = fpr.read()
    else:   # if not args.input:
        # クリップボードの資料讀込み
        data = ppc.paste()
    # End of else:

    # 結果出力の指定
    result = run(scripts, data, args.verbose)
    if args.output:
        result = run(scripts, data, args.verbose).replace('\r', '')
        # 結果を書類に出力する。
        with open(args.output, mode='w', encoding='utf-8') as fpw:
            fpw.write(result)
    elif args.stdout:
        # 結果を標準出力する。
        print(result)
    else:   # elif not args.display:
        # 結果をクリップボードに出力する。
        ppc.copy(result)
    # End of else:
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
    parser.add_argument('-e', '--expression',
                        default=None,
                        help='臺本')
    parser.add_argument('-l', '--list',
                        default='./sed.lst',
                        help='臺本書類一覽（無指定なら、/sed.lst）')
    parser.add_argument('-i', '--input',
                        default=None,
                        help='入力書類（無指定ならクリップボード）')
    parser.add_argument('-o', '--output',
                        default=None,
                        help='出力書類（無指定ならクリップボード）')
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
        msg = f' EXPRESSON: {args.expression}'
        g_log.info(msg)
        msg = f'      LIST: {args.list}'
        g_log.info(msg)
        msg = f'     INPUT: {args.input}'
        g_log.info(msg)
        msg = f'    OUTPUT: {args.output}'
        g_log.info(msg)

    _analyze_options(args)

    msg = '正常終了'
    if args.verbose:
        g_log.info('[*] ' + msg)
    mbox.showinfo(TITLE, msg)
# End of def main():


if __name__ == '__main__':
    main()
