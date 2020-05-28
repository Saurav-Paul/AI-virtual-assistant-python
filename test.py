
try:
    import requests
    from bs4 import BeautifulSoup
    # from settings.logs import logger
except expression as identifier:
    pass

def google_calculation(msg):
    try :
        url = 'https://www.google.com/search?q='
        lt = msg.split()
        for word in lt :
            if word == '+':
                url += 'plus' + '+'
            else :
                url += word + '+'
        # logger.info(url)
        source = requests.get(url).text
        bs = BeautifulSoup(source,'lxml')
        key = 'BNeawe iBp4i AP7Wnd'
        ans = bs.find(class_= key).div.text
        print('Ans : ',ans)
    except Exception as e :
        # logger.info(str(e))
        pass


if __name__ == "__main__":   
    x = input('IN-> ')
    google_calculation(x)

