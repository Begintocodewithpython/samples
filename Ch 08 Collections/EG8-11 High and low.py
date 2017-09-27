# EG8-11 High and low

# test sales data
sales=[50,54,29,33,22,100,45,54,89,75]

def highest_and_lowest():
    '''
    Print out the highest and the lowest sales values
    '''
    highest=sales[0]
    lowest=sales[0]
    for sales_value in sales:
        if sales_value>highest:
            highest=sales_value
        if sales_value<lowest:
            lowest=sales_value
    print('The highest is:', highest)
    print('The lowest is:', lowest)

highest_and_lowest()
