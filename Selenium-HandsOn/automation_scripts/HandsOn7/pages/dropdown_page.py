"""
dropdown_page.py

Page Object for the "Dropdown Demo" page on the Selenium Playground.
Uses Selenium's Select class internally so test files never have to
know or care that this element is a <select> dropdown.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    DAY_DROPDOWN = (By.ID, "select-demo")

    def select_day(self, day_name):
        """Select a day from the dropdown by its visible text (e.g. 'Monday')."""
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(day_name)

    def get_selected_day(self):
        """Return the currently selected day's visible text."""
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(dropdown_element)
        return select.first_selected_option.text
