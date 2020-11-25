#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   s命令實裝
# Ver.0.2   y命令實裝
# Ver.0.3   --expression選擇肢
# Ver.0.4   --fiile選擇肢
# Ver.0.5   --display選擇肢
# Ver.0.6   入力書類對應
# Ver.0.7   負具合記録對應
# Ver.0.8   MsgBoxで命令の説明表示
# Ver.0.9   --output選擇肢
# Ver.1.0   公開
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
__version__ = '1.0'
__usage__ = '''
入力書類をストリーム・エディタで變換します。

usage: ezsed.exe [-?] [-e EXPRESSION] [-f FILE] [-s] [INPUT]

positional arguments:
  INPUT                 入力書類（無指定ならクリップボード）

optional arguments:
  -?, --description     説明を表示
  -e EXPRESSION, --expression EXPRESSION
                        臺本
  -f FILE, --file FILE  臺本書類（無指定なら、/script.sed）
  -o OUTPUT, --output OUTPUT
                        出力書類（無指定ならクリップボード）
  -V, --version         履歴情報表示
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

        Tests:
            >>> sed = Sed('green')
            >>> sed._data
            'green'
            >>> sed._vbs
            False
            >>> sed = Sed('red', True)
            >>> sed._data
            'red'
            >>> sed._vbs
            True
            >>> sed = Sed(3.14192)
            Traceback (most recent call last):
                ...
            TypeError: [!!] <data> must be a string.
            >>> sed = Sed('red', [])
            Traceback (most recent call last):
                ...
            AssertionError: [!!] <vbs> must be boolean.

        Note:
            實體作成時は工房を使用して下さい。
        """
        if not isinstance(data, str):
            raise TypeError('[!!] <data> must be a string.')
        assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'
        self._data = data
        self._vbs = vbs
    # End of def __init__(self, data, vbs=False):

    @classmethod
    def factory(cls, data, vbs=False):
        """Sed Factory.

        ストリーム・エディタ工房

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
            newstr (str):   値となる文字列("ABC")

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
            raise TypeError('[!!] <keys> must be a string.')
        if not isinstance(vals, str):
            raise TypeError('[!!] <vals> must be a string.')
        if len(vals) < len(keys):
            raise ValueError('[!!] <keys> are too many.')
        if len(keys) == 0:
            raise ValueError('[!!] <keys> must be not empty.')

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
            raise TypeError('[!!] <dic> must be a dictionary.')
        if len(dic) <= 0:
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
            raise TypeError('[!!] <oldstr> must be a string.')
        if not isinstance(newstr, str):
            raise TypeError('[!!] <newstr> must be a string.')
        if not isinstance(cnt, int):
            raise TypeError('[!!] <cnt> must be an integer.')
        if cnt < 0:
            raise ValueError('[!!] <cnt> must be not negative.')

        if cnt == 0:
            self._data = self._data.replace(oldstr, newstr)
        else:   # if 0 < cnt:
            self._data = self._data.replace(oldstr, newstr, cnt)
    # End of def s_command(self, oldstr, newstr, cnt=0):

    def __repr__(self):
        """Show representation.

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
        raise TypeError('[!!] <script> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    newscript = Sed.del_comment(script)
    if len(newscript) < 0:
        return []
    script_list = newscript.split('/')
    return script_list
# End of def analyze_script(script, vbs=False):


# @deco.stopwatch
def run(scripts, data, vbs=False):
    """Edit stream.

    ストリーム・エディタ處理の實行。.

    Args:
        scripts (list): スクリブトの一覽
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
        raise TypeError('[!!] <data> must be a string.')
    if not isinstance(scripts, list):
        raise TypeError('[!!] <scripts> must be a list.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    sed = Sed(data, vbs)
    for script in scripts:
        script = script.rstrip()
        new_script = sed.del_comment(script)
        if new_script != '':
            lst = analyze_script(new_script, vbs)
            if len(lst) <= 0:
                continue
            if lst[0] == 's':
                if lst[3] == 'g':
                    sed.s_command(lst[1], lst[2], cnt=0)
                else:   # if lst[3] != 'g':
                    sed.s_command(lst[1], lst[2], cnt=1)
                # End of else:
            elif lst[0] == 'y':
                sed.y_command(sed.mk_dict(lst[1], lst[2]))
            else:   # if lst[0] != 'y':
                msg = f'[!] Unsupported command: {lst}'
                if vbs:
                    print(msg, file=sys.stderr)
                g_log.warning(msg)
            # End of else:
        # End of if new_script != '':
    # End of for script in scripts:

    return sed.get_data()
# End of def run(scripts, data, vbs=False):


def _proc(args):
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
    else:
        if not os.path.isfile(args.file):
            msg = f'臺本がありません: {args.file}'
            mbox.showerror(TITLE, msg)
            g_log.error(msg)
            sys.exit(1)
        with open(args.file, mode='r', encoding='utf-8') as fpr:
            scripts = fpr.readlines()
    # End of else:

    # 資料の取得
    if args.infile:
        if not os.path.isfile(args.infile):
            msg = f'入力書類がありません: {args.infile}'
            mbox.showerror(TITLE, msg)
            g_log.error(msg)
            sys.exit(1)
        with open(args.infile, mode='r', encoding='utf-8') as fpr:
            data = fpr.read()
    else:   # if not args.infile:
        data = ppc.paste()
    # End of else:

    # 結果出力の指定
    result = run(scripts, data, args.verbose)
    if args.output:
        result = run(scripts, data, args.verbose).replace('\r', '')
        with open(args.output, mode='w', encoding='utf-8') as fpw:
            fpw.write(result)
    if args.stdout:
        # 結果を標準出力する。
        print(result)
    else:   # if not args.display:
        # 結果をクリップボードに出力する。
        ppc.copy(result)
    # End of else:
# End of def _proc(args):


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
    parser.add_argument(dest='infile',
                        metavar='INPUT',
                        nargs='?',
                        default=None,
                        help='入力書類（無指定ならクリップボード）')
    parser.add_argument('-?', '--description',
                        help='MsgBoxで説明表示',
                        action='store_true')
    parser.add_argument('-e', '--expression',
                        default=None,
                        help='臺本')
    parser.add_argument('-f', '--file',
                        default='./script.sed',
                        help='臺本書類（無指定なら、/script.sed）')
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
        print(f'Program: {__prog__}')
        print(f' EXPRESSON: {args.expression}')
        print(f'      FILE: {args.file}')
        print(f'     INPUT: {args.infile}')
        print(f'    OUTPUT: {args.output}')

    _proc(args)
# End of def main():


if __name__ == '__main__':
    main()
