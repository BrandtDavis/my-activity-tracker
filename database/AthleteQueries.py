import os
from database.Connection import Connection
from pymongo import MongoClient
from bson.objectid import ObjectId

DB_CONN_STRING = os.getenv("DB_CONN_STRING")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

conn = Connection()
db = conn.connect()

def save_athlete(athlete={}):
    result = db.athletes.insert_one(athlete)   
    print(result)         
    
def delete_athlete_by_id(id):
    result = db.athletes.delete_one({'_id': ObjectId(id)})            
    print(result)

def update_athlete_by_id(id):
    result = db.athletes.update_one({'_id': ObjectId(id)})            
    print(result)
