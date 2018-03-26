from bs4 import BeautifulSoup
import requests


url="https://en.wikipedia.org/wiki/Sachin_Tendulkar"
r=requests.get(url)

soup=BeautifulSoup(r.content)
links=soup.find_all("p")
for link in links:
	print "<a href='%s'>%s</a>"%(link.get("href"),link.text)

g_data=soup.find_all("div",{"class":"infobox vcard"})

for item in g_data:
	print item.contents[1].text
