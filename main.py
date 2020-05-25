#!/usr/bin/python3

from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *
from data.data import bye
from tools.string_processing import string_process
from system.screen_text import asci_banner , line_sep
from settings.settings import START_SCREEN_NAME

def check_done(msg):
    for i in bye:
        if i in msg:
            return True
    return False

def main() :
    logger.info('Bot starts.')
    asci_banner(START_SCREEN_NAME)
    speak('Hello sir, how can i help you?')
    while True :
        get =string_process(get_audio())
        if check_done(get):
            break
        msg = ai(get)
        speak(msg)
        line_sep()
    speak('Good Bye, Sir.')
    asci_banner('Have a Good Day!')
    logger.info('Bot stopped.')
    

main() 