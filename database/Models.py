from .connection import db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db

class HighScore(BaseModel):
    score = IntegerField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

