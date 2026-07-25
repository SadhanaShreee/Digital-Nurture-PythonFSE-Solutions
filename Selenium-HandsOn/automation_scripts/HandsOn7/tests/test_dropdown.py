"""
test_dropdown.py

Only assertions here. All Select/dropdown handling logic lives in
pages/dropdown_page.py.
"""

from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + "select-dropdown-demo/")

    page.select_day("Monday")

    assert page.get_selected_day() == "Monday"
