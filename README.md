# AI virtual assitant 


It is a terminal-based virtual assistant especially made for competitive programming. It has a lot of features, including running python or c++ file, parsing problem set with test cases and test against all the cases in one click, test with brute force solution, and many more. It will help you to boost your programming skill and help you to do a good performance in the programming contest.

It can give voice reply and take your voice command. You can turn off or on these features. Basic settings can be easily changed from settings/settings.py file.

![Welcome](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20welcome%20screen.png)

## Programming Features

- [x] [Run c++ or python program](#run-python-or-cpp-program)
- [x] [Competitive Companion Support](#)
- [x] [parse problemset](#Parsing-Problem-from-online-judge)
- [x] [generate file with template](#generate-file-with-template)
- [x] [test code against testcases](#Test-solution)
- [x] [add testcase](#Add-testcase)
- [x] [bruteforce test solution](#Test-solution-with-bruteforce)
- [x] [Generate-testcase-genarator-automatically](#Generate-testcase-genarator-automatically)
- [x] [login online judge](#login-and-submit-to-online-judge)
- [x] [submit code](#Login-and-Submit-to-online-Judge)
- [x] [Parse contest](#parsing-contest)
<!-- - [ ] parse contest -->
  
## Other Features

- [x] [Speaking Capability](#speaking-and-voice-command)
- [x] [taking voice command](#speaking-and-voice-command)
- [x] [Speech Recognition](#speech-recognition)
- [x] [Ai to answer quesion](#AI-to-answer-question)
- [x] [goto any website](#goto-website)
- [x] [solving math](#solve-math)
- [x] [wiki search](#wiki-search)
- [x] [google search](#search-google)
- [x] [YouTube search & play videos](#search-youtube)
- [x] [install python module](#)
- [x] [learn from answer](#)
- [x] [download files](#download-files)
- [x] [access from anywhere](#)
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



---

### [click here to go to Installation](#Installation)
---

## Run python or cpp program

Any python or c++ files from the current directory can be run using one command. The command is given below,
> jarvis -r "file_name"

If you don't specify the file_name, it will list all the available python and c++ files in the current directory and you have to choose.

![Running program](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20run%20program.png)

 ## Parsing Problem from online judge


Competitive Companion support makes parsing problems really very easy. Just give the command,

> jarvis -cp parse

or,

> jarvis -cp listen

Here -cp represent competitive programming,

It will start listening, then you can just click the competitive companion browser extension. It will parse the problem.

After parsing there will create a new folder according to the contest name and in that folder will be another folder according to the problem name. And it will contain all the sample test cases of that problem.

![parsing-problem](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20parse%20using%20competitive%20companion.png)

Also, the problem can be parsed without competitive companion though I don't recommend this. the command is given below,

> jarvis -cp problem


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


## Parsing contest

Parsing contest is the same as parsing problems using the competitive companion. Just write command,

> jarvis -cp parse

then it will start listening, then just open the contest link and click the browser extension, it will parse all the problems and create a folder for each contest with their test cases.


Also, the contest can be parsed without competitive companion though I don't recommend this. the command is given below,

> jarvis -cp contest


It will ask for the contest link. Then it will parse all the problems.

---

## Speaking and voice command

This ai can speak with you. It will reply in voice and text both. You can toggle them from settings/settings.py file.

You can also give voice commands. But you have turned this feature on from settings/settings.py file.

## Speech Recognition

Jarvis can recognize the speech using google voice recognition API.

## AI to answer question

As the name suggests you can have chat with it. You can ask jarvis a question, it will reply to you with his intelligence.

## goto website

To be honest this is one of my favorite features. You can ask Jarvis to go to any websites as with wish. It will open that in your browser.

The command is given below,

>Jarvis goto "website name"

It will open codeforces contest page for you. Basically, you can ask him to go to any website you want.

It is okay to make some typing mistakes while writing a website name. It will still find it out.

![goto-demo](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20goto.png)



## Solve Math

This ai can solve simple math. Just ask him to solve it will solve it for you.

The command is given below,

> jarvis solve ( "math" )

![math-solving-demo](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/jarvis%20math%20solving%20.png)

## wiki search

For searching something on wikipedia the command is given below,

> jarvis search wikipedia "your text"

## Search google

For searching something on google the command is given below,

> jarvis search google "your text"

## Search youtube

For searching something on youtube the command is given below,

> jarvis search youtube "your text"

## Play video on youtube

> jarvis play youtube "song name"

## Download Files

For downloading the command is given below,

> jarvis download

Then it will ask for the download link.
        
---
# Installation

Installation is simple, just follow these steps...

1. Clone or download this repository
2. Open and find setup.py
3. Run setup.py using your python3 , It will install all the dependency needed for this project.
It might take several minutes.
4. For accessing virtual assistant from any place, add this function to your ~/.bashrc, In my case, I like to call by the name "jarvis". You can replace the name jarvis by whatever name you want.


```bash
jarvis () {
python3 {path to the project folder}/run.py $PWD -arg $@
}
```

It will work fine in Linux. It should also work on Mac Os.
But unfortunately, it has some issues running on Windows(Because cmd has some problems). But still, it can be run on windows using windows subsystem for Linux.

### Issues

- If you face some problems while installation. In that case, you have to install these package manually. It occurs because some python module need a different version for a different distribution.

- If your voice command does not work properly, you have to install pyaudio manually.



### If you want to contribute on this project you are welcome.
