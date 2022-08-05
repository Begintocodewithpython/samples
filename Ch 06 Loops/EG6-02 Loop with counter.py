# EG6-02 Loop with counter
count=0
while count<5:
    print('Inside loop')
    count=count+1
print('Outside loop')

# An example of count in a loop can be - 
n=int(input("enter number:"))
count=0
while n>0:
count=count+1
n=n//10
print("The Count of digits ",count)
