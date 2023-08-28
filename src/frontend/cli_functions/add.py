from datetime import date
import datetime
import click
from src.backend.api.category_api import CategoryApi
from src.backend.api.task_api import TaskApi
from src.frontend.cli_functions.function import Function
import re

class Add(Function):
    main_description = ["add {time|category}", "Add spent time to an existing taskor add a category. For details, type 'help add {time|categories}'"]
    today_description = ["add time (task) (minutes)", "add an amount of minutes to a task. 80 minutes can be formatted like '80', '1h20m', or '14:00-15:20'"]
    otherday_description = ["add time (task) (minutes) (date)", "add an amount of minutes to a task on a specific day. Write the date as YYYY-MM-DD"]
    category_description = ["add category (task) [category]", "add one or more categories to a task"]
    #Get the description as a list of string tuples [[command, desc]]
    def get_description_precise(self, args:[str] = []) -> [[str,str]]:
        if len(args)==0:
            return [self.today_description, self.otherday_description, self.category_description]
        match args[0]:
            case 'time':
                return [self.today_description, self.otherday_description]
            case 'category':
                return [self.category_description]
            case _:
                return [[args[0], "does not exist or cannot be called in this context"]]
                        
    #Get the description as a single tuple [command, desc]
    def get_description_generic(self) -> [str,str]:
        return self.main_description
    
    def check_date_format(self, date_string) -> bool:
        try:
            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(date_string, "%Y-%m-%d")
            return True
        # If the date validation goes wrong
        except ValueError:
            print("Incorrect date format, type YYYY-MM-DD")
            return False
        
    def check_time_format(self, passed_time) -> bool:
        try:
            # formatting the date using strptime() function
            timeObject = datetime.datetime.strptime(passed_time, "%H:%M")
            return True
        # If the date validation goes wrong
        except ValueError:
            print("Incorrect time format, type HH:MM-HH:MM")
            return False

    def time(self, args:[str] = []) -> None:
        #make sure enough arguments are passed
        if(not len(args)>1):
            print(self.get_description_precise(['time']))
            return
        
        #Take the task name
        task_name = args[0]
        
        #Handle date setting
        passed_date = str(date.today())
        if(len(args)==3):
            passed_date = args[2]
        if(not self.check_date_format(passed_date)):
            return
        if(not TaskApi.exists(task_name)):
            return
        
        #Handle task time
        task_time_unparsed = args[1]
        task_time = None

        #Handle task_time_unparsed being an integer
        if(task_time_unparsed.isnumeric()):
            task_time = int(task_time_unparsed)

        #Handle task_time_unparsed being parsed like 2h30 or 2h30m
        
        try:
            time_split_by_hour = task_time_unparsed.split('h')
            
            hours = None
            minutes = None
            if(time_split_by_hour[0].isnumeric()):
                hours = int(time_split_by_hour[0])
            if(time_split_by_hour[1][-1]=='m'):
                time_split_by_hour[1] = time_split_by_hour[1][:-1]
            if(time_split_by_hour[1].isnumeric()):
                minutes = int(time_split_by_hour[1])
            if(hours):
                task_time = 60*hours
            if(hours and minutes and minutes):
                task_time = 60*hours+minutes
            if(minutes>60 or minutes<0 or hours<0):
                task_time = None
        except:
            pass

        #Handle task time being a calculation like 14:00-15:30
        try:
            task_time_split_once = task_time_unparsed.split('-')
            if(len(task_time_split_once) == 2):
                hour1_temp, min1_temp = task_time_split_once[0].split(':')
                hour2_temp, min2_temp = task_time_split_once[1].split(':')
                if(hour1_temp.isnumeric() and hour2_temp.isnumeric() and min1_temp.isnumeric() and min2_temp.isnumeric()
                   and self.check_time_format(task_time_split_once[0]) and self.check_time_format(task_time_split_once[1])):
                    hour1 = int(hour1_temp)
                    hour2 = int(hour2_temp)
                    min1 = int(min1_temp)
                    min2 = int(min2_temp)
                if(hour1):
                    min1+=60*hour1
                    min2+=60*hour2
                if(min1 < min2):
                    task_time = min2-min1
        except:
            pass

        if(task_time and task_name and passed_date):
            date_entry = datetime.datetime.strptime(passed_date, "%Y-%m-%d").date()

            print(f"adding {task_time} minutes to {task_name} on {passed_date}")

            previous_time = TaskApi.get_task_time(date_entry, task_name)

            if previous_time:
                TaskApi.update_task_duration(date_entry, task_name, task_time)
            else:
                TaskApi.add_duration(date_entry, task_time, task_name)
     
    
    #Add categories to an existing task
    def category(self, args:[str] = []) -> None:
        TaskApi.add_categories(args[0], args[1:])
        return
    
    def execute(self, args:[str] = []) -> None:
        if len(args)>0:
            match args[0]:
                case 'time':
                    self.time(args[1:])
                case 'category':
                    self.category(args[1:])
        else:
            print(self.get_description_generic())