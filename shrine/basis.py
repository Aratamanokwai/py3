#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""神社２の基本的な使い方.

usage: basis.py [-h] [-v] [-t]

options:
    -h, --help      show this help message and exit
    -v, --verbose   verbose
    -t, --test      doctest

The require modules:
（標準品以外の必要なもの）
    docopt
    jinja2
"""

import doctest
import sys
try:
    from docopt import docopt
    from jinja2 import Template
except ModuleNotFoundError:
    print('[!!] Please install the required modules.', file=sys.stderr)
    sys.exit(__doc__)
# End of except ModuleNotFoundError:


def main():
    """主函數.

    >>> import basis
    """
    args = docopt(__doc__)
    if args['--test']:
        doctest.testmod(verbose=args['--verbose'])
        sys.exit()
    if args['--verbose']:
        print('[*] basis.py')

    tpl_text = '僕の名前は{{ name }}です！！{{ lang }}が好きです！！'
    template = Template(tpl_text)

    data = {'name': 'Kuro', 'lang': 'Python'}
    # 辞書で指定する
    disp_text = template.render(data)
    # 僕の名前はKuroです！！Pythonが好きです！
    print(disp_text)
# End of def main():


if __name__ == '__main__':
    main()
