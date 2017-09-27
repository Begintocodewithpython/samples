# EG12-01 Simple Function References

def func_1(): 
    print('hello from function 1')

def func_2(): 
    print('hello from function 2')

x = func_1 
x() 
x = func_2 
x() 
