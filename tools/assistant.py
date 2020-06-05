import  wolframalpha
from settings.logs import *
from tools.wiki_search import wiki_search
from tools.browser.search import search_google
from settings.settings import bot
from termcolor import cprint

def ask_question(question) :
    """Ask me anything, I will use give my reply using wolframalpha api.if I don't find the answer
        I will search google.
        Don't worry I have alternative ;p 
        Written by Saurav Paul."""
    logger.info('Asking wolframalpha.')
    try :
        cprint('Hmm..Thinking....','yellow')
        api_key = 'GLHKQ7-R5V9E6GU3Y'
        client = wolframalpha.Client(api_key)
        res = client.query(question)
        answer = next(res.results).text
        if 'Wolfram|Alpha' in answer:
            answer = answer.replace('Wolfram|Alpha',bot['name'])
        if 'no data available' in answer:
            answer = wiki_search(question,1) 
            # search_google(question)
        return answer
    except :
        logger.info('Wolframalpha do not know the answer.')
        answer = wiki_search(question,1)
        logger.info(answer)
        # search_google(question)
        # answer = 'check browser.'
        return answer 

