from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://webdriveruniversity.com/")
driver.maximize_window() #to maximize the browser

links=driver.find_elements(By.TAG_NAME,"a") # total no of links on web page
print("total no of links")

print(len(links))
driver.close()