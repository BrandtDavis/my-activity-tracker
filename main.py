# from __future__ import print_statement
import requests
import os
from dotenv import load_dotenv

from pprint import pprint

from authorization import refresh_user_access
from activities import getAllUserActivites

json_response = getAllUserActivites()

if json_response['code'] == 'invalid' and json_response['field'] == 'access_token':
    print("Invalid token, attempting refresh...")
    originalToken = os.getenv("ACCESS_TOKEN")

    # refresh access token
    response = refresh_user_access()
    newToken = os.getenv("ACCESS_TOKEN")

    
    # if valid, carry on, else exit gracefully
    if(originalToken != newToken):
        print("Token updated successfully")
    else:
        print("Could not create new token, exitting") 


pprint(json_response)


