#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""算譜の説明.

usage: temp.py [-h] [-v] [-t] [--sum] N [N...]

options:
    -h, --help      show this help message and exit
    -v, --verbose   verbose
    -t, --test      doctest
    --sum           sum the integers (default: find the max)

The require modules:
（標準品以外の必要なもの）
    docopt
"""

import doctest
import sys
from docopt import docopt

EX_OK = 0


def main():
    """Do main function."""
    vbs = False
    args = docopt(__doc__)
    # print (args)
    if args['--verbose']:
        vbs = True
    if args['--test']:
        doctest.testmod(verbose=vbs)
        sys.exit(EX_OK)
    _ns = map(int, args["N"])
    if args["--sum"]:
        print(sum(_ns))
    else:
        print(max(_ns))
    # print(f'vbs: {vbs}')
# End of def main():


if __name__ == '__main__':
    main()
