from main import main
import sys , os
from settings.settings import read_bot

def get_args(lt,lim):
    get = ''
    for i in range(2,lim):
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
        orginal_path = lt[0]
        orginal_path = orginal_path[0:len(orginal_path)-6]
        # going to change a few bit -_-
        p = str(sys.argv)
        # x = p.split(sep='-arg')
        # print(x)
        # read_bot(orginal_path)
        file_path = make_path(lt,total)
        os.chdir(file_path)
        # print(file_path)
        arg = all_args(lt)
        main(arg,orginal_path)
        # print(f'all the args {arg}.')
        # print(lt)
        # os.chdir(sys.argv[1])
        # # print(f'path = {os.getcwd()}')
        # main(get_args(lt,total),orginal_path)
    except Exception as e:
        # print(e)
        main(orginal_path=os.getcwd())
