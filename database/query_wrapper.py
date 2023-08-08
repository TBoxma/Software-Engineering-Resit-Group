from database.connector import MySQL

def query(exec_query, transactional=False):
    """
    Manage connections for executing queries.

    - Args:
        - exec_query (`Callable`): A function that executes the query and accepts `Connection` as an argument.
        - transactional (`Bool`, optional): Indicates whether the query is transactional (create, update, delete). 
            Defaults to `False`.

    - Returns:
        `Callable`: A function that connects to the `Engine`, executes the query, returns the result,
        and closes the connection.
    """
    def wrapper(*args, **kwargs):
        with MySQL.get_engine().connect() as con:
            kwargs['connection'] = con
            result = exec_query(*args, **kwargs)

            if transactional:
                con.commit()
            else:
                return result
    
    return wrapper