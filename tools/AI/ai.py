
from tools.assistant import ask_question
from tools.AI.data import data
from tools.wiki_search import wiki_search

def ai(msg) :
    reply = "I don't know what to do, sir"
    
    for line in data :
        if msg in line:
            reply = data[line]
            return reply
    if 'wiki' in msg:
        reply = wiki_search(msg)
    # else :
    #     reply = ask_question(msg)
    
    return reply

