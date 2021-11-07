# -*- coding: utf-8 -*-

import os
import random
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
        dataline = datalines[random.randint(0, (len(datalines) - 1))].strip()
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
        sticker_switch = random.randint(0, 2)
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
        sticker_switch = random.randint(0, 2)
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

#from newsapi import NewsApiClient
#def newsapi_response():
#    """Return reply message from NewsAPI.
#
#    :returns: newsapi_reply
#    :rtype: str
#    """
#    # Top headlines - https://newsapi.org/docs/endpoints/top-headlines
#    newsapi = NewsApiClient(os.environ.get('NEWSAPI_APIKEY'))
#    headlines = newsapi.get_top_headlines(category='general', country='us')
#    newsapi_reply = '今日のニュースは無いですニャン'
#    if(headlines['totalResults'] > 0):
#        headlines_size = len(headlines['articles'])
#        i = random.randint(0, headlines_size - 1)
#        headline_title = headlines['articles'][i]['title']
#        headline_url = headlines['articles'][i]['url']
#        newsapi_reply = headline_title + ' - ' + headline_url
#    return newsapi_reply

import requests
def talkapi_response(push_text):
    """Return reply message from A3RT/TalkAPI.

    :param push_text: push message text
    :type push_text: str
    :returns: talkapi_reply
    :rtype: str
    """
    post_url = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
    post_data = {'apikey': os.environ.get('A3RT_TALKAPI_APIKEY'), 'query': push_text}
    talkapi_response = requests.post(post_url, post_data).json()
    talkapi_reply = ((talkapi_response['results'])[0])['reply']
    return talkapi_reply
