from settings.logs import *
from tools.string_processing import wiki_string
from tools.browser.search import search_google

try :
    import wikipedia
except Exception as e:
    logger.inf(str(e))

def wiki_search(msg, no = 2) :
    """ This function will search through wikipedia and will reply information
        Written by Saurav Paul.
    """
    logger.info('Searching to wikipedia.') 
    print('(Thinking...)')
    # msg = wiki_string(msg)
    logger.info('after processing the string is : ' + msg)
    try :
        results = wikipedia.summary(msg,sentences=no)
        return results
    except :
        logger.info("Haven't found anything relevant in wikipedia")
        search_google(msg)
        return "I don't know sir, but I can show you ,check browser."

