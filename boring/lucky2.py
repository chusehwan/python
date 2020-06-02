
import requests
import sys
import webbrowser


word_to_search='test'

request = requests.get('http://google.com/search?q='+word_to_search)
content=request.content.decode('UTF-8','replace')

#
# Parse the content and get the links.  I had a problem with
# bs4 so I manually searched over the content
#
links=[]
while '<h3 class="r">' in content:
    content=content.split('<h3 class="r">', 1)[1]
    split_content=content.split('</h3>', 1)
    link='http'+split_content[1].split(':http',1)[1].split('%',1)[0]
    links.append(link)
    content=split_content[1]


for link in links[:5]:  # max number of links 5
    webbrowser.open(link)