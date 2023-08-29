import click
import shlex

from src.frontend.cli_functions.delete import *
from src.frontend.cli_functions.new import *
from src.frontend.cli_functions.show import *
from src.frontend.cli_functions.update import *
from src.frontend.cli_functions.function import *
from src.frontend.cli_functions.help import *
from src.frontend.cli_functions.add import *
from src.frontend.cli_functions.report import *


class CLI:
    # whether to display a greetings message
    greetings_ = True

    def __init__(self, name="") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
    def start(self):
        if self.greetings_:
            print("Greetings from the Time Tracking App!")
            print("With this app, you can conveniently add tasks and track time spent on them!")
            print("Type 'help' for a supported list of commands:")
            print()
            
            self.greetings_ = False
        while True:
            command_str = click.prompt("  >", type=str)
            command_args = shlex.split(command_str)
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
                case "add":
                    Add().execute(command_args[1:])
                case "report":
                    Report().execute(command_args[1:])
                case "exit":
                    break
                case _:
                    print("Type 'help' for a list of commands")