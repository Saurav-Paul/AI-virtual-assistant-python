from termcolor import cprint

credit_keys = ['about','credit','credits']




def credits():
    pt = '-'*22+'Credits'+'-'*22
    cprint(pt,'magenta')
    print()
    s = """\tThis is a command line virtual assitant for competitive programming.
    \tThis software is written by Saurav Paul.

    \tBiography:
    \tName = Saurav Paul
    \tEmail = sauravpaul.sunny@gmail.com
    \tWebsite = https://saurav-paul.github.io/
    """
    cprint(s,'green')
    print()
    cprint('-'*len(pt),'magenta')

def if_credit_type(msg):
    lt = msg

    for key in credit_keys:
        if key == lt:
            credits()
            return True
    return False

