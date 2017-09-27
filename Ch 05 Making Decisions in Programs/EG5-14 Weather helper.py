# EG5-14 Weather helper

import snaps

temp = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)

print('The temperature is:', temp)

if temp < 40:
    print('Wear a coat - it is cold out there')
elif temp > 70:
    print('Remember to wear sunscreen')
