# EG8-13 Average Sales

# test sales data
sales=[50,54,29,33,22,100,45,54,89,75]

def average_sales():
    '''
    Print out the average sales value
    '''
    total=0
    for sales_value in sales:
        total = total+sales_value
    average_sales=total/len(sales)
    print('Average sales are:', average_sales)

average_sales()
