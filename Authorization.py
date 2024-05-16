import time
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
        self.access_token_expiration = os.getenv("ACCESS_TOKEN_EXPIRATION")

    def get_base_auth_params(self):
       return {
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': self.authCode
        }

    def authenticate_user(self):
        # Error response for reference:
        # {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
        try:
            response = None
            if self.accessToken == None:
                response = self.first_time_authentication()

            if self.access_token_expiration == None or self.access_token_expiration == '':
                response = self.refresh_access_token()
            
            if self.accessToken != None and self.is_expired_access_token():
                response = self.refresh_access_token()
 
            if response == None:
                return 

            print("RESPONSE: ",  response)
            # Extract into a validation/error handling function
            if response['errors']:
                errorList = response['errors']

                if errorList[0]['resource'] == "AuthorizationCode" and errorList[0]['code'] == 'invalid':
                    print("Invalid Auth code, attempting refresh")
                    self.refresh_access_token()
                
                else:
                    print("Unknown error :(")
                    return "Error"
        
        except requests.exceptions.ConnectionError:
            return 'Connection Error'

    def first_time_authentication(self):
        try: 
            print('Authenticating User')
            params = self.get_base_auth_params()
            params['grant_type'] = 'authorization_code'
            response = requests.post(self.authUrl, 
                                     params=params).json()
            return response
        except requests.exceptions.ConnectionError:
            return 'Connection Error'

    def is_expired_access_token(self):
        now = round(time.time())
        print("Now: ", now)
        print("Access Token: ", self.access_token_expiration)
        
        if int(self.access_token_expiration) < now:
            print("Access Token Expired")
            return True
        
        return False
       
    def refresh_access_token(self):
        print("Refreshing User Access Token...")
        params = self.get_base_auth_params()
        params['refresh_token'] = self.refreshToken
        params['grant_type'] = 'refresh_token'

        try:
            response = requests.post(self.authUrl, params=params).json()
            dotenv.set_key(self.envFile, "ACCESS_TOKEN", response['access_token'])
            dotenv.set_key(self.envFile, "ACCESS_TOKEN_EXPIRATION", str(response['expires_at']))
            return response
        
        except ConnectionRefusedError:
            print('Connection Refused')
            return 'Connection Refused'
        