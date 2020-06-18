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
    'Environment :: Console',
    # Indicate who your project is intended for
    'Intended Audience :: End Users/Desktop',

    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',
    ],

    keywords='ai virtual assitant',
    packages=find_packages(),
    include_package_data=True,
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
        'plyer',
        'psutil',
        'pyfiglet',
        'python-Levenshtein',
        'python-Levenshtein-wheels',
        'requests',
        'tcgen',
        'termcolor',
        'tqdm',
        'wget',
        'wikipedia-api',
        'wolframalpha',
    ],
    
    entry_points={
        'console_scripts': [
            'ai = run.run:start',
            'jarvis = run.run:start',
            'cp = run.run:cp_start',
            
        ],
    },
)
