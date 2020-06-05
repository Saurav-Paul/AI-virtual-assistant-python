
from os import system

def setup():
    # system('pip3 install -i requirements.txt')
    with open('requirements.txt') as f:
        need = f.read()
    
    # print(need)
    lt = need.split('\n')
    # print(lt)
    ok = True
    for module in lt:
        if module == '':
            continue
        try :
            system('pip3 install '+module)
        except:
            print("Can't install "+module + " :(")
            ok = False

    if ok:
        print('\nSetup succesful.')


if __name__ == "__main__":
    setup()