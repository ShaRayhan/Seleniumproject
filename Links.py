import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#click on link
#driver.find_element(By.LINK_TEXT,"Books").click()
#time.sleep(2)
#find the no of links on a page

#links=driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print("total no of links",len(links))

#print all the links
for link in links:
    print(link.text)