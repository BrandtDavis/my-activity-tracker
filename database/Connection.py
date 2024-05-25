# import sys
# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.9/bin/dotenv')
import os
from dotenv import load_dotenv
from pymongo import MongoClient

class Connection:
    def __init__(self):
        load_dotenv()
        self.DB_CONN_STRING = os.getenv("DB_CONN_STRING")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_COLLECTION = os.getenv("DB_COLLECTION")

        # self.conn = self.connect()

    def connect(self):
        # print(self.DB_CONN_STRING)
        try:
            uri = self.DB_CONN_STRING
            client = MongoClient(uri)

            database = client[self.DB_NAME]
            collection = database[self.DB_COLLECTION]

            # Extract this into a DB initialization script
            collection_list = database.list_collection_names()
            if "activities" not in collection_list:
                print("Creating collection with name 'activities'")
                database.create_collection("activities")
            

            # client.close()
            return database

        except Exception as e:
            raise Exception(
                "The following error occurred: ", e)
