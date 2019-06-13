# -*- coding: utf-8 -*-
import json
import unittest
import tempfile
from buffalo.algo.als import ALS, AlsOption
from buffalo.misc import aux


class TestALS(unittest.TestCase):
    def test0_get_default_option(self):
        AlsOption().get_default_option()
        self.assertTrue(True)

    def test0_is_valid_option(self):
        opt = AlsOption().get_default_option()
        self.assertTrue(AlsOption().is_valid_option(opt))
        opt['save_best_only'] = 1
        self.assertRaises(RuntimeError, AlsOption().is_valid_option, opt)
        opt['save_best_only'] = False
        self.assertTrue(AlsOption().is_valid_option(opt))


if __name__ == '__main__':
    unittest.main()
