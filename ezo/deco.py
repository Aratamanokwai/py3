#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 公開するときは、pylint, flake8, pydocstleを掛ける事。
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
# Ver.1.0   公開
"""装飾子.

Tests:
    >>> __prog__ == 'deco.py'
    True
"""

import time
import functools
import sys
import argparse
import doctest

__prog__ = 'deco.py'
__description__ = '装飾子.'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.1'


def uppercase(func):
    """Convert returned string to uppercase.

    文字列を返す函數を装飾して、大文字の文字列を返すやうにします。

    Args:
        func (callable):    returnで文字列を返す函數

    Returns:
        callable:           returnで大文字の文字列を返す函數

    Raises:
        AssertionError: 不具合

    Samples:
        >>> uppercase(lambda : 'Hello!')()
        'HELLO!'
        >>> uppercase(lambda st: st)('Hi')
        'HI'

    Tests:
        >>> uppercase(lambda st: 3)('Hi')
        Traceback (most recent call last):
            ...
        AssertionError: [!!] <func> must return a string.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        assert isinstance(res, str), '[!!] <func> must return a string.'
        modi = res.upper()
        return modi
    # End of def wrapper(*args, **kwargs):

    return wrapper
# End of def uppercase(func):


def trace(func):
    """Trace the function.

    函數を装飾して、
    呼出時の引數と處理後の返値を表示します。

    Args:
        func (callable):    函數

    Returns:
        callable:           追跡情報を付加した函數

    Samples:
        >>> trace(lambda st: st)('Hi')
        >TRACE: <lambda>() with ('Hi',), {}
        >  RET: <lambda>() returned 'Hi'
        'Hi'

    Todo:
        * Nestによるindent.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'>TRACE: {func.__name__}()'
              f' with {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'>  RET: {func.__name__}()'
              f' returned {res!r}')
        return res
    # End of def wrapper():

    return wrapper
# End of def trace(func):


def stopwatch(func):
    """Stopwatch.

    函數の處理時間を計測します。

    Args:
        func (callable):    函數

    Returns:
        callable:           處理時間表示を付加した函數
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(f"處理時間： {(stop-start):.5f} 秒")
        return res
    # End of def wrapper():

    return wrapper
# End of def stopwatch(func):


@stopwatch
@trace
def main():
    """Do main function.

    Tests:
        >>> import deco
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
# End of def main():


if __name__ == '__main__':
    main()
