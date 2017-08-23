from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://127.0.0.1/hotelmanagement/index.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
	print(name.get_text())