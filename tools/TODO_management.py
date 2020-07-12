import os
from system.path import getpath

todo_file_path = os.path.join(getpath(__file__),'todolist.todo')

class TODO :

    def list(self):
        pass



if __name__ == "__main__":
    print(todo_file_path)

