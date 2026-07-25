"""
conftest.py

Shared pytest fixtures for the whole suite. The `driver` fixture opens a
fresh browser before each test and quits it after - so tests stay
independent from one another (no leftover state between tests).
"""

import pytest
from selenium import webdriver

BASE_URL = "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return BASE_URL


# ------------------------------------------------------------------
# Debug helper: on any test failure, save a screenshot + the page's
# HTML at the moment of failure, so we can see what the browser was
# actually showing (cookie banner? redirect? different DOM?) instead
# of guessing blind from a TimeoutException with no visual context.
# ------------------------------------------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            name = item.name
            try:
                drv.save_screenshot(f"FAILURE_{name}.png")
                with open(f"FAILURE_{name}.html", "w", encoding="utf-8") as f:
                    f.write(drv.page_source)
                print(f"\nSaved FAILURE_{name}.png and FAILURE_{name}.html for debugging")
            except Exception as e:
                print(f"\nCould not save failure debug info: {e}")
