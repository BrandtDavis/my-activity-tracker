import time
import requests
import dotenv

class Authorization:

    def __init__(self, env_file, env_file_path):   
        self.env_file = env_file     
        self.env_file_path = env_file_path

        self.authUrl = 'https://www.strava.com/oauth/token'
        self.base_params = self.get_base_auth_params()

        self.access_token = env_file["ACCESS_TOKEN"]
        self.refresh_token = env_file["REFRESH_TOKEN"]
        self.access_token_expiration = env_file["ACCESS_TOKEN_EXPIRATION"]

    def get_base_auth_params(self):
       return {
            'client_id': self.env_file["CLIENT_ID"],
            'client_secret': self.env_file["CLIENT_SECRET"],
            'code': self.env_file["AUTHORIZATION_CODE"]
        }

    def authenticate_user(self):
        # Error response for reference:

        try:
            response = None
            if self.access_token == None:
                response = self.first_time_authentication()
            
            if self.access_token != None and self.token_refresh_required(self.env_file["ACCESS_TOKEN_EXPIRATION"]):
                response = self.refresh_access_token()
 
            if response == None:
                return "Unkown error: response = None"

            print("RESPONSE: ",  response)

            # Extract into a validation/error handling function
            # {'message': 'Bad Request', 'errors': [{'resource': 'AuthorizationCode', 'field': 'code', 'code': 'invalid'}]}
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

    # A token refresh is required under the following conditions:
    # - 
    # - 
    def token_refresh_required(self, access_token_expr):
        now = round(time.time())
        if access_token_expr == None or int(access_token_expr) < now:
            print("Access Token Expired")
            return True
        
        return False
       
    def refresh_access_token(self):
        print("Refreshing User Access Token...")
        params = self.get_base_auth_params()
        params['refresh_token'] = self.refresh_token
        params['grant_type'] = 'refresh_token'

        try:
            response = requests.post(self.authUrl, params=params).json()
            dotenv.set_key(self.env_file_path, "ACCESS_TOKEN", response['access_token'])
            dotenv.set_key(self.env_file_path, "ACCESS_TOKEN_EXPIRATION", str(response['expires_at']))
            return response
        
        except ConnectionRefusedError:
            print('Connection Refused')
            return 'Connection Refused'
        