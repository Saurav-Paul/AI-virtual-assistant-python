
try:
    import requests
    from bs4 import BeautifulSoup
    from settings.logs import logger
except Exception as identifier:
    pass

try :
    from settings.settings import bot
except Exception as e:
    logger.info(e)

def rep(msg):
    msg = msg.replace(bot['name'],'')
    msg = msg.replace("'","")
    msg = msg.replace('"','')
    msg = msg.replace('+' , '%2B')
    return str(msg)

def api_math(msg):
    # https://api.mathjs.org/v4/?expr=2%2B3*sqrt(4)
    pass
def google_calculation(msg):
    try :
        headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
        }
        # headers = {
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        # }
        # print(headers)
        url = 'https://www.google.com/search?q='
        msg = rep(msg)
        lt = msg.split()
        for word in lt :
            url += word + '+'
        logger.info('Got url : ' + url)
        source = requests.get(url,headers).text
        bs = BeautifulSoup(source,'lxml')
        # print(bs)
        key = 'BNeawe iBp4i AP7Wnd'
        ans = bs.find(class_= key).div.text
        return 'Solution is ' + ans
    except Exception as e :
        logger.info(str(e))
        return "sorry"


if __name__ == "__main__":   
    x = input('IN-> ')
    google_calculation(x)

