class Config(object):
    """Base config, uses staging database server."""
    DB_HOST = 'http://postgres'
    DB_PORT = '5432'
    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/postgres'
