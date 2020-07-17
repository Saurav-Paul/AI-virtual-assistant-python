import os
from tools.ConfigParser import ConfigParser_manager as CM 
from system.path import getpath
from termcolor import cprint

conf_path = os.path.join(getpath(__file__),'settings.conf')
default_path = os.path.join(getpath(__file__),'default.conf')
export_file_name = 'ai_virtual_assistant_configs.conf'

def import_settings():
    if not os.path.exists(export_file_name):
        return False
    else :
        cprint(' Export file exists. Do you want import(y/n) : ','cyan',end='')
        confirm = input()
        positive = ['y', 'yes', 'ok', 'okay']
        if confirm.lower() in positive :
            from settings.settings import all_sections
            try :
                obj = CM()
                for section in all_sections :
                    data = obj.read(export_file_name,section = section)
                    conf_data = obj.read(conf_path,section = section)

                    for key in conf_data:
                        try :
                            x = data[key]
                            conf_data[key] = x
                        except:
                            pass
                    obj.update(conf_path,conf_data,section = section)

                cprint(" Configs are successfully imported.",'green')
                return True

            except Exception as e:
                cprint(f" Sorry sir can't import. Error : {e}",'red')
                return False
        else :
            return False


def first_time() :
    pt = 22 * '-' + 'First time setup' + 22 * '-'
    done = import_settings()

    if done :
        return

    try :
        with open(default_path) as f :
            default_value = f.read()
        with open(conf_path,'w') as f :
            f.write(default_value)
    except Exception as e:
        cprint(e,'red')

    cprint(pt,'magenta')
    print()
    cprint(" (^-^) Enter your name : ",'cyan',end='')
    name = input()
    section = 'bot'
    obj = CM()
    x = obj.read(conf_path,section)
    x['boss'] = name
    obj.update(conf_path,x,section)

    print()
    cprint(f' (^-^) Hello {name} , do you want me to speak ?(Y/N) ','cyan',end='')
    confirm = input()
    positive_keys = ['y','yes','ok','okay']
    if confirm.lower() in positive_keys:
        from system.features_installation import install_speaking_system
        install_speaking_system()
        section = 'interaction_setting'
        x = obj.read(conf_path,section)
        x['voice_reply'] = 'True'
        obj.update(conf_path,x,section)
    else :
        section = 'interaction_setting'
        x = obj.read(conf_path,section)
        x['voice_reply'] = 'False'
        obj.update(conf_path,x,section)

    
    print()

    cprint(f' (^-^) Hello {name} , do you want me to work faster ?(Y/N) ','cyan',end='')
    confirm = input()
    positive_keys = ['y','yes','ok','okay']
    if confirm.lower() in positive_keys:
        from system.features_installation import speed_up
        speed_up()
    
    print()
    print()
    cprint(len(pt)*'-','magenta')
    from system.screen_text import clear_screen
    clear_screen(start=False)

def check_if_first_time():
    section = 'start_time'
    obj = CM()
    dic = obj.read(conf_path,section)
    if dic['first_start'] == 'False':
        return False
    else :
        first_time()
        dic['first_start'] = 'False'
        obj.update(conf_path,dic,section)
        return True
    pass

check_if_first_time()
