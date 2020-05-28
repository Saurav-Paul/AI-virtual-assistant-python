from main import main
import sys , os
from settings.settings import read_bot

def get_args(lt,lim):
    get = ''
    for i in range(2,lim):
        get += str(lt[i]) + ' '
    return get.strip()

if __name__ == "__main__":
    try :
        total = len(sys.argv)
        lt = list(sys.argv)
        orginal_path = lt[0]
        orginal_path = orginal_path[0:len(orginal_path)-6]
        # read_bot(orginal_path)
        os.chdir(sys.argv[1])
        main(get_args(lt,total),orginal_path)
    except :
        main(orginal_path=os.getcwd())
