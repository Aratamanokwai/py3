#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
# Ver.0.2   一覽化
# Ver.0.3   URLの引數化

__prog__ = 'today.py'
__description__ = '今日は何の日？'
__epilog__ = 'Python 3.9 以上で動作します。'
__version__ = '0.3'

import sys
import argparse
import doctest
import requests
from bs4 import BeautifulSoup
import pprint as pp


def get_info(url, vbs=False):
    """處理實行.

    Args:
        url(str):       URL
        vbs(bool):      詳細情報表示旌旗
    Returns:
        list;           取得情報
    Raises:
        TypeError:      引數の型の不具合
        ValueError:     引數の値の不具合
        AssertionError: 不具合
    Tests:
        >>> get_info(1)
        Traceback (most recent call last):
            ...
        AssertionError: [!!] <url> must be a string.
        >>> get_info('url', 1)
        Traceback (most recent call last):
            ...
        AssertionError: [!!] <vbs> must be boolean.
    """
    assert isinstance(url, str), '[!!] <url> must be a string.'
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    if vbs:
        print('[*] get_info():')

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    today = soup.find('div', attrs={'id': 'on_this_day'})
    #today = soup.find('div', attrs={'id': 'on_this_day'}).text

    entries = today.find_all('li')
    today_list = []

    for idx, entry in enumerate(entries):
        today_list.append([idx + 1, entry.get_text()])

    return today_list
# End of def get_info(url, vbs=False):


def main():
    """主函數.

    Tests:
        >>> import today
    """
    parser = argparse.ArgumentParser(
        prog=__prog__,
        # usage='usage',
        description=__description__,
        epilog=__epilog__,
        add_help=True,
        )
    parser.add_argument('-u', '--url',
                        default='https://ja.wikipedia.org',
                        help='URL')
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

    res = get_info(args.url, args.verbose)
    pp.pprint(res)
# End of def main():


if __name__ == '__main__':
    main()
