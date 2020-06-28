from settings._first_load_ import check_if_first_time
import sys , os
from termcolor import cprint


def cp_start():

    try :

        from system.screen_text import asci_banner
        from tools.OJ.cp import cp_manager
        from settings.settings import START_SCREEN_NAME
        asci_banner('   '+START_SCREEN_NAME)
        total = len(sys.argv)
        lt = list(sys.argv)
        lt = lt[1:]
        msg = ''
        for w in lt:
            msg +=w+' '
        cp_manager(msg.strip())

        pt = '-'*50
        cprint(pt,'magenta')
        cprint(f' (^-^) -> Good luck sir.','green')
        cprint(pt,'magenta')

    except Exception as e:
        cprint("Can't open sir.",'red')