# conftest.py
# Pytest configuration: browser setup and teardown for all tests.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Yield a headless Chrome WebDriver instance.
    The browser is fully torn down after each test to prevent state leakage.
    """
    options = ChromeOptions()
    options.add_argument("--headless=new")       # Run without a display
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    service = ChromeService(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service, options=options)

    # Disable implicit waits — we use explicit waits everywhere
    chrome.implicitly_wait(0)

    yield chrome

    chrome.quit()
