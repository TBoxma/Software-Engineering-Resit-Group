from function import Function
from src.backend.api import task_api
from src.backend.api.category_api import CategoryApi
from src.backend.model.category import Category
from src.backend.model.task import Task

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

    def category(*args:str):
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
    

    def command(self, *args:str) -> None:
        if len(args>1):
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description())