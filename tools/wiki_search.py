import wikipedia
from settings.logs import *
from tools.string_processing import wiki_string
from tools.browser.search import search_google
def wiki_search(msg, lim = 1) :
    """ This function will search through wikipedia and will reply information
        Written by Saurav Paul.
    """
    logger.info('Searching to wikipedia.') 
    print('(Thinking...)')
    msg = wiki_string(msg)
    logger.info('after processing the string is : ' + msg)
    try :
        results = wikipedia.page(msg).content.split(sep='.')
        msg = ""
        i = 0
        for line in results :
            if i == lim :
                break
            msg += line +'. '
            i += 1
        return msg 
    except :
        logger.info("Haven't found anything relevant in wikipedia")
        search_google(msg)
        return "I don't know sir, but I can show you ,check browser."

