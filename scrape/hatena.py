#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
# Ver.0.2   表示情報追加
# Ver.0.3   備考の抽出

__prog__ = 'today.py'
__description__ = 'はてなブックマーク'
__epilog__ = 'Python 3.9 以上で動作します。'
__version__ = '0.3'

import sys
import argparse
import doctest
import requests as req
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

    #if vbs:
    #    print('[*] get_info():')

    res = req.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    top = soup.find('section', attrs={'class': 'entrylist-unit'})
    entries = top.find_all('div', attrs={'class': 'entrylist-contents'})
    today_list = []

    for entry in entries:

        title_tag = entry.find(
                'h3', attrs={'class': 'entrylist-contents-title'})
        title = title_tag.find('a').get('title')

        bm_tag = entry.find(
                'span', attrs={'class': 'entrylist-contents-users'})
        bm_link = bm_tag.find('a').get('href')
        bm_url = url + bm_link

        if vbs:
            res = req.get(bm_url)
            soup = BeautifulSoup(res.content, 'html.parser')
            coms = soup.find_all(
                    'span', attrs={'class': 'entry-comment-text'})
                    #'span', attrs={'class': 'entry-comment-text js-bookmark-comment'})
            com_list = []
            for com in entries:

                #print(com)
                #exit()
                com_tag = com.find(
                    'p', attrs={'class': 'entrylist-contents-description' })
                com_list.append(com_tag.text)
            # End of for com in entries:
        #title = title_tag.find('a').get('title')
            today_list.append({'title': title,
                               'url': bm_url,
                               'comment': com_list})
        else:
            today_list.append({'title': title,
                               'url': bm_url})

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
                        default='https://b.hatena.ne.jp',
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

    #if args.verbose:
    #    print(f'Program: {__prog__}')

    res = get_info(args.url, args.verbose)
    pp.pprint(res)
# End of def main():


if __name__ == '__main__':
    main()
