import  wolframalpha
from settings.logs import *
from tools.wiki_search import wiki_search
from tools.browser.search import search_google
from settings.settings import bot

def ask_question(question) :
    """Ask me anything, I will use my reply using wolframalpha api
        Written by Saurav Paul."""
    logger.info('Asking wolframalpha.')
    try :
        print('(Hmm..Thinking....)')
        api_key = 'GLHKQ7-R5V9E6GU3Y'
        client = wolframalpha.Client(api_key)
        res = client.query(question)
        answer = next(res.results).text
        if 'Wolfram|Alpha' in answer:
            answer = answer.replace('Wolfram|Alpha',bot['name'])
        if 'data not available' in answer:
            answer = 'check browser.'
            search_google(question)
        return answer
    except :
        logger.info('Wolframalpha do not know the answer.')
        # answer = wiki_search(question)
        # logger.info(answer)
        search_google(question)
        answer = 'check browser.'
        return answer 

