
try:
    import pyttsx3
except Exception as e:
    print(str(e))

def speak_pyttsx3(msg):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate',130)
        engine.setProperty('volume',1)
        engine.say(msg)
        engine.runAndWait()
    except Exception as e:
        print(str(e))

speak_pyttsx3('Hello sir, how can i help you?')

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('rate',130)
# for voice in voices:
#     print(voice)
#     if voice.languages[0] == u'en_US' or 1:
#         engine.setProperty('voice', voice.id)
#         engine.say('Hello Saurav,Sir. How are you , sir?')
        

# engine.say('Hello sir, how can i help you?')
# engine.runAndWait()