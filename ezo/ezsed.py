#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   s命令實裝
# Ver.0.2   y命令實裝
# Ver.1.0   公開
"""ストリーム・エディタ.

Tests:
    >>> __prog__ == 'ezsed.py'
    True
"""

import sys
import argparse
import doctest

__prog__ = 'ezsed.py'
__description__ = 'Easy Stream Editor'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.2'


class Sed:
    """Sed.

    ストリーム・エディタ

    Attributes:
        line (str):     文

    Samples:
        >>> Sed.factory('This is a pen.')
        class Sed.
    """

    def __init__(self, line, vbs=False):
        """Iniitialize Sed.

        Args:
            line (str):     文
            vbs (bool):     詳細情報表示旌旗

        Raises:
            TypeError:      引數の型の不具合
            ValueError:     引數の値の不具合
            AssertionError: 不具合

        Tests:
            >>> sed = Sed('green')
            >>> sed._line
            'green'
            >>> sed._vbs
            False
            >>> sed = Sed('red', True)
            >>> sed._line
            'red'
            >>> sed._vbs
            True
            >>> sed = Sed(3.14192)
            Traceback (most recent call last):
                ...
            TypeError: [!!] <line> must be a string.
            >>> sed = Sed('red', [])
            Traceback (most recent call last):
                ...
            AssertionError: [!!] <vbs> must be boolean.

        Note:
            實體作成時は工房を使用して下さい。
        """
        if not isinstance(line, str):
            raise TypeError('[!!] <line> must be a string.')
        assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'
        self._line = line
        self._vbs = vbs
    # End of def __init__(self, line, vbs=False):

    @classmethod
    def factory(cls, line, vbs=False):
        """Sed Factory.

        ストリーム・エディタ工房

        Samples:
            >>> sed = Sed.factory('green')
            >>> sed.get_line()
            'green'
        """
        return cls(line, vbs)
    # End of def factory(cls, line, vbs=False):

    def get_line(self):
        """Ged the line.

        文を取得する。

        Returns:
            str:        文

        Samples:
            >>> sed = Sed.factory('green')
            >>> sed.get_line()
            'green'
        """
        return self._line
    # End of def get_line(self):

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

        Tests:
            >>> Sed.mk_dict([], 'CD')
            Traceback (most recent call last):
                ...
            TypeError: [!!] <keys> must be a string.
            >>> Sed.mk_dict('cd', {})
            Traceback (most recent call last):
                ...
            TypeError: [!!] <vals> must be a string.
            >>> Sed.mk_dict('abc', 'CD')
            Traceback (most recent call last):
                ...
            ValueError: [!!] <keys> are too many.
            >>> Sed.mk_dict('', 'CD')
            Traceback (most recent call last):
                ...
            ValueError: [!!] <keys> must be not empty.
        """
        if not isinstance(keys, str):
            raise TypeError('[!!] <keys> must be a string.')
        if not isinstance(vals, str):
            raise TypeError('[!!] <vals> must be a string.')
        if len(vals) < len(keys):
            raise ValueError('[!!] <keys> are too many.')
        if 0 == len(keys):
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
            >>> sed.get_line()
            'No MeloN No leMoN.'
        """
        if not isinstance(dic, dict):
            raise TypeError('[!!] <dic> must be a dictionary.')
        if len(dic) <= 0:
            raise ValueError('[!!] <dic> must be not empty.')
        self._line = self._line.translate(str.maketrans(dic))
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
            >>> sed.get_line()
            'yes melon yes lemon.'
            >>> sed.s_command('yes', 'none', 1)
            >>> sed.get_line()
            'none melon yes lemon.'

        Tests:
            >>> sed = Sed('no melon no lemon.')
            >>> sed.s_command(3, 'yes')
            Traceback (most recent call last):
                ...
            TypeError: [!!] <oldstr> must be a string.
            >>> sed.s_command('no', 2.718281828)
            Traceback (most recent call last):
                ...
            TypeError: [!!] <newstr> must be a string.
            >>> sed.s_command('no', 'yes', 'two')
            Traceback (most recent call last):
                ...
            TypeError: [!!] <cnt> must be an integer.
            >>> sed.s_command('no', 'yes', -5)
            Traceback (most recent call last):
                ...
            ValueError: [!!] <cnt> must be not negative.
            >>> sed = Sed('')
            >>> sed.s_command('no', 'yes')
            >>> sed.get_line()
            ''
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
            self._line = self._line.replace(oldstr, newstr)
        else:   # if 0 < cnt:
            self._line = self._line.replace(oldstr, newstr, cnt)
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


def run(vbs=False):
    """處理實行.

    詳細説明

    Args:
        vbs (bool):     詳細情報表示旌旗

    Returns:
        bool:           處理結果

    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合

    Examples:
        >>> run(1)
        Traceback (most recent call last):
            ...
        AssertionError: [!!] <vbs> must be boolean.
    """
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    if vbs:
        print('[*] Run:')
# End of def run(vbs=False):


def main():
    """Do main function.

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
    if args.test:
        doctest.testmod(verbose=args.verbose)
        sys.exit()

    if args.version:
        print('Ver: {}'.format(__version__))
        sys.exit()

    if args.verbose:
        print(f'Program: {__prog__}')

    run(args.verbose)
# End of def main():


if __name__ == '__main__':
    main()
