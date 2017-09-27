# EG5-10 Ride Selector Start

print('''Welcome to our Theme Park

These are the available rides:

1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator
''')

ride_number_text = input('Please enter the ride number you want: ')
ride_number = int(ride_number_text)

if ride_number == 1:
    print('You have selected the Scenic River Cruise')
    print('There are no age limits for this ride')
