# Teletype printer

import time

def teletype_print(text,delay=0.1):
    for ch in text:
        print(ch,end='')
        time.sleep(delay)
    print()

teletype_print('Hello world')
