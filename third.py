from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen("http://127.0.0.1/hotelmanagement/index.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table", {"id":"giftList"}).children:
	print(child)