import click
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.frontend.cli_functions.function import Function


class Add(Function):
    main_description = ["add time", "Add spent time to an existing task. For details, type 'help add_time {today, other_day}'"]
    today_description = ['add time (task) (minutes)', "add an amount of minutes to a task. 80 minutes can be formatted like '80', '1h20m', or '14:00-15:20'"]
    otherday_description = ['add time (task) (minutes) (date)', "add an amount of minutes to a task on a specific day"]
    category_description = ['add category (task) [category]', "add one or more categories to a task"]
    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.task_description, self.category_description]
        match args[0]:
            case 'today':
                return [self.today_description]
            case 'other_day':
                return [self.otherday_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]
                        
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description
    
    def time(self, args:[str] = []) -> None:
        return
    
    def category(self, args:[str] = []) -> None:
        #Take args[0] as the task, and add the remaining args as categories to that task
        return
    
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'time':
                    self.time(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description_generic())


