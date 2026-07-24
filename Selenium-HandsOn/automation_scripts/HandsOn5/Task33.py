from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser
driver.maximize_window()

# Open Simple Form Demo page
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")


# 1. CSS Selector using ID

element1 = driver.find_element(By.CSS_SELECTOR, "#user-message")
print("Located using CSS ID:", element1)


# 2. CSS Selector using Attribute

element2 = driver.find_element(By.CSS_SELECTOR, "input[name='message']")
print("Located using CSS Attribute:", element2)


# 3. CSS Selector using Parent > Child

element3 = driver.find_element(By.CSS_SELECTOR, "div > input")
print("Located using Parent > Child:", element3)

# Close browser
driver.quit()