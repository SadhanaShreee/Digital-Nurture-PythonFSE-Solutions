from selenium import webdriver
from selenium.webdriver.common.by import By

# Create Chrome WebDriver
driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(10)


driver.get("https://demoqa.com/text-box")

# Example
name = driver.find_element(By.ID, "userName")
name.send_keys("John")

driver.quit()