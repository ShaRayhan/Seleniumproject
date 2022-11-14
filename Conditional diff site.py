from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="E:\Software\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

user_ele=driver.find_element("name","userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())
pwd_ele=driver.find_element("name","password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element("name","submit").click()

roundtrip_radio=driver.find_element("by.cssSelector",("input[value=roundtrip]"))
print("status of roundtrip radio button",roundtrip_radio.is_selected())

oneway_radio=driver.find_element("by.cssSelector", ("input[value=oneway]"))
print("status of one way radio button",oneway_radio.is_selected())



