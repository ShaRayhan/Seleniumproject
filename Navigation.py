from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Chrome(executable_path="E:\Software\chromedriver_win32\chromedriver.exe")

driver.get("https://www.makingsenseofcents.com/")

print(driver.title) #moneycent site

driver.get("https://logicaldollar.com/")
time.sleep(5)

print(driver.title) #dollarsite
driver.back()

time.sleep(5)
print(driver.title) #moneycent site

driver.forward()
time.sleep(5)
print(driver.title) #Dollar site