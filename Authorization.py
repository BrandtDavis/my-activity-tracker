import datetime
import requests
import os
import dotenv
from dotenv import load_dotenv
from pprint import pprint

class Authorization:

    def __init__(self):
        load_dotenv()
        self.envFile = dotenv.find_dotenv()
        
        self.authUrl = 'https://www.strava.com/oauth/token'

        self.clientId = os.getenv("CLIENT_ID")
        self.clientSecret = os.getenv("CLIENT_SECRET")
        self.authCode = os.getenv("AUTHORIZATION_CODE")

        self.accessToken = os.getenv("ACCESS_TOKEN")
        self.refreshToken = os.getenv("REFRESH_TOKEN")

    def getBaseAuthParams(self):
       return {
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': self.authCode
        }
        # pass

    def authenticateUser(self):
        authUrl = 'https://www.strava.com/oauth/token'

        params = self.getBaseAuthParams()
        params['grant_type'] = 'authorization_code'

        # Error response for reference:
        # {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
        try:
            print('Authenticating User')
            
            response = requests.post(authUrl, params=params).json()
            print(response)
            
            if response['errors']:
                errorList = response['errors']

                if errorList[0]['resource'] == "AuthorizationCode" and errorList[0]['code'] == 'invalid':
                    print("Invalid Auth code, attempting refresh...")
                    self.refreshUserAccess()
                
                else:
                    print("Unknown error :(")
                    return "Error"
        
        except requests.exceptions.ConnectionError:
            print('Connection Error')
            return 'Connection Error'



    def getNewAccessToken(self):
        params = self.getBaseAuthParams()
        params['refresh_token'] = self.refreshToken
        params['grant_type'] = 'refresh_token'

        try:
            response = requests.post(self.authUrl, params=params)
            print(f"Refresh Response: {response.json()}")
            print("Received Access Token: ", response.json()['access_token'])
            return response.json()['access_token']
        
        except ConnectionRefusedError:
            print('Connection Refused')
            return 'Connection Refused'
        
        # ** Investigate why this doesn't work **
        # json_response = response.json()
        # pprint(response.__dict__)


    def refreshUserAccess(self):
        print("Resetting User Access Token...")
        newAccessToken = self.getNewAccessToken()

        dotenv.set_key(self.envFile, "ACCESS_TOKEN", newAccessToken)



