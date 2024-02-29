import peewee
# import models as {table name}_{model name}
from models.Poll import Poll as polls_Poll

pollsDb = peewee.SqliteDatabase('./src/polls.db')

def createTables():
    pollsDb.create_tables([polls_Poll])