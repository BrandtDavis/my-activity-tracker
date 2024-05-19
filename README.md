This is a Strava integration to help customize the way your data is presented.

### Authorization Steps
1. Update the client_id param, and navigate to http://www.strava.com/oauth/authorize?client_id=[REPLACE_WITH_YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read
  1. To access activities, change 'scope=read' to 'scope=activities:read' or 'scope=activities:read 
1. Save the value in the 'code' param of the resulting url
1. Use this value in the 'authorization.py' file as 'AUTHORIZATION_CODE'

### To Run Individual Test File
`python3 -m unittest tests/TestAuthorization.py`

### Sources Used for this Project
https://docs.python-guide.org/writing/structure/