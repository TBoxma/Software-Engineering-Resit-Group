import click
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.frontend.cli_functions.function import Function


class Add(Function):
    main_description = ["add", "Add spent time to an existing task"]
    today_description = ['add (task) (minutes)', "add an amount of minutes to a task"]
    otherday_description = ['add (task) (minutes)', "add an amount of minutes to a task"]

    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.task_description, self.category_description]
        match args[0]:
            case 'task':
                return [self.today_description]
            case 'category':
                return [self.otherday_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]
                        
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description