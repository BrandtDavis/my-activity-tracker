# from __future__ import print_statement
import requests
import os
from dotenv import load_dotenv



def getAllUserActivites():
    load_dotenv()
    responses = []
    activitiesUrl = 'https://www.strava.com/api/v3/athlete/activities'

    pageNum = 1

    while(1):
        params = {
            'access_token': os.getenv("ACCESS_TOKEN"),
            'per_page': 200,
            'page': pageNum
        }

        activities = requests.get(activitiesUrl, params=params).json()
        responses = responses + activities
        
        pageNum+=1

        if len(activities) < 200: break

    return responses



