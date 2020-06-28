try:
    import os
    from settings.compiler import compiler
    from tqdm import tqdm
except expression as e:
    pass

try :
    from termcolor import colored, cprint
except Exception as e:
    pass


run_keys = ['-r', '-run']
files_ext = ['cpp','py']

def run_prog(file_name , debug = False , com = False,no=1):
    try :
        # print(os.getcwd())
        pt = ("Running the " +file_name+'......')
        cprint(pt,'yellow')
        ext = file_name.rsplit(sep='.',maxsplit=1)
        if ext[1] == 'cpp':
            if debug :
                cmd = compiler['c++ debug']
            else :
                cmd = compiler['c++']

            cmd = cmd.replace('{filename}',file_name)
            cmd = cmd.replace('{executable}',ext[0])
            cmd_part = cmd.split(sep='&&')
            with tqdm(total=1.0,desc='Compilation',initial=.25) as pbar:
                okk = os.system(cmd_part[0])
                pbar.update(.75)
            if okk != 0 :
                cprint("Compilation Error.",'red')
                return
            pt = ('-'*23+file_name+'-'*22+'\n')
            x = ('\n'+'-'*23+'-'*len(file_name)+'-'*22)
            if not os.path.isfile(ext[0]):
                return
            
            try :
                for i in range(no):
                    cprint(pt,'magenta')
                    okk = os.system(cmd_part[1])
                    cprint(x,'magenta')
                    if okk :
                        cprint("Cancelled.",'red')
                        cprint(x,'magenta')
                        break
                if com == False :
                    os.remove(ext[0])
            except:
                cprint("Sorry sir can't run.",'red')
            
        elif ext[1] == 'py':
            cmd = compiler['python']
            cmd = cmd.replace('{filename}',file_name)
            x = ('-'*23+file_name+'-'*22) 
            pt = ('-'*23+'-'*len(file_name)+'-'*22) 
            try :
                for i in range(no):
                    cprint(x,'magenta')
                    okk = os.system(cmd)
                    cprint(pt,'magenta')
                    if okk :
                        cprint("Cancelled.",'red')
                        cprint(x,'magenta')
                        break
            except:
                cprint("Sorry sir can't run.",'red')
        else :
            cprint('Unknown file format.','red')
    except Exception as e:
        cprint("Compilation Error",'red')


def find_files(lt):
    # print(lt)
    debug = False
    com = False
    tm = 1
    if '-d' in lt:
        debug = True
        try :
            lt.remove('-d')
        except :
            pass 
    if '-c' in lt:
        com = True
        try :
            lt.remove('-c')
        except :
            pass 
    if '-dc' in lt:
        com = True
        debug = True
        try :
            lt.remove('-dc')
        except :
            pass 
    if '-cd' in lt:
        com = True
        debug = True
        try :
            lt.remove('-cd')
        except :
            pass
    
    # print(lt)
    for w in lt :
        if '-' in w:
            temp = w.replace('-','')
            if temp.isnumeric() :
                tm = int(temp)
                lt.remove(w)
    
    # print(tm,lt)
    num = len(lt)
    file_list=[]
    if num == 1:
        for file in os.listdir(os.getcwd()):
            try :
                    ext = file.rsplit(sep='.',maxsplit=1)
                    if ext[1] in files_ext:
                        file_list.append(file)
            except :
                pass
    else :
        arg = lt[1:]
        # print(arg)
        for w in arg:
            for file in os.listdir(os.getcwd()):
                if w.lower() in file.lower() :
                    try :
                            ext = file.rsplit(sep='.',maxsplit=1)
                            if ext[1] in files_ext:
                                file_list.append(file)
                    except :
                        pass
    no = len(file_list)
    if no > 1:
        cprint('All the available files...\n','yellow')
        no = 1
        for i in file_list:
            x = ' '*5+str(no)+") "+ i
            cprint(x,'blue')
            no += 1
        x = (' '*5+'0) stop operation')
        cprint(x,'red')
        print()
        try :
                while True :
                    cprint('Enter the file number : ','cyan',end='')
                    index = int(input())
                    if index == 0:
                        cprint('Operation Cancelled.','red')
                        break
                    elif index > 0 and index < no :
                        run_prog(file_list[index-1],debug,com,tm)
                        break 
                    else :
                        cprint('Wrong file index. Please try again.','red')
        except :
            cprint("Some error happended.",'red',attrs=['bold'])
    elif no == 1:
        run_prog(file_list[0],debug,com,tm)
    else :
        cprint('There is not any python or c++ file available.','yellow')

def if_run_type(msg):
    lt = msg.split()

    for key in run_keys:
        if key in lt:
            find_files(lt)
            return True
    return False



if __name__ == "__main__":
    msg = input('int->')
    # if_run_type(msg)