import requests

def check_internet():
    try :
        requests.get('https://www.google.com/').status_code
        return True 
    except:
        return False



if __name__ == "__main__":
    print(check_internet())