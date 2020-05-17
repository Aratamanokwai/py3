#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""算譜の説明.

usage: temp.py [-h] [-V] [-v] [-t] [--sum] N [N...]

options:
    -h, --help      show this help message and exit.
    -V, --version   show version info and exit.
    -v, --verbose   verbose
    -t, --test      doctest
    --sum           sum the integers (default: find the max)

The require modules:
（標準品以外の必要なもの）
    docopt

履歴情報:
Ver.0.0   雛型
Ver.0.1   試作
"""

__version__ = '0.0'

import doctest
import sys
try:
    from docopt import docopt
except ModuleNotFoundError:
    sys.exit(__doc__)


class Car(object):
    """車輛.

    Attributes:
        color (str):    色

    >>> Car()
    class Car.
    """

    def __init__(self, color='red'):
        """Iniitialize Car."""
        self.color = color
    # End of def __init__(self, color, mileage):

    def __repr__(self):
        """Shoe representation.

        >>> car = Car()
        >>> repr(car)
        'class Car.'
        """
        return f'class {__class__.__name__}.'
    # End of def __repr__(self):
# End of class Car(object):


def main():
    """Do main function.

    >>> import temp
    """
    args = docopt(__doc__)
    if args['--test']:
        doctest.testmod(verbose=args['--verbose'])
        sys.exit()

    if args['--version']:
        print('Ver: {}'.format(__version__))
        sys.exit()

    if args['--verbose']:
        print('[*] temp.py')

    nums = map(int, args["N"])
    if args["--sum"]:
        print(sum(nums))
    else:
        print(max(nums))
# End of def main():


if __name__ == '__main__':
    main()
