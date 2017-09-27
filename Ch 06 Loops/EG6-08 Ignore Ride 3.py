# EG6-08 Ignore Ride 3
while True:
    ride_number_text = input('Please enter the ride number you want: ')
    ride_number = int(ride_number_text)
    if ride_number == 3:
        print('Sorry, this ride is not available')
        continue
    print('You have selected ride number:',ride_number)
