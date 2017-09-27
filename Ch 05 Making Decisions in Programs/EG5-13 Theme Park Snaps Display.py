# EG5-13 Theme Park Snaps Display

import snaps

snaps.display_image('themepark.png')

prompt='''These are the available rides

1: Scenic River Cruise
2: Carnival Carousel
3: Jungle Adventure Water Splash
4: Downhill Mountain Run
5: The Regurgitator

Select your ride: '''

ride_number_text = snaps.get_string(prompt,vert='bottom',
                                    max_line_length=3)

confirm='Ride ' + ride_number_text
snaps.display_message(confirm)
