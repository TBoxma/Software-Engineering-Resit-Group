from function import Function

class Update(Function):

    def get_description(*args:str):
        if len(args)==0:
            return ['update', 'update task|category']
        match args[1]:
            case 'task':
                return ['update task (name(optional))', "update a task"]
            case 'category':
                return ['update category (name(optional))', "update a category"]
              
    #tbd
    def task(*args:str):
        return

    def category(*args:str):
        return
    

    def execute(self, *args:str) -> None:
        if len(args>1):
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description())