
from settings.settings import interaction_setting as it 
from settings.logs import *
from system.screen_text import thoughts_processing
from settings.settings import bot

import random

try :
    from termcolor import colored, cprint
except Exception as e:
    logger.info(str(e))
    

try:
    import pyttsx3
except Exception as e:
    logger.info(str(e))

color = ['blue','yellow','green']

def speak_voice_pyttsx3(msg):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate',130)
        engine.setProperty('volume',1)
        engine.say(msg)
        engine.runAndWait()
    except Exception as e:
        logger.info(str(e))

def speak_voice_gtts(sentence):
    """" This function takes a text sentence and in return it will speak that sentence.
        written by saurav paul"""
    logger.info('attempting to speak')
    try :
        from gtts import gTTS
        import os , playsound
        thoughts_processing('voice is loading, Sir')
        Gtts = gTTS(text=sentence,lang='en')
        logger.debug('Gtts setted')
        filename = 'voice.mp3'
        Gtts.save(filename)
        logger.debug('Gtts saved now will play the sound')
        playsound.playsound(filename)
        logger.debug('removeing file')
        os.remove(filename)
    except Exception as e:
        logger.critical(str(e))
        speak_voice_pyttsx3(sentence)

def speak_voice_manager(msg):
    try :
        if bot['voice_engine'] == 'gTTS':
            logger.info('Calling gTTS')
            speak_voice_gtts(msg)
        else:
            logger.info('Calling pyttsx3')
            speak_voice_pyttsx3(msg)
    except Exception as e:
        logger.info(str(e))

def speak_text(sentence):
    """ It will takes a text sentence and reply as bot"""
    print()
    bot = '(^-^)-> '
    cl = random.choice(color)
    cprint(bot,cl,attrs=['bold'],end=' ')
    # cprint(cl,cl)
    x = sentence.capitalize()
    cprint(x,cl)

    

def speak(sentence):
    """This functin will determine if bot will speak or only reply"""
    not_ok = True
    if it['text_reply']:
        speak_text(sentence)
        not_ok = False
    if it['voice_reply'] or it['voice_read_voice_reply']:
        speak_voice_manager(sentence)
        not_ok = False
    if not_ok :
        cprint('Sir your speaking and writing cabapity is disibled. Please enbale it from settings.','red')

