import os
from system.path import getpath

def get_template(fileName):
    path = getpath(__file__)
    writen = ''
    with open(os.path.join(path,fileName),'r') as f:
        writen = f.read()

    return writen

if __name__ == "__main__":
    print(get_template('cpp_template.txt') )
    print(get_template('py_template.txt') )