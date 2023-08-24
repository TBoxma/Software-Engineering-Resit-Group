import inspect

from src.frontend.cli_functions.delete import *
from src.frontend.cli_functions.new import *
from src.frontend.cli_functions.show import *
from src.frontend.cli_functions.update import *
from src.frontend.cli_functions.function import *
from src.frontend.cli_functions.help import *
    
class Help(Function):
    exit_desc = ['exit', 'escape the program']

    main_description = ["help", "get a list of commands, ask for a specific command with 'help [command]'"]
    help_description = ["help", "get a list of commands"]
    help_cmd_description = ["help [command]", "get help with a specific command"]
    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.help_description, self.help_cmd_description]
        match args[0]:
            case 'task':
                return [self.task_description]
            case 'category':
                return [self.category_description]
            
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description


#help, new, new, update, del, exit

    #Execute the function, you pass the arguments given by the user as a list.
    #Other functions in this class handle the rest of the arguments.
    def execute(self, args:[str] = []) -> None:
        helper_list = []
        if(len(args) == 0):
            helper_list.append(Delete().get_description_generic())
            helper_list.append(New().get_description_generic())
            helper_list.append(Update().get_description_generic())
            helper_list.append(Show().get_description_generic())
            helper_list.append(Help().get_description_generic())
            helper_list.append(self.exit_desc)
        else:
            match args[0]:
                case "del"|"delete"|"remove"|"rm"|"houdoe":
                    helper_list = Delete().get_description_precise(args[1:])
                case "new"|"add"|"create"|"make":
                    helper_list = New().get_description_precise(args[1:])
                case "update"|"change"|"alter":
                    helper_list = Update().get_description_precise(args[1:])
                case "show"|"view"|"give":
                    helper_list = Show().get_description_precise(args[1:])
                case "help":
                    helper_list = Help().get_description_precise(args[1:])
                case "exit"|"close"|"shutdown":
                    helper_list = [self.exit_desc]
                case _:
                    helper_list = [[args[0], "does not exist or cannot be called in this context"]]
        
        s = [[str(e) for e in row] for row in helper_list]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]

        print('\n'.join(table))
