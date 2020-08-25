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
"""雛型と辭書書類とを用ゐた神社貳の基本的な使ひ方の例.

usage: rend_html.py [-h] [-V] [-t] [-v] [-f FILE] [-p PARAM] [-o OUTPUT]

options:
    -f FILE, --file=FILE    雛型書類(jinja2)
    -p PARAM, --param=PARAM 設定（辭書）書類(json)
    -o OUTPUT, --output OUTPUT  出力書類(html)
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
import json
try:
    from docopt import docopt
    from jinja2 import Environment, FileSystemLoader
except ModuleNotFoundError:
    print('[!!] Please install the required modules.', file=sys.stderr)
    sys.exit(__doc__)
# End of except ModuleNotFoundError:

__prog__ = 'rend_html.py'
__version__ = '0.1'


def mk_html(param, temp, html='result.html', vbs=False):
    """雛型を本にhtml書類を作成します.

    Args:
        param(str):     設定（辭書）書類(json)
        temp(str):      雛型書類名(jinja2)
        vbs(bool):      詳細情報表示旌旗
    Raises:
        TypeError:      引數の型の不具合
        AssertionError: 不具合
    """
    if not isinstance(param, str):
        raise TypeError('[!!] <param> must be a string.')
    if not isinstance(temp, str):
        raise TypeError('[!!] <temp> must be a string.')
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    # 雛型書類を讀込む。
    env = Environment(loader=FileSystemLoader('.', encoding='utf-8'))
    template = env.get_template(temp)

    # 設定書類を讀込む。
    with open(param) as fpr:
        params = json.load(fpr)

    # レンダリングしてhtml出力する。
    rendered = template.render(params)
    with open(html, 'w') as fpw:
        fpw.write(rendered)
# End of def mk_html(param, temp, html='result.html', vbs=False):


def main():
    """主函數."""
    param = 'phtml.json'
    tmpfile = 'html.j2'
    htmlfile = 'result.html'
    args = docopt(__doc__)
    if args['--test']:
        doctest.testmod(verbose=args['--verbose'])
        sys.exit()
    if args['--version']:
        sys.exit(f'Ver: {__version__}')
    if args['--file']:
        tmpfile = args['--file']
    if args['--param']:
        param = args['--param']
    if args['--output']:
        htmlfile = args['--output']
    if args['--verbose']:
        print('[*] basis.py')
        print(f'\tTemplate file: {tmpfile:s}')
        print(f'\tParameter file: {param:s}')
        print(f'\tHTML file: {htmlfile:s}')

    mk_html(param, tmpfile, htmlfile, args['--verbose'])
# End of def main():


if __name__ == '__main__':
    main()
