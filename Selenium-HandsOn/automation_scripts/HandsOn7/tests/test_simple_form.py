"""
test_simple_form.py

This test file contains ONLY assertions (what should happen).
All interaction with the page (how to make it happen) lives in
pages/simple_form_page.py. There are zero driver.find_element calls here.
"""

from pages.simple_form_page import SimpleFormPage


def test_simple_form_submission(driver, base_url):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")

    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"
