#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
# Ver.1.0   公開
"""標本算譜.

Tests:
    >>> __prog__ == 'temp.py'
    True
"""

import sys
import argparse
import doctest
# try:
#     import outer_module     # 外部モジュール
# except Exception:
#     sys.exit('[!!] 外部モジュールの導入が必要です。')

__prog__ = 'temp.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.0'


class Car:
    """車輛.

    詳細説明

    Attributes:
        color (str):    色

    Tests:
        >>> Car()
        class Car.
        >>> Car.factory()
        class Car.
    """

    def __init__(self, color='red'):
        """Iniitialize Car.

        Tests:
            >>> car = Car('green')
            >>> car.color
            'green'

        Note:
            實體作成時は工房を使用して下さい。
        """
        self.color = color
    # End of def __init__(self, color, mileage):

    # selfが使用されず、束縛される必要が無い手法は
    # 靜的手法として宣言すべきである。
    # @staticmethod

    @classmethod
    def factory(cls, color='red'):
        """Car Factory.

        自動車工房

        Samples:
            >>> car = Car.factory('green')
            >>> car.color
            'green'
        """
        return cls(color)
    # End of def factory(cls, color='red'):

    def __repr__(self):
        """Show representation.

        Samples:
            >>> car = Car.factory()
            >>> repr(car)
            'class Car.'
        """
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class Car:


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
        >>> import temp

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
