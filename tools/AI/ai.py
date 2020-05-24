
from tools.assistant import ask_question
from tools.AI.data import data
from tools.wiki_search import wiki_search
from settings.logs import *
from tools.browser.search import *

def ai(msg) :
    """ Little ai for reacting to the msg .
        Written by Saurav-Paul"""
    
    logger.info('Processing with ai')
    reply = "I don't know what to do, sir ."
    try :
        for line in data :
            if msg.find(line) != -1:
                reply = data[line]
                return reply
        logger.info('not found in data')
        if 'wiki' in msg or 'wikipedia' in msg:
            reply = wiki_search(msg,2)
        else :
            reply = ask_question(msg)
        
        return reply
    except :
        return reply

