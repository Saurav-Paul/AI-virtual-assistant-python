import os
from system.screen_text import command_sep

shell_keys = ['-shell','-Shell','-s','-S','cmd:']

def execute(msg):
    command_sep()
    os.system(msg)
    command_sep()
    

def if_shell_type(msg):
    for key in shell_keys:
        if key in msg :
            msg = msg.replace(key,'',1)
            execute(msg)
            return True 
    return False