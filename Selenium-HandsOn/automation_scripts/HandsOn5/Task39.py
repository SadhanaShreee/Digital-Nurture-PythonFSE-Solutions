driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
 
# TODO: replace with the actual dynamic-table page/exercise you were given,
# e.g. the "Load Dynamic Table" / AJAX loading exercise on the playground.
driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
 
# Trigger whatever action loads the table dynamically here, e.g.:
# driver.find_element(By.ID, "someLoadTableButton").click()
 
fluent_wait = WebDriverWait(
    driver,
    timeout=10,                 # maximum wait: 10 seconds
    poll_frequency=0.5,         # poll every 500 ms
    ignored_exceptions=[NoSuchElementException]  # ignore this error while polling
)
 
# TODO: replace the locator below with the real dynamic table row locator
table_row = fluent_wait.until(
    lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr")
)
 
print("Dynamically loaded row text:", table_row.text)
 
driver.quit()