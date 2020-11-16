#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import last
"""

__prog__ = 'last.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.0'

import sys
import argparse
import doctest


def rm_last_item(mylist):
    """Remove the last item from a list."""
    mylist.pop(-1)
# End of def rm_last_item(mylist):


def but_last(mylist):
    return mylist[:-1]
# End of def but_last(mylist):


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
    lst = [idx for idx in range(5)]
    print(f'list: {lst}')
    rm_last_item(lst)
    print(f'rm_last_item: {lst}')
    lst0 = [idx for idx in range(5)]
    lst1 = but_last(lst0)
    print(f'but_last: {lst1}')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import last
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
