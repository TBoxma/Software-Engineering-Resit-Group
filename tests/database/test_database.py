from database.connector import SQLite
from database.session_wrapper import *
from config.mysql import MYSQL_DB_NAME

import sqlalchemy as sa
from sqlalchemy.orm import Session

def test_should_connect_to_database():
    engine = SQLite.get_engine()
    connection = engine.connect()
    connection.close()

    assert len(sa.inspect(engine).get_schema_names()) > 0