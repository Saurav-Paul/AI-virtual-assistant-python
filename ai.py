
from data import data
def ai(msg) :
    reply = "I don't know what to do, sir"
    for line in data :
        if msg in line:
            reply = data[line]
            return reply
    
    return reply

ai('what is the time')