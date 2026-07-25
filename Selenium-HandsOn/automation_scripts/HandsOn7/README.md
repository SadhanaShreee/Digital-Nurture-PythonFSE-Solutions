# Selenium Playground — Page Object Model (POM) Suite

## Folder Structure

```
selenium_pom_project/
├── conftest.py                 # shared pytest fixtures (driver, base_url)
├── pages/
│   ├── base_page.py            # common methods: navigate_to, get_title, wait_for_element
│   ├── simple_form_page.py     # Simple Form Demo page object
│   ├── checkbox_page.py        # Checkbox Demo page object
│   ├── dropdown_page.py        # Dropdown Demo page object
│   └── input_form_page.py      # Input Form Submit page object
└── tests/
    ├── test_simple_form.py
    ├── test_checkbox.py
    ├── test_dropdown.py
    └── test_input_form.py
```

## How to Run

```bash
pip install selenium pytest pytest-html --break-system-packages
pytest tests/ -v --html=report.html
```

`report.html` will show each test with its POM-based, business-readable name
(e.g. `test_simple_form_submission`, `test_input_form_submit`).

## The Golden Rule Followed Here

- **Test files** (`tests/`) contain only **assertions** — what should happen.
- **Page files** (`pages/`) contain only **interactions** — how to make it happen.
- There is **zero `driver.find_element`** in any test file — confirmed with:
  ```bash
  grep -rn "find_element" tests/
  ```

## Note on `test_input_form_submit`

The original target, the "Input Form Submit" demo on the main Selenium
Playground (`lambdatest.com/selenium-playground/input-form-submit/`), now
redirects to a Google Sign-In wall — confirmed by manually visiting it
while logged out. It's no longer reachable without valid credentials, so
this isn't something a locator fix can resolve.

This test was substituted to target TestMu AI's separate, still-public
**E-commerce Playground** registration form instead
(`ecommerce-playground.lambdatest.io/.../account/register`), which has a
comparable multi-field form (first/last name, email, phone, password) and
is documented in TestMu AI's own official Selenium tutorials. The email
used in each run is randomly generated so the test can be re-run
repeatedly without hitting a duplicate-registration error.

## Why POM Matters — The Submit Button ID Example

**The problem in a flat (non-POM) script:**
Imagine 15 test files all directly do:
```python
driver.find_element(By.ID, "submit").click()
```
If the developer renames the button's ID from `submit` to `btn-submit`, **every single one of those 15 test files breaks**, because the old locator no longer matches anything on the page. Someone has to open each test file, find every occurrence of `By.ID, "submit"`, and manually update it in 15 different places. This is slow, error-prone (easy to miss one file), and gets worse as the suite grows.

**How POM solves this:**
With POM, the locator lives in exactly **one place** — as a class-level constant inside the relevant Page Object, e.g.:
```python
SUBMIT_BUTTON = (By.ID, "submit")
```
When the ID changes, you update **this single line, in this single file**. Every test that calls `page.click_submit()` automatically uses the corrected locator the next time it runs — no test file needs to be touched at all. The test files stay stable and readable (`page.click_submit()`), while all HTML/locator details are isolated inside the page classes where they belong. This is the core maintenance benefit of the Page Object Model.
