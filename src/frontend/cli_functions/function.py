class Function:
    #handle a command
    def execute(self, args:[str] = []) -> None:
        return
    
    main_description = ["new task|category", "create a new task or category"]
    task_description = ['new task (name)', "create a new task"]
    category_description = ['new category (name)', "create a new category"]

    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        return self.main_description
            
    def get_description_generic(self) -> [str,str]:
        return self.main_description