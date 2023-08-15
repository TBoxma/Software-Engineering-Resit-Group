from database.connector import MySQL

from sqlalchemy.orm import Session

def query(exec_query):
    """
    Manage connections for executing queries.

    - Args:
        - exec_query (`Callable`): A function that executes the query and accepts `Connection` as an argument.
        - transactional (`Bool`, optional): Indicates whether the query is transactional (create, update, delete). 
            Defaults to `False`.

    - Returns:
        `Callable`: A function that creates new session, executes the query, returns the result,
        and closes the session.
    """
    def wrapper(*args, **kwargs):
        with Session(MySQL.get_engine()) as session:
            kwargs['session'] = session
            
            return exec_query(*args, **kwargs)
    
    return wrapper