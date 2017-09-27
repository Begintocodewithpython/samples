# EG4-02 User Configurable Egg Timer

import time

time_text = input('Enter the cooking time in seconds: ')  

time_int = int(time_text)

print('Put the egg in boiling water now')

time.sleep(time_int)

print('Take the egg out now')
