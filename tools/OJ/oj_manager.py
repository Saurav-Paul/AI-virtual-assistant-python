import os
import subprocess
import json

class Cp:

    def login():
        try :
            oj = input("Enter judge link : ")
            username = input("Enter your username : ")
            password = input("Enter the password : ")
            cmd = "USERNAME=$USERNAME PASSWORD=$PASS oj-api login-service " + oj + '> .status'
            cmd = cmd.replace("$USERNAME",username) 
            cmd = cmd.replace("$PASS",password) 
            print(cmd)
            os.system(cmd)
            with open('.status','r') as f:
                cp = f.read()
            cp = json.loads(cp)
            if cp["result"]['loggedIn']:
                print("Logged in uccessfully....")
            else :
                print("Login failed.")
            os.remove('.status')
        except Exception as e:
            # print(e)
            print("Login failed. (Sad)")
            pass

    def fetch_problem(url = ''):
        try :
            if url == '':
                url = input('Enter the url : ')
            print('-'*55)
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

                    with open(path+'.info','w') as f:
                        f.write(cp.stdout)
                    
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

                except Exception as e:
                    print(e)
                
            else :
                result = "Wrong url."

            print('-'*55)
            print(result)
        except Exception as e:
            print('-'*55)
            print(e)
            print("Sorry Can't Fetch.")

    def test_program():

if __name__ == "__main__":
    Cp.fetch_problem()
