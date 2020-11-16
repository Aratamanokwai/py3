#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""デコレータの標本.

usage: deco.py [-h] [-V] [-v] [-t]

options:
    -h, --help      show this help message and exit.
    -V, --version   shoe version info and exit.
    -v, --verbose   verbose
    -t, --test      doctest

The require modules:
（標準品以外の必要なもの）
    docopt

履歴情報:
Ver.0.1   試作
"""

__version__ = '0.1'

import doctest
import sys
import time
import functools
import warnings
# from debtcollector import moves   # 外部モジュールなので使はない。
try:
    from docopt import docopt
except ModuleNotFoundError:
    sys.exit(__doc__)


def uppercase(func):
    """Convert returned string to uppercase.

    .. deprecated:: 0.1
        Ver.0.1以降は非推奨。
        代わりにezo.decoモジュールを使用して下さい。

    Args:
        func(callable)  returnで文字列を返す函數
    Returns:
        callable:       returnで大文字の文字列を返す函數
    Todo:
        文字列返還函數を引數で與へる。

    >>> uppercase(lambda : 'Hello!')()
    'HELLO!'
    >>> uppercase(lambda st: st)('Hi')
    'HI'
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        modi = res.upper()
        return modi
    # End of def wrapper(*args, **kwargs):

    warnings.warn('[!] Ver.0.1以降は非推奨。')
    return wrapper
# End of def uppercase(func):


def trace(func):
    """Trace the function.

    .. deprecated:: 0.1
        Ver.0.1以降は非推奨。
        代わりにezo.decoモジュールを使用して下さい。

    Args:
        func(callable)  函數
    Returns:
        callable:       追跡情報を付加した函數
    Todo:
        Nestによるindent.

    >>> trace(lambda st: st)('Hi')
    >TRACE: <lambda>() with ('Hi',), {}
    >  RET: <lambda>() returned 'Hi'
    'Hi'
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

    warnings.warn('[!] Ver.0.1以降は非推奨。')
    return wrapper
# End of def trace(func):


def stopwatch(func):
    """Stopwatch.

    .. deprecated:: 0.1
        Ver.0.1以降は非推奨。
        代わりにezo.decoモジュールを使用して下さい。

    Args:
        func(callable)  函數
    Returns:
        callable:       處理時間表示を付加した函數
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(f"處理時間： {(stop-start):.5f} 秒")
        return res
    # End of def wrapper():

    warnings.warn('[!] Ver.0.1以降は非推奨。')
    return wrapper
# End of def stopwatch(func):


@stopwatch
@trace
def main():
    """Do main function.

    >>> import deco
    """
    args = docopt(__doc__)

    print(f'__name__: {main.__name__}')
    print(f'__doc__: {main.__doc__}')

    if args['--version']:
        print(f'Ver: {__version__}')
        sys.exit()

    if args['--test']:
        doctest.testmod(verbose=args['--verbose'])
        sys.exit()

    if args['--verbose']:
        print('[*] deco.py')
# End of def main():


if __name__ == '__main__':
    main()
