from src.frontend.cli_functions.function import Function
from src.backend.api import task_api
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.backend.model.category import Category
from src.backend.model.task import Task
import click
from src.backend.api.reports_api import ReportsApi

class Show(Function):

    main_description = ["show {task|category}", "show a task or category"]
    task_description = ['show task (name)', "show a task"]
    category_description = ['show category (name)', "show a category"]
    
    time_description = ["show time task|category", "show time spent on a task or category"]

    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.task_description, self.category_description, self.time_description]
        match args[0]:
            case 'task':
                return [self.task_description]
            case 'category':
                return [self.category_description]
            case 'time':
                return [self.time_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]

    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description
              
    #tbd
    def task(self, args:[str] = []) -> None:
        if(len(args) == 0):
            tasks: list[Task] = TaskApi.list_all()
            for task in tasks:
                categories = [category.name for category in task.categories]
                print(f"Task name: {task.name}")
                print(f"Task categories: {(', '.join(categories))}")
                print()
        else:
            task: Task = TaskApi.get_by_name(args[0])
            categories = [category.name for category in task.categories]
            print(f"Task name: {task.name}")
            print(f"Task categories: {(', '.join(categories))}")
            print()

    def category(self, args:[str] = []) -> None:
        if(len(args) == 0):
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
    
    # For now this function will only show how much time is spent on a task.
    def time_query(self, args:[str] = []) -> None:
        # if (len(args) == 2):
        #     if (args[1] == 'category'):
        #         # List all tasks of category & give total time spent on it
        #         pass
        #     else:
        #         # Display description
        #         print(self.time_description)
        if (len(args) == 3):
            match args[1]:
                case 'category':
                    # Ask user for begin and end date.                    
                    _start_date = click.prompt('Start date of Category')
                    _end_date = click.prompt('End date of Category') 
                    category: Category = CategoryApi.get_by_name(args[0])
                    _category = [category]
                    _total_time = ReportsApi.report_total_time_categories(_start_date, _end_date, _category)
                    print ("Total time spent on Category: " +category.name + " -> " +str(_total_time))
                case 'task':
                    # Ask for begin and end date.
                    _start_date = click.prompt('Start date of Task')
                    _end_date = click.prompt('End date of Task') 
                    task: Task = task_api.TaskApi.get_by_name(args[2])
                    _task = [task]
                    _time_on_task = ReportsApi.report_total_time_tasks(_start_date, _end_date, _task)
                    print ("Total time spent on Task: " +task.name + " -> " +str(_time_on_task))
        else:
            print(self.time_description)

    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
                # The case if we want to show the time spent on a task or category.
                case 'time':
                    self.time_query(args[1:])
        else:
            print(self.get_description_generic())