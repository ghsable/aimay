# -*- coding: utf-8 -*-
from . import helpers

def get_reply(push_type, push_text):
    """Get reply information.

    :param push_type: push message type
    :type push_type: str
    :param push_text: push message text
    :type push_text: str
    :returns: reply_type, reply_text, reply_package, reply_sticker
    :rtype: str
    """
    reply_type, reply_text, reply_package, reply_sticker = None, None, None, None
    if (push_type == 'text'):
        if ('おうむ' in push_text) or ('オウム' in push_text) or ('鸚鵡' in push_text) or ('🦜' in push_text):
            reply_type = 'text'
            reply_text = push_text + 'ニャン'
        elif ('ちゅーる' in push_text) or ('チュール' in push_text) or ('飲' in push_text) or ('食' in push_text):
            reply_type = 'text'
            reply_text = helpers.return_data('CIAO.txt')
        elif ('りんりん' in push_text) or ('りんちゃん' in push_text) or ('りんたろう' in push_text) or ('凛太郎' in push_text):
            reply_type = 'text'
            reply_text = helpers.return_data('RIN.txt')
        elif ('おんがく' in push_text) or ('うた' in push_text) or ('きょく' in push_text) or ('音' in push_text) or ('歌' in push_text) or ('曲' in push_text):
            reply_type = 'text'
            reply_text = 'これを聴いているニャン\n' + helpers.return_data('MUSIC.txt')
        elif ('えいが' in push_text) or ('映画' in push_text):
            reply_type = 'text'
            reply_text = 'これを観ているニャン\n' + helpers.return_data('MOVIE.txt')
#        elif ('にゅーす' in push_text) or ('ニュース' in push_text):
#            reply_type = 'text'
#            reply_text = 'これを読んでいるニャン\n' + helpers.newsapi_response()
        elif ('どらま' in push_text) or ('ドラマ' in push_text):
            reply_type = 'text'
            reply_text = 'ここを見ているニャン\n' + 'https://filmarks.com/list-drama/trend\n' + 'https://www.themoviedb.org/tv?language=ja'
        elif ('げーむ' in push_text) or ('ゲーム' in push_text):
            reply_type = 'text'
            reply_text = 'ここを見ているニャン\n' + 'https://www.metacritic.com/game'
        elif ('てんき' in push_text) or ('きおん' in push_text) or ('天気' in push_text) or ('気温' in push_text) or ('降水' in push_text):
            reply_type = 'text'
            reply_text = 'ここを見ているニャン\n' + 'https://www.google.co.jp/search?q=天気'
        elif ('おやすみ' in push_text):
            reply_type = 'sticker'
            reply_package, reply_sticker = helpers.return_sticker('sleep')
        elif ('debug_sticker' in push_text):
            reply_type = 'sticker'
            reply_package, reply_sticker = helpers.return_sticker(push_text)
        elif ('debug_message' in push_text):
            reply_type = push_text
        else:
            reply_type = 'text'
            reply_text = helpers.talkapi_response(push_text) + 'ニャン'
    elif (push_type == 'sticker'):
        reply_type = 'sticker'
        reply_package, reply_sticker = helpers.return_sticker('variety')
    else:
        reply_type = 'text'
        reply_text = 'よくわかりませんニャン'
    return reply_type, reply_text, reply_package, reply_sticker
