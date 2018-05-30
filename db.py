from peewee import *

mysql_db = SqliteDatabase('test.db')

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class User(BaseModel):
    username = CharField()

mysql_db.connect()