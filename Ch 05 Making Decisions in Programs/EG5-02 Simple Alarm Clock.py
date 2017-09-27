# EG5-02 Simple Alarm Clock

import time

current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min

it_is_time_to_get_up = (hour>7) or (hour==7 and minute>29) 

if it_is_time_to_get_up:
    print('IT IS TIME TO GET UP')
    
