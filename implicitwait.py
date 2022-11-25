import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)#Implicit_Wait

driver.get("https://www.google.com/")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
#driver.find_element(By.NAME, "q").send_keys("Selenium")
#driver.find_element(By.NAME, "q").submit()
driver.refresh()
time.sleep(3)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
