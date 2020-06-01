#!/usr/bin/python3

from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *
from data.data import bye
from tools.string_processing import string_process
from system.screen_text import asci_banner
from system.install import install , command
from tools.string_processing import is_matched

import json

def check_done(msg):
    for i in bye:
        if i in msg:
            return True
    return False

def test_fuzzy() :
    logger.info('Bot starts.')
    asci_banner('Hello Saurav')
    x = input('in1->')
    y = input('in2->')
    print(is_matched(x,y))
    # speak(install('subprocess pickle-mixin',2))
    logger.info('Bot stopped.')
    

def testing_json():

    with open("t.json", "r") as read_it: 
        data = json.load(read_it) 


if __name__ == "__main__":
    test_fuzzy()

