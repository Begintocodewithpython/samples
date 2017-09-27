# EG12-4 Robot Dancer

import time

def forward():
    print('robot moving forward')
    time.sleep(1)

def back():
    print('robot moving back')
    time.sleep(1)

def left():
    print('robot moving left')
    time.sleep(1)

def right():
    print('robot moving right')
    time.sleep(1)

dance_moves = [forward, back, left, right]

print('Dance starting')
for move in dance_moves:
    move()
print('Dance over')
