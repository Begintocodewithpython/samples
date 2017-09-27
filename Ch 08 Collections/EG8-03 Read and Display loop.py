# EG8-03 Read and Display loop

#fetch the input functions
from BTCInput import *  

#create an empty sales list
sales=[]

# read in 10 sales figures 
for count in range(1,11):
    # assemble a prompt string
    prompt='Enter the sales for stand ' + str(count) + ': '
    # read a value and append it to sales array
    sales.append(read_int(prompt))

# print a heading
print('Sales figures')
# initialise the stand counter
count=1
# work through the sales figures and print them
for sales_value in sales:
    # print an item
    print('Sales for stand', count,'are',sales_value)
    # advance the stand counter
    count = count + 1         
