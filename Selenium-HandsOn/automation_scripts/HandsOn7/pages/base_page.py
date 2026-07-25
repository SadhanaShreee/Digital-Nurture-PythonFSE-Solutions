"""
base_page.py

BasePage is the parent class for every Page Object in this suite.
It holds only generic, reusable browser actions that every page needs
(navigating, reading the title, waiting for elements). Page-specific
locators and actions live in the subclasses (SimpleFormPage, CheckboxPage, etc.),
never here.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Load the given URL in the browser."""
        self.driver.get(url)

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        """
        Wait until the element identified by `locator` (a (By, value) tuple)
        is present and visible on the page, then return it.
        Using an explicit wait here (instead of time.sleep) avoids flaky tests.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
