class Function:
    #handle a command
    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        return
    
    main_description = ["new task|category", "create a new task or category"]
    task_description = ['new task (name)', "create a new task"]
    category_description = ['new category (name)', "create a new category"]

    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        return self.main_description
            
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description