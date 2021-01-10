#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.2.3   Sed處理の外部化
# Ver.2.5   名前變更(coresed -> poorsed)
"""ストリーム・エディタ.

資料をストリーム・エディタで變換します。

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

# import pprint as pp         # For debug
# import ezo.deco as deco     # For debug

__prog__ = 'poorsed.py'
__description__ = '資料をストリーム・エディタで變換します。'
__epilog__ = '發生した不具合は./msg_ezsed.logに記録されます。'
__version__ = '2.5'


class Sed:
    """Sed.

    ストリーム・エディタ

    Attributes:
        data (str):     文

    Samples:
        >>> Sed.factory('This is a pen.')
        class Sed.
    """

    def __init__(self, data, vbs=False, clog=None):
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
            if clog:
                clog.error('[!!] Sed.__init__(): <data> must be a string.')
            raise TypeError('[!!] <data> must be a string.')
        assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

        self._data = data
        self._vbs = vbs
        self._log = clog
    # End of def __init__(self, data, vbs=False, clog=None):

    @classmethod
    def factory(cls, data, vbs=False, clog=None):
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
        return cls(data, vbs, clog)
    # End of def factory(cls, data, vbs=False, clog=None):

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
            raise TypeError('[!!] <keys> must be a string.')
        if not isinstance(vals, str):
            raise TypeError('[!!] <vals> must be a string.')
        if len(vals) < len(keys):
            raise ValueError('[!!] <keys> are too many.')
        if len(keys) == 0:
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
            if self._log:
                self._log.error('[!!] Sed.y_command(): <dic> must be a dictionary.')
            raise TypeError('[!!] <dic> must be a dictionary.')
        if len(dic) <= 0:
            if self._log:
                self._log.error('[!!] Sed.y_command(): <dic> are not empty.')
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
            if self._log:
                self._log.error('[!!] Sed.s_command(): <oldstr> must be a string.')
            raise TypeError('[!!] <oldstr> must be a string.')
        if not isinstance(newstr, str):
            if self._log:
                self._log.error('[!!] Sed.s_command(): <newstr> must be a string.')
            raise TypeError('[!!] <newstr> must be a string.')
        if not isinstance(cnt, int):
            if self._log:
                self._log.error('[!!] Sed.s_command(): <cnt> must be an integer.')
            raise TypeError('[!!] <cnt> must be an integer.')
        if cnt < 0:
            if self._log:
                self._log.error('[!!] Sed.s_command(): <cnt> must be not negative.')
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


def analyze_script(script, vbs=False, clog=None):
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
        if clog:
            clog.error('[!!] analyze_script(): <script> must be a string.')
        raise TypeError('[!!] <script> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    newscript = Sed.del_comment(script)
    if len(newscript) <= 0:
        msg = '[!!] analyze_script(): empty script: {script}'
        if clog:
            clog.debug(msg)
        return []
    script_list = newscript.split('/')
    return script_list
# End of def analyze_script(script, vbs=False, clog=None):


def get_scripts(script_list, vbs=False, clog=None):
    """臺本一覽書類の讀込.

    Args:
        script_list (str):  臺本の一覽書類名
        vbs (bool):         詳細情報表示旌旗

    Returns:
        list:               臺本の一覽

    Raises:
        AssertionError:     不具合
    """
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    scripts = []
    if not os.path.isfile(script_list):
        # 臺本書類一覽が無い場合
        msg = f'[!!] 臺本書類一覽がありません: {script_list}'
        if clog:
            # mbox.showerror(TITLE, msg)
            clog.error(msg)
            sys.exit(1)
        else:
            sys.exit(msg)
    with open(script_list, mode='r', encoding='utf-8') as fpr:
        # 臺本書類一覽の讀込み
        scriptfiles = fpr.readlines()

    for scriptfile in scriptfiles:
        # 臺本書類毎の處理
        if scriptfile[0] == '#':
            # コメントを讀み飛ばす。
            continue
        scriptfile = scriptfile.rstrip()
        if not os.path.isfile(scriptfile):
            msg = f'[!!] 臺本書類がありません: {scriptfile}'
            # mbox.showerror(TITLE, msg)
            if clog:
                clog.error(msg)
                sys.exit(1)
            else:
                sys.exit(msg)
        # End of if not os.path.isfile(scriptfile):

        with open(scriptfile, mode='r', encoding='utf-8') as fpr:
            # 臺本書類の讀込み
            scripts += fpr.readlines()
    # End of for scriptfile in scriptlist:

    return scripts
# End of def get_scripts(script_list, vbs=False, clog=None):


# @deco.stopwatch
def run(scripts, data, rev=False, vbs=False, clog=None):
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
        clog.error('[!!] run(): <data> must be a string.')
        raise TypeError('[!!] <data> must be a string.')
    if not isinstance(scripts, list):
        clog.error('[!!] run(): <scripts> must be a list.')
        raise TypeError('[!!] <scripts> must be a list.')
    assert isinstance(rev, bool), '[!!] <rev> must be boolean.'
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    sed = Sed(data, vbs, clog)
    for script in scripts:
        script = script.rstrip()    # 改行符號を取除く。
        new_script = sed.del_comment(script)
        if new_script != '':
            lst = analyze_script(new_script, vbs, clog)
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
                clog.warning(msg)
            # End of else:
        # End of if new_script != '':
    # End of for script in scripts:

    return sed.get_data()
# End of def run(scripts, data, rev=False, vbs=False):


def _analyze_options(args, clog):
    """選擇肢への對應.

    Args:
        args (argparse.Namespace):      處理の選擇肢情報

    Raises:
        AssertionError: 不具合
    """
    assert isinstance(args, argparse.Namespace), '[!!] args error.'

    # 臺本の讀込
    if args.list:
        scripts = get_scripts(args.list, args.verbose, clog)
    else:
        msg = '[!!] 臺本書類一覽を指定して下さい。'
        clog.error(msg)
        sys.exit(msg)
    # End of else:

    # 資料の讀込
    if args.infile:
        with open(args.infile, mode='r', encoding='utf-8') as fpr:
            data = fpr.read()
    else:
        data = ppc.paste()
    # End of else:

    # 結果出力の指定
    result = run(scripts, data, args.reverse, args.verbose, clog)
    print(result)
# End of def _analyze_options(args, clog):


# @deco.stopwatch
def main():
    """Do main function.

    選擇肢に本づいて文字列を變換します。

    Tests:
        >>> import poorsed

    Note:
        何かあれば。

    Todo:
        * 課題の項目
        * 課題の項目
    """
    parser = argparse.ArgumentParser(
        prog=__prog__,
        description=__description__,
        epilog=__epilog__,
        add_help=True,
        )
    parser.add_argument('-l', '--list',
                        default='/home/ozawa3/kali.lst',
                        help='臺本書類一覽（無指定なら、~/sed.lst）')
    parser.add_argument('-i', '--infile',
                        default=None,
                        help='資料書類')
    parser.add_argument('-r', '--reverse',
                        default=False,
                        help='Sedを逆變換',
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
    handler = log.FileHandler(filename='msg_poorsed.log', encoding='utf-8')
    _fmt = '%(asctime)s %(levelname)-5.5s %(message)s'
    fmt = log.Formatter(_fmt)
    handler.setFormatter(fmt)
    clog = log.getLogger('file-logger')
    clog.addHandler(handler)

    if args.test:
        doctest.testmod(verbose=args.verbose)
        sys.exit()

    if args.version:
        mbox.showinfo(TITLE, f'Ver: {__version__}')
        sys.exit()

    if args.verbose:
        msg = f'Program: {__prog__}'
        clog.info(msg)
        msg = f'      LIST:    {args.list}'
        clog.info(msg)
        msg = f'      DATA:    {args.data}'
        clog.info(msg)
        msg = f'      INPUT:   {args.infile}'
        clog.info(msg)
        msg = f'      REVERSE: {args.reverse}'
        clog.info(msg)

    msg = f'[*] 開始：{__prog__}'
    if args.verbose:
        clog.info(msg)

    _analyze_options(args, clog)

    msg = '[*] 正常終了'
    if args.verbose:
        clog.info(msg)
# End of def main():


if __name__ == '__main__':
    main()
