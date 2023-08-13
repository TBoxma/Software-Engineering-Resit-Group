import click

class CLI:
    helper_string = '\n'.join([
        "help:    get all possible commands as a list",
        "add:     create a new entry(not implemented)",
        "exit:    exit the program"
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
        # Attributes here:
        task_name = "new task"
        correct_input = True
        if(len(args[0])>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = unparsed_attribute.split(':')
                if (len(parsed_attribute) == 2):
                    match parsed_attribute[0]: #Case statement for each passed attribute.
                        case "name":
                            task_name = parsed_attribute[1]
                        case _:
                            correct_input = False
                else:
                    correct_input = False
        else:
            correct_input = False
        if not correct_input:
            task_name = click.prompt("name", type=str)
        #Call init function here:
        print("New task: (", task_name, ")")

    def handle_update_task(self, *args:str)-> None:
        # Attributes here:
        task_name = "new task"
        id = int(args[0][0])
        print(id)
        if not (-1<id<999999): #Exists function here
            print(id, " is not a valid id")
            return
        correct_input = True
        if(len(args[0])>0):
            for unparsed_attribute in args[0][1:]:
                parsed_attribute = unparsed_attribute.split(':')
                if (len(parsed_attribute) == 2):
                    match parsed_attribute[0]: #Case statement for each passed attribute.
                        case "name":
                            task_name = parsed_attribute[1]
                        case _:
                            correct_input = False
                else:
                    correct_input = False
        else:
            correct_input = False
        if not correct_input:
            task_name = click.prompt("id", type=int)
            task_name = click.prompt("name", type=str)
        #Call update function here:
        print("Changed task ", id, ": (", task_name, ")")
    
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
                    match command_args[1]:
                        case "task":
                            self.handle_new_task(command_args[2:])
                        case "category":
                            print("initialise and add a category, tbd by Efim")
                case "update":
                    match command_args[1]:
                        case "task":
                            self.handle_update_task(command_args[2:])
                        case "category":
                            print("update a category, tbd by Efim")



