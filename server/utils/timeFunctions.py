import pandas as pd
from datetime import datetime
from database.AthleteQueries import get_athlete_activities

# Want: 
#  1. Look at current activity data -> Identify date windows 
#  2. Group activities into date windows
#     - i.e., the date window is 1 week (Mon-Sun), we want all activities within this window, for each window identified in step 1

# Returns an array of 2 elements in the form [start_date, end_date]
# Where:
#  - Both elements are in the form 'DD-MM-YYYY'
#  - start_date is the earliest date in the dataset
#  - end_date is the most recent date in the dataset
def get_activity_list_timeframe(activityList):
    pass

# Returns an array of dates, where each date should:
# - Be a Monday
# - Include the timeframe of the dates returned by get_activity_list_timeframe
#   - i.e., The Monday for the week of each of the 2 dates returned from the function should be included in the output of get_date_windows
def get_date_windows():
    pass

def group_activities_by_week():
    pass

# Help: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
activities = get_athlete_activities(95573308)

group_activities_by_week(activities)