# EG8-17 Save sales

# test sales data
sales=[50,54,29,33,22,100,45,54,89,75]

def save_sales(file_path):
    '''
    Saves the contents of the sales list in a file
    file_path gives the path to the file to save
    Raises file exceptions if the save fails
    '''
    print('Save the sales in:', file_path)
    # Open the output file
    output_file=open(file_path,'w')
    # Write out the length of the sales list
    output_file.write(str(len(sales))+'\n')
    # Work through the sales values in the list
    for sale in sales:
        # write out the sale as a string
        output_file.write(str(sale)+'\n')
    # Close the output file
    output_file.close()

save_sales('sales.txt')
