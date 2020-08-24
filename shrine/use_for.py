#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 記法 	概要
# {% … %} 	Statements
# {{ … }} 	Expressions
# {# … #} 	コメント
# # … ## 	Line Statements
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""雛型を用ゐた神社貳の基本的な使ひ方の例.

usage: use_for [-h] [-V] [-t] [-v] [-f FILE]

options:
    -f FILE, --file=FILE    雛型書類
    -v, --verbose           詳細情報表示
    -h, --help              補助情報表示
    -V, --version           履歴情報表示
    -t, --test              埋込み試驗實施

The require modules:
（標準品以外の必要なもの）
    docopt
    jinja2

environments:
    python 3.7 以上で動作します。
"""

import doctest
import sys
try:
    from docopt import docopt
    from jinja2 import Environment, FileSystemLoader
except ModuleNotFoundError:
    print('[!!] Please install the required modules.', file=sys.stderr)
    sys.exit(__doc__)
# End of except ModuleNotFoundError:

__prog__ = 'use_for.py'
__version__ = '0.1'


def mk_txt(temp, vbs=False):
    """雛型を本に作文します.

    Args:
        temp(str):      雛型書類名
        vbs(bool):      詳細情報表示旌旗
    Returns:
        str:            作成された文
    Raises:
        TypeError:      引數の型の不具合
        AssertionError: 不具合
    Examples:
        >>> mk_txt('test00.tpl')
        'Hello !'
    """
    if not isinstance(temp, str):
        raise TypeError('[!!] <temp> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(temp)

    data = {'items': [5, 'みかん', 'りんご', 'バナナ']}
    disp_text = template.render(data)

    return disp_text
# End of def mk_txt(temp, vbs=False):


def main():
    """主函數."""
    tmpfile = 'for.tpl'
    args = docopt(__doc__)
    if args['--test']:
        doctest.testmod(verbose=args['--verbose'])
        sys.exit()
    if args['--version']:
        sys.exit(f'Ver: {__version__}')
    if args['--file']:
        tmpfile = args['--file']
    if args['--verbose']:
        print('[*] basis.py')
        print(f'\tTemplate file: {tmpfile:s}')

    text = mk_txt(tmpfile, args['--verbose'])
    print(text)
# End of def main():


if __name__ == '__main__':
    main()
