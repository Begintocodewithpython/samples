# EG14-03 Web page reader

import urllib.request

url = 'https://www.robmiles.com'
 
req = urllib.request.urlopen(url)
for line in req:
    print(line)
