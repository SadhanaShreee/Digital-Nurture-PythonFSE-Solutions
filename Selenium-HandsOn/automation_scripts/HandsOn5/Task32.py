from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize browser
driver.maximize_window()

# Open Simple Form Demo page
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")


# 1. Locate by ID

element_id = driver.find_element(By.ID, "user-message")
print("Located using ID:", element_id)


# 2. Locate by NAME

element_name = driver.find_element(By.NAME, "message")
print("Located using NAME:", element_name)


# 3. Locate by CLASS_NAME

element_class = driver.find_element(By.CLASS_NAME, "form-control")
print("Located using CLASS_NAME:", element_class)


# 4. Locate by TAG_NAME

element_tag = driver.find_element(By.TAG_NAME, "input")
print("Located using TAG_NAME:", element_tag)


# 5. Locate by Absolute XPath

element_abs_xpath = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section[2]/div/div/div[1]/div/div[2]/div/input"
)
print("Located using Absolute XPath:", element_abs_xpath)


# 6. Locate by Relative XPath

element_rel_xpath = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("Located using Relative XPath:", element_rel_xpath)

# Close browser
driver.quit()