import os
from database.Connection import Connection
from pymongo import MongoClient
from bson.objectid import ObjectId

DB_CONN_STRING = os.getenv("DB_CONN_STRING")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

conn = Connection()
db = conn.connect()

# Should save only athletes that are not already saved
# Should not save empty athletes
def save_athlete(athlete={}):
    result = db.athletes.insert_one(athlete)   
    print(result)         
    
def get_athlete_by_id(id):
    result = db.athletes.find_one({'athlete_id': {'$eq': id}})
    # print(result)
    return result

def get_athlete_by_email(email):
    result = db.athletes.find_one({'email': {'$eq': email}})
    print(result)
    return result

def delete_athlete_by_id(id):
    result = db.athletes.delete_one({'_id': ObjectId(id)})            
    print(result)

# Add error handling for:
# - Empty response
# - invalid id
def update_athlete_by_id(id):
    result = db.athletes.update_one({'_id': ObjectId(id)})            
    print(result)

# Should only be run during initial setup for an athlete
def add_athlete_activities(activities):
    result = db.activities.insert_many(activities)
    print(result)

def get_athlete_activities(athlete_id):
    result = db.activities.find({'athlete.id': {'$eq': athlete_id}})
    print(result)
    return result