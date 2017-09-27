# EG8-06 Functions and Menu elif

#fetch the input functions
from BTCInput import *  

#create an empty sales list
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

def sort_high_to_low():
    '''
    Print out a list of the sales figures sorted hight to low
    '''
    pass

def sort_low_to_high():
    '''
    Print out a list of the sales figures sorted low to high
    '''
    pass

def highest_and_lowest():
    '''
    Print out the highest and the lowest sales values
    '''
    pass

def total_sales():
    '''
    Print out the total sales value
    '''
    pass

def average_sales():
    '''
    Print out the average sales value
    '''
    pass


# Start by reading in the sales
read_sales(10)

# Now get the command from the user

menu='''Ice Cream Sales

1: Print the sales
2: Sort High to Low
3: Sort Low to High
4: Highest and Lowest
5: Total Sales
6: Average sales
7: Enter Figures

Enter your command: '''

command=read_int_ranged(menu,1,7)
if command==1:
    print_sales()
elif command==2:
    sort_high_to_low()
elif command==3:
    sort_low_to_high()
elif command==4:
    highest_and_lowest()
elif command==5:
    total_sales()
elif command==6:
    average_sales()
elif command==7:
    read_sales(10)


