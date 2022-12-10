
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='product_549']").click()
driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Shah Rehan")

driver.find_element(By.XPATH, "//input[@id='dob']").click()

datepicker_month= Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Jan")
datepicker_year= Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1989")

alldates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text=="13":
        date.click()
        break


driver.find_element(By.XPATH, "//input[@id='sex_1']").click()
driver.find_element(By.XPATH, "//input[@id='traveltype_1']").click()

driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Hyderabad")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("New Delhi")



driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("9502465879")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("rehanmind1@gmail.com")

drpcountry = Select(driver.find_element(By.XPATH, "//span[@title='Pakistan']"))
drpcountry.select_by_value("PK")


#allcountry=Select(driver.find_element(By.ID, "//span[@id='select2-billing_country-container']"))

#alloptions=allcountry.options

#for opt in alloptions:
#     if opt.text=="Pakistan":
#       opt.click()
#        break



