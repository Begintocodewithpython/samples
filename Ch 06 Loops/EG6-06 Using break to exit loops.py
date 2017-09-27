# EG6-06 Using break to exit loops
while True:    # repeat forever
    try:                           # start of code that might throw exceptions
        ride_number_text = input('Please enter the ride number you want: ') # read in some text
        ride_number = int(ride_number_text)  # convert the text into a number (might raise exception)
        break                   # if we get here we know the number is OK. Break out of the loop.
    except ValueError:          # the handler for an invalid number 
        print('Invalid number text. Please enter digits.') # display a message
    except KeyboardInterrupt:   # the handler for an interrupt 
        print('Please do not try to stop the program.') # display a message
# When we get here we have a valid ride number
print('You have selected ride',ride_number)
