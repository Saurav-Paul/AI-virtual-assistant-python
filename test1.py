

#! /usr/bin/env python3
# defineterm.py

import requests
from bs4 import BeautifulSoup
import sys
import html
import codecs

searchterm = ' '.join(sys.argv[1:])
print(searchterm)

url = 'https://www.google.com/search?q=define+' + searchterm
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print('error while loading page occured: ' + str(exc))

text = html.unescape(res.text)
soup = BeautifulSoup(text, 'lxml')
prettytext = soup.prettify()

# print(prettytext)

#next lines are for analysis (saving raw page), you can comment them
frawpage = codecs.open('rawpage.txt', 'w', 'utf-8')
frawpage.write(prettytext)
frawpage.close()

firsttag = soup.find('h3', class_="r")
if firsttag != None:
    print(firsttag.getText())
    print()

#second tag may be changed, so check it if not returns correct result. That might be situation for all searched tags.
secondtag = soup.find('div', {'style': 'color:#666;padding:5px 0'})
if secondtag != None:
    print(secondtag.getText())
    print()

termtags = soup.findAll("li", {"style" : "list-style-type:decimal"})

count = 0
for tag in termtags:
    count += 1
    print( str(count)+'. ' + tag.getText())
    print()

# import pypygo
# from tools.wiki_search import wiki_search

# def foo(q):
#     try :
#         q = pypygo.query(x)
#         return q.abstract
#     except Exception as e:
#         print(str(e))

# while 1:
#     x = input('Enter your query : ')
#     x = foo(x)
#     if(x == '' or x == None) :
#         print('here')
#         x = wiki_search(x)
#     print(x)
