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
    
    def command(self, *args:str) -> None:
