import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
#Close() Close single browser window
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"YouTube").click()
time.sleep(3)
driver.close()#executed
#driver.quit: close multiple browser window and this kill the process
driver.quit()#executed