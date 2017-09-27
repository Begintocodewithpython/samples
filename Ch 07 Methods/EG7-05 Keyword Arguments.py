# EG7-05 Keyword Arguments
def print_times_table(times_value, limit):
    count = 1
    while count < limit+1:
        result = times_value * count
        print(count,'times', times_value,'equals',result)
        count = count + 1
        
print_times_table(times_value=12,limit=7)
