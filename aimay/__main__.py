# -*- coding: utf-8 -*-
# python -m
#from . import core
# uwsgi
import aimay

# line/line-bot-sdk-python
# https://github.com/line/line-bot-sdk-python
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
    reply_type, reply_text, reply_package, reply_sticker = core.get_reply(push_type, push_text)
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
    reply_type, reply_text, reply_package, reply_sticker = core.get_reply(push_type, push_text)
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id=reply_package,sticker_id=reply_sticker))

@handler.add(MessageEvent, message=(ImageMessage, AudioMessage))
def handle_message(event):
    push_type = 'media'
    push_text = None
    reply_type, reply_text, reply_package, reply_sticker = core.get_reply(push_type, push_text)
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
