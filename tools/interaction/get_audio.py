import speech_recognition as sr 

def get_audio():
    r = sr.Recognizer()
    print("Ready to listen")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('adjusted ambient noise')
        audio = r.listen(source,timeout=8, phrase_time_limit=20)   
        said = ""
        print('audio listened')

        try :
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception occured ",str(e))
    return said


