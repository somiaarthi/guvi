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

# TC_001
print("To verify the Login functionality with valid credentials")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("papper")
driver.find_element(By.NAME,"password").send_keys("seemaa@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.close()

# Tc_002
print("To verify the login button wih invalid credentials")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("Aarthi")
driver.find_element(By.NAME,"password").send_keys("invalidpassword")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
username=driver.find_element(By.XPATH,"//p[text()='Invalid credentials']")
print("User has entered:",username.text)
print("This line will execute only if Test case Tc_002 passes")
driver.close()

#Tc_005 Delete a Record
print("Verify the Delete button")
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.LINK_TEXT,"PIM").click()
driver.find_element(By.XPATH,"//*[@class='oxd-icon bi-trash']").click()
driver.find_element(By.XPATH,"//*[text()=' Yes, Delete ']").click()
print("Sucesfully delete employee and passed Tc_005")

#Tc_004
print("Verify the Edit button by editing the date field")
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(2000)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.LINK_TEXT,"PIM").click()
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']").click()
driver.find_element(By.XPATH,"//*[@placeholder='yyyy-mm-dd']").send_keys("2023-05-12")
driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]").clear()
driver.find_element(By.XPATH,"(//*[@placeholder='yyyy-mm-dd'])[2]").send_keys("2023-05-30")
driver.find_element(By.LINK_TEXT,"Female").click()
driver.find_element(By.XPATH,"//form/div[5]/button").click()
print("This will execute only if record is been edited and saved")
driver.close()

# Tc_003
print("Verify the Add button by adding new customers")
driver=webdriver.Chrome();
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
driver.maximize_window();
driver.implicitly_wait(2000);
driver.find_element(By.NAME,"username").send_keys("Admin");
driver.find_element(By.NAME,"password").send_keys("admin123");
driver.find_element(By.XPATH,"//button[@type='submit']").click();
driver.find_element(By.LINK_TEXT,"PIM").click();
driver.find_element(By.PARTIAL_LINK_TEXT,"Add").click();
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Pinkz");
driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("Das");
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Dasari");
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("1234");
#WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//input[@type='checkbox']")));
driver.find_element(By.XPATH,"//form/div[1]/div[2]/div[2]/div/label/span").click();
driver.find_element(By.XPATH,"(//*[@class='oxd-input oxd-input--active'])[3]").send_keys("paperrr");
driver.find_element(By.XPATH,"(//*[@type='password'])[1]").send_keys("seemaa@1234");
driver.find_element(By.XPATH,"(//*[@type='password'])[2]").send_keys("seemaa@1234");
driver.find_element(By.XPATH,"//button[@type='submit']").click();
driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys("2023-05-30");
driver.find_element(By.XPATH,"//form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/i").click();
ActionChains(driver).key_down(Keys.ARROW_DOWN).click().perform()
driver.find_element(By.XPATH,"//div[text()='American']").click()
driver.find_element(By.XPATH,"(//*[@placeholder='yyyy-mm-dd'])[2]").send_keys("2023-05-30");
driver.find_element(By.XPATH,"//form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span").click();
driver.find_element(By.XPATH,"//form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i").click();
driver.find_element(By.XPATH,"(//button[@type='submit'])").click();
driver.find_element(By.XPATH,"(//*[@type='submit'])[2]").click()
print("This print statement will execute only Tc_003 passes");
driver.close();

















