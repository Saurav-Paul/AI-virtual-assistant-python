from main import main
import sys , os

def get_args(lt,lim):
    get = ''
    for i in range(2,lim):
        get += str(lt[i]) + ' '
    return get.strip()

if __name__ == "__main__":
    try :
        total = len(sys.argv)
        lt = list(sys.argv)
        os.chdir(sys.argv[1])
        main(get_args(lt,total))
    except Exception as e :
        raise e
