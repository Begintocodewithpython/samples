# EG9-09 Alarm access control

from BTCInput import *

# Create the dictionary 
access_control={1234:'complete', 1111:'limited', 4342:'limited'}
# Read in an access code
access_code=read_int('Enter your access code: ')
# Check the access level
if access_code in access_control: 
    print('You have', access_control[access_code], 'access') 
else:
    print('You are not allowed access') 
