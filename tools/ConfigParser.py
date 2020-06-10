import configparser

class ConfigParser_manager:

    def read(self,file_name,section=''):
        try :
            config = configparser.ConfigParser()
            config.read(file_name)
            if section != '':
                return dict(config[section])
            
            return config
        except :
            return ''

    def update(self,file_name,value,section='user'):
        config = configparser.ConfigParser()
        config = self.read(file_name)

        config[section] = value

        with open(file_name , 'w') as f:
            config.write(f)


if __name__ == "__main__":
    obj = ConfigParser_manager()
    # obj.update('Test.conf')

    section = 'demo'
    dic = obj.read('Test.conf',section=section)
    print(dic)
    dic[section] = 'Saurav'
    obj.update('Test.conf',dic,section=section)
    # print(getpath(__file__))



