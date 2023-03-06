import requests
import os
from dotenv import load_dotenv
from pprint import pprint

def authorize_user():
    load_dotenv()

    authUrl = 'https://www.strava.com/oauth/token'

    clientId = os.getenv("CLIENT_ID")
    clientSecret = os.getenv("CLIENT_SECRET")
    authCode = os.getenv("AUTHORIZATION_CODE")

    params = {
        'client_id': clientId,
        'client_secret': clientSecret,
        'code': authCode,
        'grant_type': 'authorization_code'
    }

    # headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(authUrl, params=params)
    return response.json()

def refresh_user_access():
    load_dotenv()

    authUrl = 'https://www.strava.com/oauth/token'

    clientId = os.getenv("CLIENT_ID")
    clientSecret = os.getenv("CLIENT_SECRET")
    refreshToken = os.getenv("REFRESH_TOKEN")

    params = {
        'client_id': clientId,
        'client_secret': clientSecret,
        'refresh_token': refreshToken,
        'grant_type': 'refresh_token'
    }

    response = requests.post(authUrl, params=params)
    
    # ** Investigate why this doesn't work **
    # json_response = response.json()
    pprint(response.__dict__)
    return response.json()

response = refresh_user_access()
#pprint(response)

