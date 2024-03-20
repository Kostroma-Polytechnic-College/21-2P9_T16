from peewee import *

db = SqliteDatabase('db.db')
class BaseModel(Model):
    class Meta:
        database = db

class Admin(BaseModel):
    ID = IntegerField()
    Telegram_id = TextField()
class Telegram(BaseModel):
    TOKEN = TextField()
