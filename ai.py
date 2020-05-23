
from data import data
from wiki_search import wiki_search

def ai(msg) :
    reply = "I don't know what to do, sir"
    for line in data :
        if msg in line:
            reply = data[line]
            return reply
    reply = wiki_search(msg)
    return reply

