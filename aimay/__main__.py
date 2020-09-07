from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, StickerMessage, StickerSendMessage, ImageMessage, ImageSendMessage
)

app = Flask(__name__)

import os      # Heroku
import random  # GitHub
import pya3rt  # A3RT/TalkAPI:requirements.txt

# get environment variables from Heroku(Settings/Config Variables)
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET       = os.environ["LINE_CHANNEL_SECRET"]
A3RT_TALKAPI_APIKEY       = os.environ["A3RT_TALKAPI_APIKEY"] # A3RT/TalkAPI

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(LINE_CHANNEL_SECRET)

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

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get push message
    push_text = event.message.text
    # get reply message and type
    reply_text, reply_type, reply_package, reply_sticker = get_replymessage(push_text)
    # reply
    if (reply_type == 'text'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text)
        )
    elif (reply_type == 'sticker'):
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(package_id=reply_package,sticker_id=reply_sticker)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='エラーみたいだニャン')
        )

# return reply message and type and index
def get_replymessage(push_text):
    reply_text     = ''
    reply_type     = ''
    reply_package  = ''
    reply_sticker  = ''
    if ('おうむ' in push_text) or ('オウム' in push_text) or ('鸚鵡' in push_text) or ('🦜' in push_text):
        reply_text = push_text + 'ニャン'
        reply_type = 'text'
    elif ('ちゅーる' in push_text) or ('チュール' in push_text) or ('飲' in push_text) or ('食' in push_text):
        reply_text = return_data('CIAO.txt')
        reply_type = 'text'
    elif ('りんりん' in push_text) or ('りんちゃん' in push_text) or ('りんたろう' in push_text) or ('凛太郎' in push_text):
        reply_text = return_data('RIN.txt')
        reply_type = 'text'
    elif ('おんがく' in push_text) or ('うた' in push_text) or ('きょく' in push_text) or ('音' in push_text) or ('歌' in push_text) or ('曲' in push_text):
        reply_text = 'これを聴いているニャン\n' + return_data('MUSIC.txt')
        reply_type = 'text'
    # Filmarks
    elif ('えいが' in push_text) or ('映画' in push_text):
        reply_text = 'これを観ているニャン\n' + return_data('MOVIE.txt')
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
        reply_text = talkapi_response(push_text) + 'ニャン'
        reply_type = 'text'
    return reply_text, reply_type, reply_package, reply_sticker

# return reply message(from data/*.txt)
def return_data(filename):
    #filepath = os.getcwd() + '/aimay/data/' + filename
    #filepath = os.path.join(os.getcwd(), 'aimay', 'data', filename)
    filepath = os.path.join(os.getcwd(), 'aimay/data', filename)
    with open(filepath) as datafile:
        datalines = datafile.readlines()
    return datalines[random.randint(0,(len(datalines) - 1))].strip()

# return reply message(A3RT/TalkAPI)
def talkapi_response(push_text):
    talkapi_client   = pya3rt.TalkClient(A3RT_TALKAPI_APIKEY)
    talkapi_response = talkapi_client.talk(push_text)
    return ((talkapi_response['results'])[0])['reply']

# test_main.py
def f():
    return 3

if __name__ == "__main__":
   # get port from Heroku
   port = int(os.getenv("PORT"))
   app.run(host="0.0.0.0", port=port)
