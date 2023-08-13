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
        status = 0 #0:not started, 1:in progress, 2:done
        correct_input = True
        if(len(args[0])>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = unparsed_attribute.split(':')
                if (len(parsed_attribute) == 2):
                    match parsed_attribute[0]:
                        case "name":
                            task_name = parsed_attribute[1]
                        case "status":
                            status = parsed_attribute[1]
                            if status not in [0,1,2]:
                                correct_input = False
                        case _:
                            correct_input = False
                else:
                    correct_input = False
        else:
            correct_input = False
        if not correct_input:
            task_name = click.prompt("name", type=str)
            status = click.prompt("status(0,1,2)", type=click.IntRange(0, 2), default=0)
        #Call init function here:
        print("New task: (", task_name, ',' ,status, ")")
    
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



