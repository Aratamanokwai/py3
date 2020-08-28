#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作

__prog__ = 'contxtmngr.py'
__description__ = '前後關係管理'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.0'

import sys
import argparse
import doctest
import contextlib as ctl


class TraceContextManager:
    """前後關係管理者追跡類型.

    Tests:
        >>> with TraceContextManager():
        ...     print('今日は。')
        ...
        入口:
        今日は。
        出口:
    """

    def __enter__(self):
        """入口."""
        print('入口:')
    # End of def __enter__(self):

    def __exit__(self, exc_type, exc_value, traceback):
        """出口."""
        print('出口:')
#        print(f'exc_type : {exc_type}')
#        print(f'exc_value: {exc_value}')
#        print(f'traceback: {traceback}')
    # End of def __exit__(self, exc_type, exc_value, traceback):

    def __repr__(self):
        """Show the representation."""
        return f'{self.__class__.__name__}({self.color})'
    # End of def __repr__(self):

    def __str__(self):
        """Show the string."""
        return f'class {self.__class__.__name__}'
    # End of def __str__(self):
# End of class TraceContextManager:


@ctl.contextmanager
def trace_context_manager():
    """前後關係管理者追跡函數.

    Tests:
        >>> with trace_context_manager():
        ...     print('今日は。')
        ...
        入口:
        今日は。
        出口:
    """
    try:
        print('入口:')
        yield
    finally:
        print('出口:')
# End of def trace_context_manager():


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
    with TraceContextManager():
        print('今日は。')
# End of def run(vbs=False):


def main():
    """主函數.

    >>> import contxtmngr
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
