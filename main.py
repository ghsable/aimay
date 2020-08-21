from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)

app = Flask(__name__)

import os     # Heroku
import random # GitHub
import pya3rt # A3RT/TalkAPI:requirements.txt

# get environment variables from Heroku(Settings/Config Variables)
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
A3RT_APIKEY = os.environ["A3RT_APIKEY"] # A3RT/TalkAPI

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
    # get reply message
    reply_text = get_replytext(push_text)
    # reply
    line_bot_api.reply_message(
        event.reply_token,
        # parrot
        #TextSendMessage(text=event.message.text)
        # A3RT/TalkAPI
        TextSendMessage(text=reply_text)
    )

# return reply message
def get_replytext(text):
    if ('おうむ' in text) or ('オウム' in text) or ('鸚鵡' in text):
        reply_text = text
    elif ('ちゅーる' in text) or ('チュール' in text) or ('飲' in text) or ('食' in text):
        ciao_path = os.getcwd() + '/data/CIAO.txt'
        with open(ciao_path) as f:
            s = f.readlines()
        reply_text = s[random.randint(0,(len(s) - 1))].strip()
    elif ('音楽' in text) or ('music' in text) or ('Music' in text) or ('歌' in text) or ('曲' in text)
        music_path = os.getcwd() + '/data/MUSIC.txt'
        with open(music_path) as f:
            s = f.readlines()
        reply_text = s[random.randint(0,(len(s) - 1))].strip()
    else:
        # get reply messgage(A3RT/TalkAPI)
        reply_text = talkapi_response(text) + 'ニャン'
    return reply_text

# return reply message(A3RT/TalkAPI)
def talkapi_response(text):
    apikey = A3RT_APIKEY
    client = pya3rt.TalkClient(apikey)
    response = client.talk(text)
    return ((response['results'])[0])['reply']

if __name__ == "__main__":
   # get port from Heroku
   port = int(os.getenv("PORT"))
   app.run(host="0.0.0.0", port=port)
