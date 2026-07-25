"""
test_checkbox.py

Only assertions here. All checkbox interaction logic lives in
pages/checkbox_page.py.
"""

from pages.checkbox_page import CheckboxPage


def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + "checkbox-demo/")

    page.check_option(0)
    assert page.is_option_checked(0) is True

    page.uncheck_option(0)
    assert page.is_option_checked(0) is False
