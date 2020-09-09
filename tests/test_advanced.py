# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_get_replymessage(self):
    reply_message = aimay.get_replymessage('text', 'おうむがえし！')
    self.assertEqual(('text', 'おうむがえし！ニャン', None, None), reply_message)

    reply_message = aimay.get_replymessage('text', 'ちゅーるを買ったよ')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'りんりん(相棒)の調子はどう？')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'いい音楽ないかな')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', '映画を観たいな')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', '面白いドラマあるかな')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'ゲームをやろうかな')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', '天気どうなるかな')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    for i in range(10):
        reply_message = aimay.get_replymessage('text', 'おやすみー')
        self.assertEqual('sticker', reply_message[0])
        self.assertIsNone(reply_message[1])
        self.assertIsNotNone(reply_message[2])
        self.assertIsNotNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'debug_sticker')
    self.assertEqual('sticker', reply_message[0])
    self.assertIsNone(reply_message[1])
    self.assertIsNotNone(reply_message[2])
    self.assertIsNotNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'debug_message')
    self.assertIsNotNone(reply_message[0])
    self.assertIsNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('text', 'あれ')
    self.assertEqual('text', reply_message[0])
    self.assertIsNotNone(reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

if __name__ == "__main__":
    unittest.main()
