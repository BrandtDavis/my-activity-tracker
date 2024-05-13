import os
from pymongo import MongoClient
from bson.objectid import ObjectId

DB_CONN_STRING = os.getenv("DB_CONN_STRING")
DB_NAME = os.getenv("DB_NAME")
DB_COLLECTION = os.getenv("DB_COLLECTION")

def save_athlete(athlete={}):
    try:
            print('inserting athlete')
            uri = os.getenv("DB_CONN_STRING")
            client = MongoClient(uri)

            database = client[os.getenv("DB_NAME")]
            result = database.athletes.insert_one(athlete)            

            print(result)
            client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    
def delete_athlete_by_id(id):
    try:
            print('deleting athlete')
            uri = os.getenv("DB_CONN_STRING")
            client = MongoClient(uri)

            database = client[os.getenv("DB_NAME")]
            result = database.athletes.delete_one({'_id': ObjectId(id)})            

            print(result)
            client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

