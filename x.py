import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

# from speak import speak

# to search
# print(chatbot_query('how old is samuel l jackson'))

def chatbot_query(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'
    result = ''

    try:
        search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))
        print(search_result_list)
        page = requests.get(search_result_list[index])

        tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback

        return result
    except:
        if len(result) == 0: result = fallback
        return result

ans = chatbot_query('what is the time in bangladesh')
print(ans)
# speak(ans)