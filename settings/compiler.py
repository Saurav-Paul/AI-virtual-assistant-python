

compiler = {
    "c++" : "g++ {filename} -o {executable} && ./{executable}",
    "c++ debug" : "g++ -std=c++17 -O2 -DPAUL -Wshift-overflow=2  -Wshadow  -Wall {filename} -o {executable} && ./{executable}",
    "python" :"python3 {filename}",

}