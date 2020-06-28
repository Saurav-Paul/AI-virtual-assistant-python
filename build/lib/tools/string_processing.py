
from fuzzywuzzy import fuzz
from settings.logs import logger

def match_string(msg,orginal,no = 1):
    if no == 1:
        return max(fuzz.WRatio(msg,orginal),fuzz.token_sort_ratio(msg,orginal))
    elif no == 2:
        return fuzz.WRatio(msg,orginal)
    elif no == 3:
        return fuzz.ratio(msg,orginal)
    else:
        return fuzz.token_sort_ratio(msg,orginal)

def is_matched(msg,orginal,need = 90, no = 1):
    percentage = match_string(msg,orginal,no)
    # logger.debug(msg + ' '+orginal+' ' +str(percentage) )
    return (True if percentage >= need else False)

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
    data = ['wiki' , 'wikipedia' , 'what' , 'is' ,'tell' , 'me', 'about' , 'information' ,'give' ,'who']
    msg = msg.split()
    key = ''
    for w in msg:
        if w not in data:
            key += w+' '

    return key.strip()
# def wiki_string(msg):
#     data = ['wiki' , 'wikipedia' , 'what' , 'is' ,'tell' , 'me', 'about' , 'information' ,'give' ,'who']
#     for word in data :
#         msg = msg.replace(word,'')
        
#     return msg.strip()