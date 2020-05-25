
from tools.assistant import ask_question
from tools.AI.data import data , youtube , wiki , google , youtube_play , goto_keys , install_keys
from tools.wiki_search import wiki_search
from settings.logs import *
from tools.browser.search import *
from tools.browser.goto import find_goto_address
from system.install import install

def check(msg,mp):
    logger.info('check->' + msg)
    for word in mp :
        if word in msg:
            return True
    return False


def rep(msg,mp):
    for word in mp :
        if word in msg:
            return msg.replace(word,'').strip().capitalize()
    return msg.strip().capitalize()

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
        logger.info('Not found in common data')
        if check(msg,youtube_play):
            msg = rep(msg,youtube_play)
            logger.info(msg)
            find_goto_address(msg)
            reply = 'Enjoy sir. :D'
        elif check(msg,goto_keys):
            msg = rep(msg,goto_keys)
            find_goto_address(msg)
            reply = 'check browser'
        elif check(msg,youtube):
            msg = rep(msg,youtube)
            search_youtube(msg)
            reply = 'check browser.'
        elif check(msg,wiki):
            msg = rep(msg,wiki)
            search_wiki(msg)
            reply = 'check browser.'
        elif check(msg,google):
            msg = rep(msg,google)
            search_google(msg)
            reply = 'check browser.'
        elif check(msg,install_keys):
            msg = rep(msg,install_keys)
            reply = install(msg)
        else :
            reply = ask_question(msg)
        return reply
    except :
        logger.info('Getting some error in ai')
        return reply

