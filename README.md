# AI virtual assitant 


It is a terminal-based virtual assistant especially made for competitive programming. It has a lot of features, including running python or c++ file, parsing problem set with test cases and test against all the cases in one click, test with brute force solution, and many more. It will help you to boost your programming skill and help you to do a good performance in the programming contest.

It can give voice reply and take your voice command. You can turn off or on these features. Basic settings can be easily changed from settings.py file.


## Programming Features

- [x] [Run c++ or python program](#run-python-or-cpp-program)
- [x] [parse problemset](#Parsing-Problem-from-online-judge)
- [x] [genarate file with template](#genarate-file-with-template)
- [x] [test code against testcases](#Test-solution)
- [x] [add testcase](#Add-testcase)
- [x] login online judges
- [x] submit code
- [x] bruteforce test solution
- [x] genarate gen.py automatcially
<!-- - [ ] parse contest -->
  
## More eaturess

- [x] voice output
- [x] voice input
- [x] reply using text
- [x] taking voice command
- [x] Speech Recognition
- [x] Ai to answer quesion
- [x] wiki search
- [x] google search
- [x] YouTube search
- [x] math calculation
- [x] goto any website
- [x] install something
- [x] learn from answer
- [x] download files
- [x] access from anywhere
<!-- - [ ] tell to remember something
- [ ] download youtube video
- [ ] arrange files -->
<!-- - [ ] coding environment
- [ ] play game
- [ ] cheak weather
- [ ] todo_function 
- [ ] gmail client
- [ ] git 
- [ ] system update && upgrade
- [ ] Search facility -->



## Run python or cpp program

Any python or c++ files from the current directory can be run using one command. The command is given below,
> jarvis -r "file_name"

If you don't specify the file_name, it will list all the available python and c++ files in the current directory and you have to choose.

![Running program](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20run%20program.png)

 ## Parsing Problem from online judge

 Problems can be parsed by given command,

> jarvis -cp parse

Here -cp represent competitive programming,

After giving the command it will ask for the problem URL. Just give the URL,it will parse the problem. There will be created a folder according to the problem name. And it will contain all the sample test cases of that problem.

![parsing-problem](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/parsing%20problem.png)

## Genarate File with Template

You can easily generate your file with the template by the given command,

> jarvis -cp -t "file_name"

If you don't specify the file_name it will be automatically created as "sol.cpp". You can create a python or c++ file.

You have to specify your template path. Just open settins/compiler.py file and find template_path and give your path for c++ and python.

You can use variables in your template file which you will be replaced,

variable available,

- $%CODER%$
- $%DATE_TIME%$

$%CODER%$ will be replaced by your name. It can be specified in coder_name in settings/compiler.py file.

$%DATE_TIME%$ will be replaced by your file creating time and date.

Example :

Template file,

```c++

/**
 *    author:  $%CODER%$ 
 *    created: $%DATE_TIME%$
**/

#include<bits/stdc++.h>
using namespace std;

int main(){

	

    return 0;
}

```

Genarated file,

```c++

/**
 *    author:  Saurav Paul 
 *    created: Jun 06 2020 9:05 PM
**/

#include<bits/stdc++.h>
using namespace std;

int main(){

	

    return 0;
}

```

![genarating file](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/template_c%2B%2B.png)

## Test solution

After parsing problem set, the solution can be tested by the given command,

> Jarvis -cp test


It will run all the sample and custom cases from the test folder(Test folder contains all the sample cases after parsing problem set) and check whether your solution is passed. It will show the taken time for running each case. If your code failed any test cases it will show the differences between the correct answer and your output. If every case passed then it will show passed.

It is not necessary to have a parsed problem set for using this command. You can make a test folder and add input(.in) and output(.out) case into that folder and then run this command.


![Test-solution](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20testing%20program.png)

## Add Testcase

Adding testcase is really very easy. Just give the command,

> Jarvis -cp add

Yes, that simple :sunglasses: .

It will ask for input and output for your new case. Then it will add this case.
