import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Open Bootstrap Alerts Demo
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

# Start timer
start = time.time()

# Click Success Message button
driver.find_element(By.ID, "autoclosable-btn-success").click()

# Fixed wait (always waits 3 seconds)
time.sleep(3)

# Read alert text
alert = driver.find_element(By.CSS_SELECTOR, ".alert-success")

print("Alert Text:", alert.text)

# End timer
end = time.time()

print("Execution Time using sleep():", round(end - start, 2), "seconds")

driver.quit()