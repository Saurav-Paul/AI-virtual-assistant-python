from speak import speak
from get_audio import get_audio
from ai import ai



def main() :
    speak('Hello sir, how can I help you?')
    get = get_audio()
    msg = ai(get)
    speak(msg)
    

main() 