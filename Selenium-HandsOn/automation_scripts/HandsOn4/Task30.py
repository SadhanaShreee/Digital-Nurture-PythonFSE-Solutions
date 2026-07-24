import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser window
driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Open Google in a new tab
driver.execute_script('window.open("https://www.google.com");')

# Get all window handles
tabs = driver.window_handles

# Switch to the Google tab
driver.switch_to.window(tabs[1])
print("Current Tab Title:", driver.title)

# Switch back to the original Selenium Playground tab
driver.switch_to.window(tabs[0])
print("Current Tab Title:", driver.title)

# Take a screenshot
screenshot_file = "playground_screenshot.png"
driver.save_screenshot(screenshot_file)

# Verify the screenshot file was created
if os.path.exists(screenshot_file):
    print("Screenshot created successfully.")
    print("File Name:", screenshot_file)
else:
    print("Screenshot was not created.")

# Close the browser
driver.quit()