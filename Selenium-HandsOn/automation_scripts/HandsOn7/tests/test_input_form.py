"""
test_input_form.py

Only assertions here. All form-filling logic lives in
pages/input_form_page.py.

NOTE: this test targets the E-commerce Playground registration form
(a separate, still-public TestMu AI demo site) instead of the original
"Input Form Submit" page, which now sits behind a Google Sign-In wall.
See the comment at the top of input_form_page.py for details.
"""

from pages.input_form_page import InputFormPage

ECOMMERCE_REGISTER_URL = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"


def test_input_form_submit(driver):
    page = InputFormPage(driver)
    page.navigate_to(ECOMMERCE_REGISTER_URL)

    page.fill_form(
        first_name="Jane",
        last_name="Doe",
        email=page.generate_unique_email(),
        phone="9876543210",
        password="SeleniumTest123!",
    )
    page.submit_form()

    assert "Account Has Been Created" in page.get_success_message()
