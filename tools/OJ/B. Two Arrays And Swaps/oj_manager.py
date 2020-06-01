import os
import subprocess
import json
from termcolor import colored as clr , cprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Cp_Problem:

    def fetch_problem(url = ''):
        try :
            if url == '':
                url = input('Enter the url : ')
            cprint('-'*55,'magenta')
            # os.system(cmd)
            cmd = 'oj-api get-problem ' + url
            cmd = list(cmd.split())

            cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            problem = json.loads(cp.stdout)
            # with open('problem.json','w') as f:
            #     f.write(cp.stdout)

            result = "Fetched problem Successfully"

            if problem['status'] == 'ok':
                # print('ok')
                alphabet = problem['result']['context']['alphabet']
                problem_name = problem['result']['name']
                problem_name = alphabet + '. '+problem_name
                # print(problem_name)
                if not os.path.isdir(problem_name):
                    os.mkdir(problem_name)
                try:

                    testcases = problem['result']['tests']
                    # print(testcases)
                    # if not os.path.isdir(problem_name):
                    # os.mkdir("'"+problem_name+"'"+'/test')
                    base = os.getcwd()
                    path = os.path.join(base,problem_name,"")

                    info = '{"name" : "$NAME" , "url" : "$URL" }'

                    info = info.replace('$NAME',problem_name)
                    info = info.replace('$URL',url)

                    with open(path+'.info','w') as f:
                        f.write(info)
                    
                    # print(path)
                    if not os.path.isdir(path+"test"):
                        os.mkdir(path+"test")
                    path = os.path.join(path,'test')
                    no = 1
                    for case in testcases:
                        # print(case)
                        fileName_in = 'Sample-'+str(no).zfill(2)+'.in'
                        fileName_out = 'Sample-'+str(no).zfill(2)+'.out'
                        # print(fileName_in)
                        no += 1
                        with open(os.path.join(path,fileName_in),'w') as fin:
                            fin.write(case['input'])
                        with open(os.path.join(path,fileName_out) ,'w') as fout:
                            fout.write(case['output'])
                    cprint(result,'green')

                except Exception as e:
                    print(e)
                
            else :
                result = "Wrong url."
                cprint(result,'result')

            cprint('-'*55,'magenta')
            
        except Exception as e:
            print('-'*55)
            # print(e)
            cprint("Sorry Can't Fetch.",'red')


class Cp_login:

    def login():
        try :
            cprint('Enter judge link : ','cyan',end='')
            oj = input()
            cprint('Enter your username : ','cyan',end='')
            username = input()
            cprint('Enter your password : ','cyan',end='')
            password = input()
            cmd = "USERNAME=$USERNAME PASSWORD=$PASS oj-api login-service " + oj + '> .status'
            cmd = cmd.replace("$USERNAME",username) 
            cmd = cmd.replace("$PASS",password) 
            # print(cmd)
            os.system(cmd)
            with open('.status','r') as f:
                cp = f.read()
            cp = json.loads(cp)
            if cp["result"]['loggedIn']:
                cprint("Logged in uccessfully....",'green')
            else :
                cprint("Login failed.",'red')
            os.remove('.status')
        except Exception as e:
            # print(e)
            cprint("Login failed. (Sad)",'red')
            pass

class Cp_Test:

    def test_it(self, file_name):
        try :
            pt='-'*20+file_name+'-'*20
            cprint(pt,'magenta')
            pt = (' '*17+"...Testing...")
            print(clr(pt,'blue'))
            cmd = "g++ "+file_name+" && oj t"
            # cmd = 'g++ '+file_name+' -o a.out'
            os.system(cmd)
            # cmd_all =[['g++',file_name,'-o','a.out'] , ['oj','t']]
            # cmd_all =[['oj','t']]
            # print(cmd)
            # for i in cmd_all:
            #     cp = subprocess.run(i, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # result = cp.stderr
            # result = result.replace('test failed',clr('test failed','red'))
            # result = result.replace('WA',clr('WA','red'))
            # result = result.replace('AC',clr('AC','green'))
            # print(result)
            pt = ('-'*20+'-'*len(file_name)+'-'*20)
            cprint(pt,'magenta')
        except Exception as e:
            print(e)
            cprint("Got some error. :(",'red')

    def find_files(self,file_name=''):

        file_list = []
        # print(file_name)
        supported_ext = ['cpp','py']
        for file in os.listdir(os.getcwd()):
            try :
                ext = file.rsplit(sep='.',maxsplit=1)
                for i in supported_ext:
                    if ext[1] == i:
                        if file_name in file:
                            file_list.append(file)
            except:
                pass
        # print(file_list)
        sz = len(file_list)
        if sz == 1:
            self.test_it(file_list[0])
        elif sz > 1:
            no = 1
            cprint("All the available files are given below.\n",'yellow')
            for file in file_list:
                pt = (' '*4+str(no)+') '+file)
                cprint(pt,'blue')
                no += 1
            cprint(' '*4+'0) Cancel operation','cyan')
            while True:
                cprint("Select the file index : ",'cyan',end='')
                index = int(input())
                if index == 0:
                    cprint("Testing operation cancelled.",'red')
                    break
                elif index < no:
                    self.test_it(file_list[index-1])
                    break
                else:
                    cprint("You have entered the wrong index.Please try again.",'red')
        else :
            cprint("NO FILE FOUND :(",'red')


class Cp_Submit:

    def submit_it(self,file_name):
        try :
            with open('.info','r') as f:
                info = f.read()
            info = json.loads(info)
            problem_name = info['name']
            url = info['url']
        except :
            cprint("Enter the problem url : ",'cyan',end='')
            url = input()
            problem_name = url
        pt = '-'*20+'Problem Description'+'-'*20
        cprint(pt,'magenta')
        cprint(' '*4+'Problem : ','yellow',end='')
        cprint(problem_name,'green')
        cprint(' '*4+'Problem url: ','yellow',end='')
        cprint(url,'yellow')
        cprint('-'*len(pt),'magenta')

    def find_files(self,file_name=''):

        file_list = []
        # print(file_name)
        supported_ext = ['cpp','py']
        for file in os.listdir(os.getcwd()):
            try :
                ext = file.rsplit(sep='.',maxsplit=1)
                for i in supported_ext:
                    if ext[1] == i:
                        if file_name in file:
                            file_list.append(file)
            except:
                pass
        # print(file_list)
        sz = len(file_list)
        if sz == 1:
            self.submit_it(file_list[0])
        elif sz > 1:
            no = 1
            cprint("All the available files are given below.\n",'yellow')
            for file in file_list:
                pt = (' '*4+str(no)+') '+file)
                cprint(pt,'blue')
                no += 1
            cprint(' '*4+'0) Cancel operation','cyan')
            while True:
                cprint("Select the file index : ",'cyan',end='')
                index = int(input())
                if index == 0:
                    cprint("Submitting operation cancelled.",'red')
                    break
                elif index < no:
                    self.submit_it(file_list[index-1])
                    break
                else:
                    cprint("You have entered the wrong index.Please try again.",'red')
        else :
            cprint("NO FILE FOUND :(",'red')


if __name__ == "__main__":
    # obj = Cp_Problem()
    # Cp_Problem.fetch_problem()
    # obj = Cp_Submit()
    # obj.find_files()
    # Cp_login.login()
    obj = Cp_Test()
    obj.find_files()
    # cprint("Enter something for testing purpose : ",'cyan',end='')
    # x = input()
    # cprint(x,'blue')
