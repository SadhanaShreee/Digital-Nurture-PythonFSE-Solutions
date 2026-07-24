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
    driver.get(base_url + "checkbox-demo")

    wait = WebDriverWait(driver, 10)

    # The element exists as soon as the page loads, but a sticky header,
    # cookie banner, or ad on this page can sit ON TOP of it — so
    # element_to_be_clickable can time out even though the checkbox is
    # technically "present". Scrolling it to the center of the viewport
    # first moves it out from under any overlay before we wait on it.
    checkbox_el = driver.find_element(By.ID, "isAgeSelected")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox_el)

    first_checkbox = wait.until(
        EC.element_to_be_clickable((By.ID, "isAgeSelected"))
    )

    # Click to select
    first_checkbox.click()
    assert first_checkbox.is_selected() is True

    # Click again to deselect
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