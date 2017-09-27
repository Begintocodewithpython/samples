# EG4-03 Ultra-precise Egg Timer

import time

time_text = input('Enter the cooking time in seconds: ')  

time_float = float(time_text)

print('Put the egg in boiling water now')

time.sleep(time_float)

print('Take the egg out now')
