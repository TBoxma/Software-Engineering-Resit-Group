from function import Function
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi


class Delete(Function):
    helperstring = "del task|update"

    
    def get_description(self, *args:str) -> [str,str]:
        if len(args)==0:
            return ['del', 'new task|category']
        match args[1]:
            case 'task':
                return ['del task (name)', "delete a task"]
            case 'category':
                return ['del category (name)', "delete a category"]

    def task(self, *args:str):
        TaskApi.delete_by_name(' '.join(args))

    def category(self, *args:str):
        CategoryApi.delete_by_name(' '.join(args))

    def command(self, *args:str) -> None:
        if len(args>1):
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])

