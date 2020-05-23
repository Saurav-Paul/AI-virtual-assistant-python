import wikipedia
#print(wikipedia.summary("Mathematics"))
#wikipedia.search("Mathematics")
from speak import speak
results = wikipedia.page("What is semiconductor").content.split(sep='.')
msg = ""
i = 0
for line in results :
    if i == 4 :
        break
    msg += line
    i += 1

print(msg)
speak(msg)