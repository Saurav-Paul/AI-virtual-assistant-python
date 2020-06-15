
from os import system,name

def setup():
    # system('pip3 install -i requirements.txt')
    # for windows 
    if name == 'nt':
        print("System found : Windows.")
        system('pip3 install pypiwin32') 

    # for mac and linux(here, os.name is 'posix') 
    else:
        print("System found : Linux.")
        system('sudo apt-get install python3-dev build-essential')
        system('sudo apt-get install python3-pyaudio')
        system('pip3 install pyttsx3') 

    with open('requirements.txt') as f:
        need = f.read()
    
    system("pip install wheel")
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
        print('\nSetup is completed.')


if __name__ == "__main__":
    setup()