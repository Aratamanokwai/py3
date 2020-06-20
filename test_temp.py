#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.0   雛型
# Ver.0.1   試作
"""標本算譜試驗."""

import unittest
import temp


class TestTemp(unittest.TestCase):
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

    def test_run_00(self):
        """正常系試驗."""
        self.assertEqual(None, temp.run())
    # End of def test_temp(self):

    def test_run_badargs_00(self):
        """異常系試驗."""
        with self.assertRaises(AssertionError) as cmv:
            temp.run(3.141592)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <vbs> must be boolean.')
        # cmv: comtext manager variale
    # End of def test_run_badargs_00(self):

    def __repr__(self):
        """Show representation."""
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class TestTemp(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
