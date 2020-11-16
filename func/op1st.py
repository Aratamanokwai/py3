#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import my1st
"""

__prog__ = 'my1st.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest
import operator as op
from functools import partial

try:
    from first import first     # 外部モジュール
except Exception:
    sys.exit('[!!] 外部モジュールの導入が必要です。')


def grtr_than(num, min=0):
    return min < num
# End of def grtr_than(num, min=0):


def grtr_than_zero(num):
    return 0 < num
# End of def grtr_than_zero(num):


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
    print(f'first([0, False, None, [], (),42]): {first([0, False, None, [], (), 42])}')
    print(f'first([-1, 0, 1, 2]): {first([-1, 0, 1, 2])}')
    print(f'first([-1, 0, 1, 2], key=lambda x: 0 < x): {first([-1, 0, 1, 2], key=lambda x: 0 < x)}')
    print(f'first([-1, 0, 1, 2], key=grtr_than_zero): {first([-1, 0, 1, 2], key=grtr_than_zero)}')
    print(f'first([-1, 0, 1, 2], key=partial(grtr_than)): {first([-1, 0, 1, 2], key=partial(grtr_than))}')
    print(f'first([-1, 0, 1, 2], key=partial(grtr_than, min=42)): {first([-1, 0, 1, 2], key=partial(grtr_than, min=42))}')
    print(f'first([-1, 0, 1, 2], key=partial(op.lt, 1)): {first([-1, 0, 1, 2], key=partial(op.lt, 1))}')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import my1st
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
