import wikipedia

def wiki_search(msg) :
    try :
        results = wikipedia.page(msg).content.split(sep='.')
        msg = ""
        i = 0
        for line in results :
            if i == 4 :
                break
            msg += line
            i += 1
        return msg 
    except :
        return "sorry sir, i don't know about " + msg

