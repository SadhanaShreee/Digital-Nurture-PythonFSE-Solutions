from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser window
driver.maximize_window()

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Open a new browser tab with Google
driver.execute_script('window.open("https://www.google.com");')

# Get all open window/tab handles
tabs = driver.window_handles

# Print all tab handles
print("Open Tabs:", tabs)

# Switch to the second tab (Google)
driver.switch_to.window(tabs[1])

# Print the title of the Google tab
print("Google Tab Title:", driver.title)

# Close the browser
driver.quit()