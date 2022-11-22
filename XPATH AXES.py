from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\Software\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#SELF

#text_msg=driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[3]/td[1]/a").text
#print(text_msg) #JaiprakashAssociates #IFB Industries
#text_msg=driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a").text
#print(text_msg) #JaiprakashAssociates #IFB Industries

#CHILD
#childs=driver.find_elements(By.XPATH, ("//*[@id='leftcontainer']/table/tbody/tr[7]/td[1]/a/ancestor::tr/child::td"))
#print(len(childs))
#driver.close()

#parent
#text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/parent::td").text
#print(text_msg) #JaiprakashAssociates

#Ancestor
#text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr").text
#print(text_msg) #JaiprakashAssociates A 8.78 9.53 + 8.54

#descendants=driver.find_elements(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr/descendant::*")
#print("N0 of descendants:",len(descendants))#No of descendant is 7

#Following
#followings=driver.find_elements(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr/following::*")
#print("N0 of Followings:",len(followings))#2575

#Followingsiblings
#followingsiblings=driver.find_elements(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr/following-sibling::*")
#print("N0 of Followingsibling:",len(followingsiblings))

#preceding
#precedings=driver.find_elements(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr/preceding::*")
#print("N0 of preceding:",len(precedings))#//a[normalize-space()='JaiprakashAssociates']

#precedingsibling
#precedingsiblings=driver.find_elements(By.XPATH, "//a[contains(text(),'JaiprakashAssociates')]/ancestor::tr/preceding-sibling::*")
#print("N0 of precedingsiblings:",len(precedingsiblings))

driver.close()