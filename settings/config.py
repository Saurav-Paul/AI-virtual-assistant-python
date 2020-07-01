from tools.ConfigParser import ConfigParser_manager as CM
from system.path import getpath
import os
from termcolor import cprint
from settings.settings import bot as bt
from settings.settings import interaction_setting as its
from settings.settings import update_bot
from tools.json_manager import JsonManager as JM

config_keys = ['-config','-settings']
conf_path = os.path.join(getpath(__file__),'settings.conf')
train_path = os.path.join(getpath(__file__),'.trained')

yes = ['yes','y']

class Config:
    obj = CM()
    lt = ['Bot','Interaction','Competitive Programming','Features Installation','Training Mode']
    cp = [
        'Coder Name',
        'Competitive companion port number',
        'Parse Problem with template',
        'Template Path',
        'Compiler'
    ]
    confirm_keys = ['y','yes','ok']
    def change_gender(self):
        pt = '-'*22 + 'Gender Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current gender : {bt['gender']}",'yellow')
        cprint(" Enter new gender : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['gender'] = new_name
            self.obj.update(conf_path,x,section)
            bt['gender'] = new_name
            update_bot(bt)
            cprint("Gender Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')


    def change_name(self):
        pt = '-'*22 + 'Name Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Name : {bt['name']}",'yellow')
        cprint(" Enter new name : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['name'] = new_name
            self.obj.update(conf_path,x,section)
            bt['name'] = new_name
            update_bot(bt)
            cprint("Name Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')

    def change_boss(self):
        
        pt = '-'*22 + 'Boss Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Boss : {bt['boss']}",'yellow')
        cprint(" Enter new boss : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['boss'] = new_name
            self.obj.update(conf_path,x,section)
            bt['boss'] = new_name
            update_bot(bt)
            cprint("Boss Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')

    def change_voice_engine(self):
        pt = '-'*22 + 'Voice Engine Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current voice engine : {bt['boss']}",'yellow')
        

    def bot(self,no):
        bot = [
            'Name',
            'Gender',
            'Boss',
            'Voice_engine'
        ]
        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        cprint(" Select the index to change,",'yellow')
        
        print()
        # print(bt)
        for i,w in enumerate(bot):
            cprint(f'  {i+1}) {w} : {bt[w.lower()]}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_name()
            elif no == 2:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_gender()
            elif no == 3:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_boss()
            elif no == 4:
                cprint(" Sorry temporary this option is unavailable.",'red')
                ok = True
                continue
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_voice_engine()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')



    def Interaction(self,no):

        options = [
            'voice_reply',
            'text_reply',
            'voice_read_voice_reply',
            'text_read'
        ]
        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        cprint(" Select the index to change,",'yellow')
        
        print()
        
        for i,w in enumerate(options):
            cprint(f'  {i+1}) {w} : {its[w.lower()]}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        try :
                            from system.features_installation import install_speaking_system
                            install_speaking_system()
                        except:
                            pass
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')


            elif no == 2:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            elif no == 3:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        try :
                            from system.features_installation import install_command_system,install_speaking_system
                            install_speaking_system()
                            install_command_system()
                        except Exception as e:
                            cprint(e,'red')

                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            elif no == 4:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')

    def competitive_companion(self):
        try :
            from settings.compiler import competitive_companion_port as ccp, update_ccp
            pt = '-'*22 + 'Competitive Companion' +'-'*22
            cprint(pt,'magenta')
            print()

            cprint(" Current port number : " + str(ccp),'yellow')

            cprint('  1) Change port.','blue')
            cprint('  0) Back.','red')

            ok = True
            while ok:
                ok = False
                cprint(' Enter the index number : ','cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Going back.",'red')
                    self.competitve_programming()
                elif no == 1:
                    print()
                    cprint(" Enter new port number(must be integer) : ",'cyan',end='')
                    port = int(input())
                    # ccp = port
                    update_ccp(port)
                    section = 'cp'
                    x = self.obj.read(conf_path,section)
                    x['competitive_companion_port'] = str(port)
                    self.obj.update(conf_path,x,section)
                    cprint(' Competitive companion port updated succussfully.','green')
                    self.competitive_companion()
                else:
                    cprint(" You have choosen wrong index.",'red')
                    ok = True
        except Exception as e:
            cprint(e,'red')

    def dev_mode(self):

        from settings.settings import update_dev

        pt = '-'*10 + 'Welcome to secret mode for developer' +'-'*10
        cprint(pt,'magenta')
        print()
        section = 'developer'
        dev = self.obj.read(conf_path,section)
        options = {
            'Debug Mode ': dev['debug'],
            'Learning Mode ' : dev['learn']
        }
        for i , w in enumerate(options):
            cprint(f' {i+1}) {w} : {options[w]}','blue')

        cprint(f' 0) Back','red')
        print()

        ok = True
        while ok:
            cprint("Enter index number : ",'cyan',end = '')
            no = int(input())
            ok = False

            if no == 0 :
                cprint("Going Back.",'red')
                return
            elif no == 1:
                cprint("Do you want to toggle Debug mode ?(Y/N) : ",'cyan',end='')
                confirm = input()
                if confirm.lower() == 'y':
                    if dev['debug'] == 'True':
                        dev['debug'] = 'False'
                    else :
                        dev['debug'] = 'True'
                
                    self.obj.update(conf_path,dev,section)
                    update_dev(dev)
                    cprint("Debug mode toggled successfully.",'green')
                else :
                    cprint("Cancelled.",'red')
                self.dev_mode()
            elif no == 2:
                cprint("Do you want to toggle Learning mode ?(Y/N) : ",'cyan',end='')
                confirm = input()
                if confirm.lower() == 'y':
                    if dev['learn'] == 'True':
                        dev['learn'] = 'False'
                    else :
                        dev['learn'] = 'True'
                
                    self.obj.update(conf_path,dev,section)
                    update_dev(dev)
                    cprint("Learning mode toggled successfully.",'green')
                else :
                    cprint("Cancelled.",'red')
                self.dev_mode()
            else :
                cprint("Wrong index. Try again.")
                ok = True
        print()
        cprint('-'*len(pt),'magenta')

    def cpp_template(self):
        from settings.compiler import template_path as tp , update_tp
        pt = '-'*22 + 'c++ Template' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Template : {tp['c++']}",'yellow')
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        
        if confirm.lower() not in yes:
            cprint(" Cancelled.",'red')
            return

        ok = True
        while ok :
            ok = False
            cprint(" Enter template path (enter cancel to cancel): ",'cyan',end='')
            path = input()

            if path.lower() == 'cancel':
                cprint(" Cancelled.",'red')
                return
            elif os.path.isfile(path):
                pt = '-'*22 +'code'+'-'*22
                cprint(pt,'magenta')

                with open(path) as f:
                    code = f.read()
                cprint(code,'yellow')

                pt = '-'*46
                cprint(pt,'magenta')

                sec = 'template_path'
                x = self.obj.read(conf_path,sec)
                x['cpp'] = path
                tp['c++'] = path
                self.obj.update(conf_path,x,sec)
                update_tp(tp)
                cprint("C++ template updated successfully.",'green')
            else :
                ok = True
                cprint("Path doesn't exist. Try again.",'red')


   

    def python_template(self):
        from settings.compiler import template_path as tp , update_tp
        pt = '-'*22 + 'Python Template' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Template : {tp['python']}",'yellow')
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        
        if confirm.lower() not in yes:
            cprint(" Cancelled.",'red')
            return

        ok = True
        while ok :
            ok = False
            cprint(" Enter template path (enter cancel to cancel): ",'cyan',end='')
            path = input()

            if path.lower() == 'cancel':
                cprint(" Cancelled.",'red')
                return
            elif os.path.isfile(path):
                pt = '-'*22 +'code'+'-'*22
                cprint(pt,'magenta')

                with open(path) as f:
                    code = f.read()
                cprint(code,'yellow')

                pt = '-'*46
                cprint(pt,'magenta')

                sec = 'template_path'
                x = self.obj.read(conf_path,sec)
                x['python'] = path
                tp['python'] = path
                self.obj.update(conf_path,x,sec)
                update_tp(tp)
                cprint("Python template updated successfully.",'green')
            else :
                ok = True
                cprint("Path doesn't exist. Try again.",'red')




    def temp_path(self):
        try :
            
            optinos = [
                'C++',
                'Python'
            ]
            pt = '-'*22 + 'Templates Path' +'-'*22
            cprint(pt,'magenta')
            print()
            cprint(" All the available settings are given below,",'yellow')
            
            print()
            # print(bt)
            for i,w in enumerate(optinos):
                cprint(f'  {i+1}) {w}','blue')
            cprint('  0) Cancel','red')
            print()
            ok = True

            while ok:
                ok = False
                cprint(" Enter the index number : ",'cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Operation cancelled.",'red')
                    return
                elif no == 1:
                    cprint(f' You have selected {optinos[no-1]} .','yellow')
                    self.cpp_template()
                elif no == 2:
                    cprint(f' You have selected {optinos[no-1]} .','yellow')
                    self.python_template()
                else :
                    ok = True
                    cprint(" You have selected wrong index. Please try again.",'red')



        except Exception as e:
            cprint(e,'red')

    def cpp_compiler(self):
        try :
            from settings.compiler import compiler, update_compiler
            pt = '-'*22 + 'C++ Compiler' +'-'*22
            cprint(pt,'magenta')
            print()
            # print(compiler)
            ccp = compiler['c++']
            # print(ccp)
            cprint(" Current Compiling Command : ",'yellow',end='')
            cprint(str(ccp),'cyan')
            print()

            cprint('  1) Change command.','blue')
            cprint('  0) Back.','red')
            print()

            ok = True
            while ok:
                ok = False
                cprint(' Enter the index number : ','cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Going back.",'red')
                    self.competitve_programming()
                elif no == 1:
                    print()
                    cprint(" Enter new command(wrong command might broke c++ compiling and testing) : ",'cyan',end='')
                    command = input()
                    # ccp = port
                    section = 'compiler'
                    x = self.obj.read(conf_path,section)
                    x['cpp'] = str(command)
                    self.obj.update(conf_path,x,section)
                    compiler['c++'] = command
                    update_compiler(compiler)
                    cprint(' C++ compiling command updated succussfully.','green')
                    self.cpp_compiler()
                else:
                    cprint(" You have choosen wrong index.",'red')
                    ok = True
        except Exception as e:
            cprint(e,'red')
    def cpp_debug_compiler(self):
        try :
            from settings.compiler import compiler, update_compiler
            pt = '-'*22 + 'C++ Debug Compiler' +'-'*22
            cprint(pt,'magenta')
            print()
            # print(compiler)
            ccp = compiler['c++ debug']
            # print(ccp)
            cprint(" Current Compiling Command : ",'yellow',end='')
            cprint(str(ccp),'cyan')
            print()

            cprint('  1) Change command.','blue')
            cprint('  0) Back.','red')
            print()

            ok = True
            while ok:
                ok = False
                cprint(' Enter the index number : ','cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Going back.",'red')
                    self.competitve_programming()
                elif no == 1:
                    print()
                    cprint(" Enter new command(wrong command might broke c++ debug compiling and testing) : ",'cyan',end='')
                    command = input()
                    # ccp = port
                    section = 'compiler'
                    x = self.obj.read(conf_path,section)
                    x['cpp_debug'] = str(command)
                    self.obj.update(conf_path,x,section)
                    compiler['c++ debug'] = command
                    update_compiler(compiler)
                    cprint(' C++ debug compiling command updated succussfully.','green')
                    self.cpp_debug_compiler()
                else:
                    cprint(" You have choosen wrong index.",'red')
                    ok = True
        except Exception as e:
            cprint(e,'red')
    
    def python_compiler(self):
        try :
            from settings.compiler import compiler, update_compiler
            pt = '-'*22 + 'Python Run Command' +'-'*22
            cprint(pt,'magenta')
            print()
            # print(compiler)
            ccp = compiler['python']
            # print(ccp)
            cprint(" Current Run Command : ",'yellow',end='')
            cprint(str(ccp),'cyan')
            print()

            cprint('  1) Change command.','blue')
            cprint('  0) Back.','red')
            print()

            ok = True
            while ok:
                ok = False
                cprint(' Enter the index number : ','cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Going back.",'red')
                    self.competitve_programming()
                elif no == 1:
                    print()
                    cprint(" Enter new command(wrong command might broke running python file) : ",'cyan',end='')
                    command = input()
                    # ccp = port
                    section = 'compiler'
                    x = self.obj.read(conf_path,section)
                    x['python'] = str(command)
                    self.obj.update(conf_path,x,section)
                    compiler['python'] = command
                    update_compiler(compiler)
                    cprint(' Python running command updated succussfully.','green')
                    self.python_compiler()
                else:
                    cprint(" You have choosen wrong index.",'red')
                    ok = True
        except Exception as e:
            cprint(e,'red')

    def compiler_option(self):
        try :
            optinos = [
                'C++',
                'C++ Debug',
                'python'
            ]

            pt = '-'*22 + "Compiler" +'-'*22
            cprint(pt,'magenta')
            print()
            cprint(" All the available settings are given below,",'yellow')
            
            print()
            # print(bt)
            for i,w in enumerate(optinos):
                cprint(f'  {i+1}) {w}','blue')
            cprint('  0) Cancel','red')
            print()
            ok = True

            while ok:
                ok = False
                cprint(" Enter the index number : ",'cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Operation cancelled.",'red')
                    return
                elif no == 1:
                    cprint(f' You have selected {optinos[no-1]} .','yellow')
                    self.cpp_compiler()
                elif no == 2:
                    cprint(f' You have selected {optinos[no-1]} .','yellow')
                    self.cpp_debug_compiler()
                elif no == 3:
                    cprint(f' You have selected {optinos[no-1]} .','yellow')
                    self.python_compiler()
                else :
                    ok = True
                    cprint(" You have selected wrong index. Please try again.",'red')

        except Exception as e:
            cprint(e,'red')


    def competitve_programming(self,no=2):
        optinos = [
            'Competitive Companion.',
            'Template Path.',
            'Compiler'
        ]

        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(" All the available settings are given below,",'yellow')
        
        print()
        # print(bt)
        for i,w in enumerate(optinos):
            cprint(f'  {i+1}) {w}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.competitive_companion()
            elif no == 2:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.temp_path()
            elif no == 3:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.compiler_option()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')


    def features(self,no):
        from system.features_installation import speed_up, install_speaking_system , install_command_system
        options = [
            'Speed Up',
            'Speaking Capability',
            'Voice Command'
        ]
        pt = '-'*22 + "Features Installaion" + '-'*22
        cprint(pt,'magenta')
        print()
        cprint(" All the available options are given below : ",'yellow')

        print()
        # print(bt)
        for i,w in enumerate(options):
            cprint(f'  {i+1}) {w}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {options[no-1]} .','yellow')
                speed_up()
            elif no == 2:
                cprint(f' You have selected {options[no-1]} .','yellow')
                install_speaking_system()
            elif no == 3:
                cprint(f' You have selected {options[no-1]} .','yellow')
                install_command_system()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')
    
    def train_answer(self):
        
        ok = True 
        while ok :
            ok = False
            print()
            cprint(" Enter the question : ",'cyan',end='')
            question = input()
            cprint(" Enter the answer : ",'cyan',end='')
            answer = input()
            print()
            pt = '-'*18+"Question-Answer"+'-'*18
            cprint(pt,"magenta")
            print()
            cprint(" Q. "+question,'yellow')
            cprint(" Answer : "+answer,'green')
            print()
            cprint(len(pt)*'-','magenta')

            cprint(" Do you want to learn it ?(y/n) : ",'cyan',end='')
            confirm = input()

            if confirm.lower() in self.confirm_keys :
                try :
                    dic = JM.json_read(train_path)
                    dic[question] = answer
                    JM.json_write(train_path,dic)
                    cprint(" Learned successfully.",'green')
                except Exception as e:
                    cprint(e)
            else :
                cprint(" Ok, sir cancelled.",'red')
            
            cprint(len(pt)*'-','magenta')
            cprint(" Do you want to learn more ?(y/n) : ",'cyan',end='')
            confirm = input()

            if confirm.lower() in self.confirm_keys :
                ok = True
            else :
                cprint(" Cancelled." , 'red')
            

    def training_mode(self,no) :
        pt = 22*'-'+self.lt[no] + 22*'-'
        cprint(pt,'magenta')
        print()
        cprint(" All the available settings are given below,",'yellow')
        print()
        options = [
            'Train Answer',
        ] 
        for i,w in enumerate(options):
            cprint(f'  {i+1}) {w}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {options[no-1]} .','yellow')
                self.train_answer()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')


    def config_list(self):
        not_done = True
        while not_done:

            pt = '-'*22 + 'Config'+'-'*22
            cprint(pt,'magenta')
            print()
            cprint(" All the available settings are given below,",'yellow')
            print()
            for i,w in enumerate(self.lt):
                cprint(f'  {i+1}) {w}','blue')
            cprint('  0) Exit','red')
            print()
            ok = True
            while ok:
                ok = False
                cprint(" Enter the index number : ",'cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Exiting.",'red')
                    cprint(" For some setting you might need to restart me.",'yellow')
                    not_done = False
                elif no == 1:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.bot(no-1)
                elif no == 2:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.Interaction(no-1)
                elif no == 3:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.competitve_programming(no-1)
                elif no == 4 :
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.features(no-1)
                elif no == 5 :
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.training_mode(no-1)
                elif no == 75:
                    self.dev_mode()
                else :
                    ok = True
                    cprint(" You have selected wrong index. Please try again.",'red')




def if_config_type(msg):
    if msg in config_keys:
        obj = Config()
        obj.config_list()
        return True
    else:
        return False