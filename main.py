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

import os       # Heroku
import requests # A3RT/TalkAPI
import pprint   # A3RT/TalkAPI
import pya3rt   # A3RT/TalkAPI

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
    # get reply messgage(A3RT/TalkAPI)
    reply_text = talkapi_response(push_text) + 'ニャン'
    # reply
    line_bot_api.reply_message(
        event.reply_token,
        # parrot
        #TextSendMessage(text=event.message.text)
        # A3RT/TalkAPI
        TextSendMessage(text=reply_text)
    )

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
