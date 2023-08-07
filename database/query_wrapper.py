from database.connector import MySQL

def transactional_query(exec_query):
    """
    Manages connection for any transactional query

    Args: 
        function which executes query and accepts `Connection` as an argument
    
    Returns:
        function which connects to `Engine`, executes transaction, commits and closes the connection
    """
    def wrapper(*args, **kwargs):
        with MySQL.get_engine().connect() as con:
            kwargs['connection'] = con
            exec_query(*args, **kwargs)
            con.commit()

    return wrapper

def query(exec_query):
    """
    Manages connection for any other query

    Args: 
        function which executes query and accepts `Connection` as an argument
    
    Returns:
        function which connects to `Engine`, executes query, returns result and closes the connection
    """
    def wrapper(*args, **kwargs):
        with MySQL.get_engine().connect() as con:
            kwargs['connection'] = con
            result = exec_query(*args, **kwargs)
        
            return result
    
    return wrapper