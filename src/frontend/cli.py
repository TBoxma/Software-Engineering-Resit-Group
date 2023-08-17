import click
from src.backend.model.category import Category

from src.backend.model.task import Task
from ..backend.api.task_api import TaskApi
from ..backend.api.category_api import CategoryApi

from cli_functions.delete import *
from cli_functions.new import *
from cli_functions.show import *
from cli_functions.update import *


class CLI:
    helper_string = '\n'.join([
        "help:         get all possible commands as a list",
        "exit:         exit the program",
        "new task:     add a task",
        "new category: add a category",
        "update task:  change task attributes",
        "del task:     delete a task",
        "del category: delete a category",
        "show task:    show a category",
        "show category:show a category",
        "exit:         exit the program"
    ])
    
    def __init__(self, name="") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
    def start(self):
        while True:
            command_str = click.prompt("  >", type=str)
            command_args = command_str.split(' ')
            match command_args[0]:
                case "help":
                    print(self.helper_string)
                case "exit":
                    break
                case "new":
                    # attributes:
                    if(len(command_args) > 1):
                        match command_args[1]:
                            case "task":
                                self.handle_new_task(command_args[2:])
                            case "category":
                                self.handle_new_category(command_args[2:])
                    else:
                        print("type 'new task' or 'new category'")
                case "update":
                    match command_args[1]:
                        case "task":
                            print("update a task, tbd")
                        case "category":
                            print("update a category, tbd")
                case "show":
                    match command_args[1]:
                        case "task":
                            if(len(command_args) == 2):
                                tasks: list[Task] = TaskApi.list_all()
                                for task in tasks:
                                    categories = [category.name for category in task.categories]
                                    print("Task name: "+task.name)
                                    print("Task categories: "+", ".join(categories))
                                    print()
                            else:
                                task: Task = TaskApi.get_by_name(command_args[2])
                                categories = [category.name for category in task.categories]
                                print("Task name: "+task.name)
                                print("Task categories: "+", ".join(categories))
                                print()
                        case "category":
                            if(len(command_args) == 2):
                                categories: list[Category] = CategoryApi.list_all()
                                for category in categories:
                                    tasks = [task.name for task in category.tasks]
                                    print("Category name: "+category.name)
                                    print("Category tasks: "+", ".join(tasks))
                                    print()
                            else:
                                category: Category = CategoryApi.get_by_name(command_args[2])
                                tasks = [task.name for task in category.tasks]
                                print("Category name: "+category.name)
                                print("Category tasks: "+", ".join(tasks))
                                print()
                case "del":
                    if(len(command_args) > 1):
                        match command_args[1]:
                            case "task":
                                TaskApi.delete_by_name(' '.join(command_args[2:]))
                            case "category":
                                CategoryApi.delete_by_name(' '.join(command_args[2:]))
                case _:
                    print("Type 'help' for a list of commands")



