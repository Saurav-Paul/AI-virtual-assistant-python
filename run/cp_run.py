from settings._first_load_ import check_if_first_time
import sys , os
from termcolor import cprint
import random

def print_start_name(name,weight,name_col,border_col) :
    spaceno = weight - len(name) - 2
    spaceno = int(spaceno/2)
    cprint('-'*weight , border_col)
    cprint('|'+' '*spaceno ,border_col,end='' )
    cprint(name,name_col,end='')
    cprint(' '*spaceno + '|',border_col)
    cprint('-'*weight , border_col)



def cp_start():

    try :

        color = ['magenta','yellow','cyan','blue']
        pt = 50 
        name_col = random.choice(color) 
        border_col = random.choice(color) 
        print_start_name('ai-virtual-assistant',50 ,name_col,border_col)
        
        pt = '-'*pt
        cprint(pt,border_col)
        # from system.screen_text import asci_banner
        from tools.OJ.cp import cp_manager
        # from settings.settings import START_SCREEN_NAME
        # asci_banner('   '+START_SCREEN_NAME)
        # total = len(sys.argv)
        lt = list(sys.argv)
        lt = lt[1:]
        msg = ''
        for w in lt:
            msg +=w+' '
        status = cp_manager(msg.strip())

        cprint(pt,border_col)
        cprint(f' (^-^) -> Good luck sir.','green')
        cprint(pt,border_col)

        if status == '$SHELL' :
            os.system('$SHELL')

    except :
        cprint("Can't open sir.",'red')
