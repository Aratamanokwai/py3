#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import abc_mro
"""

__prog__ = 'abc_mro.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.6 以上で動作します。'
__version__ = '0.0'

import sys
import argparse
import doctest


class A(object):
    bar = 42

    def foo(self):
        pass
    # End of def foo(self):
# End of class A(object):


class B(object):
    bar = 0
# End of class B(object):


class C(A, B):
    xyz = 'abc'
# End of class C(A, B):


class D(C):
    sup = super(C)
# End of class D(C):


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
    print(f'C.mro(): {C.mro()}')
    print(f'super(C, C()).bar: {super(C, C()).bar}')
    print(f'super(C, C()).foo: {super(C, C()).foo}')
    print(f'super(C, C()).foo(): {super(C, C()).foo()}')
    print(f'super(B).__self__: {super(B).__self__}')
    print(f'super(B, B()).__self__: {super(B, B()).__self__}')

    print(f'super(C): {super(C)}')
    print(f'D().sup: {D().sup}')
    print(f'D().sup.foo: {D().sup.foo}')
    print(f'D().sup.bar: {D().sup.bar}')
    #print(f's')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import abc_mro
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
