
from gtts import gTTS
import os , time , playsound
from settings.settings import interaction_setting as it

def speak_voice(sentence):
    Gtts = gTTS(text=sentence,lang='en')
    print('Gtts setted')
    filename = 'voice.mp3'
    Gtts.save(filename)
    print('Gtts saved now will play the sound')
    playsound.playsound(filename)
    print('removeing file')
    os.remove(filename)

def speak_text(sentence):
    bot = '(^-^)-> '
    print(bot,sentence)

def speak(sentence):
    """This functin will determine if bot will speak or only reply"""
    if it['voice_reply']:
        speak_voice(sentence)
    if it['text_reply']:
        speak_text(sentence)
    else :
        print('Sir your speaking and writing cabapity is disibled. Please enbale it from settings.')