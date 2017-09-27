# EG7-03 Safe Times Table
def print_times_table(times_value):
    if isinstance(times_value,int)== False:
        raise Exception('print_times_table only works with integers')
    count = 1
    while count < 13:
        result = times_value * count
        print(count,'times', times_value,'equals',result)
        count = count + 1
#this will work fine
print_times_table(6)
#this will raise an exception
print_times_table('six')
