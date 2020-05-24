import  wolframalpha


def ask_question(question) :
    api_key = 'GLHKQ7-R5V9E6GU3Y'
    client = wolframalpha.Client(api_key)
    res = client.query(question)
    answer = next(res.results).text

    return answer 

