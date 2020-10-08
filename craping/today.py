#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作

__prog__ = 'tody.py'
__description__ = '今日は何の日？'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest
import requests
from bs4 import BeautifulSoup


url = 'https://ja.wikipedia.org'


class Car:
    """車輛.

    Attributes:
        color (str):    色

    >>> Car()
    Car(red)
    """

    def __init__(self, color='red'):
        """Iniitialize Car."""
        self.color = color
    # End of def __init__(self, color, mileage):

    def __repr__(self):
        """Show the representation.

        >>> car = Car()
        >>> repr(car)
        'Car(red)'
        """
        return f'{self.__class__.__name__}({self.color})'
    # End of def __repr__(self):

    def __str__(self):
        """Show the string.

        >>> car = Car()
        >>> str(car)
        'class Car'
        """
        return f'class {self.__class__.__name__}'
    # End of def __str__(self):
# End of class Car:


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

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    today = soup.find('div', attrs={'id': 'on_this_day'}).text

    print(today)
# End of def run(vbs=False):


def main():
    """主函數.

    >>> import tody
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
