from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = "A1680"
pwd = "A1680"
server = "PX"
database = "AUTO"
url = "https://px.afdrift.se/login/login.asp"

chromeLinuxPath="/usr/bin/google-chrome"


driver = webdriver.Chrome()
driver.get(url)

#Login Window
elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem = driver.find_element_by_name("server")
elem.send_keys(server)
elem = driver.find_element_by_name("database")
elem.send_keys(database)
elem.send_keys(Keys.RETURN)




#Go inside
time.sleep(2)
#elem = driver.find_elements_by_xpath("//*/td[@class='STARTTEXTBOLD' AND @valign='center']")
elem = driver.find_elements_by_xpath('//*[@class="STARTTEXTBOLD"]')
#/a[@src='../images/SWE/text_select.PNG']
print(elem)
#elem.click()
#https://px.afdrift.se/images/SWE/text_select.PNG
#driver.close()