@py.exe D:\¼¼È¯\python\boring\lucky.py &*
#! python3

import webbrowser, requests, bs4 , sys

print('Googling...')
res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
#
soup = bs4.BeautifulSoup(res.text, features="lxml")

linkElems = soup.select('div#main > div > div > div > a')  
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get("href"))