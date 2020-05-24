import wikipedia
from settings.logs import *

def wiki_search(msg) :
    """ This function will search through wikipedia and will reply information
        Written by Saurav Paul.
    """
    logger.info('Searching to wikipedia.') 
    print('(Thinking...)')   
    try :
        results = wikipedia.page(msg).content.split(sep='.')
        msg = ""
        i = 0
        for line in results :
            if i == 1 :
                break
            msg += line
            i += 1
        return msg 
    except :
        logger.info("Haven't found anything relevant in wikipedia")
        return "Sorry sir, i don't know about " + msg

