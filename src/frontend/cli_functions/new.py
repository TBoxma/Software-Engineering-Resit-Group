from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from function import Function


class New(Function):
    def get_description(*args:str):
        if len(args)==0:
            return ['new', 'new task|category']
        match args[1]:
            case 'task':
                return ['new task (name)', "create a new task"]
            case 'category':
                return ['new category (name)', "create a new category"]

    def task(self, *args:str):
        given_attributes= {}
        given_attributes["name"] = "new task"
        given_attributes["categories"] = ""

        # List of attributes that the user needs to give:
        needs={}
        needs["name"] = True
        needs["id"] = False
        needs["categories"] = True

        # See which attributes are already passed in the input, and update given_attributes and needs accordingly:
        print(len(args[0]))
        if(len(args[0])>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = unparsed_attribute.split(':')
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
        
        print("Creating new task with attributes", str(given_attributes))
        categories = given_attributes["categories"].split(',')
        if len(categories) == 1 and categories[0]=="":
            categories = []
        TaskApi.add(given_attributes["name"], categories)

    def category(self, *args:str):
        given_attributes= {}
        given_attributes["name"] = "new category"

        # List of attributes that the user needs to give:
        needs={}
        needs["name"] = True
        needs["id"] = False
        needs["categories"] = False

        # See which attributes are already passed in the input, and update given_attributes and needs accordingly:
        print(len(args[0]))
        if(len(args[0])>0):
            for unparsed_attribute in args[0]:
                parsed_attribute = unparsed_attribute.split(':')
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
        CategoryApi.add(given_attributes["name"])


    def command(self, *args:str) -> None:
        if len(args>1):
            match args[0]:
                case 'task':
                    self.task(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description())