from settings._first_load_ import check_if_first_time
from run.main import main
import sys , os
from settings.settings import read_bot
from system.path import getpath
from termcolor import cprint

def get_args(lt,lim):
    get = ''
    for i in range(1,lim):
        get += str(lt[i]) + ' '
    return get.strip()

def all_args(lt):
    ok = False
    arg = ''
    for w in lt:
        if ok:
            arg += w +' '
        if w=='-arg':
            ok = True
    return arg.strip()

def make_path(lt,lim):
    path = ''
    ok = False
    for i in range(1,lim):
        if lt[i] == '-arg':
            break
        if ok:
            path += ' '
        path += lt[i]
        ok = True
    return path

if __name__ == "__main__":
    try :
        total = len(sys.argv)
        lt = list(sys.argv)
        if '-arg' in lt:
            # orginal_path = lt[0]
            # orginal_path = orginal_path[0:len(orginal_path)-6]
            # print(orginal_path)
            orginal_path = getpath(__file__)
            p = str(sys.argv)
            file_path = make_path(lt,total)
            os.chdir(file_path)
            # print(orginal_path)
            arg = all_args(lt)
            main(arg,orginal_path)
        else :
            arg = get_args(lt,len(lt))
            main(arg.strip() , orginal_path=os.getcwd())

    except Exception as e:
        # print(e)
        main(orginal_path=os.getcwd())


def start():
    try :
        total = len(sys.argv)
        lt = list(sys.argv)
        if '-arg' in lt:
            # orginal_path = lt[0]
            # orginal_path = orginal_path[0:len(orginal_path)-6]
            # print(orginal_path)
            orginal_path = getpath(__file__)
            p = str(sys.argv)
            file_path = make_path(lt,total)
            os.chdir(file_path)
            # print(orginal_path)
            arg = all_args(lt)
            main(arg,orginal_path)
        else :
            arg = get_args(lt,len(lt))
            main(arg.strip() , orginal_path=os.getcwd())

    except Exception as e:
        # print(e)
        main(orginal_path=os.getcwd())



# def cp_start():

#     try :
#         from system.screen_text import asci_banner
#         from tools.OJ.cp import cp_manager
#         from settings.settings import START_SCREEN_NAME
#         asci_banner(START_SCREEN_NAME)
#         total = len(sys.argv)
#         lt = list(sys.argv)
#         lt = lt[1:]
#         msg = ''
#         for w in lt:
#             msg +=w+' '
#         cp_manager(msg.strip())

#         pt = '-'*50
#         cprint(pt,'magenta')
#         cprint(f' (^-^) -> Good luck sir.','green')
#         cprint(pt,'magenta')

#     except Exception as e:
#         # print(e)
#         main(orginal_path=os.getcwd())