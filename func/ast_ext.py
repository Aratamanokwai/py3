#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> __prog__ == 'ast_ext.py'
True
"""

__prog__ = 'ast_ext.py'
__description__ = 'Bad, OK'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest
#try:
#    import outer_module     # 外部モジュール
#except Exception:
#    sys.exit('[!!] 外部モジュールの導入が必要です。')


class Bad:
    # selfは使用されず、手法が束縛される必要が無いため
    # 靜的手法として宣言すべきである。
    def foo(self, a, b, c):
        return a + b - c
    # End of def foo(self, a, b, c):
# End of class Bad:


class OK:
    # 正い宣言。
    @staticmethod
    def foo(a, b, c):
        return a + b - c
    # End of def foo(a, b, c):
# End of class OK:


def run(vbs=False):
    """處理實行.

    Args:
        vbs(bool):      詳細情報表示旌旗
    Returns:
        True:           處理成功
        False:          處理失敗
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

    >>> import ast_ext
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
