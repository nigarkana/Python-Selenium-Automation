import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Mahid")
driver.find_element(By.NAME, 'email').send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys(("Test@job1"))
driver.find_element(By.CLASS_NAME, "form-check-input").click()
#driver.find_element(By.ID, "exampleFormControlSelect1").send_keys("Male").click()
#Xpath locator = //tagname[@attribute='value']
#CSS Selector (three ways we can select CSS Selector) = tagname[attribute ='value'], #id, .classname

#Static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
#dropdown.select_by_value()
dropdown.select_by_index('0')
dropdown.select_by_visible_text('Female')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Example")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


time.sleep(4)
