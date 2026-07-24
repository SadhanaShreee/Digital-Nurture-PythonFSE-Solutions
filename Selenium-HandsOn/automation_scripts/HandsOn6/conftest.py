import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    """
    Function-scoped fixture: a new browser instance is created for EACH
    test function that requests it. This keeps tests fully isolated -
    one test's leftover state (cookies, page, alerts) can't leak into
    the next test.

    scope='function' (this)  -> new browser per test, slower but safe
    scope='session'          -> one browser reused for the whole run,
                                 faster but tests can interfere with
                                 each other (e.g. leftover form data)
    """
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.maximize_window()

    yield chrome_driver  # -------- setup ends here, test runs --------

    chrome_driver.quit()  # -------- teardown: runs after the test --------


@pytest.fixture(scope='session')
def base_url():
    """Session-scoped: same value reused across all tests, no need to
    recreate it per test since it's just a constant string."""
    return 'https://www.lambdatest.com/selenium-playground/'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Runs after every test phase (setup/call/teardown). We only care
    about the 'call' phase (the actual test body). If it failed and
    the test used the `driver` fixture, save a screenshot named after
    the test for easier debugging.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture is not None:
            test_name = item.name.replace('[', '_').replace(']', '')
            driver_fixture.save_screenshot(f'{test_name}_failure.png')