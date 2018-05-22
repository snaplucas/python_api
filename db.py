from peewee import *

mysql_db = MySQLDatabase('study', user='root', password='mypassword',
                         host='172.17.0.2', port=3306)

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class User(BaseModel):
    username = CharField()

mysql_db.connect()