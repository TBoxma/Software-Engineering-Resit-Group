from function import Function

class Show(Function):

    def get_description(*args:str):
        if len(args)==0:
            return ['show', 'show task|category']
        match args[1]:
            case 'task':
                return ['show task (name(optional))', "show all tasks or a sprecific one"]
            case 'category':
                return ['show category (name(optional))', "show all categories or a sprecific one"]
              
    #tbd
    def task(*args:str):
        return

    def category(*args:str):
        return
    
    def command(self, *args:str) -> None:
