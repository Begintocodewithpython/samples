# EG7-04 Two Parameter Times Table
def print_times_table(times_value, limit):
    count = 1
    while count < limit+1:
        result = times_value * count
        print(count,'times', times_value,'equals',result)
        count = count + 1
print_times_table(6,5)
