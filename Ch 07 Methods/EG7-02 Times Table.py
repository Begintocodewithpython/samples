# EG7-02 Times Table
def print_times_table(times_value):
    count = 1
    while count < 13:
        result = times_value * count
        print(count,'times', times_value,'equals',result)
        count = count + 1

print_times_table(6)
