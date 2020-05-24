
import webbrowser

def make_query(msg):
    q = ''
    lt = msg.split()
    i = 0
    for word in lt:
        if i :
            q += '+'
        q += word
        i += 1
    return q

def search_google(msg):
    q = "https://www.google.com/search?q="
    webbrowser.open(q+make_query(msg))

def search_wiki(msg):
    q = "https://en.wikipedia.org/w/index.php?cirrusUserTesting=control&search="
    webbrowser.open(q + make_query(msg))

def search_youtube(msg):
    q = 'https://www.youtube.com/results?search_query='
    webbrowser.open(q+make_query(msg))

search_google('Saurav Paul CEO')