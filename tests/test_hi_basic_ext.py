#!/usr/bin/env python3
import unittest
import sys
import os
if "hi_basic_ext" not in sys.modules:
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    from hi_basic_ext import *


class TestHibasicext(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        return super().tearDown()

    def test_sample(self):
        pass

    pass


if __name__ == "__main__":
    unittest.main()
    pass
