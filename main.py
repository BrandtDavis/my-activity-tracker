import requests
import os
from dotenv import load_dotenv

load_dotenv()

authUrl = 'https://www.strava.com/api/v3/athlete'

token = os.getenv("ACCESS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(authUrl, headers=headers)
json_response = response.json()

print(json_response)