
from fuzzywuzzy import fuzz

def match_string(msg,orginal,no = 1):
    if no == 1:
        return max(fuzz.WRatio(msg,orginal),fuzz.token_sort_ratio(msg,orginal))
    elif no == 2:
        return fuzz.WRatio(msg,orginal)
    elif no == 3:
        return fuzz.ratio(msg,orginal)
    else:
        return fuzz.token_sort_ratio(msg,orginal)

def string_process(msg):
    lt = list(msg.split())
    msg = ""
    i = 0 
    for word in lt:
        if i :
            msg += ' '
        i += 1
        msg += word
    return msg.lower()

def wiki_string(msg):
    if 'wiki' not in msg and 'wikipedia' not in msg:
        return msg 
    lt = list(msg.split())
    msg = ""
    ok = False 
    for word in lt:
        if ok :
            msg += word+' '
        if word == 'wiki' or word =='wikipedia':
            ok = True
    return msg.rstrip()