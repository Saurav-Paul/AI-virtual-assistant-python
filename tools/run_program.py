try:
    import os
    from settings.compiler import compiler
    import tqdm
except expression as e:
    pass


run_keys = ['-r', '-run']
files_ext = ['cpp','py']

def run_prog(file_name , debug = False):
    
    print("Running the ",file_name+'......')
    ext = file_name.rsplit(sep='.',maxsplit=1)
    if ext[1] == 'cpp':
        if debug :
            cmd = compiler['c++ debug']
        else :
            cmd = compiler['c++']

        cmd = cmd.replace('{filename}',file_name)
        cmd = cmd.replace('{executable}',ext[0])
        print('-'*23+file_name+'-'*22+'\n') 
        try :
            os.system(cmd)
        except:
            print("Sorry sir can't run.")
        print('\n'+'-'*23+'-'*len(file_name)+'-'*22) 
    elif ext[1] == 'py':
        cmd = compiler['python']
        cmd = cmd.replace('{filename}',file_name)
        print('-'*23+file_name+'-'*22) 
        try :
            os.system(cmd)
        except:
            print("Sorry sir can't run.")
        print('-'*23+'-'*len(file_name)+'-'*22) 
    else :
        print('Unknown file format.')


def find_files(lt):
    debug = False
    if '-d' in lt:
        debug = True
        try :
            lt.remove('-d')
        except :
            pass 
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
        print('Select the file -> ')
        no = 1
        for i in file_list:
            print(' '*5+str(no)+") "+ i)
            no += 1
            
        try :
                while True :
                    index = int(input('Enter the file number :'))
                    if index > 0 and index < no :
                        run_prog(file_list[index-1],debug)
                        break 
                    else :
                        print('Wrong file index. Please try again.')
        except :
            raise ValueError('Some value error happend')
    elif no == 1:
        run_prog(file_list[0],debug)
    else :
        print('There is not any python or c++ file')

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