from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
# drp-country_ele=driver.find_elements(By.XPATH, "//select[@id='input-country']")# web-element capture
drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))  # In Selenium, we have select
# class

# select option from the dropdown
#drpcountry.select_by_visible_text("Pakistan")
#drpcountry.select_by_value("54") #india
#drpcountry.select_by_index(13)  # index
#driver.close()

#capture all the option
alloptions=drpcountry.options
print("total no of options:",len(alloptions))

#for opt in alloptions:
    #print(opt.text)

#select option from dropdown without using built in method
for opt in alloptions:
    if opt.text=="Pakistan":
        opt.click()
        break