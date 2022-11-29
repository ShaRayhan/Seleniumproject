import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0 #taking variable initially

for link in alllinks:#for loop statements
    url=link.get_attribute('href')# capture href attribute value
    res=requests.head(url)#request send to server & server will respond with code
    if res.status_code>=400:#from this respond will decide broken link
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")
print("total no of broken links:", count)
