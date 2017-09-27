# EG8-12 Total Sales

# test sales data
sales=[50,54,29,33,22,100,45,54,89,75]

def total_sales():
    '''
    Print out the total sales value
    '''
    total=0
    for sales_value in sales:
        total = total+sales_value
    print('Total sales are:', total)

total_sales()
