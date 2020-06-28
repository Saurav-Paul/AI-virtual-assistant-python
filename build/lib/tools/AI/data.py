from settings.settings import bot
from datetime import datetime
import time

def get_time() :
    """This function will return current time
        written by Saurav Paul"""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    tm = current_time.split(sep=':')
    apm = 'pm'
    if int(tm[0]) < 12 :
        apm = 'am'
        if int(tm[0]) == 0 :
            tm[0] = '12'
    
    elif int(tm[0]) > 12 :
        tm[0] = str( int(tm[0]) - 12 )
    current_time = 'Sir, now is {hour} : {min} '.format(hour=tm[0],min=tm[1]) + apm +'.'

    return current_time

def digital_time():
    return 'Sir now is '+time.strftime("%-I:%M %p")

data = {
    'who are you' : 'I am '+ bot['name'] +'.',
    'how are you' : 'I am fine, thank you sir.',
    'good morning' : 'Good morning to you sir.' , 
    'good night' : 'Good night to you sir.' ,
    'what is the time' : digital_time(),
    'tell me the time' : digital_time() ,
    'what is your name' : ('my name is ' + bot['name'] + '.'),
    'who am i' : 'You are '+bot['boss'] + '.',
    'tell me my name' : 'Your name is '+bot['boss']+'.',
    "what's up" : 'I am fine, thank you sir.',
    "who is your boss" : "My boss is "+bot['boss']+'.',
    "hello" :"hey",
    "ok" :"okay",
    "okay" :"ok",
    "thank you" : "welcome",
    "hey" : "hello",
    "what about you" : "I am fine sir.",
    "how about you" : "I am fine sir.",
    
}


wiki = [  'search wikipedia','find wikipedia','wikipedia find' ,'wikipedia it','wikipedia', 'search wiki','wiki it','find wiki','wiki find','wiki' ]
youtube = ['search youtube','youtube search', 'youtube it','find youtube' ,'youtube find' , 'youtube']
google = ['search google', 'google search','find google','google find','google it' , 'google','search it' ,'search','find it', 'find','how to']
youtube_play = ['play youtube', 'youtube play']
goto_keys = ['goto','go to']
install_keys = ['pip install','install pip','install']
calc_keys = ['calculator' , 'calculate' , 'calculations' , 'calculations', 'calc', 'solve it' , 'solve']

should_not_learn = ['date','today','check browser','no data available']
version_keys = ['-v','-version','--version']