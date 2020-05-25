import os , subprocess
from settings.logs import *

def encode_to_bin(msg):
    return msg.encode('ascii')

def decode_to_normal(msg):
    return msg.decode('ascii')

def command(msg,no = 1):
    if no == 1 :
        os.system(msg)
    else :
        result = subprocess.run(list(msg.split()), stdout=subprocess.PIPE)
        out = decode_to_normal(result.communicate)
        print('printed:',out,sep='\n')

def install(msg,no = 1):
    logger.info('Trying to install ',msg)
    lt = list(msg.split())
    ans = 'Successfully installed:'
    ans = 'Done, sir.'
    for word in lt:
        try :
            cmd = 'pip install '
            command(cmd+word,no)
            logger.info('Installed '+word+' using pip insatll')
            ans += ' '+word
        except:
            logger.info('Not found '+word+' in pip')
    
    if ans == 'Successfully installed:':
        ans = "Can't install anything, sorry sir"

    return ans


# import subprocess
# >>> result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
# >>> result.stdout