from tools.voice.speak import speak
from tools.voice.get_audio import get_audio
from tools.AI.ai import ai



def main() :
    speak('Hello sir, how can I help you?')
    # get = get_audio()
    get = 'What is the time'
    msg = ai(get)
    print('got the answer :',msg)
    speak(msg)
    

main() 