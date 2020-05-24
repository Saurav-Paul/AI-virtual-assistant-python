from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *
from tools.AI.data import bye

def check_done(msg):
    for i in bye:
        if i in msg:
            return True
    return False
def string_process(msg):
    lt = list(msg.split())
    msg = ""
    i = 0 
    for word in lt:
        if i :
            msg += ' '
        i += 1
        msg += word
    return msg.lower()

def main() :
    logger.info('Bot starts.')
    speak('Hello sir, how can i help you?')
    while True :
        get =string_process(get_audio())
        if check_done(get):
            break
        msg = ai(get)
        speak(msg)
    speak('Good Bye, Sir.')
    logger.info('Bot stopped.')
    

main() 