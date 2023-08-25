from sqlalchemy import create_engine, URL

class SQLite:
    '''Holds a single instance of `Engine` configured to use `SQLite` dialect.'''
    _engine = None

    @classmethod
    def get_engine(self):
        if self._engine is None:
            self._engine = create_engine("sqlite:///data/ttt.db")

        return self._engine