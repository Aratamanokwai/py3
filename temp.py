#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""算譜の説明

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

from sys import exit
from docopt import docopt

_vb = False
EX_OK = 0

if '__main__' == __name__:
    args = docopt (__doc__)
    #print (args)
    if args['--verbose']:
        _vb = True
    if args['--test']:
        import doctest
        doctest.testmod (verbose=_vb)
        exit (EX_OK)
    Ns = map (int, args["N"])
    if args["--sum"]:
        print (sum (Ns))
    else:
        print (max (Ns))
    print (f'vb: {_vb}')
