# -*- coding: utf-8 -*-

from .context import aimay

import unittest

class TestCore(unittest.TestCase):

  def test_get_reply(self):
    reply = aimay.get_reply('text', 'おうむがえし！')
    self.assertEqual('text', reply[0])
    self.assertEqual('おうむがえし！ニャン', reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', 'ちゅーるを買ったよ')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', 'りんりん(相棒)の調子はどう？')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', 'いい音楽ないかな')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', '映画を観たいな')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', '面白いドラマあるかな')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', 'ゲームをやろうかな')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', '天気どうなるかな')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    for i in range(10):
        reply = aimay.get_reply('text', 'おやすみー')
        self.assertEqual('sticker', reply[0])
        self.assertIsNone(reply[1])
        self.assertIsNotNone(reply[2])
        self.assertIsNotNone(reply[3])

    reply = aimay.get_reply('text', 'debug_sticker')
    self.assertEqual('sticker', reply[0])
    self.assertIsNone(reply[1])
    self.assertIsNotNone(reply[2])
    self.assertIsNotNone(reply[3])

    reply = aimay.get_reply('text', 'debug_message')
    self.assertIsNotNone(reply[0])
    self.assertIsNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

    reply = aimay.get_reply('text', 'あれ')
    self.assertEqual('text', reply[0])
    self.assertIsNotNone(reply[1])
    self.assertIsNone(reply[2])
    self.assertIsNone(reply[3])

if __name__ == "__main__":
    unittest.main()
