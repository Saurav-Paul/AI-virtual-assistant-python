from setuptools import find_packages , setup
import system.__about__ as version



from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=version.__package_name__,
    version=version.__version__,
    author=version.__author__,
    author_email=version.__email__,
    url=version.__url__,
    license=version.__license__,
    description=version.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',


    classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Programmer',
    'Topic :: Competitive Programmer :: ai virtual assitant',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',
    ],

    keywords='ai virtual assitant',
    packages=find_packages(),
    package_data = {
    # If any package contains *.txt or *.rst files, include them:
    '': ['*.conf', '*.json', '*.txt', '.learnt'],
    },


    python_requires='>=3.5',
    install_requires=[
       'beautifulsoup4',
        'fuzzywuzzy',
        'google',
        'lxml',
        'online-judge-api-client',
        'online-judge-tools',
        'pickle-mixin',
        'ply',
        'plyer',
        'psutil',
        'PyAudio',
        'pyfiglet',
        'python-Levenshtein',
        'python-Levenshtein-wheels',
        'pyttsx3',
        'requests',
        'SpeechRecognition',
        'tcgen',
        'termcolor',
        'tqdm',
        'wget',
        'wikipedia',
        'wolframalpha',

    ],
    
    entry_points={
        'console_scripts': [
            'ai = run:start',
            'cp = system.fun:start',
        ],
    },
)