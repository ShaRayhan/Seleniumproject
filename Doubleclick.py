from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(2)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
Field1=driver.find_element(By.XPATH, "//input[@id='field1']")
Field1.clear()
Field1.send_keys("Welcome")
buttun=driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")

act=ActionChains(driver)
act.double_click(buttun).perform()






