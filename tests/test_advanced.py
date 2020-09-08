# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_get_replymessage(self):
    reply_message = aimay.get_replymessage('おうむ返し')
    self.assertEqual(('おうむ返しニャン', 'text', None, None), reply_message)

    reply_message = aimay.get_replymessage('ちゅーる')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('りんりん')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('おんがく')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('えいが')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('どらま')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('げーむ')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('てんき')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('おやすみ')
    self.assertIsNone(reply_message[0])
    self.assertEqual('sticker', reply_message[1])
    self.assertIsNotNone(reply_message[2])
    self.assertIsNotNone(reply_message[3])

    reply_message = aimay.get_replymessage('あ')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

if __name__ == "__main__":
    unittest.main()
