
from gtts import gTTS
import os , time , playsound

def speak(sentence):
    Gtts = gTTS(text=sentence,lang='en')
    print('Gtts setted')
    filename = 'voice.mp3'
    Gtts.save(filename)
    print('Gtts saved now will play the sound')
    playsound.playsound(filename)
    print('removeing file')
    os.remove(filename)

