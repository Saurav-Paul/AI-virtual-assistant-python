import requests
from bs4 import BeautifulSoup
from settings.logs import logger
# ok = input('give ok: ')
# url = 'https://www.google.com/search?q={}'.format(ok)
# print(url)
# url = 'http://api.mathjs.org/v4/?expr=500*(7-3)'
# source = requests.get(url).text
# bs = BeautifulSoup(source, 'lxml')
# print(bs)
# with open('h.html','w') as f:
#     f.write(bs.prettify())
# for i in  bs.find_all('span'):
#     print(i)

# q = bs.find(class_="BNeawe iBp4i AP7Wnd").div.text
# print(q)
def google_calculation(msg):
    try :
        url = 'https://www.google.com/search?q='
        lt = msg.split()
        for word in lt :
            if word == '+':
                url += word + '+'
            else :
                url += word + '+'
        logger.info(url)
        source = requests.get(url).text
        bs = BeautifulSoup(source,'lxml')
        key = 'BNeawe iBp4i AP7Wnd'
        ans = bs.find(class_= key).div.text
        print('Ans : ',ans)
    except Exception as e :
        logger.info(str(e))

x = input('IN-> ')
google_calculation(x)