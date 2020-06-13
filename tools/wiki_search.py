from settings.logs import *
from tools.string_processing import wiki_string
from tools.browser.search import search_google
from tools.browser.goto import find_address
from termcolor import cprint

try :
    import wikipedia
except Exception as e:
    logger.inf(str(e))

def make_wiki_key(msg):
    try :
        msg = 'en.wikipedia.org '+msg
        msg = find_address(msg)
        msg = msg.rsplit(sep='/',maxsplit=1)
        return msg[1]
    except:
        return msg

def wiki_search(msg, no = 2) :
    """ This function will search through wikipedia and will reply information
        Written by Saurav Paul.
    """
    logger.info('Searching to wikipedia.') 
    cprint('\t\t(Thinking)','yellow')
    rem = msg
    msg = wiki_string(msg.lower())
    msg = make_wiki_key(msg)
    logger.info('after processing the string is : ' + msg)
    try :
        results = wikipedia.summary(msg,sentences=no)
        return results
    except :
        logger.info("Haven't found anything relevant in wikipedia")
        search_google(rem)
        return "I don't know sir, but I can show you ,check browser."

