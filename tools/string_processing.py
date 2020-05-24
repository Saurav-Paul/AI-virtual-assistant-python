

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