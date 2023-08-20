from src.frontend.cli_functions.function import Function
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi


class Delete(Function):
    main_description = ["del task|category", "delete a task or category"]
    task_description = ['del task (name)', "delete a task"]
    category_description = ['del category (name)', "delete a category"]

    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.task_description, self.category_description]
        match args[0]:
            case 'task':
                return [self.task_description]
            case 'category':
                return [self.category_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]
                  
    def get_description_generic(self) -> [str,str]:
        return self.main_description
    

    def task(self, args:[str] = []) -> None:
        try:
            TaskApi.delete_by_name(' '.join(args))
        except:
            print("The task wasn't deleted, something went wrong")

    def category(self, args:[str] = []) -> None:
        try:
            CategoryApi.delete_by_name(' '.join(args))
        except:
            print("The category wasn't deleted, something went wrong")
        
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description_generic())