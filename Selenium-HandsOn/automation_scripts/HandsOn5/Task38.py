import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
 
 
# TASK 38 — Wait for element to be clickable before clicking

 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
 
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
 
start = time.time()
wait = WebDriverWait(driver, 10)
success_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "autoclosable-btn-success"))
)
success_btn.click()
 
# Wait for the alert to actually become visible instead of a fixed sleep
alert = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
)
 
print("Alert Text:", alert.text)
 
end = time.time()
print("Execution Time using element_to_be_clickable():", round(end - start, 2), "seconds")
 
driver.quit()