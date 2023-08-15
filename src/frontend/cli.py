import click
from ..backend.api.task_api import TaskApi

class CLI:
    helper_string = '\n'.join([
        "help:         get all possible commands as a list",
        "add:          create a new entry(not implemented)",
        "exit:         exit the program",
        "new task:     add a task",
        "update task:  change task attributes",
        "del task:     delete a task",
        "exit:         exit the program"
    ])
    
    def __init__(self, name="") -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
    def print_ln(self, text) -> None:
        print(text)
    
    def ask_user_input(self, question=">") -> None:
        return click.prompt(question, type=str)
     
    def handle_new_task(self, *args:str) -> None:

        given_attributes= {}
        given_attributes["name"] = "new task"
        given_attributes["categories"] = ""

        # List of attributes that the user needs to give:
        needs={}
        needs["name"] = True
        needs["id"] = False
        needs["categories"] = True

        # See which attributes are already passed in the input, and update given_attributes and needs accordingly:
        print(len(args[0]))
        if(len(args[0])>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = unparsed_attribute.split(':')
                if (len(parsed_attribute) == 2):
                    if(needs.get(parsed_attribute[0])):
                        try:
                            given_attributes[parsed_attribute[0]] = parsed_attribute[1]
                        except KeyError:
                            continue
                        try:
                            needs[parsed_attribute[0]] = False
                        except KeyError:
                            continue
                        
        #get the needs that haven't been set yet
        needs_to_do = {key : val for key, val in needs.items() if val == True}
        if(len(needs_to_do)>0):
            for need in needs_to_do:
                given_attributes[need] = click.prompt(need, type=str)
        
        print("Creating new task with attributes", str(given_attributes))
        TaskApi.add(given_attributes["name"], given_attributes["categories"].split(','))

    
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
                                print("initialise and add a category, tbd by Efim")
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
                            print("show a task, tbd")
                        case "category":
                            print("show a category, tbd")
                case "del":
                    match command_args[1]:
                        case "task":
                            print("delete a task, tbd")
                        case "category":
                            print("delete a category, tbd")
                case _:
                    print("Type 'help' for a list of commands")



