# from peewee import *
#
# sql_lite = SqliteDatabase('test.db')
#
#
# class BaseModel(Model):
#     """A base model that will use our MySQL database"""
#
#     class Meta:
#         database = sql_lite
#
#
# class User(BaseModel):
#     username = CharField()
#
#
# sql_lite.connect()


# coding: utf-8

import dataset

db = dataset.connect('sqlite:///noticias.db')
noticias = db['noticias']
