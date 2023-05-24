from gettext import gettext

import pytest
import time
import json

import self as self
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

#Tc_001
print("To verify the forgot password button is clickable")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("papper")
driver.find_element(By.XPATH,"//div[@class='orangehrm-login-forgot']").click()
driver.find_element(By.NAME,"username").send_keys("papper")
driver.find_element(By.XPATH," //button[@type='submit']").click()
#driver.find_element(By.LINK_TEXT," Reset Password ")
username=driver.find_element(By.XPATH,"//h6[text()='Reset Password link sent successfully']")
print("Confirmation Message is:" ,username.text)
driver.close()



#Tc_003
print("To verify the Admin options on the page")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
admin=driver.find_element(By.XPATH,"//span[text()='Admin']")
print(admin.text)
pim=driver.find_element(By.XPATH,"//span[text()='PIM']")
print(pim.text)
leave=driver.find_element(By.XPATH,"//*[text()='Leave']")
print(leave.text)
time=driver.find_element(By.XPATH,"//*[text()='Time']")
print(time.text)
rec=driver.find_element(By.XPATH,"//*[text()='Recruitment']")
print(rec.text)
myinfo=driver.find_element(By.XPATH,"//*[text()='My Info']")
print(myinfo.text)
performance=driver.find_element(By.XPATH,"//*[text()='Performance']")
print(performance.text)
dash=driver.find_element(By.XPATH,"//*[text()='Dashboard']")
print(dash.text)
maintain=driver.find_element(By.XPATH,"//*[text()='Maintenance']")
print(maintain.text)
buzz=driver.find_element(By.XPATH,"//*[text()='Buzz']")
print(buzz.text)
driver.close()

#Tc_002
print("To verify the OrangeHRM Title")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
titlemy=driver.title
print("The Page title is:",titlemy)
driver.find_element(By.LINK_TEXT,"Admin").click()
username1=driver.find_element(By.XPATH,"//h6[text()='User Management']")
print("The Option",username1.text,"is visible")
job=driver.find_element(By.XPATH,"//span[text()='Job ']")
print("The Option",job.text,"is visible")
Organization=driver.find_element(By.XPATH,"//span[text()='Organization ']")
print("The Option",Organization.text,"is visible")
quali=driver.find_element(By.XPATH,"//span[text()='Qualifications ']")
print("The Option",quali.text,"is visible")
Configuration=driver.find_element(By.XPATH,"//span[text()='Configuration ']")
print("The Option",Configuration.text,"is visible")
#national=driver.find_element(By.XPATH,"//*[text()='Nationalities ']")
#print("The Option",national.text,"is visible")
corporate=driver.find_element(By.XPATH,"//*[text()='Corporate Branding ']")
print("The Option",corporate.text,"is visible")
driver.close()


