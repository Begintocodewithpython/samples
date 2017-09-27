# EG6-05 Catching multiple exceptions
ride_number_valid=False            # create a flag value and set it to False
while ride_number_valid==False:    # repeat while the flag is False
    try:                           # start of code that might throw exceptions
        ride_number_text = input('Please enter the ride number you want: ') # read in some text
        ride_number = int(ride_number_text)  # convert the text into a number (might raise exception)
        ride_number_valid=True  # if we get here we know the number is OK. Set the flag.
    except ValueError:          # the handler for an invalid number 
        print('Invalid number text. Please enter digits.') # display a message
    except KeyboardInterrupt:   # the handler for an interrupt 
        print('Please do not try to stop the program.') # display a message
# When we get here we have a valid ride number
print('You have selected ride',ride_number)
