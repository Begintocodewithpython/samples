# EG8-10 Sort low to high

# test sales data
sales=[50,54,29,33,22,100,45,54,89,75]

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

def sort_low_to_high():
    '''
    Print out a list of the sales figures sorted hight to low
    '''
    for sort_pass in range(0,len(sales)):
        done_swap=False
        for count in range(0,len(sales)-1-sort_pass):
            if sales[count]>sales[count+1]:
                temp=sales[count]
                sales[count]=sales[count+1]
                sales[count+1]=temp
                done_swap=True
        if done_swap==False:
            break
    print_sales()

sort_low_to_high()
