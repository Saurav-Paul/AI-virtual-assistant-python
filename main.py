from tools.interaction.speak import speak
from tools.interaction.get_audio import get_audio
from tools.AI.ai import ai
from settings.logs import *

def main() :
    logger.debug('Bot starts')
    speak('Hello sir, how can i help you?')
    get = get_audio()
    # get = 'What is the time'
    msg = ai(get.lower())
    print('got the answer :',msg)
    speak(msg)
    

main() 