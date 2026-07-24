from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")


# 1. By.ID (Most Preferred)
# Reason:
# - Usually unique
# - Fastest locator
# - Easy to read and maintain

driver.find_element(By.ID, "user-message")


# 2. By.NAME
# Reason:
# - Usually stable
# - Easy to understand
# - May not always be unique

driver.find_element(By.NAME, "message")


# 3. By.CSS_SELECTOR
# Reason:
# - Fast and flexible
# - Easier to maintain than XPath
# - Supports ID, class, and attribute selection

driver.find_element(By.CSS_SELECTOR, "#user-message")


# 4. Relative XPath
# Reason:
# - Useful when ID or NAME is unavailable
# - More reliable than Absolute XPath
# - Can become lengthy if overused

driver.find_element(By.XPATH, "//input[@id='user-message']")


# 5. By.CLASS_NAME
# Reason:
# - Multiple elements can share the same class
# - UI framework changes may break the locator

driver.find_element(By.CLASS_NAME, "form-control")


# 6. By.TAG_NAME / Absolute XPath (Least Preferred)
# Reason:
# - TAG_NAME is rarely unique
# - Absolute XPath breaks easily if HTML changes
# - Difficult to maintain

driver.find_element(By.TAG_NAME, "input")

driver.quit()