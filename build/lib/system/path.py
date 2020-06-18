import os

def getpath(file):
    x = os.path.dirname(os.path.abspath(file))
    return os.path.join(x,'')