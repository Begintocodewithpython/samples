# EG6-07 Loop with condition early ending
count=0
while count<5:
    print('Inside loop')
    count=count+1
    if count==3:
        break
print('Outside loop')
