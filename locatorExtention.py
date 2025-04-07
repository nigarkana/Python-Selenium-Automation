import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, 'Forgot password?').click() #it would be a lind and a tag will be there
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys("nigarkana@gmail.com")
driver.find_element(By.CSS_SELECTOR,'form div:nth-child(2) input').send_keys("12345")
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(3) input').send_keys("12345")
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#using the text, if there is not link and anchor tag, it will work
driver.find_element(By.XPATH, "//button[text()='Save New Password']").send_keys("12345")
passwordReset = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").text
print(passwordReset)
assert 'Save New Password' in passwordReset


time.sleep(2)