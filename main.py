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

import os                         # Heroku
import random                     # GitHub
import pya3rt                     # A3RT/TalkAPI:requirements.txt
from tmdbv3api import TMDb, Movie # TMDb:requirements.txt

# get environment variables from Heroku(Settings/Config Variables)
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
A3RT_TALKAPI_APIKEY = os.environ["A3RT_TALKAPI_APIKEY"] # A3RT/TalkAPI
# TMDb
TMDB_API_KEY = os.environ["TMDB_API_KEY"]
tmdb = TMDb()
tmdb.api_key = TMDB_API_KEY
tmdb.language = 'ja'
tmdb.debug = True
movie = Movie()
popular = movie.popular()

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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

# return reply message and type
def get_replymessage(text):
    reply_text = ''
    reply_type = ''
    reply_package = ''
    reply_sticker = ''
    if ('おうむ' in text) or ('オウム' in text) or ('鸚鵡' in text) or ('🦜' in text):
        reply_text = text
        reply_type = 'text'
    elif ('ちゅーる' in text) or ('チュール' in text) or ('飲' in text) or ('食' in text):
        ciao_path = os.getcwd() + '/data/CIAO.txt'
        with open(ciao_path) as ciao_txt:
            ciao_lines = ciao_txt.readlines()
        reply_text = ciao_lines[random.randint(0,(len(ciao_lines) - 1))].strip()
        reply_type = 'text'
    elif ('おんがく' in text) or ('うた' in text) or ('きょく' in text) or ('みゅーじっく' in text) or ('音' in text) or ('歌' in text) or ('曲' in text) or ('Music' in text) or ('music' in text):
        music_path = os.getcwd() + '/data/MUSIC.txt'
        with open(music_path) as music_txt:
            music_lines = music_txt.readlines()
        reply_text = 'これを聴いてるニャン\n' + music_lines[random.randint(0,(len(music_lines) - 1))].strip()
        reply_type = 'text'
    # TMDb
    elif ('映画' in text):
        populars = ''
        for p in popular:
            populars += p.title + '\n'
        reply_text = '最近のトレンドだニャン\n\n' + populars
        reply_type = 'text'
    elif ('てんき' in text) or ('きおん' in text) or ('天気' in text) or ('気温' in text) or ('降水' in text):
        reply_text = 'ここを見ているニャン\n' + 'https://www.google.co.jp/search?q=天気'
        reply_type = 'text'
    elif ('おやすみ' in text):
        reply_type = 'sticker'
        s = random.randint(0,2)
        # ----- LINE Available sticker list
        #       https://developers.line.biz/media/messaging-api/sticker_list.pdf
        # Brown, Cony & Sally
        if (s == 0):
            reply_package = '11537'
            reply_sticker = random.choice(['52002753', '52002757', '52002764', '52002771'])
        # CHOCO & Friends
        elif (s == 1):
            reply_package = '11538'
            reply_sticker = random.choice(['51626513', '51626533'])
        # UNIVERSTAR BT21
        else:
            reply_package = '11539'
            reply_sticker = random.choice(['52114110', '52114120', '52114121', '52114128'])
        # -----
    else:
        # get reply messgage(A3RT/TalkAPI)
        reply_text = talkapi_response(text) + 'ニャン'
        reply_type = 'text'
    return reply_text, reply_type, reply_package, reply_sticker

# return reply message(A3RT/TalkAPI)
def talkapi_response(text):
    apikey = A3RT_TALKAPI_APIKEY
    client = pya3rt.TalkClient(apikey)
    response = client.talk(text)
    return ((response['results'])[0])['reply']

if __name__ == "__main__":
   # get port from Heroku
   port = int(os.getenv("PORT"))
   app.run(host="0.0.0.0", port=port)
