from sqlalchemy import create_engine, URL
from config.mysql import *

# TODO: add configuration

class MySQL:
    '''Holds a single instance of `Engine` configured to use `MySQL` dialect.'''
    _engine = None

    @classmethod
    def get_engine(self):
        if self._engine is None:
            db_url = URL.create(
                "mysql+pymysql",
                username=MYSQL_USER,
                password=MYSQL_PASSWORD,
                host=MYSQL_DB_HOST,
                database=MYSQL_DB_NAME
            )
            self._engine = create_engine(db_url)

        return self._engine