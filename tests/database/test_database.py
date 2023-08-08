from database.connector import MySQL
from database.query_wrapper import *
import sqlalchemy as sa

def test_should_connect_to_database():

    engine = MySQL.get_engine()
    connection = engine.connect()
    connection.close()

    assert len(sa.inspect(engine).get_schema_names()) > 0

def test_should_find_ttt_database():
    rows = show_databases_query()
    result = [row[0] for row in rows]
    
    assert "ttt" in result

@query
def show_databases_query(connection: sa.engine.Connection = None):
    return connection.execute(sa.text("SHOW DATABASES"))