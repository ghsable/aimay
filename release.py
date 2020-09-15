# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, FollowEvent, 
    TextMessage, StickerMessage, ImageMessage, AudioMessage, 
    TextSendMessage, StickerSendMessage, ImageSendMessage
)

app = Flask(__name__)

# get environment variables from Heroku(Settings/Config Variables)
import os
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    push_type = 'text'
    push_text = event.message.text
    # get reply information
    reply_type, reply_text, reply_package, reply_sticker = get_reply(push_type, push_text)
    # reply
    if (reply_type == 'text'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
    elif (reply_type == 'sticker'):
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(package_id=reply_package,sticker_id=reply_sticker))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='error'))

@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
    push_type = 'sticker'
    push_text = None
    reply_type, reply_text, reply_package, reply_sticker = get_reply(push_type, push_text)
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id=reply_package,sticker_id=reply_sticker))

@handler.add(MessageEvent, message=(ImageMessage, AudioMessage))
def handle_message(event):
    push_type = 'media'
    push_text = None
    reply_type, reply_text, reply_package, reply_sticker = get_reply(push_type, push_text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text))

@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='友達追加ありがとうございますニャン'))

if __name__ == "__main__":
   # get port from Heroku
   port = int(os.environ.get('PORT'))
   app.run(host="0.0.0.0", port=port)

import random
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
            reply_text = return_data('CIAO.txt')
        elif ('りんりん' in push_text) or ('りんちゃん' in push_text) or ('りんたろう' in push_text) or ('凛太郎' in push_text):
            reply_type = 'text'
            reply_text = return_data('RIN.txt')
        elif ('おんがく' in push_text) or ('うた' in push_text) or ('きょく' in push_text) or ('音' in push_text) or ('歌' in push_text) or ('曲' in push_text):
            reply_type = 'text'
            reply_text = 'これを聴いているニャン\n' + return_data('MUSIC.txt')
        elif ('えいが' in push_text) or ('映画' in push_text):
            reply_type = 'text'
            reply_text = 'これを観ているニャン\n' + return_data('MOVIE.txt')
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
            reply_package, reply_sticker = return_sticker('sleep')
        elif ('debug_sticker' in push_text):
            reply_type = 'sticker'
            reply_package, reply_sticker = return_sticker(push_text)
        elif ('debug_message' in push_text):
            reply_type = push_text
        else:
            reply_type = 'text'
            reply_text = talkapi_response(push_text) + 'ニャン'
    elif (push_type == 'sticker'):
        reply_type = 'sticker'
        reply_package, reply_sticker = return_sticker('variety')
    else:
        reply_type = 'text'
        reply_text = 'よくわかりませんニャン'
    return reply_type, reply_text, reply_package, reply_sticker

def return_data(filename):
    """Return reply message from data directory.

    :param filename: filename in data directory
    :type filename: str
    :returns: dataline
    :rtype: str
    """
    filepath = os.path.join(os.getcwd(), 'aimay/data', filename)
    with open(filepath) as datafile:
        datalines = datafile.readlines()
        dataline = datalines[random.randint(0,(len(datalines) - 1))].strip()
    return dataline

# LINE Available sticker list
# https://developers.line.biz/media/messaging-api/sticker_list.pdf
def return_sticker(index):
    """Return reply sticker.

    :param index: index of stickers
    :type index: str
    :returns: reply_package, reply_sticker
    :rtype: str
    """
    if (index == 'sleep'):
        sticker_switch = random.randint(0,2)
        if (sticker_switch == 0):
            # Brown, Cony & Sally
            reply_package = '11537'
            reply_sticker = random.choice(['52002753', '52002757', '52002764', '52002771'])
        elif (sticker_switch == 1):
            # CHOCO & Friends
            reply_package = '11538'
            reply_sticker = random.choice(['51626513'])
        else:
            # UNIVERSTAR BT21
            reply_package = '11539'
            reply_sticker = random.choice(['52114120', '52114121'])
    elif (index == 'variety'):
        sticker_switch = random.randint(0,2)
        if (sticker_switch == 0):
            # Brown, Cony & Sally
            reply_package = '11537'
            reply_sticker = random.choice(['52002734', '52002735', '52002736', '52002737', '52002738', '52002739', '52002740', '52002741', '52002742', '52002743', \
                                           '52002744', '52002745', '52002746', '52002747', '52002748', '52002749', '52002750', '52002751', '52002752', '52002753', \
                                           '52002754', '52002755', '52002756', '52002757', '52002758', '52002759', '52002760', '52002761', '52002762', '52002763', \
                                           '52002764', '52002765', '52002766', '52002767', '52002768', '52002769', '52002770', '52002771', '52002772', '52002773'])
        elif (sticker_switch == 1):
            # CHOCO & Friends
            reply_package = '11538'
            reply_sticker = random.choice(['51626494', '51626495', '51626496', '51626497', '51626498', '51626499', '51626500', '51626501', '51626502', '51626503', \
                                           '51626504', '51626505', '51626506', '51626507', '51626508', '51626509', '51626510', '51626511', '51626512', '51626513', \
                                           '51626514', '51626515', '51626516', '51626517', '51626518', '51626519', '51626520', '51626521', '51626522', '51626523', \
                                           '51626524', '51626525', '51626526', '51626527', '51626528', '51626529', '51626530', '51626531', '51626532', '51626533'])
        else:
            # UNIVERSTAR BT21
            reply_package = '11539'
            reply_sticker = random.choice(['52114110', '52114111', '52114112', '52114113', '52114114', '52114115', '52114116', '52114117', '52114118', '52114119', \
                                           '52114120', '52114121', '52114122', '52114123', '52114124', '52114125', '52114126', '52114127', '52114128', '52114129', \
                                           '52114130', '52114131', '52114132', '52114133', '52114134', '52114135', '52114136', '52114137', '52114138', '52114139', \
                                           '52114140', '52114141', '52114142', '52114143', '52114144', '52114145', '52114146', '52114147', '52114148', '52114149'])
    else:
        reply_package = '11537'
        reply_sticker = '52002734'
    return reply_package, reply_sticker

import pya3rt
def talkapi_response(push_text):
    """
    Return reply message from A3RT/TalkAPI.

    :param push_text: push message text
    :type push_text: str
    :returns: talkapi_reply
    :rtype: str
    """
    talkapi_client = pya3rt.TalkClient(os.environ.get('A3RT_TALKAPI_APIKEY'))
    talkapi_response = talkapi_client.talk(push_text)
    talkapi_reply = ((talkapi_response['results'])[0])['reply']
    return talkapi_reply
