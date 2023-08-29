from src.frontend.cli_functions.function import Function

class Update(Function):

    main_description = ["update {task|category}", "update a task or category"]
    task_description = ['update task (name)', "update a task"]
    category_description = ['update category (name)', "update a category"]

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
              
    #tbd
    def task(self, args:[str] = []) -> None:
        print("updating a task is not yet supported in this version, but it will come out in a later release")
        return

    def category(self, args:[str] = []) -> None:
        print("updating a category is not yet supported in this version, but it will come out in a later release")
        return

    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
                case _:
                    print(self.get_description_precise())
        else:
            print(self.get_description_precise())