"""
simple_form_page.py

Page Object for the "Simple Form Demo" page on the Selenium Playground.
Holds all locators as class-level constants and all interaction methods.
NOTE: no assert statements live here - this file only performs actions
and returns values. Assertions belong in the test files.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    # ---- Locators (class-level constants; never hardcoded inside methods) ----
    MESSAGE_INPUT = (By.ID, "user-message")
    # The real button text is "Get Checked Value" - locating by visible text
    # is more resilient than guessing a container id (the old "#your-name"
    # guess didn't exist on the redesigned page).
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Get Checked Value']")
    # The real page shows the message directly under a "Your Message:"
    # heading rather than in an element with id="display" (that guess
    # doesn't exist on the redesigned page). Grab the next element after
    # that heading text instead - stable regardless of its actual id/class.
    DISPLAYED_MESSAGE = (
        By.XPATH,
        "//*[normalize-space()='Your Message:']/following::*[normalize-space()!=''][1]"
    )

    def enter_message(self, text):
        """Type the given text into the message input box."""
        message_box = self.wait_for_element(self.MESSAGE_INPUT)
        message_box.clear()
        message_box.send_keys(text)

    def click_submit(self):
        """
        Click the Submit button.
        Uses a JS click as a fallback: the site now runs an auto-launching
        AI chat widget that can visually overlap page content and intercept
        a normal .click(), even though the button itself is present and
        "visible" by CSS rules.
        """
        submit_btn = self.wait_for_element(self.SUBMIT_BUTTON)
        try:
            submit_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", submit_btn)

    def get_displayed_message(self):
        """Return the text shown back to the user after submitting the form."""
        displayed = self.wait_for_element(self.DISPLAYED_MESSAGE)
        return displayed.text

