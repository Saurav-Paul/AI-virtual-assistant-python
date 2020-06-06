# AI virtual assitant 


It is a terminal-based virtual assistant especially made for competitive programming. It has a lot of features, including running python or c++ file, parsing problem set with test cases and test against all the cases in one click, test with brute force solution, and many more. It will help you to boost your programming skill and help you to do a good performance in the programming contest.

It can give voice reply and take your voice command. You can turn off or on these features. Basic settings can be easily changed from settings.py file.


## Programming Features

- [x] [parse problemset](#Parsing-Problem-from-online-judge)
- [x] [genarate file with template](#genarate-file-with-template)
- [x] test code against testcases
- [x] add testcase
- [x] login online judges
- [x] submit code
- [x] run program
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



 ## Parsing Problem from online judge

 Problems can be parsed by given command,

> jarvis -cp parse

Here -cp represent competitive programming,

After giving the command it will ask for the problem URL. Just give the URL,it will parse the problem. There will be created a folder according to the problem name. And it will contain all the sample test cases of that problem.

![parsing-problem](https://github.com/Saurav-Paul/Saurav-Paul.github.io/blob/master/images/parsing%20problem.png)

## Genarate File with Template

You can easily genarate your file with template by the given command,

> jarvis -cp -t "file_name"

If you don't specify the file_name it will be automatically created as "sol.cpp" . You can create python or c++ file.

You have to specify your template path. Just open settins/compiler.py file and find template_path and give your path for c++ and python.

You can use variable in your template file which you will be replaced,

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