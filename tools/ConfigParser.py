import configparser

class ConfigParser_manager:

    def read(self,file_name,section=''):
        config = configparser.ConfigParser()
        config.read(file_name)
        if section != '':
            return dict(config[section])
        
        return config

    def update(self,file_name,value,section='user'):
        config = configparser.ConfigParser()
        config = self.read(file_name)

        config[section] = value

        with open(file_name , 'w') as f:
            config.write(f)


if __name__ == "__main__":
    obj = ConfigParser_manager()
    # obj.update('Test.conf')
    dic = obj.read('Test.conf',section='user')
    print(dic)
    dic['name'] = 'Bot'
    obj.update('Test.conf',dic,section='user')
    print(getpath(__file__))



