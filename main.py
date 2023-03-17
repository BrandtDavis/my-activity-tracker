import os
from dotenv import load_dotenv

from pprint import pprint

from authorization import refresh_user_access
from Athlete import getAllUserActivites, getAllRunBasedActivities

# print(json_response[0]['map'])

# if json_response.errors and json_response.errors.code == 'invalid':
#     print("Invalid token, attempting refresh...")
#     originalToken = os.getenv("ACCESS_TOKEN")

    # refresh access token
# response = refresh_user_access()
    # newToken = os.getenv("ACCESS_TOKEN")

    
    # if valid, carry on, else exit gracefully
    # if(originalToken != newToken):
    #     print("Token updated successfully")
    # else:
    #     print("Could not create new token, exitting") 

activities = getAllUserActivites()

print(len(activities))



# pprint(activities[3]['type'])
runs = getAllRunBasedActivities(activities)
pprint(len(runs))
# pprint(runs[10464)





