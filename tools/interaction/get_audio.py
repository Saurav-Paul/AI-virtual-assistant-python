
from settings.settings import interaction_setting as it 
from settings.logs import *

def get_audio_text():
    msg = input("(Write Something)-> ")
    return msg

def get_audio_microphone():
    try :
        import speech_recognition as sr
        r = sr.Recognizer()
        logger.info("Ready to listen")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            logger.info('adjusted ambient noise')
            audio = r.listen(source,timeout=8, phrase_time_limit=20)   
            said = ""
            logger.info('audio listened')
            print('(Say someting) ->',sep=' ')
            try :
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception occured ",str(e))
        return said
    except :
        return get_audio_text() 


def get_audio():
    if it['voice_read+voice_reply']:
        return get_audio_microphone()
    elif it['text_read']:
        return get_audio_text()
    else: 
        logger.error('Your mircrophone audio and read text both are disabled, enable them from settings')
        print('Your BOT do not have any listing power, give him the power from settings -_-')
        return 'NONE'
