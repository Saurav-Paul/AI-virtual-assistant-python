import os , subprocess
try :
    from system.screen_text import command_sep
except:
    pass

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
    command_sep()
    lt = list(msg.split())
    ans = 'Successfully installed:'
    for word in lt:
        try :
            cmd = 'pip install '
            command(cmd+word,no)
            ans += ' '+word
        except:
            pass
    
    if ans == 'Successfully installed:':
        ans = "Can't install anything, sorry sir"

    ans = 'Done, sir.'
    command_sep()
    return ans

