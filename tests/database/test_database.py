from database.connector import SQLite
from database.session_wrapper import *

import sqlalchemy as sa

def test_should_connect_to_database():
    engine = SQLite.get_engine()
    connection = engine.connect()
    connection.close()

    assert len(sa.inspect(engine).get_schema_names()) > 0