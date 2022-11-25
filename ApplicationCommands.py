from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")#get()
driver.maximize_window()

#print(driver.title)#title
#print(driver.current_url)#current_url
#driver.close()
#is_displayed(), is_enabled()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",searchbox.is_displayed())#Displaye status:true
print("Enabled status:",searchbox.is_enabled())#Enabled status:True

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("dafault radio buttons status...")
print(rd_male.is_selected())#False
print(rd_female.is_selected())#False
rd_male.click()
print("after selecting male radio button...")
print(rd_male.is_selected())#True
print(rd_female.is_selected())#True
driver.close()