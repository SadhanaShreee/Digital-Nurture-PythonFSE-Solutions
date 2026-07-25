"""
checkbox_page.py

Page Object for the "Checkbox Demo" page on the Selenium Playground.
Locators are stored as class-level constants; this file only performs
actions and returns state - no assertions here.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    # A list-style locator: each checkbox on the page can be reached by index.
    # NOTE: after TestMu AI's site redesign, guessed IDs (e.g. ex1-check1) no
    # longer match anything, and there are TWO "Option 1-4" checkbox groups on
    # this page (Disabled Checkbox Demo + Multiple Checkbox Demo). Instead of
    # relying on IDs/classes that may change again, this locator finds the 4
    # checkbox <input> elements that immediately follow the visible
    # "Multiple Checkbox Demo" heading text - stable as long as that heading
    # and section order don't change.
    CHECKBOX_OPTIONS = (
        By.XPATH,
        "//*[self::h2 or self::h3 or self::h4][normalize-space()='Multiple Checkbox Demo']"
        "/following::input[@type='checkbox'][position()<=4]"
    )

    def _get_checkbox(self, index):
        """Internal helper: return the checkbox WebElement at the given index."""
        checkboxes = self.driver.find_elements(*self.CHECKBOX_OPTIONS)
        return checkboxes[index]

    def check_option(self, index):
        """Check the checkbox at the given index, if not already checked."""
        checkbox = self._get_checkbox(index)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index):
        """Uncheck the checkbox at the given index, if currently checked."""
        checkbox = self._get_checkbox(index)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index):
        """Return True if the checkbox at the given index is currently checked."""
        checkbox = self._get_checkbox(index)
        return checkbox.is_selected()
