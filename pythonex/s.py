from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen("https://www.mgtv.com/").read().decode('utf-8')
print(html)