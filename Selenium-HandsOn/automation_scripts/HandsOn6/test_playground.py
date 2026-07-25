import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation', '12345'])
def test_simple_form_submission(driver, base_url, message):
    driver.get(base_url + "simple-form-demo")

    wait = WebDriverWait(driver, 10)

    message_input = wait.until(
        EC.element_to_be_clickable((By.ID, "user-message"))
    )
    message_input.send_keys(message)

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )
    submit_btn.click()

    displayed_message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert displayed_message.text == message


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo/")
    wait = WebDriverWait(driver, 10)

    checkboxes_locator = (
        By.XPATH,
        "//*[self::h2 or self::h3 or self::h4][normalize-space()='Multiple Checkbox Demo']"
        "/following::input[@type='checkbox'][position()<=4]"
    )
    wait.until(EC.presence_of_all_elements_located(checkboxes_locator))

    first_checkbox = driver.find_elements(*checkboxes_locator)[0]

    first_checkbox.click()
    assert first_checkbox.is_selected() is True

    first_checkbox.click()
    assert first_checkbox.is_selected() is False


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo")

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(
        EC.element_to_be_clickable((By.ID, "select-demo"))
    )

    select = Select(dropdown_element)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text == "Wednesday"