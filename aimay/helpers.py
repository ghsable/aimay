# -*- coding: utf-8 -*-

# return reply message(from data/*.txt)
import os
import random
def return_data(filename):
    filepath = os.path.join(os.getcwd(), 'aimay/data', filename)
    with open(filepath) as datafile:
        datalines = datafile.readlines()
    return datalines[random.randint(0,(len(datalines) - 1))].strip()

# return reply message(A3RT/TalkAPI)
import pya3rt
def talkapi_response(push_text):
    talkapi_client   = pya3rt.TalkClient(os.environ.get('A3RT_TALKAPI_APIKEY'))
    talkapi_response = talkapi_client.talk(push_text)
    return ((talkapi_response['results'])[0])['reply']

