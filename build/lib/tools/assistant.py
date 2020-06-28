import  wolframalpha
from settings.logs import *
from tools.wiki_search import wiki_search , wiki_summary
from tools.browser.search import search_google
from settings.settings import bot
from termcolor import cprint
from time import time , sleep
from threading import Thread
import multiprocessing
from tqdm import tqdm



not_found = ['no data available']

wiki_result = 'no data available'

qus = ''

def wiki(msg):
    try :
        global wiki_result
        t = time()
        # print("Calling")
        wiki_result = wiki_search(msg,1)
        # cprint(time()-t,'blue')
        # print(wiki_result)
        logger.info('wiki time : '+time()-t +' sec')
    except Exception as e:
        # cprint(e,'red')
        pass

ans = 'x'
def wiki_multi():
    try :
        global wiki_result
        global ans
        t = time()
        # print("Calling")
        wiki_result = wiki_search(qus,1)
        # cprint(time()-t,'blue')
        cprint(wiki_result,'yellow')
        share['ans'] = wiki_result
        logger.info('wiki time : '+time()-t +' sec')
        
    except Exception as e:
        # cprint(e,'red')
        pass






def worker(procnum, return_dict):
    '''worker function'''
    st_time = time()
    return_dict[procnum] = wiki_summary(procnum,2)
    logger.info(time()-st_time)


def ask_question(question):
    global wiki_result
    answer = 'no data available'
    cprint('\t\t(Thinking)','yellow')
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = multiprocessing.Process(target=worker, args=(question,return_dict))
    p.start()
    sleep_time = 1/10
    for i in tqdm(range(100),desc='Thinking',unit='it'):
        sleep(sleep_time)
        if not p.is_alive():
            sleep_time = 0
    if p.is_alive():
        p.terminate()
    p.join()
    # jobs = []
    # for i in range(1):
    #     p = multiprocessing.Process(target=worker, args=(question,return_dict))
    #     jobs.append(p)
    #     p.start()

    # for proc in jobs:
    #     proc.join()


    if len(return_dict) > 0 :
        answer =  return_dict.values()[0]

    if answer in not_found:
        answer = 'Check browser'
        search_google(question)

    return answer


def ask_question2(question) :
    global wiki_result
    global qus
    qus = question
    print("here")
    manager = multiprocessing.Manager()
    share = manager.dict()
    p = multiprocessing.Process(target=wiki_multi,args=(share))
    p.start()

    cnt = 0
    tot = 15
    # try :
    #     with tqdm(total=tot,desc='Thinking',initial=0) as pbar:
    #         for i in range(tot):
    #             sleep(1)
    #             pbar.update(1)
    #             cnt += 1
    #             # if not p.is_alive():
    #             #     break
            
    #         pbar.update(cnt-tot)
    # except :
    #     pass
    for i in tqdm(range(15)):
        sleep(1)
    p.join(15)
    if p.is_alive():
        print("Sorry Can't find answer")
        p.terminate()
    
    # p.join()
    cprint(share.values(),'green')
    return wiki_result


def ask_question1(question) :
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
        raise Exception
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

