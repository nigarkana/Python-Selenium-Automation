from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")

print(len(checkboxes))
#print(driver.find_elements(By.XPATH, "//input[@type = 'checkbox']").text)

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break



time.sleep(4)