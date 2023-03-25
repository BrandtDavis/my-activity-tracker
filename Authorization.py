import requests
import os
import dotenv
from dotenv import load_dotenv
from pprint import pprint

class Authorization:

    def __init__(self):
        pass

    def authorize_user(self):
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

        # {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
        try:
            response = requests.post(authUrl, params=params).json()
            if response['errors']:
                errorList = response['errors']
                if errorList[0]['resource'] == "AuthorizationCode" and errorList[0]['code'] == 'invalid':
                    print("Invalid Auth code, attempting refresh...")
                    response = self.refresh_user_access()
                else:
                    print("Unknown error :(")

            return response
        
        except requests.exceptions.ConnectionError:
            return 'Connection Error'



    def get_new_access_token(self):
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

        try:
            response = requests.post(authUrl, params=params)
            return response.json()['access_token']
        except ConnectionRefusedError:
            return 'Connection Refused'
        # ** Investigate why this doesn't work **
        # json_response = response.json()
        # pprint(response.__dict__)


    def refresh_user_access(self):
        load_dotenv()
        dotenvFile = dotenv.find_dotenv()

        newAccessToken = self.get_new_access_token()
        
        print("Resetting User Access Token...")
        dotenv.set_key(dotenvFile, "ACCESS_TOKEN", newAccessToken)


    # refresh_user_access()


