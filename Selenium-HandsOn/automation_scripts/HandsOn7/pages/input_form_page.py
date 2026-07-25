"""
input_form_page.py

Page Object for a multi-field form. Originally targeted the "Input Form
Submit" demo on the main Selenium Playground, but that page now redirects
to a Google Sign-In wall and can no longer be reached without valid
credentials (verified manually - the redirect happens even when logged
out, so it isn't a locator bug).

SUBSTITUTED with the "Register Account" form on TestMu AI's separate,
still-public E-commerce Playground demo site:
https://ecommerce-playground.lambdatest.io/index.php?route=account/register

This page has a comparable multi-field form (first name, last name, email,
telephone, password) and is documented/used in TestMu AI's own official
Selenium tutorials, so it's a stable substitute for practicing multi-field
form automation.
"""

import random
import string

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InputFormPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    PHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    PRIVACY_CHECKBOX = (By.XPATH, "//label[@for='input-agree']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")
    # OpenCart's standard post-registration heading text
    SUCCESS_HEADING = (By.XPATH, "//h1[contains(text(), 'Account Has Been Created')]")

    def fill_form(self, first_name, last_name, email, phone, password):
        """Fill every field of the registration form in one call."""
        self.wait_for_element(self.FIRST_NAME_INPUT).send_keys(first_name)
        self.wait_for_element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PHONE_INPUT).send_keys(phone)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.PRIVACY_CHECKBOX).click()

    def submit_form(self):
        """Click the Continue button."""
        self.wait_for_element(self.CONTINUE_BUTTON).click()

    def get_success_message(self):
        """Return the confirmation heading text shown after successful registration."""
        return self.wait_for_element(self.SUCCESS_HEADING).text

    @staticmethod
    def generate_unique_email():
        """
        Build a random, never-before-used email so this test can be re-run
        repeatedly without hitting a 'this email is already registered' error.
        """
        random_part = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return f"selenium.{random_part}@example.com"
