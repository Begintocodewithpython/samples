# EG12-04 Lamdba Example

# Create a list of numbers
numbers = [1,2,3,4,5,6,7,8]

# Create an increment function
def increment(x):
    return x+1

# Use the increment function to make an incremented list
new_numbers_increment = map(increment, numbers)

# print the incremented list
print('Increment list: ', list(new_numbers_increment))

# Use a lambda function to make an incremented list
new_numbers_lambda = map(lambda x : x+1, numbers)

# print the lambada incremented list
print('Increment list: ', list(new_numbers_lambda))
