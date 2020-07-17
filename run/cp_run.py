from settings._first_load_ import check_if_first_time
import sys , os
from termcolor import cprint


def cp_start():

    try :
        nm = 'ai-virtual-assistant'
        st = int((56 - len(nm))/2)
        pt = '-' * (st-1) + nm + '-' * (st+1)
        cprint(pt,'magenta')
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

        pt = '-'*len(pt)
        cprint(pt,'magenta')
        cprint(f' (^-^) -> Good luck sir.','green')
        cprint(pt,'magenta')

        if status == '$SHELL' :
            os.system('$SHELL')

    except :
        cprint("Can't open sir.",'red')
