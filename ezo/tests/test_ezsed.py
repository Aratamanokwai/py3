#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 履歴情報:
# Ver.0.3
"""標本算譜試驗."""

import unittest
from ezo import ezsed


class TestSed(unittest.TestCase):
    """ストリーム・エディタ類型試驗."""

    def setUp(self):
        """前處理."""
        self.sed = ezsed.Sed.factory('no melon, no lemon.')
    # End of def setUp(self):

#    def tearDown(self):
#        """後處理."""
#        super().tearDown()
#    # End of def tearDown(self):

    def test_get_data_00(self):
        """正常系試驗."""
        self.assertEqual('no melon, no lemon.', self.sed.get_data())
    # End of def test_get_data_00(self):

    def test_mk_dict_00(self):
        """正常系試驗."""
        self.assertEqual({'a': 'A', 'b': 'B'},
                         self.sed.mk_dict('ab', 'AB'))
    # End of def test_mk_dict_00(self):

    def test_mk_dict_01(self):
        """正常系試驗."""
        self.assertEqual({'a': 'A', 'b': 'B', 'c': 'C'},
                         self.sed.mk_dict('abc', 'ABC'))
    # End of def test_mk_dict_01(self):

    def test_y_command_00(self):
        """正常系試驗."""
        self.sed.y_command({'n': 'N', 'm': 'M'})
        self.assertEqual('No MeloN, No leMoN.', self.sed.get_data())
    # End of def test_y_command_00(self):

    def test_s_command_00(self):
        """正常系試驗."""
        self.sed.s_command('no', 'yes')
        self.assertEqual('yes melon, yes lemon.', self.sed.get_data())
    # End of def test_s_command_00(self):

    def test_s_command_01(self):
        """正常系試驗."""
        self.sed.s_command('no', 'yes', 1)
        self.assertEqual('yes melon, no lemon.', self.sed.get_data())
    # End of def test_s_command_01(self):

    def test_s_command_02(self):
        """正常系試驗."""
        self.sed = ezsed.Sed.factory('')
        self.sed.s_command('no', 'yes')
        self.assertEqual('', self.sed.get_data())
    # End of def test_s_command_02(self):

    def test_s_commannd_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.s_command(5, 'yes', 1)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <oldstr> must be a string.')
    # End of def test_s_commannd_badargs_01(self):

    def test_s_commannd_badargs_02(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.s_command('no', 5, 1)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <newstr> must be a string.')
    # End of def test_s_commannd_badargs_02(self):

    def test_s_commannd_badargs_03(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.s_command('no', 'yes', [])
        self.assertEqual(
            cmv.exception.args[0], '[!!] <cnt> must be an integer.')
    # End of def test_s_commannd_badargs_03(self):

    def test_s_commannd_badargs_04(self):
        """異常系試驗."""
        with self.assertRaises(ValueError) as cmv:
            self.sed.s_command('no', 'yes', -6)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <cnt> must be not negative.')
    # End of def test_s_commannd_badargs_04(self):

    def test_y_commannd_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.y_command(34)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <dic> must be a dictionary.')
    # End of def test_y_commannd_badargs_01(self):

    def test_y_commannd_badargs_02(self):
        """異常系試驗."""
        with self.assertRaises(ValueError) as cmv:
            self.sed.y_command({})
        self.assertEqual(
            cmv.exception.args[0], '[!!] <dic> must be not empty.')
    # End of def test_y_commannd_badargs_02(self):

    def test_mk_dict_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.mk_dict([], 'ABC')
        self.assertEqual(
            cmv.exception.args[0], '[!!] <keys> must be a string.')
    # End of def test_mk_dict_badargs_01(self):

    def test_mk_dict_badargs_02(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            self.sed.mk_dict('abc', {})
        self.assertEqual(
            cmv.exception.args[0], '[!!] <vals> must be a string.')
    # End of def test_mk_dict_badargs_02(self):

    def test_mk_dict_badargs_03(self):
        """異常系試驗."""
        with self.assertRaises(ValueError) as cmv:
            self.sed.mk_dict('abc', 'AB')
        self.assertEqual(
            cmv.exception.args[0], '[!!] <keys> are too many.')
    # End of def test_mk_dict_badargs_03(self):

    def test_mk_dict_badargs_04(self):
        """異常系試驗."""
        with self.assertRaises(ValueError) as cmv:
            self.sed.mk_dict('', 'AB')
        self.assertEqual(
            cmv.exception.args[0], '[!!] <keys> must be not empty.')
    # End of def test_mk_dict_badargs_04(self):

    def __repr__(self):
        """Show representation."""
        return f'class {self.__class__.__name__}.'
    # End of def __repr__(self):
# End of class TestSed(unittest.TestCase):


class TestEzSed(unittest.TestCase):
    """ストリーム・エディタ試驗."""

    def test_analyze_script_00(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.analyze_script('y/nm/NM/'),
                ['y', 'nm', 'NM', ''])
    # End of def test_analyze_script_00(self):

    def test_analyze_script_01(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.analyze_script('y/nm/NM/g'),
                ['y', 'nm', 'NM', 'g'])
    # End of def test_analyze_script_01(self):

    def test_analyze_script_02(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.analyze_script('s/nm/NM/'),
                ['s', 'nm', 'NM', ''])
    # End of def test_analyze_script_02(self):

    def test_del_comment_00(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.del_comment('abgfd'),
                'abgfd')
    # End of def test_del_comment_00(self):

    def test_del_comment_01(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.del_comment('  abgfd   '),
                'abgfd')
    # End of def test_del_comment_01(self):

    def test_del_comment_02(self):
        """正常系試驗."""
        self.assertEqual(
                ezsed.del_comment('#abgfd'),
                '')
    # End of def test_del_comment_02(self):

    def test_del_comment_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(AssertionError) as cmv:
            ezsed.del_comment(5)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <script> must be a string.')
    # End of def test_del_comment_badargs_01(self):

    def test_analyze_script_badargs_01(self):
        """異常系試驗."""
        with self.assertRaises(TypeError) as cmv:
            ezsed.analyze_script(5)
        self.assertEqual(
            cmv.exception.args[0], '[!!] <script> must be a string.')
    # End of def test_analyze_script_badargs_01(self):

    def test_analyze_script_badargs_02(self):
        """異常系試驗."""
        with self.assertRaises(AssertionError) as cmv:
            ezsed.analyze_script('', [])
        self.assertEqual(
            cmv.exception.args[0], '[!!] <vbs> must be boolean.')
    # End of def test_analyze_script_badargs_02(self):
# End of class TestEzSed(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
