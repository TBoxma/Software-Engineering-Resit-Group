from typing import Callable
from database.connector import MySQL

from sqlalchemy.orm import Session

def query(exec_query: Callable):
    """
    Manage connections for executing queries.

    :param exec_query: A function that executes the query and takes `sqlalchemy.orm.Session` as a keyword argument.
    :returns: A decorator that creates new session, executes the query, returns the result, and closes the session.
    """
    def wrapper(*args, **kwargs):
        with Session(MySQL.get_engine()) as session:
            kwargs['session'] = session
            
            return exec_query(*args, **kwargs)
    
    return wrapper