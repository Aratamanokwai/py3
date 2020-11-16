#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import myfilter
"""

__prog__ = 'myfilter.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest




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
    print(f'map:')
    lst0 = ["I think", "I'm good"]
    print(f'list: {lst0}')
    print(f'map(lambda x: x + "bzz!", list): {map(lambda x: x + "bzz!", lst0)}')
    print(f'list(map(lambda x: x + "bzz!", list)): {list(map(lambda x: x + "bzz!", lst0))}')
    print(f'(x + "bzz!" for x in list): {(x + "bzz!" for x in lst0)}')
    print(f'[x + "bzz!" for x in list]: {[x + "bzz!" for x in lst0]}')

    print(f'\nfilter:')
    print(f'filter(lambda x: x.startswith("I "), list): {filter(lambda x: x.startswith("I "), lst0)}')
    print(f'list(filter(lambda x: x.startswith("I "), list)): {list(filter(lambda x: x.startswith("I "), lst0))}')
    print(f's')
    print(f's')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import myfilter
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
