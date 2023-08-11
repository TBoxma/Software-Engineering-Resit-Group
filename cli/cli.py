import click

class CLI:
    
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
    

