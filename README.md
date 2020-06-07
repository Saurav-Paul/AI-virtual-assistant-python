# AI virtual assitant 


It is a terminal-based virtual assistant especially made for competitive programming. It has a lot of features, including running python or c++ file, parsing problem set with test cases and test against all the cases in one click, test with brute force solution, and many more. It will help you to boost your programming skill and help you to do a good performance in the programming contest.

It can give voice reply and take your voice command. You can turn off or on these features. Basic settings can be easily changed from settings.py file.


## Programming Features

- [x] [Run c++ or python program](#run-python-or-cpp-program)
- [x] [parse problemset](#Parsing-Problem-from-online-judge)
- [x] [generate file with template](#generate-file-with-template)
- [x] [test code against testcases](#Test-solution)
- [x] [add testcase](#Add-testcase)
- [x] [bruteforce test solution](#Test-solution-with-bruteforce)
- [x] [Generate-testcase-genarator-automatically](#Generate-testcase-genarator-automatically)
- [x] [login online judges](#login-and-submit-to-online-judge)
- [x] [submit code](#Login-and-Submit-to-online-Judge)

<!-- - [ ] parse contest -->
  
## More Featuress

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

## Generate File with Template

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

## Test solution with bruteforce

If you have any doubts about your optimal solution, then you can write a brute-force solution and write a random test case generator. You can test your optimal solution with a brute force solution using a random test case.

For that, you need three files.

    1. Main solution
    2. Bruteforce solution
    3. Testcase Generator (My AI can generate it automatically)

Then run this command,

> Jarvis -cp brute

It will ask for the number of times you want to generate random test cases and test solutions (Stress).

It will match output with the brute-force solution's output. If it failed, it will show the differences and ask you to add this to your test case so that you can test this later. Otherwise, it will show Accepted :smile: .

![bruteforce-solution](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20bruteforce.png)

## Generate testcase genarator automatically

Test case generator can be generated using the given command,

> Jarvis -cp gen

It will analyze all the sample cases and generate gen.py(Test case generator) automatically. Yes, sometimes it might fail (In case of complex test cases).
In this case, you have to write a generator manually (You can write in python or c++).

There is also one command, to generate gen.py, brute.cpp(empty file) and sol.cpp(with your template). The command is given below,

> Jarvis -cp setup

![testcase generator](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20automatically%20setup.png)

## Login and submit to online Judge

For login write the given command,

> Jarvis -cp login

It will ask for a judge link, your username, and a password.

For submitting code just write the given command,

> Jarvis -cp submit

N.B.: I have used online-judge-api-client for login and submitting codes.

![login and submitting demo](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20login%20and%20submit.png)