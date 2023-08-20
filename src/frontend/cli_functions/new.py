import click
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.frontend.cli_functions.function import Function


class New(Function):
    main_description = ["new task|category", "create a new task or category"]
    task_description = ['new task (name)', "create a new task"]
    category_description = ['new category (name)', "create a new category"]

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
        print(args)
        given_attributes= {}
        given_attributes["name"] = "new task"
        given_attributes["categories"] = ""

        # List of attributes that the user needs to give:
        needs={}
        needs["name"] = True
        needs["id"] = False
        needs["categories"] = True

        # See which attributes are already passed in the input, and update given_attributes and needs accordingly:
        if(len(args)>0):
            for unparsed_attribute in args[0:]:
                parsed_attribute = str(unparsed_attribute).split(':')
                if (len(parsed_attribute) == 2):
                    if(needs.get(parsed_attribute[0])):
                        try:
                            given_attributes[parsed_attribute[0]] = parsed_attribute[1]
                        except KeyError:
                            continue
                        try:
                            needs[parsed_attribute[0]] = False
                        except KeyError:
                            continue
                    else:
                        given_attributes["name"] = parsed_attribute[0]
                        
        #get the needs that haven't been set yet
        needs_to_do = {key : val for key, val in needs.items() if val == True}
        if(len(needs_to_do)>0):
            for need in needs_to_do:
                given_attributes[need] = click.prompt(need, type=str, default="")
        
        print("Creating new task with attributes", str(given_attributes))
        categories = given_attributes["categories"].split(',')
        if len(categories) == 1 and categories[0]=="":
            categories = []
        try:
            TaskApi.add(given_attributes["name"], categories)
        except:
            print("The task wasn't created, something went wrong")
            

    def category(self, args:[str] = []) -> None:
        print(args)
        given_attributes= {}
        given_attributes["name"] = "new category"

        # List of attributes that the user needs to give:
        needs={}
        needs["name"] = True
        needs["id"] = False
        needs["categories"] = False

        # See which attributes are already passed in the input, and update given_attributes and needs accordingly:
        if(len(args)>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = str(unparsed_attribute).split(':')
                if (len(parsed_attribute) == 2):
                    if(needs.get(parsed_attribute[0])):
                        try:
                            given_attributes[parsed_attribute[0]] = parsed_attribute[1]
                        except KeyError:
                            continue
                        try:
                            needs[parsed_attribute[0]] = False
                        except KeyError:
                            continue
                        
        #get the needs that haven't been set yet
        needs_to_do = {key : val for key, val in needs.items() if val == True}
        if(len(needs_to_do)>0):
            for need in needs_to_do:
                given_attributes[need] = click.prompt(need, type=str, default="")
        
        print("Creating new category with attributes", str(given_attributes))
        try:
            CategoryApi.add(given_attributes["name"])
        except:
            print("The category wasn't created, something went wrong")


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

