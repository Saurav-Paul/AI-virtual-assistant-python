import requests
from googlesearch import search
from settings.logs import *
import webbrowser
from tools.interaction.speak import speak

def goto(link):
    webbrowser.open(link)

def find_goto_address(msg):
    logger.info('finding addresses')
    try :
        search_result_list = list(search(msg,tld='co.in',num = 3,stop=1 , pause =1))
        logger.info('Found : ' + search_result_list[0])
        print(search_result_list)
        goto(search_result_list[0])
    except:
        speak("Sorry sir, haven't found any.")

