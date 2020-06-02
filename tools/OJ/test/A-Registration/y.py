import os

with open('first_file','r') as f1, open('second_file','r') as f2:
    x = f1.read()
    y = f2.read()

if x == y:
    print("Passed")
else :
    print('output =')
    print(x)
    print('Excepted =')
    print(y)
if 1 :
    print("Congratulations")

