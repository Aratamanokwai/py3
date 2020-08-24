#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜試驗."""

import unittest
import use_if as ut


class TestUseIf(unittest.TestCase):
    """標本試驗."""

    def setUp(self):
        """前處理."""
        super().setUp()
        self.data = {'x': 0}
    # End of def setUp(self):

#    def tearDown(self):
#        """後處理."""
#        super().tearDown()
#    # End of def tearDown(self):

    def test_mk_txt_00(self):
        """正常系試驗."""
        self.assertEqual('x is zero.\n', ut.mk_txt(self.data, 'test01.tpl'))
    # End of def test_temp(self):

    def test_mk_txt_badargs_00(self):
        """異常系試驗."""
        with self.assertRaises(AssertionError) as cmv:
            ut.mk_txt(self.data, 'test.tpl01', 3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <vbs> must be boolean.')
    # End of def test_mk_txt_badargs_00(self):

    def test_mk_txt_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            ut.mk_txt([], 'test01.tpl', 3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <data> must be a dictionary.')
    # End of def test_mk_txt_badargs_01(self):

    def test_mk_txt_badargs_02(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            ut.mk_txt(self.data, 3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <temp> must be a string.')
    # End of def test_mk_txt_badargs_02(self):

    def __repr__(self):
        """Show representation."""
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class TestUseIf(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
