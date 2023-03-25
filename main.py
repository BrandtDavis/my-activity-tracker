import os
from dotenv import load_dotenv

from pprint import pprint

from Authorization import Authorization
from Athlete import getAllUserActivites, getAllRunBasedActivities

auth = Authorization()
auth.authorize_user()

# activities = getAllUserActivites()

# print(len(activities))



# pprint(activities[3]['type'])
# runs = getAllRunBasedActivities(activities)
# pprint(len(runs))
# pprint(runs[10464)





