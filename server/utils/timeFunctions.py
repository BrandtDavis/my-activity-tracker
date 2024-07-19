import pandas as pd
from datetime import datetime, timedelta
from database.AthleteQueries import get_athlete_activities

# Want: 
#  1. Look at current activity data -> Identify date windows 
#  2. Group activities into date windows
#     - i.e., the date window is 1 week (Mon-Sun), we want all activities within this window, for each window identified in step 1

# Returns an array of 2 elements in the form [start_date, end_date]
# Where:
#  - Both elements are in the form 'DD-MM-YYYY'
#  - start_date is the earliest start_date in the dataset
#  - end_date is the most recent start_date_local in the dataset
def get_activity_list_timeframe(activityList):
    start_dates_df = pd.DataFrame.from_records(activityList)['start_date']
    start_date = start_dates_df.min().split("T")[0]
    end_date = start_dates_df.max().split("T")[0] 

    return [start_date, end_date]

# Returns an array of dates, where each date should:
# - Be a Monday
# - Include the timeframe of the dates returned by get_activity_list_timeframe
#   - i.e., The Monday for the week of each of the 2 dates returned from the function should be included in the output of get_date_windows
# Help: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
def get_date_windows(start_date, end_date):
    start_date_weekday = get_weekday(start_date)
    end_date_weekday = get_weekday(end_date)

    start_date_offset = start_date_weekday - 1
    end_date_offset = end_date_weekday - 1

    start_date_window = get_date_object(start_date) - timedelta(days=start_date_offset)
    end_date_window = get_date_object(end_date) - timedelta(days=end_date_offset)

    date_windows = []
    date_window = start_date_window
    while date_window != end_date_window:
        date_windows.append(date_window.strftime('%Y-%m-%d'))
        date_window = date_window + timedelta(days=7)

    return date_windows

# Expects a string in the form of "YYYY-mm-dd"
def get_date_object(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()

# Expects a date in the form of "YYYY-mm-dd"
def get_weekday(date):
    return get_date_object(date).isoweekday()

def group_activities_by_week():
    pass


activities = get_athlete_activities(95573308)

timeframe = get_activity_list_timeframe(activities)
print(f'\nTimeframe: {timeframe}\n')

date_windows = get_date_windows(timeframe[0], timeframe[1])
print(date_windows)
# group_activities_by_week(activities)