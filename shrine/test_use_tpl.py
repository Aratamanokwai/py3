#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜試驗."""

import unittest
import use_tpl as ut


class TestUseTpl(unittest.TestCase):
    """標本試驗."""

#    def setUp(self):
#        """前處理."""
#        super().setUp()
#    # End of def setUp(self):
#
#    def tearDown(self):
#        """後處理."""
#        super().tearDown()
#    # End of def tearDown(self):

    def test_mk_txt_00(self):
        """正常系試驗."""
        self.assertEqual('Hello Kurau!', ut.mk_txt('test.tpl'))
    # End of def test_temp(self):

    def test_mk_txt_badargs_00(self):
        """異常系試驗."""
        with self.assertRaises(AssertionError) as cmv:
            ut.mk_txt('test.tpl', 3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <vbs> must be boolean.')
    # End of def test_mk_txt_badargs_00(self):

    def test_mk_txt_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            ut.mk_txt(3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <temp> must be a string.')
    # End of def test_mk_txt_badargs_01(self):

    def __repr__(self):
        """Show representation."""
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class TestUseTpl(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
