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
    
    def print_ln(self, text):
        print(text)
    
    def ask_user_input(self, question=">"):
        return click.prompt(question, type=str)
    
    def start(self):
        while True:
            command_str = click.prompt("  >", type=str)
            command_args = command_str.split(' ')
            match command_args[0]:
                case "help":
                    print(self.helper_string)
                case "exit":
                    break



