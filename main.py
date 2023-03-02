# from __future__ import print_statement
import requests
import os
from dotenv import load_dotenv

import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

load_dotenv()

authUrl = 'https://www.strava.com/api/v3/athlete'

token = os.getenv("ACCESS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(authUrl, headers=headers)
json_response = response.json()

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = token

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 0 # Long | The identifier of the activity.
includeAllEfforts = True # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
    api_response = api_instance.getActivityById(id, includeAllEfforts=includeAllEfforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)

