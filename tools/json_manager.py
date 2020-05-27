try :
    import json
except Exception as e:
    pass


class JsonManager:
    """ It will loads data and dumps data into json. Written By Saurav Paul"""

    def json_read(json_file):
        try :
            with open(json_file, "r") as read_file:
                data = json.load(read_file)
            return data
        except Exception as e:
            print(e)
    def json_write(json_file,data={}):
        try :
            with open(json_file, "w") as write_file:
                json.dump(data, write_file)

            json_string = json.dumps(data)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    x = JsonManager.json_read('tools/AI/conversations.json')
    print(x)
    for i in  x:
        print(i)
        print(x[i])
        for j in x[i]:
            print(x[i][j])