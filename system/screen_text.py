import pyfiglet
from os import system , name
from settings.settings import START_SCREEN_NAME
  

def line_sep(t=1):
    for i in range(t):
        print('-'*50)

def asci_banner(msg):
    banner = pyfiglet.figlet_format(msg)
    line_sep(2)
    print(banner)
    line_sep(2)

def thoughts_processing(msg):
    print('.'*10 + msg + '.'*10)   

def command_sep():
    print('-'*23+'X-X-X'+'-'*22) 


def clear_screen(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
    asci_banner(START_SCREEN_NAME)
  


