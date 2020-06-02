from termcolor import cprint
import os , time
import subprocess

class Cp_my_tester:

    def sub_process(self,cmd,value):

        x = subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        with x.stdin as f:
            f.write(value.encode())
            result = (x.communicate()[0]).decode('utf-8')
            print(result)
        
        return result

    def test(self,file_name):
        path = os.getcwd()

        if not os.path.isdir('test'):
            cprint("Test folder not available.",'red',attrs=['bold'])
            return
        
        file_path = os.path.join(path,'test')
        lt = os.listdir(file_path)
        print(lt)
        if len(lt) == 0 :
            cprint('Not test file available.')
            return 
        cmd = f'g++ {file_name} -o test.out'
        t = time.time()
        os.system(cmd)
        t = time.time() - t
        print(f'Compilation time {t}')
        passed = 0 
        failed = 0
        for file in lt:
            ext = file.rsplit(sep='.',maxsplit=1)
            print(f'file = {ext}')
            if ext[1] == 'in':
                out = ext[0] + '.out'
                if os.path.isfile(os.path.join(file_path,out)):
                    print(f'testing {file} with {out}')
                    with open(os.path.join(file_path,file),'r') as f:
                        value = f.read()
                    t = time.time()
                    result = self.sub_process(['./test.out'],value)
                    print(f'Time taken = {time.time()-t}')
                    print('code :\n',result)
                    with open(os.path.join(file_path,out)) as f:
                        ans = f.read()
                    print('Expected :\n',ans)
                    if result == ans:
                        cprint('Passed','green')
                        passed += 1
                    else :
                        cprint('WA','red')
                        failed += 1
                else:
                    print(f'{out} not found.')
        if passed + failed == 0 :
            cprint('No test data available','red')
            return
        cprint(f'Status : {passed}/{passed+failed}','yellow')
        if failed == 0:
            cprint("Passed....",'green')
        else :
            cprint("Failed....",'red')


if __name__ == "__main__":
    obj = Cp_my_tester()
    obj.test('test1.cpp')