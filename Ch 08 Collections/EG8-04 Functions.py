# EG8-03 Functions

#fetch the input functions
from BTCInput import *  

#sales list used by the program
sales=[]

def read_sales(no_of_sales):
    '''
    Reads in the sales values and stores them in
    the sales list.
    no_of_sales gives the number of sales values to store
    '''
    # remove all the previous sales values
    sales.clear()
    # read in sales figures 
    for count in range(1,no_of_sales+1):
        # assemble a prompt string
        prompt='Enter the sales for stand ' + str(count) + ': '
        # read a value and append it to sales list
        sales.append(read_int(prompt))

def print_sales():
    '''
    Prints the sales figures on the screen with
    a heading. Each figure is numbered in seqeuence
    '''
    # print a heading
    print('Sales figures')
    # initialise the stand counter
    count=1
    # work through the sales figures
    for sales_value in sales:
        # print an item
        print('Sales for stand', count,'are',sales_value)
        # advance the stand counter
        count = count + 1         
#Program runs here
read_sales(10) 
print_sales() 

