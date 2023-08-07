from sqlalchemy import create_engine

# TODO: add configuration

class MySQL:
    _engine = None

    @classmethod
    def get_engine(self):
        '''Returns Engine configured to use MySQL dialect'''
        if self._engine is None:
            # Configure your database URL here
            db_url = "mysql://root:root@localhost/ttt"
            self._engine = create_engine(db_url)

        return self._engine