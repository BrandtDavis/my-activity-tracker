import os
from dotenv import load_dotenv

from pprint import pprint

import pymongo
from pymongo import MongoClient

from Authorization import Authorization
from Athlete import getAllUserActivites, getAllRunBasedActivities

auth = Authorization()
auth.authenticateUser()

activities = getAllUserActivites()

print(len(activities))


try:
    uri = os.getenv("DB_CONN_STRING")
    client = MongoClient(uri)

    database = client[os.getenv("DB_NAME")]
    collection = database[os.getenv("DB_COLLECTION")]

    collection_list = database.list_collections()
    if "activities" not in collection_list:
        database.create_collection("activities")

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)


# pprint(activities[3]['type'])
# runs = getAllRunBasedActivities(activities)
# pprint(len(runs))





