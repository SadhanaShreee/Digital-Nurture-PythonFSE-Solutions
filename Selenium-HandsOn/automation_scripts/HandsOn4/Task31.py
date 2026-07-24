from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Get the current browser window size
current_size = driver.get_window_size()
print("Current Window Size:", current_size)

# Set the browser window size to 1280 x 800
driver.set_window_size(1280, 800)

# Verify the new window size
new_size = driver.get_window_size()
print("New Window Size:", new_size)


# Why use a consistent window size?
#
# Using the same browser size ensures that:
# 1. The web page layout remains consistent across test runs.
# 2. Responsive websites display the same elements and layout.
# 3. Tests produce reliable and repeatable results.
# 4. Element locations do not change due to different screen sizes.
# 5. It reduces failures caused by responsive design changes.

# Close the browser
driver.quit()