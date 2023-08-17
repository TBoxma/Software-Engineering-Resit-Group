from function import Function

class Help(Function):
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

    exit_desc = ['exit', 'escape the program']

    def get_description():
        return ['help', "get all possible commands as a list.  e.g. 'help new'"]
#help, new, new, update, del, exit

    def execute(self, *args:str) -> None:
        if len(args)==0:
            