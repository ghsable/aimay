# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_get_replymessage(self):
    reply_message = aimay.get_replymessage('おうむがえし！')
    self.assertEqual(('おうむがえし！ニャン', 'text', None, None), reply_message)

    reply_message = aimay.get_replymessage('ちゅーるを買ったよ')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('りんりん(相棒)の調子はどう？')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('いい音楽ないかな')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('映画を観たいな')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('面白いドラマあるかな')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('ゲームをやろうかな')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    reply_message = aimay.get_replymessage('天気どうなるかな')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

    for i in range(5):
        reply_message = aimay.get_replymessage('おやすみー')
        self.assertIsNone(reply_message[0])
        self.assertEqual('sticker', reply_message[1])
        self.assertIsNotNone(reply_message[2])
        self.assertIsNotNone(reply_message[3])

    reply_message = aimay.get_replymessage('あれ')
    self.assertIsNotNone(reply_message[0])
    self.assertEqual('text', reply_message[1])
    self.assertIsNone(reply_message[2])
    self.assertIsNone(reply_message[3])

if __name__ == "__main__":
    unittest.main()
