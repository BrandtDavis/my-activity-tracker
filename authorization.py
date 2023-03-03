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
    json_response = response.json()
    return json_response

response = authorize_user()
pprint(response)