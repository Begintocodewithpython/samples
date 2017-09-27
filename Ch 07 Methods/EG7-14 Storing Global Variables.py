# EG7-14 Storing Global Variables

cheese=99

def func():
    global cheese
    cheese=100
    print('Global cheese is:',cheese)

func()
print('Global cheese is:',cheese)

