# -*- coding: utf-8 -*-

from . import helpers

# return reply message and type and index
import random
def get_replymessage(push_text):

    reply_text, reply_type, reply_package, reply_sticker = '', '', '', ''
    suffix = 'ニャン'

    if ('おうむ' in push_text) or ('オウム' in push_text) or ('鸚鵡' in push_text) or ('🦜' in push_text):
        #reply_text = push_text + 'ニャン'
        reply_text = ''.join(push_text, suffix)
        reply_type = 'text'
    elif ('ちゅーる' in push_text) or ('チュール' in push_text) or ('飲' in push_text) or ('食' in push_text):
        reply_text = helpers.return_data('CIAO.txt')
        reply_type = 'text'
    elif ('りんりん' in push_text) or ('りんちゃん' in push_text) or ('りんたろう' in push_text) or ('凛太郎' in push_text):
        reply_text = helpers.return_data('RIN.txt')
        reply_type = 'text'
    elif ('おんがく' in push_text) or ('うた' in push_text) or ('きょく' in push_text) or ('音' in push_text) or ('歌' in push_text) or ('曲' in push_text):
        reply_text = 'これを聴いているニャン\n' + helpers.return_data('MUSIC.txt')
        reply_type = 'text'
    # Filmarks
    elif ('えいが' in push_text) or ('映画' in push_text):
        reply_text = 'これを観ているニャン\n' + helpers.return_data('MOVIE.txt')
        reply_type = 'text'
    elif ('どらま' in push_text) or ('ドラマ' in push_text):
        reply_text = 'ここを見ているニャン\n' + 'https://filmarks.com/list-drama/trend\n' + 'https://www.themoviedb.org/tv?language=ja'
        reply_type = 'text'
    elif ('げーむ' in push_text) or ('ゲーム' in push_text):
        reply_text = 'ここを見ているニャン\n' + 'https://www.metacritic.com/game'
        reply_type = 'text'
    elif ('てんき' in push_text) or ('きおん' in push_text) or ('天気' in push_text) or ('気温' in push_text) or ('降水' in push_text):
        reply_text = 'ここを見ているニャン\n' + 'https://www.google.co.jp/search?q=天気'
        reply_type = 'text'
    elif ('おやすみ' in push_text):
        reply_type     = 'sticker'
        sticker_switch = random.randint(0,2)
        # ----- LINE Available sticker list
        #       https://developers.line.biz/media/messaging-api/sticker_list.pdf
        # Brown, Cony & Sally
        if (sticker_switch == 0):
            reply_package = '11537'
            reply_sticker = random.choice(['52002753', '52002757', '52002764', '52002771'])
        # CHOCO & Friends
        elif (sticker_switch == 1):
            reply_package = '11538'
            reply_sticker = random.choice(['51626513'])
        # UNIVERSTAR BT21
        else:
            reply_package = '11539'
            reply_sticker = random.choice(['52114120', '52114121'])
        # -----
    # A3RT/TalkAPI
    else:
        reply_text = helpers.talkapi_response(push_text) + 'ニャン'
        reply_type = 'text'
    return reply_text, reply_type, reply_package, reply_sticker
