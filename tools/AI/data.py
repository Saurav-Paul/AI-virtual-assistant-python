
from datetime import datetime
def get_time() :
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    tm = current_time.split(sep=':')
    apm = 'pm'
    if int(tm[0]) < 12 :
        apm = 'am'
        if int(tm[0]) == 0 :
            tm[0] = '12'
    
    elif int(tm[0]) > 12 :
        tm[0] = str( int(tm[0]) - 12 )
    current_time = 'Sir, now is {hour} : {min} '.format(hour=tm[0],min=tm[1]) + apm 
    print(current_time)

    return current_time

data = {
    'how are you' : 'I am fine, thank you sir',
    'good morning' : 'Good morning to you sir' , 
    'good night' : 'Good night to you sir' ,
    'what is the time' : get_time(),
}

