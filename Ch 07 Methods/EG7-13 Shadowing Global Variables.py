# EG7-13 Shadowing Global Variables

cheese=99

def func():
    cheese=100
    print('Local cheese is:',cheese)

func()
print('Global cheese is:',cheese)

