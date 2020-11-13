#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜.

>>> import pizza
"""

__prog__ = 'pizza.py'
__description__ = 'プログラムの説明'
__epilog__ = 'Python 3.7 以上で動作します。'
__version__ = '0.1'

import sys
import argparse
import doctest
import abc


class BasePizza(object, metaclass=abc.ABCMeta):

    default_ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """Returns the default ingredient List."""
        return cls.default_ingredients
    # End of def get_ingredients(cls):
# End of class BasePizza(object, metaclass=abc.ABCMeta):


class DietPizza(BasePizza):
    def get_ingredients(self):
        return ['Egg'] + super(DietPizza,self).get_ingredients()
    # End of def get_ingredients(self):
# End of class DietPizza(BasePizza):


class Pizza(object):
    """車輛.

    Attributes:
        color (str):    色

    >>> Pizza()
    class Pizza.
    """

    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius
    # End of def get_radius(cls):

    def __init__(self, size=0):
        """Iniitialize Pizza."""
        self.size = size
    # End of def __init__(self, size=0):

    @staticmethod
    def mix_ingredients(x, y):
        return x + y
    # End of def mix_ingredients(x, y):

    def get_size(self):
        return self.size
    # End of def get_size(self):

    def __repr__(self):
        """Show representation.

        >>> car = Pizza()
        >>> repr(car)
        'class Pizza.'
        """
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class Pizza:


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
        AssertionError
    """
    assert isinstance(vbs, bool), '[!!] <vbs> must be boolean.'

    if vbs:
        print('[*] Run:')

##    print(f'Pizza.get_size: {Pizza.get_size}')
##    print(f'Pizza(8).size: {Pizza(8).size}')
##    print(f'Pizza(3).get_size(): {Pizza(3).get_size()}')

    print(f'Pizza.get_radius: {Pizza.get_radius}')
    print(f'Pizza().get_radius: {Pizza().get_radius}')
    print(f'Pizza.get_radius is Pizza().get_radius: {Pizza.get_radius is Pizza().get_radius}')
    print(f'Pizza.get_radius(): {Pizza.get_radius()}')

    #print(f's')
# End of def run(vbs=False):


def main():
    """Do main function.

    >>> import pizza
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
