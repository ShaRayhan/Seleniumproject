from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()#driver.maximize_window()
#Absolute xpath
#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("laptops")
#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

#Relative xpath
#driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("laptops")
#driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

#Xpath OR & AND Option
#driver.find_element(By.XPATH, "//input[@id='small-searchterms' or @name='q' ]").send_keys("laptops")
#driver.find_element(By.XPATH, "//button[@type='submit' and @class='button-1 search-box-button']").click()
#sleep(3)
#driver.close()

#Contains() & Start-with()
#driver.find_element(By.XPATH,"//input[contains(@id,'small')]").send_keys("laptops")
#driver.find_element(By.XPATH,"//button[starts-with(@class, 'button')]").click()
#driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/ul[1]/li[1]/a").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[1]/a").click()

driver.find_element(By.XPATH,"//html/body/div[6]/div[3]/div/div[2]/div[1]/div[2]/ul/li[1]/ul/li[1]/a").click()