from termcolor import cprint
import subprocess
import json
import os
import time

class Cp_Problem:

    def fetch_problem(self,url = ''):
        try :
            cprint(' '*17+'...Parsing Problem...'+' '*17,'blue')
            if url == '':
                cprint('Enter the url : ','cyan',end='')
                url = input()
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
                problem_name = alphabet + '-'+problem_name
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



class Cp_contest():



    def fetch_problem(self,url = ''):
        try :
            cmd = 'oj-api get-problem ' + url
            cmd = list(cmd.split())

            cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            problem = json.loads(cp.stdout)
            # with open('problem.json','w') as f:
            #     f.write(cp.stdout)

            

            if problem['status'] == 'ok':
                # print('ok')
                try :
                    alphabet = problem['result']['context']['alphabet']
                except:
                    alphabet = ''
                problem_name = problem['result']['name']
                problem_name = alphabet + '-'+problem_name
                # print(problem_name)
                if not os.path.isdir(problem_name):
                    os.mkdir(problem_name)
                try:
                    result = f"  * Fetched '{problem_name}'' Successfully"
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

            
            
        except Exception as e:
            print('-'*55)
            # print(e)
            cprint("Sorry Can't Fetch.",'red')

    def parse_contest(self,url=''):
        try :

            url = 'https://codeforces.com/contest/1343'
            # url = 'https://atcoder.jp/contests/abc167/tasks/abc167_a'
            cprint(' '*17+'...Parsing Contest...'+' '*17,'blue')
            if url == '':
                cprint('Enter the url : ','cyan',end='')
                url = input()
            cprint('-'*55,'magenta')
            # os.system(cmd)
            t = time.time()
            cmd = 'oj-api get-contest ' + url
            cmd = list(cmd.split())

            cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            contest = json.loads(cp.stdout)
            # with open('problem.json','w') as f:
            #     f.write(cp.stdout)

            result = "\tFetched Contest info."
            if contest['status'] == 'ok':
                cprint(result,'green')
            else :
                cprint("Sorry contest can't be fetched. Sorry sir. :( ",'red')
                return
            # print(contest)
            path = os.getcwd()
            # print(path)
            contest_name = contest['result']['name']
            cprint(f' # Contest name : {contest_name}','green')

            if not os.path.isdir(contest_name):
                os.mkdir(contest_name)
                # cprint('Contest folder created.','green')


            print()
            os.chdir(os.path.join(path,contest_name))
            # print(os.getcwd())
            problem = contest['result']['problems']
            with open('t.json','w') as f:
                f.write(str(contest))

            for key in problem:
                url = key['url']
                # print(url)
                # Cp_Problem.fetch_problem(url)
                self.fetch_problem(url=url)

            os.chdir(path)
            # print(os.getcwd())
            print()
            cprint(" # Done. :D",'green')
            cprint(f" # Time taken {time.time()-t:.4f} sec.",'blue')
            cprint('-'*55,'magenta')
        
        except Exception as e:
            cprint(e,'red')





if __name__ == "__main__":
    obj = Cp_contest()
    obj.parse_contest()