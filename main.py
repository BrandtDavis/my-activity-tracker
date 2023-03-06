# from __future__ import print_statement
import requests
import os
from dotenv import load_dotenv

from pprint import pprint

load_dotenv()

activitiesUrl = 'https://www.strava.com/api/v3/athlete/activities'

token = os.getenv("ACCESS_TOKEN")
# headers = {"Authorization": f"Bearer {token}"}

params = {
    'access_token': os.getenv("ACCESS_TOKEN")
}

response = requests.get(activitiesUrl, params=params)
json_response = response.json()

pprint(json_response)


