# EG12-06 Aribitrary Arguments

def add_function(*values): 
    total = 0 
    for value in values: 
        total = total + value 
    return total 

print(add_function())
print(add_function(1))
print(add_function(1, 2))
print(add_function(1, 2, 3))
print(add_function(1, 2, 3, 4))
print(add_function(1, 2, 3, 4, 5))

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(add_function(*num_list))
