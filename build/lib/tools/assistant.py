import  wolframalpha
from settings.logs import *
from tools.wiki_search import wiki_search
from tools.browser.search import search_google
from settings.settings import bot
from termcolor import cprint
from time import time
from threading import Thread

wiki_result = 'no data available'

def wiki(msg):
    try :
        global wiki_result
        # t = time()
        # print("Calling")
        wiki_result = wiki_search(msg,1)
        # cprint(time()-t,'blue')
        # print(wiki_result)
    except Exception as e:
        cprint(e,'red')

def ask_question(question) :
    """Ask me anything, I will use give my reply using wolframalpha api.if I don't find the answer
        I will search google.
        Don't worry I have alternative ;p 
        Written by Saurav Paul."""
    logger.info('Asking wolframalpha.')
    global wiki_result
    p = Thread(target=wiki,args=(question,) )
    p.start()
    # xt = time()
    try :
        
        answer = 'no data available'
        # cprint('Hmm..Thinking....','yellow')
        # t = time()
        api_key = 'GLHKQ7-R5V9E6GU3Y'
        client = wolframalpha.Client(api_key)
        res = client.query(question)
        answer = next(res.results).text
        # cprint(time()-t,'cyan')
        if 'Wolfram|Alpha' in answer:
            answer = answer.replace('Wolfram|Alpha',bot['name'])
        if 'no data available' in answer:
            # answer = wiki_search(question,1)
            # print("waiting")
            p.join()
            # print("waiting done")
            answer = wiki_result
            # search_google(question)
        return answer
    except :
        logger.info('Wolframalpha do not know the answer.')
        # answer = wiki_search(question,1)
        # t = time()
        # cprint(t-xt,'magenta')
        p.join()
        # cprint(time()-t,'red')
        answer = wiki_result
        logger.info(answer)
        # search_google(question)
        # answer = 'check browser.'
        return answer 

# def ask_question(question) :
#     """Ask me anything, I will use give my reply using wolframalpha api.if I don't find the answer
#         I will search google.
#         Don't worry I have alternative ;p 
#         Written by Saurav Paul."""
#     logger.info('Asking wolframalpha.')
#     try :
#         answer = 'no data available'
#         cprint('Hmm..Thinking....','yellow')
#         api_key = 'GLHKQ7-R5V9E6GU3Y'
#         client = wolframalpha.Client(api_key)
#         res = client.query(question)
#         answer = next(res.results).text
#         if 'Wolfram|Alpha' in answer:
#             answer = answer.replace('Wolfram|Alpha',bot['name'])
#         if 'no data available' in answer:
#             answer = wiki_search(question,1) 
#             # search_google(question)
#         return answer
#     except :
#         logger.info('Wolframalpha do not know the answer.')
#         answer = wiki_search(question,1)
#         logger.info(answer)
#         # search_google(question)
#         # answer = 'check browser.'
#         return answer 

