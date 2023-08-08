from sqlalchemy import create_engine

# TODO: add configuration

class MySQL:
    '''Holds a single instance of `Engine` configured to use `MySQL` dialect.'''
    _engine = None

    @classmethod
    def get_engine(self):
        if self._engine is None:
            db_url = "mysql://root:root@localhost/ttt"
            self._engine = create_engine(db_url)

        return self._engine