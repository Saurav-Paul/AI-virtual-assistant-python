from settings.logs import *
from tools.string_processing import wiki_string , is_matched
from tools.browser.search import search_google
from tools.browser.goto import find_address
from termcolor import cprint



def make_wiki_key(msg):
    try :
        msg = 'en.wikipedia.org '+msg
        msg = find_address(msg)
        msg = msg.rsplit(sep='/',maxsplit=1)
        return msg[1]
    except:
        return msg

def get_summary(msg , no):
    msg = msg.split(sep='.')
    ans = ''
    cnt = 0
    for i in msg:
        if cnt == no:
            break
        ans += i+'.'
        cnt += 1

    return ans

def wiki_summary(msg,no = 2):
    """ This function will reply the summary of the given text"""

    # print("wiki_summary")
    got_error = 'no data available'
    try :
        import wikipediaapi
    except Exception as e:
        logger.info(e)
        return got_error

    key_msg = wiki_string(msg)
    logger.info("After string process : "+key_msg)
    msg = make_wiki_key(key_msg)
    
    logger.info("Wiki key : "+str(msg))

    key_msg = str(key_msg)
    msg = str(msg)
    
    matched = is_matched(key_msg,msg, need = 75)
    logger.info("Matched : " + str(matched))
    if not matched:
        return got_error
    wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page(msg)
    logger.info(page_py.exists())
    summary = get_summary(page_py.summary,no)

    # cprint(summary,'yellow')

    return summary
    

def wiki_search(msg,no =2):
    return wiki_summary(msg,no)

# def wiki_search(msg, no = 2) :
#     """ This function will search through wikipedia and will reply information
#         Written by Saurav Paul.
#     """
#     try :
#         import wikipedia
#     except Exception as e:
#         logger.inf(str(e))
#         return wiki_summary(msg,no)
    
#     logger.info('Searching to wikipedia.') 
#     cprint('\t\t(Thinking)','yellow')
#     rem = msg
#     msg = wiki_string(msg.lower())
#     msg = make_wiki_key(msg)
#     logger.info('after processing the string is : ' + msg)
#     try :
#         results = wikipedia.summary(msg,sentences=no)
#         return results
#     except :
#         logger.info("Haven't found anything relevant in wikipedia")
#         # search_google(rem)
#         return 'no data available'

