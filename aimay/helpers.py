# -*- coding: utf-8 -*-

# return reply message(from data/*.txt)
import os
import random
def return_data(filename):
    filepath = os.path.join(os.getcwd(), 'aimay/data', filename)
    with open(filepath) as datafile:
        datalines = datafile.readlines()
    return datalines[random.randint(0,(len(datalines) - 1))].strip()

# return reply sticker
#  - LINE Available sticker list
#    https://developers.line.biz/media/messaging-api/sticker_list.pdf
def return_sticker(index):
    # sleep
    if (index == 0):
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
    # variety
    elif (index == 1):
        reply_package = '11537'
        reply_sticker = '52002735'
    # other
    else:
        reply_package = '11537'
        reply_sticker = '52002734'
    return reply_package reply_sticker

# return reply message(A3RT/TalkAPI)
import pya3rt
def talkapi_response(push_text):
    talkapi_client = pya3rt.TalkClient(os.environ.get('A3RT_TALKAPI_APIKEY'))
    talkapi_response = talkapi_client.talk(push_text)
    return ((talkapi_response['results'])[0])['reply']

