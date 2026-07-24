from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser
driver.maximize_window()

# Open Checkbox Demo page
driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")


# 1. Find the first checkbox label using text()

option1 = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("First Checkbox Label:", option1.text)


# 2. Find all option labels using contains()

options = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("\nCheckbox Labels:")

for option in options:
    print(option.text)

# Close browser
driver.quit()