#!/usr/bin/ python3

from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *
from data.data import bye
from tools.string_processing import string_process
from system.screen_text import asci_banner , line_sep , clear_screen
from settings.settings import START_SCREEN_NAME
from tools.AI.data import google
import os

def check_done(msg):
    for i in google:
        if i in msg:
            return False
    for i in bye:
        if i in msg:
            return True
    return False

def main(get='',orginal_path='') :

    logger.debug('Bot starts at ' + str(os.getcwd()))
    asci_banner(START_SCREEN_NAME)
    if get == '':
        speak('Hello sir, how can I help you?')
        while True :
            get =string_process(get_audio())
            print()
            if check_done(get):
                break
            if get == 'clear':
                clear_screen()
            else :
                msg = ai(get,orginal_path)
                speak(msg)
                line_sep()
        speak('Good Bye Sir.')
        asci_banner('BYE!')
    else :
        msg = ai(get,orginal_path)
        speak(msg)
        line_sep(t=2)
    logger.debug('Bot stopped.')
    

if __name__ == "__main__":
    main()