from bs4 import BeautifulSoup
import requests

url1 = "http://testphp.vulnweb.com/"
source = requests.get(url1).text
soup =  BeautifulSoup(source, 'lxml')
print("all href links:-")
links = soup.find_all('a')
for link in links:
	if(link['href'][0:4] == "http"):
		print(link['href'])
	else:
		print(url1 + link['href'] )
print()

source = requests.get("http://testphp.vulnweb.com/artists.php").text
soup =  BeautifulSoup(source, 'lxml')
print(soup.find('title').text + ":-")
artists = soup.find_all(class_="story")
for artist in artists:
	print(artist.a.h3.text)
print()

source = requests.get("http://testphp.vulnweb.com/categories.php").text
soup =  BeautifulSoup(source, 'lxml')
print(soup.find('title').text + ":-")
headlines = soup.find_all(class_="story")
for headline in headlines:
	print(headline.a.h3.text)

#xss

#sql