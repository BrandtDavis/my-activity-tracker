import os
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.DB_CONN_STRING = os.getenv("DB_CONN_STRING")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_COLLECTION = os.getenv("DB_COLLECTION")

        self.connect()

    def connect(self):
        try:
            uri = os.getenv("DB_CONN_STRING")
            client = MongoClient(uri)

            database = client[os.getenv("DB_NAME")]
            collection = database[os.getenv("DB_COLLECTION")]

            collection_list = database.list_collection_names()
            if "activities" not in collection_list:
                print("Creating collection with name 'activities'")
                database.create_collection("activities")
            

            client.close()

        except Exception as e:
            raise Exception(
                "The following error occurred: ", e)
