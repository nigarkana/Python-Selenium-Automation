import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radioButtons = driver.find_elements(By.XPATH, "//input[@type = 'radio']")
print(len(radioButtons))

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio3":
        radioButton.click()
        assert radioButton.is_selected()
        break
#another way to handle radio button, if I know that the button will static
rodioButton1 = driver.find_elements(By.CSS_SELECTOR,".radioButton")
rodioButton1[1].click()


time.sleep(4)