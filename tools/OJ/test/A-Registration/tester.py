from termcolor import cprint 
import os , time
import subprocess
from itertools import zip_longest

TLE = 4

class Cp_my_tester:


    def diff_print(self,name,value):
        print('  '+name+' :')
        for x in value:
            x = '  '+ x
            print(x)
        
    def different(self,value,output,expected,case):
        x = output.split('\n')
        y = expected.split('\n')
        i = value.split('\n')
        pt  = '  '+'-'*5+'Problem Found in '+case+'-'*5
        cprint(pt,'yellow')
        # print('Input :')
        # print(value)
        self.diff_print('Input',i)
        self.diff_print('Output',x)
        self.diff_print('Expected',y)
        # print('Output :')
        # print(output)
        # print("Expected :")
        # print(expected)
        print("  Difference :")
        for wx,wy in zip_longest(x,y,fillvalue=''):
            print('  ',end='')
            for o , e in zip_longest(wx,wy,fillvalue=''):
                if(o == e):
                    cprint(o,'green',end='')
                else :
                    cprint(o,'red',end='')
                    cprint(e,'yellow',end='')
            print()
        cprint('  '+'-'*(len(pt)-2),'yellow')

    def sub_process(self,cmd,value):
        tle = False
        try :
            x = subprocess.call(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,timeout=TLE)
            with x.stdin as f:
                f.write(value.encode())
                result = (x.communicate()[0]).decode('utf-8')
        except :
            result = "$TLE$"
            tle = True
        return (result,tle)

    def test(self,file_name):
        path = os.getcwd()

        pt='-'*20+file_name+'-'*20
        cprint(pt,'magenta')
        pt = (' '*17+"...Testing...")
        cprint(pt,'blue')
        print()

        if not os.path.isdir('test'):
            cprint("Test folder not available.",'red',attrs=['bold'])
            return
        
        file_path = os.path.join(path,'test')
        lt = os.listdir(file_path)
        # print(lt)
        if len(lt) == 0 :
            cprint('Not test file available.')
            return 
        cmd = f'g++ {file_name} -o test.out'
        t = time.time()
        os.system(cmd)
        t = time.time() - t
        t = '{:.4f}'.format(t)
        pt = (f' #  Compilation time {t} s')
        cprint(pt,'blue')
        passed = 0 
        failed = 0
        test_files =[]
        cases = 0
        is_tle = False
        for file in lt:
            ext = file.rsplit(sep='.',maxsplit=1)
            # print(f'file = {ext}')
            try :
                if ext[1] == 'in':
                    out = ext[0] + '.out'
                    if os.path.isfile(os.path.join(file_path,out)):
                        test_files.append((file,out))
                        cases += 1
                    else:
                        # print(f'{out} not found.')
                        pass
            except:
                pass
        if cases == 0:
            cprint(" # No testcase available.",'red')
            return
        if cases == 1:
            cprint(" # 1 testcase found.",'yellow')
        else :
            cprint(f' # {cases} testcases found','yellow')

        st = -1.0
        slowest = ''
        for f in test_files:
            file = f[0]
            out = f[1]
            # print(f'testing {file} with {out}')
            ext = file.rsplit(sep='.',maxsplit=1)
            with open(os.path.join(file_path,file),'r') as f:
                value = f.read()
            t = time.time()
            result = self.sub_process(['./test.out'],value)
            tle = result[1]
            result = result[0]
            # print(tle)
            t = time.time() - t
            if t > st:
                st = t
                slowest = ext[0]
            t = '{:.4}'.format(t) + 'sec'
            # print('code :\n',result)
            print()
            cprint('  * '+ext[0],'yellow')
            cprint('  * Time : ','cyan',end='')
            if tle :
                cprint('TLE','red')
                is_tle = True
            else :
                cprint(t,'cyan')
            with open(os.path.join(file_path,out)) as f:
                ans = f.read()
            # print('Expected :\n',ans)
            if tle == False and result == ans:
                cprint('  * Passed','green')
                passed += 1
            else :
                cprint('  * WA','red')
                failed += 1
                if tle == False:
                    self.different(value,result,ans,ext[0])

        print()
        st = f'{st:.4f}'
        pt = f' # Slowest : '
        cprint(pt,'blue', end='')
        if is_tle :
            cprint('TLE','red',end='')
        cprint(' ['+slowest+']','blue')
        pt = (f' # Status : {passed} / {passed+failed} ')
        cprint(pt,'yellow')
        if failed == 0:
            cprint(" # Passed....",'green')
        else :
            cprint(" # Failed....",'red')

        pt='-'*20+'-'*len(file_name)+'-'*20
        cprint(pt,'magenta')

    def find_files(self,file_name=''):

        file_list = []
        # print(file_name)
        supported_ext = ['cpp','py']
        # print(os.getcwd)
        for file in os.listdir(os.getcwd()):
            try :
                ext = file.rsplit(sep='.',maxsplit=1)
                for i in supported_ext:
                    if ext[1] == i:
                        if file_name in file:
                            file_list.append(file)
            except:
                pass
        # print(file_list)
        sz = len(file_list)
        if sz == 1:
            self.test_it(file_list[0])
        elif sz > 1:
            no = 1
            cprint("All the available files are given below.\n",'yellow')
            for file in file_list:
                pt = (' '*4+str(no)+') '+file)
                cprint(pt,'blue')
                no += 1
            cprint(' '*4+'0) Cancel operation','red')
            print()
            while True:
                cprint("Select the file index : ",'cyan',end='')
                index = int(input())
                if index == 0:
                    cprint("Testing operation cancelled.",'red')
                    break
                elif index < no:
                    self.test(file_list[index-1])
                    break
                else:
                    cprint("You have entered the wrong index.Please try again.",'red')
        else :
            cprint("NO FILE FOUND :(",'red')

if __name__ == "__main__":
    obj = Cp_my_tester()
    obj.find_files()