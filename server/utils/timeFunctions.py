from datetime import datetime

# get the past x number of weeks
# Returns an array of dates in the format: DD-MM-YYYY

# Help: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
<<<<<<< HEAD
def get_last_x_weeks(x: int):
=======
def get_last_x_weeks(x: int, activityList):
>>>>>>> a83e715 (Add time timeFunctions)
    now = datetime.now()
    print(now.today().weekday())

get_last_x_weeks(3)