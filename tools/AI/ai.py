
from tools.assistant import ask_question
from tools.AI.data import data
from tools.wiki_search import wiki_search
from settings.logs import *

def ai(msg) :
    """ Little ai for reacting to the msg .
        Written by Saurav-Paul"""
    
    logger.info('Processing with ai')
    reply = "I don't know what to do, sir ."
    try :
        for line in data :
            if line.find(msg) != -1:
                reply = data[line]
                return reply
        if 'wiki' in msg:
            reply = wiki_search(msg)
        else :
            reply = ask_question(msg)
        
        return reply
    except :
        return reply

