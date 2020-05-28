try:
    import os
    from settings.compiler import compiler
except expression as e:
    pass

run_keys = ['-r', '-run']
files_ext = ['cpp','py']


def find_files(lt):
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
                if w in file :
                    try :
                            ext = file.rsplit(sep='.',maxsplit=1)
                            if ext[1] in files_ext:
                                file_list.append(file)
                    except :
                        pass
    if len(file_list) > 1:
        print('Select the file -> ')
        no = 1
        for i in file_list:
            print(' '*5+no") "+ i)
        while True :
            try :
                index = input('Enter the file number :')
                run_prog(file_list[])

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