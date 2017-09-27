import urllib.request
import xml.etree.ElementTree

# EG14-06 Weather Feed Reader

def get_weather_temp(latitude,longitude):
    address = 'http://forecast.weather.gov/MapClick.php' 
    query = '?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml'.\
            format(latitude,longitude)
    req=urllib.request.urlopen(address+query) 
    page=req.read() 
    doc=xml.etree.ElementTree.fromstring(page) 
    for d in doc.iter('temperature'): 
        if d.get('type') == 'apparent': 
            text_temp_value = d.find('value').text 
            return int(text_temp_value) 


def get_weather_desciption(latitude,longitude):
    '''
    Uses forecast.weather.gov to get the weather
    for the specified latitude and longitude
    '''
    address = 'http://forecast.weather.gov/MapClick.php'
    query = '?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml'.\
        format(latitude,longitude)
    req=urllib.request.urlopen(address+query)
    page=req.read()
    doc=xml.etree.ElementTree.fromstring(page)
    for d in doc.iter('data'):
        if d.get('type') == 'current observations':
            param = d.find('parameters')
            weather = param.find('weather')
            conditions = weather.find('weather-conditions')
            return conditions.get('weather-summary')
                       
if __name__ == '__main__':
    temp = get_weather_temp(latitude=47.61, longitude=-122.33)
    print('The temperature is:', temp)
    temp = get_weather_desciption(latitude=47.61, longitude=-122.33)
    print('The weather is:', temp)

