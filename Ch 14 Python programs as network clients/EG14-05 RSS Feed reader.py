# EG14-05 RSS Feed reader

import urllib.request
import xml.etree.ElementTree as ElementTree

url = 'https://www.robmiles.com/journal/rss.xml'
url = "http://feeds.bbci.co.uk/news/rss.xml"
url = "http://www.huffingtonpost.co.uk/feeds/index.xml"
url = "http://feeds.reuters.com/reuters/UKTopNews"

req = urllib.request.urlopen(url)
page=req.read()

doc = ElementTree.fromstring(page)

for item in doc.iter('item'):
    title = item.find('title').text
    print(title.strip())
    description = item.find('description').text
    print('    ',description.strip())
