import click
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.frontend.cli_functions.function import Function


class New(Function):
    main_description = ["new {task|category} [name]", "create one or more new tasks or categories"]
    task_description = ['new task [name]', "create one or more new tasks, you'll be prompted to add or remove categories. You can add or remove 'homework' by typing 'homework' or '-homework'"]
    category_description = ['new category [name]', "create one or more new categories."]

    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.task_description, self.category_description]
        match args[0]:
            case 'task':
                return [self.task_description]
            case 'category':
                return [self.category_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]
                        
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description
    

    def task(self, args:[str] = []) -> None:
        #Each arg represents a new task to create
        if(len(args)==0):
            args = {click.prompt("task name")}
        for task_name in args:
            if(not TaskApi.exists(task_name)):
                if click.confirm(("Do you want to create a task named '"+task_name+"'?"), default=True):
                    categories=[]
                    while True:
                        category_input = click.prompt("add or remove a category", default="")
                        print(category_input)
                        if (len(category_input)>1 and category_input[0] == '-'):
                            if(category_input[1:] in categories):
                                categories.remove(category_input[1:])
                        else:
                            if(CategoryApi.exists(category_input)):
                                categories.append(category_input)
                            else:
                                print("Not a valid category")
                            
                        if click.confirm((task_name+" will have categories "+str(categories)+". Is that correct?")):
                            try:
                                TaskApi.add(task_name, categories)
                                print(("Created task '"+task_name+"'"))
                            except:
                                print("The task wasn't created, something went wrong")
                            return
            else:
                print((task_name+" already exists."))

    def category(self, args:[str] = []) -> None:
        if(len(args)==0):
            args = {click.prompt("category name")}
        for name in args:
            if click.confirm("Do you want to create category '"+name+"'?", default=True):
                if(not CategoryApi.exists(name)):
                    try:    
                        CategoryApi.add(str(name))
                        print("category '"+str(name)+"' was created.")
                    except:
                        print("The category wasn't created, something went wrong")
                else:
                    print("This category already exists")


    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description_generic())

