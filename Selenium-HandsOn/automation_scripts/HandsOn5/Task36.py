from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser
driver.maximize_window()

# Open Bootstrap Alerts page
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

# Click the "Success Message" button
driver.find_element(By.ID, "autoclosable-btn-success").click()

# Wait until the success alert is visible
success_alert = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

# Get the alert text
alert_text = success_alert.text
print("Alert Text:", alert_text)

# Verify the alert contains 'successfully'
assert "successfully" in alert_text.lower()

print("Test Passed: Success alert displayed correctly.")

# Close browser
driver.quit()