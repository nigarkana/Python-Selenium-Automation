import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

# service_obj = Service("/Users/nigarkana/Documents/QA/Selenium-Python")
# driver  = webdriver.Chrome(service = service_obj)

driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)





time.sleep(2)