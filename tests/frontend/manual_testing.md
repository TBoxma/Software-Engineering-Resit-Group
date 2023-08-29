Test cases:
1. Should show greeting message on app startup
    - **Expected output**: `Greetings from the Time Tracking App!
With this app, you can conveniently add tasks and track time spent on them!
Type 'help' for a supported list of commands:`
**passed**

2. Should list all commands if type 'help'
    - **Expected output:** 
    `(argument)                      you can type one word here                                                                                                  
    {argument1|argument2}           you can type one of the words here                                                                                          
    [name]                          you can type several words, seperated by a space here. If you want the name to contain a space, surround it with parenthesis
    del {task|category}             delete a task or category                                                                                                   
    new {task|category} [name]      create one or more new tasks or categories                                                                                  
    update {task|category}          update a task or category                                                                                                   
    show {task|category}            show a task or category                                                                                                     
    add {time|category}             Add spent time to an existing taskor add a category. For details, type 'help add {time|categories}'                         
    help                            get a list of commands, ask for a specific command with 'help (command)'                                                    
    exit                            escape the program`
    **passed**


3. Should correctly handle non-existent command
    - **Input**: `blabla`
    - **Expected output**: Type 'help' for a list of commands
    **passed**

4. Should create a new category with command `new`
    - **Input**: `new category hey`, then answer `y` on prompt
    - **Expected output**: category 'hey' was created.

    - **Expected output when run `show category`**: category hey is among outputs and has 0 tasks
    **passed**

4. Should create a new task with command `new`
    - **Input**: `new task hello`, then answer `y` on prompt then add category `hey` then answer `y` on prompt
    - **Expected output**: `Created task 'hello'`

    - **Expected output when run `show task`**: task hello is among outputs and has category `hey`
    **passed**

5. Should warn non-existent category when creating task and using category that does not exist
    - **Input**: `new task bonjour`, then answer `y` on prompt then add category `blabla`
    - **Expected output**: `blabla is not a valid category`
    **passed**

6. Should correctly show task and category
    - **Input**: `show category`
    - **Expected output**: lists all existing categories and their tasks

    - **Input**: `show task`
    - **Expected output**: lists all existing tasks and their categories
    **passed**

7. Should add time to a task
    - **Input**: `add time hello 60`
    - **Expected output**: `adding 60 minutes to hello on [todays date]`

    - **Input**: `add time hello 15:00-19:00`
    - **Expected output**: `adding 240 minutes to hello on [todays date]`
    **passed**

8. Should correctly report total time, total time by tasks/categories and % of total time by tasks/categories
    - **Given**: only tasks, categories and time created in scope of this tests are in database

    - **Input**: `report` then `1` then `2023-01-01` then `2023-12-12`
    - **Expected output**: `total time spent on tasks from 2023-01-01 to 2023-12-12: 300`

    - **Input**: `report` then `2` then `2023-01-01` then `2023-12-12` then `hey`
    - **Expected output**: `Total time spent on specified categories from 2023-01-01 to 2023-12-12 is displayed below: hey: 300`

    - **Input**: `report` then `3` then `2023-01-01` then `2023-12-12` then `hello`
    - **Expected output**: `Total time spent on specified tasks from 2023-01-01 to 2023-12-12 is displayed below: hello: 300`

    - **Input**: `report` then `4` then `2023-01-01` then `2023-12-12` then `hey`
    - **Expected output**: `Percentage of total time spent on specified categories from 2023-01-01 to 2023-12-12 is displayed below: hey: 100%`

    - **Input**: `report` then `5` then `2023-01-01` then `2023-12-12` then `hello`
    - **Expected output**: `Percentage of total time spent on specified tasks from 2023-01-01 to 2023-12-12 is displayed below: hello: 100.0`
    **passed**

9. Should exit the program on `exit`
    - **Expected output**: program execution terminated without errors
    **passed**


    **passed 9/9 tests**


