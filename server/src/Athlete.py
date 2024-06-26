# from __future__ import print_statement
import requests
import os
from dotenv import load_dotenv

def getAuthenticatedAthlete():
    load_dotenv()

    url = f"https://www.strava.com/api/v3/athlete"

    headers = {
        'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
    }

    athlete = requests.get(url, headers=headers).json()
    return athlete

def getAllUserActivites():
    load_dotenv()
    responses = []
    activitiesUrl = 'https://www.strava.com/api/v3/athlete/activities'

    pageNum = 1

    while(1):
        params = {
            'access_token': os.getenv('ACCESS_TOKEN'),
            'per_page': 200,
            'page': pageNum
        }

        try:
            activities = requests.get(activitiesUrl, params=params).json()

        except requests.exceptions.ConnectionError: 
            print("Connection error on Activities request :(")
            break

        print(responses)
        responses = responses + activities
        pageNum+=1

        if len(activities) < 200: break
    return responses

def getAllRunBasedActivities(activities):
    runs = []
    for activity in activities:
        if activity['type'] == "Run" or activity['type'] == "Trail Run":
            runs.append(activity)
    return runs


