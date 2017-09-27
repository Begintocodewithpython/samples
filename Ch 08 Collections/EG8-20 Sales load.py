# EG8-EG8-19 Sales load

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
    # Open the output file
    output_file=open(file_path,'w')
    # Work through the sales values in the list
    for sale in sales:
        # write out the sale as a string
        output_file.write(str(sale)+'\n')
    # Close the output file
    output_file.close()

def load_sales(file_path):
    '''
    Loads the sales list from a file 
    file_path gives the path to the file to load
    Raises file exceptions if the load fails
    '''
    print('Load the sales from:', file_path)
    # Clear the sales array
    sales.clear()
    # Open the file for input
    input_file=open(file_path,'r')
    for line in input_file:
        line=line.strip()
        sales.append(int(line))
       

save_sales('sales.txt')
load_sales('sales.txt')
print_sales()
