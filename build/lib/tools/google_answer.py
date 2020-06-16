
try:
    import requests
    from bs4 import BeautifulSoup
    # from settings.logs import logger
except Exception as e:
    pass

try :
    from settings.settings import bot
except Exception as e:
    # logger.info(e)
    pass

def rep(msg):
    msg = msg.replace(bot['name'],'')
    msg = msg.replace("'","")
    msg = msg.replace('"','')
    msg = msg.replace('+' , 'plus')
    return str(msg)

def google_answer(msg):
    try :
        url = 'https://www.google.com/search?q='
        url ='https://www.wolframalpha.com/input/?i=125+-+375'
        msg = rep(msg)
        lt = msg.split()
        for word in lt :
            url += word + '+'
        # logger.info('Got url : ' + url)
        source = requests.get(url).text
        bs = BeautifulSoup(source,'lxml')
        print(bs)
        # key = 'BNeawe iBp4i AP7Wnd'
        # ans = bs.find(class_= key).div.text
        return 'Solution is ' + ans
    except Exception as e :
        # logger.info(str(e))
        print(e)
        return "sorry"


if __name__ == "__main__":   
    # x = input('IN-> ')
    x=''
    x = google_answer(x)
    print(x)

