# EG8-02 Read and Display

from BTCInput import * 

sales=[] 

for count in range(1,11): 
    prompt='Enter the sales for stand ' + str(count) + ': ' 
    sales.append(read_int(prompt)) 

print(sales)
