from peewee import *


db = PostgresqlDatabase('warsn_stars',
    user='root',
    password='password',
    host='localhost',
    port=5432
)

def initialize_database():
    from .Models import HighScore

    db.connect()
    db.create_tables([HighScore], safe=True)
    print("Database initialized successfully!")

def close_database():
    if not db.is_closed():
        db.close()
        print("Database connection closed!")