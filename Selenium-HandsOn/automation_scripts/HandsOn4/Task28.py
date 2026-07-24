from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser window
driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Click on "Simple Form Demo" link
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify the URL contains 'simple-form-demo'
assert "simple-form-demo" in driver.current_url

print("URL Verification Passed!")
print("Current URL:", driver.current_url)

# Navigate back to the Selenium Playground
driver.back()

print("Returned to:", driver.title)

# Close the browser
driver.quit()