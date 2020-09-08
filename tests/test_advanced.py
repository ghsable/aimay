# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_get_replymessage(self):
    reply_message = aimay.get_replymessage('おうむ返し')
    self.assertEqual(('おうむ返しニャン', 'text', '', ''), reply_message)
    reply_message = aimay.get_replymessage('ちゅーる')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    #self.assertIsNotNone(reply_message[2])
    #self.assertIsNotNone(reply_message[3])

if __name__ == "__main__":
    unittest.main()
