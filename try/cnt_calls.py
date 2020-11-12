#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import cnt_calls
"""

__prog__ = 'cnt_calls.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.0'

import sys
import argparse
import doctest


class CountCalls:
    """車輛.

    Attributes:
        color (str):    色

    >>> CountCalls()
    class CountCalls.
    """

    def __init__(self, fn):
        """Iniitialize CountCalls."""
        self.fn = fn
        self.called = 0
    # End of def __init__(self, fn):

    def __call__(self, *args, **kwargs):
        """Calls."""
        self.called = 1
        return self.fn(*args, **kwargs)
    # End of def __call__(self, *args, **kwargs):

    def __repr__(self):
        """Show representation.

        >>> car = CountCalls()
        >>> repr(car)
        'class CountCalls.'
        """
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class CountCalls:


@CountCalls
def pr_hello():
    print('hello')
# End of def pr_hello():


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
        AssertionError
    """
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    if vbs:
        print('[*] Run:')

    print(f'called: {pr_hello.called}')
    pr_hello()
    print(f'called: {pr_hello.called}')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import cnt_calls
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
