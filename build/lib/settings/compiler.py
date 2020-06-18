from tools.ConfigParser import ConfigParser_manager as CM
from system.path import getpath
import os
from termcolor import cprint
from settings.settings import bot

positive = ['yes','1','true']

compiler = {
    "c++" : "g++ '{filename}' -o '{executable}' && ./'{executable}'",
    "c++ debug" : "g++ -std=c++17 -O2 -DPAUL -Wshift-overflow=2  -Wshadow  -Wall '{filename}' -o '{executable}' && ./'{executable}'",
    "python" :"python3 '{filename}'",

}

template_path = {
    'c++' :'/media/saurav/Programming/GIthub/Code-Lab/geany/ai_template.cpp',
    'python':'/media/saurav/Programming/GIthub/Code-Lab/geany/ai_template.py',
}

coder_name = bot['boss']
competitive_companion_port = 8080

parse_problem_with_template = True # If true, after parsing all the codes will contain a file name sol.cpp (with your template)


conf_path = os.path.join(getpath(__file__),'settings.conf')

try :

    section = 'cp'
    obj = CM()
    x = obj.read(conf_path,section = section)
    coder_name = x['coder_name']
    if coder_name == "${boss}":
        coder_name = bot['boss']

    competitive_companion_port = int(x['competitive_companion_port'])
    parse_problem_with_template = x['parse_problem_with_template']
    if parse_problem_with_template.lower() in positive:
        parse_problem_with_template = True
    else:
        parse_problem_with_template = False

    section = 'template_path'
    x = obj.read(conf_path,section= section)

    template_path['c++'] = x['cpp']
    template_path['python'] = x['python']

    section = 'compiler'
    x = obj.read(conf_path,section)

    compiler['c++'] = x['cpp']
    compiler['c++ debug'] = x['cpp_debug']
    compiler['python'] = x['python']



except Exception as e:
    print(e)
    cprint("Settings error.",'red')

def update_ccp(port):
    global competitive_companion_port
    competitive_companion_port = port

def update_tp(x):
    global template_path
    template_path = x

def update_compiler(x):
    global compiler
    compiler = x