# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_f(self):
    self.assertEqual(3, aimay.f())

  def test_get_replymessage(self):
    self.assertEqual(('おうむ返しニャン', 'text', '', ''), aimay.get_replymessage('おうむ返し'))

if __name__ == "__main__":
    unittest.main()
