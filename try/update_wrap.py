#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import update_wrap
"""

__prog__ = 'update_wrap.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.0'

import sys
import argparse
import doctest
import functools


def is_admin(fn):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('[!!] This user is not allowed.')
        return fn(*args, **kwargs)
    # End of def wrapper(*args, **kwargs):

    return wrapper
# End of def is_admin(fn):


def foobar(username='someone'):
    """Do crazy stuff."""
    pass
# End of def foobar(username='someone'):


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

    _foobar = functools.update_wrapper(is_admin, foobar)
    print('[*] foobar')
    print(f'__name__: {_foobar.__name__}')
    print(f'__doc__: {_foobar.__doc__}')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import update_wrap
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
