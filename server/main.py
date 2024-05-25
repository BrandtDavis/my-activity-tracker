import os
from database.Connection import Connection
from database.AthleteQueries import save_athlete, get_athlete_by_id, delete_athlete_by_id

import dotenv

from pprint import pprint

import pymongo
from pymongo import MongoClient

import json

from src.Authorization import Authorization
from src.Athlete import getAuthenticatedAthlete, getAllUserActivites, getAllRunBasedActivities

# from application import app

# env_file_path = "./tests/test.env"
# env_file_path = "./.env"
# env_file = dotenv.dotenv_values(env_file_path)
# print(env_file['CLIENT_SECRET'])

# auth = Authorization(env_file, env_file_path)
# auth.authenticate_user()

# activities = getAllUserActivites()
# pprint(activities[700])
# print(len(activities))

# athlete = getAuthenticatedAthlete()
# print(athlete)

# athlete_record = {}
# athlete_record.update({"athlete_id": athlete['id']})
# athlete_record.update({"first_name": athlete['firstname']})
# athlete_record.update({"last_name": athlete['lastname']})
# athlete_record.update({"created_date": athlete['created_at']})
# athlete_record.update({"last_update": athlete['updated_at']})
# athlete_record.update({"premium_status": athlete['premium']})

# get_athlete_by_id(95573308)

# save_athlete(athlete_record)
# delete_athlete_by_id('6642f17233b4e6e8287dc98b')

# 
# pprint(athlete_record)
# conn = Connection()




# pprint(activities[3]['type'])
# runs = getAllRunBasedActivities(activities)
# pprint(len(runs))





