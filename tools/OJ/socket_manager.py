#!/usr/bin/env python3

import socket
import json
from termcolor import cprint
import threading
import os


# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 9999        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             result = (data.decode('utf-8'))
#             print('result : ',result)
            
#             if not data:
#                 print('breaked')
#                 break
#             conn.sendall(data)
#     # print(data.decode('utf-8'))
    


class cp_extension:

    HOST = '127.0.0.1'
    PORT = 9999   

    def rectify(self,s):
        try:
            i = s.find('{')
            s = s[i:]
            return s
        except Exception as e:
            return ''

    def fetch_problem(self,url = ''):
        try :
            # cprint(' '*17+'...Parsing Problem...'+' '*17,'blue')
            # if url == '':
            #     cprint('Enter the url : ','cyan',end='')
            #     url = input()
            # cprint('-'*55,'magenta')
            # # os.system(cmd)
            # cmd = 'oj-api get-problem ' + url
            # cmd = list(cmd.split())

            # cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # problem = json.loads(cp.stdout)
            # # with open('problem.json','w') as f:
            # #     f.write(cp.stdout)

            

            if problem['status'] == 'ok':
                # print('ok')
                try :
                    alphabet = problem['result']['context']['alphabet']
                except :
                    alphabet = ''
                problem_name = problem['result']['name']
                problem_name = alphabet + '-'+problem_name
                # print(problem_name)
                if not os.path.isdir(problem_name):
                    os.mkdir(problem_name)
                try:
                    result = f"\tFetched '{problem_name}' Successfully"
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

    def create(self,problem):
        # print("here")
        try :
            problem = self.rectify(problem)
            dic = json.loads(problem)
            # cprint(dic,'yellow')

            problem_name = dic['name']
            contest_name = dic['group']
            url = dic['url']
            # cprint(f'{problem_name} : {contest_name} : {url} ','cyan')
            base = os.getcwd()
            base_name = os.path.basename(base)
            # cprint(f'{base_name}','cyan')
            if base_name != contest_name:
                if not os.path.isdir(contest_name):
                    os.mkdir(contest_name)
                    # print("directory created")
                os.chdir(os.path.join(base,contest_name))
            
            # print(os.getcwd())
            if not os.path.isdir(problem_name):
                os.mkdir(problem_name)
                # print("problem created")
            
            info = '{"name" : "$NAME" , "url" : "$URL" }'

            info = info.replace('$NAME',problem_name)
            info = info.replace('$URL',url)

            path = os.path.join(os.getcwd(),problem_name,"")
            # print(path)
            with open(path+'.info','w') as f:
                f.write(info)
            
            testcases = dic['tests']
            # print(testcases)
            # return
            no = 1
            if not os.path.isdir(path+"testcases"):
                os.mkdir(path+"testcases")
            path = os.path.join(path,'testcases')

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
            # cprint(result,'green')
            # print(info)
            cprint(f'{problem_name} fetched successfully.','green')
            os.chdir(base)

        except Exception as e:
            cprint("Can't fetch.",'red')
            

    def listen(self):

        x = ''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST,self.PORT))
            cprint("Listening....",'yellow')
            timeout = 20
            cnt = 0
            ok = True
            while ok:
                try :
                    s.listen()
                    s.settimeout(timeout)
                    timeout = 2
                    conn , addr = s.accept()
                    with conn:
                        # cprint("Connected...",'green')
                        while True:
                            data = conn.recv(1024)
                            result = (data.decode('utf-8'))
                            # result = self.rectify(result)
                            
                            # cprint(result,'cyan')

                            if not data :
                                cnt += 1
                                break
                            else:
                                t = threading.Thread(target=self.create,args=(result,))
                                t.start()
                                x = result
                except :
                    ok = False
        cprint(f'Total {cnt} problems fetched.','blue')
        x = self.rectify(x)
        # print(x)
        # p = threading.Thread(target=self.create,args=(x,))
        # p.start()
        # p.join()


if __name__ == "__main__":
    obj = cp_extension()
    obj.listen()

# import socket
# c = socket.socket()

# c.bind((HOST,PORT))
# print(c.recv(1024).decode())



# An example script to connect to Google using socket 
# programming in Python 
# import socket # for socket 
# import sys  
  
# try: 
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#     print ("Socket successfully created")
# except socket.error as err: 
#     print ("socket creation failed with error %s" %(err) )
  
# # default port for socket 
# port = 9998
  
# try: 
#     host_ip = socket.gethostbyname('www.google.com') 
# except socket.gaierror: 
  
#     # this means could not resolve the host 
#     print ("there was an error resolving the host")
#     sys.exit() 
  
# # connecting to the server 
# s.bind((HOST, PORT)) 
  
# print ("the socket has successfully connected to google.")


# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('',9000))
# reuslt = ''

# while True:
#     data = s.recv(8)
#     if len(msg) <= 0 :
#         break 
#     reuslt += data.decode('utf-8')

# print(reuslt)