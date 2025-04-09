import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ban")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class ='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Bangladesh":
        country.click()
        break

time.sleep(4)