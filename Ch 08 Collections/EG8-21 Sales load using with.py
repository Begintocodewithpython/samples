# EG8-21 Sales load using with

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

def save_sales(file_path):
    '''
    Saves the contents of the sales list in a file
    file_path gives the path to the file to save
    Raises file exceptions if the save fails
    '''
    print('Save the sales in:', file_path)
    try:
        # create a file object 
        with open(file_path,'w'):
            # Work through the sales values in the list
            for sale in sales:
                # write out the sale as a string
                output_file.write(str(sale)+'\n')
    except:
        print('Something went wrong writing the file')

def load_sales(file_path):
    '''
    Loads the sales list from a file 
    file_path gives the path to the file to load
    Raises file exceptions if the load fails
    '''
    print('Load the sales from:', file_path)
    # Clear the sales array
    sales.clear()
    try:
        with open(file_path,'r') as input_file:
            # Read each line of the file
            for line in input_file:
                # strip of the line ending
                line=line.strip()
                # convert the text into a number
                # and append it to the sales list
                sales.append(int(line))
    except:
        print('Something went wrong reading the file')

save_sales('sales.txt')
load_sales('sales.txt')
print_sales()
