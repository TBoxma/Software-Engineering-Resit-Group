import click

from src.frontend.cli_functions.delete import *
from src.frontend.cli_functions.new import *
from src.frontend.cli_functions.show import *
from src.frontend.cli_functions.update import *
from src.frontend.cli_functions.function import *
from src.frontend.cli_functions.help import *


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
                    Help().execute(command_args[1:])
                case "new":
                    New().execute(command_args[1:])
                case "update":
                    Update().execute(command_args[1:])
                case "show":
                    Show().execute(command_args[1:])
                case "del":
                    Delete().execute(command_args[1:])
                case "exit":
                    break
                case _:
                    print("Type 'help' for a list of commands")



