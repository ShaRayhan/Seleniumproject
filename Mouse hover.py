from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

Computer=driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
Notebook=driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']")


act=ActionChains(driver)

act.move_to_element(Computer).move_to_element(Notebook).click().perform()

