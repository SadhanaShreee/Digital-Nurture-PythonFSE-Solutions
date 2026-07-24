from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print page title
print("Page Title:", driver.title)

# Close browser
driver.quit()