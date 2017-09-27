# EG14-04 Python ElementTree

import xml.etree.ElementTree as ElementTree

rss_text = '''
<rss version="2.0"> 
  <channel> 
    <title> 
      robmiles.com 
    </title> 
    <item> 
      <title> 
        Water Meter Day
      </title>
      <category>Life</category> 
      <description> 
        <![CDATA[ We had a new water meter installed yay! ]]>
      </description>
    </item> 
    <item> 
      <title>
        Python now in Visual Studio 2017
      </title>
      <category>Python</category> 
      <category>Visual Studio</category> 
      <description>
        <![CDATA[ Python is now available in Visual Studio 2017 yay! ]]>
      </description>
    </item> 
  </channel> 
</rss>
'''

doc = ElementTree.fromstring(rss_text)
for item in doc.iter('item'):
    title = item.find('title').text
    print(title.strip())
    description = item.find('description').text
    print('    ',description.strip())
