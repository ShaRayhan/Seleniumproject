from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome(executable_path="E:\Software\chromedriver_win32\chromedriver.exe")

driver.get("https://phptravels.org/login/")

ele=driver.find_element("name","username")
print(ele.is_displayed()) # return true/false based on element status
print(ele.is_enabled()) # return true/false
pwd_ele=driver.find_element("name","password")
print(pwd_ele.is_displayed()) #return true/false based on element status
print(pwd_ele.is_enabled()) # return true/false
