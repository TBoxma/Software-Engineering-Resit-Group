from src.frontend.cli_functions.function import Function
from src.backend.api import task_api
from src.backend.api.category_api import CategoryApi
from src.backend.model.category import Category
from src.backend.model.task import Task

class Show(Function):

    main_description = ["show task|category", "show a task or category"]
    task_description = ['show task (name)', "show a task"]
    category_description = ['show category (name)', "show a category"]

    #Get the description as a list of string tuples [[command, desc]]
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

    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description
              
    #tbd
    def task(self, args:[str] = []) -> None:
        if(len(args) == 0):
            tasks: list[Task] = task_api.list_all()
            for task in tasks:
                categories = [category.name for category in task.categories]
                print("Task name: "+task.name)
                print("Task categories: "+", ".join(categories))
                print()
        else:
            task: Task = task_api.TaskApi.get_by_name(args[0])
            categories = [category.name for category in task.categories]
            print("Task name: "+task.name)
            print("Task categories: "+", ".join(categories))
            print()

    def category(self, args:[str] = []) -> None:
        if(len(args) == 2):
            categories: list[Category] = CategoryApi.list_all()
            for category in categories:
                tasks = [task.name for task in category.tasks]
                print("Category name: "+category.name)
                print("Category tasks: "+", ".join(tasks))
                print()
        else:
            category: Category = CategoryApi.get_by_name(args[0])
            tasks = [task.name for task in category.tasks]
            print("Category name: "+category.name)
            print("Category tasks: "+", ".join(tasks))
            print()
    

    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description_generic())