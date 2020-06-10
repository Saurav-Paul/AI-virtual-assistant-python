# Written By Saurav Paul
from tools.json_manager import JsonManager as JM
from tools.ConfigParser import ConfigParser_manager as CM
from system.path import getpath
import os
from termcolor import cprint

positive = ['yes','1','true']

interaction_setting = {
    'voice_reply' : True,
    'text_reply' : True ,
    'voice_read_voice_reply' : False ,
    'text_read' : True,
}
bot = {
    'name' : 'Jarvis', # You can change bot name from here
    'gender' : 'male', #Whatever you want ;p
    'boss' : 'Saurav Paul', # you can put your name her ;p 
    'voice_engine' : 'robotic' , # you can change it to 'gTTS' for more natural voice (online) 
    
}

conf_path = os.path.join(getpath(__file__),'settings.conf')
print(conf_path)
try :

    section = 'bot'
    obj = CM()
    bot = obj.read(conf_path,section = section)
    section = 'interaction_setting'
    x = obj.read(conf_path,section=section)
    for i in interaction_setting:
        if x[i].lower() in positive:
            interaction_setting[i] = True
        else :
            interaction_setting[i] = False


except Exception as e:
    print(e)
    cprint("Settings error.",'red')

START_SCREEN_NAME = bot['name'] # Enter a string to make start screen banner

def update_bot(orginal_path):
    f = orginal_path + '/settings/bot.json'
    JM.json_write(f,bot)

def read_bot(orginal_path):
    f = orginal_path + '/settings/bot.json'
    bot = JM.json_read(f)
    print(bot)
    # return bot

DEBUG = False