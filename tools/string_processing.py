

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

