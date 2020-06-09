# Written By Saurav Paul
from tools.json_manager import JsonManager as JM

interaction_setting = {
    'voice_reply' : True,
    'text_reply' : True ,
    'voice_read+voice_reply' : False ,
    'text_read' : True,
}
bot = {
    'name' : 'Jarvis', # You can change bot name from here
    'gender' : 'male', #Whatever you want ;p
    'Boss' : 'Saurav Paul', # you can put your name her ;p 
    'voice_engine' : 'robotic' , # you can change it to 'gTTS' for more natural voice (online) 
    
}
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