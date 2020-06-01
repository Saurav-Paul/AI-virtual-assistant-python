#!/usr/bin/env python3

# import socket
# import json

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


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('',9000))
reuslt = ''

while True:
    data = s.recv(8)
    if len(msg) <= 0 :
        break 
    reuslt += data.decode('utf-8')

print(reuslt)