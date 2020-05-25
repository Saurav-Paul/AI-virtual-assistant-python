
from fuzzywuzzy import fuzz

def match_string(msg,orginal,no = 1):
    if no == 1:
        return max(fuzz.WRatio(msg,orginal),fuzz.token_sort_ratio(msg,orginal))
    elif no == 2:
        return fuzz.WRatio(msg,orginal)
    elif no == 3:
        return fuzz.ratio(msg,orginal)
    else:
        return fuzz.token_sort_ratio(msg,orginal)

x = 'what is the tell me the time'
y = 'can you tell me the time'

print(match_string(x,y))
print(match_string(y,x))
print(match_string(x,y,2))
print(match_string(x,y,3))
